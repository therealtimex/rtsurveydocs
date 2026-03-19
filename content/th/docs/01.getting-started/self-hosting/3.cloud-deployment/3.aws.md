---
weight: 3
title: "AWS EC2"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-16T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "cloud"
toc: true
description: "ติดตั้ง rtCloud บนอินสแตนซ์ AWS EC2 โดยใช้สคริปต์ user data aws-ec2.sh"
---

ใช้ `aws-ec2.sh` เป็นสคริปต์ **User Data** เมื่อเปิดใช้งานอินสแตนซ์ EC2 สคริปต์ทำงานอัตโนมัติเมื่อบูตครั้งแรก

**ดาวน์โหลดสคริปต์:** [aws-ec2.sh](/scripts/aws-ec2.sh)

---

## ขั้นตอนที่ 1 — กรอกการกำหนดค่า

เปิดสคริปต์และแก้ไขบล็อก `CONFIGURATION` ที่ด้านบน:

```bash
# --- ต้องมี ---
PROJECT_ID="rtsurvey"
ADMIN_PASSWORD="admin"                       # เปลี่ยนหลังเข้าสู่ระบบครั้งแรก

# --- โดเมน + SSL ---
DOMAIN="myapp.example.com"
LETSENCRYPT_EMAIL="admin@example.com"

# --- Keycloak แบบฝัง ---
EMBED_KEYCLOAK="true"
KEYCLOAK_ADMIN_PASSWORD="${ADMIN_PASSWORD}"  # ค่าเริ่มต้นเป็น ADMIN_PASSWORD
```

| ฟิลด์ | ต้องมี | คำอธิบาย |
|-------|----------|-------------|
| `PROJECT_ID` | ใช่ | ใช้เป็นชื่อฐานข้อมูลและ Keycloak client ID ตัวเล็ก ไม่มีช่องว่าง |
| `ADMIN_PASSWORD` | ไม่ | รหัสผ่านผู้ดูแลระบบแอปและ Keycloak ค่าเริ่มต้นเป็น `admin` — **เปลี่ยนหลังเข้าสู่ระบบครั้งแรก** |
| `DOMAIN` | ไม่ | โดเมนของคุณสำหรับ HTTPS เว้นว่างสำหรับโหมด HTTP เท่านั้น |
| `LETSENCRYPT_EMAIL` | ใช่ (ถ้าตั้ง DOMAIN) | อีเมลสำหรับการแจ้งเตือน Let's Encrypt |
| `EMBED_KEYCLOAK` | ไม่ | `true` เพื่อติดตั้ง Keycloak แบบฝัง (ต้องการ RAM 4 GB) |

> **ความปลอดภัย:** รหัสผ่านทั้งหมดเริ่มต้นเป็น `admin` เปลี่ยนทันทีหลังจากเข้าสู่ระบบครั้งแรก

---

## ขั้นตอนที่ 2 — เปิดใช้งานอินสแตนซ์ EC2

ใน [AWS EC2 console](https://console.aws.amazon.com/ec2):

1. คลิก **Launch instance**
2. **AMI:** Ubuntu Server 22.04 LTS (64-bit x86)
3. **Instance type:** `t3.medium` (4 GB RAM) หรือใหญ่กว่า
4. **Key pair:** เลือกหรือสร้างสำหรับการเข้าถึง SSH
5. **Network settings:** สร้างหรือเลือก Security Group (ดูด้านล่าง)
6. **Advanced details** → **User data** → วางเนื้อหาสคริปต์ทั้งหมด
7. คลิก **Launch instance**

---

## ขั้นตอนที่ 3 — กำหนดค่า Security Group

เปิดพอร์ตเหล่านี้ใน Security Group ของอินสแตนซ์:

| พอร์ต | โปรโตคอล | ต้นทาง | วัตถุประสงค์ |
|------|----------|--------|---------|
| 22 | TCP | IP ของคุณ | การเข้าถึง SSH |
| 80 | TCP | 0.0.0.0/0 | HTTP (เปลี่ยนเส้นทางไปยัง HTTPS โดย Nginx) |
| 443 | TCP | 0.0.0.0/0 | HTTPS |
| 3838 | TCP | 0.0.0.0/0 | การเข้าถึง Shiny โดยตรง |

> **อย่า** เปิดพอร์ต 3306 (MySQL) — ไม่ควรเข้าถึงได้สาธารณะ

---

## ขั้นตอนที่ 4 — เพิ่ม DNS record

ขณะที่อินสแตนซ์บูต ให้เพิ่ม **A record** ในผู้ให้บริการ DNS ของคุณ:

```
Type  : A
Name  : myapp
Value : <instance-public-ip>
TTL   : 300
```

---

## ขั้นตอนที่ 5 — ตรวจสอบความคืบหน้า

```bash
ssh ubuntu@<instance-ip>
tail -f /var/log/rtcloud-setup.log
```

---

## ขั้นตอนที่ 6 — เข้าถึงแอป

เมื่อการตั้งค่าเสร็จสิ้น ล็อกแสดงสรุปพร้อม URL แอปและข้อมูลประจำตัว เข้าสู่ระบบด้วยชื่อผู้ใช้ `admin` และรหัสผ่าน `admin` แล้วเปลี่ยนรหัสผ่านทันที

---

## หลังการติดตั้ง

### เปลี่ยนรหัสผ่าน

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### ดูคอนเทนเนอร์ทั้งหมด

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```

### กำหนด Elastic IP (ไม่บังคับ)

หากคุณหยุดและเริ่มอินสแตนซ์ IP สาธารณะจะเปลี่ยน เพื่อรักษา IP ที่เสถียร ให้จัดสรร **Elastic IP** และเชื่อมโยงกับอินสแตนซ์ใน EC2 console
