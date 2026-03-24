---
layout: post
title: Simulator - SimWorld 간단 평가...
category: note
date: 2026-03-24
---

* TOC
{:toc}

---

## 1. 개요 (Overview)

### SimWorld란?

**SimWorld**는 Unreal Engine 기반의 자율주행 시뮬레이션 플랫폼으로,
고해상도 그래픽과 물리 엔진을 활용하여 **로봇 및 차량 환경을 가상으로 재현**할 수 있다.

주요 특징은 다음과 같다:

* Unreal Engine 기반 고품질 렌더링
* 다양한 환경(도시, 보행자, 차량) 시뮬레이션
* AI 기반 객체 행동 모델링 지원

> ✅ **Key Point**
> SimWorld는 “로봇을 제공하는 플랫폼”이 아니라
> **환경을 제공하는 시뮬레이터**이다.

---

### UnrealCV란?

SimWorld 내부 동작을 이해하려면 **UnrealCV**를 반드시 알아야 한다.

**UnrealCV**는 Unreal Engine에서 컴퓨터 비전 연구를 위해 사용하는 플러그인으로,
외부(Python 등)에서 엔진 내부 데이터를 제어 및 추출할 수 있게 해준다.

주요 기능:

* 카메라 위치 및 각도 제어
* RGB / Depth / Segmentation 데이터 추출
* Object-level 정보 획득

> ⚠️ **중요한 구조적 사실**
> SimWorld는 내부적으로 **UnrealCV를 통해 센서 데이터를 생성한다**

즉, 미우나 고우나 

* 기본 제공 Asset을 쓰거나
* Custom Asset을 만들거나

👉 눈물을 흘리면서 **UnrealCV 인터페이스를 따라야 한다** > 이 것을 모르면 SimWorld를 사용하기 어렵다는 것이다.
- 본격! OpenSource로 OpenSource 만들기 (들어만 봤지 직접 경험한것은 이번이 처음이긴하다.)

---

## 2. 테스트 환경 (Environment Setup)

SimWorld는 [환경설정 하는 것](https://simworld.readthedocs.io/en/latest/getting_started/introduction.html#overview)은 다른 시뮬레이터 보다는 잘 알려주는 편이다 .

* Unreal Engine 기반 SimWorld
* UnrealCV 플러그인
* Python 인터페이스 (외부 제어)

> 🔎 **정리**
> SimWorld는 독립적인 시스템이 아니라
> **Unreal Engine + UnrealCV 위에 올라간 구조**다.

---

## 3. 센서 구성 방식: SetCamera vs Custom Asset

SimWorld에서 카메라 센서를 구성하는 방식은 크게 두 가지로 나뉜다.

---

### 3.1 SetCamera (동적 배치)

런타임에서 코드로 카메라를 생성 및 제어하는 방식이다.

**특징**

* 코드 기반 동적 제어
* 빠른 테스트 가능

**장점**

* 유연한 위치/각도 변경
* 초기 실험에 적합

**단점**

* 센서 간 정밀한 위치 관계 유지 어려움
* 복잡한 센서 구성 관리 어려움

---

### 3.2 Custom Asset (.pak) 기반 정적 구성

Unreal Editor에서 로봇 및 센서를 구성한 뒤 `.pak`으로 패키징하는 방식이다.
SimWorld에서 [자랑스럽게 이야기](https://simworld.readthedocs.io/en/latest/customization/make_your_own_pak.html)하는 방식이기도 하다  

**특징**

* 사전 정의된 센서 구조 사용

**장점**

* 센서 간 Extrinsics 정확히 고정
* 복잡한 멀티 센서 구성 가능
* 실행 시 항상 동일한 환경 보장

**단점**

* 수정 비용 높음
* Unreal Engine 작업 필요

> ✅ **선택 이유**
> 실제 로봇 환경과 동일한 센서 구성을 유지하기 위해
> Custom Asset 방식을 선택

---

## 4. Known Issue: Multi-Camera FPS Drop

Custom Asset 기반으로 다중 카메라를 구성할 경우
심각한 성능 저하 문제가 발생한다.

---

### 현상

* 단일 카메라: 약 20~25 FPS
* 다중 카메라 (5~7개): 약 2~5 FPS

👉 카메라 수 증가에 따라 **선형이 아닌 급격한 성능 저하 발생**

---

### 원인 (Root Cause)

핵심 원인은 UnrealCV 내부의 데이터 처리 방식인 것으로 판단된다. (미천한 나로서는 여기까지가 한계이다. 디버깅을 할 수도 없고..ㅠㅠ)

* `ReadPixels()` 호출
* GPU → CPU 데이터 복사 발생
* 이 과정이 **동기(Synchronous)로 수행됨**

즉,

```
Render → ReadPixels → CPU Copy → 다음 Frame
```

👉 이 구조 때문에 카메라 수만큼 병목이 누적되는 것으로 보여짐
* 단일 카메라 : 25 FPS
* 다중카메라 7개 적용 : 3x7 ≈ 25 FPS

---

### 구조적 문제
이것 때문에 지금 살짝 블로킹이 걸려 있다..
* UnrealCV는 기본적으로 **동기식 데이터 수집 구조**
* 멀티 카메라 환경에서 병렬 처리 불가능
* 결과적으로 **프레임 드랍이 필연적**

---

### 관련 논의

* [SimWorld GitHub Issue #86](https://github.com/SimWorld-AI/SimWorld/issues/86)
* Multi-camera 환경에서 FPS 급락 문제 보고

핵심 요약:

* 설정 문제가 아님
* UnrealCV 구조 자체의 한계로 보여짐
* 우리는 `SimWorld`설정을 수정 할 수 없음

이걸 SimWorld에서 해결해줄까? 싶긴 하지만 일단 질문은 던져놨고 답은 기다리고 있는 중이다.. <br>
오픈소스이지만, 한계가 있는 슬픔이 나를 괴롭게 한다

---

> ⚠️ **핵심 결론**
> 이 문제는 단순 성능 문제가 아니라
> **센서 데이터 수집 구조(Architecture)의 한계**이다.

---

## 5. 정리

SimWorld + UnrealCV 기반 시뮬레이션 환경에서의 핵심 포인트:

* SimWorld는 환경 제공 도구
* 센서 데이터는 UnrealCV에 의존
* 멀티 카메라 환경에서 구조적 병목 존재

결론 - SimWorld 쓰고싶으면 UnrealEngine공부를 좀 해놔야한다


---

