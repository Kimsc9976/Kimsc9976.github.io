---
layout: practice
title: "시뮬레이터 기반 검증 환경 구축"
permalink: /practice/simulator-verification/
eyebrow: QA Engineering Practice / 뉴빌리티
headline: 실기체 없이도 같은 조건을 반복 재현할 수 있는 테스트베드 — 도입 전에 "QA에 맞는 시뮬레이터인가"부터 검증
role: 시뮬레이터 조사·환경 셋업·적합성 평가
tech: [SimWorld, Unreal Engine, UnrealCV, URBAN-SIM, Isaac Sim, Python]
# cover:                      # 대표 이미지 (이미지 업로드 후 주석 해제)
#   src: /assets/images/practice/simulator/simworld-overview.png
#   alt: SimWorld 환경에 구성한 로봇 센서
#   caption: 실제 로봇과 동일한 센서 배치로 구성한 시뮬레이션 환경
highlights:
  - value: "20~25 → 2~5"
    label: 카메라 1대 → 7대 구성 시 FPS (SimWorld 구조적 한계 분석)
resources:
  - title: Simulator - SimWorld 간단 평가
    url: /log/note/2026/03/24/simulator-simworld/
  - title: Simulator - Urban Sim 간단 평가
    url: /log/note/2026/04/02/simulator-urban-sim/
  - title: SimWorld GitHub Issue #86 (다중 카메라 FPS 이슈 보고)
    url: https://github.com/SimWorld-AI/SimWorld/issues/86
---

<!--
  이미지 업로드 위치: /assets/images/practice/simulator/
  아래 <figure> 주석을 풀면 해당 위치에 표시됩니다. (파일명은 자유롭게 바꿔도 됩니다)
-->

## 배경과 문제

배달 로봇이 다니는 인도·골목·광장·횡단보도는 변수가 많고, 같은 상황을 실기체로 다시 만들기 어렵습니다.
HILS·실기체 반복 검증만으로는 **edge case 재현, regression, 장시간 안정성 검증**을 원하는 만큼 늘리기 어려웠고,
실기체 투입 전 단계에서 시나리오를 반복 검증할 **테스트베드**가 필요했습니다.

다만 시뮬레이터는 목적에 따라 성격이 크게 다릅니다. QA에 필요한 것은 **같은 입력에 같은 결과가 나오는(deterministic) 시나리오 기반 검증**이므로,
"좋은 시뮬레이터"가 아니라 **"우리 검증 목적에 맞는 시뮬레이터"**를 고르는 것이 먼저였습니다.

## 접근 방법

### 1. SimWorld — 실제 로봇과 동일한 센서 구성으로 환경 셋업

- SimWorld = Unreal Engine + **UnrealCV** + Python 인터페이스 구조를 분석 — 로봇이 아닌 **환경을 제공하는 플랫폼**이라 로봇·센서는 직접 구성
- 카메라 구성 방식 비교
  - `SetCamera`(런타임 동적 배치): 빠른 실험에는 유리하지만 카메라 간 Extrinsics 고정이 어려움
  - **Custom Asset(.pak) 정적 구성**: 실제 로봇과 동일한 센서 배치·Extrinsics를 항상 같은 조건으로 재현 → **채택**
- 다중 카메라 구성 시 성능 검증 — 카메라 1대 20~25 FPS → 7대 2~5 FPS로 **비선형 급락** 확인
  - 원인: UnrealCV `ReadPixels()`의 동기식 GPU→CPU 복사가 카메라 수만큼 직렬 누적
  - 설정이 아닌 **아키텍처 한계**로 판단하고, 재현 조건과 함께 오픈소스에 이슈 보고

<!--
<figure>
  <img src="/assets/images/practice/simulator/simworld-cameras.png" alt="SimWorld 다중 카메라 구성">
  <figcaption>Custom Asset 기반 다중 카메라 구성</figcaption>
</figure>
-->

### 2. URBAN-SIM — Micromobility 전용 시뮬레이터 비교 평가

- Isaac Sim 기반, 대규모 환경 생성·병렬 학습을 전제로 한 **학습/평가 인프라** 성격 확인
- QA 관점 평가 기준으로 비교: 시나리오 재현성, 디버깅 난이도, 운영 비용(GPU 병렬 인프라)
- 결론: 강화학습 기반 대규모 학습에는 강력하지만, **시나리오 기반·deterministic 검증이 목적인 QA에는 오버스펙**

<!--
<div class="figures paired">
  <figure>
    <img src="/assets/images/practice/simulator/simworld-env.png" alt="SimWorld 환경">
    <figcaption>SimWorld</figcaption>
  </figure>
  <figure>
    <img src="/assets/images/practice/simulator/urbansim-env.png" alt="URBAN-SIM 환경">
    <figcaption>URBAN-SIM</figcaption>
  </figure>
</div>
-->

## 결과

- 실제 로봇 센서 배치를 그대로 옮긴 시뮬레이션 환경을 구성해, 실기체 없이 주행 시나리오를 검증할 기반을 마련했습니다.
- 다중 카메라 성능 한계를 수치로 정리해, 시뮬레이터 도입 범위(카메라 수·용도)를 판단하는 근거로 활용했습니다.
- 두 시뮬레이터의 성격 차이를 QA 관점으로 정리해, 팀이 **목적에 맞는 테스트베드**를 선택할 수 있는 기준을 공유했습니다.

<!-- 확정된 결과가 있다면 여기에 추가 (예: 자동화 파이프라인 연동, 재현한 시나리오 수 등) -->

## 배운 점

- **도구의 정체성부터 확인하기.** SimWorld는 "로봇을 주는 플랫폼"이 아니라 "환경을 주는 플랫폼"이고, URBAN-SIM은 시뮬레이터라기보다 학습 파이프라인에 가까웠습니다. 이걸 먼저 파악하지 못하면 셋업 시간이 크게 낭비됩니다.
- **한계를 설정 문제와 구조 문제로 구분하기.** FPS 급락을 튜닝으로 해결하려 하기보다, 내부 동작을 외부에서 추적해 구조적 한계임을 확인하고 이슈로 남기는 것이 더 빠른 판단이었습니다.
- 시뮬레이터 선택 기준은 성능이 아니라 **검증 목적(재현성·결정성·운영 비용)**이어야 합니다.
