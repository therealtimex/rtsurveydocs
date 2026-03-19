---
title: "HTML Styling"
description: "rtSurvey គាំទ្រ HTML tags ក្នុង labels និង hints, អនុញ្ញាតឱ្យ rich text formatting, links, និង dynamic color theming។"
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 297
---

rtSurvey render **label** និង **hint** text ជា HTML ។ នេះ មាន ន័យ ថា អ្នក អាច ប ្ រ ើ HTML tags ។

{{% alert icon=" " context="warning" %}}
HTML ក ្ ន ុ ង labels ត ្ រ ូ វ ប ា ន render ន ៅ ល ើ **web form** ហ ើ យ rtSurvey mobile apps ។ Test ន ៅ ល ើ target platform ។
{{% /alert %}}

---

## HTML tags ដែល គាំទ្រ

### Text formatting

| Tag | Result |
|-----|--------|
| `<strong>text</strong>` ឬ `<b>text</b>` | **Bold text** |
| `<em>text</em>` ឬ `<i>text</i>` | *Italic text* |
| `<u>text</u>` | Underlined text |
| `<br>` | Line break |
| `<span style="...">text</span>` | Inline styling |

### Links

```html
<a href="https://example.com" target="_blank">Click here</a>
```

### Colors

```html
<span style="color: red;">Warning: value is out of range</span>
<span style="color: #009688;">Section completed</span>
```

---

## Multi-language labels

```
<en>Enter the household size</en><vi>Nhập quy mô hộ gia đình</vi>
```

---

## Examples

### Section instruction

| type | name | label |
|------|------|-------|
| note | section_intro | `<strong>Section 3: Land Use</strong><br>Ask all questions in this section to the household head only.` |

### Warning ជ ា red

| type | name | label | relevant |
|------|------|-------|----------|
| note | age_warning | `<span style="color: red;"><strong>Warning:</strong> Age entered (${age}) is unusually high.</span>` | `${age} > 100` |

---

## Special rtSurvey HTML Tags

### `<webbox src='url' title='title'>...</webbox>`

Embed button ដ ែ ល បើ ក URL ក ្ ន ុ ង modal ។

### `<delete-repeat-current>label</delete-repeat-current>`

Render button ក ្ ន ុ ង repeat group ដ ែ ល delete current instance ។

---

## Best Practices

1. ប ្ រ ើ HTML ដ ោ យ ក ំ ណ ត ់ ។
2. ប ្ រ ើ `<strong>` bold ហ ើ យ `<em>` italic ។
3. Test HTML rendering ទ ា ំ ង ន ៅ mobile app ហ ើ យ web form ។

## Limitations

- Complex HTML ម ិ ន ត ្ រ ូ វ ប ា ន គ ា ំ ទ ្ រ ។
- `<a>` links បើ ក ក ្ ន ុ ង browser ។
