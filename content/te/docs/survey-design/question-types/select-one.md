---
title: "Select_one"
description: "Select_one ప్రశ్నలు ప్రతిస్పందించే వ్యక్తులు ముందే నిర్వచించిన ఎంపికల జాబితా నుండి ఖచ్చితంగా ఒక ఎంపిక ఎంచుకోవడానికి అనుమతిస్తాయి."
icon: "radio_button_checked"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 224
---

`select_one` ప్రశ్న రకం ప్రతిస్పందించే వ్యక్తిని ముందే నిర్వచించిన జాబితా నుండి **ఖచ్చితంగా ఒక ఎంపిక** ఎంచుకోమని అడుగుతుంది. డిఫాల్ట్‌గా ఎంపికలు radio buttons గా రెండర్ అవుతాయి, కానీ layout మరియు ప్రవర్తన మార్చడానికి అపీరెన్స్ ఎంపికల విస్తృత శ్రేణి అందుబాటులో ఉంది.

## ప్రాథమిక XLSForm స్పెసిఫికేషన్

**survey worksheet:**

| type | name | label |
|------|------|-------|
| select_one yesno | consent | Did the respondent give consent? |

**choices worksheet:**

| list_name | name | label |
|-----------|------|-------|
| yesno | yes | Yes |
| yesno | no | No |

`select_one listname` లో `listname` choices worksheet లోని `list_name` కాలమ్‌తో సరిపోలాలి.

