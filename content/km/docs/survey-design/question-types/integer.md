---
title: "Integer"
description: "សំណួរ integer អនុញ្ញាតឱ្យបញ្ចូលចំនួនគត់ក្នុងការស្ទង់មតិ។"
icon: "123"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 222
---

ប្រភេទសំណួរ integer ក្នុង XLSForms និង rtSurvey ប្រើសម្រាប់ប្រមូលការឆ្លើយតបជាចំនួនគត់។ ប្រភេទសំណួរនេះចាំបាច់សម្រាប់ការប្រមូលទិន្នន័យលេខដោយគ្មានខ្ទង់ទសភាគ ដូចជាការរាប់ អាយុ ឬឆ្នាំ។

## ការបញ្ជាក់ XLSForm មូលដ្ឋាន

| type    | name  | label                 |
|---------|-------|------------------------|
| integer | age   | Enter your age in years|

សម្រាប់ព័ត៌មានបន្ថែម សូមមើល [XLSForm specification](https://xlsform.org/en/#question-types)។

## ការប្រើប្រាស់

សំណួរ integer ប្រើជាទូទៅសម្រាប់:

1. ការបញ្ចូលអាយុ
2. ការរាប់ items (ឧ. ចំនួនកូន សមាជិកគ្រួសារ)
3. ការបញ្ចូលឆ្នាំ (ឧ. ឆ្នាំកំណើត)
4. ការវាយតម្លៃលើ척 scale លេខ
5. ការប្រមូលទិន្នន័យចំនួនគត់ណាមួយ

## ផ្នែកពង្រីករបស់ rtSurvey

ខណៈដែល XLSForm specification មូលដ្ឋានសម្រាប់សំណួរ integer គឺ straightforward rtSurvey អាចផ្តល់លក្ខណៈ ឬការប្ដូរតាមបំណងបន្ថែម:

1. ការបញ្ជាក់ range
2. messages error ផ្ទាល់ខ្លួន
3. ជម្រើស appearance សម្រាប់ number input

## ការអនុវត្តល្អ

1. ប្រើ labels ច្បាស់ស្បែក ដើម្បីបញ្ជាក់ input ដែលរំពឹងទុក។
2. អនុវត្ត range constraints ដើម្បីការពារ inputs ដែលមិនប្រក្រតី។
3. ពិចារណាប្រើ hint text ដើម្បីផ្តល់ឧទាហរណ៍ ឬបញ្ជាក់ទម្រង់ដែលរំពឹងទុក។
4. សម្រាប់ numbers ធំ ពិចារណាប្រើ commas ឬ spaces ក្នុង label ដើម្បីកែប្រែ readability។

## Constraints និងការបញ្ជាក់

អ្នកអាចបន្ថែម constraints ដើម្បីធានាថាតម្លៃដែលបញ្ចូលស្ថិតក្នុង range ជាក់លាក់:

| type    | name  | label                 | constraint        | constraint_message                    |
|---------|-------|------------------------|-------------------|---------------------------------------|
| integer | age   | Enter your age in years| .>0 and .<=120    | Age must be between 1 and 120 years   |

## ឧទាហរណ៍ការប្រើប្រាស់

នេះជាឧទាហរណ៍របៀបប្រើប្រាស់សំណួរ integer ក្នុងការស្ទង់មតិគ្រួសារ:

| type    | name           | label                                     | constraint | constraint_message                |
|---------|----------------|-------------------------------------------|------------|-----------------------------------|
| integer | household_size | How many people live in your household?   | .>0        | Household size must be at least 1 |
| integer | num_children   | How many children under 18 in the household? | .>=0    | Number of children cannot be negative |
| integer | year_built     | In what year was your house built?        | .>1800 and .<=2023 | Year must be between 1800 and 2023 |

## ការគណនាជាមួយ Integer Values

Integer values អាចប្រើក្នុងការគណនា។ នេះជាឧទាហរណ៍:

| type    | name           | label                                     |
|---------|----------------|-------------------------------------------|
| integer | num_adults     | Number of adults in the household         |
| integer | num_children   | Number of children in the household       |
| calculate | total_members | | 

ក្នុងជួរ calculate, អ្នកអាចប្រើ:

```
calculation | ${num_adults} + ${num_children}
```

នេះនឹងបូកចំនួន adults និង children ដើម្បីទទួលបានសមាជិកគ្រួសារសរុប។
