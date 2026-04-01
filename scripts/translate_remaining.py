#!/usr/bin/env python3
"""
Translate remaining 10 self-hosting pages into 35 languages.
All translations are hardcoded — no external API calls.
Run: python3 scripts/translate_remaining.py
"""

import os

BASE = "/Volumes/ExDisk/rtLab/webapp/doc.rtsurvey.com/content"

LANGUAGES = [
    "ar","bg","cs","da","de","el","es","fi","fr","hi",
    "hu","id","it","ja","km","ko","lt","lv","nb","nl",
    "pl","pt","pt-br","ru","sk","sq","sr","sv","te","th",
    "tr","uk","vi","zh-hans","zh-hant"
]

# ──────────────────────────────────────────────────────────────
# FILE DEFINITIONS
# Each entry: (relative_path, front_matter_per_lang, body_per_lang)
# front_matter_per_lang: dict[lang] -> {title, description}
# body_per_lang: dict[lang] -> str  (markdown body, no front matter)
# ──────────────────────────────────────────────────────────────

FILES = {}

# ═══════════════════════════════════════════════════════════════
# 1. first-login.md
# ═══════════════════════════════════════════════════════════════

FILES["docs/getting-started/self-hosting/first-login.md"] = {
    "meta": {
        "weight": 5,
        "date": "2026-04-01T00:00:00+07:00",
        "lastmod": "2026-04-01T00:00:00+07:00",
        "draft": "false",
        "author": "rtSurvey",
        "icon": "login",
        "toc": "true",
    },
    "titles": {
        "ar": "تسجيل الدخول الأول",
        "bg": "Първо влизане",
        "cs": "První přihlášení",
        "da": "Første login",
        "de": "Erste Anmeldung",
        "el": "Πρώτη Σύνδεση",
        "es": "Primer inicio de sesión",
        "fi": "Ensimmäinen kirjautuminen",
        "fr": "Première connexion",
        "hi": "पहली बार लॉगिन",
        "hu": "Első bejelentkezés",
        "id": "Login Pertama",
        "it": "Primo accesso",
        "ja": "初回ログイン",
        "km": "ការចូលលើកដំបូង",
        "ko": "첫 번째 로그인",
        "lt": "Pirmasis prisijungimas",
        "lv": "Pirmā pieteikšanās",
        "nb": "Første innlogging",
        "nl": "Eerste aanmelding",
        "pl": "Pierwsze logowanie",
        "pt": "Primeiro início de sessão",
        "pt-br": "Primeiro login",
        "ru": "Первый вход",
        "sk": "Prvé prihlásenie",
        "sq": "Hyrja e parë",
        "sr": "Прво пријављивање",
        "sv": "Första inloggning",
        "te": "మొదటి లాగిన్",
        "th": "การเข้าสู่ระบบครั้งแรก",
        "tr": "İlk Giriş",
        "uk": "Перший вхід",
        "vi": "Đăng nhập lần đầu",
        "zh-hans": "首次登录",
        "zh-hant": "首次登入",
    },
    "descriptions": {
        "ar": "كيفية تسجيل الدخول إلى نسخة rtSurvey الخاصة بك لأول مرة بعد النشر.",
        "bg": "Как да влезете в своя rtSurvey за първи път след разгръщането.",
        "cs": "Jak se přihlásit do vaší instance rtSurvey poprvé po nasazení.",
        "da": "Sådan logger du ind på din rtSurvey-instans for første gang efter installation.",
        "de": "So melden Sie sich nach der Bereitstellung zum ersten Mal bei Ihrer rtSurvey-Instanz an.",
        "el": "Πώς να συνδεθείτε στην εγκατάσταση rtSurvey για πρώτη φορά μετά την ανάπτυξη.",
        "es": "Cómo iniciar sesión en su instancia de rtSurvey por primera vez después de la implementación.",
        "fi": "Kuinka kirjautua rtSurvey-instanssiisi ensimmäistä kertaa käyttöönoton jälkeen.",
        "fr": "Comment se connecter à votre instance rtSurvey pour la première fois après le déploiement.",
        "hi": "तैनाती के बाद पहली बार अपने rtSurvey इंस्टेंस में लॉगिन करने का तरीका।",
        "hu": "Hogyan jelentkezzen be az rtSurvey példányába az üzembe helyezés utáni első alkalommal.",
        "id": "Cara masuk ke instance rtSurvey Anda untuk pertama kali setelah deployment.",
        "it": "Come accedere alla propria istanza rtSurvey per la prima volta dopo la distribuzione.",
        "ja": "デプロイ後、初めてrtSurveyインスタンスにログインする方法。",
        "km": "របៀបចូលទៅក្នុង rtSurvey instance របស់អ្នកជាលើកដំបូងបន្ទាប់ពីការដំឡើង។",
        "ko": "배포 후 처음으로 rtSurvey 인스턴스에 로그인하는 방법.",
        "lt": "Kaip prisijungti prie savo rtSurvey egzemplioriaus pirmą kartą po diegimo.",
        "lv": "Kā pirmo reizi pieteikties savā rtSurvey instancē pēc izvietošanas.",
        "nb": "Slik logger du inn på rtSurvey-instansen din for første gang etter distribusjon.",
        "nl": "Hoe u voor het eerst inlogt op uw rtSurvey-instantie na de implementatie.",
        "pl": "Jak zalogować się do swojej instancji rtSurvey po raz pierwszy po wdrożeniu.",
        "pt": "Como iniciar sessão na sua instância rtSurvey pela primeira vez após a implementação.",
        "pt-br": "Como fazer login na sua instância do rtSurvey pela primeira vez após a implantação.",
        "ru": "Как войти в экземпляр rtSurvey в первый раз после развёртывания.",
        "sk": "Ako sa prihlásiť do vašej inštancie rtSurvey po prvýkrát po nasadení.",
        "sq": "Si të identifikoheni në instancën tuaj rtSurvey për herë të parë pas vendosjes.",
        "sr": "Kako да се пријавите у свој rtSurvey инстанцу по prvi put после распоређивања.",
        "sv": "Hur du loggar in på din rtSurvey-instans för första gången efter driftsättning.",
        "te": "విన్యాసం తర్వాత మొదటిసారి మీ rtSurvey ఇన్‌స్టాన్స్‌లో లాగిన్ అవ్వడం ఎలా.",
        "th": "วิธีเข้าสู่ระบบ rtSurvey instance ของคุณเป็นครั้งแรกหลังการติดตั้ง",
        "tr": "Dağıtımdan sonra rtSurvey örneğinize ilk kez nasıl giriş yapılır.",
        "uk": "Як увійти до вашого екземпляра rtSurvey вперше після розгортання.",
        "vi": "Cách đăng nhập vào phiên bản rtSurvey của bạn lần đầu tiên sau khi triển khai.",
        "zh-hans": "如何在部署后首次登录您的 rtSurvey 实例。",
        "zh-hant": "如何在部署後首次登入您的 rtSurvey 執行個體。",
    },
    "bodies": {
        "ar": """> **يجب تكوين SSL قبل تسجيل الدخول.** إذا وصلت إلى التطبيق عبر HTTP، ستظهر لك تحذيرات أمنية وسيتم حظر SSO. أكمل [إعداد SSL](ssl-setup) أولاً.

بعد تفعيل SSL، افتح المتصفح على عنوان HTTPS الخاص بك:

```
https://your-domain.com
```

---

## شاشة تسجيل الدخول

<!-- SCREENSHOT NEEDED: login page over HTTPS — username/password form + SSO button -->

تعرض صفحة تسجيل الدخول:

- حقلي **اسم المستخدم** و**كلمة المرور**
- زر **تسجيل الدخول**
- زر **تسجيل الدخول بـ SSO** (أسفل فاصل) — لأعضاء الفريق الذين لديهم حسابات SSO

---

## بيانات اعتماد المسؤول الافتراضية

أدخل بيانات الاعتماد الافتراضية وانقر على **تسجيل الدخول**:

| الحقل | القيمة |
|-------|-------|
| اسم المستخدم | `admin` |
| كلمة المرور | `admin` |

> **غيّر كلمة مرورك فور تسجيل الدخول للمرة الأولى.**

---

## إذا ظهر تحذير أمني

إذا وصلت إلى التطبيق عبر HTTP (قبل تكوين SSL)، ستشاهد:

- شريط تحذير أصفر في أعلى صفحة تسجيل الدخول
- نافذة منبثقة عند النقر على **تسجيل الدخول** تحذر من إرسال بيانات الاعتماد غير مشفرة

<!-- SCREENSHOT NEEDED: HTTP warning banner on login page -->
<!-- SCREENSHOT NEEDED: SSL warning modal with "Set up SSL" and "Continue anyway" buttons -->

انقر على **إعداد SSL** لتكوين HTTPS، أو **المتابعة على أي حال** لتسجيل الدخول بدون SSL (غير موصى به).

تسجيل الدخول بـ SSO محظور تماماً عبر HTTP — النقر على **تسجيل الدخول بـ SSO** سيعرض إشعاراً بدلاً من إعادة التوجيه.

---

## بعد تسجيل الدخول

بمجرد الدخول، ستنتقل إلى لوحة التحكم. من هنا:

1. **غيّر كلمة مرور المسؤول** — إعدادات الحساب ← تغيير كلمة المرور
2. **أنشئ مشروعك الأول** — المشاريع ← مشروع جديد
3. **رفع نموذج أو بناؤه** — النماذج ← رفع XLSForm أو فتح منشئ النماذج
4. **إضافة مستخدمين** — المستخدمون ← دعوة أو إنشاء حسابات لفريقك
""",
        "bg": """> **SSL трябва да е конфигуриран преди влизане.** Ако достъпвате приложението по HTTP, ще видите предупреждение за сигурност и SSO ще бъде блокиран. Завършете [Настройка на SSL](ssl-setup) първо.

След като SSL е активен, отворете браузъра на вашия HTTPS адрес:

```
https://your-domain.com
```

---

## Екранът за влизане

<!-- SCREENSHOT NEEDED: login page over HTTPS — username/password form + SSO button -->

Страницата за влизане показва:

- Полета за **потребителско име** и **парола**
- Бутон **Влизане**
- Бутон **Влизане чрез SSO** (под разделител) — за членове на екипа с SSO акаунти

---

## Идентификационни данни на администратора по подразбиране

Въведете идентификационните данни по подразбиране и натиснете **Влизане**:

| Поле | Стойност |
|------|---------|
| Потребителско име | `admin` |
| Парола | `admin` |

> **Сменете паролата си веднага след първото влизане.**

---

## Ако видите предупреждение за сигурност

Ако достъпвате приложението по HTTP (преди конфигуриране на SSL), ще видите:

- Жълт банер за предупреждение в горната част на страницата за влизане
- Модален прозорец при натискане на **Влизане**, предупреждаващ, че идентификационните данни ще бъдат изпратени некриптирани

<!-- SCREENSHOT NEEDED: HTTP warning banner on login page -->
<!-- SCREENSHOT NEEDED: SSL warning modal with "Set up SSL" and "Continue anyway" buttons -->

Натиснете **Настройка на SSL**, за да конфигурирате HTTPS, или **Продължи така**, за да влезете без SSL (не се препоръчва).

Влизането чрез SSO е напълно блокирано по HTTP — натискането на **Влизане чрез SSO** ще покаже известие вместо пренасочване.

---

## След влизане

Веднъж вътре, ще попаднете на таблото. Оттам:

1. **Сменете паролата на администратора** — настройки на акаунта → смяна на парола
2. **Създайте първия си проект** — Проекти → Нов проект
3. **Качете или създайте формуляр** — Формуляри → Качване на XLSForm или отваряне на Form Builder
4. **Добавете потребители** — Потребители → Покана или създаване на акаунти за вашия екип
""",
        "cs": """> **Před přihlášením musí být nakonfigurován SSL.** Pokud přistupujete k aplikaci přes HTTP, zobrazí se bezpečnostní upozornění a SSO bude zablokováno. Nejprve dokončete [Nastavení SSL](ssl-setup).

Po aktivaci SSL otevřete prohlížeč na své HTTPS adrese:

```
https://your-domain.com
```

---

## Přihlašovací obrazovka

<!-- SCREENSHOT NEEDED: login page over HTTPS — username/password form + SSO button -->

Přihlašovací stránka zobrazuje:

- Pole **Uživatelské jméno** a **Heslo**
- Tlačítko **Přihlásit se**
- Tlačítko **Přihlásit se přes SSO** (pod oddělovačem) — pro členy týmu s SSO účty

---

## Výchozí přihlašovací údaje správce

Zadejte výchozí přihlašovací údaje a klikněte na **Přihlásit se**:

| Pole | Hodnota |
|------|---------|
| Uživatelské jméno | `admin` |
| Heslo | `admin` |

> **Změňte heslo ihned po prvním přihlášení.**

---

## Pokud se zobrazí bezpečnostní upozornění

Pokud přistupujete k aplikaci přes HTTP (před konfigurací SSL), zobrazí se:

- Žlutý varovný banner v horní části přihlašovací stránky
- Modální okno při kliknutí na **Přihlásit se**, upozorňující, že přihlašovací údaje budou odeslány nešifrovaně

<!-- SCREENSHOT NEEDED: HTTP warning banner on login page -->
<!-- SCREENSHOT NEEDED: SSL warning modal with "Set up SSL" and "Continue anyway" buttons -->

Klikněte na **Nastavit SSL** pro konfiguraci HTTPS, nebo **Přesto pokračovat** pro přihlášení bez SSL (nedoporučeno).

Přihlášení přes SSO je přes HTTP zcela blokováno — kliknutí na **Přihlásit se přes SSO** zobrazí oznámení místo přesměrování.

---

## Po přihlášení

Po přihlášení se ocitnete na nástěnce. Odtud:

1. **Změňte heslo správce** — nastavení účtu → změna hesla
2. **Vytvořte svůj první projekt** — Projekty → Nový projekt
3. **Nahrajte nebo vytvořte formulář** — Formuláře → Nahrát XLSForm nebo otevřít Form Builder
4. **Přidejte uživatele** — Uživatelé → Pozvat nebo vytvořit účty pro váš tým
""",
        "da": """> **SSL skal konfigureres, før du logger ind.** Hvis du tilgår appen via HTTP, vil du se en sikkerhedsadvarsel, og SSO vil blive blokeret. Fuldfør [Opsætning af SSL](ssl-setup) først.

Når SSL er aktivt, åbn din browser på din HTTPS-adresse:

```
https://your-domain.com
```

---

## Login-skærmen

<!-- SCREENSHOT NEEDED: login page over HTTPS — username/password form + SSO button -->

Login-siden viser:

- **Brugernavn** og **Adgangskode** felter
- En **Log ind** knap
- En **Log ind med SSO** knap (under en skillelinje) — for teammedlemmer med SSO-konti

---

## Standard administratorlegitimationsoplysninger

Indtast standardlegitimationsoplysningerne og klik på **Log ind**:

| Felt | Værdi |
|------|-------|
| Brugernavn | `admin` |
| Adgangskode | `admin` |

> **Skift din adgangskode straks efter dit første login.**

---

## Hvis du ser en sikkerhedsadvarsel

Hvis du tilgår appen via HTTP (før SSL er konfigureret), vil du se:

- Et gult advarselsbanner øverst på login-siden
- En modal, når du klikker på **Log ind**, der advarer om, at legitimationsoplysninger vil blive sendt ukrypteret

<!-- SCREENSHOT NEEDED: HTTP warning banner on login page -->
<!-- SCREENSHOT NEEDED: SSL warning modal with "Set up SSL" and "Continue anyway" buttons -->

Klik på **Opsæt SSL** for at konfigurere HTTPS, eller **Fortsæt alligevel** for at logge ind uden SSL (anbefales ikke).

SSO-login er fuldstændigt blokeret via HTTP — klik på **Log ind med SSO** vil vise en meddelelse i stedet for at omdirigere.

---

## Efter login

Når du er inde, lander du på dashboardet. Herfra:

1. **Skift administratoradgangskode** — kontoindstillinger → skift adgangskode
2. **Opret dit første projekt** — Projekter → Nyt projekt
3. **Upload eller byg en formular** — Formularer → Upload XLSForm eller åbn Form Builder
4. **Tilføj brugere** — Brugere → Inviter eller opret konti til dit team
""",
        "de": """> **SSL muss vor der Anmeldung konfiguriert werden.** Wenn Sie über HTTP auf die App zugreifen, wird eine Sicherheitswarnung angezeigt und SSO wird blockiert. Schließen Sie zuerst [SSL einrichten](ssl-setup) ab.

Nachdem SSL aktiv ist, öffnen Sie Ihren Browser unter Ihrer HTTPS-URL:

```
https://your-domain.com
```

---

## Der Anmeldebildschirm

<!-- SCREENSHOT NEEDED: login page over HTTPS — username/password form + SSO button -->

Die Anmeldeseite zeigt:

- Felder für **Benutzername** und **Passwort**
- Eine **Anmelden**-Schaltfläche
- Eine **Mit SSO anmelden**-Schaltfläche (unter einem Trennstrich) — für Teammitglieder mit SSO-Konten

---

## Standard-Administratorzugangsdaten

Geben Sie die Standardzugangsdaten ein und klicken Sie auf **Anmelden**:

| Feld | Wert |
|------|------|
| Benutzername | `admin` |
| Passwort | `admin` |

> **Ändern Sie Ihr Passwort unmittelbar nach der ersten Anmeldung.**

---

## Wenn eine Sicherheitswarnung angezeigt wird

Wenn Sie über HTTP auf die App zugreifen (bevor SSL konfiguriert ist), sehen Sie:

- Ein gelbes Warnbanner oben auf der Anmeldeseite
- Ein Modal beim Klicken auf **Anmelden**, das warnt, dass Zugangsdaten unverschlüsselt gesendet werden

<!-- SCREENSHOT NEEDED: HTTP warning banner on login page -->
<!-- SCREENSHOT NEEDED: SSL warning modal with "Set up SSL" and "Continue anyway" buttons -->

Klicken Sie auf **SSL einrichten**, um HTTPS zu konfigurieren, oder auf **Trotzdem fortfahren**, um sich ohne SSL anzumelden (nicht empfohlen).

Die SSO-Anmeldung ist über HTTP vollständig blockiert — ein Klick auf **Mit SSO anmelden** zeigt einen Hinweis anstelle einer Weiterleitung.

---

## Nach der Anmeldung

Nach der Anmeldung landen Sie auf dem Dashboard. Von hier aus:

1. **Administratorpasswort ändern** — Kontoeinstellungen → Passwort ändern
2. **Erstes Projekt erstellen** — Projekte → Neues Projekt
3. **Formular hochladen oder erstellen** — Formulare → XLSForm hochladen oder Form Builder öffnen
4. **Benutzer hinzufügen** — Benutzer → Einladen oder Konten für Ihr Team erstellen
""",
        "el": """> **Το SSL πρέπει να διαμορφωθεί πριν από τη σύνδεση.** Εάν αποκτάτε πρόσβαση στην εφαρμογή μέσω HTTP, θα δείτε μια προειδοποίηση ασφαλείας και το SSO θα αποκλειστεί. Ολοκληρώστε πρώτα την [Εγκατάσταση SSL](ssl-setup).

Μετά την ενεργοποίηση του SSL, ανοίξτε τον περιηγητή σας στη διεύθυνση HTTPS:

```
https://your-domain.com
```

---

## Η οθόνη σύνδεσης

<!-- SCREENSHOT NEEDED: login page over HTTPS — username/password form + SSO button -->

Η σελίδα σύνδεσης εμφανίζει:

- Πεδία **Όνομα χρήστη** και **Κωδικός πρόσβασης**
- Κουμπί **Σύνδεση**
- Κουμπί **Σύνδεση με SSO** (κάτω από διαχωριστικό) — για μέλη ομάδας με λογαριασμούς SSO

---

## Προεπιλεγμένα διαπιστευτήρια διαχειριστή

Εισαγάγετε τα προεπιλεγμένα διαπιστευτήρια και κάντε κλικ στο **Σύνδεση**:

| Πεδίο | Τιμή |
|-------|------|
| Όνομα χρήστη | `admin` |
| Κωδικός πρόσβασης | `admin` |

> **Αλλάξτε τον κωδικό πρόσβασής σας αμέσως μετά την πρώτη σύνδεση.**

---

## Εάν εμφανιστεί προειδοποίηση ασφαλείας

Εάν αποκτάτε πρόσβαση στην εφαρμογή μέσω HTTP (πριν από τη διαμόρφωση SSL), θα δείτε:

- Ένα κίτρινο banner προειδοποίησης στην κορυφή της σελίδας σύνδεσης
- Ένα modal κατά το κλικ στο **Σύνδεση**, που προειδοποιεί ότι τα διαπιστευτήρια θα αποσταλούν μη κρυπτογραφημένα

<!-- SCREENSHOT NEEDED: HTTP warning banner on login page -->
<!-- SCREENSHOT NEEDED: SSL warning modal with "Set up SSL" and "Continue anyway" buttons -->

Κάντε κλικ στο **Εγκατάσταση SSL** για να διαμορφώσετε HTTPS ή **Συνέχεια ούτως ή άλλως** για σύνδεση χωρίς SSL (δεν συνιστάται).

Η σύνδεση SSO αποκλείεται εντελώς μέσω HTTP — το κλικ στο **Σύνδεση με SSO** θα εμφανίσει ειδοποίηση αντί για ανακατεύθυνση.

---

## Μετά τη σύνδεση

Μόλις μπείτε, θα βρεθείτε στον πίνακα ελέγχου. Από εκεί:

1. **Αλλαγή κωδικού διαχειριστή** — ρυθμίσεις λογαριασμού → αλλαγή κωδικού
2. **Δημιουργία πρώτου έργου** — Έργα → Νέο έργο
3. **Ανέβασμα ή δημιουργία φόρμας** — Φόρμες → Ανέβασμα XLSForm ή άνοιγμα Form Builder
4. **Προσθήκη χρηστών** — Χρήστες → Πρόσκληση ή δημιουργία λογαριασμών για την ομάδα σας
""",
        "es": """> **El SSL debe configurarse antes de iniciar sesión.** Si accede a la aplicación por HTTP, verá una advertencia de seguridad y el SSO quedará bloqueado. Complete primero [Configurar SSL](ssl-setup).

Una vez que SSL esté activo, abra su navegador en su URL HTTPS:

```
https://your-domain.com
```

---

## La pantalla de inicio de sesión

<!-- SCREENSHOT NEEDED: login page over HTTPS — username/password form + SSO button -->

La página de inicio de sesión muestra:

- Campos de **Usuario** y **Contraseña**
- Un botón **Iniciar sesión**
- Un botón **Iniciar sesión con SSO** (debajo de un divisor) — para miembros del equipo con cuentas SSO

---

## Credenciales de administrador predeterminadas

Ingrese las credenciales predeterminadas y haga clic en **Iniciar sesión**:

| Campo | Valor |
|-------|-------|
| Usuario | `admin` |
| Contraseña | `admin` |

> **Cambie su contraseña inmediatamente después de su primer inicio de sesión.**

---

## Si ve una advertencia de seguridad

Si accede a la aplicación por HTTP (antes de configurar SSL), verá:

- Un banner de advertencia amarillo en la parte superior de la página de inicio de sesión
- Un modal al hacer clic en **Iniciar sesión**, advirtiendo que las credenciales se enviarán sin cifrar

<!-- SCREENSHOT NEEDED: HTTP warning banner on login page -->
<!-- SCREENSHOT NEEDED: SSL warning modal with "Set up SSL" and "Continue anyway" buttons -->

Haga clic en **Configurar SSL** para configurar HTTPS, o en **Continuar de todos modos** para iniciar sesión sin SSL (no recomendado).

El inicio de sesión SSO está completamente bloqueado a través de HTTP — hacer clic en **Iniciar sesión con SSO** mostrará un aviso en lugar de redirigir.

---

## Después de iniciar sesión

Una vez dentro, llegará al panel de control. Desde aquí:

1. **Cambiar la contraseña de administrador** — configuración de cuenta → cambiar contraseña
2. **Crear su primer proyecto** — Proyectos → Nuevo proyecto
3. **Subir o construir un formulario** — Formularios → Subir XLSForm o abrir Form Builder
4. **Agregar usuarios** — Usuarios → Invitar o crear cuentas para su equipo
""",
        "fi": """> **SSL täytyy määrittää ennen kirjautumista.** Jos käytät sovellusta HTTP:n kautta, näet tietoturvawarauksen ja SSO estetään. Suorita ensin [SSL:n asennus](ssl-setup).

Kun SSL on aktiivinen, avaa selain HTTPS-osoitteessasi:

```
https://your-domain.com
```

---

## Kirjautumissivu

<!-- SCREENSHOT NEEDED: login page over HTTPS — username/password form + SSO button -->

Kirjautumissivulla näkyy:

- **Käyttäjänimi** ja **Salasana** -kentät
- **Kirjaudu sisään** -painike
- **Kirjaudu SSO:lla** -painike (jakajan alla) — tiimin jäsenille, joilla on SSO-tilit

---

## Oletusarvoinen ylläpitäjän tunniste

Anna oletustunnisteet ja napsauta **Kirjaudu sisään**:

| Kenttä | Arvo |
|--------|------|
| Käyttäjänimi | `admin` |
| Salasana | `admin` |

> **Vaihda salasanasi välittömästi ensimmäisen kirjautumisen jälkeen.**

---

## Jos näet tietoturvawarauksen

Jos käytät sovellusta HTTP:n kautta (ennen SSL:n määrittämistä), näet:

- Keltainen varoitusbanneri kirjautumissivun yläosassa
- Modaali-ikkuna, kun napsautat **Kirjaudu sisään**, varoittaen, että tunnisteet lähetetään salaamattomina

<!-- SCREENSHOT NEEDED: HTTP warning banner on login page -->
<!-- SCREENSHOT NEEDED: SSL warning modal with "Set up SSL" and "Continue anyway" buttons -->

Napsauta **Asenna SSL** määrittääksesi HTTPS tai **Jatka joka tapauksessa** kirjautuaksesi ilman SSL:ää (ei suositella).

SSO-kirjautuminen on täysin estetty HTTP:n kautta — **Kirjaudu SSO:lla** -painikkeen napsauttaminen näyttää ilmoituksen uudelleenohjauksen sijaan.

---

## Kirjautumisen jälkeen

Kirjautumisen jälkeen pääset kojelautaan. Sieltä:

1. **Vaihda ylläpitäjän salasana** — tilin asetukset → vaihda salasana
2. **Luo ensimmäinen projektisi** — Projektit → Uusi projekti
3. **Lataa tai luo lomake** — Lomakkeet → Lataa XLSForm tai avaa Form Builder
4. **Lisää käyttäjiä** — Käyttäjät → Kutsu tai luo tiimisi jäsenille tilit
""",
        "fr": """> **Le SSL doit être configuré avant de vous connecter.** Si vous accédez à l'application via HTTP, vous verrez un avertissement de sécurité et le SSO sera bloqué. Terminez d'abord la [configuration SSL](ssl-setup).

Une fois SSL actif, ouvrez votre navigateur à votre URL HTTPS :

```
https://your-domain.com
```

---

## L'écran de connexion

<!-- SCREENSHOT NEEDED: login page over HTTPS — username/password form + SSO button -->

La page de connexion affiche :

- Les champs **Nom d'utilisateur** et **Mot de passe**
- Un bouton **Se connecter**
- Un bouton **Se connecter avec SSO** (sous un séparateur) — pour les membres de l'équipe avec des comptes SSO

---

## Identifiants administrateur par défaut

Entrez les identifiants par défaut et cliquez sur **Se connecter** :

| Champ | Valeur |
|-------|--------|
| Nom d'utilisateur | `admin` |
| Mot de passe | `admin` |

> **Changez votre mot de passe immédiatement après votre première connexion.**

---

## Si vous voyez un avertissement de sécurité

Si vous accédez à l'application via HTTP (avant la configuration SSL), vous verrez :

- Une bannière d'avertissement jaune en haut de la page de connexion
- Un modal en cliquant sur **Se connecter**, avertissant que les identifiants seront envoyés non chiffrés

<!-- SCREENSHOT NEEDED: HTTP warning banner on login page -->
<!-- SCREENSHOT NEEDED: SSL warning modal with "Set up SSL" and "Continue anyway" buttons -->

Cliquez sur **Configurer SSL** pour configurer HTTPS, ou sur **Continuer quand même** pour vous connecter sans SSL (non recommandé).

La connexion SSO est entièrement bloquée via HTTP — cliquer sur **Se connecter avec SSO** affichera un avis au lieu de rediriger.

---

## Après la connexion

Une fois connecté, vous arriverez sur le tableau de bord. De là :

1. **Changer le mot de passe administrateur** — paramètres du compte → changer le mot de passe
2. **Créer votre premier projet** — Projets → Nouveau projet
3. **Télécharger ou créer un formulaire** — Formulaires → Télécharger XLSForm ou ouvrir Form Builder
4. **Ajouter des utilisateurs** — Utilisateurs → Inviter ou créer des comptes pour votre équipe
""",
        "hi": """> **लॉगिन से पहले SSL कॉन्फ़िगर करना आवश्यक है।** यदि आप HTTP के माध्यम से ऐप एक्सेस करते हैं, तो आपको सुरक्षा चेतावनी दिखेगी और SSO ब्लॉक हो जाएगा। पहले [SSL सेटअप](ssl-setup) पूरा करें।

SSL सक्रिय होने के बाद, अपने HTTPS URL पर ब्राउज़र खोलें:

```
https://your-domain.com
```

---

## लॉगिन स्क्रीन

<!-- SCREENSHOT NEEDED: login page over HTTPS — username/password form + SSO button -->

लॉगिन पेज दिखाता है:

- **उपयोगकर्ता नाम** और **पासवर्ड** फ़ील्ड
- एक **साइन इन** बटन
- एक **SSO से लॉगिन** बटन (विभाजक के नीचे) — SSO खातों वाले टीम सदस्यों के लिए

---

## डिफ़ॉल्ट एडमिन क्रेडेंशियल

डिफ़ॉल्ट क्रेडेंशियल दर्ज करें और **साइन इन** पर क्लिक करें:

| फ़ील्ड | मान |
|--------|-----|
| उपयोगकर्ता नाम | `admin` |
| पासवर्ड | `admin` |

> **पहली बार लॉगिन के तुरंत बाद अपना पासवर्ड बदलें।**

---

## यदि सुरक्षा चेतावनी दिखे

यदि आप HTTP के माध्यम से ऐप एक्सेस करते हैं (SSL कॉन्फ़िगर होने से पहले), तो आप देखेंगे:

- लॉगिन पेज के ऊपर एक पीला चेतावनी बैनर
- **साइन इन** पर क्लिक करने पर एक मोडल, जो चेतावनी देता है कि क्रेडेंशियल अनएन्क्रिप्टेड भेजे जाएंगे

<!-- SCREENSHOT NEEDED: HTTP warning banner on login page -->
<!-- SCREENSHOT NEEDED: SSL warning modal with "Set up SSL" and "Continue anyway" buttons -->

HTTPS कॉन्फ़िगर करने के लिए **SSL सेट करें** पर क्लिक करें, या SSL के बिना लॉगिन के लिए **फिर भी जारी रखें** पर क्लिक करें (अनुशंसित नहीं)।

HTTP पर SSO लॉगिन पूरी तरह ब्लॉक है — **SSO से लॉगिन** पर क्लिक करने से रीडायरेक्ट की बजाय एक सूचना दिखाई देगी।

---

## लॉगिन के बाद

अंदर आने पर आप डैशबोर्ड पर पहुंचेंगे। यहाँ से:

1. **एडमिन पासवर्ड बदलें** — खाता सेटिंग → पासवर्ड बदलें
2. **अपना पहला प्रोजेक्ट बनाएं** — प्रोजेक्ट → नया प्रोजेक्ट
3. **फ़ॉर्म अपलोड करें या बनाएं** — फ़ॉर्म → XLSForm अपलोड करें या Form Builder खोलें
4. **उपयोगकर्ता जोड़ें** — उपयोगकर्ता → अपनी टीम के लिए खाते आमंत्रित करें या बनाएं
""",
        "hu": """> **Az SSL-t be kell állítani a bejelentkezés előtt.** Ha HTTP-n keresztül éri el az alkalmazást, biztonsági figyelmeztetést fog látni, és az SSO le lesz tiltva. Először fejezze be az [SSL beállítást](ssl-setup).

Miután az SSL aktív, nyissa meg böngészőjét a HTTPS URL-jén:

```
https://your-domain.com
```

---

## A bejelentkezési képernyő

<!-- SCREENSHOT NEEDED: login page over HTTPS — username/password form + SSO button -->

A bejelentkezési oldal mutatja:

- **Felhasználónév** és **Jelszó** mezők
- Egy **Bejelentkezés** gomb
- Egy **Bejelentkezés SSO-val** gomb (elválasztó alatt) — SSO-fiókkal rendelkező csapattagok számára

---

## Alapértelmezett adminisztrátori hitelesítő adatok

Adja meg az alapértelmezett hitelesítő adatokat, és kattintson a **Bejelentkezés** gombra:

| Mező | Érték |
|------|-------|
| Felhasználónév | `admin` |
| Jelszó | `admin` |

> **Azonnal változtassa meg jelszavát az első bejelentkezés után.**

---

## Ha biztonsági figyelmeztetést lát

Ha HTTP-n keresztül éri el az alkalmazást (az SSL konfigurálása előtt), a következőket fogja látni:

- Sárga figyelmeztető szalag a bejelentkezési oldal tetején
- Egy modális ablak a **Bejelentkezés** kattintásakor, amely figyelmeztet, hogy a hitelesítő adatokat titkosítás nélkül küldi el

<!-- SCREENSHOT NEEDED: HTTP warning banner on login page -->
<!-- SCREENSHOT NEEDED: SSL warning modal with "Set up SSL" and "Continue anyway" buttons -->

Kattintson az **SSL beállítása** gombra a HTTPS konfigurálásához, vagy a **Folytatás mindenképpen** gombra az SSL nélküli bejelentkezéshez (nem ajánlott).

Az SSO-bejelentkezés teljesen le van tiltva HTTP-n keresztül — az **SSO-val bejelentkezés** gombra kattintva értesítés jelenik meg az átirányítás helyett.

---

## Bejelentkezés után

Bejelentkezés után az irányítópulton landol. Innen:

1. **Adminisztrátori jelszó módosítása** — fiókbeállítások → jelszó módosítása
2. **Első projekt létrehozása** — Projektek → Új projekt
3. **Űrlap feltöltése vagy készítése** — Űrlapok → XLSForm feltöltése vagy Form Builder megnyitása
4. **Felhasználók hozzáadása** — Felhasználók → Meghívás vagy fiókok létrehozása csapatának
""",
        "id": """> **SSL harus dikonfigurasi sebelum masuk.** Jika Anda mengakses aplikasi melalui HTTP, Anda akan melihat peringatan keamanan dan SSO akan diblokir. Selesaikan [Pengaturan SSL](ssl-setup) terlebih dahulu.

Setelah SSL aktif, buka browser Anda di URL HTTPS Anda:

```
https://your-domain.com
```

---

## Layar login

<!-- SCREENSHOT NEEDED: login page over HTTPS — username/password form + SSO button -->

Halaman login menampilkan:

- Kolom **Nama Pengguna** dan **Kata Sandi**
- Tombol **Masuk**
- Tombol **Masuk dengan SSO** (di bawah pemisah) — untuk anggota tim dengan akun SSO

---

## Kredensial admin default

Masukkan kredensial default dan klik **Masuk**:

| Kolom | Nilai |
|-------|-------|
| Nama Pengguna | `admin` |
| Kata Sandi | `admin` |

> **Segera ubah kata sandi Anda setelah login pertama.**

---

## Jika Anda melihat peringatan keamanan

Jika Anda mengakses aplikasi melalui HTTP (sebelum SSL dikonfigurasi), Anda akan melihat:

- Spanduk peringatan kuning di bagian atas halaman login
- Modal saat mengklik **Masuk**, memperingatkan bahwa kredensial akan dikirim tidak terenkripsi

<!-- SCREENSHOT NEEDED: HTTP warning banner on login page -->
<!-- SCREENSHOT NEEDED: SSL warning modal with "Set up SSL" and "Continue anyway" buttons -->

Klik **Atur SSL** untuk mengonfigurasi HTTPS, atau **Lanjutkan saja** untuk masuk tanpa SSL (tidak disarankan).

Login SSO sepenuhnya diblokir melalui HTTP — mengklik **Masuk dengan SSO** akan menampilkan pemberitahuan alih-alih mengalihkan.

---

## Setelah login

Setelah masuk, Anda akan berada di dasbor. Dari sini:

1. **Ubah kata sandi admin** — pengaturan akun → ubah kata sandi
2. **Buat proyek pertama Anda** — Proyek → Proyek Baru
3. **Unggah atau buat formulir** — Formulir → Unggah XLSForm atau buka Form Builder
4. **Tambahkan pengguna** — Pengguna → Undang atau buat akun untuk tim Anda
""",
        "it": """> **SSL deve essere configurato prima dell'accesso.** Se si accede all'applicazione tramite HTTP, verrà visualizzato un avviso di sicurezza e SSO sarà bloccato. Completare prima la [Configurazione SSL](ssl-setup).

Una volta che SSL è attivo, aprire il browser all'URL HTTPS:

```
https://your-domain.com
```

---

## La schermata di accesso

<!-- SCREENSHOT NEEDED: login page over HTTPS — username/password form + SSO button -->

La pagina di accesso mostra:

- Campi **Nome utente** e **Password**
- Un pulsante **Accedi**
- Un pulsante **Accedi con SSO** (sotto un divisore) — per i membri del team con account SSO

---

## Credenziali amministratore predefinite

Inserire le credenziali predefinite e fare clic su **Accedi**:

| Campo | Valore |
|-------|--------|
| Nome utente | `admin` |
| Password | `admin` |

> **Cambiare la password immediatamente dopo il primo accesso.**

---

## Se viene visualizzato un avviso di sicurezza

Se si accede all'applicazione tramite HTTP (prima della configurazione SSL), si vedrà:

- Un banner di avviso giallo nella parte superiore della pagina di accesso
- Un modal quando si fa clic su **Accedi**, che avverte che le credenziali verranno inviate non crittografate

<!-- SCREENSHOT NEEDED: HTTP warning banner on login page -->
<!-- SCREENSHOT NEEDED: SSL warning modal with "Set up SSL" and "Continue anyway" buttons -->

Fare clic su **Configura SSL** per configurare HTTPS, o su **Continua comunque** per accedere senza SSL (non consigliato).

Il login SSO è completamente bloccato tramite HTTP — fare clic su **Accedi con SSO** mostrerà un avviso anziché reindirizzare.

---

## Dopo l'accesso

Una volta dentro, si atterrerà sulla dashboard. Da qui:

1. **Cambiare la password amministratore** — impostazioni account → cambia password
2. **Creare il primo progetto** — Progetti → Nuovo progetto
3. **Caricare o creare un modulo** — Moduli → Carica XLSForm o apri Form Builder
4. **Aggiungere utenti** — Utenti → Invita o crea account per il tuo team
""",
        "ja": """> **ログイン前にSSLを設定する必要があります。** HTTPでアプリにアクセスすると、セキュリティ警告が表示され、SSOがブロックされます。まず[SSLのセットアップ](ssl-setup)を完了してください。

SSLが有効になったら、HTTPS URLでブラウザを開いてください：

```
https://your-domain.com
```

---

## ログイン画面

<!-- SCREENSHOT NEEDED: login page over HTTPS — username/password form + SSO button -->

ログインページには以下が表示されます：

- **ユーザー名**と**パスワード**フィールド
- **サインイン**ボタン
- **SSOでログイン**ボタン（区切り線の下）— SSOアカウントを持つチームメンバー向け

---

## デフォルトの管理者認証情報

デフォルトの認証情報を入力し、**サインイン**をクリックしてください：

| フィールド | 値 |
|-----------|-----|
| ユーザー名 | `admin` |
| パスワード | `admin` |

> **初回ログイン後、すぐにパスワードを変更してください。**

---

## セキュリティ警告が表示された場合

HTTPでアプリにアクセスした場合（SSL設定前）、以下が表示されます：

- ログインページ上部の黄色い警告バナー
- **サインイン**をクリックすると、認証情報が暗号化されずに送信されることを警告するモーダル

<!-- SCREENSHOT NEEDED: HTTP warning banner on login page -->
<!-- SCREENSHOT NEEDED: SSL warning modal with "Set up SSL" and "Continue anyway" buttons -->

HTTPSを設定するには**SSLをセットアップ**をクリック、またはSSLなしでログインするには**とにかく続ける**をクリックしてください（推奨しません）。

HTTP経由のSSOログインは完全にブロックされています—**SSOでログイン**をクリックすると、リダイレクトの代わりに通知が表示されます。

---

## ログイン後

ログインするとダッシュボードが表示されます。ここから：

1. **管理者パスワードの変更** — アカウント設定 → パスワード変更
2. **最初のプロジェクトの作成** — プロジェクト → 新規プロジェクト
3. **フォームのアップロードまたは作成** — フォーム → XLSFormのアップロードまたはForm Builderを開く
4. **ユーザーの追加** — ユーザー → チームのアカウントを招待または作成
""",
        "km": """> **SSL ត្រូវតែកំណត់រចនាសម្ព័ន្ធមុនពេលចូល។** ប្រសិនបើអ្នកចូលប្រើកម្មវិធីតាម HTTP អ្នកនឹងឃើញការព្រមានសុវត្ថិភាព ហើយ SSO នឹងត្រូវបិទ។ សូមបំពេញ [ការដំឡើង SSL](ssl-setup) ជាមុនសិន។

បន្ទាប់ពី SSL ដំណើរការ សូមបើកកម្មវិធីរុករករបស់អ្នកនៅ URL HTTPS របស់អ្នក:

```
https://your-domain.com
```

---

## អេក្រង់ចូល

<!-- SCREENSHOT NEEDED: login page over HTTPS — username/password form + SSO button -->

ទំព័រចូលបង្ហាញ:

- វាល **ឈ្មោះអ្នកប្រើ** និង **លេខសម្ងាត់**
- ប៊ូតុង **ចូល**
- ប៊ូតុង **ចូលដោយ SSO** (នៅក្រោមមែក) — សម្រាប់សមាជិកក្រុមដែលមានគណនី SSO

---

## លិខិតបញ្ជាក់អ្នកគ្រប់គ្រងលំនាំដើម

បញ្ចូលលិខិតបញ្ជាក់លំនាំដើម ហើយចុច **ចូល**:

| វាល | តម្លៃ |
|-----|-------|
| ឈ្មោះអ្នកប្រើ | `admin` |
| លេខសម្ងាត់ | `admin` |

> **ផ្លាស់ប្តូរលេខសម្ងាត់របស់អ្នកភ្លាមៗបន្ទាប់ពីការចូលលើកដំបូង។**

---

## ប្រសិនបើអ្នកឃើញការព្រមានសុវត្ថិភាព

ប្រសិនបើអ្នកចូលប្រើកម្មវិធីតាម HTTP (មុនពេលកំណត់រចនាសម្ព័ន្ធ SSL) អ្នកនឹងឃើញ:

- ផ្ទាំងព្រមានពណ៌លឿងនៅផ្នែកខាងលើនៃទំព័រចូល
- បង្អួចលេចឡើងនៅពេលចុច **ចូល** ដែលព្រមានថាព័ត៌មានសម្ងាត់នឹងត្រូវបញ្ជូនដោយមិនបានអ៊ិនគ្រីប

<!-- SCREENSHOT NEEDED: HTTP warning banner on login page -->
<!-- SCREENSHOT NEEDED: SSL warning modal with "Set up SSL" and "Continue anyway" buttons -->

ចុច **ដំឡើង SSL** ដើម្បីកំណត់រចនាសម្ព័ន្ធ HTTPS ឬ **បន្តទោះជាយ៉ាងណា** ដើម្បីចូលដោយគ្មាន SSL (មិនត្រូវបានណែនាំ)។

ការចូល SSO ត្រូវបានបិទទាំងស្រុងតាម HTTP — ការចុច **ចូលដោយ SSO** នឹងបង្ហាញការជូនដំណឹងជំនួសការបញ្ជូន។

---

## បន្ទាប់ពីចូល

នៅពេលចូល អ្នកនឹងបង្ហាញនៅផ្ទាំងគ្រប់គ្រង។ ពីទីនេះ:

1. **ផ្លាស់ប្តូរលេខសម្ងាត់អ្នកគ្រប់គ្រង** — ការកំណត់គណនី → ផ្លាស់ប្តូរលេខសម្ងាត់
2. **បង្កើតគម្រោងដំបូងរបស់អ្នក** — គម្រោង → គម្រោងថ្មី
3. **បង្ហោះឬបង្កើតទម្រង់** — ទម្រង់ → បង្ហោះ XLSForm ឬបើក Form Builder
4. **បន្ថែមអ្នកប្រើ** — អ្នកប្រើ → អញ្ជើញឬបង្កើតគណនីសម្រាប់ក្រុមរបស់អ្នក
""",
        "ko": """> **로그인하기 전에 SSL을 구성해야 합니다.** HTTP로 앱에 접근하면 보안 경고가 표시되고 SSO가 차단됩니다. 먼저 [SSL 설정](ssl-setup)을 완료하세요.

SSL이 활성화된 후 HTTPS URL로 브라우저를 여세요:

```
https://your-domain.com
```

---

## 로그인 화면

<!-- SCREENSHOT NEEDED: login page over HTTPS — username/password form + SSO button -->

로그인 페이지에는 다음이 표시됩니다:

- **사용자 이름** 및 **비밀번호** 필드
- **로그인** 버튼
- **SSO로 로그인** 버튼 (구분선 아래) — SSO 계정이 있는 팀 구성원을 위해

---

## 기본 관리자 자격 증명

기본 자격 증명을 입력하고 **로그인**을 클릭하세요:

| 필드 | 값 |
|------|----|
| 사용자 이름 | `admin` |
| 비밀번호 | `admin` |

> **첫 번째 로그인 후 즉시 비밀번호를 변경하세요.**

---

## 보안 경고가 표시되는 경우

HTTP로 앱에 접근할 경우 (SSL 구성 전) 다음이 표시됩니다:

- 로그인 페이지 상단의 노란색 경고 배너
- **로그인**을 클릭하면 자격 증명이 암호화되지 않고 전송된다는 경고 모달

<!-- SCREENSHOT NEEDED: HTTP warning banner on login page -->
<!-- SCREENSHOT NEEDED: SSL warning modal with "Set up SSL" and "Continue anyway" buttons -->

HTTPS를 구성하려면 **SSL 설정**을 클릭하거나, SSL 없이 로그인하려면 **그래도 계속**을 클릭하세요 (권장하지 않음).

HTTP를 통한 SSO 로그인은 완전히 차단됩니다 — **SSO로 로그인**을 클릭하면 리다이렉션 대신 알림이 표시됩니다.

---

## 로그인 후

로그인하면 대시보드로 이동합니다. 여기서:

1. **관리자 비밀번호 변경** — 계정 설정 → 비밀번호 변경
2. **첫 번째 프로젝트 만들기** — 프로젝트 → 새 프로젝트
3. **양식 업로드 또는 빌드** — 양식 → XLSForm 업로드 또는 Form Builder 열기
4. **사용자 추가** — 사용자 → 팀 계정 초대 또는 생성
""",
        "lt": """> **Prieš prisijungimą turi būti sukonfigūruotas SSL.** Jei pasiekiate programą per HTTP, pamatysite saugos įspėjimą ir SSO bus užblokuotas. Pirmiausia užbaikite [SSL nustatymą](ssl-setup).

Kai SSL aktyvus, atidarykite naršyklę savo HTTPS URL:

```
https://your-domain.com
```

---

## Prisijungimo ekranas

<!-- SCREENSHOT NEEDED: login page over HTTPS — username/password form + SSO button -->

Prisijungimo puslapis rodo:

- **Vartotojo vardas** ir **Slaptažodis** laukai
- **Prisijungti** mygtukas
- **Prisijungti per SSO** mygtukas (žemiau skyriklio) — komandos nariams su SSO paskyromis

---

## Numatytieji administratoriaus duomenys

Įveskite numatytuosius duomenis ir spustelėkite **Prisijungti**:

| Laukas | Reikšmė |
|--------|---------|
| Vartotojo vardas | `admin` |
| Slaptažodis | `admin` |

> **Nedelsdami pakeiskite slaptažodį po pirmojo prisijungimo.**

---

## Jei matote saugos įspėjimą

Jei pasiekiate programą per HTTP (prieš SSL konfigūraciją), pamatysite:

- Geltoną įspėjimo juostą prisijungimo puslapio viršuje
- Modalinį langą paspaudus **Prisijungti**, įspėjantį, kad duomenys bus siunčiami nešifruoti

<!-- SCREENSHOT NEEDED: HTTP warning banner on login page -->
<!-- SCREENSHOT NEEDED: SSL warning modal with "Set up SSL" and "Continue anyway" buttons -->

Spustelėkite **Nustatyti SSL** HTTPS konfigūravimui arba **Tęsti bet kokiu atveju** prisijungimui be SSL (nerekomenduojama).

SSO prisijungimas visiškai užblokuotas per HTTP — paspaudus **Prisijungti per SSO** bus rodomas pranešimas vietoj nukreipimo.

---

## Po prisijungimo

Prisijungę pateksite į prietaisų skydelį. Iš čia:

1. **Keisti administratoriaus slaptažodį** — paskyros nustatymai → keisti slaptažodį
2. **Kurti pirmąjį projektą** — Projektai → Naujas projektas
3. **Įkelti arba kurti formą** — Formos → Įkelti XLSForm arba atidaryti Form Builder
4. **Pridėti vartotojus** — Vartotojai → Pakviesti arba sukurti paskyras jūsų komandai
""",
        "lv": """> **Pirms pieteikšanās jākonfigurē SSL.** Ja piekļūstat lietotnei caur HTTP, tiks parādīts drošības brīdinājums un SSO tiks bloķēts. Vispirms pabeidziet [SSL iestatīšanu](ssl-setup).

Kad SSL ir aktīvs, atveriet pārlūkprogrammu savā HTTPS URL:

```
https://your-domain.com
```

---

## Pieteikšanās ekrāns

<!-- SCREENSHOT NEEDED: login page over HTTPS — username/password form + SSO button -->

Pieteikšanās lapā redzams:

- **Lietotājvārds** un **Parole** lauki
- **Pierakstīties** poga
- **Pierakstīties ar SSO** poga (zem atdalītāja) — komandas locekļiem ar SSO kontiem

---

## Noklusējuma administratora akreditācijas dati

Ievadiet noklusējuma akreditācijas datus un noklikšķiniet uz **Pierakstīties**:

| Lauks | Vērtība |
|-------|---------|
| Lietotājvārds | `admin` |
| Parole | `admin` |

> **Nomainiet paroli uzreiz pēc pirmās pieteikšanās.**

---

## Ja tiek parādīts drošības brīdinājums

Ja piekļūstat lietotnei caur HTTP (pirms SSL konfigurēšanas), redzēsit:

- Dzeltenu brīdinājuma joslu pieteikšanās lapas augšā
- Modālo logu, noklikšķinot uz **Pierakstīties**, brīdinot, ka akreditācijas dati tiks nosūtīti nešifrēti

<!-- SCREENSHOT NEEDED: HTTP warning banner on login page -->
<!-- SCREENSHOT NEEDED: SSL warning modal with "Set up SSL" and "Continue anyway" buttons -->

Noklikšķiniet uz **Iestatīt SSL**, lai konfigurētu HTTPS, vai uz **Turpināt tāpat** pieteikšanās bez SSL (nav ieteicams).

SSO pieteikšanās caur HTTP ir pilnībā bloķēta — noklikšķinot uz **Pierakstīties ar SSO**, tiks parādīts paziņojums, nevis novirzīšana.

---

## Pēc pieteikšanās

Pēc pieteikšanās nokļūsit informācijas panelī. No šejienes:

1. **Mainīt administratora paroli** — konta iestatījumi → mainīt paroli
2. **Izveidot pirmo projektu** — Projekti → Jauns projekts
3. **Augšupielādēt vai izveidot veidlapu** — Veidlapas → Augšupielādēt XLSForm vai atvērt Form Builder
4. **Pievienot lietotājus** — Lietotāji → Uzaicināt vai izveidot kontus jūsu komandai
""",
        "nb": """> **SSL må konfigureres før du logger inn.** Hvis du åpner appen via HTTP, vil du se en sikkerhetsadvarsel og SSO vil bli blokkert. Fullfør [Oppsett av SSL](ssl-setup) først.

Når SSL er aktivt, åpne nettleseren på HTTPS-adressen din:

```
https://your-domain.com
```

---

## Innloggingsskjermen

<!-- SCREENSHOT NEEDED: login page over HTTPS — username/password form + SSO button -->

Innloggingssiden viser:

- Feltene **Brukernavn** og **Passord**
- En **Logg inn** knapp
- En **Logg inn med SSO** knapp (under en skillelinje) — for teammedlemmer med SSO-kontoer

---

## Standard administratorlegitimasjon

Skriv inn standardlegitimasjonen og klikk **Logg inn**:

| Felt | Verdi |
|------|-------|
| Brukernavn | `admin` |
| Passord | `admin` |

> **Endre passordet ditt umiddelbart etter første innlogging.**

---

## Hvis du ser en sikkerhetsadvarsel

Hvis du åpner appen via HTTP (før SSL er konfigurert), vil du se:

- Et gult advarselsbanner øverst på innloggingssiden
- En modal når du klikker **Logg inn**, som advarer om at legitimasjon vil sendes ukryptert

<!-- SCREENSHOT NEEDED: HTTP warning banner on login page -->
<!-- SCREENSHOT NEEDED: SSL warning modal with "Set up SSL" and "Continue anyway" buttons -->

Klikk **Sett opp SSL** for å konfigurere HTTPS, eller **Fortsett uansett** for å logge inn uten SSL (anbefales ikke).

SSO-innlogging er fullstendig blokkert via HTTP — å klikke **Logg inn med SSO** vil vise et varsel i stedet for å omdirigere.

---

## Etter innlogging

Når du er inne, lander du på dashbordet. Herfra:

1. **Endre administratorpassord** — kontoinnstillinger → endre passord
2. **Opprett ditt første prosjekt** — Prosjekter → Nytt prosjekt
3. **Last opp eller bygg et skjema** — Skjemaer → Last opp XLSForm eller åpne Form Builder
4. **Legg til brukere** — Brukere → Inviter eller opprett kontoer for teamet ditt
""",
        "nl": """> **SSL moet worden geconfigureerd voordat u kunt inloggen.** Als u de app via HTTP benadert, ziet u een beveiligingswaarschuwing en wordt SSO geblokkeerd. Voltooi eerst de [SSL-instelling](ssl-setup).

Nadat SSL actief is, open uw browser op uw HTTPS URL:

```
https://your-domain.com
```

---

## Het aanmeldscherm

<!-- SCREENSHOT NEEDED: login page over HTTPS — username/password form + SSO button -->

De aanmeldpagina toont:

- Velden voor **Gebruikersnaam** en **Wachtwoord**
- Een **Aanmelden** knop
- Een **Aanmelden met SSO** knop (onder een scheidslijn) — voor teamleden met SSO-accounts

---

## Standaard beheerdersgegevens

Voer de standaardgegevens in en klik op **Aanmelden**:

| Veld | Waarde |
|------|--------|
| Gebruikersnaam | `admin` |
| Wachtwoord | `admin` |

> **Wijzig uw wachtwoord onmiddellijk na uw eerste aanmelding.**

---

## Als u een beveiligingswaarschuwing ziet

Als u de app via HTTP benadert (voordat SSL is geconfigureerd), ziet u:

- Een gele waarschuwingsbanner bovenaan de aanmeldpagina
- Een modaal venster bij het klikken op **Aanmelden**, dat waarschuwt dat gegevens onversleuteld worden verzonden

<!-- SCREENSHOT NEEDED: HTTP warning banner on login page -->
<!-- SCREENSHOT NEEDED: SSL warning modal with "Set up SSL" and "Continue anyway" buttons -->

Klik op **SSL instellen** om HTTPS te configureren, of op **Toch doorgaan** om in te loggen zonder SSL (niet aanbevolen).

SSO-aanmelding is volledig geblokkeerd via HTTP — klikken op **Aanmelden met SSO** toont een melding in plaats van door te verwijzen.

---

## Na het aanmelden

Eenmaal binnen landt u op het dashboard. Van hieruit:

1. **Beheerderwachtwoord wijzigen** — accountinstellingen → wachtwoord wijzigen
2. **Uw eerste project aanmaken** — Projecten → Nieuw project
3. **Formulier uploaden of bouwen** — Formulieren → XLSForm uploaden of Form Builder openen
4. **Gebruikers toevoegen** — Gebruikers → Uitnodigen of accounts aanmaken voor uw team
""",
        "pl": """> **SSL musi być skonfigurowany przed zalogowaniem.** Jeśli uzyskasz dostęp do aplikacji przez HTTP, zobaczysz ostrzeżenie bezpieczeństwa i SSO zostanie zablokowane. Najpierw ukończ [Konfigurację SSL](ssl-setup).

Po aktywowaniu SSL otwórz przeglądarkę pod adresem HTTPS:

```
https://your-domain.com
```

---

## Ekran logowania

<!-- SCREENSHOT NEEDED: login page over HTTPS — username/password form + SSO button -->

Strona logowania pokazuje:

- Pola **Nazwa użytkownika** i **Hasło**
- Przycisk **Zaloguj się**
- Przycisk **Zaloguj się przez SSO** (poniżej separatora) — dla członków zespołu z kontami SSO

---

## Domyślne dane logowania administratora

Wprowadź domyślne dane i kliknij **Zaloguj się**:

| Pole | Wartość |
|------|---------|
| Nazwa użytkownika | `admin` |
| Hasło | `admin` |

> **Zmień hasło natychmiast po pierwszym logowaniu.**

---

## Jeśli pojawi się ostrzeżenie bezpieczeństwa

Jeśli uzyskasz dostęp do aplikacji przez HTTP (przed konfiguracją SSL), zobaczysz:

- Żółty baner ostrzegawczy na górze strony logowania
- Okno modalne po kliknięciu **Zaloguj się**, ostrzegające, że dane zostaną wysłane niezaszyfrowane

<!-- SCREENSHOT NEEDED: HTTP warning banner on login page -->
<!-- SCREENSHOT NEEDED: SSL warning modal with "Set up SSL" and "Continue anyway" buttons -->

Kliknij **Skonfiguruj SSL**, aby skonfigurować HTTPS, lub **Kontynuuj mimo to** aby zalogować się bez SSL (niezalecane).

Logowanie SSO jest całkowicie zablokowane przez HTTP — kliknięcie **Zaloguj się przez SSO** wyświetli powiadomienie zamiast przekierowania.

---

## Po zalogowaniu

Po zalogowaniu znajdziesz się na pulpicie nawigacyjnym. Stąd:

1. **Zmień hasło administratora** — ustawienia konta → zmień hasło
2. **Utwórz swój pierwszy projekt** — Projekty → Nowy projekt
3. **Prześlij lub utwórz formularz** — Formularze → Prześlij XLSForm lub otwórz Form Builder
4. **Dodaj użytkowników** — Użytkownicy → Zaproś lub utwórz konta dla swojego zespołu
""",
        "pt": """> **O SSL tem de ser configurado antes de iniciar sessão.** Se aceder à aplicação via HTTP, verá um aviso de segurança e o SSO será bloqueado. Complete primeiro a [Configuração de SSL](ssl-setup).

Depois de o SSL estar ativo, abra o seu browser no URL HTTPS:

```
https://your-domain.com
```

---

## O ecrã de início de sessão

<!-- SCREENSHOT NEEDED: login page over HTTPS — username/password form + SSO button -->

A página de início de sessão mostra:

- Campos de **Nome de utilizador** e **Palavra-passe**
- Um botão **Iniciar sessão**
- Um botão **Iniciar sessão com SSO** (abaixo de um separador) — para membros da equipa com contas SSO

---

## Credenciais de administrador predefinidas

Introduza as credenciais predefinidas e clique em **Iniciar sessão**:

| Campo | Valor |
|-------|-------|
| Nome de utilizador | `admin` |
| Palavra-passe | `admin` |

> **Altere a sua palavra-passe imediatamente após o primeiro início de sessão.**

---

## Se vir um aviso de segurança

Se aceder à aplicação via HTTP (antes de o SSL estar configurado), verá:

- Um banner de aviso amarelo no topo da página de início de sessão
- Um modal ao clicar em **Iniciar sessão**, avisando que as credenciais serão enviadas sem encriptação

<!-- SCREENSHOT NEEDED: HTTP warning banner on login page -->
<!-- SCREENSHOT NEEDED: SSL warning modal with "Set up SSL" and "Continue anyway" buttons -->

Clique em **Configurar SSL** para configurar HTTPS, ou em **Continuar mesmo assim** para iniciar sessão sem SSL (não recomendado).

O início de sessão SSO está completamente bloqueado via HTTP — clicar em **Iniciar sessão com SSO** mostrará um aviso em vez de redirecionar.

---

## Após o início de sessão

Depois de entrar, chegará ao painel de controlo. Daqui:

1. **Alterar a palavra-passe do administrador** — definições de conta → alterar palavra-passe
2. **Criar o primeiro projeto** — Projetos → Novo projeto
3. **Carregar ou criar um formulário** — Formulários → Carregar XLSForm ou abrir Form Builder
4. **Adicionar utilizadores** — Utilizadores → Convidar ou criar contas para a sua equipa
""",
        "pt-br": """> **O SSL deve ser configurado antes de fazer login.** Se você acessar o aplicativo via HTTP, verá um aviso de segurança e o SSO será bloqueado. Conclua a [Configuração de SSL](ssl-setup) primeiro.

Depois que o SSL estiver ativo, abra seu navegador na URL HTTPS:

```
https://your-domain.com
```

---

## A tela de login

<!-- SCREENSHOT NEEDED: login page over HTTPS — username/password form + SSO button -->

A página de login mostra:

- Campos de **Usuário** e **Senha**
- Um botão **Entrar**
- Um botão **Entrar com SSO** (abaixo de um divisor) — para membros da equipe com contas SSO

---

## Credenciais padrão do administrador

Insira as credenciais padrão e clique em **Entrar**:

| Campo | Valor |
|-------|-------|
| Usuário | `admin` |
| Senha | `admin` |

> **Altere sua senha imediatamente após o primeiro login.**

---

## Se você vir um aviso de segurança

Se você acessar o aplicativo via HTTP (antes de o SSL ser configurado), verá:

- Um banner de aviso amarelo no topo da página de login
- Um modal ao clicar em **Entrar**, avisando que as credenciais serão enviadas sem criptografia

<!-- SCREENSHOT NEEDED: HTTP warning banner on login page -->
<!-- SCREENSHOT NEEDED: SSL warning modal with "Set up SSL" and "Continue anyway" buttons -->

Clique em **Configurar SSL** para configurar HTTPS ou em **Continuar assim mesmo** para fazer login sem SSL (não recomendado).

O login SSO está completamente bloqueado via HTTP — clicar em **Entrar com SSO** mostrará um aviso em vez de redirecionar.

---

## Após o login

Depois de entrar, você chegará ao painel. Daqui:

1. **Alterar a senha do administrador** — configurações de conta → alterar senha
2. **Criar seu primeiro projeto** — Projetos → Novo projeto
3. **Fazer upload ou criar um formulário** — Formulários → Fazer upload de XLSForm ou abrir o Form Builder
4. **Adicionar usuários** — Usuários → Convidar ou criar contas para sua equipe
""",
        "ru": """> **Перед входом необходимо настроить SSL.** Если вы обращаетесь к приложению через HTTP, вы увидите предупреждение безопасности, и SSO будет заблокирован. Сначала выполните [Настройку SSL](ssl-setup).

После активации SSL откройте браузер по вашему HTTPS-адресу:

```
https://your-domain.com
```

---

## Экран входа

<!-- SCREENSHOT NEEDED: login page over HTTPS — username/password form + SSO button -->

Страница входа показывает:

- Поля **Имя пользователя** и **Пароль**
- Кнопку **Войти**
- Кнопку **Войти через SSO** (под разделителем) — для членов команды с SSO-аккаунтами

---

## Учётные данные администратора по умолчанию

Введите учётные данные по умолчанию и нажмите **Войти**:

| Поле | Значение |
|------|---------|
| Имя пользователя | `admin` |
| Пароль | `admin` |

> **Смените пароль сразу после первого входа.**

---

## Если появляется предупреждение безопасности

Если вы обращаетесь к приложению через HTTP (до настройки SSL), вы увидите:

- Жёлтый баннер предупреждения в верхней части страницы входа
- Модальное окно при нажатии **Войти**, предупреждающее, что учётные данные будут отправлены незашифрованными

<!-- SCREENSHOT NEEDED: HTTP warning banner on login page -->
<!-- SCREENSHOT NEEDED: SSL warning modal with "Set up SSL" and "Continue anyway" buttons -->

Нажмите **Настроить SSL** для настройки HTTPS или **Продолжить в любом случае** для входа без SSL (не рекомендуется).

Вход через SSO полностью заблокирован по HTTP — нажатие **Войти через SSO** покажет уведомление вместо перенаправления.

---

## После входа

После входа вы окажетесь на панели управления. Отсюда:

1. **Сменить пароль администратора** — настройки аккаунта → сменить пароль
2. **Создать первый проект** — Проекты → Новый проект
3. **Загрузить или создать форму** — Формы → Загрузить XLSForm или открыть Form Builder
4. **Добавить пользователей** — Пользователи → Пригласить или создать аккаунты для команды
""",
        "sk": """> **Pred prihlásením musí byť nakonfigurovaný SSL.** Ak pristupujete k aplikácii cez HTTP, zobrazí sa bezpečnostné upozornenie a SSO bude zablokované. Najprv dokončite [Nastavenie SSL](ssl-setup).

Po aktivácii SSL otvorte prehliadač na vašej HTTPS adrese:

```
https://your-domain.com
```

---

## Prihlasovacia obrazovka

<!-- SCREENSHOT NEEDED: login page over HTTPS — username/password form + SSO button -->

Prihlasovacia stránka zobrazuje:

- Polia **Používateľské meno** a **Heslo**
- Tlačidlo **Prihlásiť sa**
- Tlačidlo **Prihlásiť sa cez SSO** (pod oddeľovačom) — pre členov tímu s SSO účtami

---

## Predvolené prihlasovacie údaje správcu

Zadajte predvolené prihlasovacie údaje a kliknite na **Prihlásiť sa**:

| Pole | Hodnota |
|------|---------|
| Používateľské meno | `admin` |
| Heslo | `admin` |

> **Zmeňte heslo ihneď po prvom prihlásení.**

---

## Ak sa zobrazí bezpečnostné upozornenie

Ak pristupujete k aplikácii cez HTTP (pred konfiguráciou SSL), uvidíte:

- Žltý varovný banner v hornej časti prihlasovacej stránky
- Modálne okno pri kliknutí na **Prihlásiť sa**, upozorňujúce, že prihlasovacie údaje budú odoslané nešifrovane

<!-- SCREENSHOT NEEDED: HTTP warning banner on login page -->
<!-- SCREENSHOT NEEDED: SSL warning modal with "Set up SSL" and "Continue anyway" buttons -->

Kliknite na **Nastaviť SSL** pre konfiguráciu HTTPS alebo **Pokračovať napriek tomu** pre prihlásenie bez SSL (neodporúča sa).

Prihlásenie cez SSO je cez HTTP úplne zablokované — kliknutím na **Prihlásiť sa cez SSO** sa zobrazí oznámenie namiesto presmerovania.

---

## Po prihlásení

Po prihlásení pristanete na dashboarde. Odtiaľ:

1. **Zmeniť heslo správcu** — nastavenia účtu → zmeniť heslo
2. **Vytvoriť prvý projekt** — Projekty → Nový projekt
3. **Nahrať alebo vytvoriť formulár** — Formuláre → Nahrať XLSForm alebo otvoriť Form Builder
4. **Pridať používateľov** — Používatelia → Pozvať alebo vytvoriť účty pre váš tím
""",
        "sq": """> **SSL duhet konfiguruar para hyrjes.** Nëse aksesoni aplikacionin nëpërmjet HTTP, do të shihni një paralajmërim sigurie dhe SSO do të bllokohet. Plotësoni fillimisht [Konfigurimin e SSL](ssl-setup).

Pasi SSL të jetë aktiv, hapni shfletuesin tuaj në URL-in HTTPS:

```
https://your-domain.com
```

---

## Ekrani i hyrjes

<!-- SCREENSHOT NEEDED: login page over HTTPS — username/password form + SSO button -->

Faqja e hyrjes shfaq:

- Fushat **Emri i përdoruesit** dhe **Fjalëkalimi**
- Butonin **Hyr**
- Butonin **Hyr me SSO** (nën një ndarës) — për anëtarët e ekipit me llogari SSO

---

## Kredencialet e paracaktuara të administratorit

Vendosni kredencialet e paracaktuara dhe klikoni **Hyr**:

| Fusha | Vlera |
|-------|-------|
| Emri i përdoruesit | `admin` |
| Fjalëkalimi | `admin` |

> **Ndryshoni fjalëkalimin tuaj menjëherë pas hyrjes së parë.**

---

## Nëse shihni një paralajmërim sigurie

Nëse aksesoni aplikacionin nëpërmjet HTTP (para konfigurimit të SSL), do të shihni:

- Një baner paralajmërimi të verdhë në krye të faqes së hyrjes
- Një modal kur klikoni **Hyr**, që paralajmëron se kredencialet do të dërgohen të pashifruara

<!-- SCREENSHOT NEEDED: HTTP warning banner on login page -->
<!-- SCREENSHOT NEEDED: SSL warning modal with "Set up SSL" and "Continue anyway" buttons -->

Klikoni **Konfiguro SSL** për të konfiguruar HTTPS, ose **Vazhdoni gjithsesi** për të hyrë pa SSL (nuk rekomandohet).

Hyrja SSO është bllokuar plotësisht nëpërmjet HTTP — klikimi i **Hyr me SSO** do të shfaqë një njoftim në vend të ridrejtimit.

---

## Pas hyrjes

Pasi të jeni brenda, do të arrini në panel. Nga këtu:

1. **Ndryshoni fjalëkalimin e administratorit** — cilësimet e llogarisë → ndrysho fjalëkalimin
2. **Krijoni projektin tuaj të parë** — Projektet → Projekt i ri
3. **Ngarkoni ose ndërtoni një formular** — Formularët → Ngarko XLSForm ose hapni Form Builder
4. **Shtoni përdorues** — Përdoruesit → Ftoni ose krijoni llogari për ekipin tuaj
""",
        "sr": """> **SSL мора бити конфигурисан пре пријављивања.** Ако приступате апликацији преко HTTP, видећете безбедносно упозорење и SSO ће бити блокиран. Прво завршите [Подешавање SSL](ssl-setup).

Када је SSL активан, отворите прегледач на вашој HTTPS адреси:

```
https://your-domain.com
```

---

## Екран за пријавање

<!-- SCREENSHOT NEEDED: login page over HTTPS — username/password form + SSO button -->

Страница за пријавање показује:

- Поља **Корисничко ime** и **Лозинка**
- Дугме **Пријави се**
- Дугме **Пријави се преко SSO** (испод раздвајача) — за чланове тима са SSO налозима

---

## Подразумевани административни акредитиви

Унесите подразумеване акредитиве и кликните на **Пријави се**:

| Поље | Вредност |
|------|---------|
| Корисничко ime | `admin` |
| Лозинка | `admin` |

> **Одмах промените лозинку после прве пријаве.**

---

## Ако видите безбедносно упозорење

Ако приступате апликацији преко HTTP (пре конфигурисања SSL), видећете:

- Жути баннер упозорења на врху странице за пријаву
- Модални прозор при клику на **Пријави се**, упозоравајући да ће акредитиви бити послати нешифровано

<!-- SCREENSHOT NEEDED: HTTP warning banner on login page -->
<!-- SCREENSHOT NEEDED: SSL warning modal with "Set up SSL" and "Continue anyway" buttons -->

Кликните на **Подеси SSL** за конфигурисање HTTPS, или **Наставите ипак** за пријаву без SSL (не препоручује се).

SSO пријава је потпуно блокирана преко HTTP — кликом на **Пријави се преко SSO** биће приказано обавештење уместо преусмеравања.

---

## После пријаве

Када уђете, доспећете на контролну таблу. Одатле:

1. **Промените лозинку администратора** — подешавања налога → промени лозинку
2. **Направите свој prvi пројекат** — Пројекти → Нови пројекат
3. **Отпремите или направите образац** — Обрасци → Отпремите XLSForm или отворите Form Builder
4. **Додајте кориснике** — Корисници → Позовите или направите налоге за ваш тим
""",
        "sv": """> **SSL måste konfigureras innan du loggar in.** Om du öppnar appen via HTTP kommer du att se en säkerhetsvarning och SSO blockeras. Slutför [SSL-konfiguration](ssl-setup) först.

När SSL är aktivt, öppna din webbläsare på din HTTPS-URL:

```
https://your-domain.com
```

---

## Inloggningsskärmen

<!-- SCREENSHOT NEEDED: login page over HTTPS — username/password form + SSO button -->

Inloggningssidan visar:

- Fält för **Användarnamn** och **Lösenord**
- En **Logga in** knapp
- En **Logga in med SSO** knapp (under en avdelare) — för teammedlemmar med SSO-konton

---

## Standardadministratörsinloggning

Ange standarduppgifterna och klicka på **Logga in**:

| Fält | Värde |
|------|-------|
| Användarnamn | `admin` |
| Lösenord | `admin` |

> **Byt lösenord omedelbart efter din första inloggning.**

---

## Om du ser en säkerhetsvarning

Om du öppnar appen via HTTP (innan SSL är konfigurerat) kommer du att se:

- En gul varningsbanner högst upp på inloggningssidan
- En modal när du klickar på **Logga in**, som varnar för att inloggningsuppgifter skickas okrypterade

<!-- SCREENSHOT NEEDED: HTTP warning banner on login page -->
<!-- SCREENSHOT NEEDED: SSL warning modal with "Set up SSL" and "Continue anyway" buttons -->

Klicka på **Konfigurera SSL** för att konfigurera HTTPS, eller **Fortsätt ändå** för att logga in utan SSL (rekommenderas inte).

SSO-inloggning är helt blockerad via HTTP — att klicka på **Logga in med SSO** visar ett meddelande istället för att omdirigera.

---

## Efter inloggning

När du är inne landas du på dashboarden. Härifrån:

1. **Byt administratörslösenord** — kontoinställningar → byt lösenord
2. **Skapa ditt första projekt** — Projekt → Nytt projekt
3. **Ladda upp eller bygg ett formulär** — Formulär → Ladda upp XLSForm eller öppna Form Builder
4. **Lägg till användare** — Användare → Bjud in eller skapa konton för ditt team
""",
        "te": """> **లాగిన్ కావడానికి ముందు SSL కాన్ఫిగర్ చేయబడాలి.** మీరు HTTP ద్వారా యాప్‌ను యాక్సెస్ చేస్తే, మీరు భద్రతా హెచ్చరికను చూస్తారు మరియు SSO నిరోధించబడుతుంది. ముందు [SSL సెటప్](ssl-setup) పూర్తి చేయండి.

SSL యాక్టివ్ అయిన తర్వాత, మీ HTTPS URL లో బ్రౌజర్ తెరవండి:

```
https://your-domain.com
```

---

## లాగిన్ స్క్రీన్

<!-- SCREENSHOT NEEDED: login page over HTTPS — username/password form + SSO button -->

లాగిన్ పేజీ చూపిస్తుంది:

- **వినియోగదారు పేరు** మరియు **పాస్‌వర్డ్** ఫీల్డ్‌లు
- ఒక **సైన్ ఇన్** బటన్
- ఒక **SSO తో లాగిన్** బటన్ (విభజకం క్రింద) — SSO ఖాతాలు ఉన్న జట్టు సభ్యుల కోసం

---

## డిఫాల్ట్ అడ్మిన్ క్రెడెన్షియల్స్

డిఫాల్ట్ క్రెడెన్షియల్స్ నమోదు చేసి **సైన్ ఇన్** క్లిక్ చేయండి:

| ఫీల్డ్ | విలువ |
|--------|-------|
| వినియోగదారు పేరు | `admin` |
| పాస్‌వర్డ్ | `admin` |

> **మీ మొదటి లాగిన్ తర్వాత వెంటనే పాస్‌వర్డ్ మార్చండి.**

---

## మీరు భద్రతా హెచ్చరిక చూస్తే

మీరు HTTP ద్వారా యాప్‌ను యాక్సెస్ చేస్తే (SSL కాన్ఫిగర్ కావడానికి ముందు), మీరు చూస్తారు:

- లాగిన్ పేజీ పైభాగంలో పసుపు హెచ్చరిక బ్యానర్
- **సైన్ ఇన్** క్లిక్ చేసినప్పుడు ఒక మోడల్, క్రెడెన్షియల్స్ గుప్తీకరించకుండా పంపబడతాయని హెచ్చరిస్తుంది

<!-- SCREENSHOT NEEDED: HTTP warning banner on login page -->
<!-- SCREENSHOT NEEDED: SSL warning modal with "Set up SSL" and "Continue anyway" buttons -->

HTTPS కాన్ఫిగర్ చేయడానికి **SSL సెటప్ చేయండి** క్లిక్ చేయండి, లేదా SSL లేకుండా లాగిన్ అవడానికి **అయినా కొనసాగించండి** క్లిక్ చేయండి (సిఫార్సు చేయబడలేదు).

HTTP ద్వారా SSO లాగిన్ పూర్తిగా నిరోధించబడింది — **SSO తో లాగిన్** క్లిక్ చేయడం రీడైరెక్ట్ కాకుండా నోటీసు చూపిస్తుంది.

---

## లాగిన్ తర్వాత

లోపలికి వెళ్ళిన తర్వాత, మీరు డాష్‌బోర్డ్‌కు చేరుకుంటారు. ఇక్కడ నుండి:

1. **అడ్మిన్ పాస్‌వర్డ్ మార్చండి** — ఖాతా సెట్టింగులు → పాస్‌వర్డ్ మార్చండి
2. **మీ మొదటి ప్రాజెక్ట్ సృష్టించండి** — ప్రాజెక్ట్‌లు → కొత్త ప్రాజెక్ట్
3. **ఫారమ్ అప్‌లోడ్ చేయండి లేదా నిర్మించండి** — ఫారమ్‌లు → XLSForm అప్‌లోడ్ చేయండి లేదా Form Builder తెరవండి
4. **వినియోగదారులను జోడించండి** — వినియోగదారులు → మీ జట్టు కోసం ఖాతాలు ఆహ్వానించండి లేదా సృష్టించండి
""",
        "th": """> **ต้องกำหนดค่า SSL ก่อนเข้าสู่ระบบ** หากคุณเข้าถึงแอปผ่าน HTTP คุณจะเห็นคำเตือนด้านความปลอดภัยและ SSO จะถูกบล็อก ให้ทำ [การตั้งค่า SSL](ssl-setup) ให้เสร็จก่อน

หลังจาก SSL ใช้งานได้แล้ว เปิดเบราว์เซอร์ที่ URL HTTPS ของคุณ:

```
https://your-domain.com
```

---

## หน้าจอเข้าสู่ระบบ

<!-- SCREENSHOT NEEDED: login page over HTTPS — username/password form + SSO button -->

หน้าเข้าสู่ระบบแสดง:

- ช่อง **ชื่อผู้ใช้** และ **รหัสผ่าน**
- ปุ่ม **ลงชื่อเข้าใช้**
- ปุ่ม **เข้าสู่ระบบด้วย SSO** (ด้านล่างตัวคั่น) — สำหรับสมาชิกทีมที่มีบัญชี SSO

---

## ข้อมูลรับรองผู้ดูแลระบบเริ่มต้น

ป้อนข้อมูลรับรองเริ่มต้นและคลิก **ลงชื่อเข้าใช้**:

| ฟิลด์ | ค่า |
|-------|-----|
| ชื่อผู้ใช้ | `admin` |
| รหัสผ่าน | `admin` |

> **เปลี่ยนรหัสผ่านของคุณทันทีหลังจากเข้าสู่ระบบครั้งแรก**

---

## หากคุณเห็นคำเตือนด้านความปลอดภัย

หากคุณเข้าถึงแอปผ่าน HTTP (ก่อนกำหนดค่า SSL) คุณจะเห็น:

- แบนเนอร์คำเตือนสีเหลืองที่ด้านบนของหน้าเข้าสู่ระบบ
- หน้าต่างป๊อปอัปเมื่อคลิก **ลงชื่อเข้าใช้** เตือนว่าข้อมูลรับรองจะถูกส่งโดยไม่เข้ารหัส

<!-- SCREENSHOT NEEDED: HTTP warning banner on login page -->
<!-- SCREENSHOT NEEDED: SSL warning modal with "Set up SSL" and "Continue anyway" buttons -->

คลิก **ตั้งค่า SSL** เพื่อกำหนดค่า HTTPS หรือ **ดำเนินการต่อไปอยู่ดี** เพื่อเข้าสู่ระบบโดยไม่มี SSL (ไม่แนะนำ)

การเข้าสู่ระบบ SSO ถูกบล็อกทั้งหมดผ่าน HTTP — การคลิก **เข้าสู่ระบบด้วย SSO** จะแสดงการแจ้งเตือนแทนการเปลี่ยนเส้นทาง

---

## หลังจากเข้าสู่ระบบ

เมื่อเข้ามาแล้ว คุณจะอยู่ที่แดชบอร์ด จากที่นี่:

1. **เปลี่ยนรหัสผ่านผู้ดูแลระบบ** — การตั้งค่าบัญชี → เปลี่ยนรหัสผ่าน
2. **สร้างโปรเจกต์แรกของคุณ** — โปรเจกต์ → โปรเจกต์ใหม่
3. **อัปโหลดหรือสร้างแบบฟอร์ม** — แบบฟอร์ม → อัปโหลด XLSForm หรือเปิด Form Builder
4. **เพิ่มผู้ใช้** — ผู้ใช้ → เชิญหรือสร้างบัญชีสำหรับทีมของคุณ
""",
        "tr": """> **Giriş yapmadan önce SSL yapılandırılmalıdır.** Uygulamaya HTTP üzerinden erişirseniz bir güvenlik uyarısı görürsünüz ve SSO engellenecektir. Önce [SSL Kurulumu](ssl-setup) tamamlayın.

SSL etkin olduktan sonra, tarayıcınızı HTTPS URL'nizde açın:

```
https://your-domain.com
```

---

## Giriş ekranı

<!-- SCREENSHOT NEEDED: login page over HTTPS — username/password form + SSO button -->

Giriş sayfası şunları gösterir:

- **Kullanıcı Adı** ve **Şifre** alanları
- **Giriş Yap** düğmesi
- **SSO ile Giriş Yap** düğmesi (ayırıcının altında) — SSO hesapları olan ekip üyeleri için

---

## Varsayılan yönetici kimlik bilgileri

Varsayılan kimlik bilgilerini girin ve **Giriş Yap**'a tıklayın:

| Alan | Değer |
|------|-------|
| Kullanıcı Adı | `admin` |
| Şifre | `admin` |

> **İlk girişinizden hemen sonra şifrenizi değiştirin.**

---

## Güvenlik uyarısı görürseniz

Uygulamaya HTTP üzerinden erişirseniz (SSL yapılandırılmadan önce) şunları görürsünüz:

- Giriş sayfasının üstünde sarı bir uyarı banner'ı
- **Giriş Yap**'a tıkladığınızda kimlik bilgilerinin şifresiz gönderileceğini uyaran bir modal

<!-- SCREENSHOT NEEDED: HTTP warning banner on login page -->
<!-- SCREENSHOT NEEDED: SSL warning modal with "Set up SSL" and "Continue anyway" buttons -->

HTTPS yapılandırmak için **SSL Kur**'a tıklayın veya SSL olmadan giriş yapmak için **Yine de devam et**'e tıklayın (önerilmez).

SSO girişi HTTP üzerinden tamamen engellenmiştir — **SSO ile Giriş Yap**'a tıklamak yönlendirme yerine bir bildirim gösterecektir.

---

## Giriş yaptıktan sonra

İçeri girdikten sonra panoya gelirsiniz. Buradan:

1. **Yönetici şifresini değiştirin** — hesap ayarları → şifreyi değiştir
2. **İlk projenizi oluşturun** — Projeler → Yeni Proje
3. **Form yükleyin veya oluşturun** — Formlar → XLSForm Yükle veya Form Builder'ı aç
4. **Kullanıcı ekleyin** — Kullanıcılar → Ekibiniz için hesap davet edin veya oluşturun
""",
        "uk": """> **Перед входом потрібно налаштувати SSL.** Якщо ви отримуєте доступ до застосунку через HTTP, ви побачите попередження безпеки, а SSO буде заблоковано. Спочатку виконайте [Налаштування SSL](ssl-setup).

Після активації SSL відкрийте браузер за своєю HTTPS-адресою:

```
https://your-domain.com
```

---

## Екран входу

<!-- SCREENSHOT NEEDED: login page over HTTPS — username/password form + SSO button -->

Сторінка входу показує:

- Поля **Ім'я користувача** та **Пароль**
- Кнопку **Увійти**
- Кнопку **Увійти через SSO** (під роздільником) — для членів команди з SSO-акаунтами

---

## Облікові дані адміністратора за замовчуванням

Введіть облікові дані за замовчуванням і натисніть **Увійти**:

| Поле | Значення |
|------|---------|
| Ім'я користувача | `admin` |
| Пароль | `admin` |

> **Змініть пароль одразу після першого входу.**

---

## Якщо з'являється попередження безпеки

Якщо ви отримуєте доступ до застосунку через HTTP (до налаштування SSL), ви побачите:

- Жовтий банер попередження у верхній частині сторінки входу
- Модальне вікно при натисканні **Увійти**, що попереджає про відправлення облікових даних без шифрування

<!-- SCREENSHOT NEEDED: HTTP warning banner on login page -->
<!-- SCREENSHOT NEEDED: SSL warning modal with "Set up SSL" and "Continue anyway" buttons -->

Натисніть **Налаштувати SSL** для налаштування HTTPS або **Продовжити в будь-якому разі** для входу без SSL (не рекомендується).

Вхід через SSO повністю заблоковано через HTTP — натискання **Увійти через SSO** покаже сповіщення замість перенаправлення.

---

## Після входу

Після входу ви потрапите на панель керування. Звідси:

1. **Змінити пароль адміністратора** — налаштування акаунта → змінити пароль
2. **Створити перший проєкт** — Проєкти → Новий проєкт
3. **Завантажити або створити форму** — Форми → Завантажити XLSForm або відкрити Form Builder
4. **Додати користувачів** — Користувачі → Запросити або створити акаунти для команди
""",
        "vi": """> **SSL phải được cấu hình trước khi đăng nhập.** Nếu bạn truy cập ứng dụng qua HTTP, bạn sẽ thấy cảnh báo bảo mật và SSO sẽ bị chặn. Hãy hoàn thành [Cài đặt SSL](ssl-setup) trước.

Sau khi SSL hoạt động, mở trình duyệt tại URL HTTPS của bạn:

```
https://your-domain.com
```

---

## Màn hình đăng nhập

<!-- SCREENSHOT NEEDED: login page over HTTPS — username/password form + SSO button -->

Trang đăng nhập hiển thị:

- Các trường **Tên người dùng** và **Mật khẩu**
- Nút **Đăng nhập**
- Nút **Đăng nhập bằng SSO** (bên dưới đường phân cách) — cho thành viên nhóm có tài khoản SSO

---

## Thông tin đăng nhập quản trị viên mặc định

Nhập thông tin đăng nhập mặc định và nhấp **Đăng nhập**:

| Trường | Giá trị |
|--------|---------|
| Tên người dùng | `admin` |
| Mật khẩu | `admin` |

> **Hãy đổi mật khẩu ngay sau lần đăng nhập đầu tiên.**

---

## Nếu bạn thấy cảnh báo bảo mật

Nếu bạn truy cập ứng dụng qua HTTP (trước khi SSL được cấu hình), bạn sẽ thấy:

- Biểu ngữ cảnh báo màu vàng ở đầu trang đăng nhập
- Hộp thoại khi nhấp **Đăng nhập**, cảnh báo rằng thông tin đăng nhập sẽ được gửi không mã hóa

<!-- SCREENSHOT NEEDED: HTTP warning banner on login page -->
<!-- SCREENSHOT NEEDED: SSL warning modal with "Set up SSL" and "Continue anyway" buttons -->

Nhấp **Cài đặt SSL** để cấu hình HTTPS, hoặc **Tiếp tục dù sao** để đăng nhập không có SSL (không khuyến nghị).

Đăng nhập SSO bị chặn hoàn toàn qua HTTP — nhấp **Đăng nhập bằng SSO** sẽ hiển thị thông báo thay vì chuyển hướng.

---

## Sau khi đăng nhập

Khi vào trong, bạn sẽ thấy bảng điều khiển. Từ đây:

1. **Đổi mật khẩu quản trị viên** — cài đặt tài khoản → đổi mật khẩu
2. **Tạo dự án đầu tiên** — Dự án → Dự án mới
3. **Tải lên hoặc xây dựng biểu mẫu** — Biểu mẫu → Tải lên XLSForm hoặc mở Form Builder
4. **Thêm người dùng** — Người dùng → Mời hoặc tạo tài khoản cho nhóm của bạn
""",
        "zh-hans": """> **登录前必须配置 SSL。** 如果您通过 HTTP 访问应用，将看到安全警告且 SSO 将被阻止。请先完成 [SSL 设置](ssl-setup)。

SSL 激活后，在您的 HTTPS 地址打开浏览器：

```
https://your-domain.com
```

---

## 登录界面

<!-- SCREENSHOT NEEDED: login page over HTTPS — username/password form + SSO button -->

登录页面显示：

- **用户名**和**密码**字段
- **登录**按钮
- **使用 SSO 登录**按钮（分隔线下方）— 供拥有 SSO 账户的团队成员使用

---

## 默认管理员凭据

输入默认凭据并点击**登录**：

| 字段 | 值 |
|------|----|
| 用户名 | `admin` |
| 密码 | `admin` |

> **首次登录后立即更改密码。**

---

## 如果看到安全警告

如果您通过 HTTP 访问应用（SSL 配置前），将看到：

- 登录页面顶部的黄色警告横幅
- 点击**登录**时弹出的模态框，警告凭据将以未加密形式发送

<!-- SCREENSHOT NEEDED: HTTP warning banner on login page -->
<!-- SCREENSHOT NEEDED: SSL warning modal with "Set up SSL" and "Continue anyway" buttons -->

点击**设置 SSL** 来配置 HTTPS，或点击**无论如何继续**以不使用 SSL 登录（不推荐）。

HTTP 上的 SSO 登录被完全阻止——点击**使用 SSO 登录**将显示通知而非重定向。

---

## 登录后

登录后，您将进入仪表板。从这里：

1. **更改管理员密码** — 账户设置 → 更改密码
2. **创建第一个项目** — 项目 → 新建项目
3. **上传或构建表单** — 表单 → 上传 XLSForm 或打开表单构建器
4. **添加用户** — 用户 → 邀请或为您的团队创建账户
""",
        "zh-hant": """> **登入前必須設定 SSL。** 如果您透過 HTTP 存取應用程式，將看到安全性警告且 SSO 將被封鎖。請先完成 [SSL 設定](ssl-setup)。

SSL 啟用後，在您的 HTTPS 網址開啟瀏覽器：

```
https://your-domain.com
```

---

## 登入畫面

<!-- SCREENSHOT NEEDED: login page over HTTPS — username/password form + SSO button -->

登入頁面顯示：

- **使用者名稱**和**密碼**欄位
- **登入**按鈕
- **使用 SSO 登入**按鈕（分隔線下方）— 供擁有 SSO 帳戶的團隊成員使用

---

## 預設管理員憑證

輸入預設憑證並點選**登入**：

| 欄位 | 值 |
|------|----|
| 使用者名稱 | `admin` |
| 密碼 | `admin` |

> **首次登入後立即變更密碼。**

---

## 如果看到安全性警告

如果您透過 HTTP 存取應用程式（SSL 設定前），將看到：

- 登入頁面頂部的黃色警告橫幅
- 點選**登入**時彈出的對話框，警告憑證將以未加密形式傳送

<!-- SCREENSHOT NEEDED: HTTP warning banner on login page -->
<!-- SCREENSHOT NEEDED: SSL warning modal with "Set up SSL" and "Continue anyway" buttons -->

點選**設定 SSL** 來設定 HTTPS，或點選**無論如何繼續**以不使用 SSL 登入（不建議）。

HTTP 上的 SSO 登入被完全封鎖——點選**使用 SSO 登入**將顯示通知而非重新導向。

---

## 登入後

登入後，您將進入儀表板。從這裡：

1. **變更管理員密碼** — 帳戶設定 → 變更密碼
2. **建立第一個專案** — 專案 → 新增專案
3. **上傳或建立表單** — 表單 → 上傳 XLSForm 或開啟表單建構器
4. **新增使用者** — 使用者 → 邀請或為您的團隊建立帳戶
""",
    },
}

