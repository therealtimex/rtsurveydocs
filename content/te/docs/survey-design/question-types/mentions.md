---
title: "Mentions"
description: "వినియోగదారులు లేదా ఎంటిటీలను ఇన్‌లైన్‌లో ట్యాగ్ చేయడానికి @-మెన్షన్ ఆటోకంప్లీట్‌తో కూడిన టెక్స్ట్ ఫీల్డ్."
icon: "alternate_email"
date: "2026-04-08T00:00:00+00:00"
lastmod: "2026-04-08T00:00:00+00:00"
draft: false
toc: true
weight: 262
---

`mentions` ప్రశ్న రకం వినియోగదారు `@` టైప్ చేసినప్పుడు autocomplete dropdown సక్రియం చేసే text input. స్వేచ్ఛా-టెక్స్ట్ ప్రతిస్పందనలో వినియోగదారులు, సిబ్బంది పేర్లు, కోడ్‌లు, లేదా ఏ ఎంటిటీనైనా inline లో tag చేయడానికి ఉపయోగించబడుతుంది.

## ప్రాథమిక XLSForm స్పెసిఫికేషన్

| type | name | label |
|------|------|-------|
| mentions | note_text | పరిశీలన నోట్‌లు నమోదు చేయండి (సిబ్బంది సభ్యుని tag చేయడానికి @ ఉపయోగించండి) |

## ప్రవర్తన

- సాధారణ టైపింగ్ సాధారణ టెక్స్ట్ ఉత్పత్తి చేస్తుంది.
- `@` తర్వాత అక్షరాలు టైప్ చేయడం configured జాబితా లేదా API కు వ్యతిరేకంగా autocomplete search సక్రియం చేస్తుంది.
- ఒక suggestion ఎంచుకోవడం mention token ని టెక్స్ట్‌లో insert చేస్తుంది.
- నిల్వ చేయబడిన విలువ embedded mention tokens తో సహా పూర్తి text string.

## వినియోగాలు

1. నిర్దిష్ట సిబ్బంది సభ్యులు లేదా ఎంటిటీలను పేరు ద్వారా reference చేసే qualitative notes
2. బహుళ వ్యక్తులు లేదా స్థానాలు tag చేయవలసిన పరిశీలన records
3. Controlled inline references downstream analysis మెరుగుపరిచే ఏ free-text field

## ప్లాట్‌ఫారమ్ మద్దతు

వెబ్ ఫారాలలో మద్దతు ఇవ్వబడింది.

## పరిమితులు

- ప్రామాణిక XLSForm స్పెసిఫికేషన్‌లో భాగం కాదు — rtSurvey పొడిగింపు మాత్రమే.
- Mention జాబితా source (static లేదా API-driven) XLSForm లో కాకుండా server స్థాయిలో configure చేయబడుతుంది.
