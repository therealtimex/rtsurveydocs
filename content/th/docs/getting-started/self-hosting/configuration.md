---
weight: 2
title: "การอ้างอิงการกำหนดค่า"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "settings"
toc: true
description: "การอ้างอิงที่สมบูรณ์สำหรับตัวแปรสภาพแวดล้อมทั้งหมดที่ใช้ในการกำหนดค่าการติดตั้ง rtCloud แบบโฮสต์ด้วยตนเอง"
---

การกำหนดค่าทั้งหมดทำผ่านตัวแปรสภาพแวดล้อมในไฟล์ `.env` ที่รูทของไดเรกทอรีการติดตั้งใช้งาน Docker Compose อ่านไฟล์นี้โดยอัตโนมัติ — ไม่จำเป็นต้องใช้แฟล็ก `--env-file`

ตัวแปรที่ทำเครื่องหมาย **ต้องมี** ต้องถูกตั้งค่าก่อนเริ่มต้นคอนเทนเนอร์ ตัวแปรอื่นๆ มีค่าเริ่มต้นและเป็นตัวเลือก

---

## โครงการ

ตัวแปรเหล่านี้กำหนดตัวตนและจุดเข้าถึงอินสแตนซ์ rtCloud ของคุณ

| ตัวแปร | ค่าเริ่มต้น | ต้องมี | คำอธิบาย |
|----------|---------|----------|-------------|
| `PROJECT_ID` | — | **ใช่** | ตัวระบุเฉพาะสำหรับการติดตั้งนี้ ไม่มีช่องว่างหรืออักขระพิเศษ ใช้เป็นคำนำหน้าสำหรับการตั้งชื่อภายใน |
| `PROJECT_URL` | — | **ใช่** | ชื่อโดเมนหรือที่อยู่ IP ที่ผู้ใช้เข้าถึงแอป (เช่น `rtcloud.example.com` หรือ `192.168.1.100`) |
| `PROJECT_TYPE` | `rtsurvey` | ไม่ | ตัวแปรแพลตฟอร์มที่จะเปิดใช้งาน ตัวเลือก: `rtwork`, `rtsurvey`, `rthome` |
| `PROJECT_PORT` | `80` | ไม่ | พอร์ตที่แอปพลิเคชันรับฟังภายในคอนเทนเนอร์ อย่าเปลี่ยนเว้นแต่คุณรู้ว่ากำลังทำอะไร |
| `HTTP_PROTOCOL` | `https` | ไม่ | โปรโตคอลที่ใช้สร้าง URL ภายใน ตั้งเป็น `http` ถ้าไม่ได้ใช้ SSL |

---

## ฐานข้อมูล

ข้อมูลประจำตัวการเชื่อมต่อ MySQL ฐานข้อมูลได้รับการจัดการโดยอัตโนมัติโดยคอนเทนเนอร์ MySQL — คุณเพียงแค่ต้องตั้งรหัสผ่านที่แข็งแกร่ง

| ตัวแปร | ค่าเริ่มต้น | ต้องมี | คำอธิบาย |
|----------|---------|----------|-------------|
| `MYSQL_DATABASE` | `smartsurvey` | ไม่ | ชื่อฐานข้อมูลแอปพลิเคชัน |
| `MYSQL_USER` | `smartsurvey` | ไม่ | ผู้ใช้ MySQL สำหรับแอปพลิเคชัน |
| `MYSQL_PASSWORD` | — | **ใช่** | รหัสผ่านสำหรับ `MYSQL_USER` ใช้ค่าที่แข็งแกร่งและเฉพาะ |
| `MYSQL_ROOT_PASSWORD` | — | **ใช่** | รหัสผ่าน root MySQL จำเป็นสำหรับการเริ่มต้นฐานข้อมูลและการดำเนินการผู้ดูแลระบบ |
| `MYSQL_HOST` | `mysql` | ไม่ | ชื่อโฮสต์ MySQL ใช้ค่าเริ่มต้นเว้นแต่คุณกำลังเชื่อมต่อกับฐานข้อมูลภายนอก |
| `MYSQL_PORT` | `3306` | ไม่ | พอร์ต MySQL |

---

## บัญชีผู้ดูแลระบบ

บัญชีผู้ดูแลระบบถูกสร้างโดยอัตโนมัติเมื่อบูตครั้งแรกของฐานข้อมูลใหม่

