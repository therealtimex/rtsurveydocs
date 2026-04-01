---
weight: 1
title: "ចាប់ផ្ដើមរហ័ស"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "play_circle"
toc: true
description: "ដំណើរការ rtCloud នៅលើម៉ាស៊ីនមេផ្ទាល់ខ្លួនរបស់អ្នក ក្នុងរយៈពេលតិចជាង ១០ នាទី ដោយប្រើ Docker Compose។"
---

មគ្គុទ្ទេសក៍នេះ ណែនាំអ្នក ក្នុងការដំណើរការ rtCloud instance ដែល host ខ្លួនឯង នៅលើ Linux server ចាប់ពីដំបូង។ នៅចុងបញ្ចប់ អ្នកនឹងមាន rtCloud ដែលកំពុងដំណើរការ ដែលអាចចូលដំណើរការបាន នៅក្នុង browser របស់អ្នក។

## លក្ខខណ្ឌជាមុន

ធានាថាម៉ាស៊ីនមេរបស់អ្នកបំពេញ តម្រូវការខាងក្រោម មុននឹងចាប់ផ្ដើម៖

### Hardware

| ធនធាន | អប្បបរមា | បានណែនាំ |
|----------|---------|-------------|
| RAM | 2 GB | 4 GB |
| ថាស | 10 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPUs |

### Software

| Software | កំណែ |
|----------|---------|
| OS | Ubuntu 20.04 LTS ឬថ្មីជាងនេះ (ឬ Linux ណាមួយ ដែលគាំទ្រ Docker) |
| Docker | 20.10 ឬថ្មីជាងនេះ |
| Docker Compose | v2.x (`docker compose`) ឬ v1.x (`docker-compose`) |

**ដំឡើង Docker នៅ Ubuntu:**

```bash
curl -fsSL https://get.docker.com | sh
```

ផ្ទៀងផ្ទាត់ការដំឡើង៖

```bash
docker --version
docker compose version
```

---

## ជំហានទី ១ — ទទួលបានឯកសារ

Clone repository ការដាក់ deployed ទៅម៉ាស៊ីនមេរបស់អ្នក៖

```bash
git clone ssh://git@rtgit.rta.vn:2224/rtlab/rtwebteam/rta-smart-survey-docker.git rtcloud
cd rtcloud
```

---

## ជំហានទី ២ — ការកំណត់ Environment

Copy ឯកសារការកំណត់គំរូ៖

```bash
cp .env.production.sample .env
```

បើក `.env` នៅក្នុង text editor ហើយបំពេញតម្លៃដែលត្រូវការ៖

```dotenv
# អត្តសញ្ញាណតែមួយគត់ សម្រាប់ការដាក់ deployed នេះ (គ្មានចន្លោះ, គ្មានតួអក្សរពិសេស)
PROJECT_ID=myproject

# Domain ឬ IP address ដែលអ្នកប្រើ នឹងចូលដំណើរការ app
# ឧទាហរណ៍: rtcloud.example.com  ឬ  192.168.1.100
PROJECT_URL=rtcloud.example.com

# Protocol: ប្រើ "https" ប្រសិនបើអ្នកមី domain ជាមួយ SSL, "http" បើមិនមែន
HTTP_PROTOCOL=https

# ពាក្យសម្ងាត់ខ្លាំង តែមួយគត់ — ផ្លាស់ប្ដូរទាំងបី មុននឹងចាប់ផ្ដើម
MYSQL_PASSWORD=change_me_strong_password
MYSQL_ROOT_PASSWORD=change_me_root_password
ADMIN_PASSWORD=change_me_admin_password
```

> **សំខាន់:** មានតែ `.env` ប៉ុណ្ណោះ ដែលអានដោយ Docker Compose ដោយស្វ័យប្រវត្តិ។ កុំបង្កើតឯកសារ ដែលមានឈ្មោះ `.env.production` ព្រោះវានឹងបណ្ដាលឱ្យមានការភ្លេច។ `ADMIN_PASSWORD` ត្រូវបានអនុវត្ត មានតែ **boot ដំបូង** នៃ database ថ្មី។

---

## ជំហានទី ៣ — ចាប់ផ្ដើម Containers

បើក services ទាំងអស់ ក្នុង background៖

```bash
docker compose -f docker-compose.production.yml up -d
```

ការ startup ដំបូង ចំណាយពេល **៣–៥ នាទី** ខណៈ Docker៖

