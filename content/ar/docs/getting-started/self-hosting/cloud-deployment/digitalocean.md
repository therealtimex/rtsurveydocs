---
weight: 1
title: "DigitalOcean"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-17T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "water_drop"
toc: true
description: "نشر rtCloud على Droplet في DigitalOcean باستخدام سكريبتات بيانات المستخدم الآلية."
---

تستخدم DigitalOcean سكريبتات **User Data** التي تعمل تلقائياً عند التشغيل الأول. تملأ متغيرات الإعداد في أعلى السكريبت، ثم تلصق السكريبت بالكامل عند إنشاء Droplet.

> على عكس Linode StackScripts، لا توجد واجهة نموذج في DigitalOcean — يجب تعديل السكريبت مباشرةً قبل اللصق.

**تنزيل السكريبت:** [digitalocean-droplet-keycloak-embed.sh](/scripts/digitalocean-droplet-keycloak-embed.sh)

---

## Keycloak المدمج (موصى به)

استخدم `digitalocean-droplet-keycloak-embed.sh` للإعداد الأبسط مع SSO مدمج.

### الخطوة 1 — ملء الإعداد

افتح السكريبت وعدّل كتلة `CONFIGURATION` في الأعلى:

```bash
# --- مطلوب ---
PROJECT_ID="rtsurvey"                  # معرّف فريد لمشروعك (بدون مسافات)
ADMIN_PASSWORD="admin"                 # كلمة مرور مسؤول التطبيق وKeycloak — غيّرها بعد تسجيل الدخول الأول

# --- النطاق + SSL ---
DOMAIN="myapp.example.com"            # نطاقك — يجب أن يشير سجل DNS A هنا
PROJECT_URL=""                         # اتركه فارغاً ما لم يكن خلف Cloudflare/وكيل
LETSENCRYPT_EMAIL="admin@example.com" # البريد الإلكتروني لإشعارات Let's Encrypt

# --- اختياري ---
STATA_ENABLED="false"
TZ="Asia/Ho_Chi_Minh"
```

| الحقل | مطلوب | الوصف |
|-------|----------|-------------|
| `PROJECT_ID` | نعم | يُستخدم كاسم قاعدة البيانات ومعرّف عميل Keycloak. أحرف صغيرة، بدون مسافات. |
| `ADMIN_PASSWORD` | لا | كلمة مرور تسجيل الدخول الإداري للتطبيق ووحدة تحكم Keycloak الإدارية. الافتراضي `admin` — **غيّرها بعد تسجيل الدخول الأول**. |
| `DOMAIN` | نعم | اسم نطاقك. يجب أن يشير سجل DNS A إلى IP الـ Droplet. |
| `LETSENCRYPT_EMAIL` | نعم | عنوان البريد الإلكتروني لإشعارات شهادة Let's Encrypt. |
| `PROJECT_URL` | لا | تجاوز عنوان URL العام. اتركه فارغاً لاستخدام `DOMAIN`. مفيد خلف Cloudflare. |

> **الأمان:** جميع كلمات المرور افتراضها `admin`. غيّرها فوراً بعد تسجيل دخولك الأول.

### الخطوة 2 — إنشاء Droplet

في [لوحة تحكم DigitalOcean](https://cloud.digitalocean.com):

1. انقر **Create** ← **Droplets**
2. اختر **Ubuntu 22.04 LTS** كصورة
3. اختر **Basic، 4 GB RAM / 2 vCPUs** أو أعلى
4. انتقل إلى **Advanced Options** ← ضع علامة على **Add Initialization scripts**
5. الصق محتوى السكريبت الكامل في منطقة النص
6. انقر **Create Droplet**

### الخطوة 3 — إضافة سجل DNS

بينما يعمل Droplet على التشغيل، أضف **سجل A** في مزود DNS الخاص بك:

```
Type  : A
Name  : myapp          (أو @ للنطاق الجذر)
Value : <droplet-ip>
TTL   : 300
```

### الخطوة 4 — مراقبة التقدم

اتصل بـ Droplet عبر SSH وشاهد السجل:

```bash
ssh root@<droplet-ip>
tail -f /var/log/rtcloud-setup.log
```

تطبع السكريبت IP الخادم في البداية — أضف سجل DNS فور رؤيته.

### الخطوة 5 — الوصول إلى التطبيق

عند اكتمال الإعداد، يعرض السجل ملخصاً:

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

افتح `https://myapp.example.com` في متصفحك وسجّل الدخول باسم المستخدم `admin` وكلمة المرور `admin`.

> **غيّر كلمة مرورك** فوراً بعد تسجيل الدخول عبر **Settings** في القائمة العلوية اليمنى.

---

## بعد النشر

### تغيير كلمة مرور

اتصل بـ Droplet عبر SSH، وعدّل `.env`، وأعد تشغيل الحاوية المتأثرة:

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### تحديث النطاق

إذا عيّنت نطاقاً مختلفاً بعد النشر، حدّث `PROJECT_URL` في `.env`:

```bash
nano /opt/rtcloud/.env   # حدّث PROJECT_URL=
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### عرض جميع الحاويات

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```
