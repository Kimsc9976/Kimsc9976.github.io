# 반응형 레이아웃 구조

## Breakpoint 정의 (3단계, Mobile First)

| 구간 | 범위 | 용도 |
|------|------|------|
| **Mobile** | 0 ~ 767px | 기본 스타일 (미디어 쿼리 없음) |
| **Tablet** | 768px ~ 1023px | `@media (min-width: 768px)` |
| **Desktop** | 1024px 이상 | `@media (min-width: 1024px)` |

- 모든 기본 규칙은 **모바일 기준**으로 작성하고 `min-width` 로만 단계별로 덮어쓴다.
- `max-width` 쿼리는 쓰지 않는다. 예외: `pages/problem.css` 의 인라인 float 이미지 해제(사유는 파일 주석), Practice 전용 CSS(별도 관리).

---

## 디자인 토큰 (`base.css`)

팔레트: colorhunt `F3EEEA · EBE3D5 · B0A695 · 776B5D`

| 토큰 | 값 | 용도 |
|------|----|------|
| `--c-paper` | `#F3EEEA` | 페이지 바탕 |
| `--c-sand` | `#EBE3D5` | 옅은 채움, hover 배경 |
| `--c-stone` | `#B0A695` | 강한 구분선, 장식 |
| `--c-umber` | `#776B5D` | 포인트, 메타 텍스트 |
| `--c-surface` | `#FBF9F6` | 본문·헤더 면 |
| `--c-ink` / `--c-ink-soft` | `#2B2620` / `#5C5247` | 본문 / 보조 텍스트 |
| `--c-line` | `#E2D9CC` | 기본 구분선 |

새 스타일은 hex 대신 토큰을 쓴다. 미니멀 원칙: 그림자·그라디언트 대신 1px 선, 장식 이모지 대신 작은 모노스페이스 라벨.

---

## 레이아웃 동작

### Header (`_includes/site-header.html`, `chrome.css`)

- 우측 상단: 연락처 링크 `_data/contacts.yml` (아이콘 `_includes/brand-icon.html`)
- 좌측 제목/설명, 우측 UPC-A 바코드 `_includes/barcode.html` (숫자는 `_config.yml` 의 `header_barcode`, 체크 숫자 자동 계산)
- 1024px 미만에서만 목차(☰) 버튼 노출

### Container + Sidebar + Content (`layout.css`)

| 단계 | Container | Sidebar | Content |
|------|-----------|---------|---------|
| Mobile | 세로, 여백 0 | **오프캔버스 드로어** (☰ 로 열기) | 화면 폭 전체 |
| Tablet | 세로, 좌우 20px | 드로어 | 1px 테두리 카드 |
| Desktop | 가로 | `260px` 고정 + 내부 `.sidebar` **sticky** (`top: 20px`, 길면 내부 스크롤) | `flex: 1` |

- 드로어 열림 상태는 `<html class="nav-open">`, 동작은 `assets/js/site.js`
  (닫기 버튼 / 배경 클릭 / ESC / 링크 클릭 / 데스크톱 폭 전환 시 닫힘, 포커스 트랩)
- JS 가 없으면 `head.html` 의 `<noscript>` 가 모바일에서 사이드바를 본문 위에 펼쳐 둔다.

### 블로그 페이지 공통 (`pages/blog.css`, `pages/post.css`)

- `.page-intro`: 라벨 + 제목 + 설명 (Log 허브, 카테고리, Side Project 허브·목록)
- `.log-cards` / `.log-card`: 번호가 붙은 인덱스 카드. 모바일 1열 → 768px 이상 3열
- `.post-list` / `.post-item`: 제목 + 날짜. 모바일은 날짜가 아래 → 480px 이상 한 줄
- `.post`, `.sideproject-post`: 본문 최대 760px 가운데 정렬

---

### Home · About 공통 — container query

