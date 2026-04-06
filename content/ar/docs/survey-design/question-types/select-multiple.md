---
title: "الاختيار المتعدد"
description: "تتيح أسئلة select_multiple للمستجيبين اختيار خيار واحد أو أكثر من قائمة محددة مسبقاً."
icon: "check_box"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 225
---

يعرض نوع سؤال `select_multiple` قائمة حيث يمكن للمستجيب اختيار **خيار واحد أو أكثر**. تُعرض الخيارات افتراضياً كخانات اختيار. القيمة المخزنة هي **قائمة مفصولة بمسافات** من جميع قيم الخيارات المحددة.

## مواصفة XLSForm الأساسية

**ورقة عمل survey:**

| type | name | label |
|------|------|-------|
| select_multiple crops | crops_grown | Which crops does the household grow? |

**ورقة عمل choices:**

| list_name | name | label |
|-----------|------|-------|
| crops | maize | Maize |
| crops | beans | Beans |
| crops | rice | Rice |
| crops | vegetables | Vegetables |
| crops | other | Other |

## تنسيق البيانات المصدَّرة

يحتوي العمود المصدَّر على قائمة مفصولة بمسافات من القيم المحددة:

```
maize beans vegetables
```

استخدم الدالة `selected()` — وليس `=` — عند اختبار قيم select_multiple في التعبيرات.

## خيارات المظهر

{{< table >}}
| المظهر | الوصف |
|------------|-------------|
| *(none)* | خانات الاختيار الافتراضية، واحدة لكل سطر |
| `minimal` | أداة اختيار منسدلة متعدد |
| `compact` | شبكة مدمجة |
| `compact-N` | شبكة مدمجة مثبتة على N أعمدة |
| `horizontal` | خيارات مرتبة أفقياً في صف (ويب) |
| `columns(N)` | عرض في N أعمدة (امتداد rtSurvey) |
{{< /table >}}

## استخدام `selected()` في التعبيرات

لأن القيمة المخزنة سلسلة مفصولة بمسافات، **يجب** استخدام `selected()` لاختبار ما إذا كان خيار محدد قد اختِير. استخدام `=` لن يعمل بشكل صحيح.

### في `relevant`

| type | name | label | relevant |
|------|------|-------|----------|
| select_multiple crops | crops_grown | Which crops are grown? | |
| text | crops_other | Please specify other crops | `selected(${crops_grown}, 'other')` |

### في `constraint`

| type | name | constraint | constraint_message |
|------|------|------------|-------------------|
| select_multiple issues | issues | `count-selected(.) >= 2` | Select at least 2 issues |

## أفضل الممارسات

1. استخدم دائماً `selected()` في `relevant` و`constraint` و`calculate` — لا تستخدم `=` أو `!=` أبداً.
2. أضف قيداً لتحديد الحد الأقصى من التحديدات إذا تطلب تصميم السؤال ذلك.
3. أدرج خيار "لا شيء" أو "غير قابل للتطبيق" عندما تكون التحديدات الصفرية إجابة صالحة.
