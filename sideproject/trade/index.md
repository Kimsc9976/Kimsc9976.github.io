---
layout: sideproject-list
title: 매매 제작 기록
project: trade
permalink: /sideprojects/trade/
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