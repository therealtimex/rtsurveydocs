---
weight: 1
title: "DigitalOcean"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-17T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "water_drop"
toc: true
description: "ปรับใช้ rtCloud บน DigitalOcean Droplet โดยใช้สคริปต์ข้อมูลผู้ใช้อัตโนมัติ"
---

DigitalOcean ใช้สคริปต์ **ข้อมูลผู้ใช้** ที่ทำงานโดยอัตโนมัติเมื่อบูตครั้งแรก คุณกรอกตัวแปรการกำหนดค่าที่ด้านบนของสคริปต์ จากนั้นวางสคริปต์ทั้งหมดเมื่อสร้าง Droplet

> ต่างจาก Linode StackScripts ตรงที่ DigitalOcean ไม่มี UI ของฟอร์ม — คุณต้องแก้ไขสคริปต์โดยตรงก่อนที่จะวาง

**Download script:** [digitalocean-droplet-keycloak-embed.sh](/scripts/digitalocean-droplet-keycloak-embed.sh)

---

## Keycloak แบบฝัง (แนะนำ)

ใช้ `digitalocean-droplet-keycloak-embed.sh` เพื่อการตั้งค่าที่ง่ายที่สุดด้วย SSO ในตัว

### ขั้นตอนที่ 1 — กรอกการกำหนดค่า

เปิดสคริปต์และแก้ไขบล็อก `CONFIGURATION` ที่ด้านบน:

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

| สนาม | จำเป็น | คำอธิบาย |
|-------|----------|-------------|
| `โครงการ_ID` | ใช่ | ใช้เป็นชื่อฐานข้อมูลและรหัสไคลเอ็นต์ Keycloak ตัวพิมพ์เล็กไม่มีช่องว่าง |
| `ADMIN_PASSWORD` | ไม่ | รหัสผ่านสำหรับการเข้าสู่ระบบผู้ดูแลระบบแอปและคอนโซลผู้ดูแลระบบ Keycloak ค่าเริ่มต้นคือ `admin` — **เปลี่ยนหลังจากเข้าสู่ระบบครั้งแรก** |
| `โดเมน` | ใช่ | ชื่อโดเมนของคุณ DNS ระเบียนจะต้องชี้ไปที่ Droplet IP |
| `LETSENCRYPT_EMAIL` | ใช่ | ที่อยู่อีเมลสำหรับการแจ้งเตือนใบรับรอง Let's Encrypt |
| `PROJECT_URL` | ไม่ | แทนที่ URL สาธารณะ เว้นว่างไว้เพื่อใช้ `DOMAIN` มีประโยชน์เบื้องหลัง Cloudflare |

> **ความปลอดภัย:** รหัสผ่านทั้งหมดมีค่าเริ่มต้นเป็น `admin` เปลี่ยนทันทีหลังจากการเข้าสู่ระบบครั้งแรกของคุณ

### ขั้นตอนที่ 2 — สร้าง Droplet

In the [DigitalOcean control panel](https://cloud.digitalocean.com):

1. คลิก **สร้าง** → **หยด**
2. เลือก **Ubuntu 22.04 LTS** เป็นรูปภาพ
3. เลือก **พื้นฐาน, RAM 4 GB / 2 vCPUs** หรือใหญ่กว่า
4. เลื่อนไปที่ **ตัวเลือกขั้นสูง** → ทำเครื่องหมาย **เพิ่มสคริปต์การเริ่มต้น**
5. วางเนื้อหาสคริปต์แบบเต็มลงในพื้นที่ข้อความ
6. คลิก **สร้าง Droplet**

### ขั้นตอนที่ 3 — เพิ่มระเบียน DNS

ในขณะที่ Droplet บู๊ต ให้เพิ่ม **บันทึก** ในผู้ให้บริการ DNS ของคุณ:

```
Type  : A
Name  : myapp          (or @ for root domain)
Value : <droplet-ip>
TTL   : 300
```

### ขั้นตอนที่ 4 — ติดตามความคืบหน้า

SSH เข้าสู่ Droplet และดูบันทึก:

```bash
ssh root@<droplet-ip>
tail -f /var/log/rtcloud-setup.log
```

สคริปต์จะพิมพ์ IP เซิร์ฟเวอร์ของคุณใกล้กับจุดเริ่มต้น — เพิ่มบันทึก DNS ทันทีที่คุณเห็น

### ขั้นตอนที่ 5 — เข้าถึงแอป

เมื่อการตั้งค่าเสร็จสมบูรณ์ บันทึกจะแสดงข้อมูลสรุป:

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

> **เปลี่ยนรหัสผ่าน** ทันทีหลังจากเข้าสู่ระบบผ่าน **การตั้งค่า** ในเมนูด้านบนขวา

---

## หลังจากการปรับใช้

### เปลี่ยนรหัสผ่าน

SSH ลงใน Droplet แก้ไข `.env` และรีสตาร์ทคอนเทนเนอร์ที่ได้รับผลกระทบ:

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### อัพเดทโดเมน

หากคุณกำหนดโดเมนอื่นหลังจากการปรับใช้ ให้อัปเดต `PROJECT_URL` ใน `.env`:

```bash
nano /opt/rtcloud/.env   # update PROJECT_URL=
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### ดูคอนเทนเนอร์ทั้งหมด

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```
