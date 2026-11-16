/*
 * Site chrome — 모바일/태블릿(<1024px) 사이드바 드로어
 * - 데스크톱(>=1024px)은 CSS 만으로 sticky 사이드바, 이 스크립트는 관여하지 않음
 * - 열림 상태: <html class="nav-open">
 * - 닫기: 닫기 버튼 / 배경 클릭 / ESC / 사이드바 링크 클릭 / 데스크톱 폭으로 전환
 */
(function () {
  'use strict';

  var root = document.documentElement;
  var sidebar = document.getElementById('site-sidebar');
  var toggle = document.querySelector('[data-sidebar-toggle]');
  if (!sidebar || !toggle) return;

  var OPEN_CLASS = 'nav-open';
  var desktop = window.matchMedia('(min-width: 1024px)');
  var returnFocus = null;

  function isOpen() {
    return root.classList.contains(OPEN_CLASS);
  }

  function focusables() {
    var nodes = sidebar.querySelectorAll('a[href], button:not([disabled]), summary');
    return Array.prototype.filter.call(nodes, function (el) {
      return el.getClientRects().length > 0;
    });
  }

  function open() {
    if (isOpen() || desktop.matches) return;
    returnFocus = document.activeElement;
    root.classList.add(OPEN_CLASS);
    toggle.setAttribute('aria-expanded', 'true');
    var closeBtn = sidebar.querySelector('[data-sidebar-close]');
    (closeBtn || sidebar).focus({ preventScroll: true });
  }

  function close(restoreFocus) {
    if (!isOpen()) return;
    root.classList.remove(OPEN_CLASS);
    toggle.setAttribute('aria-expanded', 'false');
    if (restoreFocus !== false && returnFocus && typeof returnFocus.focus === 'function') {
      returnFocus.focus({ preventScroll: true });
    }
    returnFocus = null;
  }

  toggle.addEventListener('click', function () {
    if (isOpen()) close();
    else open();
  });

  document.addEventListener('click', function (event) {
    if (event.target.closest('[data-sidebar-close]')) close();
  });

  sidebar.addEventListener('click', function (event) {
    if (isOpen() && event.target.closest('a[href]')) close(false);
  });

  document.addEventListener('keydown', function (event) {
    if (!isOpen()) return;

    if (event.key === 'Escape') {
      event.preventDefault();
      close();
      return;
    }

    if (event.key !== 'Tab') return;
    var items = focusables();
    if (!items.length) return;
    var first = items[0];
    var last = items[items.length - 1];
    var active = document.activeElement;

    if (!sidebar.contains(active)) {
      event.preventDefault();
      first.focus();
    } else if (event.shiftKey && active === first) {
      event.preventDefault();
      last.focus();
    } else if (!event.shiftKey && active === last) {
      event.preventDefault();
      first.focus();
    }
  });

  function onViewportChange() {
    if (desktop.matches) close(false);
  }
  if (desktop.addEventListener) desktop.addEventListener('change', onViewportChange);
  else if (desktop.addListener) desktop.addListener(onViewportChange);

  // 뒤로가기(bfcache)로 돌아왔을 때 열린 채로 남지 않도록
  window.addEventListener('pageshow', function () {
    close(false);
  });
})();
