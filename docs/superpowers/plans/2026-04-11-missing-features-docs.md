# Missing Features Documentation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Document all missing and incomplete RTSurvey features identified in `specs/missing-features.md` — covering 5 new pages, 5 expanded pages, 12 new appearance entries, and 1 new concept page.

**Architecture:** Pure MDX documentation. Each task writes or modifies one file. No code logic, no tests — verification is visual inspection via `npm run dev`. New pages require `_meta.json` updates to appear in the sidebar.

**Tech Stack:** Nextra (MDX), Next.js, existing page patterns from `pages/survey-design/`

---

## Source Verification Notes

Before writing: the spec was cross-checked against `/Volumes/ExDisk/rtLab/webapp/survey-dockerize` source code. Corrections and caveats:

| Feature | Spec claim | Source finding |
|---------|-----------|----------------|
| `search-autocomplete-noedit-v2('rawquery', ...)` | Documented in spec | **CONFIRMED** — `helpers.js:925 searchAutocompleteNoeditV2()`, `questionTypeHelper.js:100` |
| `pulldata('rawquery', path, sql, ?)` | Needs docs | **CONFIRMED** — param substitution in `StringHelperV2.php` |
| `audio-start` / `audio-end` | text field appearance | **NOT in webform source** — likely mobile app only. Document with caveat. |
| `autopull(concat(...))` | note field appearance | **CONFIRMED** — `miscellaneousHelpers.js:150` |
| `SaveFinalizedExit<#COLOR/>` | color syntax `<#RRGGBB/>` | **CONFIRMED** — `getColors()` in `helpers.js:2372` handles `<#XXXXXX/>` format |
| `SaveIncompleteExit` | same as SaveFinalizedExit | **CONFIRMED** — detected together at `stateHelpers.js:340`, separate component `SaveIncompleteExitButton.js` |
| `section` on `begin_group` | group appearance | **NOT FOUND** in `XMLFormParser.php` or webform JS — likely mobile-only. Document with caveat. |
| `rating_box-fill-{c1}-{c2}-{c3}-{c4}` | 4 colors | **CORRECTED** — `boxtagStyle.js` destructures 5 colors: `[borderWrap, uncheckedBorder, checkedBorder, uncheckedColor, checkedColor]`. Use 5-color format. |
| `tagging-choices-noshow-v2-{c1}-{c2}-{c3}-{c4}-{c5}` | 5 colors | **CONFIRMED** — `renderUtils.js:268`, `selectHelpers.js:140`, `boxtagStyle.js` |
| `toc-hide` | excludes from TOC | **CONFIRMED** — `TOCQuestion.js:13` |
| `change_language-{colors} default('lang')` | color + default param | **CONFIRMED** — `default(...)` parsed and rewritten to `rtDefault(...)` at `questionTypeHelper.js:121`; colors via `getColors()` |
| `scroll-view(N%)` | note field | **CONFIRMED** — `miscellaneousHelpers.js:157`, `ScrollView.js` |
| `minilog` | begin_repeat | **CONFIRMED** — `XMLFormParser.php:618` |
| `horizontal(N)` | N% width | **CONFIRMED** — `helpers.js:2251`, `styleUtils.js` |
| `STRFTIME` | SQLite function | **NOT in webform code** — is a SQLite built-in, works inside rawquery SQL but no explicit docs/tests found |

---

## File Map

**Create:**
- `pages/survey-design/advanced-features/local-database-search.mdx` — Task 1
- `pages/survey-design/advanced-features/audio-recording.mdx` — Task 3
- `pages/survey-design/advanced-features/form-navigation.mdx` — Task 5
- `pages/survey-design/advanced-features/family-path.mdx` — Task 10

**Modify:**
- `pages/survey-design/operators-and-functions/pulldata.mdx` — Tasks 2
- `pages/survey-design/advanced-features/html-styling.mdx` — Task 4
- `pages/survey-design/appearance.mdx` — Task 6
- `pages/survey-design/advanced-features/dynamic-search.mdx` — Task 7
- `pages/survey-design/multi-language.mdx` — Task 8
- `pages/survey-design/operators-and-functions/functions.mdx` — Task 9
- `pages/survey-design/advanced-features/_meta.json` — Tasks 1, 3, 5, 10

---

## Task 1: Local Database Search page

**Files:**
- Create: `pages/survey-design/advanced-features/local-database-search.mdx`
- Modify: `pages/survey-design/advanced-features/_meta.json`

- [ ] **Step 1: Create the MDX page**

