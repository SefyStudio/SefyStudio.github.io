// SefyStudio site: reveal on scroll, copy email, mobile menu, current year. No tracking, no cookies.
(function () {
  var y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();

  var nav = document.querySelector('.nav'), menu = document.querySelector('.menu');
  if (nav && menu) {
    menu.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      menu.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    nav.querySelectorAll('nav a').forEach(function (a) { a.addEventListener('click', function () { nav.classList.remove('open'); }); });
  }

  var items = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -8% 0px' });
    items.forEach(function (el) { io.observe(el); });
  } else items.forEach(function (el) { el.classList.add('in'); });

  document.querySelectorAll('[data-copy]').forEach(function (b) {
    b.addEventListener('click', function () {
      var text = b.getAttribute('data-copy'), label = b.textContent;
      var done = function () { b.textContent = 'Copied!'; setTimeout(function () { b.textContent = label; }, 1600); };
      if (navigator.clipboard) navigator.clipboard.writeText(text).then(done, function () { location.href = 'mailto:' + text; });
      else location.href = 'mailto:' + text;
    });
  });
})();
