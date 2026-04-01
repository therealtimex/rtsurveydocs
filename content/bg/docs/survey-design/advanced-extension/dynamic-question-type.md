---
title: "Динамичен тип въпрос"
description: "Динамичният тип въпрос позволява типът въпрос и уиджетът на поле да се определят по времe на изпълнение въз основа на API отговор или изчислена стойност."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 301
---

The **Dynamic Question Type** feature allows a field's input widget and validation behaviour to be determined **at runtime** rather than at form design time. This is an advanced rtSurvey extension used when the type of data to collect depends on a server-side configuration, API response, or preceding field value.

A common use case is a configurable inspection checklist where the server defines which fields are required, what type they are (text, integer, select, etc.), and what options are available — without rebuilding the form for every configuration.

---

## Как работи

A field marked as a dynamic question type uses `callapi()` to fetch its configuration from an API. The API response defines:

- The input type to render (text, integer, select_one, etc.)
- The available choices (for select types)
- Validation rules

The field is marked with `specialFeature: isDynamicQuestionType` internally, which tells the form engine to use the API response to construct the widget rather than the static form definition.

---

## Setup

### Step 1: Fetch the field configuration

Use a `calculate` field with `callapi()` to retrieve the dynamic configuration:

| type | name | label | appearance | calculation |
|------|------|-------|------------|-------------|
| calculate | field_config | | callapi | `callapi('POST', 'https://api.example.com/field-config', 1, 2, 0, '$.config', 10000, 0, '', '', '{"form_id": "##form_id##", "field_id": "inspection_result"}')` |

### Step 2: Reference the configuration in the dynamic field

The dynamic field uses `callapi-verify()` in its `appearance` or `constraint` to link to the fetched config:

| type | name | label | appearance |
|------|------|-------|------------|
| text | inspection_result | Inspection result | `callapi-verify(dynamicParams)` |

The form engine reads `field_config` and dynamically determines whether to render `inspection_result` as a `text`, `integer`, or `select_one` field.

---

## API response format

The API should return a JSON object describing the field configuration. A typical response:

```json
{
  "config": {
    "type": "select_one",
    "choices": [
      {"value": "pass", "label": "Pass"},
      {"value": "fail", "label": "Fail"},
      {"value": "na", "label": "N/A"}
    ],
    "required": true,
    "constraint": ". != ''"
  }
}
```

---

## Пример: Configurable inspection form

An inspection form where the checklist items and their answer types are fetched from a server based on the inspection category:

| type | name | label | appearance | calculation |
|------|------|-------|------------|-------------|
| select_one inspection_type | insp_type | Type of inspection | | |
| calculate | checklist_config | | callapi | `callapi('POST', 'https://api.example.com/checklist', 1, 2, 0, '$.items', 10000, 0, '', '', '{"type": "##insp_type##"}')` |
| text | item_1 | Item 1 | `callapi-verify(dynamicParams)` | |
| text | item_2 | Item 2 | `callapi-verify(dynamicParams)` | |
| text | item_3 | Item 3 | `callapi-verify(dynamicParams)` | |

The server returns the correct widget type, label, choices, and validation for each item based on `insp_type`.

---

## Best Practices

1. Use dynamic question types only when the field structure genuinely varies at runtime — for static forms, use standard question types.
2. Ensure the configuration API responds quickly (under 2 seconds) and is available on the field network.
3. Always define a sensible fallback in the form for the case where the API is unreachable — a plain `text` field with a note is better than a broken widget.
4. Version your API response schema — changes to the response format will affect all active forms using that endpoint.
5. Test every combination of field types the API may return before deployment.

## Limitations

- Dynamic question types require network connectivity to fetch the configuration.
- The full range of widget types available dynamically depends on rtSurvey client version — test your target version.
- This is an advanced rtSurvey extension with no equivalent in the standard XLSForm specification.
- Debug errors are harder to trace since the field definition lives partly in the form and partly in the API response.
