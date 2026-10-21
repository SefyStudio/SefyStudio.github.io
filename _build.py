#!/usr/bin/env python3
"""Builds every page of the SefyStudio site from one template (nav, footer, head), styled by assets/site.css.

    python3 _build.py

Edit the page bodies below, never the generated .html files. Files starting with "_" are not published by GitHub Pages.
pip-and-pals/play/ is the Pip & Pals web game (a copy of pip-and-pals/web/index.html with house ads), not built here.
"""
import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = "https://sefystudio.com"
EMAIL = "support@sefystudio.com"
LOOM_STORE = "https://apps.apple.com/app/id6822636298"
PIP_STORE = "https://apps.apple.com/app/id6819880110"
MIX_STORE = "https://apps.apple.com/app/id6823995084"
APPLE = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M16.4 12.6c0-2.4 2-3.6 2.1-3.7-1.2-1.7-3-1.9-3.6-2'
         '-1.5-.2-3 .9-3.8.9-.8 0-2-.9-3.3-.9-1.7 0-3.3 1-4.1 2.5-1.8 3.1-.5 7.6 1.3 10.1.8 1.2 1.8 2.6 3.1 2.5 1.2 0 1.7-.8 3.2-.8s1.9.8 '
         '3.2.8c1.3 0 2.2-1.2 3-2.4.9-1.4 1.3-2.7 1.3-2.8 0 0-2.4-1-2.4-4.2zM14 5.4c.7-.8 1.1-1.9 1-3-1 0-2.1.7-2.8 1.5-.6.7-1.2 1.8-1 2.9 '
         '1 .1 2.1-.6 2.8-1.4z"/></svg>')
PLAY = '<svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path fill="currentColor" d="M8 5.5v13l10.5-6.5z"/></svg>'


def live_mascot():
    """The mascot SVG inlined with hooks for CSS/JS: blinking eyes that follow the pointer, pulsing rays, a breathing body."""
    svg = open(os.path.join(ROOT, "assets/brand/sefy-mascot.svg"), encoding="utf-8").read()
    svg = svg.replace('<svg ', '<svg class="mascot" role="img" aria-label="Sefy, the SefyStudio mascot" ', 1)
    svg = re.sub(r'width="\d+" height="\d+"', '', svg, count=1)
    eyes = re.findall(r'<rect [^>]*fill="#16112A"[^>]*/>', svg)
    for e in eyes:
        svg = svg.replace(e, f'<g class="eye">{e}</g>')
    svg = svg.replace(f'<g class="eye">{eyes[0]}</g>', f'<g class="eyes"><g class="eye">{eyes[0]}</g>', 1)
    svg = svg.replace(f'<g class="eye">{eyes[1]}</g>', f'<g class="eye">{eyes[1]}</g></g>', 1)
    svg = svg.replace('<g transform="scale(0.25)', '<g class="rays-wrap"><g transform="scale(0.25)', 1)
    i = svg.index('<g class="rays-wrap">'); j = svg.index('</g>', i) + 4
    svg = svg[:j] + '</g>' + svg[j:]
    return svg


def ver(rel):
    """Cache-busting query from the file's content, so browsers pick up CSS/JS changes at once."""
    import hashlib
    return hashlib.sha1(open(os.path.join(ROOT, rel), "rb").read()).hexdigest()[:8]


def store(url, small=False):
    return (f'<a class="btn store{" small" if small else ""}" href="{url}">{APPLE}'
            '<span><small>Download on the</small>App Store</span></a>')


def page(path, title, desc, body, game=None, current=None, image="/assets/brand/og-image.png", icon=None, extra=""):
    links = [("/#games", "Games", "games", ""), ("/loom-pop/", "Loom Pop!", "loom", "opt"), ("/pip-and-pals/", "Pip &amp; Pals", "pip", "opt"), ("/mix-bar/", "Mix Bar", "mix", "opt"),
             ("/#about", "About", "about", "opt"), ("/#contact", "Contact", "contact", "")]
    icons = (f'<link rel="icon" href="{icon}">\n<link rel="apple-touch-icon" href="{icon}">' if icon else
             '<link rel="icon" href="/favicon.ico" sizes="48x48">\n<link rel="icon" type="image/png" sizes="192x192" href="/assets/brand/favicon-192.png">\n'
             '<link rel="apple-touch-icon" href="/assets/brand/apple-touch-icon.png">')
    nav = "".join(f'<a href="{h}"{" class=" + chr(34) + c + chr(34) if c else ""}{" aria-current=" + chr(34) + "page" + chr(34) if k == current else ""}>{t}</a>'
                  for h, t, k, c in links)
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#f7f5ff" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0f0c19" media="(prefers-color-scheme: dark)">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE}{image}">
<meta property="og:url" content="{SITE}{path}">
<meta name="twitter:card" content="summary_large_image">
{icons}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@600;700;800&amp;family=Figtree:wght@400;500;600;700&amp;display=swap">
<link rel="stylesheet" href="/assets/site.css?v={ver('assets/site.css')}">
{extra}</head>
<body{f' data-game="{game}"' if game else ""}>
<header class="nav"><div class="wrap"><div class="bar">
  <a class="logo" href="/"><img class="on-light" src="/assets/brand/sefystudio-logo-horizontal.svg" alt="SefyStudio" width="300" height="96"><img class="on-dark" src="/assets/brand/sefystudio-logo-horizontal-white.svg" alt="SefyStudio" width="300" height="96"></a>
  <nav aria-label="Main">{nav}</nav>
