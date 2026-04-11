# docs.rtsurvey.com — Form Configuration Files

These special CSV files are uploaded as family media alongside a form. The app reads them at
form load time to configure behavior and data sources. They are RTSurvey-specific — not part
of the XLSForm standard.

Two new pages are needed under `pages/survey-design/advanced-features/`.

---

## Page 1: `form-settings.mdx` — `formSetting.csv`

**Nav title:** Form Settings  
**URL:** `/survey-design/advanced-features/form-settings`

### What to cover

- **Purpose:** Per-form behavior overrides. Settings here take precedence over the global
  collect-setting configuration for this form only.
- **File format:** CSV with 5 columns — `type`, `name`, `value`, `disable`, `description`
  - `type`: `boolean` (`1`/`0`) or `text`
  - `disable`: `yes` = locked in app UI, `no` = user-editable
  - Only include rows you want to override — omitted settings inherit from collect config
- **How to include:** Upload as family media with exact filename `formSetting.csv`
- **How it loads:** App reads it at the start of every form entry session

### Full settings reference table

| name | type | default | disable | description |
|------|------|---------|---------|-------------|
| `change_language` | boolean | 1 | yes | Show language switcher in form |
| `save_mid` | boolean | 0 | yes | Allow save incomplete (mid-form exit) |
| `jump_to` | boolean | 0 | yes | Show table of contents / prompt list |
| `autosend_wifi` | boolean | 1 | yes | Auto-submit finalized instances over WiFi |
| `autosend_network` | boolean | 1 | no | Auto-submit finalized instances over any network |
| `hide_incomplete_button` | boolean | 0 | no | Hide "save incomplete and exit" on end-of-form screen |
| `show_welcome_screen` | boolean | 1 | no | Show welcome screen at form start |
| `show_final_screen` | boolean | 1 | no | Show final screen at form end |
| `show_required_asterisk` | boolean | 1 | no | Show red asterisk on required questions |
| `navigation` | text | `swipe_one` | no | Navigation mode: `swipe_one` or `swipe_two` |
| `buttons` | boolean | 1 | no | Show 2-button (prev/next) navigation |
| `navigation_swipe_up_down_left_right` | boolean | 1 | no | Show 4-button navigation |
| `font_size` | text | 21 | no | Font size in pt |
| `disable_screen_off` | boolean | 1 | yes | Prevent device screen from turning off during form entry |
| `disable_fullscreen` | boolean | 0 | yes | Disable fullscreen mode |
| `access_settings` | boolean | 0 | yes | Show settings access menu item |
| `validate_form` | boolean | 1 | yes | Validate form constraints on save-incomplete |
| `long_press_remove_answer` | boolean | 1 | no | Long-press to clear a field answer |
| `long_press_remove_repeat` | boolean | 0 | no | Long-press to delete a repeat instance |
| `change_fontsize` | boolean | 0 | no | Show font-size menu item |
| `disable_screen_navigation` | text | -1 | no | Disable nav buttons: `-1`=off, `0`=prev, `1`=next, `2`=both |
| `disable_swipe` | text | -1 | no | Disable swipe: `-1`=off, `0`=prev, `1`=next, `2`=both |

### Minimal example

```csv
type,name,value,disable,description
boolean,autosend_wifi,1,no,Auto send over WiFi
boolean,save_mid,0,yes,No mid-form save
text,font_size,18,no,Slightly smaller font
```

---

## Page 2: `data-settings.mdx` — `dataSetting.csv`

**Nav title:** Data Settings  
**URL:** `/survey-design/advanced-features/data-settings`

### What to cover

- **Purpose:** Configures remote databases the app downloads at form load time and stores as
  local SQLite files. Once downloaded they are queryable via `rawquery` — same as any bundled
  CSV database.
- **File format:** CSV with 7 columns — `filepath`, `service_url`, `option`, `frequency`,
  `primary_key`, `where`, `dynamic_part`
- **How to include:** Upload as family media with exact filename `dataSetting.csv`. The app
  converts it to `dataSetting.db` on the device and processes each row at form open.

### Column reference

| column | required | description |
|--------|----------|-------------|
| `filepath` | yes | Local path where the downloaded file is stored. Root = app internal folder. Must be unique. Supports `##key##` from form opening arguments — on failure, key is replaced with empty string. |
| `service_url` | yes | Direct download URL returning a SQLite `.db` or `.zip` file. Use `.` prefix for current server (`./api/download/...`). Does **not** support `##openArgs.key##` syntax. |
| `option` | yes | `overwrite` — replace local file with fresh download. (`append` is deprecated — do not use.) |
| `frequency` | yes | Seconds between re-downloads. App re-downloads when elapsed time exceeds this value. |
| `primary_key` | no | Primary key column. Only required for `append` mode (deprecated). |
| `where` | no | SQL-style filter appended to `service_url` as a `where` GET param. Supports `##key##` from openArgs and App API keys. Ignored entirely if key resolution fails. |
| `dynamic_part` | no | Additional GET params appended after `where`. Supports `##key##`. Overrides duplicate keys in `service_url`. Ignored if key resolution fails. |

### Downloaded file requirements

- Must be a SQLite `.db` file, or a `.zip` containing a `.db` + optional binary attachments
- The SQLite file must have exactly **one table named `externalData`**
- Two system-reserved columns exist in every downloaded table:
  - `max_order` — update recency (higher = newer)
  - `marked_as_deleted` — soft-delete flag. Filter these out: `WHERE marked_as_deleted != 1`

### `##key##` substitution rules

| column | supports openArgs | supports App API | on failure |
|--------|------------------|-----------------|------------|
| `filepath` | yes | yes | replaced with empty string |
| `service_url` | **no** | yes | n/a |
| `where` | yes | yes | `where` param dropped entirely |
| `dynamic_part` | yes | yes | `dynamic_part` dropped entirely |

### `where` vs `dynamic_part`

- Both are appended to `service_url` as GET params
- `dynamic_part` is appended after `where`
- `dynamic_part` overrides duplicate keys (including from `service_url` and `where`)

### Example

```csv
filepath,service_url,option,frequency,primary_key,where,dynamic_part
resources/familyMedia/FORM_A/staff.db,./api/dm/getData?token=tk&dm_name=staff_list,overwrite,3600,id,`department`='##department##',
resources/familyMedia/FORM_A/facilities.db,./api/download/facilities,overwrite,86400,,,
```

- `staff.db` — downloads staff list filtered by the `department` argument passed when opening the form; refreshes hourly
- `facilities.db` — downloads full facility reference with no filter; refreshes daily

### Querying after download

After download, the file is a standard local SQLite database queryable with `rawquery`:

```
search-autocomplete-noedit-v2('rawquery',
  concat(${family_path}, '/staff.db::externalData'),
  '[name]', 'id',
  'SELECT name, id FROM externalData WHERE marked_as_deleted != 1')
```

See [Local Database Search](/survey-design/advanced-features/local-database-search) for the
full rawquery reference.

### When to use `dataSetting.csv` vs bundled CSV

| Situation | Use |
|-----------|-----|
| Data is static, finalized at form design time | Bundled CSV in family media |
| Data changes periodically (daily/weekly), offline access needed | `dataSetting.csv` |
| Data changes in real-time, online access acceptable | `search-api()` |
