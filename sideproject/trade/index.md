---
layout: sideproject-list
title: 자동매매 제작 기록
project: trade
permalink: /sideproject/trade/
description: 일간 레포트(A)와 매매일지(B)를 자동 생성해 정리하는 트레이딩 기록 허브입니다.
---

<div class="trade-hub-grid">

  <a href="/sideproject/trade/daily-report/" class="trade-section-card">
    <span class="trade-section-card__icon">📊</span>
    <h2 class="trade-section-card__title">일간 레포트</h2>
    <p class="trade-section-card__desc">A 프로젝트에서 자동 생성 · 오전/오후 세션별 .md</p>
    <span class="trade-section-card__link">전체 보기 →</span>
  </a>

  <a href="/sideproject/trade/journal/" class="trade-section-card">
    <span class="trade-section-card__icon">📈</span>
    <h2 class="trade-section-card__title">매매일지</h2>
    <p class="trade-section-card__desc">B 프로젝트에서 생성 · <strong>1일 1건</strong> buy/sell 차트(PNG) + .md</p>
    <span class="trade-section-card__link">전체 보기 →</span>
  </a>

</div>

<hr class="trade-hub-divider">

<div class="trade-hub-recent-grid">

  <section class="trade-hub-recent-col">
    <div class="trade-hub-recent-col__head">
      <h2 class="trade-hub-section-title">최근 일간 레포트</h2>
      <a class="trade-hub-recent-col__more" href="/sideproject/trade/daily-report/">전체 →</a>
    </div>
    <ul class="post-list trade-recent-list">
      {% assign daily_posts = site.pages | where: "project", "trade" | where: "trade_section", "daily-report" | where: "layout", "sideproject" | sort: "date" | reverse %}
      {% for post in daily_posts limit: 4 %}
        <li class="post-item">
          <a href="{{ post.url }}">
            <span class="trade-recent-list__row">
              <span class="post-title">{{ post.report_date | default: post.date | date: "%Y.%m.%d" }}</span>
              {% if post.session_label %}
                <span class="trade-session-badge trade-session-badge--{{ post.session }}">{{ post.session_label }}</span>
              {% endif %}
            </span>
            {% if post.date %}
              <span class="post-date">{{ post.date | date: "%H:%M" }} 생성</span>
            {% endif %}
          </a>
        </li>
      {% else %}
        <li class="post-item trade-empty">등록된 일간 레포트가 없습니다.</li>
      {% endfor %}
    </ul>
  </section>

  <section class="trade-hub-recent-col">
    <div class="trade-hub-recent-col__head">
      <h2 class="trade-hub-section-title">최근 매매일지</h2>
      <a class="trade-hub-recent-col__more" href="/sideproject/trade/journal/">전체 →</a>
    </div>
    <ul class="post-list trade-recent-list trade-journal-recent-list">
      {% assign journal_posts = site.pages | where: "project", "trade" | where: "trade_section", "journal" | where: "layout", "sideproject" | sort: "date" | reverse %}
      {% for post in journal_posts limit: 4 %}
        <li class="post-item trade-journal-list__item">
          <a href="{{ post.url }}" class="trade-journal-list__link trade-journal-recent-list__link">
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
  </section>

</div>

