---
title: "Note"
description: "Note ప్రశ్నలు మీ సర్వేలో సమాచారం లేదా సూచనలు అందించడానికి read-only text లేదా media చూపిస్తాయి."
icon: "info"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 255
---

XLSForms మరియు rtSurvey లో note ప్రశ్న రకం survey respondent కు read-only text లేదా media చూపించడానికి ఉపయోగిస్తారు. ఇది సమాధానం అవసరమైన ప్రశ్న కాదు, బదులుగా survey లో సమాచారం, సూచనలు, లేదా సందర్భం అందించే మార్గం.

## ప్రాథమిక XLSForm స్పెసిఫికేషన్

| type | name | label |
|------|------|-------|
| note | info_text | This survey is about your reading habits. |

ప్రాథమిక note ప్రశ్న రకంపై మరిన్ని వివరాలకు, [XLSForm specification](https://xlsform.org/en/#question-types) చూడండి.

## వినియోగాలు

Note ప్రశ్నలు సాధారణంగా వీటికి ఉపయోగిస్తారు:

1. రాబోయే ప్రశ్నలకు సూచనలు లేదా సందర్భం అందించడం
2. లెక్కించిన ఫలితాలు లేదా summaries చూపించడం
3. Images లేదా ఇతర media చూపించడం
4. Survey sections వేరు చేయడం
5. మునుపటి ప్రతిస్పందనల ఆధారంగా feedback ఇవ్వడం

## ఉత్తమ పద్ధతులు

1. Respondent engagement నిలుపుకోవడానికి note text సంక్షిప్తంగా మరియు స్పష్టంగా ఉంచండి.
2. ముఖ్యమైన సమాచారాన్ని నొక్కిచెప్పడానికి formatting (bold, italics) ఉపయోగించండి.
3. అవసరమైనప్పుడు అర్థం మెరుగుపరచడానికి media (images, audio) ఉపయోగించడాన్ని పరిగణించండి.
4. Survey crowded అవ్వకుండా notes తక్కువగా ఉపయోగించండి.

## ఉదాహరణ వినియోగం

సర్వేలో note ప్రశ్నలు ఎలా ఉపయోగించవచ్చో ఒక ఉదాహరణ:

| type | name | label |
|------|------|-------|
| note | intro | Welcome to our reading habits survey. We'll ask about your preferences and reading frequency. |
| ... | ... | ... |
| calculate | books_per_month | ${fiction_books} + ${non_fiction_books} |
| note | reading_summary | You read approximately ${books_per_month} books per month. |

ఈ ఉదాహరణలో, survey introduce చేయడానికి మరియు లెక్కించిన ఫలితాల summary అందించడానికి notes ఉపయోగిస్తున్నాము.

## rtSurvey పొడిగింపులు

note ప్రశ్నల కోసం ప్రాథమిక XLSForm specification సరళంగా ఉన్నప్పటికీ, rtSurvey అదనపు ఫీచర్‌లు లేదా అనుకూలీకరణలు అందించవచ్చు:

1. Rich text formatting
2. Embedded media కు మద్దతు (images, audio, video)
3. మునుపటి ప్రతిస్పందనల ఆధారంగా dynamic content
4. Custom styling options

## అధునాతన వినియోగం

### షరతులతో కూడిన Display

Notes conditionally చూపించడానికి relevance expressions ఉపయోగించవచ్చు:

| type | name | label | relevant |
|------|------|-------|----------|
| note | high_reader_note | You're an avid reader! | ${books_per_month} > 5 |

### Calculations చేర్చడం

Notes dynamic feedback అందించడానికి calculations చేర్చవచ్చు:

| type | name | label |
|------|------|-------|
| note | reading_time | Based on your responses, you spend approximately ${books_per_month * 5} hours reading each month. |

## పరిమితులు

- Notes డేటా సేకరించవు, కాబట్టి respondents నుండి సమాచారం పొందాల్సినప్పుడు వాటిని ఉపయోగించకూడదు.
- Notes అతిగా ఉపయోగిస్తే survey crowded గా లేదా చాలా పొడవుగా అనిపించవచ్చు.
- కొన్ని అధునాతన formatting లేదా media options అన్ని devices లేదా platforms పై మద్దతు లేకపోవచ్చు.
