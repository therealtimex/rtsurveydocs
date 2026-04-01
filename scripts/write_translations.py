#!/usr/bin/env python3
"""Write translated overview.md for all 35 languages."""
import os

CONTENT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "content")

FRONT = """---
weight: 1
date: "2026-04-01T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
title: "{title}"
icon: "rocket_launch"
toc: false
description: "{description}"
---

"""

TRANSLATIONS = {
    "ar": {
        "title": "نظرة عامة",
        "description": "ما هو rtSurvey، كيف يعمل، وما تحتاجه قبل البدء.",
        "body": """rtSurvey هو منصة ذاتية الاستضافة لتصميم النماذج وجمع البيانات الميدانية وتحليل النتائج في الوقت الفعلي. تشغّله على خادمك الخاص — بياناتك لا تغادر بنيتك التحتية أبداً.

---

## كيف يعمل

| الخطوة | ما تفعله |
|--------|---------|
| **١. النشر** | شغّل خادماً وأطلق مجموعة rtSurvey بسكريبت تلقائي واحد |
| **٢. التصميم** | أنشئ نماذج باستخدام XLSForm أو Form Builder المرئي |
| **٣. الجمع** | ترسل فرق الميدان البيانات عبر التطبيق المحمول أو المتصفح — عبر الإنترنت أو بدونه |
| **٤. التحليل** | راجع الإدخالات في لوحة التحكم، وصدّر إلى CSV/Stata، أو اتصل بـ Power BI / R |

---

## قبل أن تبدأ

تحتاج إلى:

- **خادم Linux** (أو حساب سحابي على Linode أو DigitalOcean أو AWS أو GCP)
- **اسم نطاق** يشير إلى خادمك
- حوالي **١٠ دقائق**

لا تحتاج إلى معرفة مسبقة بـ Docker — يتولى سكريبت النشر كل شيء.

---

## هل أنت مستعد؟

**[انشر خادمك ←](self-hosting/quick-start)**"""
    },
    "bg": {
        "title": "Преглед",
        "description": "Какво е rtSurvey, как работи и какво ви трябва преди да започнете.",
        "body": """rtSurvey е самостоятелно хоствана платформа за проектиране на формуляри, събиране на данни на терен и анализиране на резултати в реално време. Работи на вашия собствен сървър — данните ви никога не напускат вашата инфраструктура.

---

## Как работи

| Стъпка | Какво правите |
|--------|--------------|
| **1. Разгръщане** | Стартирайте сървър и пуснете rtSurvey стека с един автоматизиран скрипт |
| **2. Проектиране** | Създайте формуляри с XLSForm или визуалния Form Builder |
| **3. Събиране** | Полевите екипи изпращат данни чрез мобилното приложение или браузъра — онлайн или офлайн |
| **4. Анализиране** | Прегледайте подадените данни в таблото, експортирайте в CSV/Stata или се свържете с Power BI / R |

---

## Преди да започнете

Необходими са ви:

- **Linux сървър** (или облачен акаунт в Linode, DigitalOcean, AWS или GCP)
- **Домейн**, насочен към вашия сървър
- Около **10 минути**

Не се изисква предварително познаване на Docker — скриптът за разгръщане се грижи за всичко.

---

## Готови ли сте?

**[Разгърнете своя сървър →](self-hosting/quick-start)**"""
    },
    "cs": {
        "title": "Přehled",
        "description": "Co je rtSurvey, jak funguje a co potřebujete před začátkem.",
        "body": """rtSurvey je self-hosted platforma pro vytváření formulářů, sběr dat v terénu a analýzu výsledků v reálném čase. Provozujete ji na vlastním serveru — vaše data nikdy neopustí vaši infrastrukturu.

---

## Jak to funguje

| Krok | Co děláte |
|------|-----------|
| **1. Nasazení** | Spusťte server a spusťte stack rtSurvey jedním automatizovaným skriptem |
| **2. Návrh** | Vytvořte formuláře pomocí XLSForm nebo vizuálního Form Builderu |
| **3. Sběr** | Terénní týmy odesílají data přes mobilní aplikaci nebo prohlížeč — online nebo offline |
| **4. Analýza** | Zkontrolujte odeslané údaje v dashboardu, exportujte do CSV/Stata nebo se připojte k Power BI / R |

---

## Než začnete

Potřebujete:

- **Linux server** (nebo cloudový účet u Linode, DigitalOcean, AWS nebo GCP)
- **Doménové jméno** nasměrované na váš server
- Přibližně **10 minut**

Žádné předchozí znalosti Dockeru nejsou potřeba — o vše se postará nasazovací skript.

---

## Připraveni?

**[Nasaďte svůj server →](self-hosting/quick-start)**"""
    },
    "da": {
        "title": "Oversigt",
        "description": "Hvad rtSurvey er, hvordan det virker, og hvad du skal bruge inden du starter.",
        "body": """rtSurvey er en selvhostet platform til at designe formularer, indsamle data i felten og analysere resultater i realtid. Du kører det på din egen server — dine data forlader aldrig din infrastruktur.

---

## Sådan fungerer det

| Trin | Hvad du gør |
|------|-------------|
| **1. Implementer** | Start en server og kør rtSurvey-stakken med ét automatiseret script |
| **2. Design** | Opret formularer med XLSForm eller den visuelle Form Builder |
| **3. Indsaml** | Feltteams indsender data via mobilappen eller browseren — online eller offline |
| **4. Analysér** | Gennemgå indsendelser i dashboardet, eksportér til CSV/Stata eller forbind til Power BI / R |

---

## Inden du begynder

Du har brug for:

- En **Linux-server** (eller en cloudkonto hos Linode, DigitalOcean, AWS eller GCP)
- Et **domænenavn** der peger på din server
- Cirka **10 minutter**

Ingen forudgående Docker-viden påkrævet — implementeringsscriptet håndterer det hele.

---

## Klar?

**[Implementér din server →](self-hosting/quick-start)**"""
    },
    "de": {
        "title": "Übersicht",
        "description": "Was rtSurvey ist, wie es funktioniert und was Sie vor dem Start benötigen.",
        "body": """rtSurvey ist eine selbst gehostete Plattform zum Entwerfen von Formularen, Sammeln von Felddaten und Analysieren von Ergebnissen in Echtzeit. Sie betreiben es auf Ihrem eigenen Server — Ihre Daten verlassen niemals Ihre Infrastruktur.

---

## So funktioniert es

| Schritt | Was Sie tun |
|---------|-------------|
| **1. Bereitstellen** | Starten Sie einen Server und führen Sie den rtSurvey-Stack mit einem automatisierten Skript aus |
| **2. Entwerfen** | Erstellen Sie Formulare mit XLSForm oder dem visuellen Form Builder |
| **3. Erfassen** | Außendienstteams übermitteln Daten über die mobile App oder den Browser — online oder offline |
| **4. Analysieren** | Überprüfen Sie Einsendungen im Dashboard, exportieren Sie nach CSV/Stata oder verbinden Sie mit Power BI / R |

---

## Bevor Sie beginnen

Sie benötigen:

- Einen **Linux-Server** (oder ein Cloud-Konto bei Linode, DigitalOcean, AWS oder GCP)
- Einen **Domainnamen**, der auf Ihren Server zeigt
- Etwa **10 Minuten**

Keine Docker-Vorkenntnisse erforderlich — das Bereitstellungsskript erledigt alles.

---

## Bereit?

**[Stellen Sie Ihren Server bereit →](self-hosting/quick-start)**"""
    },
    "el": {
        "title": "Επισκόπηση",
        "description": "Τι είναι το rtSurvey, πώς λειτουργεί και τι χρειάζεστε πριν ξεκινήσετε.",
        "body": """Το rtSurvey είναι μια πλατφόρμα αυτο-φιλοξενίας για σχεδιασμό φορμών, συλλογή δεδομένων στο πεδίο και ανάλυση αποτελεσμάτων σε πραγματικό χρόνο. Την εκτελείτε στον δικό σας διακομιστή — τα δεδομένα σας δεν φεύγουν ποτέ από την υποδομή σας.

---

## Πώς λειτουργεί

| Βήμα | Τι κάνετε |
|------|-----------|
| **1. Ανάπτυξη** | Εκκινήστε έναν διακομιστή και τρέξτε το stack rtSurvey με ένα αυτοματοποιημένο script |
| **2. Σχεδιασμός** | Δημιουργήστε φόρμες με XLSForm ή τον οπτικό Form Builder |
| **3. Συλλογή** | Οι ομάδες πεδίου υποβάλλουν δεδομένα μέσω της εφαρμογής ή του προγράμματος περιήγησης — online ή offline |
| **4. Ανάλυση** | Ελέγξτε τις υποβολές στον πίνακα ελέγχου, εξάγετε σε CSV/Stata ή συνδεθείτε με Power BI / R |

---

## Πριν ξεκινήσετε

Χρειάζεστε:

- Έναν **διακομιστή Linux** (ή λογαριασμό cloud στο Linode, DigitalOcean, AWS ή GCP)
- Ένα **όνομα τομέα** που δείχνει στον διακομιστή σας
- Περίπου **10 λεπτά**

Δεν απαιτείται προηγούμενη γνώση Docker — το script ανάπτυξης φροντίζει τα πάντα.

---

## Έτοιμοι;

**[Αναπτύξτε τον διακομιστή σας →](self-hosting/quick-start)**"""
    },
    "es": {
        "title": "Descripción general",
        "description": "Qué es rtSurvey, cómo funciona y qué necesita antes de comenzar.",
        "body": """rtSurvey es una plataforma de alojamiento propio para diseñar formularios, recopilar datos en el campo y analizar resultados en tiempo real. Lo ejecuta en su propio servidor — sus datos nunca salen de su infraestructura.

---

## Cómo funciona

| Paso | Qué hace |
|------|----------|
| **1. Desplegar** | Inicie un servidor y ejecute la pila rtSurvey con un script automatizado |
| **2. Diseñar** | Cree formularios usando XLSForm o el Form Builder visual |
| **3. Recopilar** | Los equipos de campo envían datos a través de la app móvil o el navegador — en línea o sin conexión |
| **4. Analizar** | Revise las respuestas en el panel, exporte a CSV/Stata o conéctese a Power BI / R |

---

## Antes de empezar

Necesita:

- Un **servidor Linux** (o una cuenta en la nube en Linode, DigitalOcean, AWS o GCP)
- Un **nombre de dominio** que apunte a su servidor
- Aproximadamente **10 minutos**

No se requieren conocimientos previos de Docker — el script de despliegue lo maneja todo.

---

## ¿Listo?

**[Despliegue su servidor →](self-hosting/quick-start)**"""
    },
    "fi": {
        "title": "Yleiskatsaus",
        "description": "Mitä rtSurvey on, miten se toimii ja mitä tarvitset ennen aloittamista.",
        "body": """rtSurvey on itse isännöity alusta lomakkeiden suunnitteluun, kenttätiedon keräämiseen ja tulosten analysointiin reaaliajassa. Pyörität sitä omalla palvelimellasi — tietosi eivät koskaan poistu infrastruktuuristasi.

---

## Miten se toimii

| Vaihe | Mitä teet |
|-------|-----------|
| **1. Käyttöönotto** | Käynnistä palvelin ja aja rtSurvey-pino yhdellä automaattiskripting |
| **2. Suunnittelu** | Luo lomakkeita XLSFormilla tai visuaalisella Form Builderilla |
| **3. Keruu** | Kenttätiimit lähettävät tietoja mobiilisovelluksen tai selaimen kautta — verkossa tai offline-tilassa |
| **4. Analyysi** | Tarkastele lähetyksiä kojelaudalla, vie CSV/Stataan tai yhdistä Power BI:hin / R:ään |

---

## Ennen kuin aloitat

Tarvitset:

- **Linux-palvelimen** (tai pilvitilin Linodessa, DigitalOceanissa, AWS:ssä tai GCP:ssä)
- **Verkkotunnuksen**, joka osoittaa palvelimellesi
- Noin **10 minuuttia**

Docker-osaamisesta ei tarvitse huolehtia — käyttöönottoskripti hoitaa kaiken.

---

## Valmis?

**[Ota palvelimesi käyttöön →](self-hosting/quick-start)**"""
    },
    "fr": {
        "title": "Vue d'ensemble",
        "description": "Ce qu'est rtSurvey, comment il fonctionne et ce dont vous avez besoin avant de commencer.",
        "body": """rtSurvey est une plateforme auto-hébergée pour concevoir des formulaires, collecter des données sur le terrain et analyser les résultats en temps réel. Vous l'exécutez sur votre propre serveur — vos données ne quittent jamais votre infrastructure.

---

## Comment ça fonctionne

| Étape | Ce que vous faites |
|-------|-------------------|
| **1. Déployer** | Démarrez un serveur et lancez la stack rtSurvey avec un script automatisé |
| **2. Concevoir** | Créez des formulaires avec XLSForm ou le Form Builder visuel |
| **3. Collecter** | Les équipes terrain soumettent des données via l'appli mobile ou le navigateur — en ligne ou hors ligne |
| **4. Analyser** | Consultez les soumissions dans le tableau de bord, exportez en CSV/Stata ou connectez-vous à Power BI / R |

---

## Avant de commencer

Vous avez besoin de :

- Un **serveur Linux** (ou un compte cloud sur Linode, DigitalOcean, AWS ou GCP)
- Un **nom de domaine** pointant vers votre serveur
- Environ **10 minutes**

Aucune connaissance de Docker requise — le script de déploiement s'occupe de tout.

---

## Prêt ?

**[Déployez votre serveur →](self-hosting/quick-start)**"""
    },
    "hi": {
        "title": "अवलोकन",
        "description": "rtSurvey क्या है, यह कैसे काम करता है और शुरू करने से पहले आपको क्या चाहिए।",
        "body": """rtSurvey फॉर्म डिज़ाइन करने, मैदानी डेटा एकत्र करने और रियल-टाइम में परिणामों का विश्लेषण करने के लिए एक स्व-होस्टेड प्लेटफ़ॉर्म है। आप इसे अपने स्वयं के सर्वर पर चलाते हैं — आपका डेटा कभी भी आपकी अवसंरचना नहीं छोड़ता।

---

## यह कैसे काम करता है

| चरण | आप क्या करते हैं |
|-----|----------------|
| **1. तैनात करें** | एक सर्वर शुरू करें और एक स्वचालित स्क्रिप्ट के साथ rtSurvey स्टैक चलाएं |
| **2. डिज़ाइन करें** | XLSForm या विज़ुअल Form Builder का उपयोग करके फॉर्म बनाएं |
| **3. एकत्र करें** | मैदानी टीमें मोबाइल ऐप या ब्राउज़र के माध्यम से डेटा जमा करती हैं — ऑनलाइन या ऑफलाइन |
| **4. विश्लेषण करें** | डैशबोर्ड में सबमिशन की समीक्षा करें, CSV/Stata में निर्यात करें, या Power BI / R से कनेक्ट करें |

---

## शुरू करने से पहले

आपको चाहिए:

- एक **Linux सर्वर** (या Linode, DigitalOcean, AWS या GCP पर क्लाउड अकाउंट)
- एक **डोमेन नाम** जो आपके सर्वर की ओर इंगित करता हो
- लगभग **10 मिनट**

Docker का पूर्व ज्ञान आवश्यक नहीं — तैनाती स्क्रिप्ट सब कुछ संभालती है।

---

## तैयार हैं?

**[अपना सर्वर तैनात करें →](self-hosting/quick-start)**"""
    },
    "hu": {
        "title": "Áttekintés",
        "description": "Mi az rtSurvey, hogyan működik és mire van szükség az indulás előtt.",
        "body": """Az rtSurvey egy saját szervereken futtatható platform, amellyel űrlapokat tervezhet, terepi adatokat gyűjthet és valós időben elemezheti az eredményeket. Saját szerverén futtatja — az adatai soha nem hagyják el az infrastruktúráját.

---

## Hogyan működik

| Lépés | Mit tesz |
|-------|---------|
| **1. Telepítés** | Indítson el egy szervert, és futtassa az rtSurvey-vermet egyetlen automatizált szkripttel |
| **2. Tervezés** | Hozzon létre űrlapokat XLSForm vagy a vizuális Form Builder segítségével |
| **3. Gyűjtés** | A terepi csapatok mobilalkalmazáson vagy böngészőn keresztül küldik be az adatokat — online vagy offline |
| **4. Elemzés** | Tekintse át a beküldéseket az irányítópulton, exportálja CSV/Stata formátumba, vagy csatlakozzon a Power BI / R-hez |

---

## Mielőtt elkezdi

Szüksége lesz:

- Egy **Linux szerverre** (vagy felhőfiókra Linode, DigitalOcean, AWS vagy GCP szolgáltatóknál)
- Egy **domainnevere**, amely a szerverére mutat
- Körülbelül **10 percre**

Nem szükséges Docker-ismeret — a telepítési szkript mindent elvégez.

---

## Készen áll?

**[Telepítse a szerverét →](self-hosting/quick-start)**"""
    },
    "id": {
        "title": "Ikhtisar",
        "description": "Apa itu rtSurvey, cara kerjanya, dan apa yang Anda butuhkan sebelum memulai.",
        "body": """rtSurvey adalah platform self-hosted untuk merancang formulir, mengumpulkan data di lapangan, dan menganalisis hasil secara real-time. Anda menjalankannya di server Anda sendiri — data Anda tidak pernah meninggalkan infrastruktur Anda.

---

## Cara kerjanya

| Langkah | Yang Anda lakukan |
|---------|------------------|
| **1. Deploy** | Jalankan server dan jalankan stack rtSurvey dengan satu skrip otomatis |
| **2. Rancang** | Buat formulir menggunakan XLSForm atau Form Builder visual |
| **3. Kumpulkan** | Tim lapangan mengirimkan data melalui aplikasi mobile atau browser — online maupun offline |
| **4. Analisis** | Tinjau kiriman di dasbor, ekspor ke CSV/Stata, atau hubungkan ke Power BI / R |

---

## Sebelum memulai

Anda membutuhkan:

- Sebuah **server Linux** (atau akun cloud di Linode, DigitalOcean, AWS, atau GCP)
- Sebuah **nama domain** yang mengarah ke server Anda
- Sekitar **10 menit**

Tidak perlu pengetahuan Docker sebelumnya — skrip deployment menangani segalanya.

---

## Siap?

**[Deploy server Anda →](self-hosting/quick-start)**"""
    },
    "it": {
        "title": "Panoramica",
        "description": "Cos'è rtSurvey, come funziona e cosa occorre prima di iniziare.",
        "body": """rtSurvey è una piattaforma self-hosted per progettare moduli, raccogliere dati sul campo e analizzare i risultati in tempo reale. La si esegue sul proprio server — i dati non lasciano mai la propria infrastruttura.

---

## Come funziona

| Passo | Cosa si fa |
|-------|-----------|
| **1. Distribuire** | Avviare un server ed eseguire lo stack rtSurvey con uno script automatizzato |
| **2. Progettare** | Creare moduli con XLSForm o il Form Builder visivo |
| **3. Raccogliere** | I team sul campo inviano dati tramite l'app mobile o il browser — online o offline |
| **4. Analizzare** | Esaminare le risposte nel pannello, esportare in CSV/Stata o connettersi a Power BI / R |

---

## Prima di iniziare

Occorre:

- Un **server Linux** (o un account cloud su Linode, DigitalOcean, AWS o GCP)
- Un **nome di dominio** puntato al proprio server
- Circa **10 minuti**

Non è richiesta alcuna conoscenza di Docker — lo script di distribuzione gestisce tutto.

---

## Pronti?

**[Distribuire il server →](self-hosting/quick-start)**"""
    },
    "ja": {
        "title": "概要",
        "description": "rtSurveyとは何か、どのように機能するか、開始前に必要なもの。",
        "body": """rtSurveyは、フォームの設計、フィールドでのデータ収集、リアルタイムでの結果分析を行うためのセルフホスト型プラットフォームです。自分のサーバーで実行するため、データがインフラ外に出ることはありません。

---

## 仕組み

| ステップ | 行うこと |
|---------|---------|
| **1. デプロイ** | サーバーを起動し、自動化スクリプトでrtSurveyスタックを実行する |
| **2. 設計** | XLSFormまたはビジュアルForm Builderでフォームを作成する |
| **3. 収集** | フィールドチームがモバイルアプリまたはブラウザでデータを送信する — オンラインまたはオフライン |
| **4. 分析** | ダッシュボードで提出データを確認し、CSV/Stataにエクスポートするか、Power BI / Rに接続する |

---

## 始める前に

必要なもの：

- **Linuxサーバー**（またはLinode、DigitalOcean、AWS、GCPのクラウドアカウント）
- サーバーに向けた**ドメイン名**
- 約**10分**

Dockerの事前知識は不要 — デプロイスクリプトがすべてを処理します。

---

## 準備はいいですか？

**[サーバーをデプロイする →](self-hosting/quick-start)**"""
    },
    "km": {
        "title": "ទិដ្ឋភាពទូទៅ",
        "description": "rtSurvey គឺជាអ្វី របៀបដំណើរការ និងអ្វីដែលអ្នកត្រូវការមុនពេលចាប់ផ្តើម។",
        "body": """rtSurvey គឺជាវេទិកា self-hosted សម្រាប់ការរចនាទម្រង់ ការប្រមូលទិន្នន័យនៅក្នុងវាល និងការវិភាគលទ្ធផលក្នុងពេលវេលាជាក់ស្តែង។ អ្នកដំណើរការវានៅលើម៉ាស៊ីនមេរបស់អ្នកផ្ទាល់ — ទិន្នន័យរបស់អ្នកមិនចាកចេញពីហេដ្ឋារចនាសម្ព័ន្ធរបស់អ្នកឡើយ។

---

## របៀបដំណើរការ

| ជំហាន | អ្វីដែលអ្នកធ្វើ |
|-------|---------------|
| **១. ដាក់ឱ្យប្រើប្រាស់** | ចាប់ផ្ដើមមា៉ស៊ីនមេ ហើយដំណើរការ rtSurvey stack ជាមួយស្គ្រីបស្វ័យប្រវត្តិ |
| **២. រចនា** | បង្កើតទម្រង់ដោយប្រើ XLSForm ឬ Form Builder ដែលមើលឃើញ |
| **៣.ប្រមូល** | ក្រុមការងារនៅវាលបញ្ជូនទិន្នន័យតាមមាតិការចល័ត ឬ browser — អនឡាញ ឬ ក្រៅបណ្ដាញ |
| **៤. វិភាគ** | ពិនិត្យការបញ្ជូននៅក្នុង dashboard នាំចេញទៅ CSV/Stata ឬភ្ជាប់ទៅ Power BI / R |

---

## មុនពេលអ្នកចាប់ផ្ដើម

អ្នកត្រូវការ៖

- **ម៉ាស៊ីនមេ Linux** (ឬគណនី cloud នៅ Linode, DigitalOcean, AWS ឬ GCP)
- **ឈ្មោះដែន** ដែលចង្អុលទៅម៉ាស៊ីនមេរបស់អ្នក
- ប្រហែល **១០ នាទី**

មិនចាំបាច់មានចំណេះដឹង Docker ជាមុន — ស្គ្រីបដាក់ឱ្យប្រើប្រាស់ដោះស្រាយអ្វីៗទាំងអស់។

---

## រួចរាល់ហើយឬ?

**[ដាក់ម៉ាស៊ីនមេរបស់អ្នកឱ្យប្រើប្រាស់ →](self-hosting/quick-start)**"""
    },
    "ko": {
        "title": "개요",
        "description": "rtSurvey가 무엇인지, 어떻게 작동하는지, 시작하기 전에 필요한 것.",
        "body": """rtSurvey는 양식 설계, 현장 데이터 수집, 실시간 결과 분석을 위한 자체 호스팅 플랫폼입니다. 자체 서버에서 실행하므로 데이터가 인프라 밖으로 나가지 않습니다.

---

## 작동 방식

| 단계 | 수행 작업 |
|------|---------|
| **1. 배포** | 서버를 시작하고 자동화 스크립트로 rtSurvey 스택을 실행합니다 |
| **2. 설계** | XLSForm 또는 시각적 Form Builder로 양식을 만듭니다 |
| **3. 수집** | 현장 팀이 모바일 앱이나 브라우저를 통해 데이터를 제출합니다 — 온라인 또는 오프라인 |
| **4. 분석** | 대시보드에서 제출 내용을 검토하고, CSV/Stata로 내보내거나 Power BI / R에 연결합니다 |

---

## 시작하기 전에

다음이 필요합니다:

- **Linux 서버** (또는 Linode, DigitalOcean, AWS, GCP의 클라우드 계정)
- 서버를 가리키는 **도메인 이름**
- 약 **10분**

Docker 사전 지식이 필요 없습니다 — 배포 스크립트가 모든 것을 처리합니다.

---

## 준비되셨나요?

**[서버 배포하기 →](self-hosting/quick-start)**"""
    },
    "lt": {
        "title": "Apžvalga",
        "description": "Kas yra rtSurvey, kaip tai veikia ir ko reikia prieš pradedant.",
        "body": """rtSurvey yra savarankiškai talpinama platforma formų kūrimui, lauko duomenų rinkimui ir rezultatų analizei realiuoju laiku. Ją leidžiate savo serveryje — jūsų duomenys niekada nepalieka jūsų infrastruktūros.

---

## Kaip tai veikia

| Žingsnis | Ką darote |
|---------|-----------|
| **1. Diegimas** | Paleiskite serverį ir vykdykite rtSurvey rinkinį naudodami automatizuotą scenarijų |
| **2. Kūrimas** | Kurkite formas naudodami XLSForm arba vizualinį Form Builder |
| **3. Rinkimas** | Lauko komandos pateikia duomenis per mobilią programėlę arba naršyklę — online arba offline |
| **4. Analizė** | Peržiūrėkite pateiktus duomenis informaciniame skydelyje, eksportuokite į CSV/Stata arba prijunkite prie Power BI / R |

---

## Prieš pradedant

Jums reikia:

- **Linux serverio** (arba debesijos paskyros Linode, DigitalOcean, AWS ar GCP)
- **Domeno vardo**, nukreipto į jūsų serverį
- Maždaug **10 minučių**

Nereikia išankstinių Docker žinių — diegimo scenarijus viską sutvarko.

---

## Pasiruošę?

**[Diekite savo serverį →](self-hosting/quick-start)**"""
    },
    "lv": {
        "title": "Pārskats",
        "description": "Kas ir rtSurvey, kā tas darbojas un kas nepieciešams pirms sākšanas.",
        "body": """rtSurvey ir pašmitināta platforma veidlapu projektēšanai, lauka datu vākšanai un rezultātu analīzei reāllaikā. Jūs to darbināt savā serverī — jūsu dati nekad nepamet jūsu infrastruktūru.

---

## Kā tas darbojas

| Solis | Ko jūs darāt |
|-------|-------------|
| **1. Izvietošana** | Startējiet serveri un palaidiet rtSurvey kopu ar automatizētu skriptu |
| **2. Projektēšana** | Veidojiet veidlapas ar XLSForm vai vizuālo Form Builder |
| **3. Vākšana** | Lauka komandas iesniedz datus, izmantojot mobilo lietotni vai pārlūku — tiešsaistē vai bezsaistē |
| **4. Analīze** | Pārskatiet iesniegumus informācijas panelī, eksportējiet uz CSV/Stata vai savienojiet ar Power BI / R |

---

## Pirms sākšanas

Jums nepieciešams:

- **Linux serveris** (vai mākoņpakalpojumu konts Linode, DigitalOcean, AWS vai GCP)
- **Domēna vārds**, kas norāda uz jūsu serveri
- Aptuveni **10 minūtes**

Iepriekšējas Docker zināšanas nav nepieciešamas — izvietošanas skripts visu nokārto.

---

## Gatavs?

**[Izvietojiet savu serveri →](self-hosting/quick-start)**"""
    },
    "nb": {
        "title": "Oversikt",
        "description": "Hva rtSurvey er, hvordan det fungerer og hva du trenger før du starter.",
        "body": """rtSurvey er en selvhostet plattform for å designe skjemaer, samle inn feltdata og analysere resultater i sanntid. Du kjører det på din egen server — dataene dine forlater aldri din infrastruktur.

---

## Slik fungerer det

| Trinn | Hva du gjør |
|-------|-------------|
| **1. Distribuer** | Start en server og kjør rtSurvey-stakken med ett automatisert skript |
| **2. Utform** | Lag skjemaer med XLSForm eller den visuelle Form Builder |
| **3. Samle inn** | Feltteam sender inn data via mobilappen eller nettleseren — online eller offline |
| **4. Analyser** | Se gjennom innleveringer i dashbordet, eksporter til CSV/Stata eller koble til Power BI / R |

---

## Før du begynner

Du trenger:

- En **Linux-server** (eller en skykonto hos Linode, DigitalOcean, AWS eller GCP)
- Et **domenenavn** som peker til serveren din
- Omtrent **10 minutter**

Ingen forkunnskaper om Docker kreves — distribusjonsskriptet tar seg av alt.

---

## Klar?

**[Distribuer serveren din →](self-hosting/quick-start)**"""
    },
    "nl": {
        "title": "Overzicht",
        "description": "Wat rtSurvey is, hoe het werkt en wat u nodig hebt voordat u begint.",
        "body": """rtSurvey is een zelf-gehoste platform voor het ontwerpen van formulieren, het verzamelen van veldgegevens en het analyseren van resultaten in realtime. U draait het op uw eigen server — uw gegevens verlaten nooit uw infrastructuur.

---

## Hoe het werkt

| Stap | Wat u doet |
|------|------------|
| **1. Implementeren** | Start een server en voer de rtSurvey-stack uit met een geautomatiseerd script |
| **2. Ontwerpen** | Maak formulieren met XLSForm of de visuele Form Builder |
| **3. Verzamelen** | Veldteams dienen gegevens in via de mobiele app of browser — online of offline |
| **4. Analyseren** | Bekijk inzendingen in het dashboard, exporteer naar CSV/Stata of koppel aan Power BI / R |

---

## Voordat u begint

U hebt nodig:

- Een **Linux-server** (of een cloudaccount bij Linode, DigitalOcean, AWS of GCP)
- Een **domeinnaam** die naar uw server wijst
- Ongeveer **10 minuten**

Geen voorkennis van Docker vereist — het implementatiescript regelt alles.

---

## Klaar?

**[Implementeer uw server →](self-hosting/quick-start)**"""
    },
    "pl": {
        "title": "Przegląd",
        "description": "Czym jest rtSurvey, jak działa i czego potrzebujesz przed rozpoczęciem.",
        "body": """rtSurvey to samodzielnie hostowana platforma do projektowania formularzy, zbierania danych w terenie i analizowania wyników w czasie rzeczywistym. Uruchamiasz ją na własnym serwerze — Twoje dane nigdy nie opuszczają Twojej infrastruktury.

---

## Jak to działa

| Krok | Co robisz |
|------|-----------|
| **1. Wdrożenie** | Uruchom serwer i uruchom stos rtSurvey jednym zautomatyzowanym skryptem |
| **2. Projektowanie** | Twórz formularze za pomocą XLSForm lub wizualnego Form Buildera |
| **3. Zbieranie** | Zespoły terenowe przesyłają dane przez aplikację mobilną lub przeglądarkę — online lub offline |
| **4. Analiza** | Przeglądaj przesłane dane w panelu, eksportuj do CSV/Stata lub połącz z Power BI / R |

---

## Przed rozpoczęciem

Potrzebujesz:

- **Serwera Linux** (lub konta w chmurze na Linode, DigitalOcean, AWS lub GCP)
- **Nazwy domeny** wskazującej na Twój serwer
- Około **10 minut**

Nie jest wymagana wcześniejsza wiedza o Docker — skrypt wdrożeniowy zajmuje się wszystkim.

---

## Gotowy?

**[Wdróż swój serwer →](self-hosting/quick-start)**"""
    },
    "pt": {
        "title": "Visão geral",
        "description": "O que é o rtSurvey, como funciona e o que precisa antes de começar.",
        "body": """rtSurvey é uma plataforma auto-hospedada para criar formulários, recolher dados no terreno e analisar resultados em tempo real. Executa-a no seu próprio servidor — os seus dados nunca saem da sua infraestrutura.

---

## Como funciona

| Etapa | O que faz |
|-------|-----------|
| **1. Implementar** | Inicie um servidor e execute a stack rtSurvey com um script automatizado |
| **2. Criar** | Crie formulários com XLSForm ou o Form Builder visual |
| **3. Recolher** | As equipas de terreno enviam dados pela app móvel ou browser — online ou offline |
| **4. Analisar** | Reveja as submissões no painel, exporte para CSV/Stata ou ligue ao Power BI / R |

---

## Antes de começar

Precisa de:

- Um **servidor Linux** (ou uma conta cloud no Linode, DigitalOcean, AWS ou GCP)
- Um **nome de domínio** apontado para o seu servidor
- Cerca de **10 minutos**

Não são necessários conhecimentos prévios de Docker — o script de implementação trata de tudo.

---

## Pronto?

**[Implemente o seu servidor →](self-hosting/quick-start)**"""
    },
    "pt-br": {
        "title": "Visão geral",
        "description": "O que é o rtSurvey, como funciona e o que você precisa antes de começar.",
        "body": """rtSurvey é uma plataforma auto-hospedada para criar formulários, coletar dados em campo e analisar resultados em tempo real. Você a executa no seu próprio servidor — os seus dados nunca saem da sua infraestrutura.

---

## Como funciona

| Etapa | O que você faz |
|-------|----------------|
| **1. Implantar** | Inicie um servidor e execute a stack rtSurvey com um script automatizado |
| **2. Criar** | Crie formulários usando XLSForm ou o Form Builder visual |
| **3. Coletar** | As equipes de campo enviam dados pelo app móvel ou navegador — online ou offline |
| **4. Analisar** | Revise os envios no painel, exporte para CSV/Stata ou conecte-se ao Power BI / R |

---

## Antes de começar

Você precisa de:

- Um **servidor Linux** (ou uma conta em nuvem no Linode, DigitalOcean, AWS ou GCP)
- Um **nome de domínio** apontando para o seu servidor
- Cerca de **10 minutos**

Nenhum conhecimento prévio de Docker necessário — o script de implantação cuida de tudo.

---

## Pronto?

**[Implante o seu servidor →](self-hosting/quick-start)**"""
    },
    "ru": {
        "title": "Обзор",
        "description": "Что такое rtSurvey, как это работает и что нужно перед началом работы.",
        "body": """rtSurvey — это самостоятельно размещаемая платформа для разработки форм, сбора данных в поле и анализа результатов в режиме реального времени. Вы запускаете её на собственном сервере — ваши данные никогда не покидают вашу инфраструктуру.

---

## Как это работает

| Шаг | Что вы делаете |
|-----|---------------|
| **1. Развёртывание** | Запустите сервер и разверните стек rtSurvey с помощью одного автоматизированного скрипта |
| **2. Проектирование** | Создавайте формы с помощью XLSForm или визуального Form Builder |
| **3. Сбор данных** | Полевые команды отправляют данные через мобильное приложение или браузер — онлайн или офлайн |
| **4. Анализ** | Просматривайте отправленные данные в панели управления, экспортируйте в CSV/Stata или подключайтесь к Power BI / R |

---

## Прежде чем начать

Вам понадобится:

- **Сервер Linux** (или облачный аккаунт на Linode, DigitalOcean, AWS или GCP)
- **Доменное имя**, указывающее на ваш сервер
- Около **10 минут**

Предварительные знания Docker не требуются — скрипт развёртывания сделает всё сам.

---

## Готовы?

**[Разверните ваш сервер →](self-hosting/quick-start)**"""
    },
    "sk": {
        "title": "Prehľad",
        "description": "Čo je rtSurvey, ako funguje a čo potrebujete pred začatím.",
        "body": """rtSurvey je samostatne hostovaná platforma na vytváranie formulárov, zber dát v teréne a analýzu výsledkov v reálnom čase. Prevádzkujete ju na vlastnom serveri — vaše dáta nikdy neopustia vašu infraštruktúru.

---

## Ako to funguje

| Krok | Čo robíte |
|------|-----------|
| **1. Nasadenie** | Spustite server a spustite stack rtSurvey jedným automatizovaným skriptom |
| **2. Návrh** | Vytvárajte formuláre pomocou XLSForm alebo vizuálneho Form Buildera |
| **3. Zber** | Terénne tímy odosielajú dáta cez mobilnú aplikáciu alebo prehliadač — online alebo offline |
| **4. Analýza** | Skontrolujte odoslané dáta v dashboarde, exportujte do CSV/Stata alebo pripojte k Power BI / R |

---

## Pred začatím

Potrebujete:

- **Linux server** (alebo cloudový účet u Linode, DigitalOcean, AWS alebo GCP)
- **Doménové meno** smerujúce na váš server
- Približne **10 minút**

Nevyžadujú sa predchádzajúce znalosti Dockeru — nasadzovací skript sa postará o všetko.

---

## Pripravení?

**[Nasaďte svoj server →](self-hosting/quick-start)**"""
    },
    "sq": {
        "title": "Pasqyrë",
        "description": "Çfarë është rtSurvey, si funksionon dhe çfarë ju nevojitet para fillimit.",
        "body": """rtSurvey është një platformë e vetë-strehuar për hartimin e formularëve, mbledhjen e të dhënave në terren dhe analizimin e rezultateve në kohë reale. E ekzekutoni në serverin tuaj — të dhënat tuaja nuk e lënë kurrë infrastrukturën tuaj.

---

## Si funksionon

| Hapi | Çfarë bëni |
|------|-----------|
| **1. Vendosja** | Nisni një server dhe ekzekutoni stek-un rtSurvey me një skript të automatizuar |
| **2. Hartimi** | Krijoni formularë duke përdorur XLSForm ose Form Builder-in vizual |
| **3. Mbledhja** | Ekipet në terren dërgojnë të dhëna nëpërmjet aplikacionit celular ose shfletuesit — online ose offline |
| **4. Analiza** | Rishikoni dërgesat në panel, eksportoni në CSV/Stata ose lidhuni me Power BI / R |

---

## Para se të filloni

Ju nevojitet:

- Një **server Linux** (ose llogari cloud në Linode, DigitalOcean, AWS ose GCP)
- Një **emër domeni** që tregon drejt serverit tuaj
- Rreth **10 minuta**

Nuk kërkohen njohuri paraprake të Docker — skripti i vendosjes menaxhon gjithçka.

---

## Gati?

**[Vendosni serverin tuaj →](self-hosting/quick-start)**"""
    },
    "sr": {
        "title": "Преглед",
        "description": "Шта је rtSurvey, како функционише и шта вам је потребно пре почетка.",
        "body": """rtSurvey је самостално хостована платформа за пројектовање образаца, прикупљање теренских података и анализу резултата у реалном времену. Покрећете га на сопственом серверу — ваши подаци никада не напуштају вашу инфраструктуру.

---

## Kako функционише

| Корак | Шта радите |
|-------|-----------|
| **1. Постављање** | Покрените сервер и покрените rtSurvey стек једном аутоматизованом скриптом |
| **2. Пројектовање** | Креирајте обрасце помоћу XLSForm или визуелног Form Builder-а |
| **3. Прикупљање** | Теренски тимови шаљу податке путем мобилне апликације или претраживача — онлајн или офлајн |
| **4. Анализа** | Прегледајте поднете podatke на контролној табли, извезите у CSV/Stata или се povežite са Power BI / R |

---

## Пре почетка

Потребно вам је:

- **Linux сервер** (или налог у облаку на Linode, DigitalOcean, AWS или GCP)
- **Назив домена** усмерен на ваш сервер
- Oko **10 минута**

Није потребно претходно познавање Docker-а — скрипта за постављање се стара о свему.

---

## Спремни?

**[Поставите свој сервер →](self-hosting/quick-start)**"""
    },
    "sv": {
        "title": "Översikt",
        "description": "Vad rtSurvey är, hur det fungerar och vad du behöver innan du börjar.",
        "body": """rtSurvey är en självhostad plattform för att utforma formulär, samla in fältdata och analysera resultat i realtid. Du kör det på din egen server — dina data lämnar aldrig din infrastruktur.

---

## Hur det fungerar

| Steg | Vad du gör |
|------|------------|
| **1. Driftsätt** | Starta en server och kör rtSurvey-stacken med ett automatiserat skript |
| **2. Utforma** | Skapa formulär med XLSForm eller den visuella Form Builder |
| **3. Samla in** | Fältteam skickar in data via mobilappen eller webbläsaren — online eller offline |
| **4. Analysera** | Granska inlämningar i instrumentpanelen, exportera till CSV/Stata eller anslut till Power BI / R |

---

## Innan du börjar

Du behöver:

- En **Linux-server** (eller ett molnkonto hos Linode, DigitalOcean, AWS eller GCP)
- Ett **domännamn** som pekar på din server
- Ungefär **10 minuter**

Inga förkunskaper om Docker krävs — driftsättningsskriptet hanterar allt.

---

## Redo?

**[Driftsätt din server →](self-hosting/quick-start)**"""
    },
    "te": {
        "title": "అవలోకనం",
        "description": "rtSurvey ఏమిటి, ఇది ఎలా పనిచేస్తుంది మరియు మీరు ప్రారంభించే ముందు మీకు ఏమి కావాలి.",
        "body": """rtSurvey అనేది ఫారమ్‌లను రూపొందించడానికి, క్షేత్ర డేటాను సేకరించడానికి మరియు ఫలితాలను రియల్-టైమ్‌లో విశ్లేషించడానికి ఒక సెల్ఫ్-హోస్టెడ్ ప్లాట్‌ఫారమ్. మీరు దీన్ని మీ స్వంత సర్వర్‌లో నడుపుతారు — మీ డేటా ఎప్పుడూ మీ మౌలికసదుపాయాలను వదలదు.

---

## ఇది ఎలా పనిచేస్తుంది

| దశ | మీరు చేసేది |
|----|------------|
| **1. విన్యాసం** | ఒక స్వయంచాలిత స్క్రిప్ట్‌తో సర్వర్‌ను ప్రారంభించి rtSurvey స్టాక్‌ను అమలు చేయండి |
| **2. రూపకల్పన** | XLSForm లేదా విజువల్ Form Builder ఉపయోగించి ఫారమ్‌లను రూపొందించండి |
| **3. సేకరణ** | క్షేత్ర బృందాలు మొబైల్ యాప్ లేదా బ్రౌజర్ ద్వారా డేటాను సమర్పిస్తాయి — ఆన్‌లైన్ లేదా ఆఫ్‌లైన్ |
| **4. విశ్లేషణ** | డాష్‌బోర్డ్‌లో సమర్పణలను సమీక్షించండి, CSV/Stataకి ఎగుమతి చేయండి లేదా Power BI / Rకి కనెక్ట్ చేయండి |

---

## మీరు ప్రారంభించే ముందు

మీకు కావాలి:

- ఒక **Linux సర్వర్** (లేదా Linode, DigitalOcean, AWS లేదా GCPలో క్లౌడ్ అకౌంట్)
- మీ సర్వర్‌ను చూపే **డొమైన్ పేరు**
- సుమారు **10 నిమిషాలు**

Docker గురించి ముందస్తు జ్ఞానం అవసరం లేదు — విన్యాస స్క్రిప్ట్ అన్నింటినీ నిర్వహిస్తుంది.

---

## సిద్ధంగా ఉన్నారా?

**[మీ సర్వర్‌ను విన్యసించండి →](self-hosting/quick-start)**"""
    },
    "th": {
        "title": "ภาพรวม",
        "description": "rtSurvey คืออะไร ทำงานอย่างไร และสิ่งที่คุณต้องการก่อนเริ่มต้น",
        "body": """rtSurvey คือแพลตฟอร์มโฮสต์เองสำหรับออกแบบแบบฟอร์ม รวบรวมข้อมูลภาคสนาม และวิเคราะห์ผลลัพธ์แบบเรียลไทม์ คุณเรียกใช้งานบนเซิร์ฟเวอร์ของคุณเอง — ข้อมูลของคุณไม่เคยออกจากโครงสร้างพื้นฐานของคุณ

---

## วิธีการทำงาน

| ขั้นตอน | สิ่งที่คุณทำ |
|---------|------------|
| **1. ติดตั้ง** | เริ่มต้นเซิร์ฟเวอร์และรัน rtSurvey stack ด้วยสคริปต์อัตโนมัติ |
| **2. ออกแบบ** | สร้างแบบฟอร์มโดยใช้ XLSForm หรือ Form Builder แบบภาพ |
| **3. รวบรวม** | ทีมภาคสนามส่งข้อมูลผ่านแอปมือถือหรือเบราว์เซอร์ — ออนไลน์หรือออฟไลน์ |
| **4. วิเคราะห์** | ตรวจสอบการส่งในแดชบอร์ด ส่งออกไปยัง CSV/Stata หรือเชื่อมต่อกับ Power BI / R |

---

## ก่อนเริ่มต้น

คุณต้องการ:

- **เซิร์ฟเวอร์ Linux** (หรือบัญชีคลาวด์บน Linode, DigitalOcean, AWS หรือ GCP)
- **ชื่อโดเมน** ที่ชี้ไปยังเซิร์ฟเวอร์ของคุณ
- ประมาณ **10 นาที**

ไม่จำเป็นต้องมีความรู้ Docker ล่วงหน้า — สคริปต์การติดตั้งจัดการทุกอย่าง

---

## พร้อมหรือยัง?

**[ติดตั้งเซิร์ฟเวอร์ของคุณ →](self-hosting/quick-start)**"""
    },
    "tr": {
        "title": "Genel Bakış",
        "description": "rtSurvey nedir, nasıl çalışır ve başlamadan önce neye ihtiyacınız var.",
        "body": """rtSurvey, form tasarlamak, sahada veri toplamak ve sonuçları gerçek zamanlı olarak analiz etmek için kendi kendine barındırılan bir platformdur. Kendi sunucunuzda çalıştırırsınız — verileriniz hiçbir zaman altyapınızı terk etmez.

---

## Nasıl çalışır

| Adım | Ne yaparsınız |
|------|--------------|
| **1. Dağıtım** | Bir sunucu başlatın ve otomatik bir komut dosyasıyla rtSurvey yığınını çalıştırın |
| **2. Tasarım** | XLSForm veya görsel Form Builder kullanarak formlar oluşturun |
| **3. Toplama** | Saha ekipleri mobil uygulama veya tarayıcı aracılığıyla veri gönderir — çevrimiçi veya çevrimdışı |
| **4. Analiz** | Panelde gönderileri inceleyin, CSV/Stata'ya aktarın veya Power BI / R'ye bağlanın |

---

## Başlamadan önce

İhtiyacınız olan:

- Bir **Linux sunucusu** (veya Linode, DigitalOcean, AWS veya GCP'de bulut hesabı)
- Sunucunuza işaret eden bir **alan adı**
- Yaklaşık **10 dakika**

Önceden Docker bilgisi gerekmez — dağıtım betiği her şeyi halleder.

---

## Hazır mısınız?

**[Sunucunuzu dağıtın →](self-hosting/quick-start)**"""
    },
    "uk": {
        "title": "Огляд",
        "description": "Що таке rtSurvey, як це працює і що потрібно перед початком роботи.",
        "body": """rtSurvey — це самостійно розміщувана платформа для розробки форм, збору польових даних та аналізу результатів у режимі реального часу. Ви запускаєте її на власному сервері — ваші дані ніколи не залишають вашу інфраструктуру.

---

## Як це працює

| Крок | Що ви робите |
|------|-------------|
| **1. Розгортання** | Запустіть сервер і розгорніть стек rtSurvey одним автоматизованим скриптом |
| **2. Проектування** | Створюйте форми за допомогою XLSForm або візуального Form Builder |
| **3. Збір даних** | Польові команди надсилають дані через мобільний додаток або браузер — онлайн або офлайн |
| **4. Аналіз** | Переглядайте надіслані дані на панелі керування, експортуйте в CSV/Stata або підключайтеся до Power BI / R |

---

## Перед початком

Вам знадобиться:

- **Сервер Linux** (або хмарний акаунт на Linode, DigitalOcean, AWS або GCP)
- **Доменне ім'я**, що вказує на ваш сервер
- Близько **10 хвилин**

Попередні знання Docker не потрібні — скрипт розгортання зробить усе сам.

---

## Готові?

**[Розгорніть ваш сервер →](self-hosting/quick-start)**"""
    },
    "vi": {
        "title": "Tổng quan",
        "description": "rtSurvey là gì, cách thức hoạt động và những gì bạn cần trước khi bắt đầu.",
        "body": """rtSurvey là nền tảng tự lưu trữ để thiết kế biểu mẫu, thu thập dữ liệu thực địa và phân tích kết quả theo thời gian thực. Bạn chạy nó trên máy chủ của riêng mình — dữ liệu của bạn không bao giờ rời khỏi cơ sở hạ tầng của bạn.

---

## Cách thức hoạt động

| Bước | Bạn làm gì |
|------|------------|
| **1. Triển khai** | Khởi động máy chủ và chạy rtSurvey bằng một script tự động |
| **2. Thiết kế** | Xây dựng biểu mẫu bằng XLSForm hoặc Form Builder trực quan |
| **3. Thu thập** | Nhóm thực địa gửi dữ liệu qua ứng dụng di động hoặc trình duyệt — trực tuyến hoặc ngoại tuyến |
| **4. Phân tích** | Xem xét dữ liệu trong bảng điều khiển, xuất sang CSV/Stata, hoặc kết nối với Power BI / R |

---

## Trước khi bắt đầu

Bạn cần:

- Một **máy chủ Linux** (hoặc tài khoản đám mây trên Linode, DigitalOcean, AWS hoặc GCP)
- Một **tên miền** trỏ vào máy chủ của bạn
- Khoảng **10 phút**

Không cần kiến thức Docker trước — script triển khai xử lý tất cả mọi thứ.

---

## Sẵn sàng chưa?

**[Triển khai máy chủ của bạn →](self-hosting/quick-start)**"""
    },
    "zh-hans": {
        "title": "概述",
        "description": "rtSurvey 是什么、如何运作以及开始前需要准备什么。",
        "body": """rtSurvey 是一个自托管平台，用于设计表单、在现场收集数据并实时分析结果。您在自己的服务器上运行它——您的数据永远不会离开您的基础设施。

---

## 工作原理

| 步骤 | 您要做的事 |
|------|-----------|
| **1. 部署** | 启动服务器并使用一个自动化脚本运行 rtSurvey 堆栈 |
| **2. 设计** | 使用 XLSForm 或可视化 Form Builder 构建表单 |
| **3. 收集** | 现场团队通过移动应用或浏览器提交数据——在线或离线 |
| **4. 分析** | 在仪表盘中查看提交内容，导出为 CSV/Stata，或连接到 Power BI / R |

---

## 开始之前

您需要：

- 一台 **Linux 服务器**（或 Linode、DigitalOcean、AWS 或 GCP 上的云账户）
- 一个指向您服务器的**域名**
- 大约 **10 分钟**

无需 Docker 基础知识——部署脚本会处理一切。

---

## 准备好了吗？

**[部署您的服务器 →](self-hosting/quick-start)**"""
    },
    "zh-hant": {
        "title": "概述",
        "description": "rtSurvey 是什麼、如何運作以及開始前需要準備什麼。",
        "body": """rtSurvey 是一個自託管平台，用於設計表單、在現場收集數據並即時分析結果。您在自己的伺服器上運行它——您的數據永遠不會離開您的基礎設施。

---

## 運作方式

| 步驟 | 您要做的事 |
|------|-----------|
| **1. 部署** | 啟動伺服器並使用一個自動化腳本運行 rtSurvey 堆疊 |
| **2. 設計** | 使用 XLSForm 或視覺化 Form Builder 建立表單 |
| **3. 收集** | 現場團隊透過行動應用程式或瀏覽器提交數據——線上或離線 |
| **4. 分析** | 在儀表板中查看提交內容，匯出為 CSV/Stata，或連接到 Power BI / R |

---

## 開始之前

您需要：

- 一台 **Linux 伺服器**（或 Linode、DigitalOcean、AWS 或 GCP 上的雲端帳戶）
- 一個指向您伺服器的**網域名稱**
- 大約 **10 分鐘**

無需 Docker 基礎知識——部署腳本會處理一切。

---

## 準備好了嗎？

**[部署您的伺服器 →](self-hosting/quick-start)**"""
    },
}

