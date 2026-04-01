---
title: "Webbox"
description: "Webbox вгражда zewnętrzна уеб страница вътре в анкетата като модален iframe, позволявайки на анкетьорите да преглеждат справки или да взаимодействат с外部 инструменти без да напускат формуляра."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 299
---

**Webbox** embeds an external web page inside the survey as a **modal popup** (iframe). The enumerator taps a button in the label or note text, the page opens in a full-screen overlay within the form, and when they close it they return to exactly where they were. This lets you show reference material, maps, dashboards, or custom tools without opening a separate browser tab.

---

## Синтаксис

Insert a `<webbox>` HTML tag directly in a `label` or `note` label column:

```html
<webbox src='https://example.com/reference' title='Reference Guide'>Open Reference Guide</webbox>
```

| Attribute | Description |
|-----------|-------------|
| `src` | The URL to load in the iframe. Supports both single and double quotes. |
| `title` | Text displayed in the modal header bar. Supports plain text. |
| *(content)* | The clickable button label shown in the survey field |

---

## Основно example

| type | name | label |
|------|------|-------|
| note | ref_guide | `<webbox src='https://docs.example.com/field-guide' title='Field Guide'>📖 Open Field Guide</webbox>` |

This renders a button labelled "📖 Open Field Guide". When tapped, a modal opens displaying the field guide website.

---

## Embedding a map

| type | name | label |
|------|------|-------|
| note | area_map | `<webbox src='https://maps.example.com/survey-area' title='Survey Area Map'>🗺 View Map</webbox>` |

---

## Passing form values to the embedded page

Append form field values to the URL using `concat()` in the `calculation` column and reference the result in the label:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | webbox_url | | `concat('https://dashboard.example.com/household?id=', ${household_id})` |
| note | hh_dash | `<webbox src='${webbox_url}' title='Household Dashboard'>Open Dashboard</webbox>` |

{{% alert icon=" " context="warning" %}}
The `src` attribute in the `<webbox>` tag supports `${fieldname}` references when the label is computed from a `calculate` field. Construct the full URL in a `calculate` field and reference it.
{{% /alert %}}

---

## Repeat interaction: delete buttons

Webbox also supports special action tags for managing repeat groups inside labels:

```html
<delete-repeat-current>Remove this row</delete-repeat-current>
<delete-repeat-last>Remove last row</delete-repeat-last>
```

These render as buttons that delete repeat instances when tapped. Place them in a `note` field inside (or just after) the repeat group:

| type | name | label |
|------|------|-------|
| begin_repeat | items | Item |
| text | item_name | Item name |
| note | delete_btn | `<delete-repeat-current>✕ Remove this item</delete-repeat-current>` |
| end_repeat | | |

---

## Communication with the embedded page (postMessage)

The webbox iframe and the parent form can communicate using the browser's `postMessage` API. The parent sends an `init` message to the iframe when it opens. The embedded page can respond with:

- `delete-repeat-current` — triggers deletion of the current repeat instance
- `delete-repeat-last` — triggers deletion of the last repeat instance

This enables custom web tools (e.g., drawing tools, interactive maps) to trigger form actions when the user confirms an action inside the iframe.

---

## Best Practices

1. Use webbox for **reference material** (guidelines, lookup tables, maps) — not for collecting data that should be in the form itself.
2. Ensure the embedded URL is accessible from the device's network — webbox requires connectivity.
3. Keep the embedded page mobile-friendly — the modal is 800px wide maximum and 80% of viewport height.
4. Use descriptive button text (e.g., "View Village Map") rather than generic labels ("Click here").
5. Inform enumerators that closing the modal returns them to the survey — some users may not know how to close an iframe overlay.

## Limitations

- Webbox requires network connectivity to load the embedded URL.
- Some external sites block embedding in iframes via `X-Frame-Options` or `Content-Security-Policy` headers — these sites cannot be used with webbox.
- The modal closes when the enumerator navigates away from the question — any unsaved state in the iframe is lost.
- Webbox is an rtSurvey web form extension and may not work in other ODK-compatible clients.