</div></div></header>
<main>
{body.strip()}
</main>
<footer><div class="wrap">
  <div class="cols">
    <div class="brand"><a class="logo" href="/"><img class="on-light" src="/assets/brand/sefystudio-logo-horizontal.svg" alt="SefyStudio" width="300" height="96"><img class="on-dark" src="/assets/brand/sefystudio-logo-horizontal-white.svg" alt="SefyStudio" width="300" height="96"></a>
      <p>An independent studio making cozy games and apps for iPhone, iPad and the web.</p></div>
    <div><h4>Loom Pop!</h4><ul><li><a href="/loom-pop/">Overview</a></li><li><a href="{LOOM_STORE}">App Store</a></li>
      <li><a href="/loom-pop/support.html">Support</a></li><li><a href="/loom-pop/privacy.html">Privacy</a></li></ul></div>
    <div><h4>Pip &amp; Pals</h4><ul><li><a href="/pip-and-pals/">Overview</a></li><li><a href="/pip-and-pals/play/">Play in browser</a></li>
      <li><a href="{PIP_STORE}">App Store</a></li><li><a href="/pip-and-pals/support.html">Support</a></li><li><a href="/pip-and-pals/privacy.html">Privacy</a></li></ul></div>
    <div><h4>Mix Bar</h4><ul><li><a href="/mix-bar/">Overview</a></li><li><a href="/mix-bar/support.html">Support</a></li><li><a href="/mix-bar/privacy.html">Privacy</a></li></ul></div>
    <div><h4>Studio</h4><ul><li><a href="/#about">About</a></li><li><a href="/#contact">Contact</a></li><li><a href="/brand/">Brand assets</a></li><li><a href="/app-ads.txt">app-ads.txt</a></li></ul></div>
  </div>
  <p class="legal">© <span id="year">2026</span> SefyStudio. Apple, the Apple logo, iPhone and iPad are trademarks of Apple Inc. App Store is a service mark of Apple Inc.</p>
</div></footer>
<script src="/assets/site.js?v={ver('assets/site.js')}" defer></script>
</body>
</html>
"""
    out = os.path.join(ROOT, path.strip("/"), "index.html") if path.endswith("/") else os.path.join(ROOT, path.strip("/"))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", os.path.relpath(out, ROOT))


def contact(game_name=None):
    what = f"Questions about {game_name}? " if game_name else ""
    return f"""<section id="contact"><div class="wrap">
  <div class="contact card reveal">
    <div><h2>Say hello</h2><p>{what}Ideas, bugs, press or partnerships: we read every email.</p></div>
    <div class="copy-row"><code>{EMAIL}</code><button class="btn primary" type="button" data-copy="{EMAIL}">Copy email</button></div>
  </div>
</div></section>"""


# ───────────────────────── home ─────────────────────────
# Everything we ship, one entry each. category: "games" | "apps" | "web". The home page shows category tabs only once
# two or more categories have something in them; until then it is a plain "Games" grid.
PRODUCTS = [
    dict(category="games", cls="loom", name="Loom Pop!", page="/loom-pop/", art="/assets/loom-pop-art.webp", icon="/assets/loom-pop-icon.png",
         alt="Knitted pattern cards pegged on a yarn line", text="A cozy yarn-sorting puzzle. Tap yarn balls, fill the loom and weave 200+ patterns.",
         tags=["Puzzle", "iPhone", "Free"], cta=[store(LOOM_STORE), '<a class="btn ghost" href="/loom-pop/">Details</a>']),
    dict(category="games", cls="pip", name="Pip &amp; Pals: Hide &amp; Seek", page="/pip-and-pals/", art="/assets/pip-and-pals-art.webp",
         icon="/assets/pip-and-pals-icon.png", alt="Pip, Momo and Ziggy hiding from a drone",
         text="Morph into objects, dodge the drones and fix the rocket, alone or with up to 3 friends.",
         tags=["Adventure", "Co-op", "iPhone &amp; iPad", "Web"], cta=[store(PIP_STORE), f'<a class="btn ghost" href="/pip-and-pals/play/">{PLAY} Play in browser</a>']),
    dict(category="games", cls="mix", name="Mix Bar: Water Sort Puzzle", page="/mix-bar/", art="/assets/mix-bar-art.webp", icon="/assets/mix-bar-icon.png",
         alt="The Mix Bar logo between glasses of soda", text="Pour, mix and serve! A water sort puzzle where flavours mix when you pour them.",
         tags=["Puzzle", "iPhone", "Free", "Coming soon"], cta=['<a class="btn ghost" href="/mix-bar/">Details</a>']),
]
CATEGORIES = [("games", "Games"), ("apps", "Apps"), ("web", "Web apps")]


def product_card(p):
    tags = "".join(f'<span class="chip">{t}</span>' for t in p["tags"])
    return f"""<article class="game-card card reveal" data-tilt data-glow data-category="{p['category']}">
      <a class="art" href="{p['page']}"><img src="{p['art']}" alt="{p['alt']}" width="1600" height="685" loading="lazy"></a>
      <div class="body"><img class="icon" src="{p['icon']}" alt="" width="152" height="152">
        <div><h3>{p['name']}</h3><p>{p['text']}</p><div class="tags">{tags}</div></div></div>
      <div class="cta">{"".join(p['cta'])}</div>
    </article>"""


def products_section():
    used = [(k, t) for k, t in CATEGORIES if any(p["category"] == k for p in PRODUCTS)]
    title = used[0][1] if len(used) == 1 else "Our work"
    tabs = ""
    if len(used) > 1:
        tabs = '<div class="tabs" role="tablist">' + '<button role="tab" aria-selected="true" data-tab="all">All</button>' + "".join(
            f'<button role="tab" aria-selected="false" data-tab="{k}">{t}</button>' for k, t in used) + "</div>"
    return f"""<section id="games"><div class="wrap">
  <div class="section-head reveal"><h2>{title}</h2>{tabs}</div>
  <div class="games">{"".join(product_card(p) for p in PRODUCTS)}</div>
</div></section>"""


SHOTS = [f"/loom-pop/img/shot-{i}.webp" for i in (1, 2, 3, 5, 6)] + [f"/pip-and-pals/img/shot-{i}.webp" for i in (1, 2, 3, 4, 7)]
MARQUEE = "".join(f'<img src="{u}" alt="" width="540" height="1173" loading="lazy">' for u in SHOTS[0::2] + SHOTS[1::2])

HOME = f"""
<section class="hero"><div class="aurora" aria-hidden="true"><i></i><i></i><i></i></div><div class="wrap grid">
  <div class="hero-copy">
    <h1>Hi, we're <span class="shine">SefyStudio</span>.</h1>
    <p class="lead">A small independent studio making cozy games and apps for iPhone, iPad and the web. No accounts, fair to play, in ten languages.</p>
    <div class="actions">
      <a class="btn primary" href="#games">See our games</a>
      <a class="btn ghost" href="/pip-and-pals/play/">{PLAY} Play Pip &amp; Pals in your browser</a>
    </div>
  </div>
  <div class="stage" data-parallax>{live_mascot()}</div>
</div></section>

<div class="marquee-wrap" aria-hidden="true"><div class="marquee"><div class="track">{MARQUEE}{MARQUEE}</div></div></div>

{products_section()}

