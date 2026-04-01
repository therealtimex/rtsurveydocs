---
weight: 5
title: "การบำรุงรักษา"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "build"
toc: true
description: "การบำรุงรักษาประจำวันสำหรับอินสแตนซ์ rtCloud แบบโฮสต์ด้วยตนเอง: การอัปเกรด การสำรองข้อมูล การกู้คืน และการแก้ไขปัญหาทั่วไป"
---

## คำสั่งทั่วไป

ใช้คำสั่งเหล่านี้เป็นประจำเพื่อจัดการคอนเทนเนอร์ rtCloud ของคุณ รันจากไดเรกทอรีที่มี `docker-compose.production.yml`

```bash
# ตรวจสอบสถานะและความสมบูรณ์ของคอนเทนเนอร์ทั้งหมด
docker compose -f docker-compose.production.yml ps

# ดูล็อกสด (ทุกบริการ)
docker compose -f docker-compose.production.yml logs -f

# ดูล็อกเฉพาะแอป
docker compose -f docker-compose.production.yml logs -f rtcloud

# รีสตาร์ทคอนเทนเนอร์เดียว
docker compose -f docker-compose.production.yml restart rtcloud

# หยุดบริการทั้งหมด
docker compose -f docker-compose.production.yml down

# เริ่มบริการทั้งหมด
docker compose -f docker-compose.production.yml up -d

# เปิด shell ภายในคอนเทนเนอร์แอป
docker compose -f docker-compose.production.yml exec rtcloud bash
```

---

## การอัปเกรด

การอัปเดต rtCloud แจกจ่ายเป็น Docker image tag ใหม่ การอัปเกรดดึง image ล่าสุดและสร้างคอนเทนเนอร์แอปใหม่ การย้ายฐานข้อมูลทำงานโดยอัตโนมัติเมื่อเริ่มต้น

**1. ดึง image ล่าสุด:**

```bash
docker compose -f docker-compose.production.yml pull
```

**2. สร้างคอนเทนเนอร์แอปใหม่:**

```bash
docker compose -f docker-compose.production.yml up -d
```

Docker จะแทนที่เฉพาะคอนเทนเนอร์ที่ image เปลี่ยนแปลง คอนเทนเนอร์ MySQL และ volumes ที่มีชื่อทั้งหมดไม่ได้รับผลกระทบ

### การปักหมุดเวอร์ชัน

เพื่ออัปเกรดไปยังเวอร์ชันเฉพาะแทนที่จะเป็น `latest` ให้อัปเดต `RTCLOUD_IMAGE` ใน `.env`:

```dotenv
RTCLOUD_IMAGE=rtawebteam/rta-smartsurvey:1.2.3
```

แล้วรัน `docker compose pull` และ `up -d` ตามด้านบน

### การดาวน์เกรด

โดยทั่วไปไม่แนะนำการดาวน์เกรด เนื่องจากไม่สามารถย้อนกลับการย้ายฐานข้อมูลได้ หากจำเป็นต้องดาวน์เกรด ให้กู้คืนจากการสำรองข้อมูลฐานข้อมูลที่ทำก่อนการอัปเกรด

---

## การสำรองข้อมูลและการกู้คืน

### สำรองข้อมูลฐานข้อมูล

รันคำสั่งนี้เพื่อส่งออกฐานข้อมูลแอปพลิเคชันเป็นไฟล์ SQL:

```bash
docker compose -f docker-compose.production.yml exec mysql \
  mysqldump -u root -p"$(grep MYSQL_ROOT_PASSWORD .env | cut -d= -f2)" smartsurvey \
  > backup-$(date +%Y%m%d-%H%M%S).sql
```

ไฟล์สำรองข้อมูลถูกเขียนไปยังไดเรกทอรีปัจจุบันของคุณบนโฮสต์

### กู้คืนฐานข้อมูล

