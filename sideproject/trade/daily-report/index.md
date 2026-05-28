---
layout: sideproject-list
title: 일간 레포트
project: trade
trade_section: daily-report
permalink: /sideproject/trade/daily-report/
description: A 프로젝트 submodule에서 오전/오후 세션별로 자동 생성되는 일간 레포트 목록입니다.
---

<p class="trade-back-link">
  <a href="/sideproject/trade/" class="trade-home-btn">← 자동매매 홈</a>
</p>

<ul class="post-list">
  {% assign posts = site.pages | where: "project", "trade" | where: "trade_section", "daily-report" | where: "layout", "sideproject" | sort: "date" | reverse %}
  {% for post in posts %}
    <li class="post-item">
      <a href="{{ post.url }}">
        <span class="trade-recent-list__row">
          <span class="post-title">{{ post.report_date | default: post.date | date: "%Y.%m.%d" }} 일간 레포트</span>
          {% if post.session_label %}
            <span class="trade-session-badge trade-session-badge--{{ post.session }}">{{ post.session_label }}</span>
          {% endif %}
        </span>
        {% if post.date %}
          <span class="post-date">{{ post.date | date: "%Y.%m.%d %H:%M" }}</span>
        {% endif %}
      </a>
    </li>
  {% endfor %}
</ul>
