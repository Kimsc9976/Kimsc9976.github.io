---
layout: default
title: Side Projects
permalink: /sideproject/
---

<div class="sideproject-hub">

<section class="sideproject-hero">
  <h1>🗂️ Side Projects</h1>
  <p>개인 프로젝트 제작 과정과 기록을 모아둔 허브입니다.</p>
</section>

<section class="sideproject-categories">
  {% for item in site.data.sidebar.sideprojects %}
  <a class="sideproject-card" href="{{ item.url }}">
    <h3>{{ item.title }}</h3>
    {% if item.description %}
      <p>{{ item.description }}</p>
    {% endif %}
  </a>
  {% endfor %}
</section>

</div>
