# Hybrid Mobile Documentation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Consolidate mobile app documentation into a single "Mobile App" menu entry with "Android" and "iOS" sub-folders across all 36 locales.

**Architecture:** Use a Node.js script to programmatically migrate files, create the nested directory structure, and update all `_meta.json` files to ensure menu consistency.

**Tech Stack:** Node.js (fs, path)

---

### Task 1: Create Migration Script

**Files:**
- Create: `scripts/migrate-hybrid-mobile.mjs`

- [ ] **Step 1: Write the migration script**

```javascript
import { readFileSync, writeFileSync, mkdirSync, existsSync, rmSync } from 'fs';
import { join, resolve } from 'path';
import { fileURLToPath } from 'url';

const __dirname = fileURLToPath(new URL('.', import.meta.url));
const ROOT = resolve(__dirname, '..');

const LOCALES_DIR = join(ROOT, '_locales');
const PAGES_DIR = join(ROOT, 'pages');

const ALL_LOCALES = [
  'vi','fr','de','pt','es','zh-hans','ar','th','id','km',
  'hi','ru','zh-hant','ko','ja','it','nl','tr','uk','nb',
  'da','sv','fi','el','pl','cs','sk','hu','bg','sr',
  'sq','lv','lt','te','pt-br'
];

function processLocale(baseDir) {
  const platformDir = join(baseDir, 'platform-interfaces');
  const androidSource = join(platformDir, 'android-app');
  const iosSource = join(platformDir, 'ios-app');

  if (!existsSync(androidSource) || !existsSync(iosSource)) return;

  const mobileAppDir = join(platformDir, 'mobile-app');
  const androidDest = join(mobileAppDir, 'android');
  const iosDest = join(mobileAppDir, 'ios');

  mkdirSync(androidDest, { recursive: true });
  mkdirSync(iosDest, { recursive: true });

  // 1. Move Platform-Specific Files
  // Android
  writeFileSync(join(androidDest, 'overview.mdx'), readFileSync(join(androidSource, 'overview.mdx')));
  writeFileSync(join(androidDest, 'installation.mdx'), readFileSync(join(androidSource, 'installation.mdx')));
  
  // iOS
  writeFileSync(join(iosDest, 'overview.mdx'), readFileSync(join(iosSource, 'overview.mdx')));
  writeFileSync(join(iosDest, 'installation.mdx'), readFileSync(join(iosSource, 'installation.mdx')));

  // 2. Move Shared Files (using iOS version as source, but they are identical)
  writeFileSync(join(mobileAppDir, 'connection.mdx'), readFileSync(join(iosSource, 'connection.mdx')));
  writeFileSync(join(mobileAppDir, 'configuration.mdx'), readFileSync(join(iosSource, 'configuration.mdx')));
  writeFileSync(join(mobileAppDir, 'functionalities.mdx'), readFileSync(join(iosSource, 'functionalities.mdx')));
  writeFileSync(join(mobileAppDir, 'index.mdx'), readFileSync(join(iosSource, 'index.mdx')));

  // 3. Create Meta Files
  // Root Mobile Meta
  const rootMeta = {
    "index": { "display": "hidden" },
    "android": "Android",
    "ios": "iOS",
    "connection": "Connecting to Server",
    "configuration": "Configuration",
    "functionalities": "Functionalities"
  };
  writeFileSync(join(mobileAppDir, '_meta.json'), JSON.stringify(rootMeta, null, 2) + '\n');

  // Android/iOS Meta
  const subMeta = {
    "index": { "display": "hidden" },
    "overview": "Overview",
    "installation": "Installation"
  };
  writeFileSync(join(androidDest, '_meta.json'), JSON.stringify(subMeta, null, 2) + '\n');
  writeFileSync(join(iosDest, '_meta.json'), JSON.stringify(subMeta, null, 2) + '\n');

  // 4. Update Parent Meta (Platform Interfaces)
  const parentMetaPath = join(platformDir, '_meta.json');
  if (existsSync(parentMetaPath)) {
    const pMeta = JSON.parse(readFileSync(parentMetaPath, 'utf8'));
    delete pMeta['android-app'];
    delete pMeta['ios-app'];
    pMeta['mobile-app'] = "Mobile App";
    
    // Explicit Order
    const ordered = {
      index: pMeta.index,
      "rtsurvey-cloud": pMeta["rtsurvey-cloud"],
      "mobile-app": "Mobile App",
      "web-form": pMeta["web-form"]
    };
    writeFileSync(parentMetaPath, JSON.stringify(ordered, null, 2) + '\n');
  }

  // 5. Cleanup old dirs
  rmSync(androidSource, { recursive: true, force: true });
  rmSync(iosSource, { recursive: true, force: true });
}

console.log('Processing English...');
processLocale(PAGES_DIR);

for (const locale of ALL_LOCALES) {
  console.log(`Processing ${locale}...`);
  processLocale(join(LOCALES_DIR, locale));
}

console.log('Done.');
```

### Task 2: Execute and Verify

- [ ] **Step 1: Run the migration script**

Run: `node scripts/migrate-hybrid-mobile.mjs`

- [ ] **Step 2: Perform clean build**

Run: `rm -rf .next out dist && ./build.sh`

- [ ] **Step 3: Restart Docker**

Run: `export DOCKER_HOST=unix:///var/run/docker.sock && docker compose build && docker compose up -d`

- [ ] **Step 4: Verify in Browser**

Check `http://localhost`. Ensure "Mobile App" has "Android" and "iOS" sub-folders.

### Task 3: Cleanup and Commit

- [ ] **Step 1: Remove script**

Run: `rm scripts/migrate-hybrid-mobile.mjs`

- [ ] **Step 2: Commit changes**

```bash
git add .
git commit -m "feat: restructure mobile app docs into a unified hybrid menu with Android/iOS sub-folders"
```
