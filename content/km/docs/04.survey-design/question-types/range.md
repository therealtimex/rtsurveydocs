---
title: "Range"
description: "សំណួរ range ឱ្យអ្នកឆ្លើយតបជ្រើសរើស number ដោយ drag slider រវាង minimum និង maximum ដែលបានកំណត់។"
icon: "sliders"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 238
---

ប្រភេទសំណួរ `range` បង្ហាញ **slider** (ឬ input ស្មើ) ដែលអនុញ្ញាតឱ្យអ្នកឆ្លើយតបជ្រើស number ក្នុងជួរ minimum និង maximum ដែលបានកំណត់។ វាល្អបំផុតសម្រាប់ប្រមូល ratings, satisfaction scores, ឬ numeric value ណាមួយដែលអ្នកចង់ដាក់ដំណើរការ range ដោយ visual ជំនួស text input ជាមួយ constraints។

## ការបញ្ជាក់ XLSForm មូលដ្ឋាន

| type | name | label | parameters |
|------|------|-------|------------|
| range | satisfaction | How satisfied are you with the service? | start=1 end=5 step=1 |

ជួរ `parameters` កំណត់ slider bounds និង step size:

| Parameter | ការពិពណ៌នា | Default |
|-----------|-------------|---------|
| `start` | តម្លៃ minimum (inclusive) | 0 |
| `end` | តម្លៃ maximum (inclusive) | 10 |
| `step` | Increment រវាង valid values | 1 |

សម្រាប់ព័ត៌មានបន្ថែម សូមមើល [XLSForm specification](https://xlsform.org/en/#question-types)។

## ការប្រើប្រាស់

សំណួរ range ប្រើជាទូទៅសម្រាប់:

1. Satisfaction ឬ rating scales (ឧ. 1–5 ឬ 0–10)
2. Numeric scales Likert-style
3. ការប្រមូលការវាស់វែងដែល valid values discrete តែប៉ុណ្ណោះ
4. Age brackets ឬ score ranges ដែល slider ធ្វើអោយ usability ប្រសើរជាង text field

## ឧទាហរណ៍ការប្រើប្រាស់

### Rating scale មូលដ្ឋាន

| type | name | label | parameters |
|------|------|-------|------------|
| range | overall_rating | Overall rating (0–10) | start=0 end=10 step=1 |

### Decimal step

| type | name | label | parameters |
|------|------|-------|------------|
| range | weight_kg | Weight (kg) | start=0 end=200 step=0.5 |

### ការប្រើប្រាស់តម្លៃក្នុងការគណនា

| type | name | label | parameters | calculation |
|------|------|-------|------------|-------------|
| range | score | Test score (0–100) | start=0 end=100 step=5 | |
| calculate | grade | | | if(${score} >= 90, 'A', if(${score} >= 80, 'B', if(${score} >= 70, 'C', 'F'))) |
| note | grade_note | Your grade is: ${grade} | | |

## Appearance

ប្រភេទ `range` render ជា slider ជាលំនាំដើម។ គ្មាន appearance values បន្ថែមចាំបាច់សម្រាប់ basic usage។ អ្នកអាចរួមបញ្ចូលជាមួយ `horizontal` សម្រាប់ layout ទំហំទូលក្នុង web forms:

| type | name | label | parameters | appearance |
|------|------|-------|------------|------------|
| range | nps | How likely are you to recommend us? (0–10) | start=0 end=10 step=1 | horizontal |

## ការអនុវត្តល្អ

1. ដូចជាកំណត់ `start`, `end`, និង `step` values ដែលមានន័យ — កុំពឹងលើ defaults។
2. ធ្វើ label ចុងក្រោយ scale របស់អ្នកក្នុងជួរ `hint` (ឧ. `hint: 0 = Very dissatisfied, 10 = Very satisfied`) ដើម្បីផ្តល់ context ដល់អ្នកឆ្លើយតប។
3. សម្រាប់ 5-point Likert scales ប្រើ `start=1 end=5 step=1` ជំនួស 0–4 ដោយសារអ្នកឆ្លើយតបរំពឹងថា "1" មានន័យ lowest។
4. ប្រើ `range` ជំនួស `integer` + constraint នៅពេល bounded nature នៃ input គឺជាផ្នែកនៃ question design (slider ទំនាក់ scale ដោយ visual)។

## ការដាក់កំហិត

- Slider widget ប្រហែលមិនល្អបំផុតសម្រាប់ ranges ទូលំទូលាយ (ឧ. 0–10000) — text `integer` ជាមួយ constraints user-friendly ជាងក្នុងករណីទាំងនោះ។
- លើ mobile devices step values ល្អិតល្អន់ (ឧ. `step=0.1`) អាចពិបាក control ដោយ touch slider។
