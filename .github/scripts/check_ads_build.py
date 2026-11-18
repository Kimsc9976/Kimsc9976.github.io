#!/usr/bin/env python3
"""Verify rendered Jekyll ad loader rules. Runs only on CI build outputs."""
from pathlib import Path
from html.parser import HTMLParser
import re
import sys

if len(sys.argv) != 2 or sys.argv[1] not in {"prod_config", "prod_test", "prod_empty", "dev_test"}:
    raise SystemExit("Usage: check_ads_build.py {prod_config|prod_test|prod_empty|dev_test}")

mode = sys.argv[1]
site = Path("_site")
home = site / "index.html"
about = site / "about" / "index.html"
practice = sorted((site / "practice").rglob("index.html"))
posts = sorted((site / "log").rglob("index.html"))

assert home.is_file(), "Home page missing"
assert about.is_file(), "About page missing"
assert len(practice) >= 7, f"Expected seven practice pages, found {len(practice)}"
assert posts, "No blog posts were generated"
assert not (site / "room" / "index.html").exists(), "Deferred room was accidentally published"

def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")

def has_ad(path: Path) -> bool:
    return "adsbygoogle.js" in read(path)

def has_ga(path: Path) -> bool:
    return "googletagmanager.com/gtag/js" in read(path)

class AdScripts(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_head = False
        self.scripts = []

    def handle_starttag(self, tag, attrs):
        if tag == "head":
            self.in_head = True
        if tag == "script" and "adsbygoogle.js" in dict(attrs).get("src", ""):
            self.scripts.append((self.in_head, dict(attrs)))

    def handle_endtag(self, tag):
        if tag == "head":
            self.in_head = False

included = [home, *posts]
excluded = [about, *practice]

configured = re.findall(r'^  client: "([^"]*)"$', read(Path("_config.yml")), re.M)
assert len(configured) == 1, "Expected one configured publisher ID"
assert not configured[0] or re.fullmatch(r"ca-pub-\d{16}", configured[0]), "Invalid publisher ID"
client = configured[0] if mode == "prod_config" else "ca-pub-0000000000000000"
expected_ads_txt = "" if mode == "prod_empty" or not client else f"google.com, {client.removeprefix('ca-')}, DIRECT, f08c47fec0942fa0"
assert read(site / "ads.txt").strip() == expected_ads_txt, "ads.txt publisher mismatch"
assert "/ads.txt</loc>" not in read(site / "sitemap.xml"), "ads.txt must stay out of the sitemap"

if mode in {"prod_config", "prod_test"} and client:
    for path in included:
        parser = AdScripts()
        parser.feed(read(path))
        assert len(parser.scripts) == 1, f"Expected exactly one AdSense loader on {path}"
        in_head, attrs = parser.scripts[0]
        assert in_head, f"AdSense must be inside head on {path}"
        assert attrs.get("src") == f"https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={client}", f"Wrong AdSense URL on {path}"
        assert "async" in attrs and attrs.get("crossorigin") == "anonymous", f"Wrong script attributes on {path}"
    for path in excluded:
        assert not has_ad(path), f"AdSense should be excluded from {path}"
        assert has_ga(path), f"GA should stay enabled on {path}"
elif mode in {"prod_empty", "prod_config"}:
    for path in included + excluded:
        assert not has_ad(path), f"AdSense must stay off without a client: {path}"
    for path in excluded:
        assert has_ga(path), f"GA should stay enabled in production on {path}"
else:
    for path in included + excluded:
        assert not has_ad(path), f"AdSense must stay off in development: {path}"
        assert not has_ga(path), f"GA should be disabled in development on {path}"

print(f"PASS: {mode}; {len(practice)} practice pages, {len(posts)} post pages")
