---
layout: practice
title: "데이터 시각화 도구 구축"
permalink: /practice/qa-visualization-tools/
eyebrow: QA Engineering Practice / 뉴빌리티
headline: 로봇 로그부터 인지(Perception) 결과까지 — QA·개발·운영이 같은 화면, 같은 기준으로 판단하게 만드는 도구
role: 도구 기획·설계·개발 및 운영
tech: [Python, ROS2, PyQt5, FastAPI, React, TypeScript, three.js]
# cover:                      # 대표 이미지 (이미지 업로드 후 주석 해제)
#   src: /assets/images/practice/visualization/ss-tool-overview.png
#   alt: SS 검증 도구 전체 화면
#   caption: 카메라·SS·LDM 동기화 뷰어와 검증 패널
# highlights:                 # 핵심 수치 (확정된 수치가 있으면 채워주세요)
#   - value: ""
#     label: ""
# resources:
#   - title: 관련 블로그 글
#     url: /log/...
---

<!--
  이미지 업로드 위치: /assets/images/practice/visualization/
  아래 <figure> 주석을 풀면 해당 위치에 표시됩니다. (파일명은 자유롭게 바꿔도 됩니다)
-->

## 배경과 문제

자율주행 로봇의 이슈는 대부분 **"로봇이 그 순간 무엇을 보고, 어떤 상태였는가"**를 알아야 원인을 좁힐 수 있습니다.
하지만 그 정보는 ROS2 토픽의 Raw 메시지와 숫자 코드로만 남아 있어서, 같은 로그를 두고도 QA·개발·운영이 서로 다르게 해석하는 일이 잦았습니다.

- **로깅 단계** — 상태 코드(예: 경로 계획 실패 코드, 횡단보도 시나리오 단계)를 사람이 매번 명세와 대조해야 했고, 현장에서 즉시 확인하기 어려웠습니다.
- **인지(Perception) 단계** — Semantic Segmentation·Object Detection 결과가 "보증 거리 안에서 맞게 판단했는지"를 눈으로만 확인했기 때문에, 판단 기준이 사람마다 달랐고 버전 간 비교(Regression)도 수작업이었습니다.

## 접근 방법

같은 문제를 두 단계로 나눠, 각 단계에 맞는 도구를 만들었습니다.

### 1. NTT (Neubie Test Tool) — 로깅 시각화 (2024.12)

로봇에 연결해 실시간 토픽을 구독하고, **숫자 코드를 명세 기반의 의미 있는 상태로 변환해 보여주는** 데스크톱 도구입니다.

- ROS2 토픽 구독 기반 **시스템 모니터** — 관제 주시 신호(remote attention flag) 등 운영 핵심 상태 표시
- **Ego 상태 디버그 뷰** — Local Path Planner 실패 사유, 횡단보도 시나리오 단계 등을 코드가 아닌 설명으로 표시
- SSH 기반 **기체 SW 버전 확인·ROS 파라미터 설정**으로 현장 테스트 준비 시간 단축
- 로봇 SW 버전(2.1.x ~ 2.11.x)별 브랜치로 메시지 구조 변경에 대응

<!--
<figure>
  <img src="/assets/images/practice/visualization/ntt-main.png" alt="NTT 메인 화면">
  <figcaption>NTT — 토픽 구독·시스템 모니터 화면</figcaption>
</figure>
-->

### 2. SS 검증 도구 — 인지 결과 검증 (2026.06 ~ 2026.09)

ROS2 bag 또는 실시간 토픽에서 카메라·SS·LDM·Cliff 데이터를 읽어, **브라우저에서 인지 품질을 정량적으로 검증**하는 도구입니다. (FastAPI + React/three.js)

- **동기화 뷰어** — Raw 카메라 + SS 2×3 뷰, LDM top-down 3D 뷰, 타임라인 scrubbing을 한 화면에서 동기화
- **ROI 기반 정량 지표** — 보증 거리(ROI) 안의 클래스별 점유율을 시계열·누적 차트로 표시
- **교차 검증** — SS ↔ LDM 점유율 비교, 오토레이블링 GT 대비 **픽셀 일치율**
- **Object Detection** — 2D 검출 박스와 3D 객체 컨투어를 같은 클래스 색상 체계로 표시해 "이 박스 = 이 물체"를 바로 확인
- **Regression 자동화** — 티켓별 테스트 데이터 업로드 → 대상 버전 설치 및 perception 재기록 → 결과 회수 → 이슈별 PNG·HTML 리포트 캡처를 버튼 하나로 실행, 중단 시 이어서 진행

<!--
<div class="figures paired">
  <figure>
    <img src="/assets/images/practice/visualization/ss-tool-viewer.png" alt="SS 검증 도구 뷰어">
    <figcaption>카메라·SS·LDM 동기화 뷰어</figcaption>
  </figure>
  <figure>
    <img src="/assets/images/practice/visualization/ss-tool-od.png" alt="Object Detection 검증 화면">
    <figcaption>2D bbox ↔ 3D 컨투어 색상 일치</figcaption>
  </figure>
</div>
-->

## 결과

- 상태 코드·인지 결과를 **같은 화면, 같은 지표**로 보게 되면서 QA·개발·운영 간 해석 차이와 커뮤니케이션 비용이 줄었습니다.
- 이슈 재현 시 해당 시점으로 바로 이동(메모·절대 시각 기반 seek)할 수 있어 원인 분석 시간이 단축되었습니다.
- 인지 모듈 버전 간 비교가 수작업에서 **자동화된 Regression 리포트**로 바뀌어, 반복 검증이 가능한 구조가 되었습니다.

<!-- 확정된 수치가 있다면 여기에 추가 (예: 분석 시간 N분 → M분, Regression 케이스 N건 자동화) -->

## 배운 점

- **지표는 "무엇을 틀렸다고 판단하는가"를 정의하는 일**이었습니다. SS와 GT를 클래스 분포로 비교하면, 좌우가 뒤바뀐 결과도 분포가 같아 100%로 나옵니다. 같은 격자의 GT에는 위치까지 보는 픽셀 일치율을 쓰고, 픽셀 대응이 없는 LDM에만 분포 비교를 쓰는 식으로 데이터 특성에 맞는 지표를 골라야 했습니다.
- **검증되지 않은 전제 위에 알고리즘을 쌓지 않기.** 2D 박스와 3D 컨투어를 공간 매칭하는 알고리즘을 먼저 만들었지만, 원본 트래킹 메시지가 이미 클래스 정보를 갖고 있다는 것을 확인한 뒤 매칭 로직을 통째로 제거해 더 단순하고 신뢰할 수 있는 구조로 바꿨습니다.
- 도구는 만드는 것보다 **계속 쓰이게 하는 것**이 어렵습니다. 로봇 SW 버전별 대응, 실행 스크립트 자동화, 사용 가이드 문서화까지 함께 챙겨야 팀의 도구가 되었습니다.
