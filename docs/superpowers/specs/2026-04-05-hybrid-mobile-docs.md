# Design: Hybrid Mobile App Documentation Structure

## Goal
Consolidate mobile app documentation into a single "Mobile App" menu entry while keeping platform-specific details (Android vs. iOS) clearly separated for installation and setup.

## Problem Analysis
Having "Android App" and "iOS App" as two completely separate top-level entries causes significant duplication of content for "Functionalities", "Connection", and "Configuration", as these aspects are identical across platforms. A hybrid structure improves maintainability and user navigation.

## Proposed Structure

### 1. File System Organization
The new structure within `pages/platform-interfaces/mobile-app/` (and all `_locales/*/platform-interfaces/mobile-app/`):

- `mobile-app/`
    - `_meta.json` (Root mobile meta)
    - `index.mdx` (Hidden container)
    - `connection.mdx` (Shared: Connecting to Server)
    - `configuration.mdx` (Shared: Configuration)
    - `functionalities.mdx` (Shared: Features & Functionalities)
    - `android/`
        - `_meta.json` (Android-specific meta)
        - `overview.mdx` (Android features & requirements)
        - `installation.mdx` (Google Play instructions)
    - `ios/`
        - `_meta.json` (iOS-specific meta)
        - `overview.mdx` (App Store features & requirements)
        - `installation.mdx` (App Store instructions)

### 2. Menu Updates (`_meta.json`)

**`platform-interfaces/_meta.json`**:
```json
{
  "index": { "display": "hidden" },
  "rtsurvey-cloud": "rtSurvey Cloud",
  "mobile-app": "Mobile App",
  "web-form": "Web Form"
}
```

**`mobile-app/_meta.json`**:
```json
{
  "index": { "display": "hidden" },
  "android": "Android",
  "ios": "iOS",
  "connection": "Connecting to Server",
  "configuration": "Configuration",
  "functionalities": "Functionalities"
}
```

**`mobile-app/android/_meta.json`** and **`mobile-app/ios/_meta.json`**:
```json
{
  "index": { "display": "hidden" },
  "overview": "Overview",
  "installation": "Installation"
}
```

### 3. Content Strategy
- **Shared Files**: Use generic "mobile app" terminology.
- **Platform Files**: Retain the specific links and requirements (Android 7.0+ vs iOS 15.0+).

## Implementation Strategy
A Node.js script will:
1. Create the `mobile-app`, `android`, and `ios` directories.
2. Distribute the current `android-app` and `ios-app` files into the new structure.
3. Consolidate the shared `.mdx` files into the `mobile-app` root.
4. Generate the three-level `_meta.json` hierarchy for all 36 locales.
5. Cleanup the now-obsolete `android-app` and `ios-app` directories.

## Success Criteria
1. Sidebar shows a single "Mobile App" entry.
2. Expanding "Mobile App" reveals "Android", "iOS", and the shared functionality pages.
3. Platform-specific content is restricted to the "Android" and "iOS" sub-menus.
4. All 36 languages are updated correctly.
