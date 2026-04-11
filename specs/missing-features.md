# docs.rtsurvey.com — Missing & Incomplete Feature Documentation

Discovered by analyzing real production forms (PAPI 2023 G7, permanent_residence_v1).
Each item is either completely missing from the docs or insufficiently documented.

---

## Priority 1 — Missing pages (features used heavily, zero docs)

### 1. `search-autocomplete-noedit` / `rawquery` SQL lookup

**What it is:** Local SQLite database autocomplete — different from `search-api` (REST) and `search()` (simple file match). Allows full SQL SELECT queries against bundled `.db` files, with parameterized queries and UNION for injecting special values.

**Needs a new page under:** `pages/survey-design/advanced-features/local-database-search.mdx`

**Must cover:**
- Variants: `search-autocomplete-noedit()`, `search-autocomplete-noedit-v2()`, `search()`
- The `rawquery` data source type and how `.db::tableName` path works
- `family_path` convention — the standard `calculate` field every form needs to resolve database paths
- Parameterized queries: `WHERE field = ?` with trailing field references
- `UNION SELECT` for injecting special values (888 = Don't Know, 999 = Refuse)
- Multi-language display using `label_vi` / `label_en` columns
- How it differs from `search-api` (REST) — when to use each
- `selected-at(., 0) != -997` constraint pattern for validating a real selection was made

**Example from production:**
```
appearance: search-autocomplete-noedit-v2('rawquery',
  concat(${family_path}, '/vnxa3.db::externalData'),
  '[provv]', 'provid',
  'SELECT provv, provid FROM externalData WHERE rta_filter = "1"
   UNION SELECT "<i>Không biết</i>", "888"')
```

---

### 2. `pulldata('rawquery', ...)` with SQL

**What it is:** Extension of `pulldata()` that executes a SQL SELECT against a bundled database instead of a simple CSV/file lookup. Supports parameterized queries.

**Current state:** `pulldata.mdx` exists but only documents the simple `pulldata('file', 'column', 'key', value)` form. The `rawquery` variant is completely absent.

**Needs to be added to:** `pages/survey-design/operators-and-functions/pulldata.mdx`

**Must cover:**
- `pulldata('rawquery', path, sql, param1, param2, ...)` signature
- How parameters map to `?` placeholders in the SQL
- Difference from standard pulldata (SQL vs key-value lookup)
- Combining with `concat(${family_path}, '/file.db::table')` path construction

**Example from production:**
```
pulldata('rawquery',
  concat(${family_path}, '/vnxa3.db::externalData'),
  'SELECT provv FROM externalData WHERE provid = ? AND rta_filter = "1"',
  ${tinh})
```

---

### 3. `audio-start` / `audio-end` appearance markers

**What it is:** Marks the start and end of an audio recording session. Any questions between `audio-start` and `audio-end` fields are recorded. The `invisible` variant records silently without showing a recording indicator.

**Needs a new page under:** `pages/survey-design/advanced-features/audio-recording.mdx`
(or added to `pages/survey-design/question-types/audio.mdx`)

**Must cover:**
- `audio-start` and `audio-end` on `text` type fields
- `audio-start invisible` / `audio-end invisible` for silent recording
- The section of questions that gets recorded
- How recordings are stored and retrieved
- Naming convention for start/end field pairs

**Example from production:**
```
| type | name       | appearance    |
|------|------------|---------------|
| text | audio_s_a1 | audio-start   |
| ...questions being recorded...   |
| text | audio_e_a1 | audio-end     |
```

---

### 4. `autopull()` with HTML in appearance

**What it is:** Dynamically generates and displays HTML content in a note field, pulling values from other fields at runtime. Commonly used to show summary tables that update as the enumerator fills in data.

**Needs to be added to:** `pages/survey-design/advanced-features/html-styling.mdx`
(or a new page `pages/survey-design/advanced-features/autopull-html.mdx`)

**Must cover:**
- `autopull(concat('<html>...</html>'))` syntax in the appearance column
- Combining with `scroll-view(N%)` to constrain height
- Embedding `${field}` references inside the HTML string via `concat()`
- CSS styling within the HTML (inline styles, table formatting)
- When to use: summary screens, review-before-submit tables

**Example from production:**
```
appearance: scroll-view(45%) autopull(concat(
  '<html><table style="width:100%">
   <tr><td>Province:</td><td>', ${tinh_name}, '</td></tr>
   <tr><td>District:</td><td>', ${huyen_name}, '</td></tr>
   </table></html>'))
```

---

### 5. Form navigation controls: `SaveFinalizedExit` / `SaveIncompleteExit`

**What it is:** Special appearance values on `note` or `text` fields that render as styled exit buttons. Allow the enumerator to save and exit with a finalized or incomplete status.

**Needs a new page or section under:** `pages/survey-design/advanced-features/`

**Must cover:**
- `SaveFinalizedExit<#COLOR/>` — saves as finalized and exits
- `SaveIncompleteExit<#COLOR/>` — saves as draft/incomplete and exits
- Color customization syntax `<#RRGGBB/>`
- Combining with `toc-hide` to exclude from table of contents
- Placement convention (typically at form end)

**Example from production:**
```
| type | name        | appearance                            |
|------|-------------|---------------------------------------|
| note | btn_finish  | SaveFinalizedExit<#04B404/> toc-hide  |
| note | btn_pause   | SaveIncompleteExit<#EDC602/> toc-hide |
```

---

## Priority 2 — Appearance page gaps (`appearance.mdx` is incomplete)

The `pages/survey-design/appearance.mdx` page is missing the following RTSurvey-specific appearances. Each needs a documented entry with description and example.

| Appearance | Description | Example field |
|-----------|-------------|--------------|
| `section` | Top-level section container for `begin_group`. Shows a section header/divider, does NOT show questions on one screen (unlike `field-list`). | `frontpage`, `part_a` |
| `rating_box-fill-{bg}-{selected}-{unselected}-{text}` | Renders choices as a colored rating box (Likert scale). Colors are hex codes separated by `-`. | `d100`, `d201` |
| `tagging-choices-noshow-v2-{color1}-{color2}-{color3}-{color4}-{color5}` | Renders choices as colored interactive tags. Supports custom color theming via 5 hyphen-separated hex codes. | `d307` |
| `toc-hide` | Excludes the field/group from the form's table of contents navigation. | Exit buttons, hidden fields |
| `invisible` | Field is rendered but not visible to the enumerator. Used for background calculations that need to be on-screen. | `language_use`, `family_path` |
| `proper` | Auto-capitalizes text input (proper case). | Name fields |
| `text-nolabel` | Renders a text input without displaying its label. | Combined with other appearances |
| `inline-1line` | Single-line inline display variant. | Short text fields |
| `horizontal(N)` | Horizontal layout with N% width per choice. E.g. `horizontal(50)` for two choices side-by-side. | Two-column yes/no |
| `popup` | Renders field content as a popup/modal overlay. | Help notes, supplementary info |
| `scroll-view(N%)` | Wraps content in a scrollable container with N% of screen height. | Summary HTML tables |
| `minilog` | Marks a repeat group as an event log (compact list view). | Action log repeats |
| `displaytitle` | Renders the field label as a prominent title heading. | Section titles |
| `change_language-{colors} default('lang')` | Renders a language switcher control. Colors customize the button style. | `language_use` |

---

## Priority 3 — Expand existing pages

### `dynamic-search.mdx` — add `search()` variant
The page covers `search-api()` (REST) but not the local `search()` function for SQLite file matching:
```
search(concat(${family_path}, '/d307.db::externalData'), 'matches', 'list_name', ${field})
```

### `appearance.mdx` — document `display{}` and `results{}` modifiers more completely
Current docs mention `inline` but don't fully cover all modifier combinations:
- `display{left, large}`, `display{center, large, #COLOR}`
- `results{left}`, `results{hide(value)}`, `results{hide(capture), hide(filename)}`

### `multi-language.mdx` — add localized constraint/required messages
The page documents `label::lang` and `hint::lang` but is missing:
- `constraint_message::lang` — localized validation error messages
- `required_message::lang` — localized required field messages
- HTML formatting inside bilingual labels (`<big>`, `<font color>`, `<u>`, `<i>`)
- Language-aware calculations: `if(${language_use} = 'en', label_en, label_vi)` pattern

### `pulldata.mdx` — add `app-api` source
```
pulldata('app-api', 'user.username')
pulldata('app-api', 'user.name')
pulldata('app-api', 'appPlatform')
pulldata('app-api', 'appVersion')
```
Used to read device/user metadata at runtime. Currently undocumented.

### `functions.mdx` — add missing functions
- `selected-at(field, index)` — get the nth selected value from a multi-select
- `STRFTIME(format, datetime)` — SQLite-style date formatting
- `format-date-time(field, format)` — XLSForm date formatting with `%Y-%m-%d %H:%M:%S`
- `string-length(field)` usage in `relevant` for cascade dependency (e.g. `string-length(${province}) >= 0`)

---

## Priority 4 — New concept pages needed

### `family_path` convention
Every form that uses local database lookups needs a `family_path` calculate field. This is a standard RTSurvey pattern that has no documentation:
- What `family_path` is and why it's needed
- How the value is constructed
- How it's referenced in `rawquery` paths
- Where to put it in the form (typically near the top, after meta fields)
