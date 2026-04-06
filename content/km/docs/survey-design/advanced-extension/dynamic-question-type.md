---
title: "ប្រភេទ Question Dynamic"
description: "Dynamic question type អនុញ្ញាតឱ្យ field's question type និង widget ត្រូវ កំណត់ at runtime ដោយ API response ។"
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 301
---

**Dynamic Question Type** feature អនុញ្ញាតឱ្យ field's input widget ត្រូវ កំណត់ **at runtime** ។ Use case ទូ ទៅ ជា configurable inspection checklist ។

---

## How it works

Field ដែល dynamic ប្រើ `callapi()` ដើម្បី fetch configuration ពី API ។ API response កំណត់:
- input type ដើម្បី render
- available choices
- Validation rules

---

## Setup

### ជំហានទី ១: Fetch field configuration

| type | name | label | appearance | calculation |
|------|------|-------|------------|-------------|
| calculate | field_config | | callapi | `callapi('POST', 'https://api.example.com/field-config', 1, 2, 0, '$.config', 10000, 0, '', '', '{"form_id": "##form_id##", "field_id": "inspection_result"}')` |

### ជំហានទី ២: Reference configuration ក្នុង dynamic field

| type | name | label | appearance |
|------|------|-------|------------|
| text | inspection_result | Inspection result | `callapi-verify(dynamicParams)` |

---

## API response format

```json
{
  "config": {
    "type": "select_one",
    "choices": [
      {"value": "pass", "label": "Pass"},
      {"value": "fail", "label": "Fail"},
      {"value": "na", "label": "N/A"}
    ],
    "required": true
  }
}
```

---

## Best Practices

1. ប្រើ dynamic question types ត ែ ព េ ល structure ប ្ ដ ូ រ at runtime ។
2. ធានា API response ឆ ាប ់ (< 2 seconds) ។
3. Version API response schema ។

## Limitations

- ត ្ រ ូ វ ក ា រ network connectivity ។
- ជ ា advanced rtSurvey extension ។
