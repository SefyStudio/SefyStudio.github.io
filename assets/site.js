// Sefy Studio: small page helpers (reveal on scroll, copy-to-clipboard). The page reads fine without them.
(function () {
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!reduce && 'IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.remove('pending'); io.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -8% 0px' });
    document.querySelectorAll('.reveal').forEach(function (el) {
      var r = el.getBoundingClientRect();
      if (r.top > window.innerHeight) { el.classList.add('pending'); io.observe(el); }   // only what is below the fold
    });
  }
  document.querySelectorAll('[data-copy]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var text = btn.getAttribute('data-copy'), done = function () { var t = btn.textContent; btn.textContent = 'Copied'; setTimeout(function () { btn.textContent = t; }, 1600); };
      if (navigator.clipboard) navigator.clipboard.writeText(text).then(done, function () {}); else done();
    });
  });
  var y = document.getElementById('year'); if (y) y.textContent = new Date().getFullYear();
})();
