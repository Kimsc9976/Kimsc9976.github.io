---
layout: sideproject-list
title: 안뇨 제작 기록
project: anyo
permalink: /sideprojects/anyo/
---

<ul>
  {% assign posts = site.sideprojects | where: "project", page.project %}
  {% for post in posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
      <span>{{ post.date | date: "%Y-%m-%d" }}</span>
    </li>
  {% endfor %}
</ul>