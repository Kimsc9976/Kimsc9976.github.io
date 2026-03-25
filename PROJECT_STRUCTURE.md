# 프로젝트 파일 구조

> 프롬프트/문서용 참고. `modules/` 및 algorithm 관련 경로는 서브모듈이므로 내부 구조는 나열하지 않음.

```
Kimsc9976.github.io/
├── _config.yml              # Jekyll 사이트 설정
├── Gemfile
├── Gemfile.lock
├── .gitignore
├── .gitmodules              # 서브모듈 정의 (modules/Algorithm)
├── SETUP_INSTRUCTIONS.md
│
├── index.md                 # 루트/홈 페이지
├── about.md                 # 소개 페이지
├── blog.md                  # 블로그 진입점
│
├── _data/                   # Jekyll 데이터
│   ├── sidebar_structure.yml
│   ├── sidebar.yml
│   └── urls.yml
│
├── _includes/               # 재사용 HTML 조각
│   ├── tier.html
│   ├── problem.html
│   └── sidebar.html
│
├── _layouts/                # 레이아웃 템플릿
│   ├── default.html
│   ├── home.html
│   ├── about.html
│   ├── post.html
│   ├── platform.html
│   ├── tier.html
│   ├── problem.html
│   ├── category.html
│   ├── blog-category.html
│   ├── sideproject.html
│   └── sideproject-list.html
│
├── _posts/                  # 블로그 포스트 (날짜-슬러그.md)
│   ├── 2026-02-03-test-file-dev.md
│   ├── 2026-02-03-test-file-note.md
│   └── 2026-02-03-test-file-qa.md
│
├── blog/                    # 블로그 카테고리별 index
│   ├── dev/
│   │   └── index.md
│   ├── note/
│   │   └── index.md
│   └── qa/
│       └── index.md
│
├── sideproject/             # 사이드 프로젝트 페이지
│   ├── anyo/
│   │   └── index.md
│   ├── blog/
│   │   └── index.md
│   └── trade/
│       └── index.md
│
├── assets/
│   ├── css/
│   │   ├── base.css
│   │   ├── components.css
│   │   ├── layout.css
│   │   ├── sidebar.css
│   │   ├── style.css
│   │   └── pages/
│   │       ├── about.css
│   │       ├── blog.css
│   │       ├── home.css
│   │       ├── platform.css
│   │       ├── post.css
│   │       ├── problem.css
│   │       └── tier.css
│   └── images/
│       ├── c_programming.svg
│       ├── git.png
│       ├── profile1.jpg
│       ├── profile2.jpg
│       ├── qa.png
│       └── qtcreator.jpg
│
├── scripts/                 # 빌드/생성 스크립트 (Ruby)
│   ├── _data/
│   │   └── sidebar_structure.yml
│   ├── generate_algo_level.rb
│   ├── generate_problem.rb
│   ├── generate_sidebar.rb
│   └── generate_tier.rb
│
├── .github/
│   └── workflows/
│       ├── jekyll.yml
│       ├── trigger-main-repo.yml.example
│       └── update-submodule.yml
│
└── modules/                 # [서브모듈] 내부 구조 미나열
    └── Algorithm/           # study_algorithm 서브모듈
```

---

## 프로젝트 구조 및 역할

### 사이트 종류

- **Jekyll 기반 정적 사이트** (GitHub Pages 배포)
- **주제**: QA·자동화·엔지니어링 블로그 + 알고리즘 풀이 정리 + 사이드 프로젝트

### 디렉터리별 역할

| 경로 | 역할 |
|------|------|
| `_config.yml` | Jekyll 전역 설정. `collections`(algorithm, blog, sideprojects), permalink, exclude 등. |
| `_data/` | 사이트 전역 데이터. `sidebar.yml`(사이드바 메뉴, 스크립트로 생성), `sidebar_structure.yml`, `urls.yml`. |
| `_includes/` | 반복 사용 HTML 조각. `sidebar.html`(네비게이션), `tier.html`, `problem.html`. |
| `_layouts/` | 페이지 레이아웃. `default.html`(공통 헤더·사이드바·푸터), post/blog/tier/problem 등 페이지별 레이아웃. |
| `_posts/` | 블로그 포스트. 파일명 `YYYY-MM-DD-슬러그.md`, front matter에 `layout: post`, `categories` 등. |
| `blog/` | 블로그 카테고리(dev, qa, note)별 `index.md`. |
| `sideproject/` | 사이드 프로젝트별 페이지(anyo, blog, trade 등). |
| `assets/` | CSS, 이미지. `style.css`가 메인, `pages/`는 페이지별 스타일. |
| `scripts/` | **빌드 전 실행 스크립트(Ruby)**. `modules/Algorithm` 서브모듈을 읽어 `_algorithm/`, `_data/sidebar.yml` 생성. |
| `modules/` | **서브모듈** `Algorithm`(study_algorithm). 소스만 참조하고, Jekyll 빌드에는 제외(`exclude`)됨. |

