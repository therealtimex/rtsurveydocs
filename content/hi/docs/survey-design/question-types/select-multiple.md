---
title: "Select_multiple"
description: "Select_multiple questions उत्तरदाताओं को predefined list से एक या अधिक विकल्प चुनने देते हैं।"
icon: "check_box"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 225
---

`select_multiple` question type एक list प्रदर्शित करता है जहाँ उत्तरदाता **एक या अधिक विकल्प** चुन सकता है। Default रूप से choices checkboxes के रूप में render होती हैं। Stored value सभी selected choice values की **space-separated list** है।

## Basic XLSForm Specification

**survey worksheet:**

| type | name | label |
|------|------|-------|
| select_multiple crops | crops_grown | Household किन crops को उगाता है? |

**choices worksheet:**

| list_name | name | label |
|-----------|------|-------|
| crops | maize | Maize |
| crops | beans | Beans |
| crops | rice | Rice |
| crops | vegetables | सब्जियाँ |
| crops | other | अन्य |

अधिक जानकारी के लिए [XLSForm specification](https://xlsform.org/en/#question-types) देखें।

## Stored data format

Exported column selected values की space-separated list contains करता है:

```
maize beans vegetables
```

Expressions में select_multiple values test करते समय `=` के बजाय `selected()` function का उपयोग करें (नीचे देखें)।

## उपयोग

Select_multiple questions का उपयोग इनके लिए किया जाता है:

1. Multiple applicable answers एकत्र करना (जैसे income के sources, उगाए गए crops, symptoms)
2. Checkbox-style agreement items (जैसे "Select all that apply")
3. Language या skill inventories
4. कोई भी प्रश्न जहाँ multiple answers एक साथ valid हों

## Appearance options

{{< table >}}
| Appearance | विवरण |
|------------|-------------|
| *(none)* | Default checkboxes, प्रति line एक |
| `minimal` | Dropdown multi-select widget |
| `compact` | Compact grid, columns screen width के अनुसार adjust होते हैं |
| `compact-N` | N columns पर forced Compact grid |
| `horizontal` | Horizontal row में arranged Choices (web) |
| `horizontal-compact` | Horizontal, compact spacing (web) |
| `label` | केवल labels दिखाता है, कोई checkboxes नहीं (`list-nolabel` के साथ उपयोग करें) |
| `list-nolabel` | केवल checkboxes दिखाता है, कोई labels नहीं (`label` के साथ उपयोग करें) |
| `columns(N)` | N columns में प्रदर्शित करें (rtSurvey extension) |
| `tagging` | Choices pill-shaped tag chips के रूप में render होती हैं |
| `boxtag` | Choices आयताकार styled boxes के रूप में render होती हैं |
| `boxtag -search` | बॉक्स के ऊपर search/filter input के साथ Boxtag layout |
| `duolingo-style1` | बड़ा card layout — छोटी choice lists के लिए सबसे अच्छा |
| `rating_box` | Grid-आधारित rating boxes |
| `choices-noshow` | शुरू में पहले 10 choices दिखाता है; बाकी को मांग पर दिखाता है |
| `checkall` | List के शीर्ष पर "Select all" विकल्प जोड़ता है |
| `max-items(N)` | Visible choices की संख्या को N तक सीमित करता है |
{{< /table >}}

### उदाहरण: 3-column compact layout

| type | name | label | appearance |
|------|------|-------|------------|
| select_multiple symptoms | symptoms | सभी observed symptoms चुनें | compact-3 |

## Expressions में `selected()` का उपयोग करना

क्योंकि stored value एक space-separated string है, आपको **`selected()` का उपयोग करना होगा** यह test करने के लिए कि कोई specific choice pick की गई थी। `=` का उपयोग करने से सही ढंग से काम नहीं होगा।

### `relevant` में

केवल तभी follow-up question दिखाएं जब "other" चुना गया हो:

| type | name | label | relevant |
|------|------|-------|----------|
| select_multiple crops | crops_grown | कौन से crops उगाए जाते हैं? | |
| text | crops_other | कृपया अन्य crops निर्दिष्ट करें | `selected(${crops_grown}, 'other')` |

### `constraint` में

कम से कम 2 choices की आवश्यकता करें:

| type | name | constraint | constraint_message |
|------|------|------------|-------------------|
| select_multiple issues | issues | `count-selected(.) >= 2` | कम से कम 2 issues चुनें |

अधिकतम 3 तक सीमित करें:

| type | name | constraint | constraint_message |
|------|------|------------|-------------------|
| select_multiple priorities | priorities | `count-selected(.) <= 3` | अधिकतम 3 priorities चुनें |

### `calculate` में — selected labels को join करना

पठनीय summary build करने के लिए `selected-at()`, `count-selected()`, और `choice-label()` को combine करें:

| type | name | calculation |
|------|------|-------------|
| calculate | crops_summary | join(', ', ${crops_grown}) |

## "None of the above" / exclusive विकल्प

एक सामान्य pattern एक विकल्प को सभी अन्य विकल्पों के साथ mutually exclusive बनाना है। इसे enforce करने के लिए `constraint` का उपयोग करें:

| type | name | label | constraint | constraint_message |
|------|------|-------|------------|-------------------|
| select_multiple issues | issues | सभी present issues चुनें | `not(selected(., 'none') and count-selected(.) > 1)` | "None" को अन्य विकल्पों के साथ नहीं चुना जा सकता |

**choices:**

| list_name | name | label |
|-----------|------|-------|
| issues | water | पानी की कमी |
| issues | roads | खराब सड़कें |
| issues | health | स्वास्थ्य सेवाओं का अभाव |
| issues | none | इनमें से कोई नहीं |

## Selections की गिनती और summarising

| Function | Example | Result |
|----------|---------|--------|
| `count-selected(field)` | `count-selected(${crops_grown})` | चुनी गई choices की संख्या |
| `selected(field, value)` | `selected(${crops_grown}, 'maize')` | true/false |
| `selected-at(field, index)` | `selected-at(${crops_grown}, 0)` | पहली selected value |
| `choice-label(field, value)` | `choice-label(${crops_grown}, 'maize')` | एक value के लिए label |

## Best Practices

1. `relevant`, `constraint`, और `calculate` में हमेशा `selected()` का उपयोग करें — कभी `=` या `!=` का नहीं।
2. यदि question design की आवश्यकता हो तो selections की maximum संख्या सीमित करने के लिए constraint जोड़ें।
3. "None" या "Not applicable" विकल्प शामिल करें जब zero selections एक valid उत्तर हो।
4. लंबी lists (15+ choices) के लिए, अत्यधिक scrolling से बचने के लिए `minimal` (multi-select dropdown) का उपयोग करें।
5. Data export करें और अपने analysis tool में string-splitting का उपयोग करें।

## सीमाएं

- Select_multiple values को `=` से directly compare नहीं किया जा सकता। हमेशा `selected()` का उपयोग करें।
- Compact appearance बहुत लंबे choice labels के लिए अच्छी तरह render नहीं हो सकती।
- `choice_filter` के साथ choices filter करते समय, filtering सभी displayed choices पर apply होती है, वैसे ही जैसे `select_one` में।
