---
layout: default
title: My Life's Log
permalink: /log/
---

<div class="log-hub">

<header class="page-intro">
  <p class="page-intro__eyebrow">Log</p>
  <h1>My Life's Log</h1>
  <p>QA · 개발 · 일하면서 남겨두는 엔지니어링 기록</p>
</header>

<ul class="log-cards">
  <li>
    <a class="log-card" href="/log/qa/">
      <span class="log-card__title">For QA</span>
      <span class="log-card__desc">테스트 전략, 자동화, 품질을 엔지니어링으로 다룬 기록</span>
    </a>
  </li>
  <li>
    <a class="log-card" href="/log/dev/">
      <span class="log-card__title">For Dev</span>
      <span class="log-card__desc">개발 이슈, 구조 설계, 코드 관련 메모</span>
    </a>
  </li>
  <li>
    <a class="log-card" href="/log/note/">
      <span class="log-card__title">Note</span>
      <span class="log-card__desc">짧은 생각, 정리되지 않은 기록들</span>
    </a>
  </li>
</ul>

<section class="log-recent">
  <h2 class="section-label">Recent Posts</h2>
  <ul class="post-list">
    {% for post in site.posts limit:5 %}
    <li class="post-item">
      <a href="{{ post.url }}">{{ post.title }}</a>
      <span class="post-date">{{ post.date | date: "%Y.%m.%d" }}</span>
    </li>
    {% endfor %}
  </ul>
</section>

</div>
