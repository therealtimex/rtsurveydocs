---
weight: 4
title: "Google Cloud (GCP)"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-16T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "travel_explore"
toc: true
description: "نشر rtCloud على Google Cloud Compute Engine باستخدام سكريبت التشغيل gcp-compute.sh."
---

استخدم `gcp-compute.sh` كـ **Startup script** عند إنشاء نسخة VM في Compute Engine. تعمل السكريبت تلقائياً عند التشغيل الأول.

**تنزيل السكريبت:** [gcp-compute.sh](/scripts/gcp-compute.sh)

---

## الخطوة 1 — ملء الإعداد

افتح السكريبت وعدّل كتلة `CONFIGURATION` في الأعلى:

```bash
# --- مطلوب ---
PROJECT_ID="rtsurvey"
ADMIN_PASSWORD="admin"                       # غيّرها بعد تسجيل الدخول الأول

# --- النطاق + SSL ---
DOMAIN="myapp.example.com"
LETSENCRYPT_EMAIL="admin@example.com"

# --- Keycloak المدمج ---
EMBED_KEYCLOAK="true"
KEYCLOAK_ADMIN_PASSWORD="${ADMIN_PASSWORD}"  # الافتراضي ADMIN_PASSWORD
```

| الحقل | مطلوب | الوصف |
|-------|----------|-------------|
| `PROJECT_ID` | نعم | يُستخدم كاسم قاعدة البيانات ومعرّف عميل Keycloak. أحرف صغيرة، بدون مسافات. |
| `ADMIN_PASSWORD` | لا | كلمة مرور مسؤول التطبيق وكلمة مرور مسؤول Keycloak. الافتراضي `admin` — **غيّرها بعد تسجيل الدخول الأول**. |
| `DOMAIN` | لا | نطاقك لـ HTTPS. اتركه فارغاً للوضع HTTP فقط. |
| `LETSENCRYPT_EMAIL` | نعم (إذا ضُبط DOMAIN) | البريد الإلكتروني لإشعارات Let's Encrypt. |
| `EMBED_KEYCLOAK` | لا | `true` لنشر Keycloak المدمج (يتطلب 4 GB RAM). |

> **الأمان:** جميع كلمات المرور افتراضها `admin`. غيّرها فوراً بعد تسجيل دخولك الأول.

---

## الخطوة 2 — إنشاء نسخة VM

في [وحدة تحكم Google Cloud](https://console.cloud.google.com/compute):

1. انقر **Create instance**
2. **إعداد الجهاز:**
   - السلسلة: `E2`
   - نوع الجهاز: `e2-medium` (4 GB RAM) أو أعلى
3. **قرص التشغيل:**
   - نظام التشغيل: Ubuntu
   - الإصدار: Ubuntu 22.04 LTS
   - الحجم: 40 GB أو أكثر
4. **جدار الحماية:** ضع علامة على **Allow HTTP traffic** و**Allow HTTPS traffic**
5. **الخيارات المتقدمة** ← **Management** ← **Automation** ← **Startup script** ← الصق محتوى السكريبت الكامل
6. انقر **Create**

---

## الخطوة 3 — إضافة سجل DNS

بينما تعمل الـ VM على التشغيل، أضف **سجل A** في مزود DNS الخاص بك:

```
Type  : A
Name  : myapp
Value : <vm-external-ip>
TTL   : 300
```

ابحث عن IP الخارجي في قائمة نسخ VM في وحدة التحكم.

---

## الخطوة 4 — مراقبة التقدم

باستخدام أداة سطر الأوامر `gcloud`:

```bash
gcloud compute ssh <instance-name> -- tail -f /var/log/rtcloud-setup.log
```

أو الاتصال مباشرةً عبر SSH:

```bash
ssh <username>@<vm-external-ip>
tail -f /var/log/rtcloud-setup.log
```

---

## الخطوة 5 — الوصول إلى التطبيق

عند اكتمال الإعداد، يعرض السجل ملخصاً مع عنوان URL التطبيق وبيانات الاعتماد. سجّل الدخول باسم المستخدم `admin` وكلمة المرور `admin`، ثم غيّر كلمة مرورك فوراً.

---

## قواعد جدار الحماية

تفتح مربعات اختيار **Allow HTTP/HTTPS** في GCP المنافذ 80 و443. للسماح أيضاً بوصول مباشر لـ Shiny على المنفذ 3838، أضف قاعدة جدار حماية:

```bash
gcloud compute firewall-rules create allow-shiny \
  --allow tcp:3838 \
  --target-tags http-server
```

أو أضفها عبر وحدة التحكم: **VPC Network** ← **Firewall** ← **Create rule**.

> **لا** تفتح المنفذ 3306 (MySQL) — يجب ألا يكون متاحاً للعموم أبداً.

---

## IP ثابت (اختياري)

بشكل افتراضي، تُعيّن GCP عنوان IP خارجياً مؤقتاً يتغير عند إعادة تشغيل الـ VM. للحفاظ على IP ثابت:

1. اذهب إلى **VPC Network** ← **IP addresses**
2. انقر **Reserve external static address**
3. عيّنه لنسخة الـ VM الخاصة بك

---

## بعد النشر

### تغيير كلمة مرور

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### عرض جميع الحاويات

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```