```mdx
---
title: "Local Database Search"
description: "Use bundled SQLite databases with SQL queries to power autocomplete fields — ideal for offline-capable lookups of large reference datasets."
---

import { Callout } from 'nextra/components'

**Local Database Search** lets a `select_one` or `text` field autocomplete against a bundled SQLite `.db` file using a full SQL `SELECT` query. This is different from [Dynamic Search](dynamic-search) (which hits a remote REST API) and from the simple `search()` function (which does a plain file match). Use it when:

- The dataset is too large for a CSV choice list but must work offline.
- You need SQL filtering, ordering, or UNION to inject special options.
- You need multi-language display columns in the same database.

---

## Appearance variants

Three variants exist, each taking the same parameters:

| Variant | Notes |
|---------|-------|
| `search-autocomplete-noedit()` | Enumerator must select from results; free-text entry is rejected |
| `search-autocomplete-noedit-v2()` | Same behaviour, updated rendering (preferred for new forms) |
| `search()` | Allows free-text entry if nothing is selected |

All three use the `rawquery` data source type described below.

---

## `rawquery` data source

The first parameter `'rawquery'` tells rtSurvey to execute a SQL query against a bundled database file instead of doing a plain name match.

### Path convention: `.db::tableName`

```
concat(${family_path}, '/vnxa3.db::externalData')
```

The path is always constructed with `concat()` using `${family_path}` as the base directory. See [family_path](family-path) for details on how to set this up.

### Full signature

```
search-autocomplete-noedit-v2(
  'rawquery',
  path,          -- concat(${family_path}, '/file.db::table')
  '[displayCol]',-- column to show in the dropdown (bracket syntax)
  'valueCol',    -- column to store as the answer
  'SELECT ...'   -- SQL query; use ? for parameterized values
  [, param1, param2, ...]  -- values substituted for ? placeholders
)
```

---

## Basic example

Look up provinces from a bundled database:

| type | name | label | appearance |
|------|------|-------|------------|
| calculate | family_path | | `pulldata('app-api', 'family_path')` |
| select_one | tinh | Province | `search-autocomplete-noedit-v2('rawquery', concat(${family_path}, '/vnxa3.db::externalData'), '[provv]', 'provid', 'SELECT provv, provid FROM externalData WHERE rta_filter = "1"')` |

The dropdown shows the `provv` column (province name); `${tinh}` stores the `provid` value.

---

## Parameterized queries

Use `?` placeholders in the SQL and pass field references as extra arguments. Each `?` is replaced in order by the arguments that follow the SQL string.

Filter districts by a previously selected province:

| type | name | label | appearance |
|------|------|-------|------------|
| select_one | tinh | Province | `search-autocomplete-noedit-v2('rawquery', concat(${family_path}, '/vnxa3.db::externalData'), '[provv]', 'provid', 'SELECT provv, provid FROM externalData WHERE rta_filter = "1"')` |
| select_one | huyen | District | `search-autocomplete-noedit-v2('rawquery', concat(${family_path}, '/vnxa3.db::externalData'), '[distv]', 'distid', 'SELECT distv, distid FROM externalData WHERE provid = ? AND rta_filter = "1"', ${tinh})` |

The `?` in the district query is replaced by `${tinh}` at runtime.

---

## UNION SELECT to inject special values

Add "Don't Know" and "Refuse" options at the end of any lookup:

```
search-autocomplete-noedit-v2('rawquery',
  concat(${family_path}, '/vnxa3.db::externalData'),
  '[provv]', 'provid',
  'SELECT provv, provid FROM externalData WHERE rta_filter = "1"
   UNION SELECT "<i>Không biết</i>", "888"
   UNION SELECT "<i>Từ chối</i>", "999"')
```

The injected rows appear at the bottom of the results. HTML tags in the display column are rendered — use `<i>` for italics.

---

## Multi-language display

When the database has separate columns per language, use an `if()` expression to pick the right column:

```
search-autocomplete-noedit-v2('rawquery',
  concat(${family_path}, '/vnxa3.db::externalData'),
  '[label_vi]', 'provid',
  'SELECT label_vi, label_en, provid FROM externalData WHERE rta_filter = "1"')
```

Or switch dynamically based on a `${language_use}` field:

```
if(${language_use} = 'en',
  search-autocomplete-noedit-v2('rawquery', ..., '[label_en]', 'provid', 'SELECT ...'),
  search-autocomplete-noedit-v2('rawquery', ..., '[label_vi]', 'provid', 'SELECT ...'))
```

---

## Validating a real selection was made

The `selected-at(., 0) != -997` constraint checks that the enumerator actually picked a result rather than leaving the field with a system placeholder:

| type | name | constraint | constraint_message |
|------|------|------------|-------------------|
| select_one | tinh | `selected-at(., 0) != -997` | Please select a province from the list |

`-997` is the internal sentinel value rtSurvey stores when no choice has been made.

---

## Comparison: when to use each search type

| Approach | Connectivity | Data location | Use when |
|----------|-------------|---------------|----------|
| `search-autocomplete-noedit-v2('rawquery', ...)` | Offline | Bundled `.db` file | Large reference data, SQL filtering needed |
| `search-api(...)` | Online required | Remote REST API | Live or very large data, updated frequently |
| `search()` | Offline | Bundled `.db` file | Simple name match, free-text allowed |
| Choice list CSV | Offline | Attached CSV | Small, static choice lists |

---

## Limitations

- The `.db` file must be bundled with the form before deployment — it cannot be fetched at runtime.
- SQL is executed locally on the device; complex queries with many joins may be slow on low-end devices.
- Only `SELECT` queries are supported — no `INSERT`, `UPDATE`, or `DELETE`.
```

- [ ] **Step 2: Add entry to `_meta.json`**

Edit `pages/survey-design/advanced-features/_meta.json` to add `"local-database-search": "Local Database Search"` after `"grid-layout"`:

```json
{
  "index": "Overview",
  "call-api": "Call API",
  "dynamic-question-type": "Dynamic Question Type",
  "dynamic-search": "Dynamic Search",
  "grid-layout": "Grid Layout",
  "html-styling": "HTML Styling",
  "images": "Images",
  "local-database-search": "Local Database Search",
  "repeats": "Advanced Repeats"
}
```

- [ ] **Step 3: Commit**

```bash
git add pages/survey-design/advanced-features/local-database-search.mdx \
        pages/survey-design/advanced-features/_meta.json
git commit -m "docs(local-db-search): add local database search page"
```

---

## Task 2: pulldata rawquery — SQL parameterized variant

**Files:**
- Modify: `pages/survey-design/operators-and-functions/pulldata.mdx`

The existing `pulldata('rawquery', ...)` section documents a CSV WHERE-clause form. The spec requires documenting the SQL form that supports parameterized `?` queries against bundled `.db` files.

- [ ] **Step 1: Replace the existing `pulldata('rawquery', ...)` section**

Find the section starting with `### \`pulldata('rawquery', ...)\`` at the bottom of `pulldata.mdx` and replace it with:

```mdx
### `pulldata('rawquery', path, sql, param1, ...)`

Execute a SQL `SELECT` against a bundled SQLite `.db` file and return the value from the first matching row's first column. Parameters after the SQL string are substituted in order for `?` placeholders in the query.

```
pulldata('rawquery',
  concat(${family_path}, '/vnxa3.db::externalData'),
  'SELECT provv FROM externalData WHERE provid = ? AND rta_filter = "1"',
  ${tinh})
```

| Position | Parameter | Description |
|----------|-----------|-------------|
| 1 | `'rawquery'` | Selects the SQL database source |
| 2 | Path | `concat(${family_path}, '/file.db::table')` — database file and table name |
| 3 | SQL | A `SELECT` statement; use `?` for parameterized values |
| 4+ | Parameters | Values substituted for `?` in order; usually field references |

Returns the value of the first column of the first matching row, or empty string if no row matches.

**Multi-parameter example** — look up a ward name by province + district codes:

```
pulldata('rawquery',
  concat(${family_path}, '/vnxa3.db::externalData'),
  'SELECT wardname FROM externalData WHERE provid = ? AND distid = ?',
  ${tinh}, ${huyen})
```

**Difference from standard pulldata:** Standard `pulldata('file.csv', col, key, value)` does a simple column match on a CSV file. The `rawquery` variant executes full SQL against a SQLite database, enabling filtering, multi-column lookups, and parameterized queries.

See [Local Database Search](../advanced-features/local-database-search) for using rawquery in autocomplete appearance fields.
```

- [ ] **Step 2: Commit**

```bash
git add pages/survey-design/operators-and-functions/pulldata.mdx
git commit -m "docs(pulldata): expand rawquery section with SQL parameterized queries"
```

---

## Task 3: Audio recording page

**Files:**
- Create: `pages/survey-design/advanced-features/audio-recording.mdx`
- Modify: `pages/survey-design/advanced-features/_meta.json`

- [ ] **Step 1: Create the MDX page**

```mdx
---
title: "Audio Recording"
description: "Mark sections of a form for automatic audio recording using audio-start and audio-end appearance markers on text fields."
---

import { Callout } from 'nextra/components'

rtSurvey can record audio during a survey session. You mark the **start** and **end** of the recording window by placing special `text` fields with `audio-start` and `audio-end` appearances. All questions between those two fields are captured in the recording.

<Callout type="warning">
Audio recording is a **mobile app feature**. It is not available on the rtSurvey web form. Forms using `audio-start` / `audio-end` will silently ignore these appearances when opened in a browser.
</Callout>

---

## How it works

1. Place a `text` field with `appearance: audio-start` where recording should begin.
2. Place questions normally.
3. Place a `text` field with `appearance: audio-end` where recording should stop.

The enumerator sees a recording indicator while inside the recorded section. The audio file is attached to the submission.

---

## Basic example

| type | name | label | appearance |
|------|------|-------|------------|
| text | audio_s_a1 | | `audio-start` |
| integer | income | Monthly income | |
| select_one yn | has_loan | Does the household have a loan? | |
| text | audio_e_a1 | | `audio-end` |

The fields `income` and `has_loan` are recorded. The `audio_s_a1` and `audio_e_a1` fields themselves are not shown to the enumerator.

---

## Silent recording: `audio-start invisible`

Add `invisible` to hide the recording indicator from the enumerator entirely. The recording proceeds in the background without any visible indication:

| type | name | label | appearance |
|------|------|-------|------------|
| text | audio_s_a1 | | `audio-start invisible` |
| integer | income | Monthly income | |
| text | audio_e_a1 | | `audio-end invisible` |

Use `invisible` when the survey protocol requires passive recording without alerting the respondent (subject to applicable consent and ethics requirements).

---

## Naming convention

Use matching suffixes on start/end pairs to make the pairing clear:

| Field name | Appearance | Meaning |
|------------|------------|---------|
| `audio_s_a1` | `audio-start` | Start of section A, recording 1 |
| `audio_e_a1` | `audio-end` | End of section A, recording 1 |
| `audio_s_b1` | `audio-start` | Start of section B, recording 1 |
| `audio_e_b1` | `audio-end` | End of section B, recording 1 |

You can have multiple non-overlapping recording sections in a single form.

---

## Storage and retrieval

- Recordings are stored as `.m4a` or `.mp3` files attached to the submission.
- They appear in the submission detail view in the rtSurvey web portal.
- Files are named after the `audio-start` field name.
- Recordings are included in bulk exports alongside other submission data.

---

## Limitations

- Recording sections cannot be nested — do not place an `audio-start` inside another active recording section.
- Audio files increase submission size. On slow connections, upload may take longer.
- The `audio-start` / `audio-end` fields must be `text` type — using any other type is unsupported.
```

- [ ] **Step 2: Add entry to `_meta.json`**

```json
{
  "index": "Overview",
  "audio-recording": "Audio Recording",
  "call-api": "Call API",
  "dynamic-question-type": "Dynamic Question Type",
  "dynamic-search": "Dynamic Search",
  "grid-layout": "Grid Layout",
  "html-styling": "HTML Styling",
  "images": "Images",
  "local-database-search": "Local Database Search",
  "repeats": "Advanced Repeats"
}
```

- [ ] **Step 3: Commit**

```bash
git add pages/survey-design/advanced-features/audio-recording.mdx \
        pages/survey-design/advanced-features/_meta.json
git commit -m "docs(audio-recording): add audio-start/audio-end page"
```

---

## Task 4: autopull() HTML in html-styling.mdx

**Files:**
- Modify: `pages/survey-design/advanced-features/html-styling.mdx`

- [ ] **Step 1: Append the autopull() section before the Best Practices section**

Add the following MDX block immediately before the `## Best Practices` heading in `html-styling.mdx`:

```mdx
---

## Dynamic HTML summaries with `autopull()`

The `autopull()` appearance on a `note` field renders an HTML string that is re-evaluated every time any referenced field changes. This is the primary way to build **live summary tables** that update as the enumerator fills in the form.

### Syntax

```
appearance: autopull(concat('<html>...</html>'))
```

The argument to `autopull()` must be a `concat()` expression that produces a valid HTML string. Field references (`${field}`) inside the `concat()` are substituted with live values.

### Combined with `scroll-view(N%)`

Wrap the note in a scrollable container to prevent the table from pushing other questions off-screen:

```
scroll-view(45%) autopull(concat('<html>...'))
```

`N%` is the maximum height as a percentage of the screen. Content beyond that height scrolls vertically.

### Example — household summary table

| type | name | label | appearance |
|------|------|-------|------------|
| note | summary | | `scroll-view(45%) autopull(concat('<html><table style="width:100%;border-collapse:collapse"><tr style="background:#f0f0f0"><td style="padding:4px"><b>Province</b></td><td style="padding:4px">', ${tinh_name}, '</td></tr><tr><td style="padding:4px"><b>District</b></td><td style="padding:4px">', ${huyen_name}, '</td></tr><tr style="background:#f0f0f0"><td style="padding:4px"><b>Commune</b></td><td style="padding:4px">', ${xa_name}, '</td></tr></table></html>'))` |

As `${tinh_name}`, `${huyen_name}`, and `${xa_name}` are filled in earlier questions, the table updates in real time.

### Inline styles

Use `style=""` attributes directly on HTML elements. External stylesheets and `<style>` blocks are not supported:

```
<table style="width:100%;border-collapse:collapse">
<tr style="background:#e8f5e9">
  <td style="padding:6px;font-weight:bold">Label</td>
  <td style="padding:6px">' + ${value} + '</td>
</tr>
```

### When to use `autopull()`

- Review-before-submit screens showing a full data summary
- Running totals or computed values that should stay visible while filling other questions
- Formatted address blocks assembled from multiple fields

<Callout type="info">
`autopull()` only works on `note` fields. The `label` column is ignored — all HTML comes from the `appearance` column via `concat()`.
</Callout>
```

- [ ] **Step 2: Commit**

```bash
git add pages/survey-design/advanced-features/html-styling.mdx
git commit -m "docs(html-styling): add autopull() dynamic HTML summary section"
```

---

## Task 5: Form navigation controls page

**Files:**
- Create: `pages/survey-design/advanced-features/form-navigation.mdx`
- Modify: `pages/survey-design/advanced-features/_meta.json`

- [ ] **Step 1: Create the MDX page**

```mdx
---
title: "Form Navigation Controls"
description: "Use SaveFinalizedExit and SaveIncompleteExit appearance values to add styled exit buttons that save the form with a finalized or incomplete status."
---

import { Callout } from 'nextra/components'

rtSurvey supports special appearance values that render a `note` field as a full-width styled **exit button**. When tapped, the button saves the form and exits with either a finalized or incomplete status.

---

## `SaveFinalizedExit<#COLOR/>`

Saves the submission as **finalized** and returns to the form list. A finalized submission is marked as complete and can be submitted to the server.

```
appearance: SaveFinalizedExit<#04B404/>
```

The color argument is a hex color code for the button background.

---

## `SaveIncompleteExit<#COLOR/>`

Saves the submission as **incomplete** (draft) and returns to the form list. Incomplete submissions can be reopened and continued later.

```
appearance: SaveIncompleteExit<#EDC602/>
```

---

## Color syntax

```
SaveFinalizedExit<#RRGGBB/>
```

- Must be a 6-digit hex color prefixed with `#`.
- The closing `/>` is required.
- Common choices: `#04B404` (green) for finalized, `#EDC602` (amber) for incomplete.

---

## Example — end-of-form buttons

Place both buttons at the end of the form, typically hidden from the table of contents:

| type | name | label | appearance |
|------|------|-------|------------|
| note | btn_finish | Submit survey | `SaveFinalizedExit<#04B404/> toc-hide` |
| note | btn_pause | Save and continue later | `SaveIncompleteExit<#EDC602/> toc-hide` |

<Callout type="info">
Add `toc-hide` to exclude these fields from the form's table of contents navigation. See [Appearance — toc-hide](../appearance#toc-hide).
</Callout>

---

## Placement convention

- Put exit buttons at the **very end** of the form or at the end of a major section.
- Always include both a finalized and an incomplete exit so the enumerator can choose.
- Use `relevant` to show a finalized exit only after required sections are complete.

### Example with conditional visibility

```
| type | name | label | appearance | relevant |
|------|------|-------|------------|----------|
| note | btn_finish | Submit | SaveFinalizedExit<#04B404/> toc-hide | ${section_a_done} = 'yes' and ${section_b_done} = 'yes' |
| note | btn_pause | Save draft | SaveIncompleteExit<#EDC602/> toc-hide | true() |
```

---

## Limitations

- These appearances only work on `note` (and `text`) type fields.
- The button label comes from the field's `label` column.
- Color must be a valid 6-digit hex value — shorthand (`#FFF`) is not supported.
```

- [ ] **Step 2: Add entry to `_meta.json`**

```json
{
  "index": "Overview",
  "audio-recording": "Audio Recording",
  "call-api": "Call API",
  "dynamic-question-type": "Dynamic Question Type",
  "dynamic-search": "Dynamic Search",
  "form-navigation": "Form Navigation Controls",
  "grid-layout": "Grid Layout",
  "html-styling": "HTML Styling",
  "images": "Images",
  "local-database-search": "Local Database Search",
  "repeats": "Advanced Repeats"
}
```

- [ ] **Step 3: Commit**

```bash
git add pages/survey-design/advanced-features/form-navigation.mdx \
        pages/survey-design/advanced-features/_meta.json
git commit -m "docs(form-navigation): add SaveFinalizedExit / SaveIncompleteExit page"
```

---

## Task 6: appearance.mdx — add 12 missing RTSurvey appearances

**Files:**
- Modify: `pages/survey-design/appearance.mdx`

Add a new section `### Group and navigation` and expand the existing RTSurvey Extended section. The section `invisible` and `displaytitle` already exist — do not duplicate them.

- [ ] **Step 1: Add a new RTSurvey section for group and navigation appearances**

Append the following block before the `## Known Limitations` heading in `appearance.mdx`:

```mdx
### Group and navigation

| Appearance | Question Types | Description |
|------------|----------------|-------------|
| `section` | `begin_group` | Renders the group as a top-level section container with a section header/divider. Unlike `field-list`, questions are NOT shown on one screen — navigation proceeds question by question within the section. Typically used for top-level parts (`part_a`, `frontpage`). **Note: this appearance is not handled in the web form parser — it is a mobile app behavior.** |
| `toc-hide` | any | Excludes this field or group from the form's table of contents navigation panel. Use on exit buttons, hidden calculate fields, and any field the enumerator should not jump to directly. |
| `minilog` | `begin_repeat` | Renders the repeat group as a compact event-log list view instead of the default card layout. Each repeat instance appears as a single summary row. |

### Input behaviour

| Appearance | Question Types | Description |
|------------|----------------|-------------|
| `proper` | `text` | Auto-capitalizes the first letter of each word as the enumerator types (proper case). Use for name fields. |
| `text-nolabel` | `text`, `integer`, `decimal` | Renders the input widget without displaying the field label. Use when the label is provided by an adjacent `note` or HTML element. |
| `inline-1line` | `text` | Single-line inline display. The input appears on the same line as the label, constrained to one line of height. |
| `popup` | `note` | Renders the field content as a popup/modal overlay triggered by a button. Use for supplementary help text or reference tables that would otherwise crowd the form. |

### Layout

| Appearance | Question Types | Description |
|------------|----------------|-------------|
| `horizontal(N)` | `select_one`, `select_multiple` | Displays choices in a horizontal row, each choice taking `N%` of the row width. Example: `horizontal(50)` for two side-by-side choices. Differs from `horizontal` (standard, no width control) and `columns(n)` (n-column grid). |
| `scroll-view(N%)` | `note` | Wraps the field content in a scrollable container with a maximum height of `N%` of the screen. Use with `autopull()` for HTML tables that might exceed the viewport. Example: `scroll-view(45%)`. |

### Rating and tagging widgets

| Appearance | Question Types | Description |
|------------|----------------|-------------|
| `rating_box-fill-{borderWrap}-{uncheckedBorder}-{checkedBorder}-{uncheckedColor}-{checkedColor}` | `select_one` | Renders choices as colored rating boxes (Likert scale). Takes **5 hyphen-separated 6-digit hex codes** (no `#` prefix): container border, unselected border, selected border (also used as fill background with `-fill`), unselected text color, selected text color. Example: `rating_box-fill-cccccc-cccccc-04B404-333333-ffffff`. |
| `tagging-choices-noshow-v2-{c1}-{c2}-{c3}-{c4}-{c5}` | `select_multiple` | Renders choices as interactive colored tags. Takes **5 hyphen-separated 6-digit hex codes** matching the same positions as `rating_box` above. Example: `tagging-choices-noshow-v2-cccccc-cccccc-3498db-333333-ffffff`. |

### Language switcher

| Appearance | Question Types | Description |
|------------|----------------|-------------|
| `change_language-{colors} default('lang')` | `text`, `calculate` | Renders a language-switcher control. The `{colors}` segment customizes button appearance; `default('lang')` sets the initial language (e.g., `default('vi')`). Example: `change_language-3498db-ffffff default('vi')`. Typically placed near the top of the form on an `invisible` field. |
```

- [ ] **Step 2: Commit**

```bash
git add pages/survey-design/appearance.mdx
git commit -m "docs(appearance): add 12 missing RTSurvey appearance attributes"
```

---

## Task 7: dynamic-search.mdx — add local search() function

**Files:**
- Modify: `pages/survey-design/advanced-features/dynamic-search.mdx`

- [ ] **Step 1: Append the local search() section before the Best Practices section**

Add the following block immediately before `## Best Practices` in `dynamic-search.mdx`:

```mdx
---

## Local file search with `search()`

The `search()` function is the offline counterpart to `search-api()`. It matches choices from a bundled SQLite `.db` file without any network request.

```
search(path, 'matches', 'list_name', ${field})
```

| Parameter | Description |
|-----------|-------------|
| `path` | `concat(${family_path}, '/file.db::table')` — database file and table |
| `'matches'` | Match operator — `'matches'` filters rows where the column equals the value |
| `'list_name'` | The column in the table to match against |
| `${field}` | The value to match — usually a field reference |

### Example

Populate a `select_one` with choices from a local database that match the current value of `${d307}`:

| type | name | label | appearance |
|------|------|-------|------------|
| calculate | family_path | | `pulldata('app-api', 'family_path')` |
| select_one | d307_detail | Select item | `search(concat(${family_path}, '/d307.db::externalData'), 'matches', 'list_name', ${d307})` |

### Comparison: `search()` vs `search-autocomplete-noedit-v2('rawquery', ...)`

| Feature | `search()` | `rawquery` autocomplete |
|---------|-----------|------------------------|
| SQL queries | No — column equality only | Yes — full SELECT |
| Parameterized | No | Yes (`?` placeholders) |
| Free-text entry | Yes (allows typed input) | No (`noedit` blocks it) |
| UNION inject | No | Yes |
| Use when | Simple match, free text OK | SQL filtering needed, must select |
```

- [ ] **Step 2: Commit**

```bash
git add pages/survey-design/advanced-features/dynamic-search.mdx
git commit -m "docs(dynamic-search): add local search() function section"
```

---

## Task 8: multi-language.mdx — add missing sections

**Files:**
- Modify: `pages/survey-design/multi-language.mdx`

The page already has `constraint_message::lang`. Add: `required_message::lang`, HTML in bilingual labels, and language-aware calculation pattern.

- [ ] **Step 1: Add required_message column documentation**

Find the existing `constraint_message` example table (around "Language-Specific Validation Messages") and add `required_message` immediately after it:

```mdx
### Localized required messages

Use `required_message::Language (code)` to show a translated message when a required field is left blank:

```
| type | name | required | required_message::English (en) | required_message::Tiếng Việt (vi) |
|------|------|----------|-------------------------------|----------------------------------|
| text | name | yes      | This field is required        | Trường này là bắt buộc           |
```
```

- [ ] **Step 2: Add HTML formatting in bilingual labels section**

Append before `## Best Practices for Multi-Language Surveys`:

```mdx
---

## HTML formatting in bilingual labels

You can combine HTML tags with language wrappers in a single label cell. rtSurvey strips the non-active language block and renders the remaining HTML:

```
<en><big><b>Section 2: Household Income</b></big><br>Ask the household head only.</en><vi><big><b>Phần 2: Thu nhập hộ gia đình</b></big><br>Chỉ hỏi chủ hộ.</vi>
```

Supported inline tags inside language wrappers: `<b>`, `<i>`, `<u>`, `<big>`, `<small>`, `<font color="...">`, `<br>`, `<span style="...">`.

### Colored text per language

```
<en><font color="#CC0000">Warning: verify this value carefully.</font></en><vi><font color="#CC0000">Cảnh báo: kiểm tra kỹ giá trị này.</font></vi>
```

---

## Language-aware calculations

When a form stores the active language in a `${language_use}` field, use `if()` to return values in the correct language from a database column:

```
if(${language_use} = 'en', label_en, label_vi)
```

### Example — display a lookup result in the active language

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | tinh_name | | `if(${language_use} = 'en', pulldata('rawquery', concat(${family_path}, '/vnxa3.db::externalData'), 'SELECT label_en FROM externalData WHERE provid = ?', ${tinh}), pulldata('rawquery', concat(${family_path}, '/vnxa3.db::externalData'), 'SELECT label_vi FROM externalData WHERE provid = ?', ${tinh}))` |

The `language_use` field is typically set by a `change_language` appearance widget near the top of the form. See [Appearance — change_language](appearance#language-switcher).
```

- [ ] **Step 3: Commit**

```bash
git add pages/survey-design/multi-language.mdx
git commit -m "docs(multi-language): add required_message, HTML labels, language-aware calcs"
```

---

## Task 9: functions.mdx — add STRFTIME and cascade pattern

**Files:**
- Modify: `pages/survey-design/operators-and-functions/functions.mdx`

`selected-at()` and `format-date-time()` are already documented. Add `STRFTIME` and the `string-length()` cascade dependency pattern.

- [ ] **Step 1: Append STRFTIME under the Date and time functions section**

Find the `format-date-time` entry (item 7 in the date section) and add after it:

```mdx
8. `STRFTIME(format, datetime)`: SQLite-style date formatting. Available in `rawquery` SQL expressions and `pulldata('rawquery', ...)` queries. Uses SQLite format tokens (`%Y`, `%m`, `%d`, `%H`, `%M`, `%S`).
   - Example inside SQL: `SELECT STRFTIME('%Y-%m', interview_date) AS month FROM data WHERE id = ?`
   - Note: Use `format-date-time()` for formatting in XLSForm `calculation` and `label` columns. `STRFTIME()` is only available inside SQL strings passed to `rawquery`.
```

- [ ] **Step 2: Append string-length cascade pattern under String functions**

Add after the existing `string-length(field)` entry (item 2):

```mdx
   - **Cascade dependency pattern**: `string-length(${province}) >= 0` always evaluates to `true` but forces rtSurvey to re-evaluate the expression whenever `${province}` changes. Use this in `relevant` or `calculation` fields to trigger a cascade refresh when a parent field updates:

     | type | name | relevant |
     |------|------|----------|
     | select_one | district | `string-length(${province}) >= 0` |

     This ensures the district question re-evaluates its `search()` or `rawquery` appearance whenever the province selection changes, even if the district's own `relevant` condition would otherwise remain unchanged.
```

- [ ] **Step 3: Commit**

```bash
git add pages/survey-design/operators-and-functions/functions.mdx
git commit -m "docs(functions): add STRFTIME and string-length cascade dependency pattern"
```

---

## Task 10: family_path concept page

**Files:**
- Create: `pages/survey-design/advanced-features/family-path.mdx`
- Modify: `pages/survey-design/advanced-features/_meta.json`

- [ ] **Step 1: Create the MDX page**

```mdx
---
title: "family_path"
description: "The family_path calculate field provides the base directory path for local database files bundled with the form — required by all rawquery and search() lookups."
---

import { Callout } from 'nextra/components'

Every form that uses local database lookups (`rawquery`, `search()`) needs a `family_path` calculate field. It holds the base directory path where the form's bundled `.db` files are stored on the device. Without it, database paths cannot be constructed and all lookups will fail.

---

## What it is

`family_path` is a `calculate` field placed near the top of the form (after meta fields, before the first question). Its calculation reads the base path from the app runtime:

| type | name | calculation |
|------|------|-------------|
| calculate | family_path | `pulldata('app-api', 'family_path')` |

The value returned is a platform-specific absolute path such as:

```
/data/user/0/com.rtsurvey.app/files/forms/PAPI_2023_G7/
```

---

## Why it is needed

`.db` files are bundled alongside the form and stored in the form's own directory on the device. The exact path differs by device, OS version, and app installation. `family_path` abstracts this — you always reference files relative to it, and the app fills in the real path at runtime.

---

## How to use it in database paths

Always construct database paths by concatenating `family_path` with the relative filename and table name using `::`:

```
concat(${family_path}, '/vnxa3.db::externalData')
```

This pattern is used in:
- [`search-autocomplete-noedit-v2('rawquery', ...)`](local-database-search) — autocomplete appearance
- [`pulldata('rawquery', ...)`](../operators-and-functions/pulldata#pulldata-rawquery-path-sql-param1-) — calculate field lookup
- [`search()`](dynamic-search#local-file-search-with-search) — local file match

---

## Placement in the form

Put `family_path` near the top of the survey sheet, after the `meta` group but before any question that uses a database lookup. A typical form header looks like:

| type | name | label | calculation | appearance |
|------|------|-------|-------------|------------|
| text | language_use | | | `change_language-3498db-ffffff default('vi') invisible` |
| calculate | family_path | | `pulldata('app-api', 'family_path')` | |
| begin_group | frontpage | | | `section` |
| ... | | | | |

<Callout type="warning">
If `family_path` is missing or placed after the first `rawquery` field, that field will receive an empty path and silently return no results. Always verify `family_path` is defined before the first database-dependent field.
</Callout>

---

## Multiple database files

A single `family_path` field serves all databases in the form. Reference different `.db` files by varying the filename:

```
concat(${family_path}, '/vnxa3.db::externalData')    -- province/district/commune
concat(${family_path}, '/d307.db::externalData')     -- question-specific lookup
concat(${family_path}, '/codes.db::codeTable')       -- code reference table
```

---

## Verification

To confirm `family_path` is resolving correctly during development, add a temporary `note` field:

| type | name | label |
|------|------|-------|
| note | debug_path | `Path: ${family_path}` |

Remove before deploying to production.
```

- [ ] **Step 2: Add entry to `_meta.json`**

```json
{
  "index": "Overview",
  "audio-recording": "Audio Recording",
  "call-api": "Call API",
  "dynamic-question-type": "Dynamic Question Type",
  "dynamic-search": "Dynamic Search",
  "family-path": "family_path",
  "form-navigation": "Form Navigation Controls",
  "grid-layout": "Grid Layout",
  "html-styling": "HTML Styling",
  "images": "Images",
  "local-database-search": "Local Database Search",
  "repeats": "Advanced Repeats"
}
```

- [ ] **Step 3: Commit**

```bash
git add pages/survey-design/advanced-features/family-path.mdx \
        pages/survey-design/advanced-features/_meta.json
git commit -m "docs(family-path): add family_path concept page"
```

---

---

## Task 11: Repeat improvements — 1screen, add_repeat widget, delete buttons

**Files:**
- Modify: `pages/survey-design/advanced-features/repeats.mdx`

The existing `advanced-features/repeats.mdx` has a footer note: "Use `field-list` appearance on the repeat group to show all fields on one screen per instance (mobile)." That's all. Missing:
- `1screen` appearance on `begin_repeat` (confirmed: `stateHelpers.js:482`, `RepeatContainer.js:84`)
- `add_repeat` appearance on a field inside the repeat (confirmed: `AddRepeatButton.js`, `renderUtils.js:121`)
- `delete-repeat-current` / `delete-repeat-last` appearances (confirmed: `DeleteRepeatButton.js`, `renderUtils.js:240`)
- How the three interact (if `add_repeat` exists inside, the default `1screen` button is suppressed)

Source-verified color format: `getColors(appearances)` — colorCode[0] = background, colorCode[1] = text. Use `<#RRGGBB/>` for one color or `RRGGBB-RRGGBB` for two.

- [ ] **Step 1: Add `1screen` appearance section to `repeats.mdx`**

Append the following block **before** the existing `## Best Practices` heading in `pages/survey-design/advanced-features/repeats.mdx`:

```mdx
---

## Showing all questions on one screen: `1screen`

By default each repeat instance shows its questions one at a time. Adding `appearance: 1screen` to the `begin_repeat` row shows **all questions for that instance on a single screen**:

| type | name | label | appearance |
|------|------|-------|------------|
| begin_repeat | household_members | Household member | `1screen` |
| text | member_name | Member name | |
| integer | member_age | Age | |
| end_repeat | | | |

When `1screen` is set and there is no `repeat_count` and no custom `add_repeat` button inside the group, rtSurvey renders a circular **+** button at the bottom of the repeat to add new instances.

**Comparison with `field-list`:**

| Appearance | Works on | Effect |
|-----------|---------|--------|
| `field-list` | `begin_group` or `begin_repeat` | Standard XLSForm — all questions on one screen |
| `1screen` | `begin_repeat` | RTSurvey extended — all questions on one screen, enables the default circular add button |

Both `field-list` and `1screen` achieve one-screen-per-instance rendering; `1screen` additionally integrates with the repeat add/delete button system.

---

## Custom add button: `add_repeat`

Place a `note` (or `text`) field **inside** the repeat group with `appearance: add_repeat` to render a full-width "Add" button. When this field exists, the default circular + button is hidden.

| type | name | label | appearance |
|------|------|-------|------------|
| begin_repeat | members | Member | `1screen` |
| text | member_name | Name | |
| integer | member_age | Age | |
| note | btn_add_member | + Add another member | `add_repeat` |
| end_repeat | | | |

The button label comes from the field's `label` column.

### Color customization

Use hex color codes in the appearance to customize button background and text:

```
add_repeat <#04B404/>           → green background, default text color
add_repeat 04B404-ffffff        → green background, white text
```

Color format: `<#RRGGBB/>` for background only, or `RRGGBB-RRGGBB` for background and text (no `#` prefix in the dash-separated form).

### Icon-only variant

Add `icon` to the appearance to render a circular icon button instead of the full-width button:

```
add_repeat icon
add_repeat icon <#04B404/>
```

### Where to place it

The `add_repeat` field should be the **last field** in the repeat group so it appears at the bottom of each instance.

---

## Custom delete buttons: `delete-repeat-current` / `delete-repeat-last`

A `note` field inside a repeat with `appearance: delete-repeat-current` renders a split-style delete button. When clicked, it deletes the **current** repeat instance. `delete-repeat-last` deletes the **last** instance instead.

| type | name | label | appearance |
|------|------|-------|------------|
| begin_repeat | members | Member | `1screen` |
| text | member_name | Name | |
| integer | member_age | Age | |
| note | btn_delete | Remove this member | `delete-repeat-current` |
| note | btn_add | + Add member | `add_repeat` |
| end_repeat | | | |

The rendered button shows a trash icon on the left and the field label on the right.

### Icon-only variant

Append `-icon` to get a circular trash icon button:

```
delete-repeat-current-icon
delete-repeat-current-icon <#e74c3c/>
```

### Color customization

Same format as `add_repeat`:

```
delete-repeat-current <#e74c3c/>         → red background, default text
delete-repeat-current e74c3c-ffffff      → red background, white text
```

### Typical full pattern

A repeat with custom add and delete controls and one-screen layout:

| type | name | label | appearance |
|------|------|-------|------------|
| begin_repeat | members | Member | `1screen` |
| text | member_name | Name | |
| integer | member_age | Age | |
| note | btn_del | Remove | `delete-repeat-current-icon <#e74c3c/>` |
| note | btn_add | + Add member | `add_repeat <#04B404/>` |
| end_repeat | | | |
```

- [ ] **Step 2: Update the Best Practices section tip about `field-list`**

Find the line in `repeats.mdx`:
```
5. Use `field-list` appearance on the repeat group to show all fields on one screen per instance (mobile).
```
Replace it with:
```
5. Use `1screen` appearance on `begin_repeat` to show all questions on one screen per instance. Add a `add_repeat` note field inside the group to give the enumerator a clearly labelled "Add" button.
```

- [ ] **Step 3: Commit**

```bash
git add pages/survey-design/advanced-features/repeats.mdx
git commit -m "docs(repeats): add 1screen, add_repeat widget, and delete button documentation"
```

---

## Spec coverage checklist

| Spec requirement | Task |
|-----------------|------|
| P1.1 `search-autocomplete-noedit` / `rawquery` page | Task 1 |
| P1.2 `pulldata('rawquery', sql, params)` | Task 2 |
| P1.3 `audio-start` / `audio-end` page | Task 3 |
| P1.4 `autopull()` HTML | Task 4 |
| P1.5 `SaveFinalizedExit` / `SaveIncompleteExit` | Task 5 |
| P2 `section` appearance (mobile-only caveat) | Task 6 |
| P2 `rating_box-fill-...` (corrected to 5 colors) | Task 6 |
| P2 `tagging-choices-noshow-v2-...` (5 colors confirmed) | Task 6 |
| P2 `toc-hide` | Task 6 |
| P2 `proper` | Task 6 |
| P2 `text-nolabel` | Task 6 |
| P2 `inline-1line` | Task 6 |
| P2 `horizontal(N)` | Task 6 |
| P2 `popup` | Task 6 |
| P2 `scroll-view(N%)` | Task 6 |
| P2 `minilog` | Task 6 |
| P2 `change_language-{colors} default('lang')` | Task 6 |
| P3.1 `search()` variant in dynamic-search.mdx | Task 7 |
| P3.3 `required_message::lang` | Task 8 |
| P3.3 HTML in bilingual labels | Task 8 |
| P3.3 Language-aware calculations | Task 8 |
| P3.5 `STRFTIME` | Task 9 |
| P3.5 `string-length()` cascade pattern | Task 9 |
| P4 `family_path` concept page | Task 10 |
| P2 `invisible` | already in appearance.mdx ✓ |
| P2 `displaytitle` | already in appearance.mdx ✓ |
| P3.2 `display{}` / `results{}` | already in appearance.mdx ✓ |
| P3.4 `pulldata('app-api', ...)` | already in pulldata.mdx ✓ |
| P3.5 `selected-at()` | already in functions.mdx ✓ |
| P3.5 `format-date-time()` | already in functions.mdx ✓ |
| P3.3 `constraint_message::lang` | already in multi-language.mdx ✓ |
| Repeat `1screen` + `add_repeat` + delete buttons | Task 11 |
