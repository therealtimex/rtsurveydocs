# docs.rtsurvey.com — Elasticsearch Integration

RTSurvey integrates Elasticsearch as a server-side data pipeline and search backend.
From a form designer's perspective, ES is accessed through existing XLSForm mechanisms —
`search-api()` for real-time queries, `rawquery` via `dataSetting.csv` for offline use.

One new page is needed under `pages/survey-design/advanced-features/`.

---

## Page: `elasticsearch.mdx`

**Nav title:** Elasticsearch  
**URL:** `/survey-design/advanced-features/elasticsearch`

### What to cover

---

### 1. What Elasticsearch is in RTSurvey

- ES is a server-side search and analytics engine managed by the platform admin
- Form designers do not configure ES directly — they consume ES data in forms via `search-api()`
  or `rawquery`
- Admins define **data collectors** that push form submission data into ES indices

---

### 2. Two ways to use ES data in a form

#### Mode 1 — Real-time search (online only)

Use `search-api()` pointing at the ES `_search` REST endpoint. Because ES exposes a standard
HTTP API, the 7-parameter `search-api()` call works without any platform-specific wrapper.

```
appearance: search-api('POST',
  'https://es.example.com/my_index/_search',
  '{"query":{"match":{"name":"%__input__%"}},"size":20}',
  '_id',
  '##_source.name## — ##_source.district##',
  '$.hits.hits',
  'es_result')
```

Key points:
- `data_path` should be `$.hits.hits` — each hit becomes one result item
- `value_column` should be `_id` or a field inside `_source`
- Display template uses `##_source.fieldname##` to access nested source fields
- After selection: `pulldata('es_result', '_source.district')` etc.

See [Dynamic Search](/survey-design/advanced-features/dynamic-search) for the full
`search-api()` parameter reference.

**When to use:** Data changes frequently (near real-time), device has reliable connectivity.

#### Mode 2 — Offline (downloaded database)

Use `dataSetting.csv` to download an ES data export as a SQLite file at form open time.
Once on device, query with `rawquery` exactly like any other local database.

`dataSetting.csv` entry:
```csv
filepath,service_url,option,frequency,primary_key,where,dynamic_part
resources/familyMedia/FORM/staff.db,./api/es/export?index=hr_staff,overwrite,3600,id,,
```

The server exports the ES index snapshot as a SQLite file with a single `externalData` table.
The app downloads it on form open (when stale by `frequency` seconds).

Then in the form:
```
search-autocomplete-noedit-v2('rawquery',
  concat(${family_path}, '/staff.db::externalData'),
  '[name]', 'id',
  'SELECT name, id FROM externalData WHERE marked_as_deleted != 1')
```

See [Data Settings](/survey-design/advanced-features/data-settings) for `dataSetting.csv`
and [Local Database Search](/survey-design/advanced-features/local-database-search) for
`rawquery`.

**When to use:** Data changes daily/weekly, offline access required.

---

### 3. Choosing the right approach

| Situation | Use |
|-----------|-----|
| Data changes every minute, device is always online | Real-time `search-api` → ES `_search` |
| Data changes daily/weekly, offline needed | `dataSetting.csv` download + `rawquery` |
| Data is static (geographic, ethnicity list) | Bundled CSV in family media |

---

### 4. Security — current state and limitations

**Current state:**
- The ES cluster uses HTTP Basic Auth managed by the platform admin
- Credentials are embedded server-side — they are never sent to devices
- When `search-api()` queries ES directly, the device sends the request to the ES endpoint
  with **no authentication header** — there is currently no mechanism to attach auth tokens
  to `search-api()` requests

**Implication for form designers:**
- Any ES endpoint used in `search-api()` must be either:
  - Publicly readable (no sensitive data), or
  - Proxied through the SmartSurvey server, which can inject auth headers before forwarding
- Do not expose sensitive personal data in an ES index queried directly via `search-api()`

**Recommended workaround (until server-side proxy is available):**
- Use offline mode (`dataSetting.csv` + `rawquery`) for sensitive data — the server handles
  the authenticated ES export; the device never talks to ES directly

---

### 5. Admin: data collector pipelines (brief reference)

For platform admins setting up ES data collection:
- Create a `SsDataCollector` with `index_name` pointing to the target ES index
- Script types: `php`, `python`, `R`, `sql`
- Configure retry: `task_retry_enabled`, `task_max_retry_count`, `task_retry_delay_minutes`
- Monitor tasks at `/api/esWorkingTask/list`
- Required permissions: `ElasticSearch.Collectors.*`, `ElasticSearch.Indices.*`
