# trade_report → 블로그 일간 레포트 동기화 설정

`modules/Algorithm` 서브모듈(`update-submodule.yml`)과 **완전히 분리**된 파이프라인입니다.

| 항목 | Algorithm 서브모듈 | trade_report |
|------|---------------------|--------------|
| 메인 워크플로 | `update-submodule.yml` | `sync-trade-daily-report.yml` |
| 트리거 예시 | `trigger-main-repo.yml.example` | `trigger-main-repo-trade-report.yml.example` |
| `repository_dispatch` | `submodule-updated` | `trade-report-updated` |

## 동작 요약

1. `trade_report`의 `daily-report/YYYY/MM/DD/morning.md`, `afternoon.md` 생성·push
2. (선택) `trade_report` Actions → 메인 레포 `repository_dispatch`
3. 메인 레포 `sync-trade-daily-report.yml` → `modules/trade_report` 서브모듈 갱신 → 동기화 스크립트 실행
4. `sideproject/trade/daily-report/` (am/pm) + `sideproject/trade/journal/` (1일 1건) + 차트 PNG 커밋 (`[skip ga]`)

## 서브모듈 초기화 (로컬)

```bash
git submodule update --init modules/trade_report
# 또는 전체
git submodule update --init --recursive
```

cron만 켜 두어도 동작합니다 (UTC 04:05, 09:05, 13:05).

## 1단계: Personal Access Token

Algorithm 서브모듈과 **동일한 classic PAT**(`repo` scope)를 재사용할 수 있습니다.  
없다면 `SETUP_INSTRUCTIONS.md` 1단계와 동일하게 생성합니다.

## 2단계: trade_report 레포에 시크릿

1. https://github.com/Kimsc9976/trade_report → **Settings** → **Secrets and variables** → **Actions**
2. **New repository secret**
   - **Name**: `MAIN_REPO_TOKEN`
   - **Secret**: PAT

## 3단계: trade_report에 트리거 워크플로 배치

메인 레포의 예시 파일을 복사합니다.

- 원본: `.github/workflows/trigger-main-repo-trade-report.yml.example`
- 대상: `trade_report` 레포의 `.github/workflows/trigger-main-repo.yml`

⚠️ 파일명에서 `.example` 을 제거해야 Actions가 실행됩니다.

`daily-report/**` 경로에 변경이 있을 때만 push 트리거됩니다.

## 4단계: 로컬 수동 동기화 (선택)

```bash
cd /path/to/Kimsc9976.github.io
git submodule update --remote modules/trade_report

ruby scripts/sync_trade_daily_report.rb --since 2026-05-25
ruby scripts/sync_trade_journal.rb --since 2026-05-25
# 기본 소스: modules/trade_report
```

### journal 소스 형식 (MVP)

| trade_report | 블로그 |
|---|---|
| `journal/YYYY/MM/DD/journal.md` | `sideproject/trade/journal/YYYY-MM-DD.md` (1일 1건) |
| `journal/YYYY/MM/DD/morning.md` + `afternoon.md` | 오전/오후 섹션으로 병합 |
| `journal/YYYY/MM/DD/chart.png` | `assets/images/trade/journal/YYYY-MM-DD-chart.png` |

`--dry-run` 으로 변경 파일만 확인할 수 있습니다.

## 문제 해결

### 메인 레포 워크플로가 안 돌아갈 때

- `trade_report`에 `trigger-main-repo.yml` 이 있는지, `event-type` 이 `trade-report-updated` 인지 확인
- `MAIN_REPO_TOKEN` 시크릿 이름·권한 확인

### submodule 워크플로와 혼동

- `update-submodule.yml`, `trigger-main-repo.yml.example` 은 **수정하지 마세요**
- trade_report 전용 파일만 사용하세요

### 동기화 후에도 cron이 매번 돌 때

- `_data/trade_report_sync.yml` 의 `last_synced_sha` 가 커밋에 포함됐는지 확인
