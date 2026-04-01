---
title: "प्रश्नों को दोहराना"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 260
---

Repeats rtSurvey में एक शक्तिशाली सुविधा है जो आपको एक ही survey के भीतर कई बार एक ही सेट की जानकारी एकत्र करने की अनुमति देती है। यह household surveys जैसे scenarios के लिए विशेष रूप से उपयोगी है, जहाँ आपको कई household members के बारे में डेटा एकत्र करना हो सकता है।

## Basic Repeat Structure

rtSurvey में repeat बनाने के लिए, `begin repeat` और `end repeat` construct का उपयोग करें:

```
| type         | name         | label                |
|--------------|--------------|----------------------|
| begin repeat | child_repeat |                      |
| text         | name         | बच्चे का नाम         |
| decimal      | birthweight  | बच्चे का जन्म वजन   |
| select_one male_female | sex | बच्चे का लिंग      |
| end repeat   |              |                      |
```

इस उदाहरण में, user form में नए repeats जोड़कर कई बच्चों के बारे में जानकारी एकत्र कर सकता है।

## Repeats को Label करना

जबकि `begin repeat` के लिए `label` कॉलम वैकल्पिक है, एक label जोड़ने से navigation बेहतर हो सकती है:

```
| type         | name         | label                |
|--------------|--------------|----------------------|
| begin repeat | child_repeat | बच्चे की जानकारी     |
| text         | name         | बच्चे का नाम         |
| decimal      | birthweight  | बच्चे का जन्म वजन   |
| select_one male_female | sex | बच्चे का लिंग      |
| end repeat   |              |                      |
```

rtSurvey प्रत्येक repeat instance के लिए "बच्चे की जानकारी" को शीर्षक के रूप में प्रदर्शित करेगा।

## Fixed Repeat Counts

repeats की एक निश्चित संख्या निर्दिष्ट करने के लिए, `repeat_count` कॉलम का उपयोग करें:

```
| type         | name         | label                | repeat_count |
|--------------|--------------|----------------------|--------------|
| begin repeat | child_repeat | बच्चे की जानकारी     | 3            |
| text         | name         | बच्चे का नाम         |              |
| decimal      | birthweight  | बच्चे का जन्म वजन   |              |
| end repeat   |              |                      |              |
```

यह ठीक 3 child repeats बनाएगा।

## Dynamic Repeat Counts

rtSurvey पिछले उत्तरों के आधार पर dynamic repeat counts का समर्थन करता है:

```
| type     | name           | label                          | repeat_count       |
|----------|----------------|--------------------------------|--------------------|
| integer  | num_hh_members | household members की संख्या?   |                    |
| begin repeat | hh_member  | Household Member               | ${num_hh_members}  |
| text     | name           | नाम                            |                    |
| integer  | age            | आयु                            |                    |
| end repeat |              |                                |                    |
```

## Conditional Repeats

आप repeats को conditionally प्रदर्शित करने के लिए `relevant` कॉलम का उपयोग कर सकते हैं:

```
| type              | name        | label                     | relevant           |
|-------------------|-------------|---------------------------|---------------------|
| select_one yes_no | has_child   | क्या यहाँ कोई बच्चे रहते हैं? |                     |
| begin repeat      | child_repeat| बच्चे की जानकारी           | ${has_child} = 'yes'|
| text              | name        | बच्चे का नाम              |                     |
| decimal           | birthweight | बच्चे का जन्म वजन         |                     |
| end repeat        |             |                           |                     |
```

## rtSurvey-Specific Features

### Repeat Summary

rtSurvey repeats का summary view प्रदान करता है। summary को customize करने के लिए, repeat के भीतर एक group का उपयोग करें:

```
| type         | name         | label                                    |
|--------------|--------------|------------------------------------------|
| begin repeat | person_repeat|                                          |
| begin group  | person       | ${first_name} ${last_name} - ${age}      |
| text         | first_name   | पहला नाम                                 |
| text         | last_name    | अंतिम नाम                                |
| integer      | age          | आयु                                      |
| end group    |              |                                          |
| end repeat   |              |                                          |
```

### Repeat Appearance Options

rtSurvey repeats के लिए additional appearance options प्रदान करता है:

- `appearance: field-list` - repeat के सभी प्रश्नों को एक screen पर प्रदर्शित करता है
- `appearance: table-list` - repeats को tabular format में प्रस्तुत करता है

```
| type         | name         | label            | appearance  |
|--------------|--------------|-------------------|-------------|
| begin repeat | child_repeat | बच्चे की जानकारी  | table-list  |
| text         | name         | नाम               |             |
| integer      | age          | आयु               |             |
| end repeat   |              |                   |             |
```

### Nested Repeats

rtSurvey जटिल data structures के लिए nested repeats का समर्थन करता है:

```
| type         | name           | label                |
|--------------|----------------|----------------------|
| begin repeat | household      | Household            |
| text         | hh_name        | Household का नाम     |
| begin repeat | hh_member      | Household Member     |
| text         | member_name    | Member का नाम        |
| integer      | member_age     | Member की आयु        |
| end repeat   |                |                      |
| end repeat   |                |                      |
```

## rtSurvey में Repeats के उपयोग के लिए Best Practices

1. data analysis को बेहतर बनाने के लिए repeats के लिए meaningful names और labels का उपयोग करें।
2. data entry errors को कम करने के लिए dynamic repeat counts का उपयोग करने पर विचार करें।
3. अपने form का पूरी तरह से परीक्षण करें, विशेषकर जटिल nested repeats का उपयोग करते समय।
4. गणनाकर्ताओं को repeats की लंबी lists में navigate करने में मदद करने के लिए summary सुविधा का उपयोग करें।
5. बड़ी संख्या में repeats के साथ सावधान रहें, क्योंकि वे form performance को प्रभावित कर सकते हैं।

## Zero Repeats को संभालना

rtSurvey में zero repeats को represent करने के लिए:

1. गणनाकर्ताओं को पहले repeat को हटाने के लिए प्रशिक्षित करें यदि आवश्यक न हो।
2. जब सटीक संख्या ज्ञात हो तो dynamic repeat counts का उपयोग करें।
3. repeats को conditionally प्रदर्शित करने के लिए `relevant` का उपयोग करें।

## Data Export से संबंधित बातें

rtSurvey से डेटा export करते समय, repeat data आमतौर पर flatten हो जाता है। प्रत्येक repeat instance exported data में एक अलग row बन जाता है, जिसमें parent form का डेटा प्रत्येक instance के लिए repeat होता है।

## Mobile App से संबंधित बातें

- rtSurvey mobile app में Repeats offline data collection का समर्थन करते हैं।
- बड़ी संख्या में repeats low-end devices पर app performance को प्रभावित कर सकते हैं।

rtSurvey में repeats का प्रभावी उपयोग करके, आप flexible और शक्तिशाली surveys बना सकते हैं जो जटिल, hierarchical data structures को capture करने में सक्षम हों, साथ ही गणनाकर्ताओं के लिए user-friendly interface बनाए रखें।
