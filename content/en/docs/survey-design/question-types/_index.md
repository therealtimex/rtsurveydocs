---
title: "Question types"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 220
---

rtSurvey supports all standard XLSForm question types, plus several extensions. Each question type controls what kind of data is collected and how the input widget is rendered on the device.

To set the question type, enter the type name in the `type` column of the **survey** worksheet in your XLSForm.

## Text input

| Type | Description |
|------|-------------|
| [text](text) | Free-text response — any characters allowed |
| [integer](integer) | Whole number (no decimals) |
| [decimal](decimal) | Number with decimal places |
| [range](range) | Number selected from a slider within a defined min/max range |

## Selection

| Type | Description |
|------|-------------|
| [select_one listname](select-one) | Pick exactly one option from a list |
| [select_multiple listname](select-multiple) | Pick one or more options from a list |
| [rank listname](rank) | Order choices by preference or priority |

## Date and Time

| Type | Description |
|------|-------------|
| [date](date) | Calendar date (year, month, day) |
| [time](time) | Time of day (hours, minutes) |
| [datetime](datetime-date-time) | Combined date and time |

## Location

| Type | Description |
|------|-------------|
| [geopoint](geopoint) | Single GPS coordinate (latitude, longitude, altitude, accuracy) |
| [geotrace](geotrace) | A path — series of GPS points forming a line |
| [geoshape](geoshape) | An area — closed polygon of GPS points |

## Media

| Type | Description |
|------|-------------|
| [image](image) | Photo capture or image upload |
| [audio](audio) | Audio recording |
| [video](video) | Video recording |
| [file](file) | General file upload (PDF, document, etc.) |

## Other

| Type | Description |
|------|-------------|
| [barcode](barcode) | Scan a barcode or QR code |
| [note](note) | Read-only display text — shows instructions or calculated summaries |
| [calculate](calculate) | Hidden field that stores a computed value |
| [hidden](hidden) | Hidden field that stores a static or prefilled value |
| [trigger / acknowledge](trigger) | A checkbox the enumerator must tick to confirm they have read a statement |
| [meta](meta) | Automatic metadata: timestamps, device ID, enumerator info |

## rtSurvey Extensions

These types are rtSurvey-specific and are not part of the standard XLSForm specification.

| Type | Description |
|------|-------------|
| [search-autocomplete](search-autocomplete) | Text input with live API-powered autocomplete suggestions |
| [mentions](mentions) | Text field with `@` mention autocomplete for tagging entities inline |
| [texttags](texttags) | Tag input — each entry becomes a removable chip; stores as space-separated string |

For repeat groups (repeating sets of questions), see [Repeats](../advanced-extension/repeats).

## How type and appearance work together

The `type` determines **what data is collected**. The `appearance` column controls **how the widget looks**. Many types support multiple appearances — for example `select_one` can appear as radio buttons, a dropdown, a Likert scale, or a compact grid.

See [Appearance](../appearance) for the full list of options.
