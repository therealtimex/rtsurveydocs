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

column `appearance` ក្នុង rtSurvey អនុញ្ញាតឱ្យអ្នក customize ការ បង្ហាញ ដោយ ភ្នែក និង behavior នៃ questions ក្នុង surveys ។ rtSurvey គាំទ្រ standard XLSForm appearance attributes ហើយ extend ពួក វា ជាមួយ options បន្ថែម ។

## Standard XLSForm Appearance Attributes

| Appearance Attribute | ប្រភេទ Questions | ការពិពណ៌នា |
|----------------------|----------------|-------------|
| multiline | text | បង្កើត multi-line text box |
| minimal | select_one, select_multiple | បង្ហាញ choices ក្នុង dropdown menu |
| quick | select_one | auto-advance ទៅ question បន្ទាប់ (mobile only) |
| no-calendar | date | Suppress calendar display (mobile only) |
| month-year | date | ជ្រើស month និង year តែ ប៉ុណ្ណោះ |
| year | date | ជ្រើស year តែ ប៉ុណ្ណោះ |
| horizontal | select_one, select_multiple | បង្ហាញ choices ដោយ ផ្ដេក (web only) |
| likert | select_one | បង្ហាញ choices ជា Likert scale |
| field-list | groups | បង្ហាញ group ទាំង មូល នៅ screen មួយ (mobile only) |
| signature | image | enable signature capture (mobile only) |
| draw | image | អនុញ្ញាត freehand drawing (mobile only) |

## rtSurvey Extended Appearance Attributes

### ការ control Data and Display

| Appearance Attribute | ប្រភេទ Questions | ការពិពណ៌នា |
|----------------------|----------------|-------------|
| `invisible` | any | លាក់ field ពីការ មើល |
| `autopull` | select_one, select_multiple | ទៅ fetch data ខាង ក្រៅ ដើម្បី populate choices |
| `floating_hint` | text, integer, decimal | បង្ហាញ hint text ជា floating label |
| `calculate-button` | calculate | បន្ថែម button ដែល trigger recalculation |

### Layout

| Appearance Attribute | ប្រភេទ Questions | ការពិពណ៌នា |
|----------------------|----------------|-------------|
| `columns(n)` | select_one, select_multiple | បង្ហាញ choices ក្នុង `n` columns |
| `gridformat<row=R col=C colspan=S>` | any | position field ក្នុង CSS-grid layout |
| `required-but-simplify` | any | Field ចាំបាច់ ប៉ុន្តែ layout របស់វានៅតែត្រូវបានធ្វើឱ្យសាមញ្ញដោយ renderer |
| `embed` | any | Render field ក្នុង embedded/inline display mode |
| `popup` | select_one, select_multiple | Render បញ្ជីជម្រើសក្នុង popup/modal overlay ជំនួស inline |
| `auto-hide-empty` | boxtag, select | លាក់ widget question ទាំងមូលនៅពេល choice list ទទេ |
| `text-nolabel` | select_one, select_multiple | លាក់ text label សម្រាប់ជម្រើសនីមួយៗ បង្ហាញតែ input control |

### Widgets

| Appearance Attribute | ប្រភេទ Questions | ការពិពណ៌នា |
|----------------------|----------------|-------------|
| `likert` | select_one | បង្ហាញ choices ជា Likert scale row |
| `distress` | select_one | Render choices ជា Kessler Psychological Distress Scale (K10) widget ជាមួយ emotional icons |

### Select visual widgets

Appearances ទាំងនេះ ផ្លាស់ប្តូរការ render ទាំងមូលនៃ select choice lists។

