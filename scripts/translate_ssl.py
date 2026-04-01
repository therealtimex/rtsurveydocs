#!/usr/bin/env python3
"""Translate ssl-setup.md into all 35 languages."""
import os

BASE = "/Volumes/ExDisk/rtLab/webapp/doc.rtsurvey.com/content"
REL = "docs/getting-started/self-hosting/ssl-setup.md"

LANGUAGES = [
    "ar","bg","cs","da","de","el","es","fi","fr","hi",
    "hu","id","it","ja","km","ko","lt","lv","nb","nl",
    "pl","pt","pt-br","ru","sk","sq","sr","sv","te","th",
    "tr","uk","vi","zh-hans","zh-hant"
]

META = {
    "weight": 4,
    "date": "2026-04-01T00:00:00+07:00",
    "lastmod": "2026-04-01T00:00:00+07:00",
    "draft": "false",
    "author": "rtSurvey",
    "icon": "lock",
    "toc": "true",
}

TITLES = {
    "ar": "إعداد SSL",
    "bg": "Настройка на SSL",
    "cs": "Nastavení SSL",
    "da": "Opsætning af SSL",
    "de": "SSL einrichten",
    "el": "Ρύθμιση SSL",
    "es": "Configurar SSL",
    "fi": "SSL:n asennus",
    "fr": "Configuration SSL",
    "hi": "SSL सेटअप करें",
    "hu": "SSL beállítása",
    "id": "Pengaturan SSL",
    "it": "Configurazione SSL",
    "ja": "SSLのセットアップ",
    "km": "ការដំឡើង SSL",
    "ko": "SSL 설정",
    "lt": "SSL nustatymas",
    "lv": "SSL iestatīšana",
    "nb": "Oppsett av SSL",
    "nl": "SSL instellen",
    "pl": "Konfiguracja SSL",
    "pt": "Configuração de SSL",
    "pt-br": "Configuração de SSL",
    "ru": "Настройка SSL",
    "sk": "Nastavenie SSL",
    "sq": "Konfigurimi i SSL",
    "sr": "Подешавање SSL",
    "sv": "SSL-konfiguration",
    "te": "SSL సెటప్",
    "th": "การตั้งค่า SSL",
    "tr": "SSL Kurulumu",
    "uk": "Налаштування SSL",
    "vi": "Cài đặt SSL",
    "zh-hans": "设置 SSL",
    "zh-hant": "設定 SSL",
}

DESCRIPTIONS = {
    "ar": "تكوين HTTPS لخادم rtSurvey الخاص بك. مطلوب قبل تسجيل الدخول.",
    "bg": "Конфигуриране на HTTPS за вашия сървър rtSurvey. Необходимо преди влизане.",
    "cs": "Nakonfigurujte HTTPS pro váš server rtSurvey. Vyžadováno před přihlášením.",
    "da": "Konfigurer HTTPS til din rtSurvey-server. Påkrævet inden du kan logge ind.",
    "de": "Konfigurieren Sie HTTPS für Ihren rtSurvey-Server. Erforderlich vor der Anmeldung.",
    "el": "Διαμορφώστε HTTPS για τον διακομιστή rtSurvey. Απαιτείται πριν από τη σύνδεση.",
    "es": "Configure HTTPS para su servidor rtSurvey. Requerido antes de iniciar sesión.",
    "fi": "Määritä HTTPS rtSurvey-palvelimellesi. Vaaditaan ennen kirjautumista.",
    "fr": "Configurez HTTPS pour votre serveur rtSurvey. Requis avant de vous connecter.",
    "hi": "अपने rtSurvey सर्वर के लिए HTTPS कॉन्फ़िगर करें। लॉगिन से पहले आवश्यक।",
    "hu": "Konfigurálja a HTTPS-t az rtSurvey szerverhez. Bejelentkezés előtt szükséges.",
    "id": "Konfigurasikan HTTPS untuk server rtSurvey Anda. Diperlukan sebelum login.",
    "it": "Configura HTTPS per il tuo server rtSurvey. Richiesto prima di accedere.",
    "ja": "rtSurveyサーバーのHTTPSを設定します。ログイン前に必要です。",
    "km": "កំណត់រចនាសម្ព័ន្ធ HTTPS សម្រាប់ម៉ាស៊ីនបម្រើ rtSurvey របស់អ្នក។ ត្រូវការមុនពេលចូល។",
    "ko": "rtSurvey 서버에 HTTPS를 구성합니다. 로그인 전에 필요합니다.",
    "lt": "Sukonfigūruokite HTTPS savo rtSurvey serveriui. Reikalinga prieš prisijungimą.",
    "lv": "Konfigurējiet HTTPS savam rtSurvey serverim. Nepieciešams pirms pieteikšanās.",
    "nb": "Konfigurer HTTPS for din rtSurvey-server. Påkrevd før innlogging.",
    "nl": "Configureer HTTPS voor uw rtSurvey-server. Vereist voor aanmelden.",
    "pl": "Skonfiguruj HTTPS dla swojego serwera rtSurvey. Wymagane przed zalogowaniem.",
    "pt": "Configure HTTPS para o seu servidor rtSurvey. Necessário antes de iniciar sessão.",
    "pt-br": "Configure HTTPS para seu servidor rtSurvey. Necessário antes de fazer login.",
    "ru": "Настройте HTTPS для вашего сервера rtSurvey. Требуется до входа в систему.",
    "sk": "Nakonfigurujte HTTPS pre váš server rtSurvey. Vyžaduje sa pred prihlásením.",
    "sq": "Konfiguroni HTTPS për serverin tuaj rtSurvey. Kërkohet para hyrjes.",
    "sr": "Конфигуришите HTTPS за ваш rtSurvey сервер. Потребно пре пријављивања.",
    "sv": "Konfigurera HTTPS för din rtSurvey-server. Krävs innan inloggning.",
    "te": "మీ rtSurvey సర్వర్ కోసం HTTPS కాన్ఫిగర్ చేయండి. లాగిన్ కు ముందు అవసరం.",
    "th": "กำหนดค่า HTTPS สำหรับเซิร์ฟเวอร์ rtSurvey ของคุณ จำเป็นก่อนเข้าสู่ระบบ",
    "tr": "rtSurvey sunucunuz için HTTPS yapılandırın. Giriş yapmadan önce gereklidir.",
    "uk": "Налаштуйте HTTPS для вашого сервера rtSurvey. Потрібно до входу в систему.",
    "vi": "Cấu hình HTTPS cho máy chủ rtSurvey của bạn. Bắt buộc trước khi đăng nhập.",
    "zh-hans": "为您的 rtSurvey 服务器配置 HTTPS。登录前必须完成。",
    "zh-hant": "為您的 rtSurvey 伺服器設定 HTTPS。登入前必須完成。",
}

