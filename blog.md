---
layout: default
title: My Life's Log
permalink: /log/
---

<section class="blog-hero">
  <h1>My Life’s Log</h1>
  <p>QA · 개발 · 일하면서 남겨두는 엔지니어링 기록</p>
</section>

<section class="blog-categories">
  <a class="blog-card qa" href="/log/qa/">
    <h3>🧪 For QA</h3>
    <p>테스트 전략, 자동화, 품질을 엔지니어링으로 다룬 기록</p>
  </a>

  <a class="blog-card dev" href="/log/dev/">
    <h3>💻 For Dev</h3>
    <p>개발 이슈, 구조 설계, 코드 관련 메모</p>
  </a>

  <a class="blog-card note" href="/log/note/">
    <h3>📝 Note</h3>
    <p>짧은 생각, 정리되지 않은 기록들</p>
  </a>
</section>

<section class="blog-recent">
  <h2>🕒 Recent Posts</h2>
  <ul>
    {% for post in site.posts limit:5 %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
      <span>{{ post.date | date: "%Y.%m.%d" }}</span>
    </li>
    {% endfor %}
  </ul>
</section>
