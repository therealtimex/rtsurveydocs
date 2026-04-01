---
title: "Appearance"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 288
---

rtSurvey में `appearance` कॉलम आपको अपने सर्वेक्षण में प्रश्नों की विज़ुअल प्रस्तुति और व्यवहार को अनुकूलित करने की अनुमति देता है। यह सुविधा उपयोगकर्ता अनुभव को बेहतर बनाती है और डेटा संग्रह दक्षता में महत्वपूर्ण सुधार कर सकती है। rtSurvey मानक XLSForm appearance attributes का समर्थन करता है और उन्हें अतिरिक्त विकल्पों के साथ विस्तारित करता है।

## मानक XLSForm Appearance Attributes

rtSurvey निम्नलिखित मानक XLSForm appearance attributes का समर्थन करता है:

| Appearance Attribute | प्रश्न प्रकार | विवरण |
|----------------------|----------------|-------------|
| multiline | text | मल्टी-लाइन टेक्स्ट बॉक्स बनाता है (वेब क्लाइंट के लिए सबसे अच्छा) |
| minimal | select_one, select_multiple | विकल्पों को ड्रॉपडाउन मेनू में प्रदर्शित करता है |
| quick | select_one | चयन के बाद अगले प्रश्न पर स्वचालित रूप से आगे बढ़ता है (केवल मोबाइल) |
| no-calendar | date | कैलेंडर प्रदर्शन को दबाता है (केवल मोबाइल) |
| month-year | date | केवल महीने और वर्ष का चयन करने की अनुमति देता है |
| year | date | केवल वर्ष का चयन करने की अनुमति देता है |
| horizontal-compact | select_one, select_multiple | विकल्पों को क्षैतिज रूप से प्रदर्शित करता है (केवल वेब) |
| horizontal | select_one, select_multiple | विकल्पों को कॉलम में क्षैतिज रूप से प्रदर्शित करता है (केवल वेब) |
| likert | select_one | विकल्पों को Likert पैमाने के रूप में प्रस्तुत करता है |
| compact | select_one, select_multiple | न्यूनतम padding के साथ विकल्पों को साथ-साथ प्रदर्शित करता है |
| quickcompact | select_one | compact प्रदर्शन और ऑटो-एडवांस को संयोजित करता है (केवल मोबाइल) |
| field-list | groups | पूरे समूह को एक स्क्रीन पर प्रदर्शित करता है (केवल मोबाइल) |
| label | select_one, select_multiple | इनपुट के बिना विकल्प लेबल दिखाता है |
| list-nolabel | select_one, select_multiple | लेबल के बिना इनपुट दिखाता है (`label` के साथ उपयोग करें) |
| table-list | groups | प्रश्नों को टेबल प्रारूप में प्रदर्शित करता है |
| signature | image | हस्ताक्षर कैप्चर सक्षम करता है (केवल मोबाइल) |
| draw | image | फ्रीहैंड ड्राइंग की अनुमति देता है (केवल मोबाइल) |
| map, quick map | select_one, select_one_from_file | मानचित्र सुविधाओं से चयन सक्षम करता है |

## Appearance का उपयोग करने के लिए सर्वोत्तम अभ्यास

1. **संगतता**: एक समान दिखने के लिए अपने पूरे सर्वेक्षण में appearance attributes का लगातार उपयोग करें।
2. **मोबाइल बनाम वेब**: विचार करें कि विभिन्न डिवाइस और प्लेटफ़ॉर्म पर appearances कैसे रेंडर होंगी।
3. **प्रदर्शन**: उन appearance attributes से सावधान रहें जो फ़ॉर्म लोडिंग को धीमा कर सकते हैं।
4. **उपयोगकर्ता अनुभव**: ऐसी appearances चुनें जो उत्तरदाताओं के लिए डेटा प्रविष्टि को आसान और अधिक सहज बनाती हैं।
5. **परीक्षण**: यह सुनिश्चित करने के लिए हमेशा अपने फ़ॉर्म का लक्ष्य डिवाइस पर परीक्षण करें।

## उन्नत तकनीकें

### Appearances संयोजित करना

कुछ appearance attributes को अधिक जटिल लेआउट के लिए संयोजित किया जा सकता है:

```
| type | name | label | appearance |
|------|------|-------|------------|
| select_one options | choice | एक चुनें: | minimal compact |
```

### डायनामिक Appearances

rtSurvey फ़ॉर्म लॉजिक के आधार पर डायनामिक appearance परिवर्तनों की अनुमति देता है:

```
| type | name | label | appearance | relevant |
|------|------|-------|------------|----------|
| text | time | समय दर्ज करें: | inline-[%H:%M] | ${show_time} = 'yes' |
```