```bash
docker compose -f docker-compose.production.yml exec -T mysql \
  mysql -u root -p"$(grep MYSQL_ROOT_PASSWORD .env | cut -d= -f2)" smartsurvey \
  < backup-20240101-120000.sql
```

### สำรองข้อมูลไฟล์ที่อัปโหลด

การส่งแบบสำรวจมักรวมถึงไฟล์ที่อัปโหลด (รูปภาพ เสียง เอกสาร) ที่จัดเก็บใน Docker volumes ที่มีชื่อ สำรองข้อมูลแยกจากฐานข้อมูล:

```bash
# สำรองข้อมูล uploads
docker run --rm \
  -v rtcloud_uploads:/data \
  -v "$(pwd):/backup" \
  alpine tar czf /backup/uploads-$(date +%Y%m%d).tar.gz -C /data .

# สำรองข้อมูลการบันทึกเสียง
docker run --rm \
  -v rtcloud_audios:/data \
  -v "$(pwd):/backup" \
  alpine tar czf /backup/audios-$(date +%Y%m%d).tar.gz -C /data .
```

### กู้คืนไฟล์ที่อัปโหลด

```bash
docker run --rm \
  -v rtcloud_uploads:/data \
  -v "$(pwd):/backup" \
  alpine tar xzf /backup/uploads-20240101.tar.gz -C /data
```

### การสำรองข้อมูลรายวันอัตโนมัติ

เพิ่มงาน cron บนโฮสต์เพื่อรันการสำรองข้อมูลโดยอัตโนมัติ แก้ไข root crontab ด้วย `crontab -e`:

```cron
# สำรองข้อมูลฐานข้อมูลรายวันเวลา 2:00 AM เก็บประวัติ 30 วัน
0 2 * * * cd /opt/rtcloud && docker compose -f docker-compose.production.yml exec -T mysql \
  mysqldump -u root -p"$(grep MYSQL_ROOT_PASSWORD .env | cut -d= -f2)" smartsurvey \
  > /backups/db-$(date +\%Y\%m\%d).sql && \
  find /backups -name "db-*.sql" -mtime +30 -delete
```

---

## การแก้ไขปัญหา

### คอนเทนเนอร์แอปไม่เริ่มต้น

ตรวจสอบล็อกคอนเทนเนอร์สำหรับข้อความข้อผิดพลาด:

```bash
docker compose -f docker-compose.production.yml logs rtcloud
```

สาเหตุทั่วไป:
- ตัวแปรสภาพแวดล้อมที่หายไปหรือไม่ถูกต้องใน `.env`
- MySQL ยังไม่พร้อม (รอ 60 วินาทีและตรวจสอบอีกครั้ง)
- ความขัดแย้งของพอร์ต — กระบวนการอื่นใช้ `APP_PORT` อยู่แล้ว

### MySQL ไม่มีสุขภาพ

```bash
docker compose -f docker-compose.production.yml logs mysql
```

สาเหตุทั่วไป:
- `MYSQL_ROOT_PASSWORD` ไม่ได้ตั้งค่าใน `.env`
- data volume เสียหาย (หายาก — ตรวจสอบพื้นที่ดิสก์ด้วย `df -h`)

MySQL อาจใช้เวลา 30–60 วินาทีในการเริ่มต้นบูตครั้งแรก รอและตรวจสอบอีกครั้งก่อนสรุปว่าล้มเหลว

### พอร์ตถูกใช้งานอยู่แล้ว

