---
title: "प्रश्नों को समूहित करना"
description: ""
icon: "auto_awesome"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 250
---

XLSForm में Groups आपको संबंधित प्रश्नों को एक साथ व्यवस्थित करने की अनुमति देते हैं, जिससे आपके survey की संरचना में सुधार होता है और data analysis क्षमताएं बढ़ती हैं। rtSurvey XLSForm groups का पूरी तरह से समर्थन करता है और उनकी functionality को additional features के साथ विस्तारित करता है।

## Basic Group Structure

प्रश्नों का एक group बनाने के लिए, `begin_group` और `end_group` syntax का उपयोग करें:

```
| type         | name       | label                                    |
|--------------|------------|------------------------------------------|
| begin_group  | respondent | उत्तरदाता की जानकारी                     |
| text         | name       | उत्तरदाता का नाम दर्ज करें              |
| text         | position   | उत्तरदाता का पद दर्ज करें               |
| end_group    |            |                                          |
```

मुख्य बातें:
- `begin_group` row को एक `name` और `label` की आवश्यकता है।
- `end_group` row को name या label की आवश्यकता नहीं है।
- `begin_group` और `end_group` के बीच के प्रश्न group का हिस्सा हैं।

## Group Appearance

rtSurvey groups के लिए विभिन्न appearance options का समर्थन करता है:

1. **field-list**: एक ही screen पर multiple प्रश्न प्रदर्शित करता है।
   ```
   | type         | name       | label     | appearance |
   |--------------|------------|-----------|------------|
   | begin_group  | respondent | उत्तरदाता | field-list |
   | text         | name       | नाम        |            |
   | text         | position   | पद         |            |
   | end_group    |            |           |            |
   ```

2. **grid**: groups के लिए एक compact, table-like layout बनाता है (rtSurvey-specific)।
   ```
   | type         | name       | label     | appearance |
   |--------------|------------|-----------|------------|
   | begin_group  | household  | Household | grid       |
   | text         | member_name| नाम       |            |
   | integer      | member_age | आयु       |            |
   | end_group    |            |           |            |
   ```

3. **collapsible**: expandable/collapsible groups बनाता है (rtSurvey-specific)।
   ```
   | type         | name       | label     | appearance  |
   |--------------|------------|-----------|-------------|
   | begin_group  | details    | विवरण     | collapsible |
   | text         | address    | पता       |             |
   | text         | phone      | फ़ोन      |             |
   | end_group    |            |           |             |
   ```

## Nested Groups

अधिक जटिल structures के लिए groups को अन्य groups के भीतर nested किया जा सकता है:

```
| type         | name       | label                                    |
|--------------|------------|------------------------------------------|
| begin_group  | hospital   | Hospital की जानकारी                      |
| text         | hosp_name  | इस hospital का नाम क्या है?              |
| begin_group  | medication | दवाओं की उपलब्धता                        |
| select_one y_n| hiv_meds  | क्या इस hospital में HIV दवाएं हैं?      |
| end_group    |            |                                          |
| end_group    |            |                                          |
```

**नोट**: उचित nesting बनाए रखने के लिए हमेशा सबसे हाल ही में शुरू किया गया group पहले समाप्त करें।

## Groups के लिए Skip Logic

पूरे groups के लिए skip logic लागू करने के लिए `relevant` कॉलम का उपयोग करें:

```
| type         | name   | label                                        | relevant        |
|--------------|--------|----------------------------------------------|-----------------|
| integer      | age    | आपकी आयु कितनी है?                          |                 |
| begin_group  | child  | बच्चा                                        | ${age} <= 5     |
| integer      | muac   | बच्चे की mid-upper arm circumference दर्ज करें |                |
| select_one y_n| mrdt  | क्या बच्चे का rapid diagnostic test positive है? |               |
| end_group    |        |                                              |                 |
```

इस उदाहरण में, `child` group केवल तभी दिखाई देगा जब उत्तरदाता की आयु 5 या उससे कम हो।

## Groups के उपयोग के लिए Best Practices

1. data analysis को बेहतर बनाने के लिए groups के लिए meaningful names का उपयोग करें।
2. groups को संबंधित प्रश्नों पर केंद्रित रखें।
3. अत्यधिक जटिल structures से बचने के लिए nested groups का विवेकपूर्वक उपयोग करें।
4. groups पर `relevant` का उपयोग करते समय skip logic का पूरी तरह से परीक्षण करें।
5. scrolling को कम करने के लिए short groups के लिए `field-list` appearance का उपयोग करने पर विचार करें।
6. संबंधित जानकारी के compact display के लिए rtSurvey के grid layout का उपयोग करें।
7. navigation को बेहतर बनाने के लिए long forms के लिए collapsible groups का उपयोग करें।

## rtSurvey-Specific Features

1. **Grid Layout**: table-like displays के लिए `grid` appearance का उपयोग करें।
2. **Collapsible Groups**: expandable sections के लिए `collapsible` appearance लागू करें।
3. **Custom Styling**: unique visual designs के लिए groups पर custom CSS लागू करें।
4. **Dynamic Group Behavior**: groups के भीतर जटिल skip logic और calculations लागू करें।

## Multilingual Support

rtSurvey multilingual groups का समर्थन करता है। labels के लिए language-specific columns का उपयोग करें:

```
| type         | name       | label::English | label::French |
|--------------|------------|----------------|---------------|
| begin_group  | personal   | Personal Info  | Infos Personnelles |
| text         | name       | Name           | Nom           |
| end_group    |            |                |               |
```

## Mobile App से संबंधित बातें

- `field-list` appearance वाले Groups mobile app में एक ही screen के रूप में प्रदर्शित होते हैं।
- Collapsible groups छोटी screens पर navigation को बेहतर बना सकते हैं।
- Grid layouts mobile devices पर बेहतर दृश्यता के लिए adjust हो सकते हैं।

## ज्ञात सीमाएं

- groups की अत्यधिक गहरी nesting कुछ devices पर performance को प्रभावित कर सकती है।
- कुछ advanced styling options mobile app में groups के लिए उपलब्ध नहीं हो सकते।

## Groups की समस्या निवारण

1. सुनिश्चित करें कि प्रत्येक `begin_group` के लिए एक corresponding `end_group` है।
2. जांचें कि group names form के भीतर unique हैं।
3. verify करें कि skip logic सही question names को संदर्भित करता है।
4. web और mobile interfaces दोनों पर groups का पूरी तरह से परीक्षण करें।

rtSurvey के साथ अपने XLSForms में groups का प्रभावी उपयोग करके, आप well-organized, कुशल surveys बना सकते हैं जो डेटा संग्रह अनुभव और आपके data analysis की गुणवत्ता दोनों में सुधार करते हैं।
