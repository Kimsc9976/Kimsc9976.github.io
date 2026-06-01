---
layout: sideproject-list
title: 매매일지
project: trade
trade_section: journal
permalink: /sideproject/trade/journal/
description: modules/trade_report 서브모듈에서 동기화되는 매매일지 + buy/sell 차트(PNG) 목록입니다.
---

<p class="trade-back-link">
  <a href="/sideproject/trade/" class="trade-home-btn">← 자동매매 홈</a>
</p>

<ul class="post-list trade-journal-list">
  {% assign posts = site.pages | where: "project", "trade" | where: "trade_section", "journal" | where: "layout", "sideproject" | sort: "date" | reverse %}
  {% for post in posts %}
    <li class="post-item trade-journal-list__item">
      <a href="{{ post.url }}" class="trade-journal-list__link">
        <span class="trade-journal-list__text">
          <span class="post-title">{{ post.journal_date | default: post.date | date: "%Y.%m.%d" }} 매매일지</span>
          {% if post.date %}
            <span class="post-date">{{ post.date | date: "%Y.%m.%d %H:%M" }} 생성</span>
          {% endif %}
        </span>
        {% if post.chart %}
          <img src="{{ post.chart }}" alt="{{ post.title }} 차트 썸네일" class="trade-journal-list__thumb" loading="lazy">
        {% endif %}
      </a>
    </li>
  {% else %}
    <li class="post-item trade-empty">등록된 매매일지가 없습니다.</li>
  {% endfor %}
</ul>
