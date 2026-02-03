---
layout: sideproject-list
title: 블로그 제작 기록
project: blog
permalink: /sideprojects/blog/
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