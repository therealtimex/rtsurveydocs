---
title: "Text"
description: "rtSurvey లో స్వేచ్ఛా టెక్స్ట్ ప్రతిస్పందన ప్రశ్న రకం"
icon: "text_fields"
date: "2024-07-01T12:00:00+01:00"
lastmod: "2024-07-01T12:00:00+01:00"
draft: false
toc: true
weight: 221
---

`text` ప్రశ్న రకం స్వేచ్ఛా-టెక్స్ట్ ప్రతిస్పందన సేకరిస్తుంది — అక్షరాల ఏ string అయినా. ఇది అత్యంత సౌలభ్యమైన input రకం మరియు పేర్లు, చిరునామాలు, వివరణలు, కోడ్‌లు మరియు మరింత నిర్దిష్ట రకానికి సరిపోని ఏదైనా కోసం ఉపయోగించబడుతుంది.

rtSurvey అదనంగా `text` ని **time input widgets** తో విస్తరిస్తుంది, ఇవి clock picker తో ఖచ్చితమైన సమయ నమోదు అనుమతిస్తాయి.

## ప్రాథమిక XLSForm స్పెసిఫికేషన్

| type | name | label |
|------|------|-------|
| text | respondent_name | Full name of respondent |
| text | address | Home address |

ప్రామాణిక XLSForm text రకంపై మరిన్ని వివరాలకు, [XLSForm specification](https://xlsform.org/en/#question-types) చూడండి.

## వినియోగాలు

Text ప్రశ్నలు వీటికి ఉపయోగిస్తారు:

1. పేర్లు, చిరునామాలు, స్వేచ్ఛా వివరణలు
2. ముక్తకంఠ వ్యాఖ్యలు లేదా అభిప్రాయం
3. integer/decimal కు సరిపోని కోడ్‌లు, IDs, లేదా reference నంబర్‌లు
4. rtSurvey time input పొడిగింపులతో సమయ విలువలు సేకరించడం
5. Autocomplete text fields (`search-autocomplete-noedit-v2()` ద్వారా)

## ప్రామాణిక అపీరెన్స్ ఎంపికలు

| అపీరెన్స్ | వివరణ |
|----------|--------|
| *(none)* | ఒకే-వరుస text input |
| `multiline` | బహుళ-వరుస text area — వెబ్‌లో పొడవైన స్వేచ్ఛా టెక్స్ట్‌కు ఉత్తమం |

## rtSurvey time input పొడిగింపులు

rtSurvey సమయ విలువలు సేకరించడానికి **clock picker widget** తో `text` ని విస్తరిస్తుంది. ఈ అపీరెన్స్ ఎంపికలు గంటలు, నిమిషాలు, సెకన్లు, లేదా మిల్లీసెకన్లు ఎంచుకోవడానికి గణికుడు నొక్కగల clock icon చూపిస్తాయి.

### అపీరెన్స్ వేరియంట్‌లు

| అపీరెన్స్ | వివరణ |
|----------|--------|
| `inline` | ఫీల్డ్ పక్కన Clock icon చూపించబడుతుంది |
| `inline colors("RRGGBB")` | Custom hex రంగుతో Clock icon |
| `inline-1line` | Compact single-row format లో Clock చూపించబడుతుంది |
| `inline-1line-RRGGBB` | Custom icon రంగుతో single-row (hex, `#` లేకుండా) |
| `inline-1line colors("RRGGBB","RRGGBB")` | రెండు రంగులతో single-row |
| `inline-onlyresult` | ఎంపిక తర్వాత Clock icon అదృశ్యమవుతుంది; విలువ మాత్రమే చూపించబడుతుంది |
| `inline-onlyresult colors("RRGGBB")` | Custom icon రంగుతో అదే |

### సమయ ఫార్మాట్ tokens

ప్రదర్శించే సమయ భాగాలు నియంత్రించడానికి brackets లో format string జోడించండి:

| Format string | చూపిస్తుంది |
|---------------|------------|
| `inline-[%H:%M]` | గంటలు మరియు నిమిషాలు (24-గంట) |
| `inline-[%h:%M]` | గంటలు మరియు నిమిషాలు (12-గంట) |
| `inline-[%H:%M:%S]` | గంటలు, నిమిషాలు, సెకన్లు (24-గంట) |
| `inline-[%H:%M:%3]` | గంటలు, నిమిషాలు, మిల్లీసెకన్లు |
| `inline-[%M:%S]` | నిమిషాలు మరియు సెకన్లు మాత్రమే |
| `inline-[%S]` | సెకన్లు మాత్రమే |
| `inline-[%3]` | మిల్లీసెకన్లు మాత్రమే |

### ఉదాహరణ: నిమిషాలు మరియు సెకన్లలో పని వ్యవధి రికార్డ్ చేయడం

| type | name | label | appearance |
|------|------|-------|------------|
| text | task_duration | Time taken to complete the task | `inline-[%M:%S]` |

### ఉదాహరణ: Custom రంగుతో 24-గంట format లో సంఘటన సమయం రికార్డ్ చేయడం

| type | name | label | appearance |
|------|------|-------|------------|
| text | event_time | Time of event | `inline-1line colors("0099FF")` |

## డేటా ఫార్మాట్

Text డేటా plain string గా నిల్వ చేయబడి ఎగుమతి చేయబడుతుంది. inline clock widget ఉపయోగించే time-ఆధారిత inputs కోసం, విలువ ఎంచుకున్న format string కి సరిపోలే ఫార్మాట్‌లో నిల్వ చేయబడుతుంది (ఉదా. `%H:%M` కోసం `14:32`).

## Constraints మరియు ధృవీకరణ

Format, పొడవు, లేదా pattern అమలు చేయడానికి constraints వర్తించండి:

| type | name | label | constraint | constraint_message |
|------|------|-------|------------|-------------------|
| text | name | Full name | `string-length(.) >= 2` | Name must be at least 2 characters |
| text | code | Reference code | `regex(., '^[A-Z]{2}[0-9]{4}$')` | Enter 2 uppercase letters followed by 4 digits |
| text | phone | Phone number | `regex(., '^[0-9]{9,15}$')` | Enter a valid phone number |

## ఉత్తమ పద్ధతులు

1. డేటా తెలిసిన నిర్మాణం కలిగి ఉన్నప్పుడు మరింత నిర్దిష్ట రకాలు (`integer`, `decimal`, `date`) ఉపయోగించండి — ఇది చెల్లుబాటు కాని నమోదులు నివారించి విశ్లేషణ సులభతరం చేస్తుంది.
2. కోడ్‌లు లేదా IDs ధృవీకరించడానికి `string-length()` లేదా `regex()` తో `constraint` జోడించండి.
3. ప్రతిస్పందించే వ్యక్తులు అనేక వాక్యాలు వ్రాయగల ముక్తకంఠ ప్రశ్నలకు `multiline` అపీరెన్స్ ఉపయోగించండి.
4. సమయ సేకరణకు, మీ విశ్లేషణకు అవసరమైన ఖచ్చితత కి సరిపోలే సమయ format tokens ఎంచుకోండి.

## ప్లాట్‌ఫారమ్ మద్దతు

Text ప్రశ్న రకం మరియు అన్ని time input appearances iOS, Android మరియు వెబ్ ప్లాట్‌ఫారమ్‌లపై మద్దతు ఇవ్వబడతాయి.

## పరిమితులు

- Text ప్రతిస్పందనలు స్వేచ్ఛా-రూపంలో ఉంటాయి — regex patterns అతీతంగా అంతర్నిర్మిత spell check లేదా vocabulary constraint లేదు.
- inline time widget rtSurvey పొడిగింపు మరియు ప్రామాణిక XLSForm స్పెసిఫికేషన్‌లో భాగం కాదు.
