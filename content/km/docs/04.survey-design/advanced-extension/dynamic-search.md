---
title: "Dynamic Search"
description: "Dynamic Search load choices ពី remote API ជាក់ស្ដែង ខណៈ enumerator type, enabling large or frequently updated datasets។"
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 293
---

**Dynamic Search** (ហ ៅ ថ ា Search API) អនុញ្ញាតឱ្យ `select_one`, `select_multiple`, ឬ `text` field load choices ពី remote web service **at runtime** ។

---

## `search-api()` appearance

```
search-api(method, url, post_body, value_column, display, data_path, save_path)
```

### Parameters

| Parameter | ការពិពណ៌នា |
|-----------|-------------|
| `method` | ជ ា ន ិ ច ្ ច ប ្ រ ើ `'POST'` |
| `url` | API endpoint |
| `post_body` | JSON body; ប ្ រ ើ `%__input__%` ជ ា placeholder |
| `value_column` | key ដើម្បី store **value** |
| `display` | key ដើម្បី display ជ ា **label** |
| `data_path` | JSONPath ទ ៅ array (ឧ. `$.data`) |
| `save_path` | Name ដើម្បី save raw response |

---

## Basic example

| type | name | label | appearance |
|------|------|-------|------------|
| select_one | facility | Select health facility | `search-api('POST', 'https://api.example.com/facilities/search', '{"query": "%__input__%"}', 'id', 'name', '$.results', 'facility_data')` |

API returns:
```json
{
  "results": [
    {"id": "HF001", "name": "Nairobi Central Clinic"},
    {"id": "HF002", "name": "Nairobi West Hospital"}
  ]
}
```

---

## Advanced display formatting

### Using `##key##` templates

```
search-api('POST', 'https://api.example.com/search', '{"q": "%__input__%"}', 'id', '##name## (##district##)', '$.data', 'res')
```

---

## Setting a default value: `search-default-api()`

```
appearance: search-api(...) search-default-api('POST', 'https://api.example.com/get', '{"id": "##saved_id##"}', 'id', 'name', '$.item')
```

---

## Using saved response data

| type | name | label | calculation |
|------|------|-------|-------------|
| select_one | facility | Select facility | `search-api(..., 'facility_data')` |
| calculate | facility_district | | `pulldata('facility_data', 'district')` |

---

## Best Practices

1. ធានា API endpoint respond ក ្ ន ុ ង 1–2 seconds ។
2. ប ្ រ ើ `%__input__%` ក ្ ន ុ ង `post_body` ។
3. Limit results ទ ៅ 20–50 items ។

## Limitations

- Dynamic Search ត ្ រ ូ វ ក ា រ network connectivity ។
- `%__input__%` inject as-is; sanitise inputs server-side ។
