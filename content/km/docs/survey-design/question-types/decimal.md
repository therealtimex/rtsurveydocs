---
title: "Decimal"
description: "សំណួរ decimal អនុញ្ញាតឱ្យបញ្ចូលលេខដែលមានខ្ទង់ទសភាគក្នុងការស្ទង់មតិ។"
icon: "calculate"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 223
---

ប្រភេទសំណួរ decimal ក្នុង XLSForms និង rtSurvey ប្រើសម្រាប់ប្រមូលការឆ្លើយតបជាលេខដែលអាចមានខ្ទង់ទសភាគ។ ប្រភេទសំណួរនេះចាំបាច់សម្រាប់ការប្រមូលទិន្នន័យលេខដែលត្រូវការភាពត្រឹមត្រូវ ដូចជាការវាស់វែង តម្លៃ ឬភាគរយ។

## ការបញ្ជាក់ XLSForm មូលដ្ឋាន

| type    | name   | label                    |
|---------|--------|--------------------------|
| decimal | weight | Enter your weight in kg  |

សម្រាប់ព័ត៌មានបន្ថែម សូមមើល [XLSForm specification](https://xlsform.org/en/#question-types)។

## ការប្រើប្រាស់

សំណួរ decimal ប្រើជាទូទៅសម្រាប់:

1. ការវាស់វែង (ឧ. ទម្ងន់, កម្ពស់, ចម្ងាយ)
2. ទិន្នន័យហិរញ្ញវត្ថុ (ឧ. តម្លៃ ប្រាក់ខែ)
3. ភាគរយ
4. ការប្រមូលទិន្នន័យវិទ្យាសាស្ត្រ
5. ទិន្នន័យលេខណាមួយដែលត្រូវការភាពត្រឹមត្រូវលើស integers

## ការអនុវត្តល្អ

1. ប្រើ labels ច្បាស់ ដើម្បីបញ្ជាក់ input ដែលរំពឹងទុក និង unit នៃការវាស់វែង។
2. អនុវត្ត range constraints ដើម្បីការពារ inputs ដែលមិនប្រក្រតី។
3. ពិចារណាប្រើ hint text ដើម្បីផ្តល់ឧទាហរណ៍ ឬបញ្ជាក់ទម្រង់ដែលរំពឹងទុក។
4. បញ្ជាក់ចំនួន decimal places ដែលត្រូវការក្នុង label ឬ hint ប្រសិនបើ precision សំខាន់។

## Constraints និងការបញ្ជាក់

អ្នកអាចបន្ថែម constraints ដើម្បីធានាថាតម្លៃដែលបញ្ចូលស្ថិតក្នុង range ជាក់លាក់:

| type    | name   | label                    | constraint        | constraint_message                    |
|---------|--------|--------------------------|-------------------|---------------------------------------|
| decimal | height | Enter your height in meters | .>0 and .<=3    | Height must be between 0 and 3 meters |

## ឧទាហរណ៍ការប្រើប្រាស់

នេះជាឧទាហរណ៍របៀបប្រើប្រាស់សំណួរ decimal ក្នុងការស្ទង់មតិសុខភាព:

| type    | name           | label                                     | constraint | constraint_message                |
|---------|----------------|-------------------------------------------|------------|-----------------------------------|
| decimal | weight         | Enter your weight in kg                   | .>0 and .<=500 | Weight must be between 0 and 500 kg |
| decimal | height         | Enter your height in meters               | .>0 and .<=3 | Height must be between 0 and 3 meters |
| decimal | body_temp      | Enter your body temperature in Celsius    | .>=35 and .<=42 | Temperature must be between 35°C and 42°C |
| calculate | bmi          |                                           |            |                                   |

ក្នុងជួរ calculate សម្រាប់ BMI, អ្នកអាចប្រើ:

```
calculation | ${weight} / (${height} * ${height})
```

នេះនឹងគណនា BMI ដោយប្រើ weight និង height ដែលបានបញ្ចូល។

## ផ្នែកពង្រីករបស់ rtSurvey

ខណៈដែល XLSForm specification មូលដ្ឋានសម្រាប់សំណួរ decimal គឺ straightforward rtSurvey អាចផ្តល់លក្ខណៈ ឬការប្ដូរតាមបំណងបន្ថែម:

1. ការគ្រប់គ្រង precision (ចំនួន decimal places)
2. ទម្រង់ input ផ្ទាល់ខ្លួន (ឧ. percentage, currency)
3. ច្បាប់ validation ខ្ពស់

## ការដាក់កំហិត

- ភាពត្រឹមត្រូវនៃ decimal numbers អាចត្រូវបានដាក់កំហិតដោយ system ឬ database ក្រោម។
- អ្នកប្រើប្រាស់ប្រហែលត្រូវការការណែនាំអំពី decimal separator ដែលរំពឹងទុក (period ឬ comma) ដោយអាស្រ័យលើ locale របស់ពួកគេ។
- Numbers decimal ធំអាចពិបាកអានឬបញ្ចូលដែលត្រឹមត្រូវលើ mobile devices។
