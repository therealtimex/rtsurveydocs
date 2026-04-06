---
title: "تخطيط الشبكة"
description: "يتيح تخطيط الشبكة تحديد مواضع الحقول في شبكة CSS داخل مجموعة، مما يُتيح تصاميم نماذج متعددة الأعمدة."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 296
---

تتيح ميزة **تخطيط الشبكة** ترتيب الأسئلة في **شبكة متعددة الأعمدة** داخل مجموعة، باستخدام علامة مظهر `gridformat<>`. هذا مفيد لنماذج إدخال البيانات الكثيفة حيث يجب أن تظهر عدة حقول ذات صلة جنباً إلى جنب بدلاً من التكديس رأسياً.

---

## كيف يعمل

يُطبَّق تخطيط الشبكة على مستويين:

1. **المجموعة** — اضبط `appearance: field-list grid(weight=N)` لتحديد عدد أعمدة الشبكة
2. **كل حقل داخل المجموعة** — اضبط `appearance: gridformat<row=R col=C colspan=S/>` لتحديد موضع الحقل

تستخدم الشبكة نظام Bootstrap ذو 12 عموداً. يُحدد `weight=N` عدد الأعمدة المنطقية في شبكتك؛ كل عمود يشغل `12/N` من أعمدة Bootstrap.

---

## مظهر مستوى المجموعة

| المظهر | الوصف |
|------------|-------------|
| `field-list grid(weight=2)` | شبكة 2 أعمدة (كل عمود = 6 أعمدة Bootstrap) |
| `field-list grid(weight=3)` | شبكة 3 أعمدة (كل عمود = 4 أعمدة Bootstrap) |
| `field-list grid(weight=4)` | شبكة 4 أعمدة (كل عمود = 3 أعمدة Bootstrap) |
| `field-list grid(weight=6)` | شبكة 6 أعمدة (كل عمود = 2 أعمدة Bootstrap) |

---

## صياغة `gridformat<>` على مستوى الحقل

```
gridformat<row=R col=C colspan=S/>
gridformat<row=R col=C colspan=S backgroundcolor=COLOR/>
```

| السمة | الوصف |
|-----------|-------------|
| `row` | رقم الصف (يبدأ من 1) |
| `col` | رقم العمود (يبدأ من 1، ضمن الشبكة المحددة بـ `weight`) |
| `colspan` | عدد الأعمدة التي يمتد إليها الحقل (الافتراضي 1) |
| `backgroundcolor` | لون CSS اختياري لخلفية الحقل (مثل `#f0f0f0`، `lightblue`) |

---

## مثال: قسم استطلاع أسرة ذو عمودين

| type | name | label | appearance |
|------|------|-------|------------|
| begin_group | demographics | Demographics | `field-list grid(weight=2)` |
| text | first_name | First name | `gridformat<row=1 col=1/>` |
| text | last_name | Last name | `gridformat<row=1 col=2/>` |
| integer | age | Age | `gridformat<row=2 col=1/>` |
| select_one gender | gender | Gender | `gridformat<row=2 col=2/>` |
| text | address | Full address | `gridformat<row=3 col=1 colspan=2/>` |
| end_group | | | |

يُصيَّر هذا كـ:

```
[ First name        ] [ Last name          ]
[ Age               ] [ Gender             ]
[ Full address (spans both columns)        ]
```

---

## مثال: إدخال بيانات قطعة أرض ذو ثلاثة أعمدة

| type | name | label | appearance |
|------|------|-------|------------|
| begin_group | plot_data | Plot details | `field-list grid(weight=3)` |
| text | plot_id | Plot ID | `gridformat<row=1 col=1/>` |
| decimal | area_ha | Area (ha) | `gridformat<row=1 col=2/>` |
| select_one crop_type | crop | Crop type | `gridformat<row=1 col=3/>` |
| decimal | yield | Yield (kg) | `gridformat<row=2 col=1/>` |
| decimal | revenue | Revenue | `gridformat<row=2 col=2/>` |
| text | notes | Notes | `gridformat<row=2 col=3/>` |
| end_group | | | |

---

## ألوان الخلفية

استخدم `backgroundcolor` للتمييز المرئي بين الأقسام:

| type | name | label | appearance |
|------|------|-------|------------|
| note | section_a | Section A | `gridformat<row=1 col=1 colspan=2 backgroundcolor=#e8f4f8/>` |

---

## أفضل الممارسات

1. استخدم تخطيط الشبكة فقط لشاشات **إدخال البيانات المكثف** حيث تقلل الحقول المتجاورة التمرير فعلاً.
2. اجعل حقول `colspan=1` قصيرة (معرّفات، رموز، تحديدات قصيرة) — التسميات العريضة تُقتطع بشكل سيئ في أعمدة الشبكة الضيقة.
3. استخدم `colspan=N` للحقول ذات التسميات الطويلة أو إدخالات النصوص متعددة الأسطر.
4. اختبر على أصغر حجم شاشة تتوقع أن يستخدمه المعدِّدون — شبكة 4 أعمدة ضيقة على الهاتف.
5. يعمل تخطيط الشبكة بشكل أفضل على نماذج عوامل الويب والجهاز اللوحي؛ على الهواتف المحمولة يكون تخطيط العمودين عادةً الحد الأقصى المريح.

## القيود

- لا يعمل `gridformat<>` إلا داخل مجموعة ذات مظهر `grid(weight=N)` — ليس له تأثير على المستوى الأعلى.
- تخطيط الشبكة امتداد لنموذج rtSurvey على الويب وقد لا يتصيّر بشكل صحيح في عملاء آخرين متوافقين مع ODK.
- لا يتم التحقق من تحديد موضع الصف والعمود في وقت بناء النموذج — ستُصيَّر الحقول المتداخلة كليهما ولكن قد تبدو معطوبة.
