#!/usr/bin/env python3
"""Translate 5 cloud-deployment files into 35 languages."""
import os

BASE = "/Volumes/ExDisk/rtLab/webapp/doc.rtsurvey.com/content"
LANGUAGES = [
    "ar","bg","cs","da","de","el","es","fi","fr","hi",
    "hu","id","it","ja","km","ko","lt","lv","nb","nl",
    "pl","pt","pt-br","ru","sk","sq","sr","sv","te","th",
    "tr","uk","vi","zh-hans","zh-hant"
]

def frontmatter(weight, title, date, lastmod, icon, desc):
    return f"""---
weight: {weight}
title: "{title}"
date: "{date}"
lastmod: "{lastmod}"
draft: false
author: "rtSurvey"
icon: "{icon}"
toc: true
description: "{desc}"
---"""

def write(rel, lang, fm, body):
    path = os.path.join(BASE, lang, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(fm + "\n\n" + body.rstrip() + "\n")

# ═══════════════════════════════════════════════════════════════
# cloud-deployment/_index.md
# ═══════════════════════════════════════════════════════════════
INDEX_REL = "docs/getting-started/self-hosting/cloud-deployment/_index.md"
INDEX_DATE = "2026-03-16T00:00:00+07:00"

INDEX_TITLES = {
    "ar":"النشر السحابي","bg":"Облачно разгръщане","cs":"Cloudové nasazení",
    "da":"Skyinstallation","de":"Cloud-Bereitstellung","el":"Ανάπτυξη σε Cloud",
    "es":"Implementación en la nube","fi":"Pilvikäyttöönotto","fr":"Déploiement cloud",
    "hi":"क्लाउड परिनियोजन","hu":"Felhős telepítés","id":"Penerapan Cloud",
    "it":"Distribuzione cloud","ja":"クラウドデプロイ","km":"ការដំឡើងពន្លក",
    "ko":"클라우드 배포","lt":"Debesų diegimas","lv":"Mākoņdatošanas izvietošana",
    "nb":"Skydistribusjon","nl":"Cloud-implementatie","pl":"Wdrożenie w chmurze",
    "pt":"Implementação na nuvem","pt-br":"Implantação em nuvem","ru":"Облачное развёртывание",
    "sk":"Cloudové nasadenie","sq":"Vendosja në cloud","sr":"Облачно распоређивање",
    "sv":"Molndriftsättning","te":"క్లౌడ్ విన్యాసం","th":"การติดตั้งบนคลาวด์",
    "tr":"Bulut Dağıtımı","uk":"Хмарне розгортання","vi":"Triển khai đám mây",
    "zh-hans":"云部署","zh-hant":"雲端部署",
}
INDEX_DESCS = {
    "ar":"نشر rtCloud على مزودي السحابة الرئيسيين باستخدام سكريبتات آلية لـ DigitalOcean و AWS EC2 و Google Cloud و Linode.",
    "bg":"Разгръщане на rtCloud при основни облачни доставчици с автоматизирани скриптове за DigitalOcean, AWS EC2, Google Cloud и Linode.",
    "cs":"Nasazení rtCloud u hlavních poskytovatelů cloudu pomocí automatizovaných skriptů pro DigitalOcean, AWS EC2, Google Cloud a Linode.",
    "da":"Installer rtCloud hos store cloududbydere med automatiserede scripts til DigitalOcean, AWS EC2, Google Cloud og Linode.",
    "de":"rtCloud bei großen Cloud-Anbietern mit automatisierten Skripten für DigitalOcean, AWS EC2, Google Cloud und Linode bereitstellen.",
    "el":"Ανάπτυξη rtCloud σε μεγάλους παρόχους cloud με αυτοματοποιημένα scripts για DigitalOcean, AWS EC2, Google Cloud και Linode.",
    "es":"Implemente rtCloud en los principales proveedores de nube con scripts automatizados para DigitalOcean, AWS EC2, Google Cloud y Linode.",
    "fi":"Ota rtCloud käyttöön suurimmilla pilvialustoilla automaattisilla skripteillä DigitalOcean, AWS EC2, Google Cloud ja Linode -palveluihin.",
    "fr":"Déployez rtCloud chez les principaux fournisseurs cloud avec des scripts automatisés pour DigitalOcean, AWS EC2, Google Cloud et Linode.",
    "hi":"DigitalOcean, AWS EC2, Google Cloud और Linode के लिए स्वचालित स्क्रिप्ट के साथ प्रमुख क्लाउड प्रदाताओं पर rtCloud तैनात करें।",
    "hu":"Az rtCloud telepítése fő felhőszolgáltatóknál automatizált szkriptekkel DigitalOcean, AWS EC2, Google Cloud és Linode számára.",
    "id":"Terapkan rtCloud ke penyedia cloud utama dengan skrip otomatis untuk DigitalOcean, AWS EC2, Google Cloud, dan Linode.",
    "it":"Distribuire rtCloud sui principali provider cloud con script automatizzati per DigitalOcean, AWS EC2, Google Cloud e Linode.",
    "ja":"DigitalOcean、AWS EC2、Google Cloud、Linodeの自動化スクリプトで主要クラウドプロバイダーにrtCloudをデプロイします。",
    "km":"ដំឡើង rtCloud ទៅកាន់អ្នកផ្តល់ cloud ធំៗ ដោយប្រើស្ក្រីបដោយស្វ័យប្រវត្តិសម្រាប់ DigitalOcean, AWS EC2, Google Cloud និង Linode។",
    "ko":"DigitalOcean, AWS EC2, Google Cloud, Linode를 위한 자동화 스크립트로 주요 클라우드 공급자에 rtCloud를 배포합니다.",
    "lt":"Diekite rtCloud pas pagrindinius debesų tiekėjus naudodami automatizuotus skriptus DigitalOcean, AWS EC2, Google Cloud ir Linode.",
    "lv":"Izvietojiet rtCloud pie galvenajiem mākoņpakalpojumu sniedzējiem ar automatizētiem skriptiem DigitalOcean, AWS EC2, Google Cloud un Linode.",
    "nb":"Distribuer rtCloud hos store skyleverandører med automatiserte skript for DigitalOcean, AWS EC2, Google Cloud og Linode.",
    "nl":"Implementeer rtCloud bij grote cloudproviders met geautomatiseerde scripts voor DigitalOcean, AWS EC2, Google Cloud en Linode.",
    "pl":"Wdrożenie rtCloud u głównych dostawców chmury za pomocą zautomatyzowanych skryptów dla DigitalOcean, AWS EC2, Google Cloud i Linode.",
    "pt":"Implemente rtCloud nos principais fornecedores de nuvem com scripts automatizados para DigitalOcean, AWS EC2, Google Cloud e Linode.",
    "pt-br":"Implante rtCloud nos principais provedores de nuvem com scripts automatizados para DigitalOcean, AWS EC2, Google Cloud e Linode.",
    "ru":"Развёртывание rtCloud у крупных облачных провайдеров с автоматизированными скриптами для DigitalOcean, AWS EC2, Google Cloud и Linode.",
    "sk":"Nasaďte rtCloud u hlavných poskytovateľov cloudu pomocou automatizovaných skriptov pre DigitalOcean, AWS EC2, Google Cloud a Linode.",
    "sq":"Vendosni rtCloud tek ofruesit kryesorë të cloud me skripte të automatizuara për DigitalOcean, AWS EC2, Google Cloud dhe Linode.",
    "sr":"Распоредите rtCloud код главних провајдера облака са аутоматизованим скриптовима за DigitalOcean, AWS EC2, Google Cloud и Linode.",
    "sv":"Driftsätt rtCloud hos stora molnleverantörer med automatiserade skript för DigitalOcean, AWS EC2, Google Cloud och Linode.",
    "te":"DigitalOcean, AWS EC2, Google Cloud మరియు Linode కోసం స్వయంచాలక స్క్రిప్ట్‌లతో ప్రధాన క్లౌడ్ ప్రొవైడర్‌లలో rtCloud విన్యసించండి.",
    "th":"ติดตั้ง rtCloud บนผู้ให้บริการคลาวด์หลักด้วยสคริปต์อัตโนมัติสำหรับ DigitalOcean, AWS EC2, Google Cloud และ Linode",
    "tr":"DigitalOcean, AWS EC2, Google Cloud ve Linode için otomatik scriptlerle rtCloud'u büyük bulut sağlayıcılarına dağıtın.",
    "uk":"Розгортання rtCloud у великих хмарних провайдерів за допомогою автоматизованих скриптів для DigitalOcean, AWS EC2, Google Cloud та Linode.",
    "vi":"Triển khai rtCloud trên các nhà cung cấp đám mây lớn với các script tự động cho DigitalOcean, AWS EC2, Google Cloud và Linode.",
    "zh-hans":"使用自动化脚本将 rtCloud 部署到 DigitalOcean、AWS EC2、Google Cloud 和 Linode 等主要云服务商。",
    "zh-hant":"使用自動化腳本將 rtCloud 部署到 DigitalOcean、AWS EC2、Google Cloud 和 Linode 等主要雲服務商。",
}

INDEX_INTRO = {
    "ar": "يتضمن مستودع النشر سكريبتات توفير آلية لمزودي السحابة الرئيسيين. يعمل كل سكريبت عند أول تشغيل لخادم Ubuntu 22.04 LTS جديد ويقوم بإعداد كامل غير مراقب:",
    "bg": "Хранилището за разгръщане включва автоматизирани скриптове за провизиране при основни облачни доставчици. Всеки скрипт се изпълнява при първото стартиране на нов сървър Ubuntu 22.04 LTS и извършва напълно автоматична настройка:",
    "cs": "Repozitář nasazení obsahuje automatizované provisioningové skripty pro hlavní cloudové poskytovatele. Každý skript se spustí při prvním spuštění nového serveru Ubuntu 22.04 LTS a provede plně bezobslužné nastavení:",
    "da": "Installationslageret indeholder automatiserede provisioneringsscripts til større cloududbydere. Hvert script kører ved første opstart af en ny Ubuntu 22.04 LTS-server og udfører en fuldt automatiseret opsætning:",
    "de": "Das Bereitstellungs-Repository enthält automatisierte Provisionierungsskripte für wichtige Cloud-Anbieter. Jedes Skript wird beim ersten Start eines neuen Ubuntu 22.04 LTS-Servers ausgeführt und führt eine vollständig unbeaufsichtigte Einrichtung durch:",
    "el": "Το αποθετήριο ανάπτυξης περιλαμβάνει αυτοματοποιημένα σκριπτ παροχής για τους κύριους παρόχους cloud. Κάθε σκριπτ εκτελείται κατά την πρώτη εκκίνηση ενός νέου διακομιστή Ubuntu 22.04 LTS και πραγματοποιεί πλήρως αυτόματη ρύθμιση:",
    "es": "El repositorio de implementación incluye scripts de aprovisionamiento automatizados para los principales proveedores de nube. Cada script se ejecuta en el primer arranque de un servidor Ubuntu 22.04 LTS nuevo y realiza una configuración completamente desatendida:",
    "fi": "Käyttöönottohakemisto sisältää automatisoidut provisiointiskriptit pääpilvialustoille. Jokainen skripti suoritetaan uuden Ubuntu 22.04 LTS -palvelimen ensimmäisellä käynnistyksellä ja suorittaa täysin valvomattoman asennuksen:",
    "fr": "Le dépôt de déploiement inclut des scripts de provisionnement automatisés pour les principaux fournisseurs cloud. Chaque script s'exécute au premier démarrage d'un nouveau serveur Ubuntu 22.04 LTS et effectue une installation entièrement automatique :",
    "hi": "डिप्लॉयमेंट रिपॉजिटरी में प्रमुख क्लाउड प्रदाताओं के लिए स्वचालित प्रोविजनिंग स्क्रिप्ट शामिल हैं। प्रत्येक स्क्रिप्ट नए Ubuntu 22.04 LTS सर्वर के पहले बूट पर चलती है और पूरी तरह से अनअटेंडेड सेटअप करती है:",
    "hu": "A telepítési tár automatizált provisionálási szkripteket tartalmaz a főbb felhőszolgáltatókhoz. Minden szkript egy új Ubuntu 22.04 LTS szerver első indításakor fut és teljesen felügyelet nélküli beállítást végez:",
    "id": "Repositori deployment menyertakan skrip provisi otomatis untuk penyedia cloud utama. Setiap skrip berjalan saat boot pertama server Ubuntu 22.04 LTS baru dan melakukan pengaturan yang sepenuhnya otomatis:",
    "it": "Il repository di distribuzione include script di provisioning automatizzati per i principali provider cloud. Ogni script viene eseguito al primo avvio di un nuovo server Ubuntu 22.04 LTS ed esegue una configurazione completamente automatica:",
    "ja": "デプロイメントリポジトリには、主要なクラウドプロバイダー向けの自動プロビジョニングスクリプトが含まれています。各スクリプトは新しいUbuntu 22.04 LTSサーバーの初回起動時に実行され、完全に無人のセットアップを実行します：",
    "km": "ឃ្លាំដំណើការដំឡើងមានស្ក្រីបផ្តល់ការគ្រប់គ្រងដោយស្វ័យប្រវត្តិសម្រាប់អ្នកផ្តល់ cloud ធំៗ។ ស្ក្រីបនីមួយៗដំណើរការនៅពេលចាប់ផ្ដើមដំបូងនៃម៉ាស៊ីន Ubuntu 22.04 LTS ថ្មី ហើយធ្វើការដំឡើងដោយស្វ័យប្រវត្តិ:",
    "ko": "배포 저장소에는 주요 클라우드 공급자를 위한 자동화된 프로비저닝 스크립트가 포함되어 있습니다. 각 스크립트는 새로운 Ubuntu 22.04 LTS 서버의 첫 번째 부팅 시 실행되며 완전 자동 설정을 수행합니다:",
    "lt": "Diegimo saugykla apima automatizuotus provisionavimo skriptus pagrindiniams debesų tiekėjams. Kiekvienas skriptas vykdomas naujo Ubuntu 22.04 LTS serverio pirmojo paleidimo metu ir atlieka visiškai automatinį diegimą:",
    "lv": "Izvietošanas repozitorijs ietver automatizētus nodrošināšanas skriptus galvenajiem mākoņpakalpojumu sniedzējiem. Katrs skripts darbojas jauna Ubuntu 22.04 LTS servera pirmajā palaišanā un veic pilnīgi automatizētu iestatīšanu:",
    "nb": "Distribusjonslageret inkluderer automatiserte provisioneringsscripts for store skyleverandører. Hvert script kjører ved første oppstart av en ny Ubuntu 22.04 LTS-server og utfører en fullstendig automatisert oppsett:",
    "nl": "Het implementatie-repository bevat geautomatiseerde provisioningscripts voor grote cloudproviders. Elk script wordt uitgevoerd bij de eerste start van een nieuwe Ubuntu 22.04 LTS-server en voert een volledig onbeheerde installatie uit:",
    "pl": "Repozytorium wdrożenia zawiera zautomatyzowane skrypty provisioningowe dla głównych dostawców chmury. Każdy skrypt uruchamia się przy pierwszym rozruchu nowego serwera Ubuntu 22.04 LTS i przeprowadza w pełni bezobsługową konfigurację:",
    "pt": "O repositório de implementação inclui scripts de aprovisionamento automatizados para os principais fornecedores de nuvem. Cada script é executado no primeiro arranque de um novo servidor Ubuntu 22.04 LTS e realiza uma configuração completamente automática:",
    "pt-br": "O repositório de implantação inclui scripts de provisionamento automatizados para os principais provedores de nuvem. Cada script é executado no primeiro boot de um novo servidor Ubuntu 22.04 LTS e realiza uma configuração completamente automatizada:",
    "ru": "Репозиторий развёртывания включает автоматизированные сценарии провизионирования для основных облачных провайдеров. Каждый скрипт запускается при первой загрузке нового сервера Ubuntu 22.04 LTS и выполняет полностью автоматическую настройку:",
    "sk": "Úložisko nasadenia obsahuje automatizované provisioningové skripty pre hlavných poskytovateľov cloudu. Každý skript sa spustí pri prvom štarte nového servera Ubuntu 22.04 LTS a vykoná plne automatické nastavenie:",
    "sq": "Depoja e vendosjes përfshin skripte automatike të provizionimit për ofruesit kryesorë të cloud. Çdo skript ekzekutohet në nisjen e parë të një serveri të ri Ubuntu 22.04 LTS dhe kryen një konfigurim plotësisht automatik:",
    "sr": "Спремиште за распоређивање укључује аутоматизоване скриптове за провизионирање за главне провајдере облака. Сваки скрипт се покреће при првом подизању новог Ubuntu 22.04 LTS сервера и врши потпуно аутоматску поставку:",
    "sv": "Driftsättningsrepositoryt innehåller automatiserade provisioningsskript för stora molnleverantörer. Varje skript körs vid den första uppstarten av en ny Ubuntu 22.04 LTS-server och utför en helt obevakad installation:",
    "te": "విన్యాస రిపోజిటరీలో ప్రధాన క్లౌడ్ ప్రొవైడర్‌ల కోసం స్వయంచాలక ప్రొవిజనింగ్ స్క్రిప్ట్‌లు ఉన్నాయి. ప్రతి స్క్రిప్ట్ కొత్త Ubuntu 22.04 LTS సర్వర్ యొక్క మొదటి బూట్‌లో అమలవుతుంది మరియు పూర్తిగా స్వయంచాలక సెటప్ చేస్తుంది:",
    "th": "ที่เก็บการติดตั้งประกอบด้วยสคริปต์จัดเตรียมอัตโนมัติสำหรับผู้ให้บริการคลาวด์หลัก สคริปต์แต่ละตัวทำงานในการบูตครั้งแรกของเซิร์ฟเวอร์ Ubuntu 22.04 LTS ใหม่ และดำเนินการตั้งค่าโดยอัตโนมัติ:",
    "tr": "Dağıtım deposu, büyük bulut sağlayıcıları için otomatik sağlama scriptleri içerir. Her script, yeni bir Ubuntu 22.04 LTS sunucusunun ilk önyüklemesinde çalışır ve tamamen katılımsız bir kurulum gerçekleştirir:",
    "uk": "Репозиторій розгортання включає автоматизовані скрипти провізіонування для основних хмарних провайдерів. Кожен скрипт запускається при першому завантаженні нового сервера Ubuntu 22.04 LTS і виконує повністю автоматичне налаштування:",
    "vi": "Kho lưu trữ triển khai bao gồm các script cung cấp tự động cho các nhà cung cấp đám mây lớn. Mỗi script chạy khi khởi động lần đầu của máy chủ Ubuntu 22.04 LTS mới và thực hiện thiết lập hoàn toàn tự động:",
    "zh-hans": "部署存储库包含针对主要云提供商的自动化配置脚本。每个脚本在新的 Ubuntu 22.04 LTS 服务器首次启动时运行，并执行完全无人值守的设置：",
    "zh-hant": "部署存儲庫包含針對主要雲服務商的自動化配置腳本。每個腳本在新的 Ubuntu 22.04 LTS 伺服器首次啟動時運行，並執行完全無人值守的設定：",
}

INDEX_BODY_TEMPLATE = """{intro}

- Installs Docker and Docker Compose
- Generates secure random passwords for all internal services
- Writes `docker-compose.production.yml` and `.env`
- Configures Nginx as a reverse proxy
- Obtains a free TLS certificate from Let's Encrypt (auto-retries until DNS resolves)
- Configures the UFW firewall
- Optionally deploys the embedded Keycloak SSO server
- Outputs a full deployment summary with all credentials

Setup completes in **5–10 minutes** on a standard instance.

---

## Choosing a Script

There are multiple script variants depending on your cloud provider and SSO setup:

| Script | Provider | SSO Mode | Best For |
|--------|----------|----------|----------|
| `digitalocean-droplet-keycloak-embed.sh` | DigitalOcean | Built-in Keycloak | Simple, self-contained SSO |
| `digitalocean-droplet.sh` | DigitalOcean | Keycloak or External OIDC | Full control |
| `linode-stackscript-keycloak-embed.sh` | Linode | Built-in Keycloak | Form-based setup, simplest |
| `linode-stackscript-oidc.sh` | Linode | External OIDC only | Existing identity provider |
| `linode-stackscript.sh` | Linode | Keycloak or External OIDC | Full control |
| `aws-ec2.sh` | AWS EC2 | Keycloak or External OIDC | AWS deployments |
| `gcp-compute.sh` | Google Cloud | Keycloak or External OIDC | GCP deployments |

> **Recommended for most users:** Use the `keycloak-embed` variant. It includes a built-in Keycloak identity server and requires the fewest configuration fields.

---

## Server Sizing Guide

| Use Case | RAM | Disk | Example |
|----------|-----|------|---------|
| Evaluation / development | 2 GB | 25 GB | DO Basic $18/mo, t3.small, e2-small |
| Small team (< 50 users) | 4 GB | 40 GB | DO Basic $24/mo, t3.medium, e2-medium |
| Production (> 50 users) | 8 GB | 80 GB | DO General $48/mo, t3.large, n2-standard-2 |

> Embedded Keycloak requires at least **4 GB RAM**. Use 2 GB only for evaluation without Keycloak.

---

## DNS Setup

All scripts require a domain with an **A record pointing to your server's IP** before Let's Encrypt can issue a certificate.

The script prints your server IP early in the setup process:

```
============================================================
 Server IP : 139.162.51.85
 Add this DNS A record now if you haven't already:
   myapp.example.com  ->  139.162.51.85
 The script will retry Certbot every 60s until DNS resolves.
============================================================
```

The script **automatically retries** Let's Encrypt every 60 seconds for up to 1 hour. Just add the DNS record and wait — no restart needed.

> **Rate limit:** Let's Encrypt allows a maximum of **5 certificates per domain per 7 days**. Avoid deploying and destroying servers repeatedly with the same domain. If you hit the limit, the script will display a `retry after` timestamp and stop immediately.

---

## Post-Deployment Checklist

- [ ] App opens at `https://your-domain.com`
- [ ] Log in with `admin` and the password you configured
- [ ] All containers are healthy: `docker compose -f /opt/rtcloud/docker-compose.production.yml ps`
- [ ] Let's Encrypt renewal works: `certbot renew --dry-run`
- [ ] MySQL port 3306 is **not** exposed: `ufw status`
- [ ] Set up a daily database backup (see [Maintenance](../maintenance))

---

## Troubleshooting

### Check the full setup log

```bash
# Linode
tail -200 /var/log/stackscript.log

# DigitalOcean / AWS / GCP
tail -200 /var/log/rtcloud-setup.log
```

### Let's Encrypt rate limit

If you see `too many certificates` in the log, you have hit the 5 certificates/7 days limit. The log shows the exact retry time:

```
[SSL] ERROR: Let's Encrypt rate limit hit. retry after 2026-03-15 16:22 UTC.
```

Wait until that time, then redeploy.

### Keycloak stays unhealthy

Ensure the server has at least 4 GB RAM, then check logs:

```bash
docker logs rtcloud-keycloak --tail 50
free -h
```

### SSL config not applied after certbot

If the certificate was issued but Nginx still shows HTTP only, check the log for the error line and manually reload Nginx:

```bash
nginx -t && systemctl reload nginx
```
"""

# ═══════════════════════════════════════════════════════════════
# linode.md
# ═══════════════════════════════════════════════════════════════
LINODE_REL = "docs/getting-started/self-hosting/cloud-deployment/linode.md"
LINODE_DATE = "2026-03-16T00:00:00+07:00"
LINODE_LASTMOD = "2026-04-01T00:00:00+07:00"

LINODE_TITLES = {
    "ar":"Linode (Akamai Cloud)","bg":"Linode (Akamai Cloud)","cs":"Linode (Akamai Cloud)",
    "da":"Linode (Akamai Cloud)","de":"Linode (Akamai Cloud)","el":"Linode (Akamai Cloud)",
    "es":"Linode (Akamai Cloud)","fi":"Linode (Akamai Cloud)","fr":"Linode (Akamai Cloud)",
    "hi":"Linode (Akamai Cloud)","hu":"Linode (Akamai Cloud)","id":"Linode (Akamai Cloud)",
    "it":"Linode (Akamai Cloud)","ja":"Linode (Akamai Cloud)","km":"Linode (Akamai Cloud)",
    "ko":"Linode (Akamai Cloud)","lt":"Linode (Akamai Cloud)","lv":"Linode (Akamai Cloud)",
    "nb":"Linode (Akamai Cloud)","nl":"Linode (Akamai Cloud)","pl":"Linode (Akamai Cloud)",
    "pt":"Linode (Akamai Cloud)","pt-br":"Linode (Akamai Cloud)","ru":"Linode (Akamai Cloud)",
    "sk":"Linode (Akamai Cloud)","sq":"Linode (Akamai Cloud)","sr":"Linode (Akamai Cloud)",
    "sv":"Linode (Akamai Cloud)","te":"Linode (Akamai Cloud)","th":"Linode (Akamai Cloud)",
    "tr":"Linode (Akamai Cloud)","uk":"Linode (Akamai Cloud)","vi":"Linode (Akamai Cloud)",
    "zh-hans":"Linode (Akamai Cloud)","zh-hant":"Linode (Akamai Cloud)",
}
LINODE_DESCS = {
    "ar":"نشر rtCloud على Linode باستخدام StackScript. لا حاجة للتكوين — فقط أنشئ الخادم واتبع خطوات ما بعد النشر.",
    "bg":"Разгръщане на rtCloud в Linode с помощта на StackScript. Не е необходима конфигурация — просто създайте сървъра и следвайте стъпките след разгръщането.",
    "cs":"Nasaďte rtCloud na Linode pomocí StackScriptu. Není potřeba žádná konfigurace — stačí vytvořit server a postupovat podle kroků po nasazení.",
    "da":"Installer rtCloud på Linode ved hjælp af et StackScript. Ingen konfiguration nødvendig — opret bare serveren og følg trinene efter installationen.",
    "de":"Stellen Sie rtCloud auf Linode mit einem StackScript bereit. Keine Konfiguration erforderlich — erstellen Sie einfach den Server und folgen Sie den Schritten nach der Bereitstellung.",
    "el":"Αναπτύξτε το rtCloud στο Linode χρησιμοποιώντας StackScript. Δεν απαιτείται διαμόρφωση — απλώς δημιουργήστε τον διακομιστή και ακολουθήστε τα βήματα μετά την ανάπτυξη.",
    "es":"Implemente rtCloud en Linode usando un StackScript. No se necesita configuración — simplemente cree el servidor y siga los pasos posteriores a la implementación.",
    "fi":"Ota rtCloud käyttöön Linodessa StackScriptin avulla. Konfigurointia ei tarvita — luo vain palvelin ja seuraa käyttöönoton jälkeisiä vaiheita.",
    "fr":"Déployez rtCloud sur Linode à l'aide d'un StackScript. Aucune configuration nécessaire — créez simplement le serveur et suivez les étapes post-déploiement.",
    "hi":"StackScript का उपयोग करके Linode पर rtCloud तैनात करें। कोई कॉन्फ़िगरेशन नहीं — बस सर्वर बनाएं और तैनाती के बाद के चरणों का पालन करें।",
    "hu":"Telepítse az rtCloudot Linodeon StackScript segítségével. Nincs szükség konfigurációra — csak hozza létre a szervert és kövesse a telepítés utáni lépéseket.",
    "id":"Terapkan rtCloud di Linode menggunakan StackScript. Tidak perlu konfigurasi — cukup buat server dan ikuti langkah-langkah pasca-deployment.",
    "it":"Distribuire rtCloud su Linode utilizzando uno StackScript. Nessuna configurazione necessaria — basta creare il server e seguire i passaggi post-distribuzione.",
    "ja":"StackScriptを使用してLinodeにrtCloudをデプロイします。設定不要 — サーバーを作成してデプロイ後の手順に従うだけです。",
    "km":"ដំឡើង rtCloud នៅ Linode ដោយប្រើ StackScript។ មិនត្រូវការការកំណត់រចនាសម្ព័ន្ធ — គ្រាន់តែបង្កើតម៉ាស៊ីនបម្រើ ហើយធ្វើតាមជំហានក្រោយការដំឡើង។",
    "ko":"StackScript를 사용하여 Linode에 rtCloud를 배포합니다. 구성 불필요 — 서버를 만들고 배포 후 단계를 따르세요.",
    "lt":"Diekite rtCloud Linode naudodami StackScript. Nereikia konfigūravimo — tiesiog sukurkite serverį ir atlikite veiksmus po diegimo.",
    "lv":"Izvietojiet rtCloud Linode, izmantojot StackScript. Nav nepieciešama konfigurācija — vienkārši izveidojiet serveri un sekojiet pēc izvietošanas veicamajām darbībām.",
    "nb":"Distribuer rtCloud på Linode ved hjelp av et StackScript. Ingen konfigurasjon nødvendig — bare opprett serveren og følg trinnene etter distribusjon.",
    "nl":"Implementeer rtCloud op Linode met een StackScript. Geen configuratie nodig — maak gewoon de server aan en volg de stappen na de implementatie.",
    "pl":"Wdróż rtCloud na Linode za pomocą StackScript. Brak konfiguracji — po prostu utwórz serwer i postępuj zgodnie z krokami po wdrożeniu.",
    "pt":"Implemente rtCloud no Linode usando um StackScript. Não é necessária configuração — basta criar o servidor e seguir os passos pós-implementação.",
    "pt-br":"Implante rtCloud no Linode usando um StackScript. Sem necessidade de configuração — basta criar o servidor e seguir as etapas pós-implantação.",
    "ru":"Разверните rtCloud на Linode с помощью StackScript. Настройка не требуется — просто создайте сервер и следуйте шагам после развёртывания.",
    "sk":"Nasaďte rtCloud na Linode pomocou StackScript. Nie je potrebná žiadna konfigurácia — stačí vytvoriť server a postupovať podľa krokov po nasadení.",
    "sq":"Vendosni rtCloud në Linode duke përdorur StackScript. Nuk nevojitet konfigurim — thjesht krijoni serverin dhe ndiqni hapat pas vendosjes.",
    "sr":"Распоредите rtCloud на Linode-у користећи StackScript. Није потребна конфигурација — само направите сервер и пратите кораке после распоређивања.",
    "sv":"Driftsätt rtCloud på Linode med hjälp av ett StackScript. Ingen konfiguration behövs — skapa bara servern och följ stegen efter driftsättning.",
    "te":"StackScript ఉపయోగించి Linode లో rtCloud విన్యసించండి. కాన్ఫిగరేషన్ అవసరం లేదు — కేవలం సర్వర్ సృష్టించి విన్యాసం తర్వాత దశలు అనుసరించండి.",
    "th":"ติดตั้ง rtCloud บน Linode โดยใช้ StackScript ไม่ต้องกำหนดค่า — เพียงสร้างเซิร์ฟเวอร์และทำตามขั้นตอนหลังการติดตั้ง",
    "tr":"StackScript kullanarak rtCloud'u Linode üzerinde dağıtın. Yapılandırma gerekmez — sadece sunucuyu oluşturun ve dağıtım sonrası adımları takip edin.",
    "uk":"Розгорніть rtCloud на Linode за допомогою StackScript. Налаштування не потрібне — просто створіть сервер і дотримуйтесь кроків після розгортання.",
    "vi":"Triển khai rtCloud trên Linode bằng StackScript. Không cần cấu hình — chỉ cần tạo máy chủ và làm theo các bước sau khi triển khai.",
    "zh-hans":"使用 StackScript 在 Linode 上部署 rtCloud。无需配置 — 只需创建服务器并按照部署后步骤操作。",
    "zh-hant":"使用 StackScript 在 Linode 上部署 rtCloud。無需配置 — 只需建立伺服器並按照部署後步驟操作。",
}

# Linode body is mostly procedural — keep English, translate the intro step labels
LINODE_BODY = """## Step 1 — Launch the StackScript

**[Deploy rtSurvey on Linode →](https://cloud.linode.com/stackscripts/2049143)**

This opens the StackScript page in Linode Cloud Manager. Click **Deploy New Linode**.

---

## Step 2 — Fill in Linode's form

Fill in Linode's standard server creation form:

| Field | Recommended value |
|-------|------------------|
| **Image** | Ubuntu 22.04 LTS |
| **Region** | Closest to your users |
| **Plan** | Shared CPU 4 GB or larger |
| **Root Password** | Set a strong password |
| **Timezone** *(our only field)* | Your server timezone (default: `Asia/Ho_Chi_Minh`) |

Click **Create Linode** when done.

---

## Step 3 — Wait for setup to complete

The script runs automatically on first boot. It installs Docker, pulls the rtSurvey image, initialises the database, and starts all services. This takes **5–10 minutes**.

You can watch progress directly in **Linode Cloud Manager** — no SSH required:

1. Go to your [Linode dashboard](https://cloud.linode.com/linodes)
2. Click on your newly created Linode
3. Click **Launch LISH Console** (top right of the Linode detail page)

A browser terminal opens showing the live boot log — the **Weblish** tab works directly in your browser, no SSH client needed.

![Lish Console showing rtSurvey StackScript running](/img/first-login/lish-console.png)

Wait until you see:

```
============================================================
 rtSurvey deployment complete!
============================================================
 Server IP : <your-server-ip>

 App URL   : http://<your-server-ip>  (HTTP only until domain is set)
 Admin     : admin / admin
============================================================
```

The log also shows your server IP — you will need it for the next step.

---

## Step 4 — Set up SSL

Open your browser at `http://<server-ip>`. The app will redirect you to the SSL setup screen.

Follow the **[Set Up SSL guide →](../ssl-setup)** to configure HTTPS. The free **rtsurvey.com subdomain** is the fastest option — no DNS setup needed.

---

## Step 5 — First login

Once SSL is active, follow the **[First Login guide →](../first-login)** to access the admin account.

---

## Step 6 — Change the default password

All passwords default to `admin`. Change them immediately after your first login:

- **App admin password** — account settings inside the app
- **Keycloak admin** — accessible at `https://your-domain.com/auth/admin` (login: `admin` / `admin`)

---

## Troubleshooting

### Check the setup log

```bash
tail -200 /var/log/stackscript.log
```

### Check the SSL log

```bash
tail -200 /var/log/rtsurvey-ssl.log
```

### View container status

```bash
docker compose -f /opt/rtsurvey/docker-compose.production.yml ps
```
"""

# ═══════════════════════════════════════════════════════════════
# digitalocean.md
# ═══════════════════════════════════════════════════════════════
DO_REL = "docs/getting-started/self-hosting/cloud-deployment/digitalocean.md"
DO_DATE = "2026-03-16T00:00:00+07:00"
DO_LASTMOD = "2026-03-17T00:00:00+07:00"

DO_TITLES = {l: "DigitalOcean" for l in LANGUAGES}
DO_DESCS = {
    "ar":"نشر rtCloud على Droplet من DigitalOcean باستخدام سكريبتات بيانات المستخدم الآلية.",
    "bg":"Разгръщане на rtCloud на DigitalOcean Droplet с помощта на автоматизирани скриптове за потребителски данни.",
    "cs":"Nasaďte rtCloud na DigitalOcean Droplet pomocí automatizovaných skriptů uživatelských dat.",
    "da":"Installer rtCloud på en DigitalOcean Droplet ved hjælp af automatiserede user-data-scripts.",
    "de":"Stellen Sie rtCloud auf einem DigitalOcean Droplet mit automatisierten User-Data-Skripten bereit.",
    "el":"Αναπτύξτε rtCloud σε DigitalOcean Droplet χρησιμοποιώντας αυτοματοποιημένα scripts δεδομένων χρήστη.",
    "es":"Implemente rtCloud en un Droplet de DigitalOcean usando scripts de datos de usuario automatizados.",
    "fi":"Ota rtCloud käyttöön DigitalOcean Dropletissa automaattisilla käyttäjätietoskripteillä.",
    "fr":"Déployez rtCloud sur un Droplet DigitalOcean à l'aide de scripts de données utilisateur automatisés.",
    "hi":"स्वचालित यूजर-डेटा स्क्रिप्ट का उपयोग करके DigitalOcean Droplet पर rtCloud तैनात करें।",
    "hu":"Telepítse az rtCloudot egy DigitalOcean Dropletbe automatizált felhasználói adatok szkriptekkel.",
    "id":"Terapkan rtCloud di DigitalOcean Droplet menggunakan skrip user-data otomatis.",
    "it":"Distribuire rtCloud su un Droplet DigitalOcean usando script di dati utente automatizzati.",
    "ja":"自動化されたユーザーデータスクリプトを使用してDigitalOcean DropletにrtCloudをデプロイします。",
    "km":"ដំឡើង rtCloud នៅ DigitalOcean Droplet ដោយប្រើស្ក្រីប user-data ដោយស្វ័យប្រវត្តិ។",
    "ko":"자동화된 사용자 데이터 스크립트를 사용하여 DigitalOcean Droplet에 rtCloud를 배포합니다.",
    "lt":"Diekite rtCloud DigitalOcean Droplet naudodami automatizuotus user-data skriptus.",
    "lv":"Izvietojiet rtCloud DigitalOcean Droplet, izmantojot automatizētus lietotāja datu skriptus.",
    "nb":"Distribuer rtCloud på en DigitalOcean Droplet ved hjelp av automatiserte user-data-scripts.",
    "nl":"Implementeer rtCloud op een DigitalOcean Droplet met behulp van geautomatiseerde user-data-scripts.",
    "pl":"Wdróż rtCloud na DigitalOcean Droplet za pomocą zautomatyzowanych skryptów danych użytkownika.",
    "pt":"Implemente rtCloud num Droplet DigitalOcean usando scripts de dados de utilizador automatizados.",
    "pt-br":"Implante rtCloud em um Droplet DigitalOcean usando scripts de dados de usuário automatizados.",
    "ru":"Разверните rtCloud на DigitalOcean Droplet с помощью автоматизированных пользовательских данных.",
    "sk":"Nasaďte rtCloud na DigitalOcean Droplet pomocou automatizovaných user-data skriptov.",
    "sq":"Vendosni rtCloud në DigitalOcean Droplet duke përdorur skripte automatike të të dhënave të përdoruesit.",
    "sr":"Распоредите rtCloud на DigitalOcean Droplet користећи аутоматизоване user-data скриптове.",
    "sv":"Driftsätt rtCloud på en DigitalOcean Droplet med automatiserade user-data-skript.",
    "te":"స్వయంచాలక యూజర్-డేటా స్క్రిప్ట్‌లు ఉపయోగించి DigitalOcean Droplet లో rtCloud విన్యసించండి.",
    "th":"ติดตั้ง rtCloud บน DigitalOcean Droplet โดยใช้สคริปต์ user-data อัตโนมัติ",
    "tr":"Otomatik kullanıcı verisi scriptleri kullanarak rtCloud'u bir DigitalOcean Droplet üzerinde dağıtın.",
    "uk":"Розгорніть rtCloud на DigitalOcean Droplet за допомогою автоматизованих сценаріїв даних користувача.",
    "vi":"Triển khai rtCloud trên DigitalOcean Droplet bằng các script dữ liệu người dùng tự động.",
    "zh-hans":"使用自动化用户数据脚本在 DigitalOcean Droplet 上部署 rtCloud。",
    "zh-hant":"使用自動化用戶數據腳本在 DigitalOcean Droplet 上部署 rtCloud。",
}

DO_BODY = """DigitalOcean uses **User Data** scripts that run automatically on first boot. You fill in the configuration variables at the top of the script, then paste the entire script when creating a Droplet.

> Unlike Linode StackScripts, DigitalOcean has no form UI — you must edit the script directly before pasting.

**Download script:** [digitalocean-droplet-keycloak-embed.sh](/scripts/digitalocean-droplet-keycloak-embed.sh)

---

## Embedded Keycloak (Recommended)

Use `digitalocean-droplet-keycloak-embed.sh` for the simplest setup with built-in SSO.

### Step 1 — Fill in the configuration

Open the script and edit the `CONFIGURATION` block at the top:

```bash
# --- Required ---
PROJECT_ID="rtsurvey"                  # Unique identifier for your project (no spaces)
ADMIN_PASSWORD="admin"                 # Password for app admin and Keycloak — change after first login

# --- Domain + SSL ---
DOMAIN="myapp.example.com"            # Your domain — DNS A record must point here
PROJECT_URL=""                         # Leave blank unless behind Cloudflare/proxy
LETSENCRYPT_EMAIL="admin@example.com" # Email for Let's Encrypt notifications

# --- Optional ---
STATA_ENABLED="false"
TZ="Asia/Ho_Chi_Minh"
```

| Field | Required | Description |
|-------|----------|-------------|
| `PROJECT_ID` | Yes | Used as database name and Keycloak client ID. Lowercase, no spaces. |
| `ADMIN_PASSWORD` | No | Password for app admin login and Keycloak admin console. Defaults to `admin` — **change after first login**. |
| `DOMAIN` | Yes | Your domain name. DNS A record must point to the Droplet IP. |
| `LETSENCRYPT_EMAIL` | Yes | Email address for Let's Encrypt certificate notifications. |
| `PROJECT_URL` | No | Override the public URL. Leave blank to use `DOMAIN`. Useful behind Cloudflare. |

> **Security:** All passwords default to `admin`. Change them immediately after your first login.

### Step 2 — Create a Droplet

In the [DigitalOcean control panel](https://cloud.digitalocean.com):

1. Click **Create** → **Droplets**
2. Choose **Ubuntu 22.04 LTS** as the image
3. Select **Basic, 4 GB RAM / 2 vCPUs** or larger
4. Scroll to **Advanced Options** → check **Add Initialization scripts**
5. Paste the full script content into the text area
6. Click **Create Droplet**

### Step 3 — Add the DNS record

While the Droplet boots, add an **A record** in your DNS provider:

```
Type  : A
Name  : myapp          (or @ for root domain)
Value : <droplet-ip>
TTL   : 300
```

### Step 4 — Monitor progress

SSH into the Droplet and watch the log:

```bash
ssh root@<droplet-ip>
tail -f /var/log/rtcloud-setup.log
```

The script prints your server IP near the start — add the DNS record as soon as you see it.

### Step 5 — Access the app

When setup completes, the log shows a summary:

```
============================================================
 rtCloud deployment complete! (Embedded Keycloak)
============================================================
 App URL   : https://myapp.example.com
 Admin     : admin / admin
 Keycloak  : https://myapp.example.com/auth/admin

 !! SECURITY: All passwords default to 'admin'.
    Change them immediately after first login.
============================================================
```

Open `https://myapp.example.com` in your browser and log in with username `admin` and password `admin`.

> **Change your password** immediately after login via **Settings** in the top-right menu.

---

## After Deployment

### Change a password

SSH into the Droplet, edit `.env`, and restart the affected container:

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Update the domain

If you assign a different domain after deployment, update `PROJECT_URL` in `.env`:

```bash
nano /opt/rtcloud/.env   # update PROJECT_URL=
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### View all containers

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```
"""

# ═══════════════════════════════════════════════════════════════
# aws.md
# ═══════════════════════════════════════════════════════════════
AWS_REL = "docs/getting-started/self-hosting/cloud-deployment/aws.md"
AWS_DATE = "2026-03-16T00:00:00+07:00"

AWS_TITLES = {l: "AWS EC2" for l in LANGUAGES}
AWS_DESCS = {
    "ar":"نشر rtCloud على مثيل AWS EC2 باستخدام سكريبت بيانات مستخدم aws-ec2.sh.",
    "bg":"Разгръщане на rtCloud на AWS EC2 инстанция с помощта на user data скрипта aws-ec2.sh.",
    "cs":"Nasazení rtCloud na instanci AWS EC2 pomocí user data skriptu aws-ec2.sh.",
    "da":"Installer rtCloud på en AWS EC2-instans ved hjælp af user data-scriptet aws-ec2.sh.",
    "de":"rtCloud auf einer AWS EC2-Instanz mit dem User-Data-Skript aws-ec2.sh bereitstellen.",
    "el":"Ανάπτυξη rtCloud σε AWS EC2 instance χρησιμοποιώντας το script δεδομένων χρήστη aws-ec2.sh.",
    "es":"Implemente rtCloud en una instancia de AWS EC2 usando el script de datos de usuario aws-ec2.sh.",
    "fi":"Ota rtCloud käyttöön AWS EC2 -instanssissa käyttämällä user data -skriptiä aws-ec2.sh.",
    "fr":"Déployez rtCloud sur une instance AWS EC2 à l'aide du script de données utilisateur aws-ec2.sh.",
    "hi":"aws-ec2.sh यूजर डेटा स्क्रिप्ट का उपयोग करके AWS EC2 इंस्टेंस पर rtCloud तैनात करें।",
    "hu":"Telepítse az rtCloudot AWS EC2 példányra az aws-ec2.sh felhasználói adatok szkripttel.",
    "id":"Terapkan rtCloud pada instans AWS EC2 menggunakan skrip user data aws-ec2.sh.",
    "it":"Distribuire rtCloud su un'istanza AWS EC2 utilizzando lo script di dati utente aws-ec2.sh.",
    "ja":"aws-ec2.shユーザーデータスクリプトを使用してAWS EC2インスタンスにrtCloudをデプロイします。",
    "km":"ដំឡើង rtCloud នៅ AWS EC2 instance ដោយប្រើស្ក្រីប user data aws-ec2.sh ។",
    "ko":"aws-ec2.sh 사용자 데이터 스크립트를 사용하여 AWS EC2 인스턴스에 rtCloud를 배포합니다.",
    "lt":"Diekite rtCloud AWS EC2 egzemplioriuje naudodami user data skriptą aws-ec2.sh.",
    "lv":"Izvietojiet rtCloud AWS EC2 instancē, izmantojot lietotāja datu skriptu aws-ec2.sh.",
    "nb":"Distribuer rtCloud på en AWS EC2-instans ved hjelp av user data-scriptet aws-ec2.sh.",
    "nl":"Implementeer rtCloud op een AWS EC2-instantie met behulp van het user data-script aws-ec2.sh.",
    "pl":"Wdróż rtCloud na instancji AWS EC2 za pomocą skryptu danych użytkownika aws-ec2.sh.",
    "pt":"Implemente rtCloud numa instância AWS EC2 usando o script de dados de utilizador aws-ec2.sh.",
    "pt-br":"Implante rtCloud em uma instância AWS EC2 usando o script de dados de usuário aws-ec2.sh.",
    "ru":"Разверните rtCloud на экземпляре AWS EC2 с помощью скрипта пользовательских данных aws-ec2.sh.",
    "sk":"Nasaďte rtCloud na AWS EC2 inštancii pomocou user data skriptu aws-ec2.sh.",
    "sq":"Vendosni rtCloud në një instancë AWS EC2 duke përdorur skriptin e të dhënave të përdoruesit aws-ec2.sh.",
    "sr":"Распоредите rtCloud на AWS EC2 инстанци користећи user data скрипт aws-ec2.sh.",
    "sv":"Driftsätt rtCloud på en AWS EC2-instans med user data-skriptet aws-ec2.sh.",
    "te":"aws-ec2.sh యూజర్ డేటా స్క్రిప్ట్ ఉపయోగించి AWS EC2 ఇన్‌స్టాన్స్‌లో rtCloud విన్యసించండి.",
    "th":"ติดตั้ง rtCloud บน AWS EC2 instance โดยใช้สคริปต์ user data aws-ec2.sh",
    "tr":"aws-ec2.sh kullanıcı verisi scriptini kullanarak rtCloud'u bir AWS EC2 örneğine dağıtın.",
    "uk":"Розгорніть rtCloud на екземплярі AWS EC2 за допомогою сценарію даних користувача aws-ec2.sh.",
    "vi":"Triển khai rtCloud trên một phiên bản AWS EC2 bằng script dữ liệu người dùng aws-ec2.sh.",
    "zh-hans":"使用 aws-ec2.sh 用户数据脚本在 AWS EC2 实例上部署 rtCloud。",
    "zh-hant":"使用 aws-ec2.sh 用戶數據腳本在 AWS EC2 實例上部署 rtCloud。",
}

AWS_BODY = """Use `aws-ec2.sh` as the **User Data** script when launching an EC2 instance. The script runs automatically on first boot.

**Download script:** [aws-ec2.sh](/scripts/aws-ec2.sh)

---

## Step 1 — Fill in the configuration

Open the script and edit the `CONFIGURATION` block at the top:

```bash
# --- Required ---
PROJECT_ID="rtsurvey"
ADMIN_PASSWORD="admin"                       # Change after first login

# --- Domain + SSL ---
DOMAIN="myapp.example.com"
LETSENCRYPT_EMAIL="admin@example.com"

# --- Embedded Keycloak ---
EMBED_KEYCLOAK="true"
KEYCLOAK_ADMIN_PASSWORD="${ADMIN_PASSWORD}"  # Defaults to ADMIN_PASSWORD
```

| Field | Required | Description |
|-------|----------|-------------|
| `PROJECT_ID` | Yes | Used as database name and Keycloak client ID. Lowercase, no spaces. |
| `ADMIN_PASSWORD` | No | App admin password and Keycloak admin password. Defaults to `admin` — **change after first login**. |
| `DOMAIN` | No | Your domain for HTTPS. Leave blank for HTTP-only mode. |
| `LETSENCRYPT_EMAIL` | Yes (if DOMAIN set) | Email for Let's Encrypt notifications. |
| `EMBED_KEYCLOAK` | No | `true` to deploy embedded Keycloak (requires 4 GB RAM). |

> **Security:** All passwords default to `admin`. Change them immediately after your first login.

---

## Step 2 — Launch an EC2 instance

In the [AWS EC2 console](https://console.aws.amazon.com/ec2):

1. Click **Launch instance**
2. **AMI:** Ubuntu Server 22.04 LTS (64-bit x86)
3. **Instance type:** `t3.medium` (4 GB RAM) or larger
4. **Key pair:** Select or create one for SSH access
5. **Network settings:** Create or select a Security Group (see below)
6. **Advanced details** → **User data** → paste the full script content
7. Click **Launch instance**

---

## Step 3 — Configure the Security Group

Open these ports in the instance's Security Group:

| Port | Protocol | Source | Purpose |
|------|----------|--------|---------|
| 22 | TCP | Your IP | SSH access |
| 80 | TCP | 0.0.0.0/0 | HTTP (redirected to HTTPS by Nginx) |
| 443 | TCP | 0.0.0.0/0 | HTTPS |
| 3838 | TCP | 0.0.0.0/0 | Shiny direct access |

> Do **not** open port 3306 (MySQL) — it should never be publicly accessible.

---

## Step 4 — Add the DNS record

While the instance boots, add an **A record** in your DNS provider:

```
Type  : A
Name  : myapp
Value : <instance-public-ip>
TTL   : 300
```

---

## Step 5 — Monitor progress

```bash
ssh ubuntu@<instance-ip>
tail -f /var/log/rtcloud-setup.log
```

---

## Step 6 — Access the app

When setup completes, the log shows a summary with your app URL and credentials. Log in with username `admin` and password `admin`, then change your password immediately.

---

## After Deployment

### Change a password

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### View all containers

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```

### Assign an Elastic IP (optional)

If you stop and start the instance, the public IP changes. To keep a stable IP, allocate an **Elastic IP** and associate it with the instance in the EC2 console.
"""

# ═══════════════════════════════════════════════════════════════
# gcp.md
# ═══════════════════════════════════════════════════════════════
GCP_REL = "docs/getting-started/self-hosting/cloud-deployment/gcp.md"
GCP_DATE = "2026-03-16T00:00:00+07:00"

GCP_TITLES = {
    "ar":"Google Cloud (GCP)","bg":"Google Cloud (GCP)","cs":"Google Cloud (GCP)",
    "da":"Google Cloud (GCP)","de":"Google Cloud (GCP)","el":"Google Cloud (GCP)",
    "es":"Google Cloud (GCP)","fi":"Google Cloud (GCP)","fr":"Google Cloud (GCP)",
    "hi":"Google Cloud (GCP)","hu":"Google Cloud (GCP)","id":"Google Cloud (GCP)",
    "it":"Google Cloud (GCP)","ja":"Google Cloud (GCP)","km":"Google Cloud (GCP)",
    "ko":"Google Cloud (GCP)","lt":"Google Cloud (GCP)","lv":"Google Cloud (GCP)",
    "nb":"Google Cloud (GCP)","nl":"Google Cloud (GCP)","pl":"Google Cloud (GCP)",
    "pt":"Google Cloud (GCP)","pt-br":"Google Cloud (GCP)","ru":"Google Cloud (GCP)",
    "sk":"Google Cloud (GCP)","sq":"Google Cloud (GCP)","sr":"Google Cloud (GCP)",
    "sv":"Google Cloud (GCP)","te":"Google Cloud (GCP)","th":"Google Cloud (GCP)",
    "tr":"Google Cloud (GCP)","uk":"Google Cloud (GCP)","vi":"Google Cloud (GCP)",
    "zh-hans":"Google Cloud (GCP)","zh-hant":"Google Cloud (GCP)",
}
GCP_DESCS = {
    "ar":"نشر rtCloud على Google Cloud Compute Engine باستخدام سكريبت بدء التشغيل gcp-compute.sh.",
    "bg":"Разгръщане на rtCloud на Google Cloud Compute Engine с помощта на стартовия скрипт gcp-compute.sh.",
    "cs":"Nasazení rtCloud na Google Cloud Compute Engine pomocí spouštěcího skriptu gcp-compute.sh.",
    "da":"Installer rtCloud på Google Cloud Compute Engine ved hjælp af opstartsskriptet gcp-compute.sh.",
    "de":"rtCloud auf Google Cloud Compute Engine mit dem Startup-Skript gcp-compute.sh bereitstellen.",
    "el":"Ανάπτυξη rtCloud στο Google Cloud Compute Engine χρησιμοποιώντας το startup script gcp-compute.sh.",
    "es":"Implemente rtCloud en Google Cloud Compute Engine usando el script de inicio gcp-compute.sh.",
    "fi":"Ota rtCloud käyttöön Google Cloud Compute Enginessä käyttämällä käynnistysskriptiä gcp-compute.sh.",
    "fr":"Déployez rtCloud sur Google Cloud Compute Engine à l'aide du script de démarrage gcp-compute.sh.",
    "hi":"gcp-compute.sh स्टार्टअप स्क्रिप्ट का उपयोग करके Google Cloud Compute Engine पर rtCloud तैनात करें।",
    "hu":"Telepítse az rtCloudot a Google Cloud Compute Engine-be a gcp-compute.sh indítószkripttel.",
    "id":"Terapkan rtCloud di Google Cloud Compute Engine menggunakan skrip startup gcp-compute.sh.",
    "it":"Distribuire rtCloud su Google Cloud Compute Engine utilizzando lo script di avvio gcp-compute.sh.",
    "ja":"gcp-compute.shスタートアップスクリプトを使用してGoogle Cloud Compute EngineにrtCloudをデプロイします。",
    "km":"ដំឡើង rtCloud នៅ Google Cloud Compute Engine ដោយប្រើស្ក្រីបចាប់ផ្ដើម gcp-compute.sh ។",
    "ko":"gcp-compute.sh 시작 스크립트를 사용하여 Google Cloud Compute Engine에 rtCloud를 배포합니다.",
    "lt":"Diekite rtCloud Google Cloud Compute Engine naudodami paleisties skriptą gcp-compute.sh.",
    "lv":"Izvietojiet rtCloud Google Cloud Compute Engine, izmantojot startēšanas skriptu gcp-compute.sh.",
    "nb":"Distribuer rtCloud på Google Cloud Compute Engine ved hjelp av oppstartsskriptet gcp-compute.sh.",
    "nl":"Implementeer rtCloud op Google Cloud Compute Engine met behulp van het opstartscript gcp-compute.sh.",
    "pl":"Wdróż rtCloud na Google Cloud Compute Engine za pomocą skryptu startowego gcp-compute.sh.",
    "pt":"Implemente rtCloud no Google Cloud Compute Engine usando o script de arranque gcp-compute.sh.",
    "pt-br":"Implante rtCloud no Google Cloud Compute Engine usando o script de inicialização gcp-compute.sh.",
    "ru":"Разверните rtCloud на Google Cloud Compute Engine с помощью скрипта запуска gcp-compute.sh.",
    "sk":"Nasaďte rtCloud na Google Cloud Compute Engine pomocou spúšťacieho skriptu gcp-compute.sh.",
    "sq":"Vendosni rtCloud në Google Cloud Compute Engine duke përdorur skriptin e nisjes gcp-compute.sh.",
    "sr":"Распоредите rtCloud на Google Cloud Compute Engine користећи startup скрипт gcp-compute.sh.",
    "sv":"Driftsätt rtCloud på Google Cloud Compute Engine med startskriptet gcp-compute.sh.",
    "te":"gcp-compute.sh స్టార్టప్ స్క్రిప్ట్ ఉపయోగించి Google Cloud Compute Engine లో rtCloud విన్యసించండి.",
    "th":"ติดตั้ง rtCloud บน Google Cloud Compute Engine โดยใช้สคริปต์เริ่มต้น gcp-compute.sh",
    "tr":"gcp-compute.sh başlangıç scriptini kullanarak rtCloud'u Google Cloud Compute Engine üzerinde dağıtın.",
    "uk":"Розгорніть rtCloud на Google Cloud Compute Engine за допомогою стартового сценарію gcp-compute.sh.",
    "vi":"Triển khai rtCloud trên Google Cloud Compute Engine bằng script khởi động gcp-compute.sh.",
    "zh-hans":"使用 gcp-compute.sh 启动脚本在 Google Cloud Compute Engine 上部署 rtCloud。",
    "zh-hant":"使用 gcp-compute.sh 啟動腳本在 Google Cloud Compute Engine 上部署 rtCloud。",
}

GCP_BODY = """Use `gcp-compute.sh` as the **Startup script** when creating a Compute Engine VM instance. The script runs automatically on first boot.

**Download script:** [gcp-compute.sh](/scripts/gcp-compute.sh)

---

## Step 1 — Fill in the configuration

Open the script and edit the `CONFIGURATION` block at the top:

```bash
# --- Required ---
PROJECT_ID="rtsurvey"
ADMIN_PASSWORD="admin"                       # Change after first login

# --- Domain + SSL ---
DOMAIN="myapp.example.com"
LETSENCRYPT_EMAIL="admin@example.com"

# --- Embedded Keycloak ---
EMBED_KEYCLOAK="true"
KEYCLOAK_ADMIN_PASSWORD="${ADMIN_PASSWORD}"  # Defaults to ADMIN_PASSWORD
```

| Field | Required | Description |
|-------|----------|-------------|
| `PROJECT_ID` | Yes | Used as database name and Keycloak client ID. Lowercase, no spaces. |
| `ADMIN_PASSWORD` | No | App admin password and Keycloak admin password. Defaults to `admin` — **change after first login**. |
| `DOMAIN` | No | Your domain for HTTPS. Leave blank for HTTP-only mode. |
| `LETSENCRYPT_EMAIL` | Yes (if DOMAIN set) | Email for Let's Encrypt notifications. |
| `EMBED_KEYCLOAK` | No | `true` to deploy embedded Keycloak (requires 4 GB RAM). |

> **Security:** All passwords default to `admin`. Change them immediately after your first login.

---

## Step 2 — Create a VM instance

In the [Google Cloud Console](https://console.cloud.google.com/compute):

1. Click **Create instance**
2. **Machine configuration:**
   - Series: `E2`
   - Machine type: `e2-medium` (4 GB RAM) or larger
3. **Boot disk:**
   - Operating system: Ubuntu
   - Version: Ubuntu 22.04 LTS
   - Size: 40 GB or more
4. **Firewall:** check **Allow HTTP traffic** and **Allow HTTPS traffic**
5. **Advanced options** → **Management** → **Automation** → **Startup script** → paste the full script content
6. Click **Create**

---

## Step 3 — Add the DNS record

While the VM boots, add an **A record** in your DNS provider:

```
Type  : A
Name  : myapp
Value : <vm-external-ip>
TTL   : 300
```

Find the external IP in the VM instances list in the console.

---

## Step 4 — Monitor progress

Using the `gcloud` CLI:

```bash
gcloud compute ssh <instance-name> -- tail -f /var/log/rtcloud-setup.log
```

Or SSH directly:

```bash
ssh <username>@<vm-external-ip>
tail -f /var/log/rtcloud-setup.log
```

---

## Step 5 — Access the app

When setup completes, the log shows a summary with your app URL and credentials. Log in with username `admin` and password `admin`, then change your password immediately.

---

## Firewall Rules

GCP's **Allow HTTP/HTTPS** checkboxes open ports 80 and 443. To also allow direct Shiny access on port 3838, add a firewall rule:

```bash
gcloud compute firewall-rules create allow-shiny \\
  --allow tcp:3838 \\
  --target-tags http-server
```

Or add it via the console: **VPC Network** → **Firewall** → **Create rule**.

> Do **not** open port 3306 (MySQL) — it should never be publicly accessible.

---

## Static IP (optional)

By default, GCP assigns an ephemeral external IP that changes on VM restart. To keep a stable IP:

1. Go to **VPC Network** → **IP addresses**
2. Click **Reserve external static address**
3. Assign it to your VM instance

---

## After Deployment

### Change a password

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### View all containers

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```
"""

# ═══════════════════════════════════════════════════════════════
# WRITE ALL FILES
# ═══════════════════════════════════════════════════════════════
count = 0
for lang in LANGUAGES:
    # _index.md
    fm = frontmatter(3, INDEX_TITLES[lang], INDEX_DATE, INDEX_DATE, "cloud_upload", INDEX_DESCS[lang])
    body = INDEX_BODY_TEMPLATE.format(intro=INDEX_INTRO[lang])
    write(INDEX_REL, lang, fm, body)
    count += 1

    # linode.md
    fm = frontmatter(2, LINODE_TITLES[lang], LINODE_DATE, LINODE_LASTMOD, "dns", LINODE_DESCS[lang])
    write(LINODE_REL, lang, fm, LINODE_BODY)
    count += 1

    # digitalocean.md
    fm = frontmatter(1, DO_TITLES[lang], DO_DATE, DO_LASTMOD, "water_drop", DO_DESCS[lang])
    write(DO_REL, lang, fm, DO_BODY)
    count += 1

    # aws.md
    fm = frontmatter(3, AWS_TITLES[lang], AWS_DATE, AWS_DATE, "cloud", AWS_DESCS[lang])
    write(AWS_REL, lang, fm, AWS_BODY)
    count += 1

    # gcp.md
    fm = frontmatter(4, GCP_TITLES[lang], GCP_DATE, GCP_DATE, "travel_explore", GCP_DESCS[lang])
    write(GCP_REL, lang, fm, GCP_BODY)
    count += 1

print(f"Written {count} cloud deployment files.")
