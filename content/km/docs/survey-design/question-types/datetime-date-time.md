---
title: "Datetime, date, time"
description: "សំណួរ datetime ឱ្យអ្នកឆ្លើយតបបញ្ចូលកាលបរិច្ឆេទ និងពេលវេលាទាំងពីរក្នុង field តែមួយ។"
icon: "event"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 226
---

ប្រភេទសំណួរ datetime ក្នុង XLSForms និង rtSurvey ឱ្យអ្នកឆ្លើយតបបញ្ចូលកាលបរិច្ឆេទ និងពេលវេលាទាំងពីរក្នុង field តែមួយ។ ប្រភេទសំណួរនេះមានប្រយោជន៍នៅពេលអ្នកត្រូវការ capture moment ជាក់លាក់ក្នុងពេលវេលា ដូចជាកាលបរិច្ឆេទ និងពេលវេលាពិតប្រាកដ។

## ការបញ្ជាក់ XLSForm មូលដ្ឋាន

| type     | name           | label                           |
|----------|----------------|--------------------------------|
| datetime | event_datetime | When did the event occur?       |

សម្រាប់ព័ត៌មានបន្ថែម សូមមើល [XLSForm specification](https://xlsform.org/en/#question-types)។

## ការប្រើប្រាស់

សំណួរ datetime ប្រើជាទូទៅសម្រាប់:

1. ការថត timestamps នៃព្រឹត្តិការណ៍ ឬការសង្កេត
2. ការ Scheduling appointments ឬ meetings
3. ការ Logging ពេលវេលាចាប់ផ្តើម និងបញ្ចប់នៃ activities
4. ការ Capturing moments ជាក់ស្តែងសម្រាប់ time-sensitive data collection

## ផ្នែកពង្រីករបស់ rtSurvey

rtSurvey ពង្រីក functionality នៃ datetime questions ជាមួយ appearances និង customization options ជាច្រើន:

### ជម្រើស Appearance

- `(default)`: បង្ហាញ calendar និង clock សម្រាប់ជ្រើសសរើស date និង time
- `inline`: បង្ហាញ calendar និង clock ជា icons
- `inline-1line`: បង្ហាញ calendar និង clock សម្រាប់ selection ក្នុងទម្រង់ single row
- `inline-onlyresult`: បង្ហាញ calendar និង clock ជា icons ចុងក្រោយ line; icons បាត់ក្រោយការជ្រើស

### ការប្ដូរពណ៌

អ្នកអាចប្ដូរពណ៌ icons calendar និង clock ដោយប្រើ function `colors()`:

- `inline colors("0099FF")`: បង្ហាញ icons ជាមួយពណ៌ custom
- `inline-1line-0000FF`: បង្ហាញក្នុង single row format ជាមួយ custom color
- `inline-1line colors("0000FF","FFFF00")`: បង្ហាញក្នុង single row format ជាមួយ multiple custom colors
- `inline-onlyresult colors("0099FF")`: បង្ហាញ icons ដែលបាត់ក្រោយការជ្រើស ជាមួយ custom color

### ទម្រង់ Date និង Time ផ្ទាល់ខ្លួន

rtSurvey អនុញ្ញាតឱ្យ custom date និង time formats ដោយប្រើ syntax ពិសេស:

- `inline-[%Y-%m-%d %H:%M:%S]`: ឧទាហរណ៍ custom format (Year-Month-Day Hour:Minute:Second)
- `inline-[%d/%m/%Y %I:%M %p]`: ឧទាហរណ៍ custom format (Day/Month/Year Hour:Minute AM/PM)

## ឧទាហរណ៍ការប្រើប្រាស់

នេះជាឧទាហរណ៍របៀបប្រើ datetime question ក្នុងការស្ទង់មតិ:

| type     | name           | label                                      | appearance                    |
|----------|----------------|--------------------------------------------|-----------------------------|
| datetime | incident_time  | When did the incident occur?               | inline-[%d/%m/%Y %I:%M %p]  |

## ការអនុវត្តល្អ

1. ផ្តល់ការណែនាំច្បាស់អំពី date និង time format ដែលរំពឹងទុក។
2. ពិចារណាប្រើ `inline` appearance សម្រាប់ compact display។
3. ប្រើ custom formats នៅពេលអ្នកត្រូវការ date និង time components ជាក់លាក់ ឬ formatting។
4. ប្រុងប្រយ័ត្នអំពី time zones នៅពេលប្រមូល datetime data នៅ regions ផ្សេងៗ។

## ការដាក់កំហិត

- Appearances ខ្លះ ឬ custom formats ប្រហែលមិនត្រូវបានគាំទ្រលើ devices ឬ platforms ទាំងអស់។
- អ្នកប្រើប្រាស់ប្រហែលត្រូវការការណែនាំអំពីការបញ្ចូល date និង time ត្រឹមត្រូវ ជាពិសេសជាមួយ custom formats។
- ភាពខុសគ្នា time zone អាចធ្វើអោយ data analysis ស្មុគ្រស្មាញ ប្រសិនបើមិនបានគិតគូរ properly។