เปลี่ยน `APP_PORT` หรือ `SHINY_PORT` ใน `.env` เป็นพอร์ตที่ว่าง แล้วสร้างคอนเทนเนอร์ใหม่:

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate
```

เพื่อหาว่าอะไรกำลังใช้พอร์ตบนโฮสต์:

```bash
lsof -i :8080
```

### 400 CSRF Token Could Not Be Verified

ข้อผิดพลาดนี้ปรากฏในสภาพแวดล้อมภายในเครื่องหรือ reverse-proxy ที่ origin ของคำขอไม่ตรงกับโฮสต์ที่คาดหวัง ปิดใช้งานการตรวจสอบ CSRF สำหรับการพัฒนาภายในเครื่องเท่านั้น:

```dotenv
CSRF_VALIDATION_ENABLED=false
```

แล้วรีสตาร์ทแอป:

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

> อย่าปิดใช้งานการตรวจสอบ CSRF ในการผลิต หากข้อผิดพลาดนี้เกิดขึ้นในการผลิต ให้ตรวจสอบว่า reverse proxy ของคุณส่ง header `Host` และ `X-Forwarded-For` ที่ถูกต้อง

### ลืมรหัสผ่านผู้ดูแลระบบ

รีเซ็ตรหัสผ่านผู้ดูแลระบบโดยตรงในฐานข้อมูล เชื่อมต่อกับคอนเทนเนอร์ MySQL และอัปเดต hash รหัสผ่าน:

**ขั้นตอนที่ 1** — สร้าง hash รหัสผ่านใหม่ แทนที่ `newpassword` ด้วยรหัสผ่านที่ต้องการ:

```bash
docker compose -f docker-compose.production.yml exec rtcloud php -r "
  \$salt = trim(shell_exec(\"mysql -h mysql -u root -p\\\"\${MYSQL_ROOT_PASSWORD}\\\" \${MYSQL_DATABASE} -se \\\"SELECT salt FROM ss_user WHERE username='admin';\\\"\")); 
  echo md5(\$salt . 'newpassword') . PHP_EOL;
"
```

**ขั้นตอนที่ 2** — อัปเดต hash ในฐานข้อมูล:

```bash
docker compose -f docker-compose.production.yml exec mysql \
  mysql -u root -p"${MYSQL_ROOT_PASSWORD}" smartsurvey \
  -e "UPDATE ss_user SET password='<hash_from_step_1>' WHERE username='admin';"
```

### คอนเทนเนอร์รีสตาร์ทซ้ำๆ

ตรวจสอบว่า health check ล้มเหลวหรือไม่:

```bash
docker compose -f docker-compose.production.yml ps
docker inspect rtcloud-app --format '{{json .State.Health}}'
```

health check ของแอปเรียก endpoint `/health` หากล้มเหลวซ้ำๆ ให้ตรวจสอบล็อกแอปพลิเคชันสำหรับข้อผิดพลาดการเริ่มต้น

### พื้นที่ดิสก์เต็ม

ระบุว่าอะไรกำลังใช้พื้นที่:

```bash
# ตรวจสอบการใช้ดิสก์โฮสต์
df -h

# ตรวจสอบการใช้ดิสก์ Docker (images, containers, volumes)
docker system df

# ลบ images ที่ไม่ได้ใช้และคอนเทนเนอร์ที่หยุดแล้ว (ปลอดภัยที่จะรัน)
docker system prune
```

อย่าใช้ `docker system prune --volumes` เพราะจะลบข้อมูลแอปพลิเคชัน

---

## Health Checks

แต่ละบริการมี health check อัตโนมัติ สถานะคอนเทนเนอร์สะท้อนผลลัพธ์:

| คอนเทนเนอร์ | วิธีการตรวจสอบ | ระยะเวลาเริ่มต้น | ช่วงเวลา |
|-----------|-------------|-------------|----------|
| `rtcloud-app` | HTTP GET `/health` | 90 วินาที | 30 วินาที |
| `rtcloud-mysql` | `mysqladmin ping` | 30 วินาที | 10 วินาที |
| `rtcloud-keycloak` | HTTP GET `:9000/health/live` | 120 วินาที | 30 วินาที |

คอนเทนเนอร์ที่มี health check ล้มเหลวจะถูกรีสตาร์ทโดยอัตโนมัติตามการตั้งค่า `RESTART_POLICY` (ค่าเริ่มต้น: `unless-stopped`)
