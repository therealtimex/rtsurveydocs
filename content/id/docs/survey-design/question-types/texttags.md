---
title: "Text Tags"
description: "Kolom input tag — responden mengetik dan menekan Enter untuk membuat token tag yang terpisah."
icon: "label"
date: "2026-04-08T00:00:00+00:00"
lastmod: "2026-04-08T00:00:00+00:00"
draft: false
toc: true
weight: 264
---

The `texttags` question type (also aliased as `text_tags`) renders an input where each value entered by the user becomes a discrete **tag token**. Users type a value, press Enter or a delimiter key, and the value is added as a removable chip. Multiple tags can be added in a single response.

## Basic XLSForm Specification

| type | name | label |
|------|------|-------|
| texttags | keywords | Enter keywords (press Enter after each) |

## Behaviour

- Each confirmed entry becomes a tag displayed as a pill/chip inside the field.
- Tags can be removed individually by clicking the × on the chip.
- The stored value is a space-separated string of all entered tags.

## Uses

1. Collecting multiple free-text keywords or codes without a predefined list
2. Labelling or categorisation fields where the set of values is open-ended
3. Any multi-value free-text input where `select_multiple` is too rigid

## Data format

Tags are stored as a single space-separated string. For example, if the user enters `malaria`, `fever`, and `cough`, the stored value is `malaria fever cough`.

## Platform support

Supported on web forms.

## Limitations

- Not part of the standard XLSForm specification — rtSurvey extension only.
- Because values are free-text, downstream analysis requires string splitting on spaces.
