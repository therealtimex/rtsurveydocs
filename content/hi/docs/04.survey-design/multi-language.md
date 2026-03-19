---
title: "बहु-भाषा समर्थन"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 285
---

rtSurvey मजबूत बहु-भाषा समर्थन प्रदान करता है, जो आपको कई भाषाओं में surveys बनाने की अनुमति देता है। यह सुविधा विविध भाषाई आबादी में या बहुभाषी वातावरण में शोध करने के लिए महत्वपूर्ण है।

## Multi-Language Surveys सेटअप करना

rtSurvey में multi-language survey बनाने के लिए, आपको अपने XLSForm में language-specific columns जोड़ने की आवश्यकता है। यहाँ बताया गया है:

1. **Label Translations**: प्रत्येक भाषा के लिए `label::Language (code)` format का उपयोग करके columns जोड़ें।
2. **Hint Translations**: hints का अनुवाद करने के लिए `hint::Language (code)` का उपयोग करें।
3. **Media File Translations**: language-specific media के लिए, `media::Language (code)` का उपयोग करें।

उदाहरण:

```
| type    | name | label::English (en) | label::Español (es) | hint::English (en) | hint::Español (es) |
|---------|------|---------------------|---------------------|---------------------|---------------------|
| integer | age  | How old are you?    | ¿Cuántos años tienes?| Enter your age      | Ingrese su edad     |
```

## Language Codes

भाषा के नाम के बाद आधिकारिक 2-character language codes (subtags) का उपयोग करने की सिफारिश की जाती है। यह form language को user interface language से match करना सुगम बनाता है। आप आधिकारिक codes [यहाँ](https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry) पा सकते हैं।

## Default Language सेट करना

data collection के लिए default language सेट करने के लिए, अपने XLSForm में `settings` worksheet का उपयोग करें:

```
| form_id   | version | default_language |
|-----------|---------|-------------------|
| test_form | 101     | French (fr)       |
```

## rtSurvey-Specific Features

### Dynamic Language Switching

rtSurvey users को data collection के दौरान dynamically भाषाएं बदलने की अनुमति देता है:

- web interface में, top navigation bar में language dropdown का उपयोग करें।
- mobile app में, settings menu के माध्यम से language options तक पहुँचें।

### Language-Specific Validation Messages

rtSurvey बहु-भाषा समर्थन को validation messages तक विस्तारित करता है:

```
| type    | name | constraint | constraint_message::English (en) | constraint_message::Español (es) |
|---------|------|------------|----------------------------------|----------------------------------|
| integer | age  | . <= 150   | Age must be 150 or less          | La edad debe ser 150 o menos     |
```

### RTL Language Support

Arabic या Hebrew जैसी right-to-left (RTL) भाषाओं के लिए, rtSurvey स्वचालित रूप से layout को adjust करता है:

```
| type | name | label::English (en) | label::Arabic (ar) |
|------|------|---------------------|---------------------|
| text | name | Your name           | اسمك                |
```

### Language-Specific Appearance

rtSurvey आपको विभिन्न भाषाओं के लिए अलग-अलग appearances निर्दिष्ट करने की अनुमति देता है:

```
| type | name | label::English (en) | label::Chinese (zh) | appearance::English (en) | appearance::Chinese (zh) |
|------|------|---------------------|---------------------|--------------------------|---------------------------|
| text | address | Address          | 地址                 | multiline                | textarea                  |
```

## Multi-Language Surveys के लिए Best Practices

1. **सुसंगत Naming**: अपने form में सुसंगत language codes का उपयोग करें।
2. **Professional Translation**: survey context से परिचित professional अनुवादकों को नियुक्त करें।
3. **Context Notes**: सटीक अनुवाद सुनिश्चित करने के लिए अनुवादकों के लिए context notes प्रदान करें।
4. **Testing**: deployment से पहले सभी भाषाओं में अपने form का परीक्षण करें।
5. **Unicode Support**: सुनिश्चित करें कि आपके data collection devices non-Latin scripts के लिए Unicode का समर्थन करते हैं।
6. **Language-Specific Media**: प्रत्येक भाषा के लिए सांस्कृतिक रूप से उचित images या audio का उपयोग करें।
7. **Images में Text से बचें**: यदि text के साथ images का उपयोग कर रहे हैं, तो प्रत्येक भाषा के लिए अलग images बनाएं।

## Special Cases को संभालना

### Mixed Language Responses

rtSurvey उत्तरदाताओं को selected form language की परवाह किए बिना किसी भी script में text input करने की अनुमति देता है। यह नामों या पतों को उनकी मूल script में capture करने के लिए उपयोगी है।

### Language-Specific Question Types

कुछ question types कुछ भाषाओं के लिए अधिक उपयुक्त हो सकते हैं। rtSurvey आपको विभिन्न भाषाओं के लिए अलग-अलग question types का उपयोग करने की अनुमति देता है:

```
| type::English (en) | type::Japanese (ja) | name | label::English (en) | label::Japanese (ja) |
|--------------------|---------------------|------|---------------------|----------------------|
| text               | select_one kanji    | name | Enter your name     | 名前を選んでください    |
```

## Multi-Language Data Export करना

rtSurvey से डेटा export करते समय:

- किसी specific भाषा में export करना चुनें या सभी language versions शामिल करें।
- Language metadata export में शामिल है, यह दर्शाते हुए कि प्रत्येक response के लिए किस भाषा का उपयोग किया गया था।

## Mobile App से संबंधित बातें

- rtSurvey mobile app offline language switching का समर्थन करता है।
- Offline जाने से पहले सभी आवश्यक language files download हों यह सुनिश्चित करें।

## ज्ञात सीमाएं

- कुछ advanced features सभी भाषाओं में उपलब्ध नहीं हो सकते।
- अत्यंत लंबे अनुवाद छोटी screens पर layout को प्रभावित कर सकते हैं।

rtSurvey की multi-language capabilities का लाभ उठाकर, आप inclusive, सुलभ surveys बना सकते हैं जो विविध आबादी तक पहुँचें और उच्च-गुणवत्ता, भाषाई रूप से सटीक डेटा प्रदान करें।
