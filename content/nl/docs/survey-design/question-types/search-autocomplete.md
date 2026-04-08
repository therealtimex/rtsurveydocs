---
title: "Search Autocomplete"
description: "Tekstveld met automatisch aanvullen dat tijdens het typen opties ophaalt via een externe API."
icon: "search"
date: "2026-04-08T00:00:00+00:00"
lastmod: "2026-04-08T00:00:00+00:00"
draft: false
toc: true
weight: 260
---

The `search-autocomplete` question type renders a text input that queries a remote API as the user types and presents matching results as a dropdown. The selected value is stored as a text string. Unlike `select_one` with `search-api()`, `search-autocomplete` treats the result as plain text — there is no fixed choice list in the XLSForm.

## Basic XLSForm Specification

| type | name | label | appearance |
|------|------|-------|------------|
| search-autocomplete | facility_name | Search for facility | `searchApi("/api/facilities", "name")` |

The `searchApi()` expression is placed in the `appearance` column and controls which API endpoint is queried and which field from the response is used as the display value.

## `searchApi()` syntax

```
searchApi("url", "display_field")
searchApi("url", "display_field", "value_field")
```

| Parameter | Required | Description |
|-----------|----------|-------------|
| `url` | Yes | Endpoint URL. Append query parameters with `?q=##QUERY##` — `##QUERY##` is replaced with the typed text at runtime |
| `display_field` | Yes | JSON field name from the API response to show in the dropdown |
| `value_field` | No | JSON field name to store as the answer value (defaults to `display_field`) |

### Example: search facilities, store the facility ID

| type | name | label | appearance |
|------|------|-------|------------|
| search-autocomplete | facility | Facility name | `searchApi("/api/facilities?q=##QUERY##", "name", "id")` |

## Variant: `search-autocomplete-noedit`

The `search-autocomplete-noedit` variant prevents the user from submitting a value that was not selected from the autocomplete results. The user must pick from the list.

| type | name | label | appearance |
|------|------|-------|------------|
| search-autocomplete | patient_id | Patient ID | `search-autocomplete-noedit searchApi("/api/patients?q=##QUERY##", "full_name", "patient_id")` |

## Uses

1. Searching large reference datasets (facilities, staff, products) without embedding all choices in the XLSForm
2. Free-text fields with optional suggestions (when `search-autocomplete-noedit` is not used)
3. Linked lookups where the selected value populates other fields via `calculate`

## Data format

The stored value is a plain string — either the value returned by `value_field` or the display text if no `value_field` is specified.

## Platform support

Supported on web forms. Mobile support depends on network connectivity to the API endpoint.

## Limitations

- Requires a network-accessible API endpoint at data collection time.
- Not part of the standard XLSForm specification — rtSurvey extension only.
- Does not support offline choice caching; use `select_one` with `search-api()` if offline fallback is needed.
