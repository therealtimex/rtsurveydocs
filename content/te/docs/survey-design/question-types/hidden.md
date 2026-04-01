---
title: "Hidden"
description: "Hidden fields ప్రతిస్పందించే వ్యక్తికి ఎప్పటికీ చూపించబడని విలువలు నిల్వ చేస్తాయి — సందర్భం pass చేయడానికి, డేటా prefill చేయడానికి, లేదా intermediate results నిల్వ చేయడానికి ఉపయోగిస్తారు."
icon: "eye-slash"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 239
---

`hidden` field ప్రతిస్పందించే వ్యక్తికి **ఎప్పటికీ చూపించబడని** విలువను నిల్వ చేస్తుంది. `calculate` (విలువను compute చేసేది) వలె కాకుండా, `hidden` **బాహ్యంగా అందించిన విలువ** carry చేయడానికి ఉపయోగిస్తారు — ఉదాహరణకు, ఒక task ID, మరొక system నుండి pass చేయబడిన household ID, లేదా form launch అయినప్పుడు inject చేయబడిన enumerator code.

## ప్రాథమిక XLSForm స్పెసిఫికేషన్

| type | name | label |
|------|------|-------|
| hidden | household_id | |

Screen పై ఏమీ render అవ్వదు కాబట్టి hidden fields కు labels అవసరం లేదు.

## వినియోగాలు

Hidden fields సాధారణంగా వీటికి ఉపయోగిస్తారు:

1. Survey management system నుండి pre-assigned ID pass చేయడం (ఉదా. household ID, case number, task code)
2. Form version లేదా deployment metadata నిల్వ చేయడం
3. Form launch అయినప్పుడు enumerator-specific configuration inject చేయడం
4. Linked workflows లో parent form నుండి child form లోకి డేటా carry చేయడం
5. Form web link ద్వారా తెరవబడినప్పుడు URL parameters నుండి విలువ నిల్వ చేయడం

## Default విలువ సెట్ చేయడం

Form తెరుచుకున్నప్పుడు విలువ సెట్ అవ్వాలంటే `default` expression తో `hidden` ఉపయోగించడం అత్యంత సాధారణ pattern:

| type | name | default |
|------|------|---------|
| hidden | deployment_code | 'ZONE_A_2024' |
| hidden | form_version | '3.1' |

## Hidden field ని calculations లో reference చేయడం

Hidden విలువలను `${fieldname}` ఉపయోగించి ఏ ఇతర field వలెనే reference చేయవచ్చు:

| type | name | label | calculation |
|------|------|-------|-------------|
| hidden | zone_code | | |
| calculate | label_prefix | | concat('[', ${zone_code}, '] ') |
| note | intro | ${label_prefix} Welcome to the household survey | |

## Hidden ని prefill / URL parameters తో ఉపయోగించడం

URL ద్వారా web form launch చేసేటప్పుడు, hidden fields populate చేసే parameters pass చేయవచ్చు. ఇది enumerator టైప్ చేయకుండా household ID లేదా task code preload చేయడానికి అనుమతిస్తుంది:

```
https://your-server.com/form/FORMID?household_id=H00123&zone_code=NORTH
```

`household_id` అనే field స్వయంచాలకంగా `H00123` తో populate అవుతుంది.

## ఉత్తమ పద్ధతులు

1. విలువ **బాహ్యంగా inject** చేయబడినప్పుడు మరియు recompute చేయకూడదనుకున్నప్పుడు `calculate` కాదు `hidden` ఉపయోగించండి.
2. విలువ **form లోని ఇతర fields నుండి derived** అయినప్పుడు `calculate` ఉపయోగించండి.
3. Hidden field కు విలువ తప్పనిసరిగా ఉండాలంటే ఎల్లప్పుడూ `default` సెట్ చేయండి — default లేని hidden field empty గా ఉంటుంది.
4. వాటిని వేరు చేయడానికి hidden fields కు స్పష్టమైన పేర్లు పెట్టండి (ఉదా. `_hidden_` తో prefix చేయండి లేదా consistent naming convention ఉపయోగించండి).

## పరిమితులు

- Hidden fields ఇతర fields వలె exported డేటాలో చేర్చబడతాయి.
- వాటిని conditionally చూపించలేరు — అవి ఎల్లప్పుడూ ఉంటాయి (కానీ invisible గా).
- Dynamically compute అయ్యే field అవసరమైతే, `calculate` ఉపయోగించండి.