| Appearance Attribute | ប្រភេទ Questions | ការពិពណ៌នា |
|----------------------|----------------|-------------|
| `tagging` | select_one, select_multiple | ជម្រើសបង្ហាញជា pill-shaped clickable tag chips។ |
| `boxtag` | select_one, select_multiple | ជម្រើសបង្ហាញជា rectangular styled boxes ដែលអ្នកប្រើប្រាស់ចុច។ |
| `boxtag -search` | select_one, select_multiple | Layout Boxtag ជាមួយ live search/filter input នៅខាងលើប្រអប់។ |
| `duolingo-style1` | select_one, select_multiple | Layout card ធំ style Duolingo — ស័ក្តិសមសម្រាប់បញ្ជីខ្លីជាមួយ icons។ |
| `rating_box` | select_one, select_multiple | Grid នៃ numbered boxes ដែលអាចចុចបាន — ស័ក្តិសមសម្រាប់ scale ឬ NPS questions។ |
| `star_rating` | select_one | ជម្រើសបង្ហាញជាផ្កាយ; ចំនួនផ្កាយស្មើចំនួនជម្រើស។ |
| `choices-noshow` | select_one, select_multiple | បង្ហាញ 10 ជម្រើសដំបូងជាដំបូងជាមួយ "Show more" control។ |
| `noshow` | select_one, select_multiple | លាក់បញ្ជីជម្រើសទាំងស្រុង; តម្លៃត្រូវបានកំណត់ដោយ program តាមរយៈ `calculate` ឬ API។ |
| `checkall` | select_multiple | បន្ថែម "Select all" shortcut នៅខាងលើបញ្ជីជម្រើស។ |
| `max-items(N)` | select_one, select_multiple | Cap visible choice list ទៅ N items។ ឧទាហរណ៍: `max-items(5)`។ |

### Text visual widgets

| Appearance Attribute | ប្រភេទ Questions | ការពិពណ៌នា |
|----------------------|----------------|-------------|
| `richtext` | text | ជំនួស plain text box ជាមួយ rich text editor (bold, italic, lists, links)។ ផ្ទុក HTML។ |
| `typingtest` | text | Typing test widget — label text គឺជា passage; widget ថតការឆ្លើយតបដែលបានវាយ និងពេលវេលា។ |

### Media extensions

| Appearance Attribute | ប្រភេទ Questions | ការពិពណ៌នា |
|----------------------|----------------|-------------|
| `watermark("expression")` | image | Overlay text watermark លើ photos ដែលបានចាប់។ argument គឺជា XPath expression ដែលបានគណនានៅពេល capture។ ឧទាហរណ៍: `watermark("${id} ${today()}")`។ |
| `editable` | image | Enable annotation/drawing លើ photo ដែលបានចាប់មុនពេលរក្សាទុក។ |

### Inline display configuration

Modifiers `display{}` និង `results{}` អាចភ្ជាប់ទៅ `inline` appearances ដើម្បីគ្រប់គ្រង icon alignment និង result display។ ទាំងនេះប្រើជាមួយ `inline` time input extension លើ `text` fields និង media capture widgets។

#### `display{}` parameters

```
inline display{left}
inline display{right,small}
inline display{top,large,inline-icon}
```

| Parameter | Values | ការពិពណ៌នា |
|-----------|--------|-------------|
| Alignment | `left`, `right`, `top`, `bottom`, `center` | ទីតាំង icon ដែលទាក់ទងនឹង input field |
| Size | `small`, `medium`, `large` | ទំហំ icon (2.5 rem, 5 rem, 8 rem ហៅ respectivement) |
| Mode | `inline-icon` | Render trigger ជា icon តែប៉ុណ្ណោះ (គ្មាន button border) |
| Mode | `inline-button` | Render trigger ជា full button |

#### `results{}` parameters

```
inline results{right}
inline results{left,hide(seconds)}
```

| Parameter | Values | ការពិពណ៌នា |
|-----------|--------|-------------|
| Alignment | `left`, `right`, `top`, `bottom`, `center` | ទីតាំងនៃការបង្ហាញ result value |
| `hide(field)` | ឈ្មោះ sub-field ណាក៏បាន | លាក់ component ជាក់លាក់នៃ result (ឧ. `hide(seconds)`) |

### API Integration

| Appearance Attribute | ប្រភេទ Questions | ការពិពណ៌នា |
|----------------------|----------------|-------------|
| `callapi` | text, integer, decimal, select_one | enable API call integration |
| `callapi-verify(params)` | text, integer, decimal | trigger API verification call |

### Inline date/time format

```
inline-[%d/%m/%Y]
inline-1line-[%d/%m/%Y %H:%M]
```

ឧទាហរណ៍:

| type | name | label | appearance |
|------|------|-------|------------|
| datetime | event_time | Event date and time | inline-[%d/%m/%Y %I:%M %p] |
| date | birth_date | Date of birth | inline-[%d/%m/%Y] |

## Best Practices

1. **ភាព consistent**: ប្រើ appearance attributes ដោយ consistent ។
2. **Mobile vs. Web**: ពិ ចារ ណា ថា appearances នឹង render យ៉ាង ណា ។
3. **Performance**: ប្រ យ័ ត ្ ន ជាមួយ appearance attributes ។
4. **Testing**: តែ ង តែ test form ។
