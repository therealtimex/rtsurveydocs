# Platform Interfaces Menu Cleanup Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Clean up the left menu by removing "Web App" and fixing duplication in "rtSurvey Cloud" and "Mobile App" across all 36 locales.

**Architecture:** Use a Node.js automation script to perform surgical JSON modifications across 100+ `_meta.json` files to ensure consistency and speed.

**Tech Stack:** Node.js (fs, path)

---

### Task 1: Create Cleanup Script

**Files:**
- Create: `scripts/cleanup-menu.mjs`

- [ ] **Step 1: Write the cleanup script**

```javascript
import { readFileSync, writeFileSync, readdirSync, existsSync } from 'fs';
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

function updateMeta(filePath, updater) {
  if (!existsSync(filePath)) return;
  try {
    const content = JSON.parse(readFileSync(filePath, 'utf8'));
    const updated = updater(content);
    if (updated) {
      writeFileSync(filePath, JSON.stringify(updated, null, 2) + '\n');
      console.log(`Updated: ${filePath}`);
    }
  } catch (e) {
    console.error(`Error updating ${filePath}: ${e.message}`);
  }
}

function processDirectory(baseDir) {
  // 1. Update platform-interfaces/_meta.json to remove web-app
  const platformMeta = join(baseDir, 'platform-interfaces', '_meta.json');
  updateMeta(platformMeta, (meta) => {
    if (meta['web-app']) {
      delete meta['web-app'];
      return meta;
    }
    return null;
  });

  // 2. Hide index in rtsurvey-cloud
  const cloudMeta = join(baseDir, 'platform-interfaces', 'rtsurvey-cloud', '_meta.json');
  updateMeta(cloudMeta, (meta) => {
    if (!meta.index || meta.index.display !== 'hidden') {
      return { index: { display: 'hidden' }, ...meta };
    }
    return null;
  });

  // 3. Hide index in mobile-app
  const mobileMeta = join(baseDir, 'platform-interfaces', 'mobile-app', '_meta.json');
  updateMeta(mobileMeta, (meta) => {
    if (!meta.index || meta.index.display !== 'hidden') {
      return { index: { display: 'hidden' }, ...meta };
    }
    return null;
  });
}

// Process English pages
console.log('Processing pages/ (English)...');
processDirectory(PAGES_DIR);

// Process all other locales
for (const locale of ALL_LOCALES) {
  console.log(`Processing _locales/${locale}...`);
  processDirectory(join(LOCALES_DIR, locale));
}

console.log('Done.');
```

- [ ] **Step 2: Run the cleanup script**

Run: `node scripts/cleanup-menu.mjs`

- [ ] **Step 3: Verify changes in English**

Check `pages/platform-interfaces/_meta.json` (should have no `web-app`) and `pages/platform-interfaces/rtsurvey-cloud/_meta.json` (should have `index: { display: "hidden" }`).

- [ ] **Step 4: Verify changes in one other locale (e.g., vi)**

Check `_locales/vi/platform-interfaces/_meta.json` and `_locales/vi/platform-interfaces/rtsurvey-cloud/_meta.json`.

- [ ] **Step 5: Remove the temporary script**

Run: `rm scripts/cleanup-menu.mjs`

- [ ] **Step 6: Commit changes**

```bash
git add pages/ _locales/
git commit -m "fix: remove Web App from menu and hide redundant index entries in all locales"
```
