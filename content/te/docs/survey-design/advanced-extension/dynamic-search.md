---
title: "డైనమిక్ శోధన"
description: "డైనమిక్ శోధన గణికుడు టైప్ చేస్తున్నప్పుడు రియల్ టైమ్‌లో రిమోట్ API నుండి ఎంపికలు లోడ్ చేస్తుంది, పెద్ద లేదా తరచుగా అప్‌డేట్ చేయబడే datasets కు మద్దతు ఇస్తుంది."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 293
---

**డైనమిక్ శోధన** (Search API అని కూడా పిలవబడుతుంది) గణికుడు టైప్ చేస్తున్నప్పుడు `select_one`, `select_multiple`, లేదా `text` ఫీల్డ్ **రన్‌టైమ్‌లో** రిమోట్ వెబ్ సేవ నుండి దాని ఎంపికలు లోడ్ చేయడానికి అనుమతిస్తుంది. మీ ఎంపిక జాబితా CSV ఫైల్‌లో చేర్చడానికి చాలా పెద్దగా ఉన్నప్పుడు, తరచుగా నవీకరించబడినప్పుడు, లేదా లైవ్ డేటాబేస్ నుండి వస్తున్నప్పుడు ఇది సరైన విధానం.

---

## `search-api()` అపీరెన్స్

డైనమిక్ శోధన `appearance` కాలమ్ ద్వారా `search-api()` ఫంక్షన్ ఉపయోగించి కాన్ఫిగర్ చేయబడుతుంది:

```
search-api(method, url, post_body, value_column, display, data_path, save_path)
```

### Parameters

| Parameter | వివరణ |
|-----------|--------|
| `method` | ఎల్లప్పుడూ `'POST'` ఉపయోగించండి |
| `url` | Query చేయవలసిన API endpoint |
| `post_body` | API కి పంపిన JSON body. గణికుని ప్రస్తుత శోధన టెక్స్ట్‌కు placeholder గా `%__input__%` ఉపయోగించండి |
| `value_column` | నిల్వ చేయబడిన **value** గా ఉపయోగించడానికి ప్రతిస్పందన ఆబ్జెక్ట్‌లోని కీ |
| `display` | dropdown లో చూపించిన **label** గా ఉపయోగించడానికి కీ (లేదా template). `##key##` placeholders మరియు `@{func}` వ్యక్తీకరణలకు మద్దతు ఇస్తుంది |
| `data_path` | ప్రతిస్పందనలో ఫలిత ఆబ్జెక్ట్‌ల array కు JSONPath (ఉదా. `$.data`, `$.hits.hits.*._source`) |
| `save_path` | ఇతర ఫీల్డ్‌లచే ఉపయోగించడానికి raw ప్రతిస్పందన నిల్వ చేయబడే పేరు |

---

## ప్రాథమిక ఉదాహరణ

గణికుడు సదుపాయం పేరులో భాగం టైప్ చేసే ఆరోగ్య సదుపాయం లుకప్:

| type | name | label | appearance |
|------|------|-------|------------|
| select_one | facility | Select health facility | `search-api('POST', 'https://api.example.com/facilities/search', '{"query": "%__input__%"}', 'id', 'name', '$.results', 'facility_data')` |

API గణికుడు "nair" టైప్ చేసినప్పుడు `{"query": "nair"}` అందుకుంటుంది మరియు తిరిగి ఇస్తుంది:

```json
{
  "results": [
    {"id": "HF001", "name": "Nairobi Central Clinic"},
    {"id": "HF002", "name": "Nairobi West Hospital"}
  ]
}
```

dropdown `Nairobi Central Clinic` మరియు `Nairobi West Hospital` చూపిస్తుంది; నిల్వ చేయబడిన విలువ `HF001` లేదా `HF002`.

---

## అధునాతన ప్రదర్శన ఫార్మాటింగ్

### `##key##` templates ఉపయోగించడం

లేబుల్‌లో బహుళ ఫీల్డ్‌లు చూపించండి:

```
search-api('POST', 'https://api.example.com/search', '{"q": "%__input__%"}', 'id', '##name## (##district##)', '$.data', 'res')
```

ఇలా ప్రదర్శించబడుతుంది: `Nairobi Central Clinic (Nairobi)`.

### `@{func}` వ్యక్తీకరణలు ఉపయోగించడం

ప్రదర్శన లేబుల్‌లో షరతులతో కూడిన లాజిక్ వర్తించండి:

```
search-api('POST', 'https://api.example.com/search', '{"q": "%__input__%"}', 'id',
  '@{if_else(eq("##status##", "active"), "✓ ##name##", "✗ ##name##")}',
  '$.data', 'res')
```

సక్రియ ఫలితాలు `✓ Clinic Name` చూపిస్తాయి; నిష్క్రియ `✗ Clinic Name` చూపిస్తాయి.

---

## డిఫాల్ట్ విలువ సెట్ చేయడం: `search-default-api()`

ఫీల్డ్‌ను వేరొక API కాల్ నుండి లోడ్ చేయబడిన డిఫాల్ట్ ఎంపికతో ముందే నింపడానికి `search-api()` తర్వాత `search-default-api()` ఉపయోగించండి (ఉదా. ఇప్పటికే ఉన్న రికార్డ్ సవరించేటప్పుడు):

```
appearance: search-api(...) search-default-api('POST', 'https://api.example.com/get', '{"id": "##saved_id##"}', 'id', 'name', '$.item')
```

---

## select_multiple కు అనుకూల separator: `search-default-separator()`

`select_multiple` ఫీల్డ్‌లకు, బహుళ ఎంచుకున్న విలువలు నిల్వ చేయబడిన స్ట్రింగ్‌లో ఎలా కలుపబడతాయో నిర్దేశించండి:

```
appearance: search-api(...) search-default-separator(' || ')
```

డిఫాల్ట్ separator ఒక స్పేస్.

---

## మద్దతు ఉన్న ప్రశ్న రకాలు

| ప్రశ్న రకం | వినియోగ కేసు |
|------------|-------------|
| `select_one` | శోధన ఫలితాల నుండి ఒకటి ఎంచుకోవడం |
| `select_multiple` | శోధన ఫలితాల నుండి బహుళ ఎంపికలు |
| `text` | Autocomplete — గణికుడు స్వేచ్ఛగా టైప్ చేస్తాడు కానీ సూచన ఎంచుకోవచ్చు |

---

## నిల్వ చేయబడిన ప్రతిస్పందన డేటా ఉపయోగించడం

`save_path` ఇచ్చిన పేరు కింద పూర్తి API ప్రతిస్పందన ఆబ్జెక్ట్ నిల్వ చేస్తుంది. ఇతర ఫీల్డ్‌లు `pulldata()` తో దాన్ని సూచించవచ్చు:

| type | name | label | calculation |
|------|------|-------|-------------|
| select_one | facility | Select facility | `search-api(..., 'facility_data')` |
| calculate | facility_district | | `pulldata('facility_data', 'district')` |
| calculate | facility_type | | `pulldata('facility_data', 'type')` |

---

## ఉత్తమ పద్ధతులు

1. మీ API endpoint 1–2 సెకన్లలో ప్రతిస్పందిస్తుందని నిర్ధారించుకోండి — నెమ్మది APIs శోధన స్పందనహీనంగా అనిపిస్తుంది.
2. API మొత్తం dataset కాకుండా సరిపోలే ఫలితాలు మాత్రమే తిరిగి ఇచ్చేలా `post_body` లో `%__input__%` ఉపయోగించండి.
3. వేగమైన ప్రతిస్పందనల కోసం సర్వర్ వైపు శోధన ఫీల్డ్‌ను index చేయండి (ఉదా. Elasticsearch, database full-text index).
4. ప్రతి query కి 20–50 అంశాలకు ఫలితాలు పరిమితం చేయండి — వేల ఫలితాలు తిరిగి ఇవ్వడం శోధన ప్రయోజనాన్ని పాడు చేస్తుంది.
5. ఒకే అక్షర ఇన్‌పుట్‌లపై విస్తృత queries ట్రిగర్ కాకుండా API లో కనిష్ట ఇన్‌పుట్ పొడవు అవసరం చేర్చండి.

## పరిమితులు

- డైనమిక్ శోధనకు నెట్‌వర్క్ కనెక్టివిటీ అవసరం — ఇది ఆఫ్‌లైన్‌లో పని చేయదు.
- `%__input__%` placeholder యథాతథంగా ఇంజెక్ట్ చేయబడుతుంది; injection దాడులు నివారించడానికి సర్వర్ వైపు ఇన్‌పుట్‌లను sanitise చేయండి.
- సంక్లిష్ట `@{func}` ప్రదర్శన వ్యక్తీకరణలు అన్ని rtSurvey క్లయింట్ వెర్షన్‌లలో పరిమిత మద్దతు ఉండవచ్చు.