<section id="about"><div class="wrap">
  <div class="section-head reveal"><h2>Small studio.<br>Big standards.</h2>
    <p>A tiny team, two games and a long list of things we refuse to cut corners on.</p></div>
  <div class="bento">
    <div class="tile big card reveal" data-glow><div class="num"><b data-count="200">200</b>+</div>
      <h3>hand-drawn patterns</h3><p>Every motif in Loom Pop! is drawn stitch by stitch and woven in eight collections, from Kilim Classics to Sea Life.</p>
      <div class="motifs"><img src="/loom-pop/img/motif-kilim.png" alt="" width="160" height="160" loading="lazy"><img src="/loom-pop/img/motif-fruit.png" alt="" width="160" height="160" loading="lazy"><img src="/loom-pop/img/motif-garden.png" alt="" width="160" height="160" loading="lazy"><img src="/loom-pop/img/motif-sweets.png" alt="" width="160" height="160" loading="lazy"><img src="/loom-pop/img/motif-sea.png" alt="" width="160" height="160" loading="lazy"><img src="/loom-pop/img/motif-home.png" alt="" width="160" height="160" loading="lazy"><img src="/loom-pop/img/motif-nature.png" alt="" width="160" height="160" loading="lazy"><img src="/loom-pop/img/motif-adventure.png" alt="" width="160" height="160" loading="lazy"></div></div>
    <div class="tile card reveal" data-glow><div class="num"><b data-count="10">10</b></div>
      <h3>languages on day one</h3><p>English, Türkçe, Español, Português, Deutsch, Français, Italiano, 日本語 and 한국어.</p></div>
    <div class="tile card reveal" data-glow><div class="num"><b data-count="3">3</b></div>
      <h3>friends, one room</h3><p>Real-time co-op in Pip &amp; Pals that works across iPhone, iPad and the browser.</p></div>
    <div class="tile card reveal" data-glow><div class="num"><b data-count="0">0</b></div>
      <h3>accounts needed</h3><p>No sign-up and no user database. Your progress belongs on your device.</p></div>
    <div class="tile card reveal" data-glow><div class="num"><b data-count="1">1</b></div>
      <h3>tap to play</h3><p>Pip &amp; Pals runs right in your browser: no download, same game as the app.</p></div>
    <div class="tile wide card reveal" data-glow><h3>We tune the feel until it's right.</h3>
      <p>Every tap, sound and haptic goes through round after round of playtests. If a level feels unfair or a sound gets tiring, it changes before it ships.</p></div>
  </div>
</div></section>

<section class="next"><div class="wrap"><div class="next-card card reveal" data-glow>
  <div><h2>More on the loom.</h2><p>New games and our first apps are in the works. Want to hear first, test early or work with us? Say hi.</p></div>
  <a class="btn primary" href="#contact">Get in touch</a>
</div></div></section>
{contact()}
"""

# ───────────────────────── Loom Pop ─────────────────────────
LOOM = f"""
<section class="ghero"><div class="wrap">
  <div class="panel card">
    <div class="art"><img src="/assets/loom-pop-art.webp" alt="Knitted pattern cards pegged on yarn lines above a pile of yarn balls" width="1600" height="685"></div>
    <div class="info">
      <img class="icon" src="/assets/loom-pop-icon.png" alt="Loom Pop! app icon" width="224" height="224">
      <div>
        <h1>Loom Pop! <span>Yarn Sort Puzzle</span></h1>
        <p class="tagline">A cozy yarn-sorting puzzle. Tap the yarn balls, fill the loom and weave colourful patterns for your customers, stitch by stitch.</p>
        <div class="meta"><span class="chip">Free</span><span class="chip">iPhone</span><span class="chip">200+ patterns</span><span class="chip">10 languages</span><span class="chip">Plays offline</span></div>
      </div>
      <div class="actions">{store(LOOM_STORE)}<span class="btn ghost small" aria-disabled="true">Web version coming soon</span></div>
    </div>
  </div>
</div></section>

<section><div class="wrap">
  <div class="section-head reveal"><h2>Tap, match &amp; weave</h2>
    <p>Easy to learn, endlessly satisfying: every yarn you sort knits its share of a picture on the loom.</p></div>
  <div class="features">
    <article class="feature card reveal"><div class="shot"><img src="img/shot-2.webp" alt="A finished woven puppy pattern" width="540" height="1173" loading="lazy"></div>
      <h3>Sort the yarn</h3><p>Pick yarn balls from the pile and send them to the right colour. Soft sounds and a gentle tick when a row is done.</p></article>
    <article class="feature card reveal"><div class="shot"><img src="img/shot-1.webp" alt="The sticker album with eight collections" width="540" height="1173" loading="lazy"></div>
      <h3>Collect 200+ patterns</h3><p>Fill a sticker album across eight collections, from Kilim Classics and Sweet Shop to Sea Life and Adventure.</p></article>
    <article class="feature card reveal"><div class="shot"><img src="img/shot-4.webp" alt="A customer waiting for their rug" width="540" height="1173" loading="lazy"></div>
      <h3>Happy customers</h3><p>Weave each order before your customer loses patience, and meet a new customer of the day.</p></article>
  </div>
</div></section>

<section><div class="wrap watch">
  <div class="phone reveal"><video src="img/preview.mp4" poster="img/preview-poster.jpg" muted loop playsinline autoplay preload="metadata" aria-label="Loom Pop! gameplay preview"></video></div>
  <div class="reveal">
    <h2>A little calm in every level</h2>
    <p class="lede">Grow your yarn shop, decorate the Cozy Corner and the Loom Workshop, keep a win streak going and open a daily gift. Play anywhere, no Wi-Fi needed.</p>
    <div class="facts-table">
      <div class="fact"><small>Patterns</small><strong>200+ in 8 collections</strong></div>
      <div class="fact"><small>Devices</small><strong>iPhone, iOS 17+</strong></div>
      <div class="fact"><small>Price</small><strong>Free, optional No Ads</strong></div>
      <div class="fact"><small>Languages</small><strong>10, incl. Türkçe &amp; 日本語</strong></div>
    </div>
  </div>
</div></section>

<section><div class="wrap">
  <div class="section-head reveal"><h2>From the App Store</h2></div>
  <div class="rail reveal" tabindex="0" aria-label="Screenshots">
    <img src="img/shot-1.webp" alt="Collect 200+ cozy patterns" width="540" height="1173" loading="lazy">
    <img src="img/shot-2.webp" alt="Tap, match and weave" width="540" height="1173" loading="lazy">
    <img src="img/shot-3.webp" alt="Watch every stitch come alive" width="540" height="1173" loading="lazy">
    <img src="img/shot-4.webp" alt="A new customer every day" width="540" height="1173" loading="lazy">
    <img src="img/shot-5.webp" alt="Weave it before they lose patience" width="540" height="1173" loading="lazy">
    <img src="img/shot-6.webp" alt="Upgrade your yarn shop" width="540" height="1173" loading="lazy">
    <img src="img/shot-7.webp" alt="Hundreds of cozy levels" width="540" height="1173" loading="lazy">
  </div>
</div></section>

<section><div class="wrap">
  <div class="help">
    <a class="card reveal" href="support.html"><b>Support</b><span>Restore No Ads, missing coins, progress and ad choices.</span></a>
    <a class="card reveal" href="privacy.html"><b>Privacy</b><span>No accounts, no user database. Ads by Google AdMob.</span></a>
    <a class="card reveal" href="{LOOM_STORE}"><b>App Store</b><span>Free download for iPhone.</span></a>
  </div>
</div></section>
{contact("Loom Pop!")}
"""

# ───────────────────────── Pip & Pals ─────────────────────────
PIP = f"""
<section class="ghero"><div class="wrap">
  <div class="panel card">
    <div class="art"><img src="/assets/pip-and-pals-art.webp" alt="Pip, Momo and Ziggy hiding behind a bush from a drone" width="1600" height="685"></div>
    <div class="info">
      <img class="icon" src="/assets/pip-and-pals-icon.png" alt="Pip &amp; Pals app icon" width="224" height="224">
      <div>
        <h1>Pip &amp; Pals <span>Hide &amp; Seek</span></h1>
        <p class="tagline">Three friends fell from their moon. Hide from the drones, finish the tasks and fix the rocket, alone or with friends.</p>
        <div class="meta"><span class="chip">Free</span><span class="chip">iPhone &amp; iPad</span><span class="chip">Co-op for up to 3</span><span class="chip">21 levels</span><span class="chip">10 languages</span></div>
      </div>
      <div class="actions"><a class="btn primary" href="play/">{PLAY} Play in browser</a>{store(PIP_STORE)}</div>
    </div>
  </div>
</div></section>

<section><div class="wrap">
  <div class="section-head reveal"><h2>Hide in plain sight</h2>
    <p>Become a bush, a barrel, even a cow. Stay still while the drones sweep past, then sneak on to the next task.</p></div>
  <div class="features">
    <article class="feature card reveal"><div class="shot"><img src="img/shot-1.webp" alt="Pip hiding as a bush" width="540" height="1173" loading="lazy"></div>
      <h3>Morph &amp; hide</h3><p>Turn into the objects around you and hold your breath. Every world brings a new drone with its own way of hunting.</p></article>
    <article class="feature card reveal"><div class="shot"><img src="img/shot-2.webp" alt="Three friends playing together" width="540" height="1173" loading="lazy"></div>
      <h3>Play with friends</h3><p>Team up with up to 3 pals: share a room code, split the tasks and revive each other. Works across phone, tablet and web.</p></article>
    <article class="feature card reveal"><div class="shot"><img src="img/shot-3.webp" alt="Running from a drone" width="540" height="1173" loading="lazy"></div>
      <h3>Spotted? Run!</h3><p>Dash, dodge and shake off the drones, crack secret codes and pull the right levers to fix the rocket home.</p></article>
  </div>
</div></section>

<section><div class="wrap watch">
  <div class="phone reveal"><video src="img/preview.mp4" poster="img/preview-poster.jpg" muted loop playsinline autoplay preload="metadata" aria-label="Pip &amp; Pals gameplay preview"></video></div>
  <div class="reveal">
    <h2>21 levels in 7 worlds</h2>
    <p class="lede">From sunny meadows to a moonlit night: clever tasks, secret codes and a rocket to fix. Play the full game right here in your browser, or get the app for iPhone and iPad.</p>
    <div class="facts-table">
      <div class="fact"><small>Players</small><strong>Solo or co-op for 2–3</strong></div>
      <div class="fact"><small>Platforms</small><strong>iPhone, iPad &amp; web</strong></div>
      <div class="fact"><small>Price</small><strong>Free, optional Plus</strong></div>
      <div class="fact"><small>Languages</small><strong>10, incl. Türkçe &amp; 한국어</strong></div>
    </div>
    <div style="display:flex;flex-wrap:wrap;gap:12px;margin-top:26px"><a class="btn primary" href="play/">{PLAY} Play now, free</a></div>
  </div>
</div></section>

<section><div class="wrap">
  <div class="section-head reveal"><h2>From the App Store</h2></div>
  <div class="rail reveal" tabindex="0" aria-label="Screenshots">
    <img src="img/shot-1.webp" alt="Hide in plain sight" width="540" height="1173" loading="lazy">
    <img src="img/shot-2.webp" alt="Play with friends" width="540" height="1173" loading="lazy">
    <img src="img/shot-3.webp" alt="Spotted? Run!" width="540" height="1173" loading="lazy">
    <img src="img/shot-4.webp" alt="Crack the code" width="540" height="1173" loading="lazy">
    <img src="img/shot-5.webp" alt="Meet the drones" width="540" height="1173" loading="lazy">
    <img src="img/shot-6.webp" alt="Clever tasks" width="540" height="1173" loading="lazy">
    <img src="img/shot-7.webp" alt="Seven worlds" width="540" height="1173" loading="lazy">
    <img src="img/shot-8.webp" alt="Fly them home" width="540" height="1173" loading="lazy">
  </div>
</div></section>

<section><div class="wrap">
  <div class="help">
    <a class="card reveal" href="support.html"><b>Support</b><span>Restore Plus, co-op tips and progress questions.</span></a>
    <a class="card reveal" href="privacy.html"><b>Privacy</b><span>No accounts, no user database. Temporary co-op rooms.</span></a>
    <a class="card reveal" href="join.html"><b>Join a room</b><span>Got an invite link? Open it here.</span></a>
  </div>
</div></section>
{contact("Pip &amp; Pals")}
"""


def doc(title, inner):
    return f'<div class="wrap"><article class="doc card">{inner.strip()}</article></div>'


LOOM_SUPPORT = f"""
<h1>Support</h1>
<p>Questions, bugs or ideas? Email us at <a href="mailto:{EMAIL}">{EMAIL}</a>. Please tell us your device, iOS version and the level you were playing.</p>
<h2>Restore my No Ads purchase</h2>
<p>Open the shop and tap “Restore Purchases”. Use the same Apple ID you bought it with. Coin packs are consumable and cannot be restored.</p>
<h2>I bought coins but didn’t get them</h2>
<p>Close and reopen the game while online; pending purchases are delivered on launch. If they still don’t arrive, email us with the date of the purchase.</p>
<h2>My progress is gone</h2>
<p>Progress is saved on your device and, when iCloud is on for your Apple ID, backed up to your iCloud. Sign in with the same Apple ID on your new phone and open the game.</p>
<h2>Change my ad privacy choices</h2>
<p>In the EEA, UK and Switzerland, open Settings in the game and tap “Privacy Choices”. Tracking permission can be changed in iOS Settings → Privacy &amp; Security → Tracking.</p>
<h2>Request a refund</h2>
<p>Purchases are handled by Apple: visit <a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>.</p>
<p style="margin-top:28px"><a class="btn ghost small" href="privacy.html">Privacy Policy</a> <a class="btn ghost small" href="./">Loom Pop! home</a></p>
"""

LOOM_PRIVACY = f"""
<h1>Privacy Policy</h1>
<p><small>Loom Pop! · Last updated: October 15, 2026 · Developer: SefyStudio · Contact: <a href="mailto:{EMAIL}">{EMAIL}</a></small></p>
<h2>The short version</h2>
<p>There are no accounts and no sign-up. We do not run servers or a user database, and we do not collect your name, email or contacts. Your progress stays on your device (and in your own iCloud). The game shows ads through Google AdMob unless you buy No Ads.</p>
<h2>What stays on your device</h2>
<p>Your progress (levels, coins, boosters, woven pieces, settings) is stored on your device. We cannot see it. Game statistics used to balance the game are only logged on your device and are not sent to us.</p>
<h2>iCloud backup</h2>
<p>If iCloud is on for your Apple ID, the game backs up your progress to your private iCloud storage (iCloud key-value storage) so you can continue on a new device. This data is stored by Apple under your Apple ID and is governed by Apple’s privacy policy. We cannot access it.</p>
<h2>Ads (Google AdMob)</h2>
<p>The game shows rewarded videos (only when you choose to watch one) and occasional full-screen ads between levels, served by Google AdMob. Google and its partners may collect and use your device’s advertising identifier (IDFA), IP address, approximate (coarse) location, ad interaction data and diagnostic data (such as crash and performance data) to deliver, measure and, with your permission, personalize ads and to prevent fraud. See <a href="https://policies.google.com/technologies/partner-sites">how Google uses information from apps that use its services</a> and <a href="https://policies.google.com/privacy">Google’s Privacy Policy</a>.</p>
<p><b>Consent (EEA, UK, Switzerland).</b> Where required, a consent form from Google’s User Messaging Platform (UMP) asks for your choices before ads load. You can change them at any time in the game: Settings → Privacy Choices.</p>
<p><b>Tracking permission (App Tracking Transparency).</b> iOS asks whether the app may track you across other companies’ apps and websites. If you decline, the advertising identifier is not shared and you see non-personalized ads. You can change this in iOS Settings → Privacy &amp; Security → Tracking.</p>
<h2>Purchases</h2>
<p>Coin packs and the No Ads purchase are handled entirely by Apple through the App Store (StoreKit). We never see your payment details or your Apple ID. The game only learns which product was bought, so it can deliver coins or remove ads. With No Ads, no ads are shown and rewards are given without videos.</p>
<h2>Sharing pictures</h2>
<p>When you share a woven piece or your album, the game creates a picture and hands it to the iOS share sheet. Nothing is uploaded by us; the app you choose to share with handles it.</p>
<h2>Children</h2>
<p>Loom Pop! is a general-audience game and is not directed to children under 13. We do not knowingly collect personal information from children. If you believe a child has given us personal information, contact us and we will help remove it.</p>
<h2>Your rights</h2>
<p>Because we do not keep personal data about you, there is usually nothing for us to export or delete. To reset on-device data, delete the app (and, if you want, its iCloud data in iOS Settings → [your name] → iCloud → Manage Storage). For ad data held by Google, use your ad choices above or Google’s privacy tools. For any privacy question or request, email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<h2>Changes</h2>
<p>If this policy changes, we will update the date above.</p>
<p style="margin-top:28px"><a class="btn ghost small" href="support.html">Support</a> <a class="btn ghost small" href="./">Loom Pop! home</a></p>
"""

# ───────────────────────── Mix Bar ─────────────────────────
MIX = f"""
<section class="ghero"><div class="wrap">
  <div class="panel card">
    <div class="art"><img src="/assets/mix-bar-art.webp" alt="The Mix Bar logo between glasses of soda" width="1600" height="600"></div>
    <div class="info">
      <img class="icon" src="/assets/mix-bar-icon.png" alt="Mix Bar app icon" width="224" height="224">
      <div>
        <h1>Mix Bar <span>Water Sort Puzzle</span></h1>
        <p class="tagline">Pour, mix and serve! A water sort puzzle with a twist: flavours mix when you pour them. Cherry on Lemonade makes Orange, and every full glass goes to the customer who ordered it.</p>
        <div class="meta"><span class="chip">Free</span><span class="chip">iPhone</span><span class="chip">10 languages</span><span class="chip">Plays offline</span></div>
      </div>
      <div class="actions"><span class="btn ghost small" aria-disabled="true">Coming soon to the App Store</span></div>
    </div>
  </div>
</div></section>

<section><div class="wrap">
  <div class="help">
    <a class="card reveal" href="support.html"><b>Support</b><span>How to play, purchases, progress and ad choices.</span></a>
    <a class="card reveal" href="privacy.html"><b>Privacy</b><span>No accounts, no user database. Ads by Google AdMob.</span></a>
  </div>
</div></section>
{contact("Mix Bar")}
"""

MIX_SUPPORT = f"""
<h1>Support</h1>
<p>Something not working, an idea, or a level you love? Email <a href="mailto:{EMAIL}">{EMAIL}</a> (please add your iPhone model and the level number). We answer within a few days.</p>
<h2>How do I play?</h2>
<p>Tap a glass, then tap another glass to pour. A glass full of one flavour goes to the customer who ordered it. Pour Cherry onto Lemonade for Orange, Lemonade onto Blue Fizz for Kiwi, Cherry onto Blue Fizz for Grape. Milk and Cola never mix. Drinks mix only when you pour.</p>
<h2>“Wrong mix!”, what now?</h2>
<p>When a level can no longer be finished, the bar at the bottom offers Rewind (back three pours), Undo, or a free Restart.</p>
<h2>I bought something but did not get it</h2>
<p>Open the Shop and tap “Restore Purchases” at the bottom. Coin packs are delivered once per purchase; No Ads and the Starter Pack restore on every device with the same Apple Account.</p>
<h2>My progress on a new phone</h2>
<p>Turn on iCloud for your Apple Account before you open the game on the new phone; your levels, stars and bar come back automatically.</p>
<h2>Change my ad privacy choices</h2>
<p>In the EEA, UK and Switzerland, open Settings in the game and tap “Privacy Choices”. Tracking permission can be changed in iOS Settings → Privacy &amp; Security → Tracking.</p>
<h2>Request a refund</h2>
<p>Purchases are handled by Apple: visit <a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>.</p>
<p style="margin-top:28px"><a class="btn ghost small" href="privacy.html">Privacy Policy</a> <a class="btn ghost small" href="./">Mix Bar home</a></p>
"""

MIX_PRIVACY = f"""
<h1>Privacy Policy</h1>
<p><small>Mix Bar: Water Sort Puzzle · Last updated: October 18, 2026 · Developer: SefyStudio · Contact: <a href="mailto:{EMAIL}">{EMAIL}</a></small></p>
<h2>The short version</h2>
<p>There are no accounts and no sign-up. We do not run a user database. Your progress stays on your device (and in your own iCloud, if it is on). The free version shows ads through Google AdMob.</p>
<h2>What stays on your device</h2>
<p>Your progress (levels, stars, coins, boosters, your bar, settings) is stored on your device. We cannot see it. Deleting the app deletes it.</p>
<h2>iCloud backup</h2>
<p>If iCloud is on for your Apple Account, the game keeps the same progress in your private iCloud storage (iCloud key-value storage) so a new phone can continue where you left off. This data is stored by Apple under your Apple Account and governed by Apple’s privacy policy. We cannot access it.</p>
<h2>Anonymous game statistics</h2>
<p>To balance the levels we may count anonymous game events (for example: a level was started, won or lost, a booster or ad was used, a purchase was made). They carry a random number made on your device, never your name, email, advertising ID or location, and they are not used for advertising or shared with advertisers. They are processed by TelemetryDeck, a privacy-focused analytics service in the EU.</p>
<h2>Ads (Google AdMob)</h2>
<p>The game shows rewarded videos (only when you choose to watch one) and occasional full-screen ads between levels, served by Google AdMob. Google and its partners may collect and use your device’s advertising identifier (IDFA), IP address, approximate (coarse) location, ad interaction data and diagnostic data (such as crash and performance data) to deliver, measure and, with your permission, personalize ads and to prevent fraud. See <a href="https://policies.google.com/technologies/partner-sites">how Google uses information from apps that use its services</a> and <a href="https://policies.google.com/privacy">Google’s Privacy Policy</a>.</p>
<p><b>Consent (EEA, UK, Switzerland).</b> Where required, a consent form from Google’s User Messaging Platform (UMP) asks for your choices before ads load. You can change them at any time in the game: Settings → Privacy Choices.</p>
<p><b>Tracking permission (App Tracking Transparency).</b> iOS asks whether the app may track you across other companies’ apps and websites. If you decline, the advertising identifier is not shared and you see non-personalized ads. You can change this in iOS Settings → Privacy &amp; Security → Tracking.</p>
<h2>Purchases</h2>
<p>Coin packs, the Starter Pack and No Ads are bought through the Apple App Store (StoreKit). We never see your payment details or your Apple Account. The game only learns which product was bought, so it can deliver it.</p>
<h2>Game Center and reminders</h2>
<p>If you are signed in to Game Center, the game reports achievements and scores to Apple’s Game Center (Apple’s privacy policy applies). Reminders are local notifications scheduled on your device; nothing is sent to a server.</p>
<h2>Children</h2>
<p>Mix Bar is a general-audience game and is not directed to children under 13. We do not knowingly collect personal information from children. If you believe a child has given us personal information, contact us and we will help remove it.</p>
<h2>Your rights</h2>
<p>Because we do not keep personal data that identifies you, there is usually nothing for us to export or delete. To reset your progress, delete the app (and, if you want, its iCloud data in iOS Settings → [your name] → iCloud → Manage Storage). For ad data held by Google, use your ad choices above or Google’s privacy tools. For any privacy question or request, email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<h2>Changes</h2>
<p>If this policy changes, we will update the date above.</p>
<p style="margin-top:28px"><a class="btn ghost small" href="support.html">Support</a> <a class="btn ghost small" href="./">Mix Bar home</a></p>
"""

PIP_SUPPORT = f"""
<h1>Support</h1>
<p>Questions, bugs or ideas? Email us at <a href="mailto:{EMAIL}">{EMAIL}</a>. Please tell us your device and OS version.</p>
<h2>Restore my Plus purchase</h2>
<p>Open the shop, tap the Plus card, then “Restore purchase”. Use the same Apple ID / Google account you bought it with.</p>
<h2>My progress is gone</h2>
<p>Progress is stored on your device only. Reinstalling the app or switching phones starts fresh. In the browser version, progress is kept in that browser; clearing site data resets it.</p>
<h2>Co-op won’t connect</h2>
<p>Every player needs an internet connection and the same 4-letter room code. App and browser players can share a room.</p>
<p style="margin-top:28px"><a class="btn ghost small" href="privacy.html">Privacy Policy</a> <a class="btn ghost small" href="./">Pip &amp; Pals home</a></p>
"""

PIP_PRIVACY = f"""
<h1>Privacy Policy</h1>
<p><small>Pip &amp; Pals: Hide &amp; Seek · Last updated: October 6, 2026 · Developer: SefyStudio · Contact: <a href="mailto:{EMAIL}">{EMAIL}</a></small></p>
<h2>The short version</h2>
<p>There are no accounts and no sign-up. We do not run a user database. Your game progress stays on your device. The game shows ads (through Google AdMob) in the free version.</p>
<h2>What stays on your device</h2>
<p>Your progress (levels, stars, coins, hats and skins, settings) and the player name you choose are stored only on your device. We cannot see them. If you delete the app, this data is deleted with it.</p>
<h2>Co-op with friends</h2>
<p>In online co-op, the game sends your chosen character, player name and in-game movement to the friends in your room through a small relay server. Rooms are temporary: nothing is saved, and the data is discarded when the room closes. Player names are filtered for inappropriate words. Please do not use your real full name or personal details as a player name.</p>
<h2>Ads</h2>
<p>The free version shows ads served by Google AdMob. AdMob and its partners may collect and use device identifiers (such as the advertising ID), IP address, approximate location and ad interaction data to deliver and measure ads, and, with your permission, to personalize them. On iOS the app asks for your permission before tracking (App Tracking Transparency). Where required (EEA, UK, Switzerland), a consent form lets you accept, reject or manage your choices. You can change your choices in your device settings (iOS: Settings → Privacy &amp; Security → Tracking; Android: Settings → Privacy → Ads). See <a href="https://policies.google.com/technologies/partner-sites">how Google uses data</a>.</p>
<h2>Purchases</h2>
<p>The optional “Pip &amp; Pals Plus” purchase is handled entirely by the Apple App Store or Google Play. We never see your payment details. We only learn whether the purchase was made, so we can unlock Plus.</p>
<h2>Game Center</h2>
<p>On iOS, if you are signed in to Game Center, the game reports achievements and scores to Apple’s Game Center. This is governed by Apple’s privacy policy.</p>
<h2>Children</h2>
<p>Pip &amp; Pals is a general-audience game and is not directed to children under 13. We do not knowingly collect personal information from children. If you believe a child has given us personal information, contact us and we will delete it.</p>
<h2>Your rights</h2>
<p>Because we do not keep personal data about you, there is usually nothing for us to delete or export. To reset on-device data, delete the app. For any privacy question or request, email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<h2>Changes</h2>
<p>If this policy changes, we will update the date above.</p>
<p style="margin-top:28px"><a class="btn ghost small" href="support.html">Support</a> <a class="btn ghost small" href="./">Pip &amp; Pals home</a></p>
"""

PIP_JOIN = f"""
<h1>Join my Pip &amp; Pals game!</h1>
<p>Your friend saved you a seat. Here is the room code:</p>
<div class="room-code" id="code">····</div>
<div class="actions-row">
  <a class="btn primary" id="open" href="pippals://join">Open in the app</a>
  <a class="btn ghost" id="web" href="play/">{PLAY} Join in the browser</a>
</div>
<p><small>Have the app? Tap “Open in the app”. If nothing happens, open Pip &amp; Pals, tap <b>Play with friends → Join</b> and type the code. No app? Join in the browser, or get it free on the <a href="{PIP_STORE}">App Store</a>.</small></p>
<script>
(function () {{
  var m = /[?&#](?:join|code)=([A-Za-z0-9]{{4}})/.exec(location.hash + location.search), c = m ? m[1].toUpperCase() : '';
  if (c) {{ document.getElementById('code').textContent = c; document.getElementById('open').href = 'pippals://join?code=' + c; document.getElementById('web').href = 'play/#join=' + c; }}
  else document.getElementById('open').hidden = true;
}})();
</script>
"""

BRAND = """
<h1>Brand assets</h1>
<p>Logos and icons of SefyStudio for press and partners. Please keep the colours and proportions as they are.</p>
<div class="brand-grid">
  <a class="card" href="/assets/brand/sefystudio-logo-horizontal.svg"><img src="/assets/brand/sefystudio-logo-horizontal.svg" alt="Horizontal logo"><span>Horizontal logo · SVG</span></a>
  <a class="card dark" href="/assets/brand/sefystudio-logo-horizontal-white.svg"><img src="/assets/brand/sefystudio-logo-horizontal-white.svg" alt="Horizontal logo, white"><span>For dark backgrounds · SVG</span></a>
  <a class="card" href="/assets/brand/sefystudio-logo.png"><img src="/assets/brand/sefystudio-logo.png" alt="Stacked logo"><span>Stacked logo · PNG</span></a>
  <a class="card" href="/assets/brand/sefy-avatar.png"><img src="/assets/brand/sefy-avatar.png" alt="Avatar" style="border-radius:50%;max-width:180px;margin:auto"><span>Avatar · PNG</span></a>
</div>
<h2>Colours</h2>
<p>Violet #7B44FF · Orange #FFA23A · Sunny #FFC765 · Deep Blue #3F3BF2 · Ink #14101F · Paper #F7F5FF</p>
"""

NOTFOUND = """
<div class="wrap"><article class="doc card" style="text-align:center">
  <img src="/assets/brand/sefy-mascot.svg" alt="" width="200" height="190" style="margin:0 auto 12px;width:200px">
  <h1>Oops, a dropped stitch!</h1>
  <p>The page you were looking for could not be found.</p>
  <p style="margin-top:22px"><a class="btn primary" href="/">Back to SefyStudio</a></p>
</article></div>
"""

PUBLISHER_PRIVACY = f"""
<h1>Privacy Policy</h1>
<p><small>SefyStudio Publisher · Last updated: October 20, 2026 · Developer: SefyStudio · Contact: <a href="mailto:{EMAIL}">{EMAIL}</a></small></p>
<p>SefyStudio Publisher is an internal tool run by SefyStudio. It posts SefyStudio’s own videos and posts to SefyStudio’s own accounts on YouTube, Instagram and X. It has no public users, no sign-up and no other customers.</p>
<h2>What the tool accesses</h2>
<p>Only the SefyStudio accounts that the studio owner has connected. For YouTube, the tool uses the <code>youtube.upload</code> permission to upload videos to SefyStudio’s own channel. For Instagram and X, it uses the permissions needed to read basic account information and publish SefyStudio’s own content.</p>
<h2>What we store</h2>
<p>Access tokens for these accounts are kept as encrypted environment secrets in our own production environment. They are never shared, sold or written into code, logs or public files. Videos waiting to be published are kept briefly in our own cloud storage and deleted after publishing.</p>
<h2>What we do not do</h2>
<p>We do not collect personal data about anyone else, and we do not sell or share data with third parties. We do not use data from Google APIs for advertising.</p>
<h2>Google API Services</h2>
<p>SefyStudio Publisher’s use of information received from Google APIs adheres to the <a href="https://developers.google.com/terms/api-services-user-data-policy">Google API Services User Data Policy</a>, including the Limited Use requirements.</p>
<p>SefyStudio Publisher uses YouTube API Services. By using it you agree to be bound by the <a href="https://www.youtube.com/t/terms">YouTube Terms of Service</a>; see the <a href="https://policies.google.com/privacy">Google Privacy Policy</a> for how Google handles data.</p>
<h2>Removing access</h2>
<p>Access can be withdrawn at any time from the connected account’s security settings (for Google: <a href="https://myaccount.google.com/permissions">myaccount.google.com/permissions</a>). Stored tokens are then deleted from our environment.</p>
<h2>Changes</h2>
<p>If this policy changes, we will update the date above.</p>
<p style="margin-top:28px"><a class="btn ghost small" href="/terms.html">Terms of Service</a> <a class="btn ghost small" href="/">SefyStudio home</a></p>
"""

PUBLISHER_TERMS = f"""
<h1>Terms of Service</h1>
<p><small>SefyStudio Publisher · Last updated: October 20, 2026 · Developer: SefyStudio · Contact: <a href="mailto:{EMAIL}">{EMAIL}</a></small></p>
<p>SefyStudio Publisher is an internal tool that publishes SefyStudio’s own content to SefyStudio’s own accounts on YouTube, Instagram and X. It is not offered to the public, and no one outside SefyStudio can sign in to it.</p>
<h2>Use</h2>
<p>The tool is used only by SefyStudio, only for its own accounts, and in line with the terms of each platform, including the <a href="https://www.youtube.com/t/terms">YouTube Terms of Service</a> and the <a href="https://developers.google.com/youtube/terms/api-services-terms-of-service">YouTube API Services Terms of Service</a>.</p>
<h2>Content</h2>
<p>SefyStudio is responsible for everything the tool publishes. The tool publishes only content SefyStudio has made or has the rights to use.</p>
<h2>No warranty</h2>
<p>The tool is provided as is, for SefyStudio’s internal use.</p>
<p style="margin-top:28px"><a class="btn ghost small" href="/privacy.html">Privacy Policy</a> <a class="btn ghost small" href="/">SefyStudio home</a></p>
"""

if __name__ == "__main__":
    page("/", "SefyStudio", "SefyStudio is an independent studio making cozy games and apps: Loom Pop!, Pip & Pals: Hide & Seek and Mix Bar.", HOME)
    page("/loom-pop/", "Loom Pop! Yarn Sort Puzzle", "A cozy yarn-sorting puzzle for iPhone. Tap yarn balls, fill the loom and weave 200+ colourful patterns.", LOOM,
         game="loom", current="loom", image="/assets/loom-pop-art.webp", icon="/assets/loom-pop-icon.png", extra='<meta name="apple-itunes-app" content="app-id=6822636298">\n')
    page("/pip-and-pals/", "Pip & Pals: Hide & Seek", "Hide from the drones, finish the tasks and fix the rocket, alone or with friends. Play free in your browser or on iPhone and iPad.", PIP,
         game="pip", current="pip", image="/assets/pip-and-pals-art.webp", icon="/assets/pip-and-pals-icon.png", extra='<meta name="apple-itunes-app" content="app-id=6819880110">\n')
    page("/loom-pop/support.html", "Loom Pop! Support", "Help with Loom Pop!: purchases, progress and ad choices.", doc("", LOOM_SUPPORT), game="loom", current="loom", icon="/assets/loom-pop-icon.png")
    page("/loom-pop/privacy.html", "Loom Pop! Privacy Policy", "Privacy policy of Loom Pop! by SefyStudio.", doc("", LOOM_PRIVACY), game="loom", current="loom", icon="/assets/loom-pop-icon.png")
    page("/mix-bar/", "Mix Bar: Water Sort Puzzle", "Pour, mix and serve: a water sort puzzle where flavours mix when you pour them. Free for iPhone.", MIX,
         current="mix", image="/assets/mix-bar-art.webp", icon="/assets/mix-bar-icon.png")
    page("/mix-bar/support.html", "Mix Bar Support", "Help with Mix Bar: how to play, purchases, progress and ad choices.", doc("", MIX_SUPPORT), current="mix", icon="/assets/mix-bar-icon.png")
    page("/mix-bar/privacy.html", "Mix Bar Privacy Policy", "Privacy policy of Mix Bar: Water Sort Puzzle by SefyStudio.", doc("", MIX_PRIVACY), current="mix", icon="/assets/mix-bar-icon.png")
    # the first Mix Bar build links /mix-bar/support/ and /mix-bar/privacy/: forward them
    for old in ("support", "privacy"):
        os.makedirs(os.path.join(ROOT, "mix-bar", old), exist_ok=True)
        with open(os.path.join(ROOT, "mix-bar", old, "index.html"), "w", encoding="utf-8") as f:
            f.write(f'<!doctype html><meta charset="utf-8"><title>Mix Bar</title><link rel="canonical" href="/mix-bar/{old}.html">'
                    f'<meta http-equiv="refresh" content="0; url=/mix-bar/{old}.html"><a href="/mix-bar/{old}.html">Mix Bar {old}</a>')
    page("/pip-and-pals/support.html", "Pip & Pals Support", "Help with Pip & Pals: purchases, progress and co-op.", doc("", PIP_SUPPORT), game="pip", current="pip", icon="/assets/pip-and-pals-icon.png")
    page("/pip-and-pals/privacy.html", "Pip & Pals Privacy Policy", "Privacy policy of Pip & Pals: Hide & Seek by SefyStudio.", doc("", PIP_PRIVACY), game="pip", current="pip", icon="/assets/pip-and-pals-icon.png")
    page("/pip-and-pals/join.html", "Join a Pip & Pals room", "Your friend invited you to a Pip & Pals co-op room.", doc("", PIP_JOIN), game="pip", current="pip",
         image="/assets/pip-and-pals-art.webp", icon="/assets/pip-and-pals-icon.png")
    # SefyStudio Publisher (our own posting tool): the Google / Meta consent screens link these
    page("/privacy.html", "Privacy Policy · SefyStudio Publisher", "Privacy policy of SefyStudio Publisher, SefyStudio's internal publishing tool.", doc("", PUBLISHER_PRIVACY))
    page("/terms.html", "Terms of Service · SefyStudio Publisher", "Terms of service of SefyStudio Publisher, SefyStudio's internal publishing tool.", doc("", PUBLISHER_TERMS))
    page("/brand/", "Brand assets · SefyStudio", "SefyStudio logos and icons for press and partners.", doc("", BRAND))
    page("/404.html", "Page not found · SefyStudio", "This page could not be found.", NOTFOUND)
