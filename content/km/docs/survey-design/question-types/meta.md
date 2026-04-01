---
title: "Meta"
description: "ប្រភេទ question Meta ចាប់ device, enumerator, និង timing information ដោយស្វ័យប្រវត្តិ ដោយ input ពី respondent។"
icon: "info"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 237
---

ប្រភេទ question meta គឺ special fields ដែលបំពេញ **ដោយស្វ័យប្រវត្តិ** — respondent មិន see ពួកវា ។ ពួកវា capture context អំពី submission: ពេល collect, device ណាត្រូវបានប្រើ, ហើយ នរណា collect ។ បន្ថែមពួកវាក្នុង `survey` worksheet ដូចគ្នា question type ណាមួយ; ពួកវា simply មិន appear ក្នុង screen ។

## ការបញ្ជាក់ XLSForm មូលដ្ឋាន

| type | name | label |
|------|------|-------|
| start | start | |
| end | end | |
| deviceid | deviceid | |

Labels ជាការ optional សម្រាប់ meta fields ដោយ ពួកវា never display ។

---

## Timing meta fields

### `start`

Records **date និង time ពេល form ត្រូវ opened**។ Store ក្នុង ISO 8601 format (`YYYY-MM-DDTHH:MM:SS.sss+HH:MM`)។

```
type    | name  | label
start   | start |
```

### `end`

Records **date និង time ពេល form ត្រូវ submitted**។ ជាមួយ `start`, អ្នកអាចគណនា time ដែលចំណាយ fill ក្នុង form:

```
type      | name          | calculation
calculate | duration_min  | (decimal-date-time(${end}) - decimal-date-time(${start})) * 1440
```

### `today`

Records **date បច្ចុប្បន្ន** (គ្មាន time component)។ Store ជា `YYYY-MM-DD`។ មានប្រយោជន៍ ពេលអ្នកត្រូវការ date តែ ដោយ ​គ្មាន full timestamp ។

```
type  | name  | label
today | today |
```

---

## Device meta fields

### `deviceid`

Records **unique identifier នៃ device** ដែលប្រើ សម្រាប់ data collection ។ លើ Android ជាធម្មតា IMEI ឬ Android ID។ មានប្រយោជន៍ ដើម្បីតាមដាន device ណាដែល submit form ហើយ detect duplicate submissions ពី device ដូចគ្នា ។

```
type      | name     | label
deviceid  | deviceid |
```

### `devicephonenum`

Records **phone number នៃ SIM card** ក្នុង device (ប្រសិនបើ available)។ ប្រហែល empty ប្រសិនបើ device គ្មាន SIM ឬ number មិន store ក្នុង SIM ។

```
type           | name          | label
devicephonenum | devicephonenum |
```

### `simserial`

Records **serial number នៃ SIM card** (ICCID)។ មានប្រយោជន៍ ដើម្បី identify SIM/carrier ណាដែលប្រើ ។

```
type      | name      | label
simserial | simserial |
```

### `subscriberid`

Records **IMSI (International Mobile Subscriber Identity)** — unique subscriber identifier លើ SIM card ។

```
type         | name        | label
subscriberid | subscriberid |
```

---

## Enumerator meta fields

### `username`

Records **username នៃ enumerator ដែល logged-in** (account ដែលប្រើក្នុង rtSurvey app)។ នេះ reliable បំផុត ដើម្បី track នរណា collect submission នីមួយៗ ។

```
type     | name     | label
username | username |
```

### `email`

Records **email address នៃ enumerator ដែល logged-in**។

```
type  | name  | label
email | email |
```

### `phonenumber`

Records **phone number ដែលពាក់ព័ន្ធ ជាមួយ account enumerator** (ប្រសិនបើ configured)។

```
type        | name       | label
phonenumber | phonenumber |
```

---

## Audit log

### `audit`

`audit` meta field ឱ្យ **detailed audit logging** — វា records timestamped log នៃ question ទាំងអស់ enumerator visited, time ប៉ុន្មាន spend ក្នុង question នីមួយៗ, ហើយ (optionally) GPS location ក្នុង step នីមួយៗ ។ Audit log ត្រូវ save ជា `audit.csv` file ដាច់ដោយឡែកជាមួយ submission នីមួយៗ ។

```
type  | name  | parameters
audit | audit | location-priority=balanced location-min-interval=30 location-max-age=60
```

#### Audit parameters

| Parameter | ការពិពណ៌នា |
|-----------|-------------|
| `location-priority` | GPS accuracy level: `no-gps`, `low-power`, `balanced`, `high-accuracy` |
| `location-min-interval` | វិនាទី minimum រវាង location captures |
| `location-max-age` | Maximum age (វិនាទី) នៃ cached location ដើម្បីអនុញ្ញាត |

Audit log captures:
- Question name និង event type (`question`, `form.start`, `form.exit`, `form.save`, `form.finalize`)
- Start និង end timestamps សម្រាប់ event នីមួយៗ
- GPS coordinates (ប្រសិនបើ `location-priority` ត្រូវ set)

{{% alert icon=" " context="warning" %}}
`audit` field generate ឯកសារ separate ក្នុង submission នីមួយៗ។ ធានា data pipeline របស់អ្នក process ទាំង main form data ហើយ audit CSV ។
{{% /alert %}}

---

## ឧទាហរណ៍ complete

Household survey ធម្មតា ប្រហែល include timing និង enumerator meta fields ទាំងអស់:

| type | name | label |
|------|------|-------|
| start | start | |
| end | end | |
| today | today | |
| deviceid | deviceid | |
| username | username | |
| email | email | |
| audit | audit | |
| text | household_id | Household ID |
| ... | ... | ... |

---

## ការអនុវត្តល្អ

1. ដូចជារួមបញ្ចូល `start` និង `end` — ពួកវា free, automatic, ហើយ invaluable សម្រាប់ quality monitoring ។
2. ដូចជារួមបញ្ចូល `username` ដើម្បី track enumerators ។
3. Include `deviceid` ពេលអ្នកចង់ detect duplicate submissions ឬ track field devices ។
4. ប្រើ `audit` ក្នុង high-accountability surveys ដែលអ្នកត្រូវ verify enumerators actually visited question នីមួយៗ ។
5. SIM-related fields (`simserial`, `subscriberid`, `devicephonenum`) reliable តែ លើ Android devices ជាមួយ active SIM cards — skip ពួកវា សម្រាប់ tablet-only deployments ។

---

## ការដាក់កំហិត

- Meta fields ទាំងអស់ **read-only** — ពួកវាមិនអាច referenced ឬ modified ដោយ calculations ផ្សេងទៀត ។
- `username` និង `email` ចាំបាច់ enumerator logged in; ពួកវានឹង empty សម្រាប់ anonymous submissions ។
- SIM/phone meta fields ប្រហែល return empty values លើ Wi-Fi-only tablets ហើយ Android versions ខ្លះ ដោយ permission restrictions ។