# ═══════════════════════════════════════════════════════════════
# HELPER: build front matter + body -> full file content
# ═══════════════════════════════════════════════════════════════

def build_file(file_def, lang):
    meta = file_def["meta"]
    title = file_def["titles"][lang]
    desc = file_def["descriptions"][lang]
    body = file_def["bodies"][lang]

    lines = ["---"]
    lines.append(f'weight: {meta["weight"]}')
    lines.append(f'title: "{title}"')
    lines.append(f'date: "{meta["date"]}"')
    lines.append(f'lastmod: "{meta["lastmod"]}"')
    lines.append(f'draft: {meta["draft"]}')
    lines.append(f'author: "{meta["author"]}"')
    lines.append(f'icon: "{meta["icon"]}"')
    lines.append(f'toc: {meta["toc"]}')
    lines.append(f'description: "{desc}"')
    lines.append("---")
    lines.append("")
    lines.append(body.rstrip())
    lines.append("")
    return "\n".join(lines)


def write_file(rel_path, lang, content):
    full_path = os.path.join(BASE, lang, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)


# ═══════════════════════════════════════════════════════════════
# MAIN — write first-login only (remaining files in separate script sections)
# ═══════════════════════════════════════════════════════════════

count = 0
for rel_path, file_def in FILES.items():
    for lang in LANGUAGES:
        content = build_file(file_def, lang)
        write_file(rel_path, lang, content)
        count += 1

print(f"Written {count} files.")
