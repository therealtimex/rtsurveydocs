---
title: "Mentions"
description: "Textové pole s automatickým doplňováním @-zmínek pro označování uživatelů nebo entit inline."
icon: "alternate_email"
date: "2026-04-08T00:00:00+00:00"
lastmod: "2026-04-08T00:00:00+00:00"
draft: false
toc: true
weight: 262
---

The `mentions` question type is a text input that activates an autocomplete dropdown when the user types `@`. It is used to tag users, staff names, codes, or any entity inline within a free-text response.

## Basic XLSForm Specification

| type | name | label |
|------|------|-------|
| mentions | note_text | Enter observation notes (use @ to tag a staff member) |

## Behaviour

- Standard typing produces ordinary text.
- Typing `@` followed by characters triggers an autocomplete search against a configured list or API.
- Selecting a suggestion inserts the mention token into the text.
- The stored value is the full text string including any embedded mention tokens.

## Uses

1. Qualitative notes that reference specific staff members or entities by name
2. Observation records where multiple people or locations need to be tagged
3. Any free-text field where controlled inline references improve downstream analysis

## Platform support

Supported on web forms.

## Limitations

- Not part of the standard XLSForm specification — rtSurvey extension only.
- The mention list source (static or API-driven) is configured at the server level, not in the XLSForm.
