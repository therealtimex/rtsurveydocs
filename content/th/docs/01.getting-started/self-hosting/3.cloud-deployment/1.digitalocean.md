---
weight: 1
title: "DigitalOcean"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-17T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "water_drop"
toc: true
description: "ติดตั้ง rtCloud บน DigitalOcean Droplet โดยใช้สคริปต์ user-data อัตโนมัติ"
---

DigitalOcean ใช้สคริปต์ **User Data** ที่ทำงานอัตโนมัติเมื่อบูตครั้งแรก คุณกรอกตัวแปรการกำหนดค่าที่ด้านบนของสคริปต์ แล้ววางสคริปต์ทั้งหมดเมื่อสร้าง Droplet

> ต่างจาก Linode StackScripts DigitalOcean ไม่มี UI แบบฟอร์ม — คุณต้องแก้ไขสคริปต์โดยตรงก่อนวาง

**ดาวน์โหลดสคริปต์:** [digitalocean-droplet-keycloak-embed.sh](/scripts/digitalocean-droplet-keycloak-embed.sh)

---

## Keycloak แบบฝัง (แนะนำ)

ใช้ `digitalocean-droplet-keycloak-embed.sh` สำหรับการตั้งค่าที่ง่ายที่สุดพร้อม SSO ในตัว

### ขั้นตอนที่ 1 — กรอกการกำหนดค่า

เปิดสคริปต์และแก้ไขบล็อก `CONFIGURATION` ที่ด้านบน:

```bash
# --- ต้องมี ---
PROJECT_ID="rtsurvey"                  # ตัวระบุเฉพาะสำหรับโครงการ (ไม่มีช่องว่าง)
ADMIN_PASSWORD="admin"                 # รหัสผ่านสำหรับผู้ดูแลระบบแอปและ Keycloak — เปลี่ยนหลังเข้าสู่ระบบครั้งแรก

# --- โดเมน + SSL ---
DOMAIN="myapp.example.com"            # โดเมนของคุณ — DNS A record ต้องชี้ที่นี่
PROJECT_URL=""                         # เว้นว่างเว้นแต่อยู่หลัง Cloudflare/proxy
LETSENCRYPT_EMAIL="admin@example.com" # อีเมลสำหรับการแจ้งเตือน Let's Encrypt

# --- ไม่บังคับ ---
STATA_ENABLED="false"
TZ="Asia/Ho_Chi_Minh"
```

| ฟิลด์ | ต้องมี | คำอธิบาย |
|-------|----------|-------------|
| `PROJECT_ID` | ใช่ | ใช้เป็นชื่อฐานข้อมูลและ Keycloak client ID ตัวเล็ก ไม่มีช่องว่าง |
| `ADMIN_PASSWORD` | ไม่ | รหัสผ่านสำหรับเข้าสู่ระบบผู้ดูแลระบบแอปและคอนโซลผู้ดูแลระบบ Keycloak ค่าเริ่มต้นเป็น `admin` — **เปลี่ยนหลังเข้าสู่ระบบครั้งแรก** |
| `DOMAIN` | ใช่ | ชื่อโดเมนของคุณ DNS A record ต้องชี้ไปยัง IP ของ Droplet |
| `LETSENCRYPT_EMAIL` | ใช่ | ที่อยู่อีเมลสำหรับการแจ้งเตือนใบรับรอง Let's Encrypt |
| `PROJECT_URL` | ไม่ | แทนที่ URL สาธารณะ เว้นว่างเพื่อใช้ `DOMAIN` มีประโยชน์หลัง Cloudflare |

> **ความปลอดภัย:** รหัสผ่านทั้งหมดเริ่มต้นเป็น `admin` เปลี่ยนทันทีหลังจากเข้าสู่ระบบครั้งแรก

### ขั้นตอนที่ 2 — สร้าง Droplet

ในแผงควบคุม [DigitalOcean](https://cloud.digitalocean.com):

1. คลิก **Create** → **Droplets**
2. เลือก **Ubuntu 22.04 LTS** เป็น image
3. เลือก **Basic, 4 GB RAM / 2 vCPUs** หรือใหญ่กว่า
4. เลื่อนไปที่ **Advanced Options** → ทำเครื่องหมาย **Add Initialization scripts**
5. วางเนื้อหาสคริปต์ทั้งหมดในพื้นที่ข้อความ
6. คลิก **Create Droplet**

### ขั้นตอนที่ 3 — เพิ่ม DNS record

ขณะที่ Droplet บูต ให้เพิ่ม **A record** ในผู้ให้บริการ DNS ของคุณ:

```
Type  : A
Name  : myapp          (หรือ @ สำหรับ root domain)
Value : <droplet-ip>
TTL   : 300
```

### ขั้นตอนที่ 4 — ตรวจสอบความคืบหน้า

SSH เข้าสู่ Droplet และดูล็อก:

```bash
ssh root@<droplet-ip>
tail -f /var/log/rtcloud-setup.log
```

สคริปต์แสดง IP ของเซิร์ฟเวอร์ใกล้กับจุดเริ่มต้น — เพิ่ม DNS record ทันทีที่คุณเห็น

### ขั้นตอนที่ 5 — เข้าถึงแอป

เมื่อการตั้งค่าเสร็จสิ้น ล็อกแสดงสรุป:

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

เปิด `https://myapp.example.com` ในเบราว์เซอร์และเข้าสู่ระบบด้วยชื่อผู้ใช้ `admin` และรหัสผ่าน `admin`

> **เปลี่ยนรหัสผ่านของคุณ** ทันทีหลังจากเข้าสู่ระบบผ่าน **Settings** ในเมนูด้านบนขวา

---

## หลังการติดตั้ง

### เปลี่ยนรหัสผ่าน

SSH เข้าสู่ Droplet แก้ไข `.env` และรีสตาร์ทคอนเทนเนอร์ที่ได้รับผลกระทบ:

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### อัปเดตโดเมน

หากคุณกำหนดโดเมนอื่นหลังการติดตั้ง ให้อัปเดต `PROJECT_URL` ใน `.env`:

```bash
nano /opt/rtcloud/.env   # อัปเดต PROJECT_URL=
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### ดูคอนเทนเนอร์ทั้งหมด

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```
