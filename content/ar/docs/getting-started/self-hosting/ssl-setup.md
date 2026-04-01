---
weight: 4
title: "إعداد SSL"
date: "2026-04-01T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "lock"
toc: true
description: "تكوين HTTPS لخادم rtSurvey الخاص بك. مطلوب قبل تسجيل الدخول."
---

يجب تكوين SSL قبل تسجيل الدخول. عند فتح التطبيق لأول مرة، ستتم إعادة توجيهك تلقائياً إلى شاشة إعداد SSL.

---

## خيارات إعداد SSL

![خيارات إعداد SSL](/img/ssl-setup/ssl-setup-options.png)

اختر أحد الخيارات الثلاثة:

| الخيار | متى تستخدمه |
|--------|-------------|
| **نطاق فرعي مجاني من rtsurvey.com** *(موصى به)* | لا حاجة لإعداد DNS. نقوم بإنشاء السجل نيابةً عنك. جاهز في 2–5 دقائق. |
| **نطاقي الخاص** | لديك نطاق بالفعل ويشير DNS الخاص به إلى هذا الخادم. |
| **تثبيت الشهادة يدوياً** | للمؤسسات أو CA مخصص. يتطلب وصول SSH. |

---

## الخيار 1 — نطاق فرعي مجاني من rtsurvey.com *(موصى به)*

هذا هو الخيار الأسرع. لا حاجة لتسجيل نطاق أو تغييرات DNS.

1. انقر على **نطاق فرعي مجاني من rtsurvey.com** لتوسيع القسم
2. اكتب اسم النطاق الفرعي المطلوب في حقل الإدخال

   > استخدم أحرفاً صغيرة وأرقاماً وشرطات. 3–30 حرفاً.
   > مثال: `myproject` ← `myproject.rtsurvey.com`

3. انقر على **إنشاء https://[subdomain].rtsurvey.com**

<!-- SCREENSHOT NEEDED: subdomain input filled in, before clicking Create -->

4. انتظر 2–5 دقائق أثناء إصدار الشهادة

<!-- SCREENSHOT NEEDED: certificate being issued / progress state -->

5. بمجرد جاهزية الشهادة، ستتم إعادة توجيهك تلقائياً إلى عنوان HTTPS الجديد

<!-- SCREENSHOT NEEDED: success state / redirect to login -->

---

## الخيار 2 — نطاقي الخاص

استخدم هذا إذا كان لديك نطاق موجود وسجل DNS `A` يشير بالفعل إلى IP هذا الخادم.

1. انقر على **نطاقي الخاص** لتوسيع القسم
2. أدخل اسم النطاق الكامل (مثل `survey.myorganization.org`)
3. انقر على **إنشاء شهادة**

<!-- SCREENSHOT NEEDED: own domain input form -->

سيتحقق Let's Encrypt من نطاقك ويصدر شهادة. يتطلب ذلك توجيه DNS بشكل صحيح مسبقاً — وإلا سيفشل الطلب.

---

## الخيار 3 — تثبيت الشهادة يدوياً

لبيئات المؤسسات التي تستخدم CA مخصصاً أو داخلياً. ستضع ملفات الشهادة على الخادم عبر SSH ثم تدخل نطاقك في التطبيق.

### المتطلبات الأساسية

- وصول SSH إلى الخادم
- شهادة صالحة ومفتاح خاص لنطاقك (بتنسيق PEM)

### الخطوة 1 — الاتصال بالخادم عبر SSH

```bash
ssh root@<server-ip>
```

### الخطوة 2 — وضع ملفات الشهادة

أنشئ المجلد وانسخ ملفاتك:

```bash
mkdir -p /etc/letsencrypt/live/<your-domain>
```

انسخ ملفاتك إلى ذلك المجلد بهذه الأسماء الدقيقة:

| الملف | الوصف |
|-------|-------|
| `fullchain.pem` | شهادتك + أي شهادات CA وسيطة (مدمجة) |
| `privkey.pem` | مفتاحك الخاص |

مثال:

```bash
# نسخ من جهازك المحلي (شغّل هذا محلياً، ليس على الخادم)
scp fullchain.pem root@<server-ip>:/etc/letsencrypt/live/<your-domain>/fullchain.pem
scp privkey.pem  root@<server-ip>:/etc/letsencrypt/live/<your-domain>/privkey.pem
```

تعيين الصلاحيات الصحيحة:

```bash
chmod 644 /etc/letsencrypt/live/<your-domain>/fullchain.pem
chmod 600 /etc/letsencrypt/live/<your-domain>/privkey.pem
```

### الخطوة 3 — إدخال نطاقك في التطبيق

<!-- SCREENSHOT NEEDED: manual certificate form -->

1. في شاشة إعداد SSL، انقر على **تثبيت الشهادة يدوياً**
2. أدخل اسم نطاقك (يجب أن يتطابق مع الاسم الشائع للشهادة أو SAN)
3. انقر على **تطبيق**

سيقوم الخادم بتكوين Nginx مع شهادتك وإعادة التحميل تلقائياً.

---

## الخطوة التالية

بعد تفعيل SSL، انتقل إلى [تسجيل الدخول الأول](first-login).
