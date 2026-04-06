---
title: "గ్రిడ్ లేఔట్"
description: "గ్రిడ్ లేఔట్ మీకు సమూహంలో CSS grid లో ఫీల్డ్‌లు ఉంచడానికి అనుమతిస్తుంది, బహుళ-కాలమ్ ఫారం డిజైన్‌లు సృష్టించడానికి వీలు కల్పిస్తుంది."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 296
---

**గ్రిడ్ లేఔట్** ఫీచర్ `gridformat<>` అపీరెన్స్ ట్యాగ్ ఉపయోగించి సమూహంలో ప్రశ్నలను **బహుళ-కాలమ్ grid** లో అమర్చడానికి అనుమతిస్తుంది. బహుళ సంబంధిత ఫీల్డ్‌లు నిలువుగా స్టాక్ చేయబడటం కాకుండా పక్కపక్కన కనిపించాల్సిన దట్టమైన డేటా-ఎంట్రీ ఫారాలకు ఇది ఉపయోగకరం.

---

## ఇది ఎలా పని చేస్తుంది

గ్రిడ్ లేఔట్ రెండు స్థాయిలలో వర్తించబడుతుంది:

1. **సమూహం** — grid ఎన్ని కాలమ్‌లు కలిగి ఉందో నిర్వచించడానికి `appearance: field-list grid(weight=N)` సెట్ చేయండి
2. **సమూహంలోని ప్రతి ఫీల్డ్** — ఫీల్డ్‌ను ఉంచడానికి `appearance: gridformat<row=R col=C colspan=S/>` సెట్ చేయండి

Grid 12-కాలమ్ Bootstrap-శైలి వ్యవస్థ ఉపయోగిస్తుంది. `weight=N` మీ grid ఎన్ని లాజికల్ కాలమ్‌లు కలిగి ఉందో నిర్వచిస్తుంది; ప్రతి కాలమ్ `12/N` Bootstrap కాలమ్‌లు ఆక్రమిస్తుంది.

---

## సమూహ-స్థాయి అపీరెన్స్

| అపీరెన్స్ | వివరణ |
|-----------|--------|
| `field-list grid(weight=2)` | 2-కాలమ్ grid (ప్రతి కాలమ్ = 6 Bootstrap cols) |
| `field-list grid(weight=3)` | 3-కాలమ్ grid (ప్రతి కాలమ్ = 4 Bootstrap cols) |
| `field-list grid(weight=4)` | 4-కాలమ్ grid (ప్రతి కాలమ్ = 3 Bootstrap cols) |
| `field-list grid(weight=6)` | 6-కాలమ్ grid (ప్రతి కాలమ్ = 2 Bootstrap cols) |

---

## ఫీల్డ్-స్థాయి `gridformat<>` సింటాక్స్

```
gridformat<row=R col=C colspan=S/>
gridformat<row=R col=C colspan=S backgroundcolor=COLOR/>
```

| Attribute | వివరణ |
|-----------|--------|
| `row` | వరుస సంఖ్య (1-ఆధారిత) |
| `col` | కాలమ్ సంఖ్య (1-ఆధారిత, `weight` నిర్వచించిన grid లో) |
| `colspan` | ఈ ఫీల్డ్ విస్తరించే కాలమ్‌ల సంఖ్య (డిఫాల్ట్ 1) |
| `backgroundcolor` | ఫీల్డ్ నేపథ్యానికి ఐచ్ఛిక CSS రంగు (ఉదా. `#f0f0f0`, `lightblue`) |

---

## ఉదాహరణ: 2-కాలమ్ గృహ సర్వే విభాగం

| type | name | label | appearance |
|------|------|-------|------------|
| begin_group | demographics | Demographics | `field-list grid(weight=2)` |
| text | first_name | First name | `gridformat<row=1 col=1/>` |
| text | last_name | Last name | `gridformat<row=1 col=2/>` |
| integer | age | Age | `gridformat<row=2 col=1/>` |
| select_one gender | gender | Gender | `gridformat<row=2 col=2/>` |
| text | address | Full address | `gridformat<row=3 col=1 colspan=2/>` |
| end_group | | | |

ఇది ఇలా రెండర్ చేయబడుతుంది:

```
[ First name        ] [ Last name          ]
[ Age               ] [ Gender             ]
[ Full address (spans both columns)        ]
```

---

## ఉదాహరణ: 3-కాలమ్ ప్లాట్ డేటా ఎంట్రీ

| type | name | label | appearance |
|------|------|-------|------------|
| begin_group | plot_data | Plot details | `field-list grid(weight=3)` |
| text | plot_id | Plot ID | `gridformat<row=1 col=1/>` |
| decimal | area_ha | Area (ha) | `gridformat<row=1 col=2/>` |
| select_one crop_type | crop | Crop type | `gridformat<row=1 col=3/>` |
| decimal | yield | Yield (kg) | `gridformat<row=2 col=1/>` |
| decimal | revenue | Revenue | `gridformat<row=2 col=2/>` |
| text | notes | Notes | `gridformat<row=2 col=3/>` |
| end_group | | | |

---

## నేపథ్య రంగులు

విభాగాలు దృశ్యంగా వేరు చేయడానికి `backgroundcolor` ఉపయోగించండి:

| type | name | label | appearance |
|------|------|-------|------------|
| note | section_a | Section A | `gridformat<row=1 col=1 colspan=2 backgroundcolor=#e8f4f8/>` |

---

## ఉత్తమ పద్ధతులు

1. పక్కపక్కన ఫీల్డ్‌లు నిజంగా స్క్రోలింగ్ తగ్గించే **డేటా-ఎంట్రీ ఇంటెన్సివ్** స్క్రీన్‌లకు మాత్రమే గ్రిడ్ లేఔట్ ఉపయోగించండి.
2. `colspan=1` ఫీల్డ్‌లు చిన్నగా ఉంచండి (IDs, కోడ్‌లు, చిన్న selects) — వెడల్పు లేబుళ్ళు ఇరుకైన grid కాలమ్‌లలో చెడుగా truncate అవుతాయి.
3. పొడవైన లేబుళ్ళు లేదా బహుళ-వరుస టెక్స్ట్ ఇన్‌పుట్‌లు కలిగిన ఫీల్డ్‌లకు `colspan=N` ఉపయోగించండి.
4. మీరు ఆశించే చిన్న స్క్రీన్ పరిమాణంపై పరీక్షించండి — 4-కాలమ్ grid ఫోన్‌లో ఇరుకుగా ఉంటుంది.
5. గ్రిడ్ లేఔట్ వెబ్ మరియు tablet ఫారం కారకాలపై ఉత్తమంగా పని చేస్తుంది; మొబైల్ ఫోన్‌లపై 2-కాలమ్ లేఔట్ సాధారణంగా గరిష్ట సౌకర్యవంతమైన వెడల్పు.

## పరిమితులు

- `gridformat<>` మాత్రమే `grid(weight=N)` అపీరెన్స్‌తో సమూహంలో పని చేస్తుంది — ఇది శీర్ష స్థాయిలో ప్రభావం చూపదు.
- గ్రిడ్ లేఔట్ rtSurvey వెబ్ ఫారం పొడిగింపు మరియు ఇతర ODK-అనుకూల క్లయింట్‌లలో సరిగ్గా రెండర్ కాకపోవచ్చు.
- వరుస మరియు కాలమ్ స్థాపన ఫారం నిర్మాణ సమయంలో ధృవీకరించబడదు — అతివ్యాపించే ఫీల్డ్‌లు రెండూ రెండర్ అవుతాయి కానీ విచ్ఛిన్నంగా కనిపించవచ్చు.
