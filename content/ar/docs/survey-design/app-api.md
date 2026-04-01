---
title: "واجهة برمجة التطبيق (App API)"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 300
---

تتيح AppAPI للمستخدمين تحميل البيانات الوصفية للنظام من التطبيق باستخدام طرق مختلفة في FormEngine وDMView. وتوفر الوصول إلى مفاتيح بيانات متنوعة لاسترداد معلومات محددة من التطبيق.

في xlsform، يمكنك استخدام الدالة `pulldata()` بالصياغة التالية:

{{< alert context="light" text="pulldata('app-api', 'data-key')" />}}

- `'app-api'`: هذه الكلمة المفتاحية تُعلم FormEngine بتحميل البيانات من App API.
- `'data-key'`: هذا هو مفتاح البيانات التي تريد تحميلها من App API.
- إذا كان مفتاح البيانات غير صالح أو غير مدعوم، سيُعيد الحساب "n/a".

فيما يلي مفاتيح البيانات المدعومة التي يمكنك استخدامها مع App-API:

`osPlatform`: يُعيد اسم نظام التشغيل الحالي (Android أو iOS) وإصداره. ستُعيد منصات الويب قيمة فارغة.

`appPlatform`: يُعيد اسم منصة التطبيق، وهو `rtSurvey`.

`appVersion`: يُعيد اسم إصدار التطبيق.

`getDisplayWidth`: يُعيد عرض شاشة الجهاز بالبكسل.

`getDisplayHeight`: يُعيد ارتفاع شاشة الجهاز بالبكسل.

`getScreenSize`: يُعيد حجم شاشة الجهاز بالبوصة.

`projectCode`: يُعيد رمز المشروع الحالي للموقع الذي يسجل المستخدم دخوله إليه.

`projectURL`: يُعيد عنوان URL الحالي للمشروع الذي يسجل المستخدم دخوله إليه. القيمة الافتراضية/الاحتياطية هي نص فارغ ("").

`startingPoint`: يُعيد مسار النقطة التي تبدأ منها النموذج. راجع "نقطة بداية النموذج" لمزيد من التفاصيل.

`serverTime`: يُعيد أفضل تقدير متاح للتاريخ والوقت على الخادم.

`user.[attribute]`: يُعيد سمات المستخدم الحالية بناءً على مفتاح السمة المحدد. راجع جدول "سمات المستخدم" لمفاتيح السمات المتاحة.

ادمج مفاتيح السمات أدناه مع "user." في معلمات `pulldata()` لاسترداد معلومات المستخدم الحالي. على سبيل المثال، استخدم `user.username`، `user.email`، إلخ.

| مفتاح السمة        | الوصف                          |
|----------------------|--------------------------------------|
| username             | اسم مستخدم المستخدم                  |
| name                 | الاسم الكامل للمستخدم                 |
| staffCode            | الرمز الوظيفي للمستخدم                     |
| phone                | رقم هاتف المستخدم              |
| email                | عنوان البريد الإلكتروني للمستخدم             |
| description          | نص الوصف في معلومات المستخدم  |
| organization_id      | معرّف المنظمة التي ينتمي إليها المستخدم    |
| organization_name    | اسم المنظمة التي ينتمي إليها المستخدم  |
| team_id              | معرّف الفريق الذي ينتمي إليه المستخدم            |
| supervisor_id        | معرّف المشرف على المستخدم            |
| is_supervisor        | 1 إذا كان المستخدم مشرفاً، 0 إذا لم يكن|

`instancePath`: يُعيد مسار مجلد المثيل الحالي.

`appLanguage`: يُعيد لغة التطبيق الحالية المضبوطة في إعدادات التطبيق (مثل vi، en).

`openArgs.[attribute]`: يُعيد وسيطة فتح النموذج الممررة من ActionButton (act_fill_form, act_get_instance). القيمة الافتراضية/الاحتياطية هي نص فارغ ("").

`primaryAppColor`: يسترد اللون الأساسي للتطبيق.

---

## أمثلة الاستخدام

### تخزين اسم المستخدم ومنظمته

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | enumerator_name | | `pulldata('app-api', 'user.name')` |
| calculate | enumerator_org | | `pulldata('app-api', 'user.organization_name')` |
| calculate | enumerator_email | | `pulldata('app-api', 'user.email')` |

استخدم هذه في تسميات note لأغراض المراجعة:
```
note | interviewer_info | Interviewer: ${enumerator_name} (${enumerator_org})
```

### معلومات الجهاز والشاشة

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | device_platform | | `pulldata('app-api', 'osPlatform')` |
| calculate | app_ver | | `pulldata('app-api', 'appVersion')` |
| calculate | screen_w | | `pulldata('app-api', 'getDisplayWidth')` |

مفيد لاستكشاف الأخطاء: صدّر `device_platform` و`app_ver` جنباً إلى جنب مع بياناتك لتحديد إصدار الجهاز المستخدم لكل إرسال.

### وقت الخادم بدلاً من وقت الجهاز

قد تكون ساعات الأجهزة غير صحيحة. استخدم `serverTime` للحصول على طابع زمني أكثر موثوقية:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | server_ts | | `pulldata('app-api', 'serverTime')` |

### المنطق الشرطي بناءً على دور المستخدم

أظهر قسماً خاصاً بالمشرفين فقط للمشرفين:

| type | name | label | relevant |
|------|------|-------|----------|
| calculate | is_supervisor | | `pulldata('app-api', 'user.is_supervisor')` |
| begin_group | supervisor_section | Supervisor review | `${is_supervisor} = '1'` |
| text | supervisor_notes | Supervisor notes | |
| end_group | | | |

### تمرير وسيطات من زر إجراء

عند تشغيل النموذج من زر إجراء `act_fill_form` مع وسيطات مخصصة:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | passed_hh_id | | `pulldata('app-api', 'openArgs.household_id')` |
| calculate | passed_task | | `pulldata('app-api', 'openArgs.task_code')` |

يجب على زر الإجراء تمرير الوسيطات بمفاتيح مطابقة (مثل `household_id`، `task_code`).

### استخدام معلومات المشروع

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | project | | `pulldata('app-api', 'projectCode')` |
| calculate | project_url | | `pulldata('app-api', 'projectURL')` |

---

## ملاحظات

- تُقيَّم جميع استدعاءات `pulldata('app-api', ...)` عند فتح النموذج ولا تُعاد تقييمها ديناميكياً خلال الجلسة (باستثناء `serverTime` و`now()`).
- إذا كان المفتاح غير مدعوم أو البيانات غير متاحة، تُعيد الدالة `'n/a'` (وليس نصاً فارغاً — اختبر باستخدام `!= 'n/a'` بدلاً من `!= ''`).
- قيم `openArgs` متاحة فقط عند تشغيل النموذج من زر إجراء؛ وإلا تُعيد نصاً فارغاً.
