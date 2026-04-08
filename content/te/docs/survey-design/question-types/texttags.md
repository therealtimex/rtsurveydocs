---
title: "Text Tags"
description: "ట్యాగ్ ఇన్‌పుట్ ఫీల్డ్ — ప్రతిస్పందకులు టైప్ చేసి Enter నొక్కి వేర్వేరు ట్యాగ్ టోకెన్‌లను సృష్టిస్తారు."
icon: "label"
date: "2026-04-08T00:00:00+00:00"
lastmod: "2026-04-08T00:00:00+00:00"
draft: false
toc: true
weight: 264
---

`texttags` ప్రశ్న రకం (`text_tags` గా కూడా alias చేయబడింది) వినియోగదారు నమోదు చేసిన ప్రతి విలువ వేర్వేరు **tag token** అయ్యే input రెండర్ చేస్తుంది. వినియోగదారులు విలువ టైప్ చేసి, Enter లేదా delimiter key నొక్కుతారు, మరియు విలువ తొలగించగలిగే chip గా జోడించబడుతుంది. ఒక ప్రతిస్పందనలో బహుళ tags జోడించవచ్చు.

## ప్రాథమిక XLSForm స్పెసిఫికేషన్

| type | name | label |
|------|------|-------|
| texttags | keywords | కీవర్డ్‌లు నమోదు చేయండి (ప్రతిదాని తర్వాత Enter నొక్కండి) |

## ప్రవర్తన

- ప్రతి confirmed entry ఫీల్డ్ లోపల pill/chip గా ప్రదర్శించబడే tag అవుతుంది.
- Chip పై × క్లిక్ చేసి Tags వ్యక్తిగతంగా తొలగించవచ్చు.
- నిల్వ చేయబడిన విలువ నమోదు చేసిన అన్ని tags యొక్క space-separated string.

## వినియోగాలు

1. ముందే నిర్వచించిన జాబితా లేకుండా బహుళ free-text keywords లేదా codes సేకరించడం
2. విలువల సమూహం open-ended అయిన labeling లేదా categorisation fields
3. `select_multiple` చాలా rigid అయిన ఏ multi-value free-text input

## డేటా ఫార్మాట్

Tags ఒకే space-separated string గా నిల్వ చేయబడతాయి. ఉదాహరణకు, వినియోగదారు `మలేరియా`, `జ్వరం`, మరియు `దగ్గు` నమోదు చేస్తే, నిల్వ చేయబడిన విలువ `మలేరియా జ్వరం దగ్గు`.

## ప్లాట్‌ఫారమ్ మద్దతు

వెబ్ ఫారాలలో మద్దతు ఇవ్వబడింది.

## పరిమితులు

- ప్రామాణిక XLSForm స్పెసిఫికేషన్‌లో భాగం కాదు — rtSurvey పొడిగింపు మాత్రమే.
- విలువలు free-text కాబట్టి, downstream analysis కు spaces పై string splitting అవసరం.