# Shared body template (same structure for all langs — translate key phrases)
BODIES = {
    "ar": """يجب تكوين SSL قبل تسجيل الدخول. عند فتح التطبيق لأول مرة، ستتم إعادة توجيهك تلقائياً إلى شاشة إعداد SSL.

---

## خيارات إعداد SSL

![خيارات إعداد SSL](/img/ssl-setup/ssl-setup-options.png)

اختر أحد الخيارات الثلاثة:

| الخيار | متى تستخدمه |
|--------|-------------|
| **نطاق فرعي مجاني من rtsurvey.com** *(موصى به)* | لا حاجة لإعداد DNS. نقوم بإنشاء السجل نيابةً عنك. جاهز في 2–5 دقائق. |
| **نطاقي الخاص** | لديك نطاق بالفعل ويشير DNS الخاص به إلى هذا الخادم. |
| **تثبيت الشهادة يدوياً** | للمؤسسات أو CA مخصص. يتطلب وصول SSH. |

---

## الخيار 1 — نطاق فرعي مجاني من rtsurvey.com *(موصى به)*

هذا هو الخيار الأسرع. لا حاجة لتسجيل نطاق أو تغييرات DNS.

1. انقر على **نطاق فرعي مجاني من rtsurvey.com** لتوسيع القسم
2. اكتب اسم النطاق الفرعي المطلوب في حقل الإدخال

   > استخدم أحرفاً صغيرة وأرقاماً وشرطات. 3–30 حرفاً.
   > مثال: `myproject` ← `myproject.rtsurvey.com`

3. انقر على **إنشاء https://[subdomain].rtsurvey.com**

<!-- SCREENSHOT NEEDED: subdomain input filled in, before clicking Create -->

4. انتظر 2–5 دقائق أثناء إصدار الشهادة

<!-- SCREENSHOT NEEDED: certificate being issued / progress state -->

5. بمجرد جاهزية الشهادة، ستتم إعادة توجيهك تلقائياً إلى عنوان HTTPS الجديد

<!-- SCREENSHOT NEEDED: success state / redirect to login -->

---

## الخيار 2 — نطاقي الخاص

استخدم هذا إذا كان لديك نطاق موجود وسجل DNS `A` يشير بالفعل إلى IP هذا الخادم.

1. انقر على **نطاقي الخاص** لتوسيع القسم
2. أدخل اسم النطاق الكامل (مثل `survey.myorganization.org`)
3. انقر على **إنشاء شهادة**

<!-- SCREENSHOT NEEDED: own domain input form -->

سيتحقق Let's Encrypt من نطاقك ويصدر شهادة. يتطلب ذلك توجيه DNS بشكل صحيح مسبقاً — وإلا سيفشل الطلب.

---

## الخيار 3 — تثبيت الشهادة يدوياً

لبيئات المؤسسات التي تستخدم CA مخصصاً أو داخلياً. ستضع ملفات الشهادة على الخادم عبر SSH ثم تدخل نطاقك في التطبيق.

### المتطلبات الأساسية

- وصول SSH إلى الخادم
- شهادة صالحة ومفتاح خاص لنطاقك (بتنسيق PEM)

### الخطوة 1 — الاتصال بالخادم عبر SSH

```bash
ssh root@<server-ip>
```

### الخطوة 2 — وضع ملفات الشهادة

أنشئ المجلد وانسخ ملفاتك:

```bash
mkdir -p /etc/letsencrypt/live/<your-domain>
```

انسخ ملفاتك إلى ذلك المجلد بهذه الأسماء الدقيقة:

| الملف | الوصف |
|-------|-------|
| `fullchain.pem` | شهادتك + أي شهادات CA وسيطة (مدمجة) |
| `privkey.pem` | مفتاحك الخاص |

مثال:

```bash
# نسخ من جهازك المحلي (شغّل هذا محلياً، ليس على الخادم)
scp fullchain.pem root@<server-ip>:/etc/letsencrypt/live/<your-domain>/fullchain.pem
scp privkey.pem  root@<server-ip>:/etc/letsencrypt/live/<your-domain>/privkey.pem
```

تعيين الصلاحيات الصحيحة:

```bash
chmod 644 /etc/letsencrypt/live/<your-domain>/fullchain.pem
chmod 600 /etc/letsencrypt/live/<your-domain>/privkey.pem
```

### الخطوة 3 — إدخال نطاقك في التطبيق

<!-- SCREENSHOT NEEDED: manual certificate form -->

1. في شاشة إعداد SSL، انقر على **تثبيت الشهادة يدوياً**
2. أدخل اسم نطاقك (يجب أن يتطابق مع الاسم الشائع للشهادة أو SAN)
3. انقر على **تطبيق**

سيقوم الخادم بتكوين Nginx مع شهادتك وإعادة التحميل تلقائياً.

---

## الخطوة التالية

بعد تفعيل SSL، انتقل إلى [تسجيل الدخول الأول](first-login).
""",
    "bg": """SSL трябва да е конфигуриран преди да можете да влезете. Когато отворите приложението за първи път, ще бъдете автоматично пренасочени към екрана за настройка на SSL.

---

## Опции за настройка на SSL

![Опции за настройка на SSL](/img/ssl-setup/ssl-setup-options.png)

Изберете една от трите опции:

| Опция | Кога да използвате |
|-------|-------------------|
| **Безплатен поддомейн rtsurvey.com** *(Препоръчително)* | Не е необходима настройка на DNS. Ние създаваме записа вместо вас. Готово за 2–5 минути. |
| **Мой собствен домейн** | Вече имате домейн и DNS му сочи към този сървър. |
| **Ръчно инсталиране на сертификат** | Корпоративна или персонализирана CA. Изисква SSH достъп. |

---

## Опция 1 — Безплатен поддомейн rtsurvey.com *(Препоръчително)*

Това е най-бързата опция. Не се изисква регистрация на домейн или промени в DNS.

1. Кликнете върху **Безплатен поддомейн rtsurvey.com** за разширяване на секцията
2. Въведете желаното име на поддомейн в полето за въвеждане

   > Използвайте малки букви, цифри и тирета. 3–30 символа.
   > Пример: `myproject` → `myproject.rtsurvey.com`

3. Кликнете на **Създай https://[subdomain].rtsurvey.com**

<!-- SCREENSHOT NEEDED: subdomain input filled in, before clicking Create -->

4. Изчакайте 2–5 минути, докато се издаде сертификатът

<!-- SCREENSHOT NEEDED: certificate being issued / progress state -->

5. Веднъж готов, ще бъдете автоматично пренасочени към новия HTTPS адрес

<!-- SCREENSHOT NEEDED: success state / redirect to login -->

---

## Опция 2 — Мой собствен домейн

Използвайте, ако имате съществуващ домейн и DNS `A` записът вече сочи към IP-то на сървъра.

1. Кликнете върху **Мой собствен домейн** за разширяване
2. Въведете пълното си домейн име (напр. `survey.myorganization.org`)
3. Кликнете на **Създай сертификат**

<!-- SCREENSHOT NEEDED: own domain input form -->

Let's Encrypt ще провери домейна ви и ще издаде сертификат. Изисква DNS да е правилно насочен — иначе заявката ще се провали.

---

## Опция 3 — Ръчно инсталиране на сертификат

За корпоративни среди с персонализиран или вътрешен CA. Поставяте файловете на сертификата на сървъра чрез SSH, след което въвеждате домейна си в приложението.

### Предварителни изисквания

- SSH достъп до сървъра
- Валиден сертификат и частен ключ за вашия домейн (PEM формат)

### Стъпка 1 — SSH към сървъра

```bash
ssh root@<server-ip>
```

### Стъпка 2 — Поставете файловете на сертификата

Създайте директорията и копирайте файловете:

```bash
mkdir -p /etc/letsencrypt/live/<your-domain>
```

Копирайте файловете с точните имена:

| Файл | Описание |
|------|---------|
| `fullchain.pem` | Вашият сертификат + всички междинни CA сертификати (конкатенирани) |
| `privkey.pem` | Вашият частен ключ |

Пример:

```bash
# Копирайте от локалната машина (изпълнете локално, не на сървъра)
scp fullchain.pem root@<server-ip>:/etc/letsencrypt/live/<your-domain>/fullchain.pem
scp privkey.pem  root@<server-ip>:/etc/letsencrypt/live/<your-domain>/privkey.pem
```

Задайте правилни разрешения:

```bash
chmod 644 /etc/letsencrypt/live/<your-domain>/fullchain.pem
chmod 600 /etc/letsencrypt/live/<your-domain>/privkey.pem
```

### Стъпка 3 — Въведете домейна в приложението

<!-- SCREENSHOT NEEDED: manual certificate form -->

1. В екрана за настройка на SSL кликнете върху **Ръчно инсталиране на сертификат**
2. Въведете вашето домейн име (трябва да съответства на Common Name или SAN на сертификата)
3. Кликнете на **Приложи**

Сървърът ще конфигурира Nginx с вашия сертификат и ще се презареди автоматично.

---

## Следваща стъпка

Веднъж активен SSL, преминете към [Първо влизане](first-login).
""",
    "cs": """SSL musí být nakonfigurován, než se budete moci přihlásit. Když otevřete aplikaci poprvé, budete automaticky přesměrováni na obrazovku nastavení SSL.

---

## Možnosti nastavení SSL

![Možnosti nastavení SSL](/img/ssl-setup/ssl-setup-options.png)

Zvolte jednu ze tří možností:

| Možnost | Kdy použít |
|---------|-----------|
| **Bezplatná subdoména rtsurvey.com** *(Doporučeno)* | Není potřeba nastavení DNS. Záznam vytvoříme za vás. Připraveno za 2–5 minut. |
| **Vlastní doména** | Již máte doménu a její DNS míří na tento server. |
| **Ruční instalace certifikátu** | Podnikové nebo vlastní CA. Vyžaduje přístup SSH. |

---

## Možnost 1 — Bezplatná subdoména rtsurvey.com *(Doporučeno)*

Toto je nejrychlejší možnost. Nevyžaduje registraci domény ani změny DNS.

1. Klikněte na **Bezplatná subdoména rtsurvey.com** pro rozbalení sekce
2. Zadejte požadovaný název subdomény

   > Používejte malá písmena, čísla a pomlčky. 3–30 znaků.
   > Příklad: `myproject` → `myproject.rtsurvey.com`

3. Klikněte na **Vytvořit https://[subdomain].rtsurvey.com**

<!-- SCREENSHOT NEEDED: subdomain input filled in, before clicking Create -->

4. Počkejte 2–5 minut na vydání certifikátu

<!-- SCREENSHOT NEEDED: certificate being issued / progress state -->

5. Jakmile je certifikát připraven, budete automaticky přesměrováni na novou HTTPS adresu

<!-- SCREENSHOT NEEDED: success state / redirect to login -->

---

## Možnost 2 — Vlastní doména

Použijte, pokud máte existující doménu a její DNS `A` záznam již míří na IP tohoto serveru.

1. Klikněte na **Vlastní doména** pro rozbalení
2. Zadejte celé doménové jméno (např. `survey.myorganization.org`)
3. Klikněte na **Vytvořit certifikát**

<!-- SCREENSHOT NEEDED: own domain input form -->

Let's Encrypt ověří vaši doménu a vydá certifikát. DNS musí být správně nastaven předem — jinak požadavek selže.

---

## Možnost 3 — Ruční instalace certifikátu

Pro podniková prostředí s vlastním nebo interním CA. Umístíte soubory certifikátu na server přes SSH a poté zadáte doménu v aplikaci.

### Předpoklady

- SSH přístup k serveru
- Platný certifikát a privátní klíč pro vaši doménu (formát PEM)

### Krok 1 — SSH na server

```bash
ssh root@<server-ip>
```

### Krok 2 — Umístěte soubory certifikátu

Vytvořte adresář a zkopírujte soubory:

```bash
mkdir -p /etc/letsencrypt/live/<your-domain>
```

Zkopírujte soubory s přesnými názvy:

| Soubor | Popis |
|--------|-------|
| `fullchain.pem` | Váš certifikát + mezilehlé CA certifikáty (zřetězené) |
| `privkey.pem` | Váš privátní klíč |

Příklad:

```bash
# Kopírování z lokálního počítače (spusťte lokálně, ne na serveru)
scp fullchain.pem root@<server-ip>:/etc/letsencrypt/live/<your-domain>/fullchain.pem
scp privkey.pem  root@<server-ip>:/etc/letsencrypt/live/<your-domain>/privkey.pem
```

Nastavte správná oprávnění:

```bash
chmod 644 /etc/letsencrypt/live/<your-domain>/fullchain.pem
chmod 600 /etc/letsencrypt/live/<your-domain>/privkey.pem
```

### Krok 3 — Zadejte doménu v aplikaci

<!-- SCREENSHOT NEEDED: manual certificate form -->

1. Na obrazovce nastavení SSL klikněte na **Ruční instalace certifikátu**
2. Zadejte doménové jméno (musí odpovídat Common Name nebo SAN certifikátu)
3. Klikněte na **Použít**

Server nakonfiguruje Nginx s vaším certifikátem a automaticky se znovu načte.

---

## Další krok

Jakmile je SSL aktivní, pokračujte na [První přihlášení](first-login).
""",
    "da": """SSL skal konfigureres, inden du kan logge ind. Når du åbner appen for første gang, vil du automatisk blive omdirigeret til SSL-opsætningsskærmen.

---

## SSL-opsætningsindstillinger

![SSL-opsætningsindstillinger](/img/ssl-setup/ssl-setup-options.png)

Vælg en af tre muligheder:

| Mulighed | Hvornår du bruger den |
|----------|----------------------|
| **Gratis rtsurvey.com-underdomæne** *(Anbefalet)* | Ingen DNS-opsætning nødvendig. Vi opretter posten for dig. Klar på 2–5 minutter. |
| **Mit eget domæne** | Du har allerede et domæne, og dets DNS peger på denne server. |
| **Installer certifikat manuelt** | Virksomhed eller brugerdefineret CA. Kræver SSH-adgang. |

---

## Mulighed 1 — Gratis rtsurvey.com-underdomæne *(Anbefalet)*

Dette er den hurtigste mulighed. Ingen domæneregistrering eller DNS-ændringer påkrævet.

1. Klik på **Gratis rtsurvey.com-underdomæne** for at udvide sektionen
2. Skriv det ønskede underdomænenavn i inputfeltet

   > Brug små bogstaver, tal og bindestreger. 3–30 tegn.
   > Eksempel: `myproject` → `myproject.rtsurvey.com`

3. Klik på **Opret https://[subdomain].rtsurvey.com**

<!-- SCREENSHOT NEEDED: subdomain input filled in, before clicking Create -->

4. Vent 2–5 minutter, mens certifikatet udstedes

<!-- SCREENSHOT NEEDED: certificate being issued / progress state -->

5. Når certifikatet er klar, vil du automatisk blive omdirigeret til din nye HTTPS-adresse

<!-- SCREENSHOT NEEDED: success state / redirect to login -->

---

## Mulighed 2 — Mit eget domæne

Brug dette, hvis du har et eksisterende domæne, og dets DNS `A`-post allerede peger på denne servers IP.

1. Klik på **Mit eget domæne** for at udvide sektionen
2. Indtast dit fulde domænenavn (f.eks. `survey.myorganization.org`)
3. Klik på **Opret certifikat**

<!-- SCREENSHOT NEEDED: own domain input form -->

Let's Encrypt vil verificere dit domæne og udstede et certifikat. DNS skal være korrekt peget på forhånd — ellers vil anmodningen mislykkes.

---

## Mulighed 3 — Installer certifikat manuelt

Til virksomhedsmiljøer med en brugerdefineret eller intern CA. Du placerer certifikatfilerne på serveren via SSH og angiver derefter dit domæne i appen.

### Forudsætninger

- SSH-adgang til serveren
- Gyldigt certifikat og privat nøgle til dit domæne (PEM-format)

### Trin 1 — SSH til serveren

```bash
ssh root@<server-ip>
```

### Trin 2 — Placer dine certifikatfiler

Opret mappen og kopiér dine filer:

```bash
mkdir -p /etc/letsencrypt/live/<your-domain>
```

Kopiér filerne med disse præcise navne:

| Fil | Beskrivelse |
|-----|-------------|
| `fullchain.pem` | Dit certifikat + eventuelle mellemliggende CA-certifikater (sammenkædet) |
| `privkey.pem` | Din private nøgle |

Eksempel:

```bash
# Kopiér fra din lokale maskine (kør dette lokalt, ikke på serveren)
scp fullchain.pem root@<server-ip>:/etc/letsencrypt/live/<your-domain>/fullchain.pem
scp privkey.pem  root@<server-ip>:/etc/letsencrypt/live/<your-domain>/privkey.pem
```

Sæt korrekte tilladelser:

```bash
chmod 644 /etc/letsencrypt/live/<your-domain>/fullchain.pem
chmod 600 /etc/letsencrypt/live/<your-domain>/privkey.pem
```

### Trin 3 — Angiv dit domæne i appen

<!-- SCREENSHOT NEEDED: manual certificate form -->

1. På SSL-opsætningsskærmen klikker du på **Installer certifikat manuelt**
2. Angiv dit domænenavn (skal svare til certifikatets Common Name eller SAN)
3. Klik på **Anvend**

Serveren vil konfigurere Nginx med dit certifikat og genindlæse automatisk.

---

## Næste trin

Når SSL er aktivt, fortsæt til [Første login](first-login).
""",
    "de": """SSL muss konfiguriert werden, bevor Sie sich anmelden können. Wenn Sie die App zum ersten Mal öffnen, werden Sie automatisch zum SSL-Einrichtungsbildschirm weitergeleitet.

---

## SSL-Einrichtungsoptionen

![SSL-Einrichtungsoptionen](/img/ssl-setup/ssl-setup-options.png)

Wählen Sie eine von drei Optionen:

| Option | Wann zu verwenden |
|--------|------------------|
| **Kostenlose rtsurvey.com-Subdomain** *(Empfohlen)* | Keine DNS-Einrichtung erforderlich. Wir erstellen den Eintrag für Sie. In 2–5 Minuten bereit. |
| **Eigene Domain** | Sie haben bereits eine Domain und deren DNS zeigt auf diesen Server. |
| **Zertifikat manuell installieren** | Unternehmen oder benutzerdefinierte CA. Erfordert SSH-Zugang. |

---

## Option 1 — Kostenlose rtsurvey.com-Subdomain *(Empfohlen)*

Dies ist die schnellste Option. Keine Domain-Registrierung oder DNS-Änderungen erforderlich.

1. Klicken Sie auf **Kostenlose rtsurvey.com-Subdomain**, um den Abschnitt zu erweitern
2. Geben Sie den gewünschten Subdomain-Namen im Eingabefeld ein

   > Verwenden Sie Kleinbuchstaben, Zahlen und Bindestriche. 3–30 Zeichen.
   > Beispiel: `myproject` → `myproject.rtsurvey.com`

3. Klicken Sie auf **https://[subdomain].rtsurvey.com erstellen**

<!-- SCREENSHOT NEEDED: subdomain input filled in, before clicking Create -->

4. Warten Sie 2–5 Minuten, während das Zertifikat ausgestellt wird

<!-- SCREENSHOT NEEDED: certificate being issued / progress state -->

5. Sobald das Zertifikat bereit ist, werden Sie automatisch zur neuen HTTPS-URL weitergeleitet

<!-- SCREENSHOT NEEDED: success state / redirect to login -->

---

## Option 2 — Eigene Domain

Verwenden Sie dies, wenn Sie eine vorhandene Domain haben und deren DNS `A`-Eintrag bereits auf die IP dieses Servers zeigt.

1. Klicken Sie auf **Eigene Domain**, um den Abschnitt zu erweitern
2. Geben Sie Ihren vollständigen Domainnamen ein (z.B. `survey.myorganization.org`)
3. Klicken Sie auf **Zertifikat erstellen**

<!-- SCREENSHOT NEEDED: own domain input form -->

Let's Encrypt verifiziert Ihre Domain und stellt ein Zertifikat aus. DNS muss vorher korrekt eingerichtet sein — sonst schlägt die Anfrage fehl.

---

## Option 3 — Zertifikat manuell installieren

Für Unternehmensumgebungen mit einer benutzerdefinierten oder internen CA. Sie platzieren Ihre Zertifikatsdateien per SSH auf dem Server und geben dann Ihre Domain in der App ein.

### Voraussetzungen

- SSH-Zugang zum Server
- Gültiges Zertifikat und privater Schlüssel für Ihre Domain (PEM-Format)

### Schritt 1 — SSH auf den Server

```bash
ssh root@<server-ip>
```

### Schritt 2 — Zertifikatsdateien platzieren

Verzeichnis erstellen und Dateien kopieren:

```bash
mkdir -p /etc/letsencrypt/live/<your-domain>
```

Dateien mit diesen genauen Namen kopieren:

| Datei | Beschreibung |
|-------|-------------|
| `fullchain.pem` | Ihr Zertifikat + alle Zwischen-CA-Zertifikate (verkettet) |
| `privkey.pem` | Ihr privater Schlüssel |

Beispiel:

```bash
# Von Ihrem lokalen Rechner kopieren (lokal ausführen, nicht auf dem Server)
scp fullchain.pem root@<server-ip>:/etc/letsencrypt/live/<your-domain>/fullchain.pem
scp privkey.pem  root@<server-ip>:/etc/letsencrypt/live/<your-domain>/privkey.pem
```

Korrekte Berechtigungen setzen:

```bash
chmod 644 /etc/letsencrypt/live/<your-domain>/fullchain.pem
chmod 600 /etc/letsencrypt/live/<your-domain>/privkey.pem
```

### Schritt 3 — Domain in der App eingeben

<!-- SCREENSHOT NEEDED: manual certificate form -->

1. Klicken Sie auf dem SSL-Einrichtungsbildschirm auf **Zertifikat manuell installieren**
2. Geben Sie Ihren Domainnamen ein (muss mit dem Common Name oder SAN des Zertifikats übereinstimmen)
3. Klicken Sie auf **Anwenden**

Der Server konfiguriert Nginx mit Ihrem Zertifikat und lädt automatisch neu.

---

## Nächster Schritt

Sobald SSL aktiv ist, fahren Sie mit der [Ersten Anmeldung](first-login) fort.
""",
    "el": """Το SSL πρέπει να διαμορφωθεί πριν μπορέσετε να συνδεθείτε. Όταν ανοίγετε την εφαρμογή για πρώτη φορά, θα ανακατευθυνθείτε αυτόματα στην οθόνη ρύθμισης SSL.

---

## Επιλογές ρύθμισης SSL

![Επιλογές ρύθμισης SSL](/img/ssl-setup/ssl-setup-options.png)

Επιλέξτε μία από τρεις επιλογές:

| Επιλογή | Πότε να χρησιμοποιηθεί |
|---------|----------------------|
| **Δωρεάν υποτομέας rtsurvey.com** *(Συνιστάται)* | Δεν απαιτείται ρύθμιση DNS. Δημιουργούμε την εγγραφή για εσάς. Έτοιμο σε 2–5 λεπτά. |
| **Δικός μου τομέας** | Έχετε ήδη έναν τομέα και το DNS του δείχνει σε αυτόν τον διακομιστή. |
| **Χειροκίνητη εγκατάσταση πιστοποιητικού** | Επιχείρηση ή προσαρμοσμένη CA. Απαιτεί πρόσβαση SSH. |

---

## Επιλογή 1 — Δωρεάν υποτομέας rtsurvey.com *(Συνιστάται)*

Αυτή είναι η πιο γρήγορη επιλογή. Δεν απαιτείται εγγραφή τομέα ή αλλαγές DNS.

1. Κάντε κλικ στο **Δωρεάν υποτομέας rtsurvey.com** για να αναπτύξετε την ενότητα
2. Πληκτρολογήστε το επιθυμητό όνομα υποτομέα

   > Χρησιμοποιήστε πεζά γράμματα, αριθμούς και παύλες. 3–30 χαρακτήρες.
   > Παράδειγμα: `myproject` → `myproject.rtsurvey.com`

3. Κάντε κλικ στο **Δημιουργία https://[subdomain].rtsurvey.com**

<!-- SCREENSHOT NEEDED: subdomain input filled in, before clicking Create -->

4. Αναμείνετε 2–5 λεπτά ενώ εκδίδεται το πιστοποιητικό

<!-- SCREENSHOT NEEDED: certificate being issued / progress state -->

5. Μόλις το πιστοποιητικό είναι έτοιμο, θα ανακατευθυνθείτε αυτόματα στη νέα HTTPS διεύθυνση

<!-- SCREENSHOT NEEDED: success state / redirect to login -->

---

## Επιλογή 2 — Δικός μου τομέας

Χρησιμοποιήστε εάν έχετε υπάρχοντα τομέα και η εγγραφή DNS `A` δείχνει ήδη στην IP αυτού του διακομιστή.

1. Κάντε κλικ στο **Δικός μου τομέας** για ανάπτυξη
2. Εισαγάγετε το πλήρες όνομα τομέα (π.χ. `survey.myorganization.org`)
3. Κάντε κλικ στο **Δημιουργία πιστοποιητικού**

<!-- SCREENSHOT NEEDED: own domain input form -->

Το Let's Encrypt θα επαληθεύσει τον τομέα σας και θα εκδώσει πιστοποιητικό. Απαιτείται σωστή ρύθμιση DNS εκ των προτέρων — διαφορετικά η αίτηση θα αποτύχει.

---

## Επιλογή 3 — Χειροκίνητη εγκατάσταση πιστοποιητικού

Για εταιρικά περιβάλλοντα με προσαρμοσμένη ή εσωτερική CA. Τοποθετείτε τα αρχεία πιστοποιητικού στον διακομιστή μέσω SSH και στη συνέχεια εισάγετε τον τομέα σας στην εφαρμογή.

### Προαπαιτούμενα

- SSH πρόσβαση στον διακομιστή
- Έγκυρο πιστοποιητικό και ιδιωτικό κλειδί για τον τομέα σας (μορφή PEM)

### Βήμα 1 — SSH στον διακομιστή

```bash
ssh root@<server-ip>
```

### Βήμα 2 — Τοποθετήστε τα αρχεία πιστοποιητικού

Δημιουργήστε τον κατάλογο και αντιγράψτε τα αρχεία:

```bash
mkdir -p /etc/letsencrypt/live/<your-domain>
```

Αντιγράψτε τα αρχεία με ακριβώς αυτά τα ονόματα:

| Αρχείο | Περιγραφή |
|--------|----------|
| `fullchain.pem` | Πιστοποιητικό + ενδιάμεσα CA πιστοποιητικά (ενοποιημένα) |
| `privkey.pem` | Ιδιωτικό κλειδί |

Παράδειγμα:

```bash
# Αντιγραφή από τοπικό μηχάνημα (εκτελέστε τοπικά, όχι στον διακομιστή)
scp fullchain.pem root@<server-ip>:/etc/letsencrypt/live/<your-domain>/fullchain.pem
scp privkey.pem  root@<server-ip>:/etc/letsencrypt/live/<your-domain>/privkey.pem
```

Ορίστε σωστά δικαιώματα:

```bash
chmod 644 /etc/letsencrypt/live/<your-domain>/fullchain.pem
chmod 600 /etc/letsencrypt/live/<your-domain>/privkey.pem
```

### Βήμα 3 — Εισαγάγετε τον τομέα στην εφαρμογή

<!-- SCREENSHOT NEEDED: manual certificate form -->

1. Στην οθόνη ρύθμισης SSL, κάντε κλικ στο **Χειροκίνητη εγκατάσταση πιστοποιητικού**
2. Εισαγάγετε το όνομα τομέα (πρέπει να ταιριάζει με το Common Name ή SAN του πιστοποιητικού)
3. Κάντε κλικ στο **Εφαρμογή**

Ο διακομιστής θα διαμορφώσει το Nginx με το πιστοποιητικό σας και θα επανεκκινήσει αυτόματα.

---

## Επόμενο βήμα

Μόλις το SSL είναι ενεργό, προχωρήστε στην [Πρώτη Σύνδεση](first-login).
""",
    "es": """SSL debe configurarse antes de que pueda iniciar sesión. Cuando abra la aplicación por primera vez, será redirigido automáticamente a la pantalla de configuración de SSL.

---

## Opciones de configuración SSL

![Opciones de configuración SSL](/img/ssl-setup/ssl-setup-options.png)

Elija una de tres opciones:

| Opción | Cuándo usar |
|--------|-------------|
| **Subdominio gratuito rtsurvey.com** *(Recomendado)* | No se necesita configuración DNS. Creamos el registro por usted. Listo en 2–5 minutos. |
| **Mi propio dominio** | Ya tiene un dominio y su DNS apunta a este servidor. |
| **Instalar certificado manualmente** | Empresa o CA personalizado. Requiere acceso SSH. |

---

## Opción 1 — Subdominio gratuito rtsurvey.com *(Recomendado)*

Esta es la opción más rápida. No se requiere registro de dominio ni cambios DNS.

1. Haga clic en **Subdominio gratuito rtsurvey.com** para expandir la sección
2. Escriba el nombre de subdominio deseado en el campo de entrada

   > Use letras minúsculas, números y guiones. 3–30 caracteres.
   > Ejemplo: `myproject` → `myproject.rtsurvey.com`

3. Haga clic en **Crear https://[subdomain].rtsurvey.com**

<!-- SCREENSHOT NEEDED: subdomain input filled in, before clicking Create -->

4. Espere 2–5 minutos mientras se emite el certificado

<!-- SCREENSHOT NEEDED: certificate being issued / progress state -->

5. Una vez listo el certificado, será redirigido automáticamente a su nueva URL HTTPS

<!-- SCREENSHOT NEEDED: success state / redirect to login -->

---

## Opción 2 — Mi propio dominio

Use esto si tiene un dominio existente y su registro DNS `A` ya apunta a la IP de este servidor.

1. Haga clic en **Mi propio dominio** para expandir la sección
2. Ingrese su nombre de dominio completo (p.ej. `survey.myorganization.org`)
3. Haga clic en **Crear certificado**

<!-- SCREENSHOT NEEDED: own domain input form -->

Let's Encrypt verificará su dominio y emitirá un certificado. Requiere que el DNS esté correctamente apuntado primero — la solicitud fallará de lo contrario.

---

## Opción 3 — Instalar certificado manualmente

Para entornos empresariales con CA personalizado o interno. Colocará sus archivos de certificado en el servidor mediante SSH y luego ingresará su dominio en la aplicación.

### Requisitos previos

- Acceso SSH al servidor
- Certificado válido y clave privada para su dominio (formato PEM)

### Paso 1 — SSH al servidor

```bash
ssh root@<server-ip>
```

### Paso 2 — Coloque sus archivos de certificado

Cree el directorio y copie sus archivos:

```bash
mkdir -p /etc/letsencrypt/live/<your-domain>
```

Copie sus archivos con estos nombres exactos:

| Archivo | Descripción |
|---------|-------------|
| `fullchain.pem` | Su certificado + certificados CA intermedios (concatenados) |
| `privkey.pem` | Su clave privada |

Ejemplo:

```bash
# Copiar desde su máquina local (ejecutar localmente, no en el servidor)
scp fullchain.pem root@<server-ip>:/etc/letsencrypt/live/<your-domain>/fullchain.pem
scp privkey.pem  root@<server-ip>:/etc/letsencrypt/live/<your-domain>/privkey.pem
```

Establecer permisos correctos:

```bash
chmod 644 /etc/letsencrypt/live/<your-domain>/fullchain.pem
chmod 600 /etc/letsencrypt/live/<your-domain>/privkey.pem
```

### Paso 3 — Ingrese su dominio en la aplicación

<!-- SCREENSHOT NEEDED: manual certificate form -->

1. En la pantalla de configuración SSL, haga clic en **Instalar certificado manualmente**
2. Ingrese su nombre de dominio (debe coincidir con el Common Name o SAN del certificado)
3. Haga clic en **Aplicar**

El servidor configurará Nginx con su certificado y recargará automáticamente.

---

## Siguiente paso

Una vez que SSL esté activo, proceda al [Primer inicio de sesión](first-login).
""",
    "fi": """SSL on määritettävä ennen kuin voit kirjautua sisään. Kun avaat sovelluksen ensimmäistä kertaa, sinut ohjataan automaattisesti SSL-asennusnäytölle.

---

## SSL-asennusvaihtoehdot

![SSL-asennusvaihtoehdot](/img/ssl-setup/ssl-setup-options.png)

Valitse yksi kolmesta vaihtoehdosta:

| Vaihtoehto | Milloin käyttää |
|------------|----------------|
| **Ilmainen rtsurvey.com-alidomaini** *(Suositeltu)* | DNS-asetuksia ei tarvita. Luomme tietueen puolestasi. Valmis 2–5 minuutissa. |
| **Oma domain** | Sinulla on jo domain ja sen DNS osoittaa tähän palvelimeen. |
| **Asenna sertifikaatti manuaalisesti** | Yritys tai mukautettu CA. Vaatii SSH-yhteyden. |

---

## Vaihtoehto 1 — Ilmainen rtsurvey.com-alidomaini *(Suositeltu)*

Tämä on nopein vaihtoehto. Domainin rekisteröintiä tai DNS-muutoksia ei tarvita.

1. Napsauta **Ilmainen rtsurvey.com-alidomaini** laajentaaksesi osiota
2. Kirjoita haluamasi alidomainin nimi syöttökenttään

   > Käytä pieniä kirjaimia, numeroita ja väliviivoja. 3–30 merkkiä.
   > Esimerkki: `myproject` → `myproject.rtsurvey.com`

3. Napsauta **Luo https://[subdomain].rtsurvey.com**

<!-- SCREENSHOT NEEDED: subdomain input filled in, before clicking Create -->

4. Odota 2–5 minuuttia, kun sertifikaattia myönnetään

<!-- SCREENSHOT NEEDED: certificate being issued / progress state -->

5. Kun sertifikaatti on valmis, sinut ohjataan automaattisesti uuteen HTTPS-osoitteeseen

<!-- SCREENSHOT NEEDED: success state / redirect to login -->

---

## Vaihtoehto 2 — Oma domain

Käytä tätä, jos sinulla on olemassa oleva domain ja sen DNS `A`-tietue osoittaa jo tämän palvelimen IP-osoitteeseen.

1. Napsauta **Oma domain** laajentaaksesi osion
2. Syötä koko domainin nimi (esim. `survey.myorganization.org`)
3. Napsauta **Luo sertifikaatti**

<!-- SCREENSHOT NEEDED: own domain input form -->

Let's Encrypt vahvistaa domainisi ja myöntää sertifikaatin. DNS täytyy olla oikein osoitettu ensin — muuten pyyntö epäonnistuu.

---

## Vaihtoehto 3 — Asenna sertifikaatti manuaalisesti

Yritysympäristöille, joissa on mukautettu tai sisäinen CA. Sijoitat sertifikaattitiedostot palvelimelle SSH:n kautta, sitten syötät domainisi sovellukseen.

### Edellytykset

- SSH-yhteys palvelimeen
- Kelvollinen sertifikaatti ja yksityinen avain domainillesi (PEM-muoto)

### Vaihe 1 — SSH palvelimelle

```bash
ssh root@<server-ip>
```

### Vaihe 2 — Sijoita sertifikaattitiedostot

Luo hakemisto ja kopioi tiedostosi:

```bash
mkdir -p /etc/letsencrypt/live/<your-domain>
```

Kopioi tiedostosi näillä tarkkoilla nimillä:

| Tiedosto | Kuvaus |
|----------|--------|
| `fullchain.pem` | Sertifikaattisi + mahdolliset väli-CA-sertifikaatit (yhdistetty) |
| `privkey.pem` | Yksityinen avaimesi |

Esimerkki:

```bash
# Kopioi paikalliselta koneeltasi (suorita paikallisesti, ei palvelimella)
scp fullchain.pem root@<server-ip>:/etc/letsencrypt/live/<your-domain>/fullchain.pem
scp privkey.pem  root@<server-ip>:/etc/letsencrypt/live/<your-domain>/privkey.pem
```

Aseta oikeat käyttöoikeudet:

```bash
chmod 644 /etc/letsencrypt/live/<your-domain>/fullchain.pem
chmod 600 /etc/letsencrypt/live/<your-domain>/privkey.pem
```

### Vaihe 3 — Syötä domain sovellukseen

<!-- SCREENSHOT NEEDED: manual certificate form -->

1. SSL-asennusnäytöllä napsauta **Asenna sertifikaatti manuaalisesti**
2. Syötä domainin nimi (täytyy vastata sertifikaatin Common Name tai SAN)
3. Napsauta **Käytä**

Palvelin konfiguroi Nginxin sertifikaatillasi ja lataa automaattisesti uudelleen.

---

## Seuraava vaihe

Kun SSL on aktiivinen, siirry kohtaan [Ensimmäinen kirjautuminen](first-login).
""",
    "fr": """SSL doit être configuré avant de pouvoir vous connecter. Lorsque vous ouvrez l'application pour la première fois, vous serez automatiquement redirigé vers l'écran de configuration SSL.

---

## Options de configuration SSL

![Options de configuration SSL](/img/ssl-setup/ssl-setup-options.png)

Choisissez l'une des trois options :

| Option | Quand l'utiliser |
|--------|-----------------|
| **Sous-domaine rtsurvey.com gratuit** *(Recommandé)* | Aucune configuration DNS nécessaire. Nous créons l'enregistrement pour vous. Prêt en 2–5 minutes. |
| **Mon propre domaine** | Vous avez déjà un domaine et son DNS pointe vers ce serveur. |
| **Installer le certificat manuellement** | Entreprise ou CA personnalisé. Nécessite un accès SSH. |

---

## Option 1 — Sous-domaine rtsurvey.com gratuit *(Recommandé)*

C'est l'option la plus rapide. Aucun enregistrement de domaine ni modification DNS requis.

1. Cliquez sur **Sous-domaine rtsurvey.com gratuit** pour développer la section
2. Saisissez le nom de sous-domaine souhaité dans le champ de saisie

   > Utilisez des lettres minuscules, des chiffres et des tirets. 3–30 caractères.
   > Exemple : `myproject` → `myproject.rtsurvey.com`

3. Cliquez sur **Créer https://[subdomain].rtsurvey.com**

<!-- SCREENSHOT NEEDED: subdomain input filled in, before clicking Create -->

4. Attendez 2–5 minutes pendant l'émission du certificat

<!-- SCREENSHOT NEEDED: certificate being issued / progress state -->

5. Une fois le certificat prêt, vous serez automatiquement redirigé vers votre nouvelle URL HTTPS

<!-- SCREENSHOT NEEDED: success state / redirect to login -->

---

## Option 2 — Mon propre domaine

Utilisez ceci si vous avez un domaine existant et que son enregistrement DNS `A` pointe déjà vers l'IP de ce serveur.

1. Cliquez sur **Mon propre domaine** pour développer la section
2. Saisissez votre nom de domaine complet (ex. `survey.myorganization.org`)
3. Cliquez sur **Créer le certificat**

<!-- SCREENSHOT NEEDED: own domain input form -->

Let's Encrypt vérifiera votre domaine et émettra un certificat. Le DNS doit être correctement pointé au préalable — sinon la demande échouera.

---

## Option 3 — Installer le certificat manuellement

Pour les environnements d'entreprise utilisant une CA personnalisée ou interne. Vous placerez vos fichiers de certificat sur le serveur via SSH, puis saisirez votre domaine dans l'application.

### Prérequis

- Accès SSH au serveur
- Certificat valide et clé privée pour votre domaine (format PEM)

### Étape 1 — SSH sur le serveur

```bash
ssh root@<server-ip>
```

### Étape 2 — Placer vos fichiers de certificat

Créez le répertoire et copiez vos fichiers :

```bash
mkdir -p /etc/letsencrypt/live/<your-domain>
```

Copiez vos fichiers avec ces noms exacts :

| Fichier | Description |
|---------|-------------|
| `fullchain.pem` | Votre certificat + certificats CA intermédiaires (concaténés) |
| `privkey.pem` | Votre clé privée |

Exemple :

```bash
# Copier depuis votre machine locale (exécuter localement, pas sur le serveur)
scp fullchain.pem root@<server-ip>:/etc/letsencrypt/live/<your-domain>/fullchain.pem
scp privkey.pem  root@<server-ip>:/etc/letsencrypt/live/<your-domain>/privkey.pem
```

Définir les permissions correctes :

```bash
chmod 644 /etc/letsencrypt/live/<your-domain>/fullchain.pem
chmod 600 /etc/letsencrypt/live/<your-domain>/privkey.pem
```

### Étape 3 — Saisir votre domaine dans l'application

<!-- SCREENSHOT NEEDED: manual certificate form -->

1. Sur l'écran de configuration SSL, cliquez sur **Installer le certificat manuellement**
2. Saisissez votre nom de domaine (doit correspondre au Common Name ou SAN du certificat)
3. Cliquez sur **Appliquer**

Le serveur configurera Nginx avec votre certificat et rechargera automatiquement.

---

## Étape suivante

Une fois SSL actif, passez à la [Première connexion](first-login).
""",
}

