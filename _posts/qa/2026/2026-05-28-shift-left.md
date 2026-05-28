---
layout: post
title: Shift Left - 적용하기 전에 먼저 물어야 할 것들
category: qa
date: 2026-05-28
---

* TOC
{:toc}

---

## 1. 말로는 아무나 다 하지...

요즘 트렌드가 어떤진 모르겠지만, 내가 처음 QA를 시작할 때 유행하던 기법이 하나 있다. <br>
'Shift Left'이다.

말로는 단순하다. <br>
프로젝트 초기, Sprint 초반부터 QA가 관여해서  
테스트 전략을 세우고, 요구를 같이 보고, 가능한 한 일찍 검증한다. <br>

근데 막상 적용하려고 보면 감이 잘 안 잡힌다.  <br>

일은 일대로 밀리면서 조금씩 left로 옮겨야 하는데,  
**"관성"** 때문에 되돌아가기도 쉽다. <br>

> **"어디서부터 왼쪽인가, 어디서부터 다른 부서가 이해해줄 수 있는가"**

라는 질문부터 막혀버린다.  <br>

이 글은 Shift Left를 **어떻게 도입한다**는 실무 가이드가 아니라,  
적용하기 **전에** 무엇을 먼저 정리해야 하는지에 대한 고찰이다.

---

## 2. 왼쪽이 어딘데

소프트웨어 흐름을 타임라인으로 그리면  
왼쪽이 시작이고, 오른쪽이 출시다.  <br>

아래 그래프는 전통적인 품질 모델과 Shift-left 모델을 비교한 것이다. <br>
*(출처: Rami Sass, Shift Left: Now for Open Source and Security Compliance, 2015)*

![Comparison of traditional quality model and shift-left model](/assets/images/post/shift_left_now_For_open_source.png)

회색 곡선(Traditional)은 **Test · Deploy** 쪽에 품질 관심이 몰린다. <br>
청록 곡선(Shift-left)은 **Plan & Design · Develop & Build** 쪽으로 피크가 옮겨진다.  <br>

즉, 테스트 단계만 앞당긴다기보다  
**품질에 쏟는 관심의 무게중심**이 왼쪽으로 이동하는 그림이다.

근데 이게 단순히 "테스트를 일찍 시작한다"는 얘기가 아니다.  <br>

> **"무엇을 왼쪽으로 옮기느냐"**가 더 본질적인 질문이다.

빨리 시작만 하면 되는 게 아니고,  
역할·비용·피드백이 함께 움직여야 한다.

- 설계할 때 이미 "이게 어떻게 깨질까?"를 논의하는가  
- 요구가 틀렸을 때 구현 후가 아니라 기획 중에 잡히는가  

이것들이 안 되면  
Plan & Design, Develop & Build에서 활동 범위가 넓어졌다 해도  
**Left가 됐다고 보기 어렵다.**

---

## 3. 왜 왼쪽으로 당기는가

"일찍 하면 좋다"만으로는 설득이 안 될 때가 많다.  <br>
그래서 비용 곡선을 한 번 보는 편이 낫다.

![Defect injection, detection timing, and cost to repair by phase](/assets/images/post/defect_.png)

*(출처: Jones, Capers — Applied Software Measurement)*

그래프에서 눈에 띄는 건 세 가지다.  <br>

- 결함 **주입**은 Coding 단계에 가장 많이 몰린다 (약 85%)  
- 결함 **발견**은 Unit Test · Functional Test 쪽에 피크가 있다  
- **수정 비용**은 오른쪽으로 갈수록 기하급수적으로 커진다 (Release 이후 640×)  

주황 곡선 아래의 파란 화살표가 Shift Left다. <br>
**발견 시점을 왼쪽으로 당기면**, 빨간 비용 곡선을 타기 전에 막을 수 있다는 뜻이다.

> **배포 이후 검증을 없애는 게 아니라,  
> 앞에서 막을 수 있는 실수의 비율을 키우는 것**

에 가깝다.

---

## 4. 진짜 질문은 "어떻게 시작하느냐"가 아니다

Shift Left를 적용하고 싶을 때  
대부분 "어느 단계에 QA를 넣을까"를 먼저 고민한다.  <br>

근데 그 전에 먼저 물어야 할 게 있는 것 같다.  <br>

**우리 팀이 왜 오른쪽에 몰려 있는가.**  <br>

- 릴리즈 직전에 버그가 몰린다면, 테스트가 늦어서인가  
  아니면 요구·설계 단계에서 이미 오해가 심어진 건가  
- QA가 병목처럼 느껴진다면, QA가 늦어서인가  
  아니면 앞 단계가 **"완성된 것만 넘기는 구조"**로 굳어진 건가  
- 자동화를 해도 릴리즈 때마다 불안하다면, 테스트가 부족한 건가  
  아니면 **검증하는 대상·완료 기준**이 막판에야 정해지는 건가  

이 질문들에 답을 못 한 상태에서 Shift Left를 "도입"하면  
결국 이름만 바뀌고 구조는 그대로인 경우가 많다.

> **"언제 테스트하느냐"보다 "무엇이 왼쪽으로 가야 하는가"를 먼저 정하는 게 맞다.**

---

## 5. 같은 이름, 다른 문제

Shift Left라는 말은 조직마다 다른 문제를 풀고 있다.  <br>

릴리스 주기가 빠른 곳에서는 **파이프라인·자동화** 얘기가 되고,  
소규모 팀에서는 **기획 단계 QA 참여·준비 시간**이 핵심이 되고,  
로봇·하드웨어처럼 실환경 테스트 비용이 큰 곳에서는  
시뮬·HIL·스테이징으로 **실차 전에 위험한 걸 터뜨리는 것**이 Left다.

