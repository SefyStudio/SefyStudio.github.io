// Sefy Studio: small page helpers (reveal on scroll, copy email, nav border, category tabs). The page reads fine without them.
(function () {
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!reduce && 'IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.remove('pending'); io.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -8% 0px' });
    document.querySelectorAll('.reveal').forEach(function (el) {
      if (el.getBoundingClientRect().top > window.innerHeight) { el.classList.add('pending'); io.observe(el); }   // only what is below the fold
    });
  }
  document.querySelectorAll('[data-copy]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var text = btn.getAttribute('data-copy'), done = function () { var t = btn.textContent; btn.textContent = 'Copied'; setTimeout(function () { btn.textContent = t; }, 1600); };
      if (navigator.clipboard) navigator.clipboard.writeText(text).then(done, function () {}); else done();
    });
  });
  var nav = document.querySelector('.nav');
  if (nav) { var on = function () { nav.classList.toggle('scrolled', window.scrollY > 8); }; on(); window.addEventListener('scroll', on, { passive: true }); }
  document.querySelectorAll('.tabs [data-tab]').forEach(function (tab) {
    tab.addEventListener('click', function () {
      var k = tab.getAttribute('data-tab');
      tab.parentNode.querySelectorAll('[data-tab]').forEach(function (t) { t.setAttribute('aria-selected', t === tab ? 'true' : 'false'); });
      document.querySelectorAll('[data-category]').forEach(function (c) { c.hidden = k !== 'all' && c.getAttribute('data-category') !== k; });
    });
  });
  var y = document.getElementById('year'); if (y) y.textContent = new Date().getFullYear();
})();
// Motion layer: pointer parallax in the hero, tilt + spotlight on cards, count-up numbers.
(function () {
  if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  var fine = window.matchMedia('(pointer: fine)').matches;
  var stage = document.querySelector('[data-parallax]'), eyes = stage && stage.querySelector('.eyes');
  if (eyes && fine) {   // the eyes look toward the pointer; a click makes Sefy blink
    window.addEventListener('pointermove', function (e) {
      var r = stage.getBoundingClientRect(), dx = e.clientX - (r.left + r.width * .55), dy = e.clientY - (r.top + r.height * .4);
      var d = Math.hypot(dx, dy) || 1, k = Math.min(1, d / 400);
      eyes.style.transform = 'translate(' + (dx / d * 14 * k).toFixed(1) + 'px,' + (dy / d * 10 * k).toFixed(1) + 'px)';
    }, { passive: true });
    stage.addEventListener('click', function () { stage.classList.remove('happy'); void stage.offsetWidth; stage.classList.add('happy'); });
  }
  document.querySelectorAll('[data-glow]').forEach(function (el) {
    el.addEventListener('pointermove', function (e) {
      var r = el.getBoundingClientRect(), x = e.clientX - r.left, y = e.clientY - r.top;
      el.style.setProperty('--mx', x + 'px'); el.style.setProperty('--my', y + 'px');
      if (fine && el.hasAttribute('data-tilt')) {
        el.style.setProperty('--ry', ((x / r.width - .5) * 8).toFixed(2) + 'deg');
        el.style.setProperty('--rx', ((.5 - y / r.height) * 8).toFixed(2) + 'deg');
      }
    });
    el.addEventListener('pointerleave', function () { el.style.setProperty('--rx', '0deg'); el.style.setProperty('--ry', '0deg'); });
  });
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (!e.isIntersecting) return; io.unobserve(e.target);
        var el = e.target, to = +el.getAttribute('data-count'), t0 = performance.now();
        if (!to) return;
        (function step(t) { var k = Math.min(1, (t - t0) / 1200); el.textContent = Math.round(to * (1 - Math.pow(1 - k, 3))); if (k < 1) requestAnimationFrame(step); })(t0);
      });
    }, { threshold: .6 });
    document.querySelectorAll('[data-count]').forEach(function (el) { io.observe(el); });
  }
})();