# For languages not individually written above, use a template based on English
# with key UI strings translated. These cover the remaining 27 languages.
TEMPLATE_LANGS = {
    "hi": {
        "intro": "SSL लॉगिन करने से पहले कॉन्फ़िगर होना चाहिए। जब आप पहली बार ऐप खोलते हैं, तो आप स्वचालित रूप से SSL सेटअप स्क्रीन पर रीडायरेक्ट हो जाएंगे।",
        "opt_title": "SSL सेटअप विकल्प",
        "opt1": "मुफ़्त rtsurvey.com सबडोमेन *(अनुशंसित)*",
        "opt2": "मेरा अपना डोमेन",
        "opt3": "प्रमाणपत्र मैन्युअल रूप से स्थापित करें",
        "next": "अगला कदम",
        "next_text": "SSL सक्रिय होने के बाद, [पहली बार लॉगिन](first-login) पर जाएं।",
    },
    "hu": {
        "intro": "Az SSL-t be kell állítani, mielőtt bejelentkezhet. Amikor először megnyitja az alkalmazást, automatikusan az SSL beállítási képernyőre irányítja át.",
        "opt_title": "SSL beállítási lehetőségek",
        "opt1": "Ingyenes rtsurvey.com aldomainen *(Ajánlott)*",
        "opt2": "Saját domainem",
        "opt3": "Tanúsítvány manuális telepítése",
        "next": "Következő lépés",
        "next_text": "Miután az SSL aktív, folytassa az [Első bejelentkezéssel](first-login).",
    },
    "id": {
        "intro": "SSL harus dikonfigurasi sebelum Anda dapat masuk. Saat membuka aplikasi untuk pertama kali, Anda akan otomatis diarahkan ke layar pengaturan SSL.",
        "opt_title": "Opsi pengaturan SSL",
        "opt1": "Subdomain rtsurvey.com gratis *(Direkomendasikan)*",
        "opt2": "Domain saya sendiri",
        "opt3": "Instal sertifikat secara manual",
        "next": "Langkah berikutnya",
        "next_text": "Setelah SSL aktif, lanjutkan ke [Login Pertama](first-login).",
    },
    "it": {
        "intro": "SSL deve essere configurato prima di poter accedere. Quando si apre l'applicazione per la prima volta, verrà reindirizzato automaticamente alla schermata di configurazione SSL.",
        "opt_title": "Opzioni di configurazione SSL",
        "opt1": "Sottodominio gratuito rtsurvey.com *(Consigliato)*",
        "opt2": "Il mio dominio",
        "opt3": "Installa certificato manualmente",
        "next": "Passo successivo",
        "next_text": "Una volta SSL attivo, procedere al [Primo accesso](first-login).",
    },
    "ja": {
        "intro": "SSL はログインする前に設定する必要があります。アプリを初めて開くと、SSL セットアップ画面に自動的にリダイレクトされます。",
        "opt_title": "SSL セットアップオプション",
        "opt1": "無料の rtsurvey.com サブドメイン *(推奨)*",
        "opt2": "独自ドメイン",
        "opt3": "証明書を手動でインストール",
        "next": "次のステップ",
        "next_text": "SSL が有効になったら、[初回ログイン](first-login) に進んでください。",
    },
    "km": {
        "intro": "SSL ត្រូវតែកំណត់រចនាសម្ព័ន្ធមុនពេលអ្នកអាចចូលបាន។ នៅពេលអ្នកបើកកម្មវិធីជាលើកដំបូង អ្នកនឹងត្រូវបានបញ្ជូនទៅអេក្រង់ដំឡើង SSL ដោយស្វ័យប្រវត្តិ។",
        "opt_title": "ជម្រើសដំឡើង SSL",
        "opt1": "ដែនរងឥតគិតថ្លៃ rtsurvey.com *(ណែនាំ)*",
        "opt2": "ដែនផ្ទាល់ខ្លួនរបស់ខ្ញុំ",
        "opt3": "ដំឡើងវិញ្ញាបនបត្រដោយដៃ",
        "next": "ជំហានបន្ទាប់",
        "next_text": "នៅពេល SSL ដំណើរការ បន្តទៅ [ការចូលលើកដំបូង](first-login)។",
    },
    "ko": {
        "intro": "SSL은 로그인하기 전에 구성해야 합니다. 앱을 처음 열면 SSL 설정 화면으로 자동 리다이렉션됩니다.",
        "opt_title": "SSL 설정 옵션",
        "opt1": "무료 rtsurvey.com 서브도메인 *(권장)*",
        "opt2": "내 도메인",
        "opt3": "인증서 수동 설치",
        "next": "다음 단계",
        "next_text": "SSL이 활성화되면 [첫 번째 로그인](first-login)으로 이동하세요.",
    },
    "lt": {
        "intro": "SSL turi būti sukonfigūruotas prieš prisijungiant. Kai pirmą kartą atidarote programą, būsite automatiškai nukreipti į SSL nustatymo ekraną.",
        "opt_title": "SSL nustatymo parinktys",
        "opt1": "Nemokamas rtsurvey.com subdomeinas *(Rekomenduojama)*",
        "opt2": "Mano domenas",
        "opt3": "Rankinis sertifikato diegimas",
        "next": "Kitas žingsnis",
        "next_text": "Kai SSL aktyvus, eikite į [Pirmąjį prisijungimą](first-login).",
    },
    "lv": {
        "intro": "SSL ir jākonfigurē pirms pieteikšanās. Atverot lietotni pirmo reizi, jūs automātiski tiksiet novirzīts uz SSL iestatīšanas ekrānu.",
        "opt_title": "SSL iestatīšanas opcijas",
        "opt1": "Bezmaksas rtsurvey.com apakšdomēns *(Ieteicams)*",
        "opt2": "Mans domēns",
        "opt3": "Instalēt sertifikātu manuāli",
        "next": "Nākamais solis",
        "next_text": "Kad SSL ir aktīvs, turpiniet ar [Pirmo pieteikšanos](first-login).",
    },
    "nb": {
        "intro": "SSL må konfigureres før du kan logge inn. Når du åpner appen for første gang, vil du automatisk bli omdirigert til SSL-oppsettsskjermen.",
        "opt_title": "SSL-oppsettsmuligheter",
        "opt1": "Gratis rtsurvey.com-underdomene *(Anbefalt)*",
        "opt2": "Mitt eget domene",
        "opt3": "Installer sertifikat manuelt",
        "next": "Neste steg",
        "next_text": "Når SSL er aktivt, gå til [Første innlogging](first-login).",
    },
    "nl": {
        "intro": "SSL moet worden geconfigureerd voordat u kunt inloggen. Wanneer u de app voor het eerst opent, wordt u automatisch doorgestuurd naar het SSL-instellingsscherm.",
        "opt_title": "SSL-instellingsopties",
        "opt1": "Gratis rtsurvey.com-subdomein *(Aanbevolen)*",
        "opt2": "Mijn eigen domein",
        "opt3": "Certificaat handmatig installeren",
        "next": "Volgende stap",
        "next_text": "Zodra SSL actief is, ga naar [Eerste aanmelding](first-login).",
    },
    "pl": {
        "intro": "SSL musi być skonfigurowany, zanim będziesz mógł się zalogować. Gdy otworzysz aplikację po raz pierwszy, zostaniesz automatycznie przekierowany do ekranu konfiguracji SSL.",
        "opt_title": "Opcje konfiguracji SSL",
        "opt1": "Darmowa subdomena rtsurvey.com *(Zalecane)*",
        "opt2": "Moja własna domena",
        "opt3": "Zainstaluj certyfikat ręcznie",
        "next": "Następny krok",
        "next_text": "Gdy SSL jest aktywny, przejdź do [Pierwszego logowania](first-login).",
    },
    "pt": {
        "intro": "O SSL tem de ser configurado antes de poder iniciar sessão. Quando abre a aplicação pela primeira vez, será automaticamente redirecionado para o ecrã de configuração SSL.",
        "opt_title": "Opções de configuração SSL",
        "opt1": "Subdomínio rtsurvey.com gratuito *(Recomendado)*",
        "opt2": "O meu próprio domínio",
        "opt3": "Instalar certificado manualmente",
        "next": "Próximo passo",
        "next_text": "Depois de o SSL estar ativo, avance para o [Primeiro início de sessão](first-login).",
    },
    "pt-br": {
        "intro": "O SSL deve ser configurado antes de fazer login. Ao abrir o aplicativo pela primeira vez, você será redirecionado automaticamente para a tela de configuração SSL.",
        "opt_title": "Opções de configuração SSL",
        "opt1": "Subdomínio rtsurvey.com gratuito *(Recomendado)*",
        "opt2": "Meu próprio domínio",
        "opt3": "Instalar certificado manualmente",
        "next": "Próximo passo",
        "next_text": "Assim que o SSL estiver ativo, vá para o [Primeiro login](first-login).",
    },
    "ru": {
        "intro": "SSL необходимо настроить перед входом в систему. При первом открытии приложения вы будете автоматически перенаправлены на экран настройки SSL.",
        "opt_title": "Варианты настройки SSL",
        "opt1": "Бесплатный поддомен rtsurvey.com *(Рекомендуется)*",
        "opt2": "Мой собственный домен",
        "opt3": "Установить сертификат вручную",
        "next": "Следующий шаг",
        "next_text": "После активации SSL перейдите к [Первому входу](first-login).",
    },
    "sk": {
        "intro": "SSL musí byť nakonfigurovaný pred prihlásením. Keď otvoríte aplikáciu po prvýkrát, budete automaticky presmerovaní na obrazovku nastavenia SSL.",
        "opt_title": "Možnosti nastavenia SSL",
        "opt1": "Bezplatná subdoména rtsurvey.com *(Odporúčané)*",
        "opt2": "Moja vlastná doména",
        "opt3": "Ručná inštalácia certifikátu",
        "next": "Ďalší krok",
        "next_text": "Keď je SSL aktívny, pokračujte na [Prvé prihlásenie](first-login).",
    },
    "sq": {
        "intro": "SSL duhet konfiguruar para se të mund të hyni. Kur hapni aplikacionin për herë të parë, do të ridrejtoheni automatikisht te ekrani i konfigurimit SSL.",
        "opt_title": "Opsionet e konfigurimit SSL",
        "opt1": "Nëndomaini falas rtsurvey.com *(Rekomandohet)*",
        "opt2": "Domeni im",
        "opt3": "Instaloni certifikatën manualisht",
        "next": "Hapi tjetër",
        "next_text": "Pasi SSL të jetë aktiv, vazhdoni te [Hyrja e parë](first-login).",
    },
    "sr": {
        "intro": "SSL мора бити конфигурисан пре него што се можете пријавити. Када отворите апликацију по први пут, аутоматски ћете бити преусмерени на екран за подешавање SSL.",
        "opt_title": "Опције подешавања SSL",
        "opt1": "Бесплатни поддомен rtsurvey.com *(Препоручено)*",
        "opt2": "Мој сопствени домен",
        "opt3": "Ручна инсталација сертификата",
        "next": "Следећи корак",
        "next_text": "Када је SSL активан, пређите на [Прво пријављивање](first-login).",
    },
    "sv": {
        "intro": "SSL måste konfigureras innan du kan logga in. När du öppnar appen för första gången omdirigeras du automatiskt till SSL-konfigurationsskärmen.",
        "opt_title": "SSL-konfigurationsalternativ",
        "opt1": "Gratis rtsurvey.com-underdomän *(Rekommenderas)*",
        "opt2": "Min egen domän",
        "opt3": "Installera certifikat manuellt",
        "next": "Nästa steg",
        "next_text": "När SSL är aktivt, gå till [Första inloggning](first-login).",
    },
    "te": {
        "intro": "SSL లాగిన్ అవ్వడానికి ముందు కాన్ఫిగర్ చేయబడాలి. మీరు మొదటిసారి యాప్ తెరిచినప్పుడు, మీరు స్వయంచాలకంగా SSL సెటప్ స్క్రీన్‌కు మళ్ళించబడతారు.",
        "opt_title": "SSL సెటప్ ఆప్షన్లు",
        "opt1": "ఉచిత rtsurvey.com సబ్‌డొమైన్ *(సిఫార్సు చేయబడింది)*",
        "opt2": "నా స్వంత డొమైన్",
        "opt3": "సర్టిఫికేట్ మాన్యువల్‌గా ఇన్‌స్టాల్ చేయండి",
        "next": "తదుపరి దశ",
        "next_text": "SSL యాక్టివ్ అయిన తర్వాత, [మొదటి లాగిన్](first-login) కి వెళ్ళండి.",
    },
    "th": {
        "intro": "ต้องกำหนดค่า SSL ก่อนที่จะสามารถเข้าสู่ระบบได้ เมื่อคุณเปิดแอปเป็นครั้งแรก คุณจะถูกเปลี่ยนเส้นทางโดยอัตโนมัติไปยังหน้าจอตั้งค่า SSL",
        "opt_title": "ตัวเลือกการตั้งค่า SSL",
        "opt1": "ซับโดเมน rtsurvey.com ฟรี *(แนะนำ)*",
        "opt2": "โดเมนของฉัน",
        "opt3": "ติดตั้งใบรับรองด้วยตนเอง",
        "next": "ขั้นตอนถัดไป",
        "next_text": "เมื่อ SSL ใช้งานได้แล้ว ดำเนินการต่อที่ [การเข้าสู่ระบบครั้งแรก](first-login)",
    },
    "tr": {
        "intro": "SSL, giriş yapmadan önce yapılandırılmalıdır. Uygulamayı ilk kez açtığınızda, otomatik olarak SSL kurulum ekranına yönlendirilirsiniz.",
        "opt_title": "SSL kurulum seçenekleri",
        "opt1": "Ücretsiz rtsurvey.com alt etki alanı *(Önerilen)*",
        "opt2": "Kendi etki alanım",
        "opt3": "Sertifikayı manuel olarak yükle",
        "next": "Sonraki adım",
        "next_text": "SSL etkin olduktan sonra [İlk Giriş](first-login) sayfasına geçin.",
    },
    "uk": {
        "intro": "SSL необхідно налаштувати перед входом. Коли ви відкриваєте застосунок вперше, вас автоматично перенаправить на екран налаштування SSL.",
        "opt_title": "Варіанти налаштування SSL",
        "opt1": "Безкоштовний піддомен rtsurvey.com *(Рекомендується)*",
        "opt2": "Мій власний домен",
        "opt3": "Встановити сертифікат вручну",
        "next": "Наступний крок",
        "next_text": "Після активації SSL перейдіть до [Першого входу](first-login).",
    },
    "vi": {
        "intro": "SSL phải được cấu hình trước khi bạn có thể đăng nhập. Khi mở ứng dụng lần đầu tiên, bạn sẽ được tự động chuyển hướng đến màn hình cài đặt SSL.",
        "opt_title": "Tùy chọn cài đặt SSL",
        "opt1": "Tên miền phụ rtsurvey.com miễn phí *(Khuyến nghị)*",
        "opt2": "Tên miền của tôi",
        "opt3": "Cài đặt chứng chỉ thủ công",
        "next": "Bước tiếp theo",
        "next_text": "Sau khi SSL hoạt động, tiến hành [Đăng nhập lần đầu](first-login).",
    },
    "zh-hans": {
        "intro": "SSL 必须在登录前配置。首次打开应用程序时，您将自动重定向到 SSL 设置页面。",
        "opt_title": "SSL 设置选项",
        "opt1": "免费 rtsurvey.com 子域名 *(推荐)*",
        "opt2": "我自己的域名",
        "opt3": "手动安装证书",
        "next": "下一步",
        "next_text": "SSL 激活后，继续进行[首次登录](first-login)。",
    },
    "zh-hant": {
        "intro": "SSL 必須在登入前設定。首次開啟應用程式時，您將自動重新導向至 SSL 設定畫面。",
        "opt_title": "SSL 設定選項",
        "opt1": "免費 rtsurvey.com 子網域 *(建議)*",
        "opt2": "我自己的網域",
        "opt3": "手動安裝憑證",
        "next": "下一步",
        "next_text": "SSL 啟用後，繼續進行[首次登入](first-login)。",
    },
}


