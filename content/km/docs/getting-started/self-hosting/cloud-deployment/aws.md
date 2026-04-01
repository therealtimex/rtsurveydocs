---
weight: 3
title: "AWS EC2"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-16T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "cloud"
toc: true
description: "ដាក់ deployed rtCloud នៅ AWS EC2 instance ដោយប្រើ aws-ec2.sh user data script។"
---

ប្រើ `aws-ec2.sh` ជា **User Data** script នៅពេល launch EC2 instance។ Script ដំណើរការ ដោយ ស្វ័យប្រវត្តិ នៅ boot ដំបូង។

**ទាញយក script:** [aws-ec2.sh](/scripts/aws-ec2.sh)

---

## ជំហានទី ១ — បំពេញ configuration

បើក script ហើយ កែ block `CONFIGURATION` នៅ ខាងលើ:

```bash
# --- ចាំបាច់ ---
PROJECT_ID="rtsurvey"
ADMIN_PASSWORD="admin"                       # ផ្លាស់ប្ដូរ បន្ទាប់ ចូល ដំបូង

# --- Domain + SSL ---
DOMAIN="myapp.example.com"
LETSENCRYPT_EMAIL="admin@example.com"

# --- Keycloak ភ្ជាប់ ---
EMBED_KEYCLOAK="true"
KEYCLOAK_ADMIN_PASSWORD="${ADMIN_PASSWORD}"  # Default ទៅ ADMIN_PASSWORD
```

| Field | ចាំបាច់ | ការពិពណ៌នា |
|-------|----------|-------------|
| `PROJECT_ID` | បាទ | ប្រើ ជា ឈ្មោះ database និង Keycloak client ID។ Lowercase, គ្មាន ចន្លោះ។ |
| `ADMIN_PASSWORD` | ទេ | ពាក្យ សម្ងាត់ app admin និង Keycloak admin។ Default `admin` — **ផ្លាស់ប្ដូរ បន្ទាប់ ចូល ដំបូង**។ |
| `DOMAIN` | ទេ | Domain របស់អ្នក សម្រាប់ HTTPS។ ទុក blank សម្រាប់ HTTP mode ប៉ុណ្ណោះ។ |
| `LETSENCRYPT_EMAIL` | បាទ (ប្រសិនបើ DOMAIN set) | Email សម្រាប់ Let's Encrypt notifications។ |
| `EMBED_KEYCLOAK` | ទេ | `true` ដើម្បី deploy Keycloak ភ្ជាប់ (ត្រូវការ RAM 4 GB)។ |

---

## ជំហានទី ២ — Launch EC2 instance

នៅ [AWS EC2 console](https://console.aws.amazon.com/ec2):

1. ចុច **Launch instance**
2. **AMI:** Ubuntu Server 22.04 LTS (64-bit x86)
3. **Instance type:** `t3.medium` (4 GB RAM) ឬ ធំ ជាង
4. **Key pair:** ជ្រើស ឬ បង្កើត មួយ សម្រាប់ SSH access
5. **Network settings:** បង្កើត ឬ ជ្រើស Security Group (មើល ខាង ក្រោម)
6. **Advanced details** → **User data** → paste ខ្លឹមសារ script ពេញ
7. ចុច **Launch instance**

---

## ជំហានទី ៣ — Configure Security Group

បើក ports ទាំងនេះ ក្នុង Security Group របស់ instance:

| Port | Protocol | Source | គោលបំណង |
|------|----------|--------|---------|
| 22 | TCP | IP របស់អ្នក | SSH access |
| 80 | TCP | 0.0.0.0/0 | HTTP (redirect ទៅ HTTPS ដោយ Nginx) |
| 443 | TCP | 0.0.0.0/0 | HTTPS |
| 3838 | TCP | 0.0.0.0/0 | Shiny direct access |

> **កុំ** បើក port 3306 (MySQL) — វា មិនគួរ accessible publicly ទេ។

---

## ជំហានទី ៤ — បន្ថែម DNS record

```
Type  : A
Name  : myapp
Value : <instance-public-ip>
TTL   : 300
```

---

## ជំហានទី ៥ — តាមដានវឌ្ឍនភាព

```bash
ssh ubuntu@<instance-ip>
tail -f /var/log/rtcloud-setup.log
```

---

## ជំហានទី ៦ — ចូលដំណើរការ app

នៅពេល setup បញ្ចប់, log បង្ហាញ summary ជាមួយ app URL និង credentials។ ចូល ជាមួយ username `admin` និង password `admin`, ហើយ ផ្លាស់ប្ដូរ ពាក្យ សម្ងាត់ ភ្លាម ៗ។

---

## បន្ទាប់ Deployment

### ផ្លាស់ប្ដូរ ពាក្យ សម្ងាត់

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### ស្វែងមើល containers ទាំងអស់

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```

### ចាត់ Elastic IP (ស្រេចចិត្ត)

ប្រសិនបើ អ្នក stop ហើយ start instance, public IP ផ្លាស់ ប្ដូរ។ ដើម្បី រក្សា IP ស្ថិរ, allocate **Elastic IP** ហើយ associate វា ជាមួយ instance ក្នុង EC2 console។