| ตัวแปร | ค่าเริ่มต้น | ต้องมี | คำอธิบาย |
|----------|---------|----------|-------------|
| `ADMIN_PASSWORD` | `admin` | **ใช่** | รหัสผ่านสำหรับผู้ใช้ `admin` ในตัว ตั้งก่อนบูตครั้งแรก ไม่มีผลถ้าฐานข้อมูลมีอยู่แล้ว |

> หลังจากเข้าสู่ระบบครั้งแรก ให้เปลี่ยนรหัสผ่านผู้ดูแลระบบจากหน้า **Account Settings** ใน UI เว็บ

---

## พอร์ต

ควบคุมว่าพอร์ตโฮสต์ใดที่แอปพลิเคชันผูกกับ

| ตัวแปร | ค่าเริ่มต้น | คำอธิบาย |
|----------|---------|-------------|
| `APP_PORT` | `8080` | พอร์ตโฮสต์สำหรับ UI เว็บหลัก เปลี่ยนถ้าพอร์ต 8080 ถูกใช้งานอยู่แล้วบนเซิร์ฟเวอร์ |
| `SHINY_PORT` | `3838` | พอร์ตโฮสต์สำหรับเซิร์ฟเวอร์ Shiny analytics |

---

## Runtime

| ตัวแปร | ค่าเริ่มต้น | คำอธิบาย |
|----------|---------|-------------|
| `RUN_ENV` | `prod` | สภาพแวดล้อม Runtime ใช้ `prod` สำหรับการผลิต `dev` สำหรับการพัฒนาภายในเครื่อง |
| `RUN_MODE` | `admin` | บทบาทคอนเทนเนอร์ `admin` รันสแตกเต็ม (web + queue + cron) `worker` รันการประมวลผลพื้นหลังเท่านั้น |
| `TZ` | `Asia/Ho_Chi_Minh` | เขตเวลาเซิร์ฟเวอร์ ส่งผลต่อ timestamps ล็อก กำหนดการ cron และการแสดงวันที่ ใช้ [ชื่อฐานข้อมูล TZ](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) |
| `LOG_LEVEL` | `info` | ระดับความละเอียดล็อกแอปพลิเคชัน ตัวเลือก: `debug`, `info`, `warning`, `error` |
| `COMPOSE_PROJECT_NAME` | `rtcloud` | คำนำหน้าที่ใช้กับชื่อคอนเทนเนอร์และ volume Docker ทั้งหมด เปลี่ยนเมื่อรันหลายอินสแตนซ์ rtCloud บนโฮสต์เดียวกัน |
| `RESTART_POLICY` | `unless-stopped` | พฤติกรรมการรีสตาร์ทคอนเทนเนอร์ Docker ตัวเลือก: `no`, `always`, `on-failure`, `unless-stopped` |
| `RTCLOUD_IMAGE` | `rtawebteam/rta-smartsurvey:survey-dockerize` | Docker image ที่จะใช้ เปลี่ยน tag เพื่อปักหมุดเวอร์ชันเฉพาะ |
| `REQUIRE_LICENSE` | `false` | เปิดใช้งานการตรวจสอบ license key เมื่อเริ่มต้น ติดต่อ RTA สำหรับข้อมูล license |

---

## ความปลอดภัย

| ตัวแปร | ค่าเริ่มต้น | คำอธิบาย |
|----------|---------|-------------|
| `CSRF_VALIDATION_ENABLED` | `true` | เปิดใช้งานการตรวจสอบ CSRF token เก็บเป็น `true` ในการผลิต ตั้งเป็น `false` เฉพาะในการพัฒนาภายในเครื่องเมื่อพบข้อผิดพลาด `400 CSRF token could not be verified` |
| `GII_ENABLED` | `false` | เปิดใช้งานเครื่องมือสร้างโค้ด Yii framework **ห้ามเปิดในการผลิตเด็ดขาด** |

---

## SSO — Keycloak แบบฝัง

เปิดใช้งานคอนเทนเนอร์ Keycloak ที่รวมมาสำหรับ SSO องค์กรเต็มรูปแบบ ต้องการโดเมนพร้อม HTTPS

