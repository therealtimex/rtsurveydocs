# Design: Platform Interfaces Menu Cleanup

## Goal
Resolve the duplication issue in the left menu for "rtSurvey Cloud" and "rtSurvey Mobile App" across all 36 languages, and remove the "Web App" interface from the documentation menu.

## Problem Analysis
1.  **Duplication**: In Nextra, when a directory has an `index.mdx` file that is not explicitly hidden or mapped in its local `_meta.json`, it is displayed as a child item in the menu using its frontmatter title. For directories like `rtsurvey-cloud`, this results in a menu structure like:
    - rtSurvey Cloud (folder)
        - rtSurvey Cloud (index.mdx)
        - Overview
        - ...
    This creates a redundant "rtSurvey Cloud" entry at the top of the folder's children.
2.  **Web App Removal**: The "Web App" interface is no longer needed in the public documentation menu.

## Proposed Solution

### 1. Fix Duplication in Folders
For every locale (including English in `pages/`), update the `_meta.json` files within the following sub-directories:
- `platform-interfaces/rtsurvey-cloud/`
- `platform-interfaces/mobile-app/`

Add the following configuration to the top of these `_meta.json` files:
```json
{
  "index": { "display": "hidden" },
  ...
}
```

### 2. Remove Web App from Menu
For every locale (including English in `pages/`), update the `platform-interfaces/_meta.json` file.
- Remove the `"web-app": "..."` entry.
- Ensure `"web-form"` remains if present.

### 3. Implementation Strategy
Since this change affects 36 locales (approximately 108 files total), a Node.js script will be used to perform the modifications programmatically. This ensures consistency and avoids manual error across the large volume of translation files.

## Files Impacted
- `pages/platform-interfaces/_meta.json`
- `pages/platform-interfaces/rtsurvey-cloud/_meta.json`
- `pages/platform-interfaces/mobile-app/_meta.json`
- `_locales/*/platform-interfaces/_meta.json`
- `_locales/*/platform-interfaces/rtsurvey-cloud/_meta.json`
- `_locales/*/platform-interfaces/mobile-app/_meta.json`

## Success Criteria
1.  The left menu shows "rtSurvey Cloud" as a folder, and its first child is "Overview" (or the next defined item), NOT another "rtSurvey Cloud" link.
2.  The same applies to "Mobile App".
3.  "Web App" is no longer visible in the "Platform Interfaces" section of the menu.
4.  All 36 languages are updated correctly.
