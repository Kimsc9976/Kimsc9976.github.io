(function () {
  const root = document.getElementById("problem-search");
  if (!root) return;

  const input = document.getElementById("problem-search-input");
  const resultsEl = document.getElementById("problem-search-results");
  const indexUrl = root.dataset.indexUrl;

  if (!input || !resultsEl || !indexUrl) return;

  const MAX_RESULTS = 10;
  let index = [];
  let activeIndex = -1;
  let loaded = false;

  function normalize(value) {
    return (value || "")
      .toString()
      .normalize("NFC")
      .toLowerCase()
      .replace(/\s+/g, " ")
      .trim();
  }

  function scoreItem(item, query) {
    const q = normalize(query);
    if (!q) return 0;

    const titleClean = normalize(item.title_clean);
    const title = normalize(item.title);
    const problemId = (item.problem_id || "").toString();

    if (problemId === q) return 100;
    if (titleClean === q || title === q) return 95;
    if (problemId.startsWith(q)) return 85;
    if (titleClean.startsWith(q)) return 75;
    if (title.startsWith(q)) return 70;
    if (problemId.includes(q)) return 60;
    if (titleClean.includes(q)) return 55;
    if (title.includes(q)) return 50;

    return 0;
  }

  function search(query) {
    return index
      .map((item) => ({ item, score: scoreItem(item, query) }))
      .filter((entry) => entry.score > 0)
      .sort((a, b) => {
        if (b.score !== a.score) return b.score - a.score;
        return a.item.title.localeCompare(b.item.title, "ko");
      })
      .slice(0, MAX_RESULTS)
      .map((entry) => entry.item);
  }

  function hideResults() {
    resultsEl.hidden = true;
    resultsEl.innerHTML = "";
    activeIndex = -1;
    input.setAttribute("aria-expanded", "false");
  }

  function renderResults(matches) {
    if (!matches.length) {
      resultsEl.innerHTML = '<li class="problem-search-empty">검색 결과가 없습니다.</li>';
      resultsEl.hidden = false;
      activeIndex = -1;
      return;
    }

    resultsEl.innerHTML = matches
      .map((item, idx) => {
        const badge = `${item.platform} · ${item.tier}`;
        return `
          <li>
            <a
              href="${item.url}"
              class="problem-search-item${idx === activeIndex ? " is-active" : ""}"
              data-index="${idx}"
              role="option"
              aria-selected="${idx === activeIndex}"
            >
              <span class="problem-search-badge">${badge}</span>
              <span class="problem-search-title">${item.title}</span>
            </a>
          </li>
        `;
      })
      .join("");

    resultsEl.hidden = false;
    input.setAttribute("aria-expanded", "true");
  }

  function updateResults() {
    const query = input.value.trim();
    if (!query) {
      hideResults();
      return;
    }

    renderResults(search(query));
  }

  function setActive(index) {
    const links = resultsEl.querySelectorAll(".problem-search-item");
    if (!links.length) return;

    activeIndex = Math.max(0, Math.min(index, links.length - 1));
    links.forEach((link, idx) => {
      link.classList.toggle("is-active", idx === activeIndex);
      link.setAttribute("aria-selected", idx === activeIndex ? "true" : "false");
    });
    links[activeIndex].scrollIntoView({ block: "nearest" });
  }

  function followActiveLink() {
    const active = resultsEl.querySelector(".problem-search-item.is-active");
    if (active) {
      window.location.href = active.getAttribute("href");
    }
  }

  async function loadIndex() {
    if (loaded) return;

    try {
      const response = await fetch(indexUrl);
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      index = await response.json();
      loaded = true;
    } catch (error) {
      console.error("Problem search index load failed:", error);
      resultsEl.innerHTML = '<li class="problem-search-empty">검색 인덱스를 불러오지 못했습니다.</li>';
      resultsEl.hidden = false;
    }
  }

  input.addEventListener("input", async () => {
    await loadIndex();
    updateResults();
  });

  input.addEventListener("focus", async () => {
    await loadIndex();
    if (input.value.trim()) updateResults();
  });

  input.addEventListener("keydown", async (event) => {
    await loadIndex();

    const links = resultsEl.querySelectorAll(".problem-search-item");
    if (!links.length) return;

    if (event.key === "ArrowDown") {
      event.preventDefault();
      setActive(activeIndex + 1);
    } else if (event.key === "ArrowUp") {
      event.preventDefault();
      setActive(activeIndex <= 0 ? links.length - 1 : activeIndex - 1);
    } else if (event.key === "Enter") {
      if (activeIndex >= 0) {
        event.preventDefault();
        followActiveLink();
      }
    } else if (event.key === "Escape") {
      hideResults();
      input.blur();
    }
  });

  document.addEventListener("click", (event) => {
    if (!root.contains(event.target)) hideResults();
  });
})();
