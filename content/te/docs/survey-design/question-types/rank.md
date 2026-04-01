---
title: "Rank"
description: "Rank ప్రశ్నలు ప్రతిస్పందించే వ్యక్తులు ఎంపికల సమితిని ప్రాధాన్యత లేదా ప్రాముఖ్యత ఆధారంగా వరుస పెట్టడానికి అనుమతిస్తాయి."
icon: "list-ol"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 242
---

`rank` ప్రశ్న రకం ప్రతిస్పందించే వ్యక్తి **drag చేసి వరుస పెట్టాల్సిన** (లేదా మొదటి నుండి చివరి వరకు rank ఇవ్వాల్సిన) ఎంపికల జాబితాను చూపిస్తుంది. ఎంచుకున్న వరుసలో ఎంపిక విలువల space-separated జాబితాగా ఫలితం నిల్వ చేయబడుతుంది, అత్యధిక-ప్రాధాన్యత ఎంపిక మొదట.

## ప్రాథమిక XLSForm స్పెసిఫికేషన్

| type | name | label |
|------|------|-------|
| rank priorities | main_priority | Rank these community needs from most to least important |

ఎంపికలు `select_one` వలె **choices worksheet** లో నిర్వచించబడతాయి:

**survey:**

| type | name | label |
|------|------|-------|
| rank priorities | main_priority | Rank these needs from most to least important |

**choices:**

| list_name | name | label |
|-----------|------|-------|
| priorities | water | Clean water |
| priorities | health | Healthcare |
| priorities | education | Education |
| priorities | roads | Roads |
| priorities | electricity | Electricity |

## నిల్వ చేయబడిన విలువ ఫార్మాట్

నిల్వ చేయబడిన విలువ rank వరుసలో ఎంపిక విలువల **space-separated జాబితా** (మొదటి = అత్యధిక ప్రాధాన్యత):

```
water education health roads electricity
```

## Ranked స్థానాలు సేకరించడం

నిర్దిష్ట rank వద్ద ఎంపిక పొందడానికి `selected-at()` ఉపయోగించండి:

| type | name | label | calculation |
|------|------|-------|-------------|
| rank priorities | main_priority | Rank community needs | |
| calculate | top_priority | | selected-at(${main_priority}, 0) |
| calculate | second_priority | | selected-at(${main_priority}, 1) |

`selected-at(${main_priority}, 0)` **మొదటి** ఉన్న విలువ తిరిగి ఇస్తుంది (index 0 = top rank).

## రిపీట్ సమూహాలతో `rank-index()` ఉపయోగించడం

రిపీట్ సమూహంలో `rank` ఉన్నప్పుడు, `rank-index()` రిపీట్ వెలుపల నుండి ordinal rank సూచించడానికి అనుమతిస్తుంది:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | first_ranked | | rank-index(1, ${score}) |

`rank-index(1, ${score})` అత్యధిక score యొక్క instance index తిరిగి ఇస్తుంది.

## వినియోగాలు

Rank ప్రశ్నలు సాధారణంగా వీటికి ఉపయోగిస్తారు:

1. **ప్రాధాన్యత ranking** — అభివృద్ధి అవసరాలు rank ఇవ్వమని communities అడగడం
2. **Preference ordering** — product features, service attributes, లేదా policy options ranking
3. **పరీక్ష అంశాల వరుస** — ఒక process లో దశలు అమర్చడం
4. **Top-N ఎంపిక** — కేవలం top 1, 2, లేదా 3 ఎంపికలు సేకరించడానికి `selected-at()` తో కలపడం

## ఉత్తమ పద్ధతులు

1. జాబితా చిన్నగా ఉంచండి (3–7 అంశాలు) — 7–8 ఎంపికలకు మించి ranking cognitively taxing అవుతుంది.
2. "మొదటి" అంటే ఏమిటో అయోమయం నివారించడానికి స్పష్టమైన, పరస్పరం ప్రత్యేకమైన choice labels ఉపయోగించండి.
3. Ranking direction వివరించడానికి hint text జోడించండి (ఉదా. "Drag to order: first = most important").
4. అన్ని ఎంపికలు rank ఇవ్వబడ్డాయని నిర్ధారించడానికి `count-selected(.) = x` తో validate చేయండి.

## పరిమితులు

- Drag-to-rank widget touch screen లేదా mouse అవసరం — keyboard-only environments లో బాగా పని చేయకపోవచ్చు.
- కొన్ని పాత మొబైల్ క్లయింట్‌లలో, rank widget numbered input interface కి fall back కావచ్చు.
- మీరు పాక్షికంగా rank ఇవ్వలేరు — అన్ని ఎంపికలు వరుస పెట్టాలి.
