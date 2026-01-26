# 서브모듈 트리거 설정 가이드

## 1단계: GitHub Personal Access Token 생성

1. GitHub에 로그인 후, 우측 상단 프로필 클릭 → **Settings**
2. 왼쪽 사이드바에서 **Developer settings** 클릭
3. **Personal access tokens** → **Tokens (classic)** 클릭
4. **Generate new token** → **Generate new token (classic)** 클릭
5. 다음 설정:
   - **Note**: `Main Repo Trigger Token` (설명)
   - **Expiration**: 원하는 만료 기간 선택
   - **Scopes**: 다음 권한 체크
     - ✅ `repo` (전체 권한) - 메인 레포지토리에 접근하기 위해 필요
6. **Generate token** 클릭
7. ⚠️ **중요**: 생성된 토큰을 복사해 안전한 곳에 보관 (다시 볼 수 없음)

## 2단계: 서브모듈 레포지토리에 시크릿 추가

1. 서브모듈 레포지토리(`study_algorithm`)로 이동
2. **Settings** → **Secrets and variables** → **Actions** 클릭
3. **New repository secret** 클릭
4. 다음 입력:
   - **Name**: `MAIN_REPO_TOKEN`
   - **Secret**: 1단계에서 생성한 토큰 붙여넣기
5. **Add secret** 클릭

## 3단계: 워크플로우 파일 확인

서브모듈 레포지토리의 `.github/workflows/trigger-main-repo.yml` 파일이 다음 내용인지 확인:

```yaml
name: Trigger Main Repository Update

on:
  push:
    branches: [main, master]

permissions:
  contents: read

jobs:
  trigger:
    runs-on: ubuntu-latest
    steps:
      - name: Trigger main repository workflow
        uses: peter-evans/repository-dispatch@v3
        with:
          token: ${{ secrets.MAIN_REPO_TOKEN }}
          repository: Kimsc9976/Kimsc9976.github.io
          event-type: submodule-updated
          client-payload: |
            {
              "submodule": "Algorithm",
              "commit": "${{ github.sha }}",
              "ref": "${{ github.ref }}"
            }
```

⚠️ **중요**: 파일명이 `trigger-main-repo.yml.example`이 아닌 `trigger-main-repo.yml`이어야 합니다!

## 4단계: 테스트

1. 서브모듈 레포지토리에 변경사항을 푸시
2. 서브모듈 레포지토리의 **Actions** 탭에서 워크플로우 실행 확인
3. 메인 레포지토리(`Kimsc9976.github.io`)의 **Actions** 탭에서 `Deploy Jekyll site to Pages` 워크플로우가 자동으로 트리거되는지 확인

## 문제 해결

### 워크플로우가 실행되지 않는 경우
- 파일명이 `.yml`인지 확인 (`.example` 제거)
- 파일이 `.github/workflows/` 폴더에 있는지 확인
- `main` 또는 `master` 브랜치에 푸시했는지 확인

### 토큰 오류가 발생하는 경우
- 토큰에 `repo` 권한이 있는지 확인
- 시크릿 이름이 정확히 `MAIN_REPO_TOKEN`인지 확인
- 토큰이 만료되지 않았는지 확인

### 메인 레포지토리 워크플로우가 트리거되지 않는 경우
- 메인 레포지토리의 `jekyll.yml`에 `repository_dispatch` 트리거가 있는지 확인
- `event-type`이 `submodule-updated`로 일치하는지 확인

