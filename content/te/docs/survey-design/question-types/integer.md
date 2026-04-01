---
title: "Integer"
description: "Integer ప్రశ్నలు మీ సర్వేలో మొత్తం సంఖ్య inputs అనుమతిస్తాయి."
icon: "123"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 222
---

XLSForms మరియు rtSurvey లో integer ప్రశ్న రకం మొత్తం సంఖ్య ప్రతిస్పందనలు సేకరించడానికి ఉపయోగించబడుతుంది. గణనలు, వయసులు, లేదా సంవత్సరాలు వంటి దశాంశ స్థానాలు లేకుండా సంఖ్యా డేటా సేకరించడానికి ఈ ప్రశ్న రకం అవసరం.

## ప్రాథమిక XLSForm స్పెసిఫికేషన్

| type    | name  | label                 |
|---------|-------|------------------------|
| integer | age   | Enter your age in years|

ప్రాథమిక integer ప్రశ్న రకంపై మరిన్ని వివరాలకు, [XLSForm specification](https://xlsform.org/en/#question-types) చూడండి.

## వినియోగాలు

Integer ప్రశ్నలు సాధారణంగా వీటికి ఉపయోగిస్తారు:

1. వయసు inputs
2. అంశాలు గణించడం (ఉదా. పిల్లల సంఖ్య, గృహ సభ్యులు)
3. సంవత్సరం inputs (ఉదా. పుట్టిన సంవత్సరం)
4. సంఖ్యా scale పై ratings
5. ఏ మొత్తం సంఖ్య డేటా సేకరణ

## Constraints మరియు ధృవీకరణ

నమోదు చేయబడిన విలువ నిర్దిష్ట శ్రేణిలో ఉందని నిర్ధారించడానికి constraints జోడించవచ్చు:

| type    | name  | label                 | constraint        | constraint_message                    |
|---------|-------|------------------------|-------------------|---------------------------------------|
| integer | age   | Enter your age in years| .>0 and .<=120    | Age must be between 1 and 120 years   |

## ఉదాహరణ వినియోగం

గృహ సర్వేలో integer ప్రశ్నలు ఎలా ఉపయోగించవచ్చో ఒక ఉదాహరణ:

| type    | name           | label                                     | constraint | constraint_message                |
|---------|----------------|-------------------------------------------|------------|-----------------------------------|
| integer | household_size | How many people live in your household?   | .>0        | Household size must be at least 1 |
| integer | num_children   | How many children under 18 in the household? | .>=0    | Number of children cannot be negative |
| integer | year_built     | In what year was your house built?        | .>1800 and .<=2023 | Year must be between 1800 and 2023 |

## Integer విలువలతో లెక్కింపు

Integer విలువలు లెక్కింపులలో ఉపయోగించవచ్చు. ఒక ఉదాహరణ:

| type    | name           | label                                     |
|---------|----------------|-------------------------------------------|
| integer | num_adults     | Number of adults in the household         |
| integer | num_children   | Number of children in the household       |
| calculate | total_members | |

calculate వరుసలో, మీరు ఉపయోగించవచ్చు:

```
calculation | ${num_adults} + ${num_children}
```

ఇది మొత్తం గృహ సభ్యుల సంఖ్య పొందడానికి వయోజనులు మరియు పిల్లల సంఖ్యను కలుపుతుంది.

## ఉత్తమ పద్ధతులు

1. ఆశించిన input నిర్దేశించడానికి స్పష్టమైన మరియు సంక్షిప్తమైన labels ఉపయోగించండి.
2. అవాస్తవికమైన లేదా తప్పు inputs నివారించడానికి range constraints అమలు చేయండి.
3. ఉదాహరణలు అందించడానికి లేదా ఆశించిన format స్పష్టం చేయడానికి hint text ఉపయోగించడం పరిగణించండి.
4. పెద్ద సంఖ్యల కోసం, చదవడం సులభతరం చేయడానికి label లో commas లేదా spaces పరిగణించండి.
