#!/usr/bin/env python3
"""Builds every page of the SefyStudio site (sefystudio.com) from one template, styled by assets/site.css.

    python3 _build.py

Look (2026-11-16): the "Masa" identity of DealCraft (baize table, printed paper, ink outlines, hard shadows).
Edit the page bodies here, never the generated .html files.

DealCraft pages: /dealcraft/ (EN) and /dealcraft/tr/ (TR), each with privacy, support and terms pages.
The App Store listing links: Privacy https://sefystudio.com/dealcraft/privacy.html (TR: /dealcraft/tr/gizlilik.html),
Support https://sefystudio.com/dealcraft/support.html (TR: /dealcraft/tr/destek.html), Marketing https://sefystudio.com/dealcraft/.

Loom Pop! (live), Mix Bar (in review) and Pip & Pals link their support and privacy pages on this site from their apps:
those URLs MUST keep working. Their texts live unchanged in _legacy.py; only the look changed.
Keep app-ads.txt, robots.txt and CNAME at the root.
"""
import hashlib
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _legacy as L  # noqa: E402  (texts of the earlier apps' support/privacy pages)

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = "https://sefystudio.com"
EMAIL = "support@sefystudio.com"
DEAL_STORE = "https://apps.apple.com/app/dealcraft"  # replace with https://apps.apple.com/app/id<APPLE_ID> once the app exists
DEAL_LIVE = False  # store badge says "coming soon" until DealCraft is on the App Store
UPDATED_EN = "November 16, 2026"
UPDATED_TR = "16 Kasım 2026"

APPLE = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M16.4 12.6c0-2.4 2-3.6 2.1-3.7-1.2-1.7-3-1.9-3.6-2'
         '-1.5-.2-3 .9-3.8.9-.8 0-2-.9-3.3-.9-1.7 0-3.3 1-4.1 2.5-1.8 3.1-.5 7.6 1.3 10.1.8 1.2 1.8 2.6 3.1 2.5 1.2 0 1.7-.8 3.2-.8s1.9.8 '
         '3.2.8c1.3 0 2.2-1.2 3-2.4.9-1.4 1.3-2.7 1.3-2.8 0 0-2.4-1-2.4-4.2zM14 5.4c.7-.8 1.1-1.9 1-3-1 0-2.1.7-2.8 1.5-.6.7-1.2 1.8-1 2.9 '
         '1 .1 2.1-.6 2.8-1.4z"/></svg>')


def ver(rel):
    return hashlib.sha1(open(os.path.join(ROOT, rel), "rb").read()).hexdigest()[:8]


def store(url, live=True, lang="en"):
    soon = "Yakında" if lang == "tr" else "Coming soon to the"
    get = "App Store'dan" if lang == "tr" else "Download on the"
    if not live:
        return f'<span class="btn store soon" aria-disabled="true">{APPLE}<span><small>{soon}</small>App Store</span></span>'
    return f'<a class="btn store" href="{url}">{APPLE}<span><small>{get}</small>App Store</span></a>'


def stub(text):
    return f'<div class="stub" aria-hidden="true"><span>{text}</span></div>'


NAV_EN = [("/", "Studio", "home"), ("/dealcraft/", "DealCraft", "deal"), ("/#games", "Games", "games"), ("/#contact", "Contact", "contact")]
NAV_TR = [("/", "Stüdyo", "home"), ("/dealcraft/tr/", "DealCraft", "deal"), ("/#games", "Oyunlar", "games"), ("/dealcraft/tr/destek.html", "Destek", "support")]


def page(path, title, desc, body, current=None, lang="en", image="/dealcraft/img/en-og.jpg", icon=None, noindex=False, alt=None):
    nav = "".join(f'<a href="{h}"{" aria-current=" + chr(34) + "page" + chr(34) if k == current else ""}>{t}</a>'
                  for h, t, k in (NAV_TR if lang == "tr" else NAV_EN))
    icons = (f'<link rel="icon" href="{icon}">\n<link rel="apple-touch-icon" href="{icon}">' if icon else
             '<link rel="icon" href="/favicon.ico" sizes="48x48">\n<link rel="icon" type="image/png" sizes="192x192" href="/assets/brand/favicon-192.png">\n'
             '<link rel="apple-touch-icon" href="/assets/brand/apple-touch-icon.png">')
    robots = '<meta name="robots" content="noindex">\n' if noindex else ""
    alternate = (f'<link rel="alternate" hreflang="{alt[0]}" href="{SITE}{alt[1]}">\n<link rel="alternate" hreflang="{lang}" href="{SITE}{path}">\n'
                 if alt else "")
    tagline = ("Küçük, bağımsız bir oyun stüdyosu. İyi düşünülmüş, el işi oyunlar." if lang == "tr"
               else "A small independent studio making well-crafted games for iPhone.")
    f_games, f_studio, f_legal = ("Oyunlar", "Stüdyo", "Yasal") if lang == "tr" else ("Games", "Studio", "Legal")
    deal = "/dealcraft/tr/" if lang == "tr" else "/dealcraft/"
    html = f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0a3534">
{robots}<link rel="canonical" href="{SITE}{path}">
{alternate}<meta property="og:type" content="website">
<meta property="og:site_name" content="SefyStudio">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE}{image}">
<meta property="og:url" content="{SITE}{path}">
<meta name="twitter:card" content="summary_large_image">
{icons}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wdth,wght@12..96,75..100,600..800&amp;family=Schibsted+Grotesk:wght@400;500;700&amp;family=Martian+Mono:wght@600&amp;display=swap">
<link rel="stylesheet" href="/assets/site.css?v={ver('assets/site.css')}">
</head>
<body>
<header class="nav"><div class="wrap bar">
  <a class="logo" href="/" aria-label="SefyStudio"><span class="mark" aria-hidden="true">S</span><b>Sefy<i>Studio</i></b></a>
  <button class="menu" type="button" aria-label="Menu" aria-expanded="false"><i></i><i></i></button>
  <nav aria-label="Main">{nav}</nav>
</div></header>
<main>
{body.strip()}
</main>
<footer><div class="wrap">
  <div class="cols">
    <div><a class="logo" href="/"><span class="mark" aria-hidden="true">S</span><b>Sefy<i>Studio</i></b></a>
      <p style="margin-top:12px;max-width:34ch;opacity:.85">{tagline}</p></div>
    <div><h4>DealCraft</h4><ul>
      <li><a href="{deal}">{"Tanıtım" if lang == "tr" else "Overview"}</a></li>
      <li><a href="{deal}{"destek.html" if lang == "tr" else "support.html"}">{"Destek" if lang == "tr" else "Support"}</a></li>
      <li><a href="{deal}{"gizlilik.html" if lang == "tr" else "privacy.html"}">{"Gizlilik" if lang == "tr" else "Privacy"}</a></li>
      <li><a href="{deal}{"kosullar.html" if lang == "tr" else "terms.html"}">{"Kullanım koşulları" if lang == "tr" else "Terms of use"}</a></li></ul></div>
    <div><h4>{f_games}</h4><ul><li><a href="/loom-pop/">Loom Pop!</a></li><li><a href="/mix-bar/">Mix Bar</a></li>
      <li><a href="{"/dealcraft/" if lang == "tr" else "/dealcraft/tr/"}">{"DealCraft (English)" if lang == "tr" else "DealCraft (Türkçe)"}</a></li></ul></div>
    <div><h4>{f_studio}</h4><ul><li><a href="/#about">{"Hakkında" if lang == "tr" else "About"}</a></li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
      <li><a href="/brand/">{"Marka" if lang == "tr" else "Brand assets"}</a></li><li><a href="/app-ads.txt">app-ads.txt</a></li></ul></div>
  </div>
  <p class="legal">© <span id="year">2026</span> SefyStudio · {f_legal}: <a href="/privacy.html">Publisher privacy</a> · <a href="/terms.html">Publisher terms</a><br>
  Apple, the Apple logo and iPhone are trademarks of Apple Inc. App Store is a service mark of Apple Inc. Game Center is a trademark of Apple Inc.</p>
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


def doc(inner, label="SEFYSTUDIO"):
    return f'<div class="wrap"><article class="doc paper ticket">{stub(label)}{inner.strip()}</article></div>'


def contact(lang="en"):
    h, t, b = (("Bize yaz", "Fikir, hata, basın ya da iş birliği: her e-postayı okuyoruz, genellikle bir iki gün içinde cevaplıyoruz.", "E-postayı kopyala")
               if lang == "tr" else
               ("Say hello", "Ideas, bugs, press or partnerships: we read every email and usually answer within a day or two.", "Copy email"))
    return f"""<section id="contact"><div class="wrap">
  <div class="contact paper ticket reveal">{stub("CONTACT")}
    <div><h2>{h}</h2><p style="margin:0;max-width:52ch">{t}</p></div>
    <div class="copy-row"><a class="mail" href="mailto:{EMAIL}">{EMAIL}</a><button class="btn primary" type="button" data-copy="{EMAIL}">{b}</button></div>
  </div>
</div></section>"""


# ───────────────────────── Home ─────────────────────────
HOME = f"""
<section class="hero"><div class="wrap hero-grid">
  <div>
    <p class="label" style="color:var(--pirinc)">Independent game studio</p>
    <h1>Games with a <span>craft</span> on the table.</h1>
    <p class="lead">SefyStudio is a small independent studio. We make iPhone games that are easy to pick up and worth getting good at, with real writing, real art and no tricks.</p>
    <div class="actions"><a class="btn primary" href="/dealcraft/">Meet DealCraft</a><a class="btn ghost" href="#games">All games</a></div>
  </div>
  <div class="shots-pair" aria-hidden="true">
    <img class="shot" src="/dealcraft/img/en-raw-turn.webp" alt="" width="660" height="1434">
    <img class="shot" src="/dealcraft/img/en-shot-3.webp" alt="" width="660" height="1434">
  </div>
</div></section>

<section id="games"><div class="wrap">
  <div class="section-head"><span class="label">No.01 · Games</span></div>
  <div class="games">
    <a class="game-card feature paper reveal" href="/dealcraft/">
      <img class="banner" src="/dealcraft/img/en-header.webp" alt="DealCraft: reply cards, a customer polaroid and the DealCraft ticket on a green table" width="1920" height="823">
      <div class="row ticket">{stub("NEW")}
        <div><h3>DealCraft <span class="stamp" style="margin-left:8px">New</span></h3>
        <p>A sales-training card game. Sit across from a customer, play one reply card per turn and close the deal. Every card hides a real sales technique; some are traps.</p></div>
        {store(DEAL_STORE, DEAL_LIVE)}
      </div>
    </a>
    <a class="game-card paper ticket reveal" href="/loom-pop/">{stub("No.02")}
      <img src="/loom-pop/img/icon-180.png" alt="" width="84" height="84"><div><h3>Loom Pop!</h3><p>Aim, pop and weave: a cozy yarn ball shooter with 200 patterns.</p></div></a>
    <a class="game-card paper ticket reveal" href="/mix-bar/">{stub("No.03")}
      <img src="/mix-bar/img/icon-180.png" alt="" width="84" height="84"><div><h3>Mix Bar</h3><p>Pour, mix and serve: a water sort puzzle where flavours mix as you pour.</p></div></a>
  </div>
</div></section>

<section id="about"><div class="wrap hero-grid">
  <div>
    <div class="section-head"><span class="label">No.02 · About</span></div>
    <h2>Small studio, <mark>finished</mark> games.</h2>
    <p class="lead">We are a one-desk studio. Every game is written, drawn, tested and supported by the people who made it. If you write to us, a person who works on the game answers.</p>
  </div>
  <div class="paper ticket tilt-r" style="padding:26px 26px 26px 72px">{stub("HOW WE WORK")}
    <ul style="margin:0;padding-left:1.1em;line-height:1.8">
      <li>No accounts, no sign-up walls.</li>
      <li>Ads only where a game is free, never in the middle of play.</li>
      <li>One-time purchases, no surprise subscriptions.</li>
      <li>Your progress stays on your device.</li>
    </ul>
  </div>
</div></section>
{contact()}
"""


# ───────────────────────── DealCraft landing ─────────────────────────
def deal_landing(lang):
    tr = lang == "tr"
    p = "tr-" if tr else "en-"
    if tr:
        h1, lead = "Müşteri masada. <span>Satışı sen kapat.</span>", "DealCraft bir satış eğitimi kart oyunu. Bir müşterinin karşısına otur, her turda bir cevap kartı oyna ve satışı kapat. Her kartın arkasında gerçek bir satış tekniği var; bazıları tuzak."
        feats = [
            ("Her kart bir teknik", "SPIN soruları, Hissediyorum-Hissetti-Buldu, BANT, değer çerçeveleme… Ezber yok, masada öğrenirsin."),
            ("İnandırıcı tuzaklar", "Abartılı vaat, sahte aciliyet, kestirme yol. Kulağa doğru gelir; bedelini müşteri sonra ödetir."),
            ("180 elle yazılmış müşteri", "Emlak, perakende, telekom, otomotiv, yazılım ve sigorta: her sektörde 30 bölüm, seslendirilmiş müşteriler."),
            ("Neden doğru, neden yanlış", "Her hamleden sonra kısa bir açıklama, her bölümün sonunda bir ders kartı."),
            ("Teknik Kütüphanesi ve karne", "13 teknik ve 8 tuzak; kendi oyunlarından çıkan güçlü ve zayıf yanların."),
            ("Unvan, madalya, sertifika", "Stajyerden Satış Efsanesine unvanlar, sektör madalyaları, sertifika, maraton ve sıralama tablosu."),
        ]
        facts = [("6", "sektör"), ("180", "müşteri"), ("13", "teknik"), ("8", "tuzak")]
        faq = [
            ("Ücretli mi?", "Perakende sektörü (30 bölüm) ücretsiz. Diğer sektörler, Satış Maratonu ve reklamsız oyun tek seferlik tam sürüm satın almasıyla açılır. Abonelik yoktur."),
            ("Hesap açmam gerekir mi?", "Hayır. İlerlemen cihazında saklanır. Sıralama tablosu isteğe bağlıdır ve yalnızca bir görünen ad ister."),
            ("İnternet gerekir mi?", "Hayır, internetsiz de oynanır. Sıralama tablosu için çevrimiçi oynanan bölümler sayılır."),
            ("Gerçek satış eğitimi yerine geçer mi?", "DealCraft bir eğitim oyunudur; teknikleri tanımana ve denemene yardım eder. Bölümlerdeki yasal ve teknik bilgiler sadeleştirilmiştir, hukuki ya da mali tavsiye değildir."),
        ]
        links = '<a class="btn small" href="destek.html">Destek</a><a class="btn small" href="gizlilik.html">Gizlilik</a><a class="btn small" href="kosullar.html">Kullanım koşulları</a><a class="btn small ghost" href="/dealcraft/">English</a>'
        shots_alt = ["Masaya otur, satışı kapat", "Her kart bir satış tekniği", "Bazı kartlar tuzak", "Satış kapandı", "6 sektör, 180 müşteri", "13 teknik, 8 tuzak", "Unvanını kazan", "Zayıf yanını gör"]
        h_feat, h_shots, h_faq = "Neler var?", "Oyundan kareler", "Sık sorulanlar"
    else:
        h1, lead = "The client is seated. <span>You close.</span>", "DealCraft is a sales-training card game. Sit across from a customer, play one reply card per turn and close the deal. Every card hides a real sales technique; some are traps."
        feats = [
            ("Every card is a technique", "SPIN questions, Feel-Felt-Found, BANT, value framing… No memorising: you learn it at the table."),
            ("Traps that sound right", "Over-promises, fake urgency, shortcuts. They sound reasonable; the customer makes you pay later."),
            ("180 hand-written customers", "Real estate, retail, telecom, automotive, software and insurance: 30 chapters each, with voiced customers."),
            ("Why it worked, or didn't", "A short explanation after every move and a lesson card at the end of each chapter."),
            ("Technique library and report card", "13 techniques and 8 pitfalls, and a report built from your own games."),
            ("Titles, medals, certificate", "From Sales Trainee to Sales Legend, sector medals, a certificate, the Sales Marathon and a leaderboard."),
        ]
        facts = [("6", "sectors"), ("180", "customers"), ("13", "techniques"), ("8", "pitfalls")]
        faq = [
            ("Is it free?", "Retail (30 chapters) is free. The other sectors, the Sales Marathon and ad-free play come with a one-time full-version purchase. No subscription."),
            ("Do I need an account?", "No. Your progress stays on your device. The leaderboard is optional and only asks for a display name."),
            ("Does it need internet?", "No, it plays offline too. For the leaderboard, chapters played online count."),
            ("Is it real sales training?", "DealCraft is a training game: it helps you recognise and try techniques. Legal and technical details in the chapters are simplified; they are not legal or financial advice."),
        ]
        links = '<a class="btn small" href="support.html">Support</a><a class="btn small" href="privacy.html">Privacy</a><a class="btn small" href="terms.html">Terms of use</a><a class="btn small ghost" href="/dealcraft/tr/">Türkçe</a>'
        shots_alt = ["Sit down and close the sale", "Every card is a technique", "Some cards are traps", "Deal closed", "6 sectors, 180 customers", "13 techniques, 8 pitfalls", "Earn your sales title", "Know your weak spot"]
        h_feat, h_shots, h_faq = "What's inside", "From the game", "Questions"
    feats_html = "".join(f'<div class="feat paper ticket reveal">{stub(f"No.0{i + 1}")}<h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(feats))
    facts_html = "".join(f'<div class="fact"><b>{n}</b><span>{l}</span></div>' for n, l in facts)
    rail = "".join(f'<img src="/dealcraft/img/{p}shot-{i + 1}.webp" alt="{a}" width="660" height="1434" loading="lazy">' for i, a in enumerate(shots_alt))
    faq_html = "".join(f"<details><summary>{q}</summary><p style='margin:.6em 0 0'>{a}</p></details>" for q, a in faq)
    return f"""
<section class="hero"><div class="wrap hero-grid">
  <div>
    <p class="label" style="color:var(--pirinc)">DealCraft · iPhone</p>
    <h1>{h1}</h1>
    <p class="lead">{lead}</p>
    <div class="actions">{store(DEAL_STORE, DEAL_LIVE, lang)}</div>
    <div class="facts">{facts_html}</div>
  </div>
  <div class="shots-pair" aria-hidden="true">
    <img class="shot" src="/dealcraft/img/{p}raw-turn.webp" alt="" width="660" height="1434">
    <img class="shot" src="/dealcraft/img/{p}shot-2.webp" alt="" width="660" height="1434">
  </div>
</div></section>
<section style="padding-top:20px"><div class="wrap"><div class="banner-art reveal"><img src="/dealcraft/img/{p}header.webp" alt="" width="1920" height="823"></div></div></section>
<section><div class="wrap">
  <div class="section-head"><span class="label">No.01 · {h_feat}</span></div>
  <div class="features">{feats_html}</div>
</div></section>
<section><div class="wrap">
  <div class="section-head"><span class="label">No.02 · {h_shots}</span></div>
  <div class="rail" tabindex="0" aria-label="{h_shots}">{rail}</div>
</div></section>
<section><div class="wrap">
  <div class="paper ticket faq reveal" style="padding:26px 26px 20px 72px">{stub("FAQ")}
    <h2>{h_faq}</h2>{faq_html}
    <div class="actions" style="margin-top:18px">{links}</div>
  </div>
</div></section>
{contact(lang)}
"""


# ───────────────────────── DealCraft legal ─────────────────────────
PRIVACY_EN = f"""
<a class="btn small ghost lang" href="/dealcraft/tr/gizlilik.html">Türkçe</a>
<h1>Privacy Policy</h1>
<p class="meta">DealCraft · Last updated: {UPDATED_EN} · Developer and data controller: SefyStudio · Contact: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
<h2>The short version</h2>
<p>You don't need an account, an email address or a phone number to play. Your progress stays on your iPhone. If you choose to join the optional leaderboard, we store the display name you pick and your chapter scores, and you can delete them in the app at any time. Players without the full version see ads from Google AdMob. Payments are handled by Apple.</p>

<h2>1. Data that stays on your device</h2>
<p>Chapter progress, stars, medals, achievements, statistics for your technique report, and your language, sound and practice settings are stored only on your device. We cannot see them. Deleting the app deletes them.</p>

<h2>2. Online play</h2>
<p>When you are online, a chapter is played on our game server (Cloudflare Workers). The server sends the customer's lines and cards and keeps the game state in an encrypted token that your app holds; it does not ask for or store personal data. To stop the same finished game from being counted twice, we keep a one-way hash of finished game tokens. Like any website, our hosting provider Cloudflare, Inc. briefly processes your IP address to deliver the service and to protect it from abuse. Offline, chapters are played on your device and nothing is sent.</p>

<h2>3. Leaderboard (optional)</h2>
<p>If you join the leaderboard we process:</p>
<ul>
  <li>the <b>display name</b> you choose and, if you enter one, a <b>company code</b> to appear on your company's board;</li>
  <li>a random <b>player id</b> and a secret key created on your device (we store only a hash of the key);</li>
  <li>the <b>score and stars</b> of chapters you finish online, with the time they were recorded.</li>
</ul>
<p><b>Why:</b> to show the leaderboards you asked to join. <b>Legal basis:</b> performance of the service you requested (GDPR Art. 6(1)(b); KVKK Art. 5(2)(c)). <b>Where:</b> Cloudflare's database (Cloudflare D1). <b>How long:</b> until you delete it.</p>
<p><b>Delete:</b> in the app, open <i>Leaderboard → Leave the board and delete my data</i>. Your name, scores and reports are deleted from our server immediately. You can also email us.</p>
<p><b>Display names and reports.</b> Names are checked against a list of offensive words. Any player can report a name; a report stores the reported player id, the reporter's player id (or, for viewers who have not joined, a one-way hash of their IP address) and the time. A name reported by two different players is hidden. Reports are deleted with the reported or reporting player's data.</p>

<h2>4. Ads (Google AdMob)</h2>
<p>Players without the full version see a rewarded video only when they choose to watch one (to remove a wrong card) and an occasional full-screen ad between chapters, never during a chapter. Ads are served by Google AdMob (Google Ireland Limited / Google LLC). Google may collect and use your device's advertising identifier (IDFA), IP address, approximate location, ad interactions and diagnostic data to deliver, measure and, with your permission, personalise ads and to prevent fraud. See <a href="https://policies.google.com/technologies/partner-sites">how Google uses information from apps that use its services</a> and <a href="https://policies.google.com/privacy">Google's Privacy Policy</a>.</p>
<p><b>Consent (EEA, UK, Switzerland).</b> Before ads load, Google's consent form (User Messaging Platform) asks for your choices. You can change them at any time from the home screen of the game: <i>Ad choices</i>.</p>
<p><b>Tracking permission.</b> iOS asks whether DealCraft may track you across other companies' apps and websites (App Tracking Transparency). If you decline, the advertising identifier is not shared and ads are not personalised. The game works the same either way. You can change this in iOS Settings → Privacy &amp; Security → Tracking. With the full version, no ads are shown.</p>

<h2>5. Purchases (Apple and RevenueCat)</h2>
<p>The full version is a one-time in-app purchase handled by Apple. We never see your payment details or your Apple ID. To confirm the purchase and restore it on your other devices, we use RevenueCat, Inc., which processes an anonymous app user id, the purchase receipt and basic device information. See <a href="https://www.revenuecat.com/privacy/">RevenueCat's privacy policy</a>.</p>

<h2>6. Game Center</h2>
<p>If you are signed in to Game Center, your achievements and seller score are sent to Apple Game Center and shown according to your Game Center settings, under <a href="https://www.apple.com/legal/privacy/">Apple's Privacy Policy</a>. We don't receive your Game Center identity.</p>

<h2>7. Voice answers</h2>
<p>If you tap <i>Answer by voice</i>, iOS asks for microphone and speech recognition permission. Your speech is turned into text by Apple's speech recognition (on your iPhone when the device supports it, otherwise by Apple's servers under Apple's privacy policy) and the text is used only to pick the matching card on your device. We do not record, store or receive your voice or the text. You can always play by tapping the cards instead.</p>

<h2>8. International transfers</h2>
<p>Cloudflare, Google and RevenueCat may process data outside your country, including in the United States. These providers use safeguards such as the EU Standard Contractual Clauses. For players in Türkiye, data is transferred abroad on the basis of these safeguards and, where required, your explicit consent given through the in-app permission and consent screens (KVKK Art. 9).</p>

<h2>9. Children</h2>
<p>DealCraft is a general-audience game and is not directed to children under 13. We do not knowingly collect personal data from children. If you believe a child has joined the leaderboard, contact us and we will delete it.</p>

<h2>10. Your rights</h2>
<p>Depending on where you live (for example under the GDPR, the UK GDPR, Türkiye's Law No. 6698 (KVKK) or US state laws such as the CCPA), you can ask to access, correct, delete or receive a copy of your data, object to or restrict processing, and withdraw consent. We do not sell or share personal data for money. Email <a href="mailto:{EMAIL}">{EMAIL}</a>; we answer within 30 days. You may also complain to your data protection authority (in Türkiye: Kişisel Verileri Koruma Kurumu).</p>

<h2>11. Changes</h2>
<p>If this policy changes, we will update the date above and, for important changes, tell you in the app.</p>
<p style="margin-top:26px"><a class="btn small" href="support.html">Support</a> <a class="btn small" href="terms.html">Terms of use</a> <a class="btn small ghost" href="./">DealCraft</a></p>
"""

PRIVACY_TR = f"""
<a class="btn small ghost lang" href="/dealcraft/privacy.html">English</a>
<h1>Gizlilik Politikası</h1>
<p class="meta">DealCraft · Son güncelleme: {UPDATED_TR} · Geliştirici ve veri sorumlusu: SefyStudio · İletişim: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
<h2>Kısaca</h2>
<p>Oynamak için hesap, e-posta ya da telefon numarası gerekmez. İlerlemen iPhone'unda kalır. İsteğe bağlı sıralama tablosuna katılırsan seçtiğin görünen adı ve bölüm puanlarını saklarız; bunları uygulamadan istediğin an silebilirsin. Tam sürümü almayan oyunculara Google AdMob reklamları gösterilir. Ödemeyi Apple alır.</p>

<h2>1. Cihazında kalan veriler</h2>
<p>Bölüm ilerlemen, yıldızların, madalyaların, başarımların, teknik karnen için istatistikler ve dil, ses, antrenman ayarların yalnızca cihazında saklanır. Biz göremeyiz. Uygulamayı silince bunlar da silinir.</p>

<h2>2. Çevrimiçi oyun</h2>
<p>İnternet varken bölümler oyun sunucumuzda (Cloudflare Workers) oynatılır. Sunucu müşterinin repliklerini ve kartları gönderir; oyun durumunu uygulamanda duran şifreli bir anahtarda tutar; kişisel veri istemez ve saklamaz. Aynı oyunun iki kez sayılmaması için biten oyun anahtarlarının tek yönlü özetini saklarız. Her web hizmetinde olduğu gibi, barındırma sağlayıcımız Cloudflare, Inc. hizmeti sunmak ve kötüye kullanımı önlemek için IP adresini kısa süreli işler. İnternetsiz oynandığında bölümler cihazında oynanır, hiçbir şey gönderilmez.</p>

<h2>3. Sıralama tablosu (isteğe bağlı)</h2>
<p>Sıralama tablosuna katılırsan şunları işleriz:</p>
<ul>
  <li>seçtiğin <b>görünen ad</b> ve, girersen, şirket tablosunda görünmek için <b>şirket kodu</b>;</li>
  <li>cihazında üretilen rastgele bir <b>oyuncu kimliği</b> ve gizli anahtar (anahtarın yalnızca özetini saklarız);</li>
  <li>çevrimiçi bitirdiğin bölümlerin <b>puan ve yıldızları</b> ve kayıt zamanı.</li>
</ul>
<p><b>Amaç:</b> katılmak istediğin tabloları göstermek. <b>Hukuki sebep:</b> talep ettiğin hizmetin sunulması (KVKK m.5/2-c; GDPR m.6/1-b). <b>Nerede:</b> Cloudflare veritabanı (Cloudflare D1). <b>Ne kadar süre:</b> sen silene kadar.</p>
<p><b>Silme:</b> Uygulamada <i>Sıralama tablosu → Tablodan çık ve verilerimi sil</i> düğmesine dokun. Adın, puanların ve bildirimlerin sunucudan hemen silinir. Bize e-posta da yazabilirsin.</p>
<p><b>Görünen adlar ve bildirimler.</b> Adlar uygunsuz kelime listesiyle kontrol edilir. Her oyuncu bir adı bildirebilir; bildirim, bildirilen oyuncu kimliğini, bildirenin oyuncu kimliğini (tabloya katılmamış izleyiciler için IP adresinin tek yönlü özetini) ve zamanı saklar. İki farklı oyuncu tarafından bildirilen ad gizlenir. Bildirimler, bildirilen ya da bildiren oyuncunun verileriyle birlikte silinir.</p>

<h2>4. Reklamlar (Google AdMob)</h2>
<p>Tam sürümü olmayan oyunculara ödüllü video yalnızca kendileri seçtiğinde (bir yanlış kartı elemek için) ve bölümler arasında arada bir tam ekran reklam gösterilir; bölüm ortasında hiçbir zaman gösterilmez. Reklamları Google AdMob (Google Ireland Limited / Google LLC) sunar. Google; reklamları sunmak, ölçmek, iznin varsa kişiselleştirmek ve sahtekârlığı önlemek için cihazın reklam kimliğini (IDFA), IP adresini, yaklaşık konumunu, reklam etkileşimlerini ve teşhis verilerini toplayıp kullanabilir. Ayrıntı: <a href="https://policies.google.com/technologies/partner-sites">Google'ın, hizmetlerini kullanan uygulamalardan gelen bilgileri nasıl kullandığı</a> ve <a href="https://policies.google.com/privacy">Google Gizlilik Politikası</a>.</p>
<p><b>Rıza (AEA, Birleşik Krallık, İsviçre).</b> Reklamlar yüklenmeden önce Google'ın rıza formu (User Messaging Platform) tercihlerini sorar. Tercihini istediğin an oyunun ana sayfasındaki <i>Reklam tercihleri</i> bağlantısından değiştirebilirsin.</p>
<p><b>Takip izni.</b> iOS, DealCraft'ın seni diğer şirketlerin uygulama ve web sitelerinde takip edip edemeyeceğini sorar (App Tracking Transparency). İzin vermezsen reklam kimliği paylaşılmaz ve reklamlar kişiselleştirilmez. Oyun iki durumda da aynı çalışır. Bunu iOS Ayarlar → Gizlilik ve Güvenlik → Takip bölümünden değiştirebilirsin. Tam sürümde reklam gösterilmez.</p>

<h2>5. Satın alma (Apple ve RevenueCat)</h2>
<p>Tam sürüm, Apple'ın aldığı tek seferlik bir uygulama içi satın almadır. Ödeme bilgilerini ve Apple kimliğini görmeyiz. Satın almayı doğrulamak ve diğer cihazlarında geri yüklemek için RevenueCat, Inc. hizmetini kullanırız; RevenueCat anonim bir uygulama kullanıcı kimliğini, satın alma makbuzunu ve temel cihaz bilgilerini işler. Ayrıntı: <a href="https://www.revenuecat.com/privacy/">RevenueCat gizlilik politikası</a>.</p>

<h2>6. Game Center</h2>
<p>Game Center'a giriş yaptıysan başarımların ve satıcı puanın Apple Game Center'a gönderilir ve Game Center ayarlarına göre, <a href="https://www.apple.com/legal/privacy/">Apple Gizlilik Politikası</a> kapsamında gösterilir. Game Center kimliğin bize ulaşmaz.</p>

<h2>7. Sesli cevap</h2>
<p><i>Sesli cevap ver</i>'e dokunursan iOS mikrofon ve konuşma tanıma izni ister. Konuşman Apple'ın konuşma tanıma hizmetiyle yazıya çevrilir (cihaz destekliyorsa iPhone'unda, desteklemiyorsa Apple'ın gizlilik politikası kapsamında Apple sunucularında) ve metin yalnızca cihazında eşleşen kartı seçmek için kullanılır. Sesini ya da metni kaydetmeyiz, saklamayız, bize ulaşmaz. Her zaman kartlara dokunarak da oynayabilirsin.</p>

<h2>8. Yurt dışına aktarım</h2>
<p>Cloudflare, Google ve RevenueCat verileri ABD dahil başka ülkelerde işleyebilir. Bu sağlayıcılar AB Standart Sözleşme Maddeleri gibi güvenceler kullanır. Türkiye'deki oyuncular için veriler bu güvencelere ve gerektiğinde uygulama içindeki izin ve rıza ekranlarıyla verdiğin açık rızaya dayanılarak yurt dışına aktarılır (KVKK m.9).</p>

<h2>9. Çocuklar</h2>
<p>DealCraft genel kitleye yönelik bir oyundur; 13 yaş altı çocuklara yönelik değildir. Bilerek çocuklardan kişisel veri toplamayız. Bir çocuğun sıralama tablosuna katıldığını düşünüyorsan bize yaz, sileriz.</p>

<h2>10. Hakların</h2>
<p>KVKK m.11 ve GDPR kapsamında verilerine erişme, düzeltilmesini, silinmesini ya da bir kopyasını isteme, işlemeye itiraz etme veya kısıtlanmasını isteme ve rızanı geri alma hakların vardır. Kişisel verileri para karşılığı satmayız ya da paylaşmayız. Taleplerin için <a href="mailto:{EMAIL}">{EMAIL}</a> adresine yaz; en geç 30 gün içinde cevaplarız. Kişisel Verileri Koruma Kurumu'na şikâyette de bulunabilirsin.</p>

<h2>11. Değişiklikler</h2>
<p>Bu politika değişirse yukarıdaki tarihi güncelleriz; önemli değişiklikleri uygulamada da bildiririz.</p>
<p style="margin-top:26px"><a class="btn small" href="destek.html">Destek</a> <a class="btn small" href="kosullar.html">Kullanım koşulları</a> <a class="btn small ghost" href="./">DealCraft</a></p>
"""

SUPPORT_EN = f"""
<a class="btn small ghost lang" href="/dealcraft/tr/destek.html">Türkçe</a>
<h1>Support</h1>
<p>Something not working, an idea, or a customer you loved? Email <a href="mailto:{EMAIL}">{EMAIL}</a> with your iPhone model, iOS version and, if it's about a chapter, its sector and number. A person who works on the game answers, usually within a day or two.</p>
<h2>How do I play?</h2>
<p>A customer sits across the table. Read their line, then tap one of the reply cards before the clock runs out. The best card uses the right sales technique for this customer at this moment; some cards are traps that sound right. After each move you see why it worked or not. Win the customer over and close the deal to finish the chapter. The <b>?</b> button on the home screen opens the full guide.</p>
<h2>Answer by voice doesn't work</h2>
<p>Voice answers need microphone and speech recognition permission. Turn them on in iOS Settings → DealCraft. You can always tap the cards instead.</p>
<h2>Get the full version / restore my purchase</h2>
<p>Tap any locked sector, or <i>Full version / restore purchase</i> at the bottom of the home screen. Use <i>Restore purchase</i> with the Apple ID you bought it with to unlock it on a new iPhone.</p>
<h2>Refunds</h2>
<p>Purchases are handled by Apple: visit <a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>.</p>
<h2>Ads and privacy choices</h2>
<p>In the EEA, UK and Switzerland, tap <i>Ad choices</i> at the bottom of the home screen. Tracking permission can be changed in iOS Settings → Privacy &amp; Security → Tracking. The full version has no ads.</p>
<h2>Leaderboard</h2>
<p>Joining is optional and only needs a display name (and a company code if your company gave you one). To report a name, tap <i>Report</i> next to it: it is hidden on your device at once and reviewed. To leave and delete your data, tap <i>Leave the board and delete my data</i>.</p>
<h2>Company boards</h2>
<p>Want a private board for your sales team? Email us with your company name and we'll send an invite code.</p>
<h2>My progress is gone</h2>
<p>Progress is saved on your device. Deleting the app or clearing its data removes it. Your full-version purchase is never lost: restore it with the same Apple ID.</p>
<p style="margin-top:26px"><a class="btn small" href="privacy.html">Privacy Policy</a> <a class="btn small" href="terms.html">Terms of use</a> <a class="btn small ghost" href="./">DealCraft</a></p>
"""

SUPPORT_TR = f"""
<a class="btn small ghost lang" href="/dealcraft/support.html">English</a>
<h1>Destek</h1>
<p>Bir şey çalışmıyor mu, bir fikrin mi var, ya da çok sevdiğin bir müşteri mi? <a href="mailto:{EMAIL}">{EMAIL}</a> adresine iPhone modelini, iOS sürümünü ve bir bölümle ilgiliyse sektörünü ve numarasını yaz. Oyunda çalışan biri, genellikle bir iki gün içinde cevaplar.</p>
<h2>Nasıl oynanır?</h2>
<p>Masanın karşısında bir müşteri oturur. Söylediğini oku, süre bitmeden cevap kartlarından birine dokun. En iyi kart, bu müşteriye bu anda doğru satış tekniğini kullanır; bazı kartlar kulağa doğru gelen tuzaklardır. Her hamleden sonra neden işe yaradığını ya da yaramadığını görürsün. Müşteriyi ikna edip satışı kapatınca bölüm biter. Ana sayfadaki <b>?</b> düğmesi tam rehberi açar.</p>
<h2>Sesli cevap çalışmıyor</h2>
<p>Sesli cevap için mikrofon ve konuşma tanıma izni gerekir. iOS Ayarlar → DealCraft bölümünden açabilirsin. Her zaman kartlara dokunarak da oynayabilirsin.</p>
<h2>Tam sürümü almak / satın alımı geri yüklemek</h2>
<p>Kilitli bir sektöre ya da ana sayfanın altındaki <i>Tam sürüm / satın alımı geri yükle</i> bağlantısına dokun. Yeni bir iPhone'da, satın aldığın Apple kimliğiyle <i>Satın alımı geri yükle</i>'ye dokunman yeterli.</p>
<h2>İade</h2>
<p>Satın almaları Apple yönetir: <a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>.</p>
<h2>Reklam ve gizlilik tercihleri</h2>
<p>AEA, Birleşik Krallık ve İsviçre'de ana sayfanın altındaki <i>Reklam tercihleri</i>'ne dokun. Takip izni iOS Ayarlar → Gizlilik ve Güvenlik → Takip bölümünden değiştirilebilir. Tam sürümde reklam yoktur.</p>
<h2>Sıralama tablosu</h2>
<p>Katılmak isteğe bağlıdır; yalnızca bir görünen ad (şirketin verdiyse bir şirket kodu) ister. Bir adı bildirmek için yanındaki <i>Bildir</i>'e dokun: ad cihazında hemen gizlenir ve incelenir. Tablodan çıkıp verilerini silmek için <i>Tablodan çık ve verilerimi sil</i>'e dokun.</p>
<h2>Şirket tabloları</h2>
<p>Satış ekibin için özel bir tablo mu istiyorsun? Şirket adınla bize yaz, davet kodunu gönderelim.</p>
<h2>İlerlemem kayboldu</h2>
<p>İlerleme cihazında saklanır. Uygulamayı silmek ya da verilerini temizlemek onu siler. Tam sürüm satın alman kaybolmaz: aynı Apple kimliğiyle geri yükleyebilirsin.</p>
<p style="margin-top:26px"><a class="btn small" href="gizlilik.html">Gizlilik Politikası</a> <a class="btn small" href="kosullar.html">Kullanım koşulları</a> <a class="btn small ghost" href="./">DealCraft</a></p>
"""

TERMS_EN = f"""
<a class="btn small ghost lang" href="/dealcraft/tr/kosullar.html">Türkçe</a>
<h1>Terms of Use</h1>
<p class="meta">DealCraft · Last updated: {UPDATED_EN} · SefyStudio · <a href="mailto:{EMAIL}">{EMAIL}</a></p>
<h2>License</h2>
<p>DealCraft is licensed to you under Apple's <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">Standard End User License Agreement</a>, together with these terms. If they conflict, Apple's agreement applies.</p>
<h2>Full version</h2>
<p>The full version is a one-time, non-consumable in-app purchase sold through the App Store. It unlocks the remaining sectors, the Sales Marathon and ad-free play on every device signed in with the same Apple ID. Refunds are handled by Apple.</p>
<h2>Training, not advice</h2>
<p>DealCraft is a game for learning and practising sales techniques. The customers, products, prices and situations are fictional. Legal, tax, insurance and technical details are simplified for training and are not legal, financial or professional advice. In real deals, follow current law and qualified professionals.</p>
<h2>Leaderboard conduct</h2>
<p>Choose a display name that is not offensive, does not impersonate anyone and contains no personal data of others. We may hide or remove names and results that break these rules or that were obtained by cheating, and we may remove company boards that are misused.</p>
<h2>Availability</h2>
<p>We work to keep online play and the leaderboard running but cannot promise they will always be available. The game can always be played offline.</p>
<h2>Contact</h2>
<p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
<p style="margin-top:26px"><a class="btn small" href="privacy.html">Privacy Policy</a> <a class="btn small" href="support.html">Support</a> <a class="btn small ghost" href="./">DealCraft</a></p>
"""

TERMS_TR = f"""
<a class="btn small ghost lang" href="/dealcraft/terms.html">English</a>
<h1>Kullanım Koşulları</h1>
<p class="meta">DealCraft · Son güncelleme: {UPDATED_TR} · SefyStudio · <a href="mailto:{EMAIL}">{EMAIL}</a></p>
<h2>Lisans</h2>
<p>DealCraft sana Apple'ın <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">Standart Son Kullanıcı Lisans Sözleşmesi</a> ve bu koşullar kapsamında lisanslanır. Çelişki olursa Apple'ın sözleşmesi geçerlidir.</p>
<h2>Tam sürüm</h2>
<p>Tam sürüm, App Store üzerinden satılan tek seferlik, tükenmeyen bir uygulama içi satın almadır. Kalan sektörleri, Satış Maratonunu ve reklamsız oyunu aynı Apple kimliğiyle giriş yapılmış bütün cihazlarda açar. İadeleri Apple yönetir.</p>
<h2>Eğitimdir, tavsiye değildir</h2>
<p>DealCraft, satış tekniklerini öğrenmek ve denemek için bir oyundur. Müşteriler, ürünler, fiyatlar ve durumlar kurgudur. Yasal, vergi, sigorta ve teknik ayrıntılar eğitim için sadeleştirilmiştir; hukuki, mali ya da mesleki tavsiye değildir. Gerçek işlemlerde güncel mevzuatı ve yetkili uzmanları esas al.</p>
<h2>Sıralama tablosu kuralları</h2>
<p>Uygunsuz olmayan, kimseyi taklit etmeyen ve başkalarının kişisel verisini içermeyen bir görünen ad seç. Bu kurallara uymayan ya da hileyle elde edilen ad ve sonuçları gizleyebilir veya kaldırabiliriz; kötüye kullanılan şirket tablolarını kapatabiliriz.</p>
<h2>Erişilebilirlik</h2>
<p>Çevrimiçi oyunun ve sıralama tablosunun çalışır kalması için çalışırız, ancak her zaman erişilebilir olacaklarını garanti edemeyiz. Oyun her zaman internetsiz oynanabilir.</p>
<h2>İletişim</h2>
<p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
<p style="margin-top:26px"><a class="btn small" href="gizlilik.html">Gizlilik Politikası</a> <a class="btn small" href="destek.html">Destek</a> <a class="btn small ghost" href="./">DealCraft</a></p>
"""


# ───────────────────────── earlier games (overview pages, simple) ─────────────────────────
def game_overview(name, sub, tagline, icon, url, live, folder, shots, links):
    rail = "".join(f'<img src="/{folder}/img/shot-{i}.webp" alt="{name} screenshot {i}" width="660" height="1434" loading="lazy">' for i in range(1, shots + 1))
    return f"""
<section class="hero"><div class="wrap">
  <div class="paper ticket" style="padding:26px 26px 26px 72px;display:flex;gap:22px;align-items:center;flex-wrap:wrap">{stub(folder.upper())}
    <img src="{icon}" alt="" width="120" height="120" style="width:120px;border-radius:26px;border:3px solid var(--ink)">
    <div style="flex:1;min-width:240px"><p class="label" style="color:var(--ink-soft)">{sub}</p><h1 style="font-size:clamp(40px,6vw,64px)">{name}</h1><p style="margin:0">{tagline}</p></div>
    {store(url, live)}
  </div>
</div></section>
<section style="padding-top:0"><div class="wrap"><div class="rail" tabindex="0" aria-label="Screenshots">{rail}</div>
  <div class="actions">{links}</div></div></section>
{contact()}
"""


if __name__ == "__main__":
    page("/", "SefyStudio · Independent games for iPhone", "SefyStudio is a small independent studio making well-crafted iPhone games: DealCraft, Loom Pop! and Mix Bar.", HOME, current="home")
    for lang, base in (("en", "/dealcraft/"), ("tr", "/dealcraft/tr/")):
        tr = lang == "tr"
        other = ("en", "/dealcraft/") if tr else ("tr", "/dealcraft/tr/")
        icon = "/dealcraft/img/icon-180.png"
        og = f"/dealcraft/img/{lang}-og.jpg"
        page(base, "DealCraft: Satış Eğitimi Kart Oyunu" if tr else "DealCraft: Sales Training Card Game",
             ("Müşteri masada, satışı sen kapat. Her kart gerçek bir satış tekniği, bazıları tuzak. 6 sektör, 180 müşteri. iPhone için." if tr else
              "The client is seated, you close. Every card is a real sales technique; some are traps. 6 sectors, 180 customers. For iPhone."),
             deal_landing(lang), current="deal", lang=lang, image=og, icon=icon, alt=other)
        page(base + ("gizlilik.html" if tr else "privacy.html"), "DealCraft Gizlilik Politikası" if tr else "DealCraft Privacy Policy",
             "DealCraft gizlilik politikası (SefyStudio)." if tr else "Privacy policy of DealCraft by SefyStudio.",
             doc(PRIVACY_TR if tr else PRIVACY_EN, "GİZLİLİK" if tr else "PRIVACY"), current="deal", lang=lang, image=og, icon=icon,
             alt=(other[0], other[1] + ("privacy.html" if tr else "gizlilik.html")))
        page(base + ("destek.html" if tr else "support.html"), "DealCraft Destek" if tr else "DealCraft Support",
             "DealCraft yardım: nasıl oynanır, satın alma, sesli cevap, sıralama tablosu." if tr else "Help with DealCraft: how to play, purchases, voice answers, leaderboard.",
             doc(SUPPORT_TR if tr else SUPPORT_EN, "DESTEK" if tr else "SUPPORT"), current="support" if tr else "deal", lang=lang, image=og, icon=icon,
             alt=(other[0], other[1] + ("support.html" if tr else "destek.html")))
        page(base + ("kosullar.html" if tr else "terms.html"), "DealCraft Kullanım Koşulları" if tr else "DealCraft Terms of Use",
             "DealCraft kullanım koşulları." if tr else "Terms of use of DealCraft.",
             doc(TERMS_TR if tr else TERMS_EN, "KOŞULLAR" if tr else "TERMS"), current="deal", lang=lang, image=og, icon=icon,
             alt=(other[0], other[1] + ("terms.html" if tr else "kosullar.html")))

    # Earlier apps: these URLs are linked from their App Store listings and apps. Keep them.
    page("/loom-pop/", "Loom Pop! Yarn Ball Shooter", "Aim, pop and weave: match three yarn balls and knit 200 cozy patterns. Free for iPhone.",
         game_overview("Loom Pop!", "Yarn Ball Shooter", "Aim, pop and weave: match three yarn balls and knit 200 cozy patterns.", "/loom-pop/img/icon-180.png",
                       L.LOOM_STORE, True, "loom-pop", 6, '<a class="btn small" href="support.html">Support</a><a class="btn small" href="privacy.html">Privacy</a>'),
         current="games", image="/loom-pop/img/poster.jpg", icon="/loom-pop/img/icon-180.png")
    page("/loom-pop/support.html", "Loom Pop! Support", "Help with Loom Pop!: purchases, progress and ad choices.", doc(L.LOOM_SUPPORT, "LOOM POP!"), icon="/loom-pop/img/icon-180.png")
    page("/loom-pop/privacy.html", "Loom Pop! Privacy Policy", "Privacy policy of Loom Pop! by SefyStudio.", doc(L.LOOM_PRIVACY, "LOOM POP!"), icon="/loom-pop/img/icon-180.png")
    mix_shots = len([f for f in os.listdir(os.path.join(ROOT, "mix-bar/img")) if f.startswith("shot-")])
    page("/mix-bar/", "Mix Bar: Water Sort Puzzle", "Pour, mix and serve: a water sort puzzle where flavours mix when you pour them. Free for iPhone.",
         game_overview("Mix Bar", "Water Sort Puzzle", "Pour, mix and serve: a water sort puzzle where flavours mix as you pour.", "/mix-bar/img/icon-180.png",
                       L.MIX_STORE, L.MIX_LIVE, "mix-bar", mix_shots, '<a class="btn small" href="support.html">Support</a><a class="btn small" href="privacy.html">Privacy</a>'),
         current="games", icon="/mix-bar/img/icon-180.png")
    page("/mix-bar/support.html", "Mix Bar Support", "Help with Mix Bar: how to play, purchases, progress and ad choices.", doc(L.MIX_SUPPORT, "MIX BAR"), icon="/mix-bar/img/icon-180.png")
    page("/mix-bar/privacy.html", "Mix Bar Privacy Policy", "Privacy policy of Mix Bar: Water Sort Puzzle by SefyStudio.", doc(L.MIX_PRIVACY, "MIX BAR"), icon="/mix-bar/img/icon-180.png")
    page("/pip-and-pals/support.html", "Pip & Pals Support", "Help with Pip & Pals: purchases, progress and co-op.", doc(L.PIP_SUPPORT, "PIP & PALS"), noindex=True)
    page("/pip-and-pals/privacy.html", "Pip & Pals Privacy Policy", "Privacy policy of Pip & Pals: Hide & Seek by SefyStudio.", doc(L.PIP_PRIVACY, "PIP & PALS"), noindex=True)
    page("/pip-and-pals/join.html", "Join a Pip & Pals room", "Your friend invited you to a Pip & Pals co-op room.", doc(L.PIP_JOIN, "PIP & PALS"), noindex=True)
    page("/privacy.html", "Privacy Policy · SefyStudio Publisher", "Privacy policy of SefyStudio Publisher, SefyStudio's internal publishing tool.", doc(L.PUBLISHER_PRIVACY))
    page("/terms.html", "Terms of Service · SefyStudio Publisher", "Terms of service of SefyStudio Publisher, SefyStudio's internal publishing tool.", doc(L.PUBLISHER_TERMS))
    page("/brand/", "Brand assets · SefyStudio", "SefyStudio logos and icons for press and partners.", doc(L.BRAND, "BRAND"))
    page("/404.html", "Page not found · SefyStudio", "This page could not be found.",
         doc('<h1>Wrong table.</h1><p>The page you were looking for could not be found.</p><p style="margin-top:22px"><a class="btn primary" href="/">Back to SefyStudio</a></p>', "404"))
