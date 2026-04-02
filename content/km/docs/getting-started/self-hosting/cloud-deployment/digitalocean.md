---
weight: 1
title: "មហាសមុទ្រឌីជីថល"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-17T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "water_drop"
toc: true
description: "ដាក់ពង្រាយ rtCloud នៅលើ DigitalOcean Droplet ដោយប្រើស្គ្រីបទិន្នន័យអ្នកប្រើប្រាស់ស្វ័យប្រវត្តិ។"
---

DigitalOcean ប្រើស្គ្រីប **ទិន្នន័យអ្នកប្រើប្រាស់** ដែលដំណើរការដោយស្វ័យប្រវត្តិនៅពេលចាប់ផ្ដើមដំបូង។ អ្នកបំពេញអថេរកំណត់រចនាសម្ព័ន្ធនៅផ្នែកខាងលើនៃស្គ្រីប បន្ទាប់មកបិទភ្ជាប់ស្គ្រីបទាំងមូលនៅពេលបង្កើត Droplet ។

> មិនដូច Linode StackScripts ទេ DigitalOcean មិនមានទម្រង់ UI ទេ អ្នកត្រូវតែកែសម្រួលស្គ្រីបដោយផ្ទាល់មុនពេលបិទភ្ជាប់។

**Download script:** [digitalocean-droplet-keycloak-embed.sh](/scripts/digitalocean-droplet-keycloak-embed.sh)

---

## កូនសោដែលបានបង្កប់ (បានណែនាំ)

ប្រើ 'digitalocean-droplet-keycloak-embed.sh' សម្រាប់ការដំឡើងដ៏សាមញ្ញបំផុតជាមួយនឹង SSO ដែលភ្ជាប់មកជាមួយ។

### ជំហានទី 1 — បំពេញការកំណត់រចនាសម្ព័ន្ធ

បើកស្គ្រីប ហើយកែសម្រួលប្លុក 'CONFIGURATION' នៅផ្នែកខាងលើ៖

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

| វាល | ទាមទារ | បរិយាយ |
|--------|----------------|----------------|
| `PROJECT_ID` | បាទ | ប្រើជាឈ្មោះមូលដ្ឋានទិន្នន័យ និងលេខសម្គាល់អតិថិជន Keycloak ។ Lowercase, no spaces. |
| `ADMIN_PASSWORD` | ទេ | ពាក្យសម្ងាត់សម្រាប់ការចូលអ្នកគ្រប់គ្រងកម្មវិធី និងកុងសូលគ្រប់គ្រង Keycloak ។ លំនាំដើមទៅ `admin` — ** ផ្លាស់ប្តូរបន្ទាប់ពីការចូលដំបូង ** ។ |
| `DOMAIN` | បាទ | ឈ្មោះដែនរបស់អ្នក។ DNS A record ត្រូវតែចង្អុលទៅ Droplet IP ។ |
| `LETSENCRYPT_EMAIL` | បាទ | អាសយដ្ឋានអ៊ីមែលសម្រាប់ការជូនដំណឹងអំពីវិញ្ញាបនបត្រ Let's Encrypt ។ |
| `PROJECT_URL` | ទេ | បដិសេធ URL សាធារណៈ។ ទុកទទេដើម្បីប្រើ `DOMAIN`។ មានប្រយោជន៍នៅពីក្រោយ Cloudflare ។ |

> ** សុវត្ថិភាព៖** ពាក្យសម្ងាត់ទាំងអស់លំនាំដើមទៅជា `admin`។ ផ្លាស់ប្តូរពួកវាភ្លាមៗបន្ទាប់ពីការចូលដំបូងរបស់អ្នក។

### ជំហានទី 2 — បង្កើត Droplet

In the [DigitalOcean control panel](https://cloud.digitalocean.com):

1. ចុច **បង្កើត** → **Droplets**
2. ជ្រើសរើស ** Ubuntu 22.04 LTS ** ជារូបភាព
3. ជ្រើសរើស **Basic, RAM 4 GB / 2 vCPUs** ឬធំជាងនេះ។
4. រមូរទៅ **ជម្រើសកម្រិតខ្ពស់** → ពិនិត្យ **បន្ថែមស្គ្រីបចាប់ផ្តើម**
5. បិទភ្ជាប់ខ្លឹមសារស្គ្រីបពេញទៅក្នុងផ្ទៃអត្ថបទ
6. ចុច **Create Droplet**

### ជំហានទី 3 — បន្ថែមកំណត់ត្រា DNS

ខណៈពេលដែល Droplet ចាប់ផ្តើម បន្ថែម ** កំណត់ត្រា ** នៅក្នុងក្រុមហ៊ុនផ្តល់ DNS របស់អ្នក៖

```
Type  : A
Name  : myapp          (or @ for root domain)
Value : <droplet-ip>
TTL   : 300
```

### ជំហានទី 4 — តាមដានដំណើរការ

SSH ចូលទៅក្នុង Droplet ហើយមើលកំណត់ហេតុ៖

```bash
ssh root@<droplet-ip>
tail -f /var/log/rtcloud-setup.log
```

ស្គ្រីបបោះពុម្ព IP ម៉ាស៊ីនមេរបស់អ្នកនៅជិតការចាប់ផ្តើម — បន្ថែមកំណត់ត្រា DNS ភ្លាមៗនៅពេលអ្នកឃើញវា។

### ជំហានទី 5 — ចូលប្រើកម្មវិធី

នៅពេលការដំឡើងបានបញ្ចប់ កំណត់ហេតុបង្ហាញសេចក្ដីសង្ខេប៖

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

> **ផ្លាស់ប្តូរពាក្យសម្ងាត់របស់អ្នក** ភ្លាមៗបន្ទាប់ពីចូលតាមរយៈ **ការកំណត់** នៅក្នុងម៉ឺនុយខាងស្តាំខាងលើ។

---

## បន្ទាប់ពីការដាក់ឱ្យប្រើប្រាស់

### ប្តូរលេខសម្ងាត់

SSH ចូលទៅក្នុង Droplet កែសម្រួល `.env` និងចាប់ផ្តើមធុងដែលរងផលប៉ះពាល់ឡើងវិញ៖

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### ធ្វើបច្ចុប្បន្នភាពដែន

ប្រសិនបើអ្នកកំណត់ដែនផ្សេងបន្ទាប់ពីការដាក់ឱ្យប្រើប្រាស់ សូមធ្វើបច្ចុប្បន្នភាព `PROJECT_URL` នៅក្នុង `.env`៖

```bash
nano /opt/rtcloud/.env   # update PROJECT_URL=
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### មើលធុងទាំងអស់។

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```
