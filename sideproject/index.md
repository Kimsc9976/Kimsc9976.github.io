---
layout: default
title: Side Projects
permalink: /sideproject/
---

<div class="sideproject-hub">

<header class="page-intro">
  <p class="page-intro__eyebrow">Side Projects</p>
  <h1>Side Projects</h1>
  <p>개인 프로젝트 제작 과정과 기록을 모아둔 허브입니다.</p>
</header>

<ul class="log-cards">
  {% for item in site.data.sidebar.sideprojects %}
  <li>
    <a class="log-card" href="{{ item.url }}">
      <span class="log-card__title">{{ item.title }}</span>
      {% if item.description %}<span class="log-card__desc">{{ item.description }}</span>{% endif %}
    </a>
  </li>
  {% endfor %}
</ul>

</div>
