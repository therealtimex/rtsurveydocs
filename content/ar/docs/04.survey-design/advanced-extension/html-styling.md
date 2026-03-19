---
title: "تنسيق HTML"
description: "يدعم rtSurvey علامات HTML في التسميات والتلميحات، مما يتيح تنسيق النصوص الغنية والروابط وتغيير لون السمة الديناميكي."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 297
---

يُصيّر rtSurvey نصوص **التسمية** و**التلميح** بتنسيق HTML على نماذج الويب. هذا يعني أنه يمكنك استخدام علامات HTML القياسية لتنسيق النصوص وإضافة فواصل الأسطر وإنشاء روابط وتطبيق الألوان. هذا مفيد بشكل خاص لحقول الملاحظات وتعليمات الأقسام والملخصات الديناميكية.

{{% alert icon=" " context="warning" %}}
يُصيَّر HTML في التسميات على **نموذج الويب** وتطبيقات rtSurvey المحمولة. قد لا يُصيَّر في جميع العملاء المتوافقين مع ODK. اختبر دائماً على منصتك المستهدفة.
{{% /alert %}}

---

## علامات HTML المدعومة

### تنسيق النص

| العلامة | النتيجة |
|-----|--------|
| `<strong>text</strong>` أو `<b>text</b>` | **نص غامق** |
| `<em>text</em>` أو `<i>text</i>` | *نص مائل* |
| `<u>text</u>` | نص مسطّر |
| `<br>` | فاصل سطر |
| `<span style="...">text</span>` | تنسيق مضمّن |

### الروابط

```html
<a href="https://example.com" target="_blank">Click here</a>
```

يفتح في علامة تبويب جديدة. استخدمه للوثائق المرجعية أو الإرشادات أو الموارد الخارجية التي يجب على المعدِّد الاطلاع عليها.

### الألوان

استخدم `<span>` مع أنماط مضمّنة:

```html
<span style="color: red;">Warning: value is out of range</span>
<span style="color: #009688;">Section completed</span>
```

---

## متغيرات سمة الألوان

يدعم rtSurvey **رموز سمات الألوان** التي تتكيف مع سمة التطبيق المكوّنة. استخدم صياغة `__COLOR_THEME_NAME__`:

```html
<span style="color: var(--color-theme-primary);">Primary color text</span>
```

أو باستخدام الاختصار في نص التسمية:

```
<font color="var(--COLOR_THEME_PRIMARY)">Important note</font>
```

يتم تحويل هذا تلقائياً إلى `<span>` المكافئ بمتغير CSS في وقت التصيير.

---

## تسميات متعددة اللغات

قم بتغليف المحتوى في علامات اللغة لدعم لغات متعددة في خلية تسمية واحدة:

```
<en>Enter the household size</en><vi>Nhập quy mô hộ gia đình</vi>
```

يستخرج rtSurvey المحتوى المطابق للغة التطبيق الحالية. إذا لم يُعثر على علامة لغة مطابقة، تُعرض السلسلة الكاملة كما هي.

---

## أمثلة في حقول الملاحظات

### تعليمات قسم بالتغميق وفاصل سطر

| type | name | label |
|------|------|-------|
| note | section_intro | `<strong>Section 3: Land Use</strong><br>Ask all questions in this section to the household head only.` |

### ملخص ديناميكي مع مرجع حساب

| type | name | label |
|------|------|-------|
| calculate | total | | `${adults} + ${children}` |
| note | summary | `Total household members: <strong>${total}</strong><br><span style="color: gray;">Adults: ${adults} · Children: ${children}</span>` |

### تحذير باللون الأحمر

| type | name | label | relevant |
|------|------|-------|----------|
| note | age_warning | `<span style="color: red;"><strong>Warning:</strong> Age entered (${age}) is unusually high. Please verify.</span>` | `${age} > 100` |

### رابط لوثيقة مرجعية

| type | name | label |
|------|------|-------|
| note | guidelines_link | `Refer to the <a href="https://docs.example.com/guidelines" target="_blank">Field Guidelines</a> before starting this section.` |

---

## علامات HTML الخاصة بـ rtSurvey

### `<webbox src='url' title='title'>...</webbox>`

يُضمّن زراً يفتح عنوان URL في نافذة مشروطة داخل النموذج. راجع [Webbox](webbox) للتفاصيل الكاملة.

### `<delete-repeat-current>label</delete-repeat-current>`

يُصيّر زراً داخل مجموعة تكرار يحذف مثيل التكرار الحالي عند الضغط عليه.

### `<delete-repeat-last>label</delete-repeat-last>`

يُصيّر زراً يحذف مثيل التكرار الأخير.

مثال الاستخدام في مجموعة تكرار:

| type | name | label |
|------|------|-------|
| note | delete_btn | `<delete-repeat-current>Remove this member</delete-repeat-current>` |

---

## أفضل الممارسات

1. استخدم HTML باعتدال — التسميات المنسّقة بشكل مفرط أصعب قراءةً، وليس أسهل.
2. فضّل `<strong>` للتغميق و`<em>` للمائل بدلاً من `<b>` و`<i>` المهجورتين.
3. اجعل استخدام الألوان ذا معنى — استخدم الأحمر للتحذيرات، وليس للزينة.
4. اختبر دائماً تصيير HTML على كل من التطبيق المحمول ونموذج الويب، إذ قد يختلف التصيير قليلاً.
5. تجنب علامات `<table>` داخل التسميات — نادراً ما تُصيَّر بشكل جيد على شاشات الجوال.
6. لا تستخدم JavaScript (`<script>`) — سيتم تجريدها أو التسبب في أخطاء.

## القيود

- HTML المعقد (جداول، نماذج، نصوص برمجية) غير مدعوم وقد يكسر التصيير.
- قد تعرض بعض عملاء الجوال الأقدم علامات HTML كنص حرفي — اختبر على جميع الأجهزة المستهدفة.
- تفتح روابط `<a>` في متصفح أو WebView — يغادر المعدِّد النموذج، وهو ما قد يكون مُربكاً على الجوال.