### 콜렉션과 생성 디렉터리

- **algorithm**: 콜렉션 소스는 `_algorithm/`(스크립트로 생성). URL 예: `/algorithm/`, `/algorithm/백준/Bronze/`, `/algorithm/백준/Bronze/문제명/`.
- **blog**: `blog/` 하위 + `_posts/` 조합.
- **sideprojects**: `sideproject/` 하위.

---

## 작업 및 동작 방식

### 1. 알고리즘 페이지 생성 파이프라인 (Ruby 스크립트)

**입력**: 서브모듈 `modules/Algorithm` 디렉터리 구조  
**출력**: `_algorithm/` 마크다운·HTML 조각, `_data/sidebar.yml`

| 스크립트 | 실행 순서 | 하는 일 |
|----------|-----------|---------|
| `generate_algorithm.rb` | 1 | `_algorithm/index.md` 생성. 플랫폼(백준, 프로그래머스 등) 목록·티어·최근 문제 링크. 레이아웃 `algorithm`. |
| `generate_algo_level.rb` | 2 | 플랫폼별 한 페이지. `_algorithm/<platform>/index.md`. 해당 플랫폼의 모든 티어 문제를 20개 단위 섹션으로 링크, 레이아웃 `platform`. |
| `generate_tier.rb` | 3 | 티어별 문제 목록 페이지. `_algorithm/<platform>/<tier>/index.md`. 해당 티어 문제만 20개 단위 섹션, 레이아웃 `tier`. |
| `generate_problem.rb` | 4 | 문제별 상세 페이지. `_algorithm/<platform>/<tier>/<문제명>/index.md`. README.md + 코드 블록(.py, .cc, .java 등), 레이아웃 `problem`. |
| `generate_sidebar.rb` | 5 | `modules/Algorithm` 디렉터리 구조를 읽어 `_data/sidebar.yml`의 `algorithm` 키 갱신. 사이드바 "Algorithm List" 메뉴에 사용. |

- 경로/URL은 한글·특수문자 대비해 `safe_path`, `safe_url_path` 등으로 정규화·URL 인코딩 후 사용.
- `_algorithm/`은 `.gitignore` 대상이며, CI에서 매 빌드마다 위 스크립트로 다시 생성.

### 2. Jekyll 빌드

- 스크립트 실행 **이후** `bundle exec jekyll build` 실행.
- `_config.yml`의 `collections.algorithm`이 `_algorithm/`을 콜렉션으로 사용해 `/algorithm/...` 페이지 생성.
- `modules`는 `exclude`에 들어가 있어 빌드 시 포함되지 않음.

### 3. GitHub Actions 워크플로우

| 워크플로우 | 파일 | 트리거 | 하는 일 |
|------------|------|--------|---------|
| **Update Submodule** | `update-submodule.yml` | `schedule`(매일 UTC 00:00), `workflow_dispatch`, `repository_dispatch`(submodule-updated) | `modules/Algorithm`을 원격 최신으로 갱신. 필요 시 커밋 후 `main`에 푸시. |
| **Deploy Jekyll** | `jekyll.yml` | `workflow_run`(Update Submodule 완료 후), `push`(main), `schedule`(매일), `workflow_dispatch` | 서브모듈 포함 체크아웃 → 5개 Ruby 스크립트 순서 실행 → Jekyll 빌드 → GitHub Pages 배포. |

- 서브모듈 레포(study_algorithm)에서 push 시 `repository_dispatch`로 메인 레포를 호출할 수 있음(설정은 `SETUP_INSTRUCTIONS.md` 참고).
- `trigger-main-repo.yml.example`: 서브모듈 쪽에서 사용할 워크플로 예시(이 레포에는 `.example`만 있고, 실제 트리거는 서브모듈 레포에 설정).

### 4. 사이드바 데이터 흐름

- **수동/고정**: `_data/sidebar.yml`의 `main`, `blog`, `sideprojects`는 직접 편집.
- **자동**: `algorithm` 키는 `generate_sidebar.rb`가 `modules/Algorithm` 디렉터리(플랫폼/티어)를 스캔해 덮어씀.
- `_includes/sidebar.html`이 `site.data.sidebar`를 참조해 좌측 네비게이션 렌더링.

### 5. 로컬에서 할 때

1. 서브모듈 있음: `git submodule update --init --recursive`
2. 알고리즘 페이지까지 보려면: `ruby scripts/generate_algorithm.rb` 등 5개 스크립트 순서 실행 후 `bundle exec jekyll build` (또는 `serve`).
3. 블로그·사이드프로젝트만 수정할 때는 스크립트 없이 Jekyll만 실행해도 됨.

---

## 비고

- **빌드 산출물**: `_site/`, `.jekyll-cache/` 는 생성 디렉터리로 무시. `_algorithm/` 도 스크립트 생성물이라 버전 관리 제외.
- **서브모듈**: `modules/` 및 그 안의 Algorithm 경로는 서브모듈이므로 이 문서에서는 파일 트리를 펼치지 않음.