| ตัวแปร | ค่าเริ่มต้น | คำอธิบาย |
|----------|---------|-------------|
| `EMBED_KEYCLOAK` | `false` | ตั้งเป็น `true` เพื่อเริ่มคอนเทนเนอร์ Keycloak แบบฝัง เปิดใช้งานโปรไฟล์ `embed-keycloak` ของ Docker Compose |
| `KEYCLOAK_URL` | — | URL เต็มของเซิร์ฟเวอร์ Keycloak (เช่น `https://rtcloud.example.com/auth`) |
| `KEYCLOAK_REALM` | — | ชื่อ realm Keycloak (เช่น `rtsurvey`) |
| `KEYCLOAK_CLIENT_ID` | — | Client ID ของ Keycloak สำหรับแอปพลิเคชัน rtCloud |
| `KEYCLOAK_CLIENT_SECRET` | — | Client secret ของ Keycloak สร้างจากคอนโซลผู้ดูแลระบบ Keycloak |
| `KEYCLOAK_ADMIN_USER` | `admin` | ชื่อผู้ใช้ผู้ดูแลระบบ Keycloak |
| `KEYCLOAK_ADMIN_PASSWORD` | — | รหัสผ่านผู้ดูแลระบบ Keycloak |
| `KEYCLOAK_DB` | `keycloak` | ชื่อฐานข้อมูลสำหรับ Keycloak สร้างโดยอัตโนมัติเมื่อบูตครั้งแรก |
| `KEYCLOAK_DB_USER` | `keycloak` | ผู้ใช้ฐานข้อมูลสำหรับ Keycloak |
| `KEYCLOAK_DB_PASSWORD` | — | รหัสผ่านฐานข้อมูลสำหรับผู้ใช้ Keycloak |
| `KC_HOSTNAME` | — | URL frontend ของ Keycloak (เช่น `https://rtcloud.example.com/auth`) |
| `KC_HOSTNAME_STRICT` | `false` | บังคับการจับคู่ชื่อโฮสต์อย่างเข้มงวด ตั้งเป็น `true` ในการผลิตพร้อมโดเมนที่แน่นอน |