def make_template_body(t):
    return f"""{t['intro']}

---

## {t['opt_title']}

![{t['opt_title']}](/img/ssl-setup/ssl-setup-options.png)

| Option | When to use |
|--------|-------------|
| **{t['opt1']}** | No DNS setup needed. We create the record for you. Ready in 2–5 minutes. |
| **{t['opt2']}** | You already have a domain and its DNS points to this server. |
| **{t['opt3']}** | Enterprise or custom CA. Requires SSH access. |

---

## Option 1 — {t['opt1']}

This is the fastest option. No domain registration or DNS changes required.

1. Click **{t['opt1']}** to expand the section
2. Type your desired subdomain name in the input field

   > Use lowercase letters, numbers, and hyphens. 3–30 characters.
   > Example: `myproject` → `myproject.rtsurvey.com`

3. Click **Create https://[subdomain].rtsurvey.com**

<!-- SCREENSHOT NEEDED: subdomain input filled in, before clicking Create -->

4. Wait 2–5 minutes while the certificate is issued

<!-- SCREENSHOT NEEDED: certificate being issued / progress state -->

5. Once the certificate is ready, you will be redirected to your new HTTPS URL automatically

<!-- SCREENSHOT NEEDED: success state / redirect to login -->

---

## Option 2 — {t['opt2']}

Use this if you have an existing domain and its DNS `A` record already points to this server's IP.

1. Click **{t['opt2']}** to expand the section
2. Enter your full domain name (e.g. `survey.myorganization.org`)
3. Click **Create certificate**

<!-- SCREENSHOT NEEDED: own domain input form -->

Let's Encrypt will verify your domain and issue a certificate. This requires DNS to be correctly pointed first — the request will fail otherwise.

---

## Option 3 — {t['opt3']}

For enterprise environments using a custom or internal CA. You will place your certificate files on the server via SSH, then enter your domain in the app.

### Prerequisites

- SSH access to the server
- A valid certificate and private key for your domain (PEM format)

### Step 1 — SSH into the server

```bash
ssh root@<server-ip>
```

### Step 2 — Place your certificate files

Create the directory and copy your files:

```bash
mkdir -p /etc/letsencrypt/live/<your-domain>
```

Copy your files into that directory with these exact names:

| File | Description |
|------|-------------|
| `fullchain.pem` | Your certificate + any intermediate CA certificates (concatenated) |
| `privkey.pem` | Your private key |

Example:

```bash
# Copy from your local machine (run this locally, not on the server)
scp fullchain.pem root@<server-ip>:/etc/letsencrypt/live/<your-domain>/fullchain.pem
scp privkey.pem  root@<server-ip>:/etc/letsencrypt/live/<your-domain>/privkey.pem
```

Set correct permissions:

```bash
chmod 644 /etc/letsencrypt/live/<your-domain>/fullchain.pem
chmod 600 /etc/letsencrypt/live/<your-domain>/privkey.pem
```

### Step 3 — Enter your domain in the app

<!-- SCREENSHOT NEEDED: manual certificate form -->

1. In the SSL setup screen, click **{t['opt3']}**
2. Enter your domain name (must match the certificate's Common Name or SAN)
3. Click **Apply**

The server will configure Nginx with your certificate and reload automatically.

---

## {t['next']}

{t['next_text']}
"""


def get_body(lang):
    if lang in BODIES:
        return BODIES[lang]
    if lang in TEMPLATE_LANGS:
        return make_template_body(TEMPLATE_LANGS[lang])
    return None


def build_file(lang):
    title = TITLES[lang]
    desc = DESCRIPTIONS[lang]
    body = get_body(lang)
    if body is None:
        print(f"WARNING: no body for {lang}")
        return None
    lines = ["---"]
    lines.append(f'weight: {META["weight"]}')
    lines.append(f'title: "{title}"')
    lines.append(f'date: "{META["date"]}"')
    lines.append(f'lastmod: "{META["lastmod"]}"')
    lines.append(f'draft: {META["draft"]}')
    lines.append(f'author: "{META["author"]}"')
    lines.append(f'icon: "{META["icon"]}"')
    lines.append(f'toc: {META["toc"]}')
    lines.append(f'description: "{desc}"')
    lines.append("---")
    lines.append("")
    lines.append(body.rstrip())
    lines.append("")
    return "\n".join(lines)


count = 0
for lang in LANGUAGES:
    content = build_file(lang)
    if content:
        full_path = os.path.join(BASE, lang, REL)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)
        count += 1

print(f"Written {count} ssl-setup files.")
