---
title: "Select_one"
description: "Select_one questions let respondents pick exactly one option from a predefined list of choices."
icon: "radio_button_checked"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 224
---

The `select_one` question type prompts the respondent to choose **exactly one option** from a predefined list. By default choices render as radio buttons, but a wide range of appearance options are available to change the layout and behavior.

## Basic XLSForm Specification

**survey worksheet:**

| type | name | label |
|------|------|-------|
| select_one yesno | consent | Did the respondent give consent? |

**choices worksheet:**

| list_name | name | label |
|-----------|------|-------|
| yesno | yes | Yes |
| yesno | no | No |

The `listname` in `select_one listname` must match the `list_name` column in the choices worksheet.

For more details see the [XLSForm specification](https://xlsform.org/en/#question-types).

## Uses

Select_one questions are used for:

1. Yes/No questions
2. Single-answer multiple choice (e.g., education level, gender, marital status)
3. Categorical ratings (e.g., poor / fair / good / excellent)
4. Cascading (linked) selects where choices filter based on a previous answer
5. Country, region, district, or other administrative unit selection

## Appearance options

Specify a value in the `appearance` column to change how choices are displayed:

{{< table >}}
| Appearance | Description |
|------------|-------------|
| *(none)* | Default radio buttons, one per line |
| `minimal` | Single dropdown/spinner instead of radio buttons |
| `quick` | Auto-advances to the next question immediately after selection (mobile only) |
| `compact` | Compact grid of choices — number of columns adjusts to screen width |
| `compact-N` | Compact grid forced to N columns (e.g., `compact-3`) |
| `quickcompact` | Combines `quick` and `compact` |
| `quickcompact-N` | Combines `quick` and `compact` with N forced columns |
| `horizontal` | Choices arranged in a horizontal row (web) |
| `horizontal-compact` | Horizontal, compact spacing (web) |
| `likert` | Likert scale row — labels above, radio buttons below |
| `label` | Shows only choice labels with no inputs (use paired with `list-nolabel`) |
| `list-nolabel` | Shows only the inputs with no labels (use paired with `label`) |
| `columns(N)` | Display in N columns (rtSurvey extension, e.g., `columns(3)`) |
| `distress` | Kessler Psychological Distress (K10) emotional icon widget |
| `search-api(...)` | Dynamic search — loads choices from an API at runtime |
| `tagging` | Displays choices as clickable tag chips instead of radio buttons |
| `boxtag` | Displays choices as styled rectangular boxes the user taps to select |
| `boxtag -search` | Boxtag layout with a search/filter input above the boxes |
| `duolingo-style1` | Duolingo-inspired card layout — large tappable cards with icons |
| `rating_box` | Grid-based rating boxes — best for numeric or scale choices |
| `star_rating` | Star rating widget — choices render as 1–N stars |
| `choices-noshow` | Shows only the first 10 choices initially; reveals the rest on demand |
| `noshow` | Hides the choice list entirely; value is set programmatically |
| `checkall` | Adds a "Select all" option at the top of the list |
| `max-items(N)` | Limits the number of visible choices to N (e.g., `max-items(5)`) |
{{< /table >}}

### Example: Likert scale

| type | name | label | appearance |
|------|------|-------|------------|
| select_one satisfaction | service_rating | How satisfied are you with the service? | likert |

### Example: Compact 3 columns

| type | name | label | appearance |
|------|------|-------|------------|
| select_one regions | region | Select region | compact-3 |

### rtSurvey visual widget appearances

#### tagging

Choices render as pill-shaped chips. Tapping a chip selects it; tapping again deselects.

| type | name | label | appearance |
|------|------|-------|------------|
| select_one colors | favourite_color | Pick your favourite color | tagging |

#### boxtag

Choices render as rectangular styled boxes. Use `-search` to add a filter input above the boxes.

| type | name | label | appearance |
|------|------|-------|------------|
| select_one products | product | Which product? | boxtag |
| select_one products | product_search | Which product? | boxtag -search |

#### duolingo-style1

Large card layout inspired by Duolingo. Best for short choice lists with icons or images.

| type | name | label | appearance |
|------|------|-------|------------|
| select_one quiz_options | answer | Choose the correct answer | duolingo-style1 |

#### star_rating

Choices render as stars. The number of stars equals the number of choices.

| type | name | label | appearance |
|------|------|-------|------------|
| select_one stars5 | satisfaction | Rate your satisfaction | star_rating |

**choices:**

| list_name | name | label |
|-----------|------|-------|
| stars5 | 1 | 1 |
| stars5 | 2 | 2 |
| stars5 | 3 | 3 |
| stars5 | 4 | 4 |
| stars5 | 5 | 5 |

#### rating_box

Numeric choices render as a grid of tappable boxes. Suited for scale questions (e.g., 0–10 NPS).

| type | name | label | appearance |
|------|------|-------|------------|
| select_one nps | nps_score | How likely are you to recommend us? (0–10) | rating_box |

#### choices-noshow / noshow / checkall / max-items(N)

| Appearance | Use when |
|------------|----------|
| `choices-noshow` | The list is long — show 10 items and a "Show more" control |
| `noshow` | The value will be set by a `calculate` or API, not by user selection |
| `checkall` | You want a "Select all" shortcut at the top of the list |
| `max-items(N)` | You want to cap the visible choices at exactly N items |

## Cascading selects

A cascading (linked) select filters choices based on the value selected in a previous question. Use the `choice_filter` column with the name of a column from your choices worksheet.

**survey:**

| type | name | label | choice_filter |
|------|------|-------|---------------|
| select_one province | province | Select province | |
| select_one district | district | Select district | province_name = ${province} |

**choices:**

| list_name | name | label | province_name |
|-----------|------|-------|---------------|
| province | nairobi | Nairobi | |
| province | mombasa | Mombasa | |
| district | westlands | Westlands | nairobi |
| district | kasarani | Kasarani | nairobi |
| district | nyali | Nyali | mombasa |
| district | likoni | Likoni | mombasa |

When the respondent selects `nairobi`, only `Westlands` and `Kasarani` appear in the district list.

{{% alert icon=" " context="warning" %}}
The column name used in `choice_filter` (e.g., `province_name`) must exist in the choices worksheet. The `${province}` references the survey field named `province`.
{{% /alert %}}

## Using the selected value in expressions

Reference the selected **value** (not label) with `${fieldname}`:

```
relevant: ${consent} = 'yes'
```

To get the choice label instead of value, use `choice-label()`:

```
calculate: choice-label(${education_level}, ${education_level})
```

## "Other" option with free text

A common pattern is to include an "other" option that reveals a text field:

| type | name | label | relevant |
|------|------|-------|----------|
| select_one occupation | job | What is your occupation? | |
| text | job_other | Please specify | `${job} = 'other'` |

**choices:**

| list_name | name | label |
|-----------|------|-------|
| occupation | farmer | Farmer |
| occupation | trader | Trader |
| occupation | student | Student |
| occupation | other | Other (please specify) |

## Best Practices

1. Keep lists short and mutually exclusive — if respondents might want more than one, use `select_multiple` instead.
2. Put the most common answer first, or order alphabetically for long lists.
3. Always include a "Don't know" or "Prefer not to answer" option where relevant.
4. Use `minimal` (dropdown) for lists with more than 7–8 choices on mobile to save screen space.
5. For cascading selects, add all filter columns in the choices worksheet before building the form.

## Limitations

- A respondent can select only one choice — use `select_multiple` for multi-answer questions.
- The `likert` appearance works best with 5–7 choices that fit on one line.
- `quick` auto-advance is mobile-only; it has no effect on web forms.
