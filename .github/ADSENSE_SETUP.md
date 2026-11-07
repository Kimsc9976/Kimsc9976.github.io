# AdSense 연결

게시자 ID는 `_config.yml`의 `adsense.client` 한 곳에서 관리합니다.
공통 `<head>`의 `ads.html`이 production 빌드에서 제공받은 스크립트를 생성합니다.
`ads.txt`도 같은 ID로 생성됩니다. 게시자 ID는 공개 HTML에 포함되는 식별자입니다.

## 배포 후 콘솔 작업

1. 이 브랜치를 PR로 검토한 뒤 `main`에 병합하고 GitHub Pages 배포 완료를 확인합니다.
2. 홈페이지 소스에서 `ca-pub-7835493657278522`가 포함된 AdSense 스크립트가 `<head>` 안에 한 번만 있는지 확인합니다.
3. `https://kimsc9976.github.io/ads.txt`에 `google.com, pub-7835493657278522, DIRECT, f08c47fec0942fa0`이 표시되는지 확인합니다.
4. AdSense에서 `https://kimsc9976.github.io`의 확인 방법을 **AdSense 코드 스니펫**으로 선택하고 연결 확인 후 **검토 요청**을 누릅니다. 저장소 설정만으로 검토가 신청되지는 않습니다.
5. 자동 광고 설정의 페이지 제외에도 `/about/`은 이 페이지, `/practice/`와 `/room/`은 해당 섹션 전체로 등록합니다.

사이트 승인은 Google의 별도 절차이며, 코드 배포가 승인 완료를 의미하지 않습니다.

## 광고 제외 및 비밀방

- `/about/`, `/practice/`, `/room/`과 `ads: false` 페이지는 광고 로더를 생성하지 않습니다. 개발 빌드에서도 생성하지 않습니다.
- About과 Practice의 기존 production GA는 유지됩니다. `/room`, `/room/*` 또는 `analytics: false` 페이지에서는 GA가 생성되지 않습니다.
- 비밀방 자체와 암호화 기능은 이 변경에 포함되지 않습니다. 향후 구현 시 `layout: null`, `ads: false`, `analytics: false`, `sitemap: false`, `noindex`를 적용하고 평문 유출 검사를 별도로 수행해야 합니다.
- 광고를 끄려면 `adsense.client`를 빈 문자열로 바꿉니다. 그러면 광고 스크립트와 ads.txt 판매자 행이 생성되지 않습니다.

## 검증

`.github/workflows/ads-only-check.yml`은 실제 Jekyll 산출물에 대해 설정된 ID, 임시 테스트 ID, 빈 ID, 개발 모드를 확인합니다.
임시 YAML 설정을 덮어 읽으며 추적 중인 `_config.yml`은 변경하지 않습니다.
검증기는 홈·전체 게시글의 스크립트 위치/중복/속성과 About·Practice의 광고 제외, GA 유지, ads.txt, 사이트맵 제외를 확인합니다.

공식 안내: [사이트 연결](https://support.google.com/adsense/answer/7584263?hl=ko), [ads.txt](https://support.google.com/adsense/answer/12171612?hl=ko)