మరిన్ని వివరాలకు [XLSForm specification](https://xlsform.org/en/#question-types) చూడండి.

## వినియోగాలు

Select_one ప్రశ్నలు వీటికి ఉపయోగిస్తారు:

1. అవును/కాదు ప్రశ్నలు
2. ఒకటే-సమాధానం multiple choice (ఉదా. విద్యా స్థాయి, లింగం, వైవాహిక స్థితి)
3. వర్గ ratings (ఉదా. poor / fair / good / excellent)
4. మునుపటి సమాధానం ఆధారంగా ఎంపికలు filter చేయబడే cascading (linked) selects
5. దేశం, ప్రాంతం, జిల్లా, లేదా ఇతర పరిపాలనా యూనిట్ ఎంపిక

## అపీరెన్స్ ఎంపికలు

ఎంపికలు ఎలా ప్రదర్శించబడతాయో మార్చడానికి `appearance` కాలమ్‌లో విలువ నిర్దేశించండి:

{{< table >}}
| అపీరెన్స్ | వివరణ |
|----------|--------|
| *(none)* | డిఫాల్ట్ radio buttons, వరుసకు ఒకటి |
| `minimal` | Radio buttons కంటే single dropdown/spinner |
| `quick` | ఎంపిక తర్వాత వెంటనే తదుపరి ప్రశ్నకు auto-advances (mobile మాత్రమే) |
| `compact` | ఎంపికల compact grid — columns సంఖ్య screen వెడల్పుకు సర్దుబాటు చేయబడుతుంది |
| `compact-N` | N columns కు forced compact grid (ఉదా. `compact-3`) |
| `horizontal` | వరుసలో అమర్చబడిన ఎంపికలు (web) |
| `likert` | Likert scale వరుస — పైన labels, క్రింద radio buttons |
| `columns(N)` | N columns లో ప్రదర్శించు (rtSurvey పొడిగింపు, ఉదా. `columns(3)`) |
| `distress` | Kessler Psychological Distress (K10) emotional icon widget |
| `search-api(...)` | డైనమిక్ శోధన — రన్‌టైమ్‌లో API నుండి ఎంపికలు లోడ్ చేస్తుంది |
{{< /table >}}

### ఉదాహరణ: Likert scale

| type | name | label | appearance |
|------|------|-------|------------|
| select_one satisfaction | service_rating | How satisfied are you with the service? | likert |

### ఉదాహరణ: Compact 3 columns

| type | name | label | appearance |
|------|------|-------|------------|
| select_one regions | region | Select region | compact-3 |

## Cascading selects

Cascading (linked) select మునుపటి ప్రశ్నలో ఎంచుకున్న విలువ ఆధారంగా ఎంపికలు filter చేస్తుంది. మీ choices worksheet లోని కాలమ్ పేరుతో `choice_filter` కాలమ్ ఉపయోగించండి.

**survey:**

| type | name | label | choice_filter |
|------|------|-------|---------------|
| select_one province | province | Select province | |
| select_one district | district | Select district | province_name = ${province} |

**choices:**

| list_name | name | label | province_name |
|-----------|------|-------|---------------|
| province | nairobi | Nairobi | |
| province | mombasa | Mombasa | |
| district | westlands | Westlands | nairobi |
| district | kasarani | Kasarani | nairobi |
| district | nyali | Nyali | mombasa |
| district | likoni | Likoni | mombasa |

ప్రతిస్పందించే వ్యక్తి `nairobi` ఎంచుకున్నప్పుడు, district జాబితాలో `Westlands` మరియు `Kasarani` మాత్రమే కనిపిస్తాయి.

{{% alert icon=" " context="warning" %}}
`choice_filter` లో ఉపయోగించిన కాలమ్ పేరు (ఉదా. `province_name`) choices worksheet లో ఉండాలి. `${province}` `province` అనే survey ఫీల్డ్‌ను సూచిస్తుంది.
{{% /alert %}}

## వ్యక్తీకరణలలో ఎంచుకున్న విలువ ఉపయోగించడం

`${fieldname}` తో ఎంచుకున్న **విలువ** (label కాదు) సూచించండి:

```
relevant: ${consent} = 'yes'
```

విలువ కంటే choice label పొందడానికి, `choice-label()` ఉపయోగించండి:

```
calculate: choice-label(${education_level}, ${education_level})
```

## స్వేచ్ఛా టెక్స్ట్‌తో "Other" ఎంపిక

ఒక text field వెల్లడించే "other" ఎంపిక చేర్చడం సాధారణ నమూనా:

| type | name | label | relevant |
|------|------|-------|----------|
| select_one occupation | job | What is your occupation? | |
| text | job_other | Please specify | `${job} = 'other'` |

**choices:**

| list_name | name | label |
|-----------|------|-------|
| occupation | farmer | Farmer |
| occupation | trader | Trader |
| occupation | student | Student |
| occupation | other | Other (please specify) |

## ఉత్తమ పద్ధతులు

1. జాబితాలు చిన్నవిగా మరియు పరస్పరం ప్రత్యేకంగా ఉంచండి — ప్రతిస్పందించే వ్యక్తులు ఒకటి కంటే ఎక్కువ కావాలనుకుంటే `select_multiple` ఉపయోగించండి.
2. అత్యంత సాధారణ సమాధానాన్ని మొదట ఉంచండి, లేదా పొడవైన జాబితాలకు alphabetically క్రమం పెట్టండి.
3. వర్తించే చోట ఎల్లప్పుడూ "Don't know" లేదా "Prefer not to answer" ఎంపిక చేర్చండి.
4. Screen space ఆదా చేయడానికి mobile లో 7–8 కంటే ఎక్కువ ఎంపికలున్న జాబితాలకు `minimal` (dropdown) ఉపయోగించండి.

## పరిమితులు

- ప్రతిస్పందించే వ్యక్తి కేవలం ఒక ఎంపిక ఎంచుకోవచ్చు — బహుళ-సమాధాన ప్రశ్నలకు `select_multiple` ఉపయోగించండి.
- `likert` అపీరెన్స్ ఒక వరుసలో సరిపోయే 5–7 ఎంపికలతో ఉత్తమంగా పని చేస్తుంది.
- `quick` auto-advance mobile-మాత్రమే; వెబ్ ఫారాలలో ఇది ప్రభావం చూపదు.
