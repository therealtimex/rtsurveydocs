---
title: "Select_multiple"
description: "Select_multiple ప్రశ్నలు ప్రతిస్పందించే వ్యక్తులు ముందే నిర్వచించిన జాబితా నుండి ఒకటి లేదా అంతకంటే ఎక్కువ ఎంపికలు ఎంచుకోవడానికి అనుమతిస్తాయి."
icon: "check_box"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 225
---

`select_multiple` ప్రశ్న రకం ప్రతిస్పందించే వ్యక్తి **ఒకటి లేదా అంతకంటే ఎక్కువ ఎంపికలు** ఎంచుకోగల జాబితా చూపిస్తుంది. డిఫాల్ట్‌గా ఎంపికలు checkboxes గా రెండర్ అవుతాయి. నిల్వ చేయబడిన విలువ అన్ని ఎంచుకున్న choice విలువల **space-separated జాబితా**.

## ప్రాథమిక XLSForm స్పెసిఫికేషన్

**survey worksheet:**

| type | name | label |
|------|------|-------|
| select_multiple crops | crops_grown | Which crops does the household grow? |

**choices worksheet:**

| list_name | name | label |
|-----------|------|-------|
| crops | maize | Maize |
| crops | beans | Beans |
| crops | rice | Rice |
| crops | vegetables | Vegetables |
| crops | other | Other |

మరిన్ని వివరాలకు [XLSForm specification](https://xlsform.org/en/#question-types) చూడండి.

## నిల్వ చేయబడిన డేటా ఫార్మాట్

ఎగుమతి చేయబడిన కాలమ్ ఎంచుకున్న విలువల space-separated జాబితాను కలిగి ఉంటుంది:

```
maize beans vegetables
```

వ్యక్తీకరణలలో select_multiple విలువలు పరీక్షించేటప్పుడు `=` కాకుండా `selected()` ఫంక్షన్ ఉపయోగించండి (దిగువ చూడండి).

## వినియోగాలు

Select_multiple ప్రశ్నలు వీటికి ఉపయోగిస్తారు:

1. బహుళ వర్తించే సమాధానాలు సేకరించడం (ఉదా. ఆదాయ వనరులు, పండించిన పంటలు, లక్షణాలు)
2. Checkbox-శైలి అంగీకరించే అంశాలు (ఉదా. "Select all that apply")
3. భాషా లేదా నైపుణ్య జాబితాలు
4. బహుళ సమాధానాలు ఒకే సమయంలో చెల్లుబాటు అయ్యే ఏ ప్రశ్న

## అపీరెన్స్ ఎంపికలు

{{< table >}}
| అపీరెన్స్ | వివరణ |
|----------|--------|
| *(none)* | డిఫాల్ట్ checkboxes, వరుసకు ఒకటి |
| `minimal` | Dropdown multi-select widget |
| `compact` | Compact grid, columns screen వెడల్పుకు సర్దుబాటు అవుతాయి |
| `compact-N` | N columns కు forced compact grid |
| `horizontal` | వరుసలో అడ్డంగా అమర్చబడిన ఎంపికలు (web) |
| `columns(N)` | N columns లో ప్రదర్శించు (rtSurvey పొడిగింపు) |
{{< /table >}}

### ఉదాహరణ: 3-column compact layout

| type | name | label | appearance |
|------|------|-------|------------|
| select_multiple symptoms | symptoms | Select all symptoms observed | compact-3 |

## వ్యక్తీకరణలలో `selected()` ఉపయోగించడం

నిల్వ చేయబడిన విలువ space-separated string కాబట్టి, నిర్దిష్ట ఎంపిక ఎంచుకోబడిందో పరీక్షించడానికి **తప్పక** `selected()` ఉపయోగించాలి. `=` ఉపయోగించడం సరిగ్గా పని చేయదు.

### `relevant` లో

"other" ఎంచుకున్నప్పుడే follow-up ప్రశ్న చూపించండి:

| type | name | label | relevant |
|------|------|-------|----------|
| select_multiple crops | crops_grown | Which crops are grown? | |
| text | crops_other | Please specify other crops | `selected(${crops_grown}, 'other')` |

### `constraint` లో

కనీసం 2 ఎంపికలు అవసరం:

| type | name | constraint | constraint_message |
|------|------|------------|-------------------|
| select_multiple issues | issues | `count-selected(.) >= 2` | Select at least 2 issues |

## `calculate` లో — ఎంచుకున్న labels కలపడం

| type | name | calculation |
|------|------|-------------|
| calculate | crops_summary | join(', ', ${crops_grown}) |

## "None of the above" / exclusive ఎంపిక

ఒక ఎంపికను అన్నింటితో పరస్పరం ప్రత్యేకంగా చేయడానికి `constraint` ఉపయోగించండి:

| type | name | label | constraint | constraint_message |
|------|------|-------|------------|-------------------|
| select_multiple issues | issues | Select all issues present | `not(selected(., 'none') and count-selected(.) > 1)` | "None" cannot be selected with other options |

## ఎంపికలు గణించడం మరియు సారాంశం

| ఫంక్షన్ | ఉదాహరణ | ఫలితం |
|---------|---------|--------|
| `count-selected(field)` | `count-selected(${crops_grown})` | ఎంచుకున్న ఎంపికల సంఖ్య |
| `selected(field, value)` | `selected(${crops_grown}, 'maize')` | true/false |
| `selected-at(field, index)` | `selected-at(${crops_grown}, 0)` | మొదట ఎంచుకున్న విలువ |
| `choice-label(field, value)` | `choice-label(${crops_grown}, 'maize')` | విలువకు label |

## ఉత్తమ పద్ధతులు

1. `relevant`, `constraint`, మరియు `calculate` లో ఎల్లప్పుడూ `selected()` ఉపయోగించండి — `=` లేదా `!=` ఎప్పుడూ వద్దు.
2. ప్రశ్న డిజైన్ అవసరమైతే గరిష్ట ఎంపికల సంఖ్య పరిమితం చేయడానికి constraint జోడించండి.
3. సున్నా ఎంపికలు చెల్లుబాటైన సమాధానం అయినప్పుడు "None" లేదా "Not applicable" ఎంపిక చేర్చండి.
4. పొడవైన జాబితాలకు (15+ ఎంపికలు) అతిగా scroll చేయడం నివారించడానికి `minimal` (multi-select dropdown) ఉపయోగించండి.

## పరిమితులు

- Select_multiple విలువలు `=` తో నేరుగా పోల్చలేరు. ఎల్లప్పుడూ `selected()` ఉపయోగించండి.
- Compact అపీరెన్స్ చాలా పొడవైన choice labels కోసం బాగా రెండర్ కాకపోవచ్చు.