Home 과 About 은 viewport 대신 **본문 폭**으로 열 수를 정한다 (데스크톱은 사이트 사이드바 때문에 태블릿보다 본문이 좁을 수 있음).
같은 디자인 문법을 쓰도록 공통 블록은 `components.css` 에 둔다.

- `.section-head` — 번호 + 제목 (+ 오른쪽 더보기 링크), 위에 진한 1px 선
- `.career-col` / `.career-list` / `.career-item` — 연도·기간(모노 작은 줄) → 제목 → 설명
- 글 목록은 Log 와 같은 `.post-list` (`pages/blog.css`)
- 아이콘은 이모지 대신 `_includes/pictogram.html` (단색 선 SVG, `currentColor`)
- 카드: 1px `--c-line` 테두리 + 8px 둥글기, 그림자 없음

#### Home (`pages/home.css`, `chartss.css`)

| 컨테이너 | 폭 | 변화 |
|----------|----|------|
| `home` (.home-page) | 600px+ | 프로필 \| 방문자 그래프 2열 (그래프가 프로필 높이만큼 늘어남) |
| `home` | 880px+ | 본문 \| 오른쪽 260px 프로필 열 (sticky, 그래프 220px) |
| `home-left` | 480 / 560px+ | 숫자 칸 여백 확대 / 타임라인: 경력 \| Side Projects 2열 |
| `home-left` | 680px+ | Recent Algorithms \| Latest Log Posts 2열 |

- 방문자 그래프 색은 `visitor-charts.html` 이 `base.css` 토큰을 읽어 쓴다
- GitHub 활동 그래프는 URL 파라미터로 팔레트 색 지정 (`bg_color`, `line`, `area_color` …)

#### About (`pages/about.css`)

| 컨테이너 | 폭 | 변화 |
|----------|----|------|
| `about` (.about-page) | 880px+ | 목차: 위쪽 sticky 가로 탭 → 왼쪽 세로 목차 + 본문 세로선 |
| `about-main` | 520 / 600px+ | Skills 2열 / Brief 사진·글 2열, Practices 슬라이드당 2×2 |
| `about-main` | 560 / 780px+ | Career: 경력 한 줄 + 자격증·대회 2열 → 3열 |
| `about-text` | 520px+ | 경험 카드 2열, 인용문의 `<br>` 표시 |

- 카드 캐러셀(`.card-carousel`, Projects·Practices 공통): 인디케이터·이전/다음 버튼을 카드 아래 한 줄(`.carousel-nav`)로 배치 (모바일·PC 동일, 간격 14px)
  - 슬라이드당 카드 수는 CSS `--per-page` 가 정하고 `about.html` 스크립트가 그 값으로 슬라이드를 다시 묶는다 (Practices: 모바일 1장 → 넓으면 4장)
- Career 데이터: `_data/timeline.yml` 의 `label` / `pictogram` (Home 타임라인은 경력 섹션만 사용)

---

## 파일 역할

- **base.css**: 토큰, body 기본값, 포커스/선택/skip-link
- **layout.css**: 반응형 구조 전담. breakpoint, container/sidebar/content, 그리드 열 수
- **chrome.css**: 헤더·본문 면·푸터의 모양
- **sidebar.css**: 사이드바 모양만 (위치/너비/드로어 동작은 layout.css)
- **components.css**: 여러 페이지가 함께 쓰는 블록 (`.section-head`, `.career-*` 등)
- **pages/*.css**: 페이지별 모양

## 호환용으로 남겨둔 규칙 (Practice·Side Project 화면 유지)

- `layout.css` 의 `.practice-detail header` — 예전 전역 `header {}` 규칙(어두운 바)을 Practice 상세 헤더가 전제로 함
- `pages/blog.css` 하단 LEGACY — Side Project(trade 등) 목록이 쓰는 `.post-date` 기본값
- `layout.css` 의 GRID 블록은 그대로 유지 (Home·About 은 각 `pages/*.css` 로 이전)
