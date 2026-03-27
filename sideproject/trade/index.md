---
layout: sideproject-list
title: 자동매매 제작 기록
project: trade
permalink: /sideproject/trade/
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