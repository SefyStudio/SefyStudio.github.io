"""DealCraft's privacy, support and terms texts (EN + TR) for the SefyStudio site. Imported by _build.py."""
EMAIL = "support@sefystudio.com"
UPDATED_EN = "November 16, 2026"
UPDATED_TR = "16 Kasım 2026"

PRIVACY_EN = f"""
<a class="btn ghost small lang" href="/dealcraft/tr/gizlilik.html">Türkçe</a>
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
<p style="margin-top:26px"><a class="btn ghost small" href="support.html">Support</a> <a class="btn ghost small" href="terms.html">Terms of use</a> <a class="btn ghost small" href="./">DealCraft</a></p>
"""

PRIVACY_TR = f"""
<a class="btn ghost small lang" href="/dealcraft/privacy.html">English</a>
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
<p style="margin-top:26px"><a class="btn ghost small" href="destek.html">Destek</a> <a class="btn ghost small" href="kosullar.html">Kullanım koşulları</a> <a class="btn ghost small" href="./">DealCraft</a></p>
"""

SUPPORT_EN = f"""
<a class="btn ghost small lang" href="/dealcraft/tr/destek.html">Türkçe</a>
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
<p style="margin-top:26px"><a class="btn ghost small" href="privacy.html">Privacy Policy</a> <a class="btn ghost small" href="terms.html">Terms of use</a> <a class="btn ghost small" href="./">DealCraft</a></p>
"""

SUPPORT_TR = f"""
<a class="btn ghost small lang" href="/dealcraft/support.html">English</a>
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
<p style="margin-top:26px"><a class="btn ghost small" href="gizlilik.html">Gizlilik Politikası</a> <a class="btn ghost small" href="kosullar.html">Kullanım koşulları</a> <a class="btn ghost small" href="./">DealCraft</a></p>
"""

TERMS_EN = f"""
<a class="btn ghost small lang" href="/dealcraft/tr/kosullar.html">Türkçe</a>
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
<p style="margin-top:26px"><a class="btn ghost small" href="privacy.html">Privacy Policy</a> <a class="btn ghost small" href="support.html">Support</a> <a class="btn ghost small" href="./">DealCraft</a></p>
"""

TERMS_TR = f"""
<a class="btn ghost small lang" href="/dealcraft/terms.html">English</a>
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
<p style="margin-top:26px"><a class="btn ghost small" href="gizlilik.html">Gizlilik Politikası</a> <a class="btn ghost small" href="destek.html">Destek</a> <a class="btn ghost small" href="./">DealCraft</a></p>
"""


