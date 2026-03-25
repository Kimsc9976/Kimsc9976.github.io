# 반응형 레이아웃 구조

## Breakpoint 정의 (3단계)

| 구간 | 범위 | 용도 |
|------|------|------|
| **Mobile** | 0 ~ 767px | 기본 스타일 (미디어 쿼리 없음) |
| **Tablet/Laptop** | 768px ~ 1023px | `@media (min-width: 768px)` |
| **Desktop** | 1024px 이상 | `@media (min-width: 1024px)` |

- **Mobile First**: 모든 기본 규칙을 모바일 기준으로 작성하고, `min-width`로 단계별로 덮어씀.
- 중복 제거: 반응형은 `layout.css` 한 곳에서만 제어해 우선순위 꼬임을 방지.

---

## 레이아웃 동작

### Container + Sidebar + Content

| 단계 | Container | Sidebar | Content |
|------|------------|---------|---------|
| Mobile | `flex-direction: column` | `width: 100%`, 상단(`order: -1`) | 아래 배치 |
| Tablet | `flex-direction: row` | `width: 30%`, `margin-right: 20px` | `flex: 1` |
| Desktop | 동일 | `width: 260px` 고정 | `flex: 1` (나머지 공간) |

### 그리드·카드

- **cards-container / card**: 모바일 1열 → 태블릿 2열 → 데스크탑 3열.
- **home-main**: 모바일 1열 → 768px 이상에서 좌측 컨텐츠 + 우측 280px(프로필).
- **home-grid, preview-grid**: 모바일 1열 → 태블릿 이상 2열(또는 행 고정).
- **blog-categories**: 1열 → 2열(768px) → 3열(1024px).
- **problem-grid**: 1열 → 768px 이상 2열.
- **post-container**: 모바일 세로 스택 → 768px 이상 좌(본문 3) / 우(사이드 1).
- **about-layout, about-grid, skill-grid**: 동일하게 모바일 1열 후 단계별 열 수 증가.

---

## 파일 역할

- **layout.css**: 반응형 구조 전담. breakpoint, container/sidebar/content, 그리드·카드 열 수.
- **sidebar.css**: 사이드바 시각 스타일만(패딩, 배경, 링크 스타일). 너비/여백은 layout.css.
- **components.css**: `.card` 박스 스타일만. 너비/미디어는 layout.css로 이전됨.
- **pages/*.css**: 페이지별 시각 스타일. 레이아웃 관련 미디어 쿼리는 layout.css에만 두고, 여기서는 제거 권장.

---

## 왜 이렇게 나눴는지

1. **한 곳에서 breakpoint 관리**: 768px/1024px를 layout.css의 `:root`와 `min-width`로만 사용해, 나중에 구간 변경 시 한 파일만 수정하면 됨.
2. **Mobile First**: 작은 화면을 기본으로 두면 미디어 쿼리가 “확장”만 하게 되어, 불필요한 덮어쓰기가 줄어듦.
3. **우선순위 정리**: 레이아웃(너비, flex, grid 열 수)을 layout.css에서만 정의하고, sidebar/components/pages는 “모양”만 담당해 충돌을 줄임.
4. **유지보수**: 새 페이지나 새 그리드 추가 시 layout.css 한 블록만 추가하면 됨.