CONTENT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "content")

count = 0
for lang, t in TRANSLATIONS.items():
    path = os.path.join(CONTENT_DIR, lang, "docs/getting-started/overview.md")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    content = FRONT.format(title=t["title"], description=t["description"]) + t["body"] + "\n"
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    count += 1
    print(f"  wrote {lang}")

print(f"\nDone — {count} files written")

# ── quick-start.md ──────────────────────────────────────────────────────────

QS_FRONT = """---
weight: 1
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
title: "{title}"
icon: "play_circle"
toc: true
description: "{description}"
---

"""

QS = {
    "ar": ("البدء السريع", "انشر rtCloud على خادمك الخاص في دقائق باستخدام سكريبت سحابي تلقائي.", """يساعدك هذا الدليل على تشغيل rtCloud على خادمك الخاص. تتولى السكريبتات التلقائية كل شيء — Docker وSSL وقاعدة البيانات والجدار الناري — في تشغيل واحد.

## المتطلبات

### الخادم

| المورد | الحد الأدنى | الموصى به |
|--------|------------|----------|
| RAM | 2 GB | 4 GB (مطلوب عند استخدام Keycloak SSO) |
| القرص | 25 GB | 40 GB |
| المعالج | 1 vCPU | 2 vCPUs |
| نظام التشغيل | Ubuntu 22.04 LTS | Ubuntu 22.04 LTS |

### النطاق

تحتاج إلى اسم نطاق مع **سجل A يشير إلى عنوان IP الخادم** قبل تشغيل السكريبت. يتطلب Let's Encrypt حل DNS لإصدار شهادة SSL.

---

## اختر مزود الخدمة السحابية

اختر مزودك أدناه. يحتوي كل منهم على سكريبت تلقائي يعمل عند الإقلاع الأول ويكمل الإعداد في **5–10 دقائق**.

| المزود | الدليل |
|--------|--------|
| Linode (Akamai) | [النشر على Linode](../cloud-deployment/linode) — الأسهل، إعداد قائم على النموذج عبر StackScript |
| DigitalOcean | [النشر على DigitalOcean](../cloud-deployment/digitalocean) |
| AWS EC2 | [النشر على AWS](../cloud-deployment/aws) |
| Google Cloud | [النشر على GCP](../cloud-deployment/gcp) |

> **الموصى به لمعظم المستخدمين:** ابدأ بـ Linode — يوفر StackScript واجهة مستخدم قائمة على النموذج لذا لا يوجد شيء لتحريره يدوياً."""),

    "bg": ("Бързо начало", "Разгърнете rtCloud на вашия собствен сървър за минути с автоматизиран облачен скрипт.", """Това ръководство ще ви помогне да стартирате rtCloud на собствения ви сървър. Автоматизираните скриптове се грижат за всичко — Docker, SSL, база данни, защитна стена — само с едно изпълнение.

## Изисквания

### Сървър

| Ресурс | Минимум | Препоръчително |
|--------|---------|---------------|
| RAM | 2 GB | 4 GB (задължително при Keycloak SSO) |
| Диск | 25 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPUs |
| ОС | Ubuntu 22.04 LTS | Ubuntu 22.04 LTS |

### Домейн

Необходимо е доменно име с **A запис, сочещ към IP адреса на сървъра** преди стартиране на скрипта. Let's Encrypt изисква DNS резолюция за издаване на SSL сертификат.

---

## Изберете доставчик на облак

Изберете вашия доставчик по-долу. Всеки разполага с автоматизиран скрипт, който се изпълнява при първото зареждане и завършва настройката за **5–10 минути**.

| Доставчик | Ръководство |
|-----------|------------|
| Linode (Akamai) | [Разгръщане на Linode](../cloud-deployment/linode) — най-лесно, базирана на форма настройка чрез StackScript |
| DigitalOcean | [Разгръщане на DigitalOcean](../cloud-deployment/digitalocean) |
| AWS EC2 | [Разгръщане на AWS](../cloud-deployment/aws) |
| Google Cloud | [Разгръщане на GCP](../cloud-deployment/gcp) |

> **Препоръчително за повечето потребители:** Започнете с Linode — StackScript предоставя базиран на форма UI, така че няма какво да редактирате ръчно."""),

    "cs": ("Rychlý start", "Nasaďte rtCloud na vlastní server během minut pomocí automatizovaného cloudového skriptu.", """Tento průvodce vám pomůže spustit rtCloud na vlastním serveru. Automatizované skripty zajistí vše — Docker, SSL, databázi, firewall — jedním spuštěním.

## Požadavky

### Server

| Prostředek | Minimum | Doporučeno |
|-----------|---------|-----------|
| RAM | 2 GB | 4 GB (nutné při použití Keycloak SSO) |
| Disk | 25 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPUs |
| OS | Ubuntu 22.04 LTS | Ubuntu 22.04 LTS |

### Doména

Před spuštěním skriptu potřebujete doménové jméno s **A záznamem ukazujícím na IP adresu serveru**. Let's Encrypt vyžaduje DNS rozlišení pro vydání SSL certifikátu.

---

## Vyberte poskytovatele cloudu

Vyberte svého poskytovatele níže. Každý má automatizovaný skript, který se spustí při prvním startu a dokončí nastavení za **5–10 minut**.

| Poskytovatel | Průvodce |
|-------------|---------|
| Linode (Akamai) | [Nasazení na Linode](../cloud-deployment/linode) — nejjednodušší, formulářové nastavení přes StackScript |
| DigitalOcean | [Nasazení na DigitalOcean](../cloud-deployment/digitalocean) |
| AWS EC2 | [Nasazení na AWS](../cloud-deployment/aws) |
| Google Cloud | [Nasazení na GCP](../cloud-deployment/gcp) |

> **Doporučeno pro většinu uživatelů:** Začněte s Linode — StackScript poskytuje formulářové UI, takže není třeba nic ručně upravovat."""),

    "da": ("Hurtig start", "Implementér rtCloud på din egen server på få minutter med et automatiseret cloudscript.", """Denne guide hjælper dig med at få rtCloud kørende på din egen server. De automatiserede scripts tager sig af alt — Docker, SSL, database, firewall — i én kørsel.

## Krav

### Server

| Ressource | Minimum | Anbefalet |
|-----------|---------|----------|
| RAM | 2 GB | 4 GB (kræves ved brug af Keycloak SSO) |
| Disk | 25 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPUs |
| OS | Ubuntu 22.04 LTS | Ubuntu 22.04 LTS |

### Domæne

Du skal bruge et domænenavn med en **A-post der peger på serverens IP** inden scriptet køres. Let's Encrypt kræver DNS-opløsning for at udstede SSL-certifikat.

---

## Vælg din cloudleverandør

Vælg din leverandør nedenfor. Hver har et automatiseret script der kører ved første opstart og fuldfører opsætningen på **5–10 minutter**.

| Leverandør | Guide |
|-----------|-------|
| Linode (Akamai) | [Implementér på Linode](../cloud-deployment/linode) — nemmest, formularbaseret opsætning via StackScript |
| DigitalOcean | [Implementér på DigitalOcean](../cloud-deployment/digitalocean) |
| AWS EC2 | [Implementér på AWS](../cloud-deployment/aws) |
| Google Cloud | [Implementér på GCP](../cloud-deployment/gcp) |

> **Anbefalet for de fleste:** Start med Linode — StackScript giver en formularbaseret brugergrænseflade så der ikke er noget at redigere manuelt."""),

    "de": ("Schnellstart", "Stellen Sie rtCloud in Minuten auf Ihrem eigenen Server mit einem automatisierten Cloud-Skript bereit.", """Diese Anleitung hilft Ihnen, rtCloud auf Ihrem eigenen Server zum Laufen zu bringen. Die automatisierten Skripte erledigen alles — Docker, SSL, Datenbank, Firewall — in einem einzigen Durchlauf.

## Anforderungen

### Server

| Ressource | Minimum | Empfohlen |
|-----------|---------|----------|
| RAM | 2 GB | 4 GB (erforderlich bei Keycloak SSO) |
| Festplatte | 25 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPUs |
| Betriebssystem | Ubuntu 22.04 LTS | Ubuntu 22.04 LTS |

### Domain

Sie benötigen einen Domainnamen mit einem **A-Eintrag, der auf die IP-Adresse des Servers zeigt**, bevor Sie das Skript ausführen. Let's Encrypt erfordert DNS-Auflösung für die SSL-Zertifikatsausstellung.

---

## Wählen Sie Ihren Cloud-Anbieter

Wählen Sie Ihren Anbieter unten. Jeder hat ein automatisiertes Skript, das beim ersten Start ausgeführt wird und die Einrichtung in **5–10 Minuten** abschließt.

| Anbieter | Anleitung |
|----------|----------|
| Linode (Akamai) | [Bereitstellen auf Linode](../cloud-deployment/linode) — am einfachsten, formularbasierte Einrichtung via StackScript |
| DigitalOcean | [Bereitstellen auf DigitalOcean](../cloud-deployment/digitalocean) |
| AWS EC2 | [Bereitstellen auf AWS](../cloud-deployment/aws) |
| Google Cloud | [Bereitstellen auf GCP](../cloud-deployment/gcp) |

> **Empfohlen für die meisten Nutzer:** Beginnen Sie mit Linode — der StackScript bietet eine formularbasierte Benutzeroberfläche, sodass nichts manuell bearbeitet werden muss."""),

    "el": ("Γρήγορη εκκίνηση", "Αναπτύξτε το rtCloud στον δικό σας διακομιστή σε λίγα λεπτά με ένα αυτοματοποιημένο cloud script.", """Αυτός ο οδηγός σάς βοηθά να εκτελέσετε το rtCloud στον δικό σας διακομιστή. Τα αυτοματοποιημένα scripts φροντίζουν για όλα — Docker, SSL, βάση δεδομένων, τείχος προστασίας — σε μία εκτέλεση.

## Απαιτήσεις

### Διακομιστής

| Πόρος | Ελάχιστο | Συνιστώμενο |
|-------|---------|------------|
| RAM | 2 GB | 4 GB (απαιτείται με Keycloak SSO) |
| Δίσκος | 25 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPUs |
| ΛΣ | Ubuntu 22.04 LTS | Ubuntu 22.04 LTS |

### Τομέας

Χρειάζεστε ένα όνομα τομέα με **εγγραφή A που δείχνει στη διεύθυνση IP του διακομιστή** πριν εκτελέσετε το script. Το Let's Encrypt απαιτεί επίλυση DNS για την έκδοση πιστοποιητικού SSL.

---

## Επιλέξτε τον πάροχο cloud

Επιλέξτε τον πάροχό σας παρακάτω. Ο καθένας διαθέτει αυτοματοποιημένο script που εκτελείται κατά την πρώτη εκκίνηση και ολοκληρώνει την εγκατάσταση σε **5–10 λεπτά**.

| Πάροχος | Οδηγός |
|---------|--------|
| Linode (Akamai) | [Ανάπτυξη σε Linode](../cloud-deployment/linode) — ευκολότερο, ρύθμιση με φόρμα μέσω StackScript |
| DigitalOcean | [Ανάπτυξη σε DigitalOcean](../cloud-deployment/digitalocean) |
| AWS EC2 | [Ανάπτυξη σε AWS](../cloud-deployment/aws) |
| Google Cloud | [Ανάπτυξη σε GCP](../cloud-deployment/gcp) |

> **Συνιστάται για τους περισσότερους χρήστες:** Ξεκινήστε με Linode — το StackScript παρέχει UI βάσει φόρμας, οπότε δεν χρειάζεται χειροκίνητη επεξεργασία."""),

    "es": ("Inicio rápido", "Despliegue rtCloud en su propio servidor en minutos con un script de nube automatizado.", """Esta guía le ayuda a poner en marcha rtCloud en su propio servidor. Los scripts automatizados se encargan de todo — Docker, SSL, base de datos, firewall — en una sola ejecución.

## Requisitos

### Servidor

| Recurso | Mínimo | Recomendado |
|---------|--------|------------|
| RAM | 2 GB | 4 GB (necesario con Keycloak SSO) |
| Disco | 25 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPUs |
| SO | Ubuntu 22.04 LTS | Ubuntu 22.04 LTS |

### Dominio

Necesita un nombre de dominio con un **registro A apuntando a la IP del servidor** antes de ejecutar el script. Let's Encrypt requiere resolución DNS para emitir el certificado SSL.

---

## Elija su proveedor de nube

Seleccione su proveedor a continuación. Cada uno tiene un script automatizado que se ejecuta en el primer arranque y completa la configuración en **5–10 minutos**.

| Proveedor | Guía |
|-----------|------|
| Linode (Akamai) | [Desplegar en Linode](../cloud-deployment/linode) — más fácil, configuración basada en formulario via StackScript |
| DigitalOcean | [Desplegar en DigitalOcean](../cloud-deployment/digitalocean) |
| AWS EC2 | [Desplegar en AWS](../cloud-deployment/aws) |
| Google Cloud | [Desplegar en GCP](../cloud-deployment/gcp) |

> **Recomendado para la mayoría:** Comience con Linode — el StackScript proporciona una interfaz basada en formulario para que no haya nada que editar manualmente."""),

    "fi": ("Pika-aloitus", "Ota rtCloud käyttöön omalla palvelimellasi muutamassa minuutissa automatisoidulla pilviskripting.", """Tämä opas auttaa sinua saamaan rtCloud käyntiin omalla palvelimellasi. Automatisoidut skriptit hoitavat kaiken — Docker, SSL, tietokanta, palomuuri — yhdellä ajolla.

## Vaatimukset

### Palvelin

| Resurssi | Minimi | Suositeltu |
|---------|--------|-----------|
| RAM | 2 GB | 4 GB (vaaditaan Keycloak SSO:n kanssa) |
| Levy | 25 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPUs |
| Käyttöjärjestelmä | Ubuntu 22.04 LTS | Ubuntu 22.04 LTS |

### Verkkotunnus

Tarvitset verkkotunnuksen, jossa on **A-tietue, joka osoittaa palvelimen IP-osoitteeseen**, ennen skriptin suorittamista. Let's Encrypt vaatii DNS-resoluution SSL-sertifikaatin myöntämiseen.

---

## Valitse pilvipalveluntarjoajasi

Valitse palveluntarjoajasi alta. Kullakin on automatisoitu skripti, joka suoritetaan ensimmäisellä käynnistyksellä ja viimeistelee asennuksen **5–10 minuutissa**.

| Palveluntarjoaja | Opas |
|-----------------|------|
| Linode (Akamai) | [Ota käyttöön Linodessa](../cloud-deployment/linode) — helpoin, lomakepohjainen asennus StackScriptin kautta |
| DigitalOcean | [Ota käyttöön DigitalOceanissa](../cloud-deployment/digitalocean) |
| AWS EC2 | [Ota käyttöön AWS:ssä](../cloud-deployment/aws) |
| Google Cloud | [Ota käyttöön GCP:ssä](../cloud-deployment/gcp) |

> **Suositeltu useimmille:** Aloita Linodesta — StackScript tarjoaa lomakepohjaisen käyttöliittymän, joten mitään ei tarvitse muokata manuaalisesti."""),

    "fr": ("Démarrage rapide", "Déployez rtCloud sur votre propre serveur en quelques minutes avec un script cloud automatisé.", """Ce guide vous aide à faire fonctionner rtCloud sur votre propre serveur. Les scripts automatisés s'occupent de tout — Docker, SSL, base de données, pare-feu — en une seule exécution.

## Prérequis

### Serveur

| Ressource | Minimum | Recommandé |
|-----------|---------|-----------|
| RAM | 2 Go | 4 Go (requis avec Keycloak SSO) |
| Disque | 25 Go | 40 Go |
| CPU | 1 vCPU | 2 vCPUs |
| OS | Ubuntu 22.04 LTS | Ubuntu 22.04 LTS |

### Domaine

Vous avez besoin d'un nom de domaine avec un **enregistrement A pointant vers l'IP du serveur** avant d'exécuter le script. Let's Encrypt nécessite une résolution DNS pour émettre le certificat SSL.

---

## Choisissez votre fournisseur cloud

Sélectionnez votre fournisseur ci-dessous. Chacun dispose d'un script automatisé qui s'exécute au premier démarrage et finalise la configuration en **5–10 minutes**.

| Fournisseur | Guide |
|------------|-------|
| Linode (Akamai) | [Déployer sur Linode](../cloud-deployment/linode) — le plus simple, configuration par formulaire via StackScript |
| DigitalOcean | [Déployer sur DigitalOcean](../cloud-deployment/digitalocean) |
| AWS EC2 | [Déployer sur AWS](../cloud-deployment/aws) |
| Google Cloud | [Déployer sur GCP](../cloud-deployment/gcp) |

> **Recommandé pour la plupart des utilisateurs :** Commencez par Linode — le StackScript offre une interface basée sur un formulaire, donc rien à modifier manuellement."""),

    "hi": ("त्वरित शुरुआत", "स्वचालित क्लाउड स्क्रिप्ट के साथ मिनटों में अपने सर्वर पर rtCloud तैनात करें।", """यह गाइड आपको अपने सर्वर पर rtCloud चलाने में मदद करती है। स्वचालित स्क्रिप्ट सब कुछ संभालती हैं — Docker, SSL, डेटाबेस, फ़ायरवॉल — एक ही रन में।

## आवश्यकताएं

### सर्वर

| संसाधन | न्यूनतम | अनुशंसित |
|--------|--------|---------|
| RAM | 2 GB | 4 GB (Keycloak SSO के साथ आवश्यक) |
| डिस्क | 25 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPUs |
| OS | Ubuntu 22.04 LTS | Ubuntu 22.04 LTS |

### डोमेन

स्क्रिप्ट चलाने से पहले आपको **सर्वर के IP की ओर इंगित A रिकॉर्ड** के साथ एक डोमेन नाम चाहिए। SSL प्रमाणपत्र जारी करने के लिए Let's Encrypt को DNS रिज़ॉल्यूशन की आवश्यकता होती है।

---

## अपना क्लाउड प्रदाता चुनें

नीचे अपना प्रदाता चुनें। प्रत्येक के पास एक स्वचालित स्क्रिप्ट है जो पहले बूट पर चलती है और **5–10 मिनट** में सेटअप पूरा करती है।

| प्रदाता | गाइड |
|--------|------|
| Linode (Akamai) | [Linode पर तैनात करें](../cloud-deployment/linode) — सबसे आसान, StackScript के माध्यम से फॉर्म-आधारित सेटअप |
| DigitalOcean | [DigitalOcean पर तैनात करें](../cloud-deployment/digitalocean) |
| AWS EC2 | [AWS पर तैनात करें](../cloud-deployment/aws) |
| Google Cloud | [GCP पर तैनात करें](../cloud-deployment/gcp) |

> **अधिकांश उपयोगकर्ताओं के लिए अनुशंसित:** Linode से शुरू करें — StackScript फॉर्म-आधारित UI प्रदान करता है इसलिए कुछ भी मैन्युअल रूप से संपादित करने की आवश्यकता नहीं है।"""),

    "hu": ("Gyors kezdés", "Telepítse az rtCloud-ot saját szerverére percek alatt automatizált felhő-szkripttel.", """Ez az útmutató segít az rtCloud saját szerveren való elindításában. Az automatizált szkriptek mindent elvégeznek — Docker, SSL, adatbázis, tűzfal — egyetlen futtatással.

## Követelmények

### Szerver

| Erőforrás | Minimum | Ajánlott |
|-----------|---------|---------|
| RAM | 2 GB | 4 GB (szükséges Keycloak SSO esetén) |
| Lemez | 25 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPUs |
| OS | Ubuntu 22.04 LTS | Ubuntu 22.04 LTS |

### Domain

A szkript futtatása előtt szükség van egy domainnevre, amelynek **A rekordja a szerver IP-jére mutat**. A Let's Encrypt DNS-feloldást igényel az SSL-tanúsítvány kiállításához.

---

## Válasszon felhőszolgáltatót

Válassza ki a szolgáltatóját alább. Mindegyiknek van automatizált szkriptje, amely az első indításkor fut le és **5–10 percen belül** befejezi a beállítást.

| Szolgáltató | Útmutató |
|------------|---------|
| Linode (Akamai) | [Telepítés Linode-ra](../cloud-deployment/linode) — legegyszerűbb, StackScript alapú form-vezérelt beállítás |
| DigitalOcean | [Telepítés DigitalOcean-ra](../cloud-deployment/digitalocean) |
| AWS EC2 | [Telepítés AWS-re](../cloud-deployment/aws) |
| Google Cloud | [Telepítés GCP-re](../cloud-deployment/gcp) |

> **A legtöbb felhasználónak ajánlott:** Kezdje a Linode-dal — a StackScript form alapú felületet biztosít, így semmit sem kell manuálisan szerkeszteni."""),

    "id": ("Mulai Cepat", "Deploy rtCloud di server Anda sendiri dalam hitungan menit menggunakan skrip cloud otomatis.", """Panduan ini membantu Anda menjalankan rtCloud di server sendiri. Skrip otomatis menangani segalanya — Docker, SSL, database, firewall — dalam satu kali jalankan.

## Persyaratan

### Server

| Sumber Daya | Minimum | Direkomendasikan |
|-------------|---------|-----------------|
| RAM | 2 GB | 4 GB (diperlukan jika menggunakan Keycloak SSO) |
| Disk | 25 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPUs |
| OS | Ubuntu 22.04 LTS | Ubuntu 22.04 LTS |

### Domain

Anda membutuhkan nama domain dengan **A record yang mengarah ke IP server** sebelum menjalankan skrip. Let's Encrypt memerlukan resolusi DNS untuk penerbitan sertifikat SSL.

---

## Pilih Penyedia Cloud Anda

Pilih penyedia di bawah ini. Masing-masing memiliki skrip otomatis yang berjalan saat boot pertama dan menyelesaikan pengaturan dalam **5–10 menit**.

| Penyedia | Panduan |
|---------|--------|
| Linode (Akamai) | [Deploy di Linode](../cloud-deployment/linode) — termudah, pengaturan berbasis formulir via StackScript |
| DigitalOcean | [Deploy di DigitalOcean](../cloud-deployment/digitalocean) |
| AWS EC2 | [Deploy di AWS](../cloud-deployment/aws) |
| Google Cloud | [Deploy di GCP](../cloud-deployment/gcp) |

> **Direkomendasikan untuk sebagian besar pengguna:** Mulai dengan Linode — StackScript memberikan UI berbasis formulir sehingga tidak perlu mengedit apa pun secara manual."""),

    "it": ("Avvio rapido", "Distribuisci rtCloud sul tuo server in pochi minuti con uno script cloud automatizzato.", """Questa guida ti aiuta a mettere in funzione rtCloud sul tuo server. Gli script automatizzati gestiscono tutto — Docker, SSL, database, firewall — in una singola esecuzione.

## Requisiti

### Server

| Risorsa | Minimo | Consigliato |
|---------|--------|------------|
| RAM | 2 GB | 4 GB (necessario con Keycloak SSO) |
| Disco | 25 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPUs |
| OS | Ubuntu 22.04 LTS | Ubuntu 22.04 LTS |

### Dominio

È necessario un nome di dominio con un **record A che punta all'IP del server** prima di eseguire lo script. Let's Encrypt richiede la risoluzione DNS per il rilascio del certificato SSL.

---

## Scegli il tuo provider cloud

Seleziona il tuo provider qui sotto. Ognuno ha uno script automatizzato che viene eseguito al primo avvio e completa la configurazione in **5–10 minuti**.

| Provider | Guida |
|---------|-------|
| Linode (Akamai) | [Distribuisci su Linode](../cloud-deployment/linode) — più semplice, configurazione basata su modulo via StackScript |
| DigitalOcean | [Distribuisci su DigitalOcean](../cloud-deployment/digitalocean) |
| AWS EC2 | [Distribuisci su AWS](../cloud-deployment/aws) |
| Google Cloud | [Distribuisci su GCP](../cloud-deployment/gcp) |

> **Consigliato per la maggior parte degli utenti:** Inizia con Linode — lo StackScript fornisce un'interfaccia basata su modulo, quindi non c'è nulla da modificare manualmente."""),

    "ja": ("クイックスタート", "自動化されたクラウドスクリプトを使用して、数分で自分のサーバーにrtCloudをデプロイします。", """このガイドは、自分のサーバーでrtCloudを起動するためのものです。自動化スクリプトがすべてを処理します — Docker、SSL、データベース、ファイアウォール — 1回の実行で完了します。

## 要件

### サーバー

| リソース | 最低限 | 推奨 |
|--------|-------|------|
| RAM | 2 GB | 4 GB（Keycloak SSO使用時に必要） |
| ディスク | 25 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPUs |
| OS | Ubuntu 22.04 LTS | Ubuntu 22.04 LTS |

### ドメイン

スクリプトを実行する前に、**サーバーのIPアドレスを指すAレコード**を持つドメイン名が必要です。Let's EncryptはSSL証明書の発行にDNS解決を必要とします。

---

## クラウドプロバイダーを選択

以下からプロバイダーを選択してください。それぞれに自動化スクリプトがあり、初回起動時に実行されて**5〜10分**でセットアップが完了します。

| プロバイダー | ガイド |
|-----------|-------|
| Linode (Akamai) | [Linodeにデプロイ](../cloud-deployment/linode) — 最も簡単、StackScript経由のフォームベース設定 |
| DigitalOcean | [DigitalOceanにデプロイ](../cloud-deployment/digitalocean) |
| AWS EC2 | [AWSにデプロイ](../cloud-deployment/aws) |
| Google Cloud | [GCPにデプロイ](../cloud-deployment/gcp) |

> **ほとんどのユーザーへの推奨:** Linodeから始めてください — StackScriptはフォームベースのUIを提供するため、手動で編集するものはありません。"""),

    "km": ("ចាប់ផ្ដើមរហ័ស", "ដាក់ rtCloud ឱ្យប្រើប្រាស់នៅលើម៉ាស៊ីនមេរបស់អ្នកក្នុងពេលប៉ុន្មាននាទីដោយប្រើស្គ្រីបស្វ័យប្រវត្តិ។", """មគ្គុទ្ទេសក៍នេះជួយអ្នកដំណើរការ rtCloud នៅលើម៉ាស៊ីនមេរបស់អ្នក។ ស្គ្រីបស្វ័យប្រវត្តិដោះស្រាយអ្វីៗទាំងអស់ — Docker, SSL, មូលដ្ឋានទិន្នន័យ, ជញ្ជាំងភ្លើង — ក្នុងការដំណើរការតែមួយ។

## តម្រូវការ

### ម៉ាស៊ីនមេ

| ធនធាន | អប្បបរមា | បានណែនាំ |
|-------|---------|---------|
| RAM | 2 GB | 4 GB (ត្រូវការជាមួយ Keycloak SSO) |
| ថាស | 25 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPUs |
| OS | Ubuntu 22.04 LTS | Ubuntu 22.04 LTS |

### ដែន

អ្នកត្រូវការឈ្មោះដែនដែលមាន **កំណត់ត្រា A ដែលចង្អុលទៅ IP ម៉ាស៊ីនមេ** មុនពេលដំណើរការស្គ្រីប។ Let's Encrypt ត្រូវការការដោះស្រាយ DNS ដើម្បីចេញវិញ្ញាបនប័ត្រ SSL។

---

## ជ្រើសរើសអ្នកផ្ដល់ Cloud របស់អ្នក

ជ្រើសរើសអ្នកផ្ដល់ខាងក្រោម។ នីមួយៗមានស្គ្រីបស្វ័យប្រវត្តិដែលដំណើរការនៅពេលចាប់ផ្ដើមដំបូង ហើយបញ្ចប់ការដំឡើងក្នុង **5–10 នាទី**។

| អ្នកផ្ដល់ | មគ្គុទ្ទេសក៍ |
|---------|-----------|
| Linode (Akamai) | [ដាក់ឱ្យប្រើប្រាស់នៅ Linode](../cloud-deployment/linode) — ងាយស្រួលបំផុត ការដំឡើងដោយផ្អែកលើទម្រង់តាម StackScript |
| DigitalOcean | [ដាក់ឱ្យប្រើប្រាស់នៅ DigitalOcean](../cloud-deployment/digitalocean) |
| AWS EC2 | [ដាក់ឱ្យប្រើប្រាស់នៅ AWS](../cloud-deployment/aws) |
| Google Cloud | [ដាក់ឱ្យប្រើប្រាស់នៅ GCP](../cloud-deployment/gcp) |

> **បានណែនាំសម្រាប់អ្នកប្រើភាគច្រើន:** ចាប់ផ្ដើមជាមួយ Linode — StackScript ផ្ដល់ UI ដោយផ្អែកលើទម្រង់ ដូច្នេះមិនចាំបាច់កែសម្រួលដោយដៃ។"""),

    "ko": ("빠른 시작", "자동화된 클라우드 스크립트를 사용하여 몇 분 만에 자체 서버에 rtCloud를 배포합니다.", """이 가이드는 자체 서버에서 rtCloud를 실행하는 데 도움을 줍니다. 자동화 스크립트가 모든 것을 처리합니다 — Docker, SSL, 데이터베이스, 방화벽 — 한 번의 실행으로 완료됩니다.

## 요구 사항

### 서버

| 리소스 | 최소 | 권장 |
|-------|-----|-----|
| RAM | 2 GB | 4 GB (Keycloak SSO 사용 시 필요) |
| 디스크 | 25 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPUs |
| OS | Ubuntu 22.04 LTS | Ubuntu 22.04 LTS |

### 도메인

스크립트를 실행하기 전에 **서버 IP를 가리키는 A 레코드**가 있는 도메인 이름이 필요합니다. Let's Encrypt는 SSL 인증서 발급을 위해 DNS 해석이 필요합니다.

---

## 클라우드 제공업체 선택

아래에서 제공업체를 선택하세요. 각각 첫 번째 부팅 시 실행되는 자동화 스크립트가 있으며 **5–10분** 내에 설정을 완료합니다.

| 제공업체 | 가이드 |
|---------|-------|
| Linode (Akamai) | [Linode에 배포](../cloud-deployment/linode) — 가장 쉬움, StackScript를 통한 폼 기반 설정 |
| DigitalOcean | [DigitalOcean에 배포](../cloud-deployment/digitalocean) |
| AWS EC2 | [AWS에 배포](../cloud-deployment/aws) |
| Google Cloud | [GCP에 배포](../cloud-deployment/gcp) |

> **대부분의 사용자에게 권장:** Linode로 시작하세요 — StackScript가 폼 기반 UI를 제공하므로 수동으로 편집할 것이 없습니다."""),

    "lt": ("Greitas pradžios vadovas", "Įdiekite rtCloud savo serveryje per kelias minutes naudodami automatizuotą debesies scenarijų.", """Šis vadovas padeda paleisti rtCloud savo serveryje. Automatizuoti scenarijai pasirūpina viskuo — Docker, SSL, duomenų baze, ugniasiene — vienu paleidimo metu.

## Reikalavimai

### Serveris

| Resursas | Minimum | Rekomenduojama |
|---------|---------|---------------|
| RAM | 2 GB | 4 GB (būtina su Keycloak SSO) |
| Diskas | 25 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPUs |
| OS | Ubuntu 22.04 LTS | Ubuntu 22.04 LTS |

### Domenas

Prieš paleidžiant scenarijų reikalingas domeno vardas su **A įrašu, nurodančiu į serverio IP**. Let's Encrypt reikalauja DNS raiškos SSL sertifikatui išduoti.

---

## Pasirinkite debesies tiekėją

Pasirinkite savo tiekėją žemiau. Kiekvienas turi automatizuotą scenarijų, kuris paleidžiamas pirmą kartą įkraunant ir baigia sąranką per **5–10 minučių**.

| Tiekėjas | Vadovas |
|---------|--------|
| Linode (Akamai) | [Diegimas Linode](../cloud-deployment/linode) — paprasčiausias, formomis pagrįsta sąranka per StackScript |
| DigitalOcean | [Diegimas DigitalOcean](../cloud-deployment/digitalocean) |
| AWS EC2 | [Diegimas AWS](../cloud-deployment/aws) |
| Google Cloud | [Diegimas GCP](../cloud-deployment/gcp) |

> **Rekomenduojama daugumai vartotojų:** Pradėkite su Linode — StackScript suteikia formomis pagrįstą UI, todėl nereikia nieko redaguoti rankiniu būdu."""),

    "lv": ("Ātrā sākšana", "Izvietojiet rtCloud savā serverī dažu minūšu laikā ar automatizētu mākoņskriptu.", """Šī rokasgrāmata palīdz palaist rtCloud savā serverī. Automatizētie skripti rūpējas par visu — Docker, SSL, datu bāzi, ugunsmūri — vienā palaišanas reizē.

## Prasības

### Serveris

| Resurss | Minimums | Ieteicamais |
|---------|---------|------------|
| RAM | 2 GB | 4 GB (nepieciešams ar Keycloak SSO) |
| Disks | 25 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPUs |
| OS | Ubuntu 22.04 LTS | Ubuntu 22.04 LTS |

### Domēns

Pirms skripta palaišanas nepieciešams domēna vārds ar **A ierakstu, kas norāda uz servera IP**. Let's Encrypt prasa DNS izšķirtspēju SSL sertifikāta izsniegšanai.

---

## Izvēlieties savu mākoņpakalpojumu sniedzēju

Izvēlieties savu sniedzēju zemāk. Katram ir automatizēts skripts, kas darbojas pirmajā sāknēšanas reizē un pabeidz iestatīšanu **5–10 minūtēs**.

| Sniedzējs | Rokasgrāmata |
|---------|------------|
| Linode (Akamai) | [Izvietošana Linode](../cloud-deployment/linode) — vieglākais, veidlapas iestatīšana caur StackScript |
| DigitalOcean | [Izvietošana DigitalOcean](../cloud-deployment/digitalocean) |
| AWS EC2 | [Izvietošana AWS](../cloud-deployment/aws) |
| Google Cloud | [Izvietošana GCP](../cloud-deployment/gcp) |

> **Ieteicams lielākajai daļai:** Sāciet ar Linode — StackScript nodrošina veidlapas UI, tāpēc nekas nav manuāli jārediģē."""),

    "nb": ("Hurtigstart", "Distribuer rtCloud på din egen server på få minutter med et automatisert skyskript.", """Denne veiledningen hjelper deg med å kjøre rtCloud på din egen server. De automatiserte skriptene tar seg av alt — Docker, SSL, database, brannmur — i én enkelt kjøring.

## Krav

### Server

| Ressurs | Minimum | Anbefalt |
|---------|---------|---------|
| RAM | 2 GB | 4 GB (påkrevd med Keycloak SSO) |
| Disk | 25 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPUs |
| OS | Ubuntu 22.04 LTS | Ubuntu 22.04 LTS |

### Domene

Du trenger et domenenavn med en **A-post som peker til serverens IP** før du kjører skriptet. Let's Encrypt krever DNS-oppløsning for å utstede SSL-sertifikat.

---

## Velg din skyleverandør

Velg din leverandør nedenfor. Hver har et automatisert skript som kjører ved første oppstart og fullfører oppsett på **5–10 minutter**.

| Leverandør | Veiledning |
|-----------|-----------|
| Linode (Akamai) | [Distribuer på Linode](../cloud-deployment/linode) — enklest, skjemabasert oppsett via StackScript |
| DigitalOcean | [Distribuer på DigitalOcean](../cloud-deployment/digitalocean) |
| AWS EC2 | [Distribuer på AWS](../cloud-deployment/aws) |
| Google Cloud | [Distribuer på GCP](../cloud-deployment/gcp) |

> **Anbefalt for de fleste:** Start med Linode — StackScript gir et skjemabasert grensesnitt slik at det ikke er noe å redigere manuelt."""),

    "nl": ("Snel starten", "Implementeer rtCloud op uw eigen server in minuten met een geautomatiseerd cloudscript.", """Deze gids helpt u rtCloud op uw eigen server te laten draaien. De geautomatiseerde scripts regelen alles — Docker, SSL, database, firewall — in één uitvoering.

## Vereisten

### Server

| Bron | Minimum | Aanbevolen |
|------|---------|-----------|
| RAM | 2 GB | 4 GB (vereist met Keycloak SSO) |
| Schijf | 25 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPUs |
| OS | Ubuntu 22.04 LTS | Ubuntu 22.04 LTS |

### Domein

U hebt een domeinnaam nodig met een **A-record dat naar het IP-adres van de server wijst** voordat u het script uitvoert. Let's Encrypt vereist DNS-omzetting voor het afgeven van het SSL-certificaat.

---

## Kies uw cloudprovider

Selecteer uw provider hieronder. Elk heeft een geautomatiseerd script dat bij de eerste opstart wordt uitgevoerd en de installatie voltooit in **5–10 minuten**.

| Provider | Gids |
|---------|------|
| Linode (Akamai) | [Implementeer op Linode](../cloud-deployment/linode) — eenvoudigst, formuliergebaseerde instelling via StackScript |
| DigitalOcean | [Implementeer op DigitalOcean](../cloud-deployment/digitalocean) |
| AWS EC2 | [Implementeer op AWS](../cloud-deployment/aws) |
| Google Cloud | [Implementeer op GCP](../cloud-deployment/gcp) |

> **Aanbevolen voor de meeste gebruikers:** Begin met Linode — de StackScript biedt een formuliergebaseerde UI, zodat er niets handmatig bewerkt hoeft te worden."""),

    "pl": ("Szybki start", "Wdróż rtCloud na własnym serwerze w kilka minut za pomocą zautomatyzowanego skryptu chmurowego.", """Ten przewodnik pomaga uruchomić rtCloud na własnym serwerze. Automatyczne skrypty zajmują się wszystkim — Docker, SSL, baza danych, zapora sieciowa — w jednym uruchomieniu.

## Wymagania

### Serwer

| Zasób | Minimum | Zalecane |
|-------|---------|---------|
| RAM | 2 GB | 4 GB (wymagane z Keycloak SSO) |
| Dysk | 25 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPUs |
| OS | Ubuntu 22.04 LTS | Ubuntu 22.04 LTS |

### Domena

Przed uruchomieniem skryptu potrzebujesz nazwy domeny z **rekordem A wskazującym na IP serwera**. Let's Encrypt wymaga rozwiązania DNS do wydania certyfikatu SSL.

---

## Wybierz dostawcę chmury

Wybierz dostawcę poniżej. Każdy ma automatyczny skrypt uruchamiany przy pierwszym rozruchu, który kończy konfigurację w **5–10 minutach**.

| Dostawca | Przewodnik |
|---------|----------|
| Linode (Akamai) | [Wdrożenie na Linode](../cloud-deployment/linode) — najłatwiejsze, konfiguracja oparta na formularzu przez StackScript |
| DigitalOcean | [Wdrożenie na DigitalOcean](../cloud-deployment/digitalocean) |
| AWS EC2 | [Wdrożenie na AWS](../cloud-deployment/aws) |
| Google Cloud | [Wdrożenie na GCP](../cloud-deployment/gcp) |

> **Zalecane dla większości użytkowników:** Zacznij od Linode — StackScript zapewnia interfejs oparty na formularzu, więc nic nie trzeba ręcznie edytować."""),

    "pt": ("Início rápido", "Implemente o rtCloud no seu próprio servidor em minutos com um script de cloud automatizado.", """Este guia ajuda-o a colocar o rtCloud a funcionar no seu próprio servidor. Os scripts automatizados tratam de tudo — Docker, SSL, base de dados, firewall — numa única execução.

## Requisitos

### Servidor

| Recurso | Mínimo | Recomendado |
|---------|--------|------------|
| RAM | 2 GB | 4 GB (necessário com Keycloak SSO) |
| Disco | 25 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPUs |
| OS | Ubuntu 22.04 LTS | Ubuntu 22.04 LTS |

### Domínio

Precisa de um nome de domínio com um **registo A a apontar para o IP do servidor** antes de executar o script. O Let's Encrypt requer resolução DNS para emitir o certificado SSL.

---

## Escolha o seu fornecedor de cloud

Selecione o seu fornecedor abaixo. Cada um tem um script automatizado que é executado no primeiro arranque e conclui a configuração em **5–10 minutos**.

| Fornecedor | Guia |
|-----------|------|
| Linode (Akamai) | [Implementar no Linode](../cloud-deployment/linode) — mais fácil, configuração baseada em formulário via StackScript |
| DigitalOcean | [Implementar no DigitalOcean](../cloud-deployment/digitalocean) |
| AWS EC2 | [Implementar na AWS](../cloud-deployment/aws) |
| Google Cloud | [Implementar no GCP](../cloud-deployment/gcp) |

> **Recomendado para a maioria dos utilizadores:** Comece com o Linode — o StackScript fornece uma interface baseada em formulário para que não haja nada a editar manualmente."""),

    "pt-br": ("Início rápido", "Implante o rtCloud no seu próprio servidor em minutos com um script de nuvem automatizado.", """Este guia ajuda você a colocar o rtCloud em funcionamento no seu próprio servidor. Os scripts automatizados cuidam de tudo — Docker, SSL, banco de dados, firewall — em uma única execução.

## Requisitos

### Servidor

| Recurso | Mínimo | Recomendado |
|---------|--------|------------|
| RAM | 2 GB | 4 GB (necessário com Keycloak SSO) |
| Disco | 25 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPUs |
| OS | Ubuntu 22.04 LTS | Ubuntu 22.04 LTS |

### Domínio

Você precisa de um nome de domínio com um **registro A apontando para o IP do servidor** antes de executar o script. O Let's Encrypt requer resolução DNS para emitir o certificado SSL.

---

## Escolha seu provedor de nuvem

Selecione seu provedor abaixo. Cada um tem um script automatizado que é executado na primeira inicialização e conclui a configuração em **5–10 minutos**.

| Provedor | Guia |
|---------|------|
| Linode (Akamai) | [Implantar no Linode](../cloud-deployment/linode) — mais fácil, configuração baseada em formulário via StackScript |
| DigitalOcean | [Implantar no DigitalOcean](../cloud-deployment/digitalocean) |
| AWS EC2 | [Implantar na AWS](../cloud-deployment/aws) |
| Google Cloud | [Implantar no GCP](../cloud-deployment/gcp) |

> **Recomendado para a maioria dos usuários:** Comece com o Linode — o StackScript fornece uma interface baseada em formulário para que não haja nada a editar manualmente."""),

    "ru": ("Быстрый старт", "Разверните rtCloud на своём сервере за несколько минут с помощью автоматизированного облачного скрипта.", """Это руководство поможет вам запустить rtCloud на собственном сервере. Автоматизированные скрипты берут на себя всё — Docker, SSL, базу данных, брандмауэр — за один запуск.

## Требования

### Сервер

| Ресурс | Минимум | Рекомендуется |
|--------|---------|--------------|
| RAM | 2 GB | 4 GB (требуется при использовании Keycloak SSO) |
| Диск | 25 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPUs |
| ОС | Ubuntu 22.04 LTS | Ubuntu 22.04 LTS |

### Домен

Перед запуском скрипта вам нужно доменное имя с **A-записью, указывающей на IP сервера**. Let's Encrypt требует DNS-разрешения для выдачи SSL-сертификата.

---

## Выберите облачного провайдера

Выберите своего провайдера ниже. У каждого есть автоматизированный скрипт, который запускается при первой загрузке и завершает настройку за **5–10 минут**.

| Провайдер | Руководство |
|----------|------------|
| Linode (Akamai) | [Развернуть на Linode](../cloud-deployment/linode) — проще всего, настройка через форму StackScript |
| DigitalOcean | [Развернуть на DigitalOcean](../cloud-deployment/digitalocean) |
| AWS EC2 | [Развернуть на AWS](../cloud-deployment/aws) |
| Google Cloud | [Развернуть на GCP](../cloud-deployment/gcp) |

> **Рекомендуется для большинства:** Начните с Linode — StackScript предоставляет интерфейс на основе формы, поэтому ничего не нужно редактировать вручную."""),

    "sk": ("Rýchly štart", "Nasaďte rtCloud na vlastný server za pár minút pomocou automatizovaného cloudového skriptu.", """Tento sprievodca vám pomôže spustiť rtCloud na vlastnom serveri. Automatizované skripty sa postarajú o všetko — Docker, SSL, databázu, bránu firewall — jedným spustením.

## Požiadavky

### Server

| Zdroj | Minimum | Odporúčané |
|-------|---------|-----------|
| RAM | 2 GB | 4 GB (nutné pri Keycloak SSO) |
| Disk | 25 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPUs |
| OS | Ubuntu 22.04 LTS | Ubuntu 22.04 LTS |

### Doména

Pred spustením skriptu potrebujete doménové meno s **A záznamom smerujúcim na IP servera**. Let's Encrypt vyžaduje DNS rozlíšenie pre vydanie SSL certifikátu.

---

## Vyberte si poskytovateľa cloudu

Vyberte svojho poskytovateľa nižšie. Každý má automatizovaný skript, ktorý sa spustí pri prvom štarte a dokončí nastavenie za **5–10 minút**.

| Poskytovateľ | Sprievodca |
|-------------|----------|
| Linode (Akamai) | [Nasadenie na Linode](../cloud-deployment/linode) — najjednoduchšie, formulárové nastavenie cez StackScript |
| DigitalOcean | [Nasadenie na DigitalOcean](../cloud-deployment/digitalocean) |
| AWS EC2 | [Nasadenie na AWS](../cloud-deployment/aws) |
| Google Cloud | [Nasadenie na GCP](../cloud-deployment/gcp) |

> **Odporúčané pre väčšinu používateľov:** Začnite s Linode — StackScript poskytuje formulárové UI, takže nie je potrebné nič ručne upravovať."""),

    "sq": ("Fillim i shpejtë", "Vendosni rtCloud në serverin tuaj në minuta me një skript cloud të automatizuar.", """Ky udhëzues ju ndihmon të drejtoni rtCloud në serverin tuaj. Skriptet e automatizuara kujdesen për gjithçka — Docker, SSL, bazën e të dhënave, murin e zjarrit — në një ekzekutim të vetëm.

## Kërkesat

### Serveri

| Burimi | Minimumi | Rekomandohet |
|--------|---------|-------------|
| RAM | 2 GB | 4 GB (kërkohet me Keycloak SSO) |
| Disku | 25 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPUs |
| OS | Ubuntu 22.04 LTS | Ubuntu 22.04 LTS |

### Domeni

Ju nevojitet një emër domeni me një **regjistrim A që tregon drejt IP-së së serverit** para se të ekzekutoni skriptin. Let's Encrypt kërkon rezolucion DNS për lëshimin e certifikatës SSL.

---

## Zgjidhni Ofruesin tuaj Cloud

Zgjidhni ofruesin tuaj më poshtë. Secili ka një skript të automatizuar që ekzekutohet gjatë nisjes së parë dhe përfundon konfigurimin brenda **5–10 minutave**.

| Ofruesi | Udhëzuesi |
|--------|---------|
| Linode (Akamai) | [Vendosni në Linode](../cloud-deployment/linode) — më i lehtë, konfigurimi i bazuar në formular nëpërmjet StackScript |
| DigitalOcean | [Vendosni në DigitalOcean](../cloud-deployment/digitalocean) |
| AWS EC2 | [Vendosni në AWS](../cloud-deployment/aws) |
| Google Cloud | [Vendosni në GCP](../cloud-deployment/gcp) |

> **Rekomandohet për shumicën e përdoruesve:** Filloni me Linode — StackScript ofron një ndërfaqe të bazuar në formular, kështu që nuk ka asgjë për të redaktuar manualisht."""),

    "sr": ("Брзи почетак", "Поставите rtCloud на сопственом серверу за неколико минута помоћу аутоматизованог скрипта.", """Овај водич помаже вам да покренете rtCloud на сопственом серверу. Аутоматизоване скрипте бринуо о свему — Docker, SSL, бази података, заштитном зиду — у jedном покретању.

## Захтеви

### Сервер

| Ресурс | Минимум | Препоручено |
|--------|---------|-----------|
| RAM | 2 GB | 4 GB (потребно са Keycloak SSO) |
| Диск | 25 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPUs |
| OS | Ubuntu 22.04 LTS | Ubuntu 22.04 LTS |

### Домен

Потребно је доменско ime са **A записом koji упућује на IP сервера** пре покретања скрипте. Let's Encrypt захтева DNS резолуцију за издавање SSL сертификата.

---

## Изаберите провајдера облака

Изаберите свог провајдера испод. Сваки има аутоматизовану скрипту која се покреће при prvом boot-у и завршава подешавање за **5–10 минута**.

| Провајдер | Водич |
|---------|------|
| Linode (Akamai) | [Постављање на Linode](../cloud-deployment/linode) — najlakše, podešavanje zasnovano na formi putem StackScript |
| DigitalOcean | [Постављање на DigitalOcean](../cloud-deployment/digitalocean) |
| AWS EC2 | [Постављање на AWS](../cloud-deployment/aws) |
| Google Cloud | [Постављање на GCP](../cloud-deployment/gcp) |

> **Препоручено за већину корисника:** Почните са Linode — StackScript пружа UI на основу форме, тако да нема ничега за ручно уређивање."""),

    "sv": ("Snabbstart", "Driftsätt rtCloud på din egen server på några minuter med ett automatiserat molnskript.", """Den här guiden hjälper dig att få igång rtCloud på din egen server. De automatiserade skripten tar hand om allt — Docker, SSL, databas, brandvägg — i en enda körning.

## Krav

### Server

| Resurs | Minimum | Rekommenderat |
|--------|---------|--------------|
| RAM | 2 GB | 4 GB (krävs med Keycloak SSO) |
| Disk | 25 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPUs |
| OS | Ubuntu 22.04 LTS | Ubuntu 22.04 LTS |

### Domän

Du behöver ett domännamn med en **A-post som pekar på serverns IP** innan du kör skriptet. Let's Encrypt kräver DNS-upplösning för att utfärda SSL-certifikat.

---

## Välj din molnleverantör

Välj din leverantör nedan. Var och en har ett automatiserat skript som körs vid första uppstarten och slutför inställningen på **5–10 minuter**.

| Leverantör | Guide |
|-----------|-------|
| Linode (Akamai) | [Driftsätt på Linode](../cloud-deployment/linode) — enklast, formulärbaserad inställning via StackScript |
| DigitalOcean | [Driftsätt på DigitalOcean](../cloud-deployment/digitalocean) |
| AWS EC2 | [Driftsätt på AWS](../cloud-deployment/aws) |
| Google Cloud | [Driftsätt på GCP](../cloud-deployment/gcp) |

> **Rekommenderas för de flesta:** Börja med Linode — StackScript ger ett formulärbaserat gränssnitt så det finns inget att redigera manuellt."""),

    "te": ("త్వరిత ప్రారంభం", "స్వయంచాలిత క్లౌడ్ స్క్రిప్ట్‌తో మీ స్వంత సర్వర్‌లో నిమిషాల్లో rtCloud విన్యసించండి.", """ఈ గైడ్ మీ స్వంత సర్వర్‌లో rtCloud నడుపుటకు సహాయపడుతుంది. స్వయంచాలిత స్క్రిప్ట్‌లు అన్నింటినీ నిర్వహిస్తాయి — Docker, SSL, డేటాబేస్, ఫైర్‌వాల్ — ఒక్క రన్‌లో.

## అవసరాలు

### సర్వర్

| వనరు | కనీసం | సిఫార్సు |
|------|------|---------|
| RAM | 2 GB | 4 GB (Keycloak SSO తో అవసరం) |
| డిస్క్ | 25 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPUs |
| OS | Ubuntu 22.04 LTS | Ubuntu 22.04 LTS |

### డొమైన్

స్క్రిప్ట్ అమలు చేయడానికి ముందు **సర్వర్ IP వైపు A రికార్డ్** ఉన్న డొమైన్ పేరు అవసరం. SSL సర్టిఫికేట్ జారీ చేయడానికి Let's Encrypt DNS రిజల్యూషన్ అవసరం.

---

## మీ క్లౌడ్ ప్రొవైడర్‌ను ఎంచుకోండి

దిగువ మీ ప్రొవైడర్‌ను ఎంచుకోండి. ప్రతి ఒక్కటి మొదటి బూట్‌లో నడిచే స్వయంచాలిత స్క్రిప్ట్‌ను కలిగి ఉంటుంది మరియు **5–10 నిమిషాల్లో** సెటప్ పూర్తి చేస్తుంది.

| ప్రొవైడర్ | గైడ్ |
|---------|-----|
| Linode (Akamai) | [Linode లో విన్యసించండి](../cloud-deployment/linode) — అత్యంత సులభం, StackScript ద్వారా ఫారమ్-ఆధారిత సెటప్ |
| DigitalOcean | [DigitalOcean లో విన్యసించండి](../cloud-deployment/digitalocean) |
| AWS EC2 | [AWS లో విన్యసించండి](../cloud-deployment/aws) |
| Google Cloud | [GCP లో విన్యసించండి](../cloud-deployment/gcp) |

> **చాలా మంది వినియోగదారులకు సిఫార్సు:** Linode తో ప్రారంభించండి — StackScript ఫారమ్-ఆధారిత UI అందిస్తుంది కాబట్టి మాన్యువల్‌గా ఏదీ సవరించాల్సిన అవసరం లేదు."""),

    "th": ("เริ่มต้นอย่างรวดเร็ว", "ติดตั้ง rtCloud บนเซิร์ฟเวอร์ของคุณในไม่กี่นาทีด้วยสคริปต์คลาวด์อัตโนมัติ", """คู่มือนี้ช่วยให้คุณเรียกใช้ rtCloud บนเซิร์ฟเวอร์ของคุณเอง สคริปต์อัตโนมัติจัดการทุกอย่าง — Docker, SSL, ฐานข้อมูล, ไฟร์วอลล์ — ในการรันครั้งเดียว

## ข้อกำหนด

### เซิร์ฟเวอร์

| ทรัพยากร | ขั้นต่ำ | แนะนำ |
|---------|--------|------|
| RAM | 2 GB | 4 GB (จำเป็นเมื่อใช้ Keycloak SSO) |
| ดิสก์ | 25 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPUs |
| OS | Ubuntu 22.04 LTS | Ubuntu 22.04 LTS |

### โดเมน

คุณต้องการชื่อโดเมนที่มี **A record ชี้ไปยัง IP ของเซิร์ฟเวอร์** ก่อนรันสคริปต์ Let's Encrypt ต้องการการแก้ไข DNS เพื่อออกใบรับรอง SSL

---

## เลือกผู้ให้บริการคลาวด์ของคุณ

เลือกผู้ให้บริการของคุณด้านล่าง แต่ละรายมีสคริปต์อัตโนมัติที่ทำงานเมื่อบูตครั้งแรกและเสร็จสิ้นการตั้งค่าใน **5–10 นาที**

| ผู้ให้บริการ | คู่มือ |
|-----------|------|
| Linode (Akamai) | [ติดตั้งบน Linode](../cloud-deployment/linode) — ง่ายที่สุด การตั้งค่าแบบฟอร์มผ่าน StackScript |
| DigitalOcean | [ติดตั้งบน DigitalOcean](../cloud-deployment/digitalocean) |
| AWS EC2 | [ติดตั้งบน AWS](../cloud-deployment/aws) |
| Google Cloud | [ติดตั้งบน GCP](../cloud-deployment/gcp) |

> **แนะนำสำหรับผู้ใช้ส่วนใหญ่:** เริ่มต้นด้วย Linode — StackScript ให้ UI แบบฟอร์มดังนั้นไม่ต้องแก้ไขด้วยตนเอง"""),

    "tr": ("Hızlı Başlangıç", "Otomatik bir bulut betiği ile dakikalar içinde kendi sunucunuza rtCloud dağıtın.", """Bu kılavuz, kendi sunucunuzda rtCloud'u çalıştırmanıza yardımcı olur. Otomatik betikler her şeyi halleder — Docker, SSL, veritabanı, güvenlik duvarı — tek bir çalıştırmayla.

## Gereksinimler

### Sunucu

| Kaynak | Minimum | Önerilen |
|--------|---------|---------|
| RAM | 2 GB | 4 GB (Keycloak SSO ile gerekli) |
| Disk | 25 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPUs |
| İşletim Sistemi | Ubuntu 22.04 LTS | Ubuntu 22.04 LTS |

### Alan Adı

Betiği çalıştırmadan önce **sunucunun IP'sine işaret eden A kaydına** sahip bir alan adına ihtiyacınız var. Let's Encrypt SSL sertifikası vermek için DNS çözümlemesi gerektirir.

---

## Bulut Sağlayıcınızı Seçin

Aşağıdan sağlayıcınızı seçin. Her birinin ilk açılışta çalışan ve **5–10 dakika** içinde kurulumu tamamlayan otomatik bir betiği vardır.

| Sağlayıcı | Kılavuz |
|---------|--------|
| Linode (Akamai) | [Linode'a Dağıt](../cloud-deployment/linode) — en kolay, StackScript üzerinden form tabanlı kurulum |
| DigitalOcean | [DigitalOcean'a Dağıt](../cloud-deployment/digitalocean) |
| AWS EC2 | [AWS'ye Dağıt](../cloud-deployment/aws) |
| Google Cloud | [GCP'ye Dağıt](../cloud-deployment/gcp) |

> **Çoğu kullanıcı için önerilir:** Linode ile başlayın — StackScript form tabanlı bir arayüz sunar, bu nedenle manuel olarak düzenlenecek hiçbir şey yoktur."""),

    "uk": ("Швидкий старт", "Розгорніть rtCloud на власному сервері за кілька хвилин за допомогою автоматизованого хмарного скрипту.", """Цей посібник допоможе вам запустити rtCloud на власному сервері. Автоматизовані скрипти беруть на себе все — Docker, SSL, базу даних, брандмауер — за один запуск.

## Вимоги

### Сервер

| Ресурс | Мінімум | Рекомендовано |
|--------|---------|--------------|
| RAM | 2 GB | 4 GB (потрібно при використанні Keycloak SSO) |
| Диск | 25 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPUs |
| ОС | Ubuntu 22.04 LTS | Ubuntu 22.04 LTS |

### Домен

Перед запуском скрипту потрібне доменне ім'я з **A-записом, що вказує на IP сервера**. Let's Encrypt вимагає DNS-розрішення для видачі SSL-сертифіката.

---

## Оберіть хмарного провайдера

Виберіть свого провайдера нижче. Кожен має автоматизований скрипт, що запускається при першому завантаженні та завершує налаштування за **5–10 хвилин**.

| Провайдер | Посібник |
|----------|---------|
| Linode (Akamai) | [Розгорнути на Linode](../cloud-deployment/linode) — найпростіше, налаштування на основі форми через StackScript |
| DigitalOcean | [Розгорнути на DigitalOcean](../cloud-deployment/digitalocean) |
| AWS EC2 | [Розгорнути на AWS](../cloud-deployment/aws) |
| Google Cloud | [Розгорнути на GCP](../cloud-deployment/gcp) |

> **Рекомендується для більшості:** Починайте з Linode — StackScript надає інтерфейс на основі форми, тому нічого не потрібно редагувати вручну."""),

    "vi": ("Bắt đầu nhanh", "Triển khai rtCloud trên máy chủ của bạn trong vài phút với script tự động.", """Hướng dẫn này giúp bạn chạy rtCloud trên máy chủ của riêng mình. Các script tự động xử lý tất cả — Docker, SSL, cơ sở dữ liệu, tường lửa — chỉ trong một lần chạy.

## Yêu cầu

### Máy chủ

| Tài nguyên | Tối thiểu | Khuyến nghị |
|-----------|---------|-----------|
| RAM | 2 GB | 4 GB (bắt buộc khi dùng Keycloak SSO) |
| Ổ đĩa | 25 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPUs |
| HĐH | Ubuntu 22.04 LTS | Ubuntu 22.04 LTS |

### Tên miền

Bạn cần tên miền với **bản ghi A trỏ đến IP máy chủ** trước khi chạy script. Let's Encrypt yêu cầu phân giải DNS để cấp chứng chỉ SSL.

---

## Chọn nhà cung cấp đám mây

Chọn nhà cung cấp bên dưới. Mỗi nhà cung cấp có script tự động chạy khi khởi động lần đầu và hoàn thành cài đặt trong **5–10 phút**.

| Nhà cung cấp | Hướng dẫn |
|------------|---------|
| Linode (Akamai) | [Triển khai trên Linode](../cloud-deployment/linode) — dễ nhất, thiết lập qua biểu mẫu với StackScript |
| DigitalOcean | [Triển khai trên DigitalOcean](../cloud-deployment/digitalocean) |
| AWS EC2 | [Triển khai trên AWS](../cloud-deployment/aws) |
| Google Cloud | [Triển khai trên GCP](../cloud-deployment/gcp) |

> **Khuyến nghị cho hầu hết người dùng:** Bắt đầu với Linode — StackScript cung cấp giao diện dựa trên biểu mẫu nên không cần chỉnh sửa thủ công."""),

    "zh-hans": ("快速开始", "使用自动化云脚本在几分钟内将 rtCloud 部署到您自己的服务器上。", """本指南帮助您在自己的服务器上运行 rtCloud。自动化脚本处理所有事情 — Docker、SSL、数据库、防火墙 — 一次运行即可完成。

## 要求

### 服务器

| 资源 | 最低 | 推荐 |
|------|-----|-----|
| RAM | 2 GB | 4 GB（使用 Keycloak SSO 时必需） |
| 磁盘 | 25 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPUs |
| 操作系统 | Ubuntu 22.04 LTS | Ubuntu 22.04 LTS |

### 域名

运行脚本前，您需要一个**A 记录指向服务器 IP** 的域名。Let's Encrypt 需要 DNS 解析来颁发 SSL 证书。

---

## 选择您的云提供商

在下方选择您的提供商。每个提供商都有一个在首次启动时运行的自动化脚本，在 **5–10 分钟**内完成设置。

| 提供商 | 指南 |
|-------|-----|
| Linode (Akamai) | [在 Linode 上部署](../cloud-deployment/linode) — 最简单，通过 StackScript 进行基于表单的设置 |
| DigitalOcean | [在 DigitalOcean 上部署](../cloud-deployment/digitalocean) |
| AWS EC2 | [在 AWS 上部署](../cloud-deployment/aws) |
| Google Cloud | [在 GCP 上部署](../cloud-deployment/gcp) |

> **大多数用户推荐：** 从 Linode 开始 — StackScript 提供基于表单的界面，无需手动编辑任何内容。"""),

    "zh-hant": ("快速開始", "使用自動化雲端腳本在幾分鐘內將 rtCloud 部署到您自己的伺服器上。", """本指南幫助您在自己的伺服器上執行 rtCloud。自動化腳本處理所有事情 — Docker、SSL、資料庫、防火牆 — 一次執行即可完成。

## 要求

### 伺服器

| 資源 | 最低 | 建議 |
|------|-----|-----|
| RAM | 2 GB | 4 GB（使用 Keycloak SSO 時必需） |
| 磁碟 | 25 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPUs |
| 作業系統 | Ubuntu 22.04 LTS | Ubuntu 22.04 LTS |

### 網域

執行腳本前，您需要一個**A 記錄指向伺服器 IP** 的網域名稱。Let's Encrypt 需要 DNS 解析來頒發 SSL 憑證。

---

## 選擇您的雲端提供商

在下方選擇您的提供商。每個提供商都有一個在首次啟動時執行的自動化腳本，在 **5–10 分鐘**內完成設定。

| 提供商 | 指南 |
|-------|-----|
| Linode (Akamai) | [在 Linode 上部署](../cloud-deployment/linode) — 最簡單，透過 StackScript 進行基於表單的設定 |
| DigitalOcean | [在 DigitalOcean 上部署](../cloud-deployment/digitalocean) |
| AWS EC2 | [在 AWS 上部署](../cloud-deployment/aws) |
| Google Cloud | [在 GCP 上部署](../cloud-deployment/gcp) |

> **大多數使用者推薦：** 從 Linode 開始 — StackScript 提供基於表單的介面，無需手動編輯任何內容。"""),
}

count = 0
for lang, (title, desc, body) in QS.items():
    path = os.path.join(CONTENT_DIR, lang, "docs/getting-started/self-hosting/quick-start.md")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    content = QS_FRONT.format(title=title, description=desc) + body + "\n"
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    count += 1
    print(f"  qs/{lang}")

print(f"Done — {count} quick-start files written")
