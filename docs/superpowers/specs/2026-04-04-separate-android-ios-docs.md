# Design: Separating Android and iOS Mobile App Documentation

## Goal
Split the existing "Mobile App" documentation into two completely independent sections: "Android App" and "iOS App". Each will have its own dedicated set of pages for Overview, Installation, Connection, Configuration, and Functionalities.

## Problem Analysis
Currently, both platforms are merged under "Mobile App". While many features are similar, separating them allows for cleaner, platform-specific instructions (especially for Installation and System Requirements) and caters to users who only care about one ecosystem.

## Proposed Structure

### 1. File System Changes
The current `pages/platform-interfaces/mobile-app/` directory will be retired. Its contents will be duplicated and adapted into two new directories:
- `pages/platform-interfaces/android-app/`
- `pages/platform-interfaces/ios-app/`

This change will also be applied across all 36 locales in `_locales/*/platform-interfaces/`.

### 2. Menu Updates (`_meta.json`)
The top-level `platform-interfaces/_meta.json` will be updated:
```json
{
  "index": { "display": "hidden" },
  "rtsurvey-cloud": "rtSurvey Cloud",
  "android-app": "Android App",
  "ios-app": "iOS App",
  "web-form": "Web Form"
}
```

Each new directory will have its own `_meta.json`:
```json
{
  "index": { "display": "hidden" },
  "overview": "Overview",
  "installation": "Installation",
  "connection": "Connecting to Server",
  "configuration": "Configuration",
  "functionalities": "Functionalities"
}
```

### 3. Content Adaptation
- **Android App**: Will focus on Google Play links, Android 7.0+ requirements, and Android-specific UI screenshots if available.
- **iOS App**: Will focus on App Store links, iOS 15.0+ requirements, and the iOS-specific details retrieved from `asc` (Business/Productivity categories, 17+ rating).

## Implementation Strategy
Since this involves duplicating and renaming files across 36 languages (approximately 36 locales * 6 files * 2 platforms = 432 files), a Node.js script will be used to:
1. Create the new directories.
2. Copy the existing files.
3. Rename files to match the new structure (e.g., `installing-rtsurvey.mdx` -> `installation.mdx`).
4. Update frontmatter and internal links programmatically.
5. Delete the old `mobile-app` directories.

## Success Criteria
1. The sidebar shows "Android App" and "iOS App" as separate items.
2. Clicking "Android App" shows Android-specific content.
3. Clicking "iOS App" shows iOS-specific content (including the 15.0+ requirement).
4. All 36 languages are updated and functional.