ดู [การยืนยันตัวตน SSO](sso-authentication#embedded-keycloak) สำหรับคู่มือการตั้งค่าที่สมบูรณ์

---

## SSO — ผู้ให้บริการ OIDC ภายนอก

เชื่อมต่อกับผู้ให้บริการตัวตนที่รองรับ OIDC ที่มีอยู่ (Supabase, Auth0, Authentik, Okta ฯลฯ)

| ตัวแปร | ค่าเริ่มต้น | คำอธิบาย |
|----------|---------|-------------|
| `OIDC_ISSUER_URL` | — | URL การค้นพบ OIDC issuer (เช่น `https://accounts.google.com`) |
| `OIDC_CLIENT_ID` | — | Client ID ที่ลงทะเบียนในผู้ให้บริการตัวตน |
| `OIDC_CLIENT_SECRET` | — | Client secret จากผู้ให้บริการตัวตน |
| `OIDC_SCOPE` | `openid profile email` | รายการ OIDC scopes ที่คั่นด้วยช่องว่างสำหรับร้องขอ |
| `OIDC_REDIRECT_URI` | — | URL callback สำหรับแอปเว็บ (เช่น `https://rtcloud.example.com/auth/callback`) |
| `OIDC_MOBILE_CLIENT_ID` | — | Client ID แยกสำหรับแอปมือถือ rtSurvey |
| `OIDC_MOBILE_REDIRECT_URI` | — | URI callback แอปมือถือ (เช่น `vn.rta.rtsurvey.auth://callback`) |
| `OPEN_REGISTRATION` | `false` | สร้างบัญชี rtCloud โดยอัตโนมัติสำหรับผู้ใช้ที่ยืนยันตัวตนผ่าน OIDC เป็นครั้งแรก |
| `OIDC_AUTHORIZATION_ENDPOINT` | — | แทนที่ URL authorization endpoint (เว้นว่างเพื่อใช้การค้นพบ) |
| `OIDC_TOKEN_ENDPOINT` | — | แทนที่ URL token endpoint (เว้นว่างเพื่อใช้การค้นพบ) |
| `OIDC_USERINFO_ENDPOINT` | — | แทนที่ URL userinfo endpoint (เว้นว่างเพื่อใช้การค้นพบ) |

---

## SSO — Azure Active Directory

| ตัวแปร | คำอธิบาย |
|----------|-------------|
| `AZURE_CLIENT_ID` | Azure AD application (client) ID |
| `AZURE_TENANT_ID` | Azure AD directory (tenant) ID |

---

## การผสานรวมเสริม

### Stata

| ตัวแปร | ค่าเริ่มต้น | คำอธิบาย |
|----------|---------|-------------|
| `STATA_ENABLED` | `false` | เปิดใช้งานการผสานรวมซอฟต์แวร์สถิติ Stata สำหรับการวิเคราะห์ข้อมูล |
| `STATA_BIN_PATH` | `/usr/bin/stata` | พาธสัมบูรณ์ไปยัง binary Stata ภายในคอนเทนเนอร์ |

### Elasticsearch

| ตัวแปร | คำอธิบาย |
|----------|-------------|
| `ES_HOST` | โฮสต์ Elasticsearch (เช่น `http://elasticsearch:9200`) |
| `ES_PORT` | พอร์ต Elasticsearch |

### Matomo Analytics

| ตัวแปร | คำอธิบาย |
|----------|-------------|
| `PIWIK_URL` | URL เซิร์ฟเวอร์ Matomo (Piwik) |
| `PIWIK_ID` | ID เว็บไซต์ Matomo |
| `PIWIK_SECRET` | โทเค็นการยืนยันตัวตน Matomo |

### OpenCPU (การคำนวณ R)

| ตัวแปร | คำอธิบาย |
|----------|-------------|
| `OCPU_HOST` | URL เซิร์ฟเวอร์ OpenCPU สำหรับการคำนวณสถิติที่ใช้ R |

### การผสานรวม RtBox

| ตัวแปร | คำอธิบาย |
|----------|-------------|
| `RTBOX_HOST` | URL โฮสต์บริการ RtBox |
| `RTBOX_USER_API` | API key ผู้ใช้ RtBox |
| `RTBOX_BASIC_AUTH` | ข้อมูลประจำตัวการยืนยันตัวตนพื้นฐานสำหรับ RtBox |

### Matrix Messaging

| ตัวแปร | คำอธิบาย |
|----------|-------------|
| `MATRIX_HOMESERVER_HOST` | โฮสต์ Matrix homeserver |
| `MATRIX_HOMESERVER_PORT` | พอร์ต Matrix homeserver |

---

## Data Volumes

ข้อมูลแอปพลิเคชันทั้งหมดถูกจัดเก็บใน Docker volumes ที่มีชื่อ Volumes ถูกสร้างโดยอัตโนมัติเมื่อเริ่มต้นครั้งแรกและคงอยู่ข้ามการรีสตาร์ทและการอัปเดตคอนเทนเนอร์

| Volume | Mount Point | เนื้อหา |
|--------|-------------|----------|
| `rtcloud_mysql_data` | `/var/lib/mysql` | ไฟล์ฐานข้อมูล MySQL |
| `rtcloud_uploads` | `…/uploads` | ไฟล์ที่ผู้ตอบแบบสำรวจอัปโหลด |
| `rtcloud_audios` | `…/audios` | การบันทึกเสียง |
| `rtcloud_downloads` | `…/downloads` | ไฟล์ส่งออกที่สร้างขึ้น |
| `rtcloud_gallery` | `…/gallery` | รูปภาพ gallery |
| `rtcloud_voicemail` | `…/voicemail` | การบันทึก voicemail |
| `rtcloud_analytics` | `…/analytics` | ข้อมูลการวิเคราะห์ |
| `rtcloud_aggregate` | `…/aggregate` | ผลการสำรวจแบบรวม |
| `rtcloud_converter` | `…/converter` | ผลลัพธ์การแปลงข้อมูล |
| `rtcloud_shiny_data` | `/srv/shiny-server/smartsurvey` | R scripts เซิร์ฟเวอร์ Shiny |
| `rtcloud_shiny_logs` | `/var/log/shiny-server` | ล็อกเซิร์ฟเวอร์ Shiny |
| `rtcloud_assets` | `…/assets` | Web assets (CSS, JS) |
| `rtcloud_runtime` | `…/protected/runtime` | แคช runtime แอปพลิเคชัน |
| `rtcloud_cache` | `…/cache` | แคชแอปพลิเคชัน |
| `rtcloud_tmp` | `…/tmp` | ไฟล์ชั่วคราว |

ชื่อ Volume นำหน้าด้วยค่าของ `COMPOSE_PROJECT_NAME` (ค่าเริ่มต้น: `rtcloud`)

แสดง volumes ทั้งหมดสำหรับการติดตั้งใช้งานของคุณ:

```bash
docker volume ls | grep rtcloud
```
