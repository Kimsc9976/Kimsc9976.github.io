---
layout: sideproject-list
title: 블로그 제작 기록
project: myblog
permalink: /sideproject/blog/
---

<ul class="post-list">
  {% assign posts = site.pages | where: "project", page.project | where: "layout", "sideproject" | sort: "date" | reverse %}
  {% for post in posts %}
    <li class="post-item">
      <a href="{{ post.url }}">
        <span class="post-title">{{ post.title }}</span>
        {% if post.date %}
          <span class="post-date">{{ post.date | date: "%Y.%m.%d %H:%M" }}</span>
        {% endif %}
      </a>
    </li>
  {% endfor %}
</ul>