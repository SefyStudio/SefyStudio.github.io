#!/usr/bin/env python3
"""Builds every page of the SefyStudio site from one template, styled by assets/site.css (cozy studio look, 2026-11-04:
cream paper, warm ink outlines, Fredoka type and colour wave bands, the same language as Loom Pop! and Mix Bar).

    python3 _build.py

Edit the page bodies below, never the generated .html files. Files starting with "_" are not published by GitHub Pages.
Pip & Pals left the site on 2026-11-04; only its privacy, support and join pages stay (unlisted) because the app links them.
"""
import hashlib
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = "https://sefystudio.com"
EMAIL = "support@sefystudio.com"
LOOM_STORE = "https://apps.apple.com/app/id6822636298"
PIP_STORE = "https://apps.apple.com/app/id6819880110"
MIX_STORE = "https://apps.apple.com/app/id6823995084"
MIX_LIVE = False  # Mix Bar is in App Review: the store badge says "coming soon" until it is live
APPLE = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M16.4 12.6c0-2.4 2-3.6 2.1-3.7-1.2-1.7-3-1.9-3.6-2'
         '-1.5-.2-3 .9-3.8.9-.8 0-2-.9-3.3-.9-1.7 0-3.3 1-4.1 2.5-1.8 3.1-.5 7.6 1.3 10.1.8 1.2 1.8 2.6 3.1 2.5 1.2 0 1.7-.8 3.2-.8s1.9.8 '
         '3.2.8c1.3 0 2.2-1.2 3-2.4.9-1.4 1.3-2.7 1.3-2.8 0 0-2.4-1-2.4-4.2zM14 5.4c.7-.8 1.1-1.9 1-3-1 0-2.1.7-2.8 1.5-.6.7-1.2 1.8-1 2.9 '
         '1 .1 2.1-.6 2.8-1.4z"/></svg>')
PLAY = '<svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path fill="currentColor" d="M8 5.5v13l10.5-6.5z"/></svg>'
SPARK = '<svg class="spark" viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1 Q11.6 8.4 19 10 Q11.6 11.6 10 19 Q8.4 11.6 1 10 Q8.4 8.4 10 1Z"/></svg>'


def ver(rel):
    """Cache-busting query from the file's content, so browsers pick up CSS/JS changes at once."""
    return hashlib.sha1(open(os.path.join(ROOT, rel), "rb").read()).hexdigest()[:8]


def store(url, live=True, small=False):
    if not live:
        return (f'<span class="btn store soon{" small" if small else ""}" aria-disabled="true">{APPLE}'
                '<span><small>Coming soon to the</small>App Store</span></span>')
    return (f'<a class="btn store{" small" if small else ""}" href="{url}">{APPLE}'
            '<span><small>Download on the</small>App Store</span></a>')


def band(cls, inner, sparks=True):
    """A colour wave band with soft stripes and an ink edge, like the store art of our games."""
    s = (f'<i class="sp s1">{SPARK}</i><i class="sp s2">{SPARK}</i><i class="sp s3">{SPARK}</i><i class="sp s4">{SPARK}</i>' if sparks else "")
    return f'<div class="band {cls}">{s}{inner}<svg class="wave" viewBox="0 0 1440 60" preserveAspectRatio="none" aria-hidden="true"><path class="fill" d="M0 24 C240 62 480 56 720 30 S1200 64 1440 22 V60 H0 Z"/><path class="edge" d="M0 24 C240 62 480 56 720 30 S1200 64 1440 22"/></svg></div>'


def page(path, title, desc, body, game=None, current=None, image="/assets/brand/og-image.png", icon=None, extra="", noindex=False):
    links = [("/#games", "Games", "games"), ("/loom-pop/", "Loom Pop!", "loom"), ("/mix-bar/", "Mix Bar", "mix"),
             ("/#about", "About", "about"), ("/#contact", "Contact", "contact")]
    icons = (f'<link rel="icon" href="{icon}">\n<link rel="apple-touch-icon" href="{icon}">' if icon else
             '<link rel="icon" href="/favicon.ico" sizes="48x48">\n<link rel="icon" type="image/png" sizes="192x192" href="/assets/brand/favicon-192.png">\n'
             '<link rel="apple-touch-icon" href="/assets/brand/apple-touch-icon.png">')
    nav = "".join(f'<a href="{h}"{" aria-current=" + chr(34) + "page" + chr(34) if k == current else ""}>{t}</a>' for h, t, k in links)
    robots = '<meta name="robots" content="noindex">\n' if noindex else ""
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
{robots}<meta name="theme-color" content="#fff6ea">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE}{image}">
<meta property="og:url" content="{SITE}{path}">
<meta name="twitter:card" content="summary_large_image">
{icons}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&amp;family=Nunito:wght@500;600;700;800&amp;display=swap">
<link rel="stylesheet" href="/assets/site.css?v={ver('assets/site.css')}">
{extra}</head>
<body{f' data-game="{game}"' if game else ""}>
<header class="nav"><div class="wrap bar">
  <a class="logo" href="/"><img src="/assets/brand/sefystudio-logo-horizontal.svg" alt="SefyStudio" width="300" height="96"></a>
  <button class="menu" type="button" aria-label="Menu" aria-expanded="false"><i></i><i></i></button>
  <nav aria-label="Main">{nav}</nav>
</div></header>
<main>
{body.strip()}
</main>
<footer><div class="wrap">
  <div class="cols">
    <div class="brand"><a class="logo" href="/"><img src="/assets/brand/sefystudio-logo-horizontal.svg" alt="SefyStudio" width="300" height="96"></a>
      <p>A small independent studio making cozy games for iPhone.</p></div>
    <div><h4>Loom Pop!</h4><ul><li><a href="/loom-pop/">Overview</a></li><li><a href="{LOOM_STORE}">App Store</a></li>
      <li><a href="/loom-pop/support.html">Support</a></li><li><a href="/loom-pop/privacy.html">Privacy</a></li></ul></div>
    <div><h4>Mix Bar</h4><ul><li><a href="/mix-bar/">Overview</a></li>{f'<li><a href="{MIX_STORE}">App Store</a></li>' if MIX_LIVE else ''}
      <li><a href="/mix-bar/support.html">Support</a></li><li><a href="/mix-bar/privacy.html">Privacy</a></li></ul></div>
    <div><h4>Studio</h4><ul><li><a href="/#about">About</a></li><li><a href="/#contact">Contact</a></li><li><a href="https://www.youtube.com/@sefystudio">YouTube</a></li>
      <li><a href="/brand/">Brand assets</a></li><li><a href="/app-ads.txt">app-ads.txt</a></li></ul></div>
  </div>
  <p class="legal">© <span id="year">2026</span> SefyStudio · <a href="/privacy.html">Privacy</a> · <a href="/terms.html">Terms</a><br>Apple, the Apple logo and iPhone are trademarks of Apple Inc. App Store is a service mark of Apple Inc.</p>
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
    <div><h2>Say hello</h2><p>{what}Ideas, bugs, press or partnerships: we read every email and answer within a day or two.</p></div>
    <div class="copy-row"><a class="mail" href="mailto:{EMAIL}">{EMAIL}</a><button class="btn primary" type="button" data-copy="{EMAIL}">Copy email</button></div>
  </div>
</div></section>"""


def rail(folder, alts):
    return '<div class="rail reveal" tabindex="0" aria-label="Screenshots">' + "".join(
        f'<img src="/{folder}/img/shot-{i + 1}.webp" alt="{a}" width="660" height="1434" loading="lazy">' for i, a in enumerate(alts)) + "</div>"


LOOM_ALTS = ["Aim, pop and weave", "Fever combos", "Weave cozy patterns", "Happy customers", "200 patterns to collect", "Your cozy yarn shop"]
MIX_ALTS = ["Sort and mix drinks", "Serve every order", "Chain big combos", "Plan every pour", "Build your diner", "Open new places", "Top of the town", "Hundreds of levels"]

GAMES = [
    dict(cls="loom", name="Loom Pop!", sub="Yarn Ball Shooter", page="/loom-pop/", icon="/loom-pop/img/icon.png", shot="/loom-pop/img/shot-1.webp",
         text="Aim, pop and weave. Match three yarn balls and every pop knits a cozy picture on the loom, stitch by stitch.",
         chips=["Puzzle", "200 patterns", "Free"], cta=store(LOOM_STORE, small=True)),
    dict(cls="mix", name="Mix Bar", sub="Water Sort Puzzle", page="/mix-bar/", icon="/mix-bar/img/icon.png", shot="/mix-bar/img/shot-1.webp",
         text="Pour, mix and serve. Cherry on lemonade makes orange, and every full glass goes to the customer who ordered it.",
         chips=["Puzzle", "Hundreds of levels", "Free"], cta=store(MIX_STORE, MIX_LIVE, small=True)),
]


def game_card(g):
    chips = "".join(f'<span class="chip">{c}</span>' for c in g["chips"])
    return f"""<article class="game card reveal {g['cls']}">
      {band(g['cls'], f'<a class="shot" href="{g["page"]}"><img src="{g["shot"]}" alt="{g["name"]} screenshot" width="660" height="1434" loading="lazy"></a>')}
      <div class="body">
        <img class="icon" src="{g['icon']}" alt="{g['name']} app icon" width="96" height="96" loading="lazy">
        <div><h3>{g['name']}</h3><p class="sub">{g['sub']}</p></div>
      </div>
      <p>{g['text']}</p>
      <div class="chips">{chips}</div>
      <div class="cta">{g['cta']}<a class="btn ghost small" href="{g['page']}">See the game</a></div>
    </article>"""


HOME = f"""
<section class="hero">
  {band("home", f'''<div class="wrap hero-grid">
    <div class="hero-copy">
      <p class="kicker">SefyStudio</p>
      <h1>Cozy little games,<br>made with care.</h1>
      <p class="lead">We are a small independent studio. Our puzzles are calm, fair and full of tiny details. No accounts, no pressure, in ten languages.</p>
      <div class="actions"><a class="btn primary" href="#games">Meet our games</a><a class="btn ghost light" href="#about">About us</a></div>
    </div>
    <div class="hero-shots" aria-hidden="true">
      <img class="ph a" src="/loom-pop/img/shot-1.webp" alt="" width="660" height="1434">
      <img class="ph b" src="/mix-bar/img/shot-1.webp" alt="" width="660" height="1434">
    </div>
  </div>''')}
</section>

<section id="games"><div class="wrap">
  <div class="section-head reveal"><h2>Our games</h2><p>Two puzzles for iPhone, both free to play.</p></div>
  <div class="games">{"".join(game_card(g) for g in GAMES)}</div>
</div></section>

<section id="about"><div class="wrap">
  <div class="about card reveal">
    <img class="mascot" src="/assets/brand/sefy-mascot.svg" alt="Sefy, the SefyStudio mascot" width="220" height="220" loading="lazy">
    <div>
      <h2>Small studio, big care</h2>
      <p class="lead">We make the kind of games we like to play on the sofa: soft colours, gentle sounds and puzzles that respect your time.</p>
    </div>
  </div>
  <div class="tiles">
    <div class="tile card reveal"><b>10</b><h3>languages</h3><p>English, Türkçe, Español, Português, Deutsch, Français, Italiano, 日本語 and 한국어.</p></div>
    <div class="tile card reveal"><b>0</b><h3>accounts</h3><p>No sign-up and no user database. Your progress stays on your device and in your own iCloud.</p></div>
    <div class="tile card reveal"><b>100%</b><h3>solvable</h3><p>Every Mix Bar level is checked by a solver before it ships. Fair puzzles only.</p></div>
    <div class="tile card reveal"><b>200</b><h3>patterns</h3><p>Every motif in Loom Pop! is drawn stitch by stitch, from Kilim Classics to Sea Life.</p></div>
  </div>
</div></section>
{contact()}
"""


def game_page(cls, name, sub, tagline, live, url, video, folder, alts, features, facts, help_links):
    feats = "".join(f'<article class="feature card reveal"><img src="/{folder}/img/shot-{n}.webp" alt="{t}" width="660" height="1434" loading="lazy"><h3>{t}</h3><p>{d}</p></article>' for n, t, d in features)
    fact = "".join(f'<div class="fact"><small>{k}</small><strong>{v}</strong></div>' for k, v in facts)
    helps = "".join(f'<a class="card reveal" href="{h}"><b>{t}</b><span>{d}</span></a>' for h, t, d in help_links)
    return f"""
<section class="ghero">
  {band(cls, f'''<div class="wrap ghero-grid">
    <div class="ghero-copy">
      <img class="icon" src="/{folder}/img/icon.png" alt="{name} app icon" width="128" height="128">
      <h1>{name}</h1><p class="sub">{sub}</p>
      <p class="lead">{tagline}</p>
      <div class="actions">{store(url, live)}</div>
    </div>
    <div class="video"><video src="/{folder}/img/preview.mp4" poster="/{folder}/img/poster.jpg" muted loop playsinline autoplay preload="metadata" aria-label="{name} gameplay"></video></div>
  </div>''')}
</section>

<section><div class="wrap">
  <div class="section-head reveal"><h2>How it plays</h2></div>
  <div class="features">{feats}</div>
</div></section>

<section><div class="wrap">
  <div class="section-head reveal"><h2>Screenshots</h2></div>
  {rail(folder, alts)}
</div></section>

<section><div class="wrap">
  <div class="facts card reveal">{fact}</div>
  <div class="help">{helps}</div>
</div></section>
{contact(name)}
"""


LOOM = game_page("loom", "Loom Pop!", "Yarn Ball Shooter",
    "Shoot yarn balls into the rolling chain, match three of a colour and watch every pop race round the loom and knit a cozy picture, stitch by stitch.",
    True, LOOM_STORE, True, "loom-pop", LOOM_ALTS,
    [(1, "Aim, pop, weave", "Match three yarn balls of a colour. Each pop sends its yarn to the loom and the picture grows."),
     (2, "Fever combos", "Chain reactions pull the yarn back and pay out coins. Six in a row and Fever starts."),
     (5, "200 patterns", "Eight cozy collections, from Kilim Classics to Sea Life, all in your pattern book.")],
    [("Patterns", "200 in 8 collections"), ("Device", "iPhone"), ("Price", "Free, optional No Ads"), ("Languages", "10")],
    [("support.html", "Support", "Restore No Ads, coins, progress and ad choices."), ("privacy.html", "Privacy", "No accounts, no user database. Ads by Google AdMob."),
     (LOOM_STORE, "App Store", "Free download for iPhone.")])

MIX = game_page("mix", "Mix Bar", "Water Sort Puzzle",
    "Tap a glass, then another to pour. Flavours mix when you pour them: cherry on lemonade makes orange. Fill a glass with one flavour and serve the customer who ordered it.",
    MIX_LIVE, MIX_STORE, True, "mix-bar", MIX_ALTS,
    [(1, "Sort and mix", "Pour layer onto layer. Some flavours mix into new drinks, milk and cola never do."),
     (4, "Plan every pour", "Every level has a move limit. No timers, just clever moves, and every level is solvable."),
     (5, "Build your bar", "Stars renovate the diner, then open a beach bar, an ice cream parlor and a rooftop lounge.")],
    [("Levels", "Hundreds, all solvable"), ("Device", "iPhone"), ("Price", "Free, optional No Ads"), ("Languages", "10")],
    [("support.html", "Support", "How to play, purchases, progress and ad choices."), ("privacy.html", "Privacy", "No accounts, no user database. Ads by Google AdMob."),
     ("/#contact", "Contact", "Questions or ideas? Write to us.")])


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
<p style="margin-top:28px"><a class="btn ghost small" href="privacy.html">Privacy Policy</a> <a class="btn ghost small" href="/">SefyStudio home</a></p>
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
<p style="margin-top:28px"><a class="btn ghost small" href="support.html">Support</a> <a class="btn ghost small" href="/">SefyStudio home</a></p>
"""

PIP_JOIN = f"""
<h1>Join my Pip &amp; Pals game!</h1>
<p>Your friend saved you a seat. Here is the room code:</p>
<div class="room-code" id="code">····</div>
<div class="actions-row">
  <a class="btn primary" id="open" href="pippals://join">Open in the app</a>
</div>
<p><small>Have the app? Tap “Open in the app”. If nothing happens, open Pip &amp; Pals, tap <b>Play with friends → Join</b> and type the code. No app? Get it free on the <a href="{PIP_STORE}">App Store</a>.</small></p>
<script>
(function () {{
  var m = /[?&#](?:join|code)=([A-Za-z0-9]{{4}})/.exec(location.hash + location.search), c = m ? m[1].toUpperCase() : '';
  if (c) {{ document.getElementById('code').textContent = c; document.getElementById('open').href = 'pippals://join?code=' + c; }}
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
    page("/", "SefyStudio · Cozy games for iPhone", "SefyStudio is a small independent studio making cozy puzzle games for iPhone: Loom Pop! and Mix Bar.", HOME)
    page("/loom-pop/", "Loom Pop! Yarn Ball Shooter", "Aim, pop and weave: match three yarn balls and knit 200 cozy patterns. Free for iPhone.", LOOM,
         game="loom", current="loom", image="/loom-pop/img/poster.jpg", icon="/loom-pop/img/icon-180.png", extra='<meta name="apple-itunes-app" content="app-id=6822636298">\n')
    page("/loom-pop/support.html", "Loom Pop! Support", "Help with Loom Pop!: purchases, progress and ad choices.", doc("", LOOM_SUPPORT), game="loom", current="loom", icon="/loom-pop/img/icon-180.png")
    page("/loom-pop/privacy.html", "Loom Pop! Privacy Policy", "Privacy policy of Loom Pop! by SefyStudio.", doc("", LOOM_PRIVACY), game="loom", current="loom", icon="/loom-pop/img/icon-180.png")
    page("/mix-bar/", "Mix Bar: Water Sort Puzzle", "Pour, mix and serve: a water sort puzzle where flavours mix when you pour them. Free for iPhone.", MIX,
         game="mix", current="mix", image="/mix-bar/img/poster.jpg", icon="/mix-bar/img/icon-180.png")
    page("/mix-bar/support.html", "Mix Bar Support", "Help with Mix Bar: how to play, purchases, progress and ad choices.", doc("", MIX_SUPPORT), game="mix", current="mix", icon="/mix-bar/img/icon-180.png")
    page("/mix-bar/privacy.html", "Mix Bar Privacy Policy", "Privacy policy of Mix Bar: Water Sort Puzzle by SefyStudio.", doc("", MIX_PRIVACY), game="mix", current="mix", icon="/mix-bar/img/icon-180.png")
    # the first Mix Bar build links /mix-bar/support/ and /mix-bar/privacy/: forward them
    for old in ("support", "privacy"):
        os.makedirs(os.path.join(ROOT, "mix-bar", old), exist_ok=True)
        with open(os.path.join(ROOT, "mix-bar", old, "index.html"), "w", encoding="utf-8") as f:
            f.write(f'<!doctype html><meta charset="utf-8"><title>Mix Bar</title><link rel="canonical" href="/mix-bar/{old}.html">'
                    f'<meta http-equiv="refresh" content="0; url=/mix-bar/{old}.html"><a href="/mix-bar/{old}.html">Mix Bar {old}</a>')
    # Pip & Pals: not on the site any more, but the app's listing and invite links still point here (unlisted)
    page("/pip-and-pals/support.html", "Pip & Pals Support", "Help with Pip & Pals: purchases, progress and co-op.", doc("", PIP_SUPPORT), noindex=True)
    page("/pip-and-pals/privacy.html", "Pip & Pals Privacy Policy", "Privacy policy of Pip & Pals: Hide & Seek by SefyStudio.", doc("", PIP_PRIVACY), noindex=True)
    page("/pip-and-pals/join.html", "Join a Pip & Pals room", "Your friend invited you to a Pip & Pals co-op room.", doc("", PIP_JOIN), noindex=True)
    page("/privacy.html", "Privacy Policy · SefyStudio Publisher", "Privacy policy of SefyStudio Publisher, SefyStudio's internal publishing tool.", doc("", PUBLISHER_PRIVACY))  # linked by the Google / Meta consent screens of our posting tool
    page("/terms.html", "Terms of Service · SefyStudio Publisher", "Terms of service of SefyStudio Publisher, SefyStudio's internal publishing tool.", doc("", PUBLISHER_TERMS))
    page("/brand/", "Brand assets · SefyStudio", "SefyStudio logos and icons for press and partners.", doc("", BRAND))
    page("/404.html", "Page not found · SefyStudio", "This page could not be found.", NOTFOUND)