> **Shift Left는 하나의 정의가 아니라, 조직마다 다른 문제를 풀고 있다**

같은 이름인데 내용이 다르다.  <br>
그래서 남의 Left 적용 사례를 그대로 가져오기보다,  
**우리 팀이 오른쪽에 몰린 이유**부터 맞춰 보는 게 낫다.

---

## 6. Left로 가기 전에 필요한 것

일을 하다 보면, 왼쪽으로 옮기기 위한 **사전 작업**이 꽤 필요하다는 걸 느낀다.

이슈는 항상 존재한다.  <br>
Left로 옮겼다고 해서 이슈가 사라지지는 않는다.  <br>
오히려 **일찍 잡을 수 있느냐**가 관건이다.

그래서 최소한 아래는 갖춰져 있어야 한다고 본다.

- **자동화·CI** — 커밋·PR마다 최소한의 검증이 돌아가는지  
- **테스트 신뢰** — "왼쪽으로 왔는데 왜 또 깨지냐"는 말이 나오지 않을 정도의 기준  
- **환경·데이터·시나리오** — 실행 직전이 아니라 준비 단계에서 갖춰지는지  
- **협업 구조** — 완성본만 넘기지 않고, 설계·API·요구 단계에서 같이 보는지  

(이걸 안 잡으면, 일도 제대로 못하면서 왼쪽으로 왜 오냐는 이야기를 듣게 된다. ㅎㅎ)

**가짜 Left** 신호도 있다.

- 이름만 "조기 QA"이고, 개발 끝난 뒤에만 검수함  
- 자동화만 늘리고, 요구·설계 참여는 그대로임  
- "일찍 테스트한다"는데 전략·범위·완료 기준은 여전히 막판에 정함  

이 경우 커버리지 숫자만 올라가고, **판단 시점**은 여전히 오른쪽에 있다.

---

## 7. Left가 못 하는 것, Right와의 관계

솔직하게 말하면, Shift Left가 만능은 아니다.  <br>

프로덕션에서만 드러나는 것들은  
아무리 앞에서 테스트해도 잡기 어렵다.  <br>

실제 부하, 사용자 패턴, 환경·외부 시스템 조합,  
운영 중에 생기는 설정 문제들.  <br>

환경이 다르면  
"로컬에서 통과했는데 현장에서 깨지는" 상황은 여전히 남는다.

배포 이후는 **Shift Right** — 모니터링, 피드백, 점진 배포 같은  
**다른 종류의 확인**이 필요하다.  <br>
Left와 Right는 대립이 아니라, 한 줄기의 품질 연속체라고 본다.

![Shift-left and shift-right in the development lifecycle](/assets/images/post/shift_left_loop.png)

Design · Code 쪽의 **Early Quality Engineering**과  
Deploy · Production 쪽의 **Real-World Validation**이  
피드백 루프로 이어지는 그림이다.  <br>

Left만 하고 Right를 비우면, 현장에서 배우는 게 설계로 돌아오지 않는다.

---

## 8. 결국 태도의 문제

여기까지 정리하고 나면  
Shift Left는 **도구나 프로세스 이전에 태도**에 가깝다는 생각이 든다.  <br>

"이건 QA가 볼 거야"가 아니라  
설계하면서도, 코딩하면서도, 배포 전에도  

> **"이게 지금 맞나?"를 물을 수 있고,  
> "이게 지금 틀려요?"라고 말할 수 있는 문화**

가 있어야 Left가 작동한다.  <br>

그 문화를 만드는 건 QA만의 일이 아니다.  <br>
혼자서 품질을 지키는 구조는 결국 한 명이 병목이 되는 구조다.

<br>

Shift Left를 고민하고 있다면, 도구 선택보다 아래부터 정리해보는 게 먼저가 아닐까.

- **왜** — 지금 품질 활동이 오른쪽에 몰려 있는가  
- **무엇을** — 테스트만 옮기는가, 확인·판단·피드백까지 옮기는가  
- **누가** — 품질 판단을 누가 하는가 (QA만이 아닌가)  
- **언제** — 릴리즈 직전이 아니라, 설계·PR·Sprint 초반에 묻는가  
- **어디서** — 어느 단계·환경에서 검증하는가 (CI, 스테이징, 시뮬 등)  
- **어떻게** — 우리 팀에 맞게 옮길 방법은 무엇인가  

<br>

> **"왜, 무엇을, 누가, 언제, 어디서, 어떻게"** —  
> How보다 Why와 What부터. 그다음이 Left다.

---

## 9. 참고자료

- [Shift-Left and Shift-Right Testing: What They Really Mean for QA — Jeevan Koneti (LinkedIn)](https://www.linkedin.com/pulse/shift-left-shift-right-testing-what-really-mean-qa-jeevan-koneti-rm2qc/)
- [Shift-Left란 무엇인가요? — OpenText](https://www.opentext.com/kr/what-is/shift-left)
- [QA가 Shift-left와 Shift-right 접근 방법을 통해 더 나은 품질을 확보하는 방법 — 채수광, LINE Engineering Blog](https://engineering.linecorp.com/ko/blog/quality-advocator-shift-left-shift-right)
- [Shift Left의 다양한 효과들 — Zeromk2, QA를 재미있게](https://goddessbest-qa.tistory.com/266)
- [시프트 레프트 테스트란 무엇인가요? — IBM Think](https://www.ibm.com/kr-ko/think/topics/shift-left-testing)

---
