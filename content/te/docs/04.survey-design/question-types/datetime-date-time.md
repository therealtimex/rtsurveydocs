---
title: "Datetime, date, time"
description: "Datetime ప్రశ్నలు ప్రతిస్పందించే వ్యక్తులు ఒకే ఫీల్డ్‌లో తేది మరియు సమయం రెండూ input చేయడానికి అనుమతిస్తాయి."
icon: "event"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 226
---

XLSForms మరియు rtSurvey లో datetime ప్రశ్న రకం ప్రతిస్పందించే వ్యక్తులు ఒకే ఫీల్డ్‌లో తేది మరియు సమయం రెండూ input చేయడానికి అనుమతిస్తుంది. తేది మరియు ఖచ్చితమైన సమయంతో సహా నిర్దిష్ట క్షణం సేకరించాల్సినప్పుడు ఈ ప్రశ్న రకం ఉపయోగకరం.

## ప్రాథమిక XLSForm స్పెసిఫికేషన్

| type     | name           | label                           |
|----------|----------------|--------------------------------|
| datetime | event_datetime | When did the event occur?       |

ప్రాథమిక datetime ప్రశ్న రకంపై మరిన్ని వివరాలకు, [XLSForm specification](https://xlsform.org/en/#question-types) చూడండి.

## వినియోగాలు

Datetime ప్రశ్నలు సాధారణంగా వీటికి ఉపయోగిస్తారు:

1. సంఘటనలు లేదా పరిశీలనల timestamps రికార్డ్ చేయడం
2. Appointments లేదా meetings schedule చేయడం
3. కార్యకలాపాల start మరియు end సమయాలు log చేయడం
4. Time-sensitive డేటా సేకరణకు ఖచ్చితమైన క్షణాలు సేకరించడం

## rtSurvey పొడిగింపులు

rtSurvey datetime ప్రశ్నల కార్యాచరణను వివిధ appearances మరియు అనుకూలీకరణ ఎంపికలతో విస్తరిస్తుంది:

### అపీరెన్స్ ఎంపికలు

- `(default)`: తేది మరియు సమయం ఎంచుకోవడానికి calendar మరియు clock చూపిస్తుంది
- `inline`: Calendar మరియు clock icons గా చూపిస్తుంది
- `inline-1line`: Calendar మరియు clock ఒకే వరుస format లో చూపిస్తుంది
- `inline-onlyresult`: line చివర్లో icons చూపిస్తుంది; ఎంపిక తర్వాత అదృశ్యమవుతాయి

### రంగు అనుకూలీకరణ

`colors()` ఫంక్షన్ ఉపయోగించి calendar మరియు clock icons రంగు అనుకూలీకరించవచ్చు:

- `inline colors("0099FF")`: Custom రంగుతో icons చూపిస్తుంది
- `inline-1line colors("0000FF","FFFF00")`: బహుళ custom రంగులతో single row format లో

### Custom తేది మరియు సమయ formats

rtSurvey ప్రత్యేక సింటాక్స్ ఉపయోగించి custom తేది మరియు సమయ formats కు అనుమతిస్తుంది:

- `inline-[%Y-%m-%d %H:%M:%S]`: Custom format ఉదాహరణ (Year-Month-Day Hour:Minute:Second)
- `inline-[%d/%m/%Y %I:%M %p]`: Custom format ఉదాహరణ (Day/Month/Year Hour:Minute AM/PM)

## ఉదాహరణ వినియోగం

సర్వేలో datetime ప్రశ్న ఎలా ఉపయోగించవచ్చో ఒక ఉదాహరణ:

| type     | name           | label                                      | appearance                    |
|----------|----------------|--------------------------------------------|-----------------------------|
| datetime | incident_time  | When did the incident occur?               | inline-[%d/%m/%Y %I:%M %p]  |

## ఉత్తమ పద్ధతులు

1. ఆశించిన తేది మరియు సమయ format పై స్పష్టమైన సూచనలు అందించండి.
2. మరింత compact ప్రదర్శన కోసం `inline` అపీరెన్స్ ఉపయోగించడాన్ని పరిగణించండి.
3. నిర్దిష్ట తేది మరియు సమయ భాగాలు లేదా formatting అవసరమైనప్పుడు custom formats ఉపయోగించండి.
4. వివిధ ప్రాంతాలలో datetime డేటా సేకరించేటప్పుడు time zones పట్ల జాగ్రత్తగా ఉండండి.

## పరిమితులు

- అన్ని పరికరాలు లేదా ప్లాట్‌ఫారమ్‌లపై కొన్ని appearances లేదా custom formats మద్దతు లేకపోవచ్చు.
- ముఖ్యంగా custom formats తో తేది మరియు సమయం సరిగ్గా input చేయడానికి వినియోగదారులకు మార్గదర్శనం అవసరం కావచ్చు.
- సరిగ్గా పరిగణించకపోతే Time zone తేడాలు డేటా విశ్లేషణను జటిలం చేయవచ్చు.
