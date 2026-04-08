---
title: "Search Autocomplete"
description: "వినియోగదారు టైప్ చేస్తున్నప్పుడు రిమోట్ API నుండి ఎంపికలను శోధించే ఆటోకంప్లీట్ టెక్స్ట్ ఫీల్డ్."
icon: "search"
date: "2026-04-08T00:00:00+00:00"
lastmod: "2026-04-08T00:00:00+00:00"
draft: false
toc: true
weight: 260
---

`search-autocomplete` ప్రశ్న రకం వినియోగదారు టైప్ చేస్తున్నప్పుడు రిమోట్ API ని query చేసే text input రెండర్ చేస్తుంది మరియు సరిపోలే ఫలితాలను dropdown గా చూపిస్తుంది. ఎంచుకున్న విలువ text string గా నిల్వ చేయబడుతుంది. `search-api()` తో `select_one` కంటే భిన్నంగా, `search-autocomplete` ఫలితాన్ని plain text గా treat చేస్తుంది — XLSForm లో నిర్దిష్ట choices జాబితా అవసరం లేదు.

## ప్రాథమిక XLSForm స్పెసిఫికేషన్

| type | name | label | appearance |
|------|------|-------|------------|
| search-autocomplete | facility_name | సౌకర్యం కోసం శోధించండి | `searchApi("/api/facilities", "name")` |

`searchApi()` వ్యక్తీకరణ `appearance` కాలమ్‌లో ఉంచబడుతుంది మరియు ఏ API endpoint query చేయబడుతుందో మరియు response నుండి ఏ field display value గా ఉపయోగించబడుతుందో నియంత్రిస్తుంది.

## `searchApi()` సింటాక్స్

```
searchApi("url", "display_field")
searchApi("url", "display_field", "value_field")
```

| పారామీటర్ | అవసరం | వివరణ |
|-----------|--------|-------|
| `url` | అవును | Endpoint URL. `?q=##QUERY##` తో query parameters జోడించండి — రన్‌టైమ్‌లో `##QUERY##` టైప్ చేసిన టెక్స్ట్‌తో భర్తీ చేయబడుతుంది |
| `display_field` | అవును | Dropdown లో చూపించడానికి API response నుండి JSON field పేరు |
| `value_field` | కాదు | సమాధాన విలువగా నిల్వ చేయడానికి JSON field పేరు (డిఫాల్ట్ `display_field`) |

### ఉదాహరణ: సౌకర్యాలు శోధించి, సౌకర్యం ID నిల్వ చేయడం

| type | name | label | appearance |
|------|------|-------|------------|
| search-autocomplete | facility | సౌకర్యం పేరు | `searchApi("/api/facilities?q=##QUERY##", "name", "id")` |

## వేరియంట్: `search-autocomplete-noedit`

`search-autocomplete-noedit` వేరియంట్ వినియోగదారు autocomplete ఫలితాల నుండి ఎంచుకోని విలువ submit చేయడాన్ని నిరోధిస్తుంది. వినియోగదారు జాబితా నుండి తప్పక ఎంచుకోవాలి.

| type | name | label | appearance |
|------|------|-------|------------|
| search-autocomplete | patient_id | రోగి ID | `search-autocomplete-noedit searchApi("/api/patients?q=##QUERY##", "full_name", "patient_id")` |

## వినియోగాలు

1. XLSForm లో అన్ని choices ఎంబెడ్ చేయకుండా పెద్ద reference datasets (సౌకర్యాలు, సిబ్బంది, ఉత్పత్తులు) శోధించడం
2. ఐచ్ఛిక సూచనలతో free-text fields (`search-autocomplete-noedit` ఉపయోగించనప్పుడు)
3. ఎంచుకున్న విలువ `calculate` ద్వారా ఇతర fields నింపే linked lookups

## డేటా ఫార్మాట్

నిల్వ చేయబడిన విలువ plain string — `value_field` ద్వారా తిరిగి వచ్చిన విలువ లేదా `value_field` నిర్దేశించకపోతే display text.

## ప్లాట్‌ఫారమ్ మద్దతు

వెబ్ ఫారాలలో మద్దతు ఇవ్వబడింది. మొబైల్ మద్దతు API endpoint కు నెట్‌వర్క్ కనెక్టివిటీపై ఆధారపడి ఉంటుంది.

## పరిమితులు

- డేటా సేకరణ సమయంలో నెట్‌వర్క్‌లో అందుబాటులో ఉండే API endpoint అవసరం.
- ప్రామాణిక XLSForm స్పెసిఫికేషన్‌లో భాగం కాదు — rtSurvey పొడిగింపు మాత్రమే.
- Offline choice caching కు మద్దతు ఇవ్వదు; offline fallback అవసరమైతే `search-api()` తో `select_one` ఉపయోగించండి.