## rtSurvey विस्तारित Appearance Attributes

मानक XLSForm appearances के अतिरिक्त, rtSurvey निम्नलिखित प्लेटफ़ॉर्म-विशिष्ट विकल्पों का समर्थन करता है:

### डेटा और प्रदर्शन नियंत्रण

| Appearance Attribute | प्रश्न प्रकार | विवरण |
|----------------------|----------------|-------------|
| `invisible` | कोई भी | फील्ड को दृष्टि से छिपाता है जबकि इसका मूल्य अभी भी एकत्र या गणना करता है। |
| `displaytitle` | कोई भी | फील्ड के लेबल/शीर्षक को जबरन प्रदर्शित करता है। |
| `autopull` | select_one, select_multiple | फ़ॉर्म लोड होने या trigger फील्ड बदलने पर विकल्पों को पॉप्युलेट करने के लिए बाहरी डेटा स्वचालित रूप से फ़ेच करता है। |
| `floating_hint` | text, integer, decimal | संकेत टेक्स्ट को इनपुट फील्ड के ऊपर फ्लोटिंग लेबल के रूप में दिखाता है। |
| `calculate-button` | calculate | एक दृश्यमान बटन जोड़ता है जो मांग पर फील्ड की पुनर्गणना ट्रिगर करता है। |

### लेआउट

| Appearance Attribute | प्रश्न प्रकार | विवरण |
|----------------------|----------------|-------------|
| `1screen` | group | समूह के आकार की परवाह किए बिना पूरे समूह को एक स्क्रीन पर प्रदर्शित करने के लिए बाध्य करता है। |
| `columns(n)` | select_one, select_multiple | विकल्पों को `n` कॉलम में प्रदर्शित करता है। |
| `gridformat<row=R col=C colspan=S align=center>` | कोई भी | फील्ड को CSS-grid लेआउट में row `R`, column `C` पर, `S` कॉलम तक फैलाकर रखता है। |
| `ignore-simplify` | कोई भी | फ़ॉर्म रेंडरर को इस फील्ड के लेआउट के स्वचालित सरलीकरण या संक्षिप्त करने को छोड़ने का निर्देश देता है। |

### Widgets

| Appearance Attribute | प्रश्न प्रकार | विवरण |
|----------------------|----------------|-------------|
| `likert` | select_one | विकल्पों को Likert पैमाने पंक्ति के रूप में प्रस्तुत करता है। |
| `distress` | select_one | विकल्पों को भावनात्मक आइकन के साथ Kessler Psychological Distress Scale (K10) विज़ुअल विजेट के रूप में रेंडर करता है। |

### API एकीकरण

| Appearance Attribute | प्रश्न प्रकार | विवरण |
|----------------------|----------------|-------------|
| `callapi` | text, integer, decimal, select_one | इस फील्ड के लिए API कॉल एकीकरण सक्षम करता है। calculation कॉलम में `callapi()` अभिव्यक्ति होनी चाहिए। |
| `callapi-verify(params)` | text, integer, decimal | स्थिर parameters का उपयोग करके API सत्यापन कॉल ट्रिगर करता है। |
| `callapi-verify(dynamicParams)` | text, integer, decimal | `callapi-verify` के समान लेकिन रनटाइम पर अन्य फील्ड मूल्यों से प्राप्त parameters के साथ। |

### इनलाइन दिनांक/समय प्रारूप

`date`, `time` और `datetime` फील्ड के लिए, आप appearance से जुड़ी एक format string का उपयोग करके एक कस्टम प्रदर्शन प्रारूप निर्दिष्ट कर सकते हैं:

```
inline-[%d/%m/%Y]
inline-1line-[%d/%m/%Y %H:%M]
```

उदाहरण:

| type | name | label | appearance |
|------|------|-------|------------|
| datetime | event_time | कार्यक्रम दिनांक और समय | inline-[%d/%m/%Y %I:%M %p] |
| date | birth_date | जन्म तिथि | inline-[%d/%m/%Y] |

## ज्ञात सीमाएं

- जटिल appearances सभी प्लेटफ़ॉर्म पर समान रूप से रेंडर नहीं हो सकती हैं।
- कुछ उन्नत rtSurvey appearances ऑफलाइन मोड में समर्थित नहीं हो सकती हैं।

## Appearance समस्याओं का समाधान

1. **Appearance लागू नहीं**: appearance कॉलम में टाइपो की जांच करें।
2. **असंगत रेंडरिंग**: प्रश्न प्रकार और प्लेटफ़ॉर्म के साथ संगतता सत्यापित करें।
3. **प्रदर्शन समस्याएं**: जटिल appearances को सरल बनाने पर विचार करें।
