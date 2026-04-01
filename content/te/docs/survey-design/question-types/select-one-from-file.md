---
title: "ఫైల్ నుండి Select"
description: "select_one_from_file మరియు select_multiple_from_file ఫారంకు జతచేయబడిన బాహ్య CSV లేదా XML ఫైల్ నుండి డైనమిక్‌గా ఎంపికలు లోడ్ చేస్తాయి."
icon: "file-earmark-spreadsheet"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 241
---

`select_one_from_file` మరియు `select_multiple_from_file` `select_one` మరియు `select_multiple` వలె పని చేస్తాయి, కానీ **choices worksheet** లో ఎంపికలు నిర్వచించే బదులు, ఎంపికలు ఫారంకు జతచేయబడిన **బాహ్య CSV లేదా XML ఫైల్** నుండి లోడ్ చేయబడతాయి. మీ choice జాబితా చాలా పొడవుగా ఉన్నప్పుడు, తరచుగా మారినప్పుడు, లేదా మొత్తం ఫారం తిరిగి నిర్మించకుండా నవీకరించాల్సినప్పుడు ఇది ఉపయోగకరం.

## ప్రాథమిక XLSForm స్పెసిఫికేషన్

| type | name | label |
|------|------|-------|
| select_one_from_file health_facilities.csv | facility | Select the health facility |
| select_multiple_from_file crops.csv | crops | Which crops does the household grow? |

రకం పేరు తర్వాత filename మీరు ఫారం upload చేసేటప్పుడు జతచేసే ఫైల్ పేరుతో సరిపోలాలి.

## CSV ఫైల్ ఫార్మాట్

మీ CSV ఫైల్ కనీసం రెండు కాలమ్‌లు కలిగి ఉండాలి: `name` (నిల్వ చేయబడిన విలువ) మరియు `label` (ప్రదర్శించిన టెక్స్ట్). Filtering కోసం మీరు ఏ సంఖ్య అదనపు కాలమ్‌లు జోడించవచ్చు.

**health_facilities.csv:**

```
name,label,district,type
HF001,Nairobi Central Clinic,Nairobi,clinic
HF002,Westlands Health Centre,Nairobi,health_centre
HF003,Kisumu District Hospital,Kisumu,hospital
```

## ఎంపికలు Filtering చేయడం

ప్రస్తుత context కు సరిపోలే ఎంపికలు మాత్రమే చూపించడానికి `choice_filter` కాలమ్ ఉపయోగించండి. CSV కాలమ్‌లను వాటి కాలమ్ పేరుతో నేరుగా సూచించండి (`${}` లేకుండా):

| type | name | label | choice_filter |
|------|------|-------|---------------|
| select_one districts.csv | district | Select district | |
| select_one_from_file health_facilities.csv | facility | Select facility | district = ${district} |

ఈ ఉదాహరణలో, ఎంచుకున్న జిల్లాలోని facilities మాత్రమే చూపించబడతాయి. `choice_filter` లో `district` CSV ఫైల్‌లోని `district` కాలమ్‌ను సూచిస్తుంది; `${district}` `district` అనే ఫారం ఫీల్డ్‌ను సూచిస్తుంది.

## వినియోగాలు

Select-from-file ప్రశ్నలు సాధారణంగా వీటికి ఉపయోగిస్తారు:

1. **పొడవైన choice జాబితాలు** — health facilities, పాఠశాలలు, గ్రామాలు, జాతుల జాబితాలు (వందలు లేదా వేల అంశాలు)
2. **తరచుగా నవీకరించబడే జాబితాలు** — master జాబితా survey rounds మధ్య మారినప్పుడు, ఫారం తిరిగి నిర్మించకుండా CSV మాత్రమే నవీకరించండి
3. **Shared reference data** — బహుళ ఫారాలలో ఉపయోగించే ఒక CSV ఫైల్
4. **Filtered cascading selects** — ఒక ఫైల్‌లో అన్ని regions/districts/villages లోడ్ చేసి, మాతృ ఎంపిక ఆధారంగా filter చేయండి

## ఫైల్ జతచేయడం

మీరు rtSurvey కి మీ ఫారం upload చేసేటప్పుడు, CSV ఫైల్‌ను **media attachment** గా జతచేయండి. ఫారం నిర్వచనంలోని filename జతచేత ఫైల్ filename తో ఖచ్చితంగా సరిపోలాలి.

{{% alert icon=" " context="warning" %}}
File names case-sensitive. `Health_Facilities.csv` మరియు `health_facilities.csv` వేర్వేరు ఫైల్‌లుగా పరిగణించబడతాయి.
{{% /alert %}}

## ఫైల్ నుండి `choice-label()` ఉపయోగించడం

నోట్ లేదా calculate ఫీల్డ్‌లో ఎంచుకున్న choice యొక్క label చూపించడానికి:

| type | name | label | calculation |
|------|------|-------|-------------|
| select_one_from_file health_facilities.csv | facility | Select facility | |
| calculate | facility_label | | choice-label(${facility}, ${facility}) |
| note | summary | Selected facility: ${facility_label} | |

## ఉత్తమ పద్ధతులు

1. మొబైల్ పరికరాలపై మంచి పనితీరు కోసం మీ CSV ఫైల్‌లను 5,000 వరుసల కంటే తక్కువగా ఉంచండి.
2. ఎల్లప్పుడూ `name` మరియు `label` కాలమ్ చేర్చండి — అదనపు కాలమ్‌లు ఐచ్ఛికం.
3. Cascading selects కోసం, మాతృ కాలమ్‌తో ఒకే CSV ఉపయోగించి `choice_filter` తో filter చేయండి.
4. కాలమ్ నిర్మాణంలో breaking మార్పులు చేసేటప్పుడు CSV filenames version చేయండి (ఉదా. `facilities_v3.csv`).

## పరిమితులు

- చాలా పెద్ద CSV ఫైల్‌లు (10,000+ వరుసలు) ఫారం loading నెమ్మదింపజేయవచ్చు.
- CSV ఫైల్‌లు ఫారంతో పాటు upload చేయాలి — అవి రన్‌టైమ్‌లో URL నుండి fetch చేయబడవు.
- `select_multiple_from_file` అన్ని క్లయింట్‌లలో తక్కువగా మద్దతు ఇవ్వబడుతుంది — ఉపయోగించే ముందు అనుకూలత ధృవీకరించండి.