1. Pull image កម្មវិធី rtCloud (~1 GB ទាញយក)
2. Initialize មូលដ្ឋានទិន្នន័យ MySQL
3. Load schema មូលដ្ឋាន
4. Run database migrations ដែលកំពុងរង់ចាំទាំងអស់

តាមដានវឌ្ឍនភាព startup ជាក់ស្ដែង៖

```bash
docker compose -f docker-compose.production.yml logs -f rtcloud
```

រង់ចាំរហូតដល់អ្នកឃើញ output ដែលបង្ហាញថា application ត្រៀមរួចហើយ។ អ្នកក៏អាចតាមដានស្ថានភាព health របស់ container ផងដែរ៖

```bash
watch docker compose -f docker-compose.production.yml ps
```

---

## ជំហានទី ៤ — ចូលដំណើរការ Application

នៅពេល containers ទាំងពីរ បង្ហាញ `Up (healthy)` បើក browser របស់អ្នក៖

```
http://<PROJECT_URL>:8080
```

ចូលដោយប្រើគណនី administrator៖

| វាល | តម្លៃ |
|-------|-------|
| ឈ្មោះអ្នកប្រើ | `admin` |
| ពាក្យសម្ងាត់ | តម្លៃដែលអ្នកបានកំណត់ `ADMIN_PASSWORD` នៅក្នុង `.env` |

> ផ្លាស់ប្ដូរពាក្យសម្ងាត់ admin ភ្លាមៗ បន្ទាប់ពីការចូលដំបូង ពីទំព័រការកំណត់គណនី។

---

## ជំហានទី ៥ — ផ្ទៀងផ្ទាត់ Services ទាំងអស់

ពិនិត្យថា containers ទាំងអស់ កំពុងដំណើរការ ហើយ healthy៖

```bash
docker compose -f docker-compose.production.yml ps
```

Output ដែលរំពឹង៖

```
NAME                    IMAGE                                   STATUS
rtcloud-app             rtawebteam/rta-smartsurvey:...          Up (healthy)
rtcloud-mysql           mysql:8.0                               Up (healthy)
```

ប្រសិនបើ container បង្ហាញ `Up (starting)` ឬ `Up (unhealthy)` រង់ចាំ ៣០–៦០ វិនាទីទៀត ហើយពិនិត្យម្ដងទៀត។ MySQL អាចចំណាយពេលរហូតដល់មួយនាទី ដើម្បី initialize ពេញលេញ នៅ boot ដំបូង។

---

## ឯកសារ Port

| Port | Service | ការពិពណ៌នា |
|------|---------|-------------|
| `8080` | rtCloud App | Web UI ចម្បង (អាចកំណត់ដោយ `APP_PORT`) |
| `3838` | Shiny Server | ការវិភាគ និងការបំភ្លឺដោយ R (អាចកំណត់ដោយ `SHINY_PORT`) |

MySQL (port 3306) និងសេវាស្រេចចិត្ត (Keycloak) គឺ internal only ហើយ មិនត្រូវបានបង្ហាញ ទៅ host ដោយ default ទេ។

---

## ជំហានបន្ទាប់

rtCloud instance របស់អ្នក ឥឡូវ កំពុងដំណើរការ។ ពិចារណាលើភារកិច្ចតាមក្រោយ ទាំងនេះ៖

- **បើក HTTPS** — ចង្អុល domain ទៅម៉ាស៊ីនមេរបស់អ្នក ហើយ configure SSL ជាមួយ Let's Encrypt។ សូមមើល [ការដាក់ Cloud](cloud-deployment) សម្រាប់ការដំឡើង HTTPS ស្វ័យប្រវត្តិ។
- **ពិនិត្យការកំណត់ទាំងអស់** — ស្វែងរកតាម [ឯកសារការកំណត់](configuration) ដើម្បី tune ការដាក់ deployed សម្រាប់ production។
- **ដំឡើង SSO** — ភ្ជាប់ identity provider សម្រាប់ការផ្ទៀងផ្ទាត់អ្នកប្រើ centralized។ សូមមើល [ការផ្ទៀងផ្ទាត់ SSO](sso-authentication)។
- **ធ្វើផែនការ backup** — ពិនិត្យទំព័រ [ការថែទាំ](maintenance) សម្រាប់នីតិវិធី backup និងការ upgrade។
