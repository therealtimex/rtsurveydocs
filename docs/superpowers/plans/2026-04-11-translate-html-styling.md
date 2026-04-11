# HTML Styling Translation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Translate the MDX file `pages/survey-design/advanced-features/html-styling.mdx` into 35 locales.

**Architecture:** Use a Python script to perform the translations for all 35 locales in a single run, ensuring consistency and adherence to technical constraints (English-only XLSForm terms and field references).

**Tech Stack:** Python 3.

---

### Task 1: Create Translation Script

**Files:**
- Create: `scripts/generate_html_styling_translations.py`

- [ ] **Step 1: Write the translation script**

The script will contain a mapping of locales to their respective translations for all prose and callout text.

```python
import os

source_path = "pages/survey-design/advanced-features/html-styling.mdx"
locales = [
    "bg", "cs", "da", "de", "el", "es", "fi", "fr", "hi", "hu", 
    "id", "it", "ja", "km", "ko", "lt", "lv", "nb", "nl", "pl", 
    "pt", "pt-br", "ru", "sk", "sq", "sr", "sv", "te", "th", "tr", 
    "uk", "vi", "zh-hans", "zh-hant"
]

# (Translation logic and data will be here)
```

- [ ] **Step 2: Execute the script**

Run: `python3 scripts/generate_html_styling_translations.py`

- [ ] **Step 3: Verify output**

Check if `_locales/de/survey-design/advanced-features/html-styling.mdx` exists and has correct German translations.

- [ ] **Step 4: Cleanup**

Run: `rm scripts/generate_html_styling_translations.py`
