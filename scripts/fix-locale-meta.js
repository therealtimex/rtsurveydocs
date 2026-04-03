#!/usr/bin/env node
/**
 * fix-locale-meta.js
 * Sync all locale _meta.json files with the English pages/ structure.
 */

const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const LOCALES_DIR = path.join(ROOT, '_locales');

const LOCALES = fs.readdirSync(LOCALES_DIR).filter(l =>
  fs.statSync(path.join(LOCALES_DIR, l)).isDirectory()
);

function readJson(filePath) {
  try {
    return JSON.parse(fs.readFileSync(filePath, 'utf8'));
  } catch {
    return null;
  }
}

function writeJson(filePath, obj) {
  fs.writeFileSync(filePath, JSON.stringify(obj, null, 2) + '\n', 'utf8');
}

function hasIndexMdx(dir) {
  return fs.existsSync(path.join(dir, 'index.mdx'));
}

/**
 * Fix deployment/_meta.json
 * Required structure:
 *   { "index": { "display": "hidden" }, "quick-start", "cloud-providers",
 *     "configuration", "maintenance", "ssl-setup", "sso-authentication" }
 * - Remove "index" string entry
 * - Remove "first-login"
 * - Add "index": { "display": "hidden" } as first
 * - Move "cloud-providers" to second position (after quick-start)
 */
function fixDeployment(localeDir) {
  const filePath = path.join(localeDir, 'deployment', '_meta.json');
  const meta = readJson(filePath);
  if (!meta) return;

  const keys = ['quick-start', 'cloud-providers', 'configuration', 'maintenance', 'ssl-setup', 'sso-authentication'];
  const result = { 'index': { display: 'hidden' } };
  for (const key of keys) {
    if (typeof meta[key] === 'string') {
      result[key] = meta[key];
    }
    // If key doesn't exist, skip (shouldn't happen for well-formed locales)
  }

  writeJson(filePath, result);
}

/**
 * Fix getting-started/_meta.json
 * Required structure:
 *   { "index": { "display": "hidden" }, "overview": "<translated>" }
 * - Remove dashboard-overview, system-user, your-subscription
 * - Keep overview
 */
function fixGettingStarted(localeDir) {
  const filePath = path.join(localeDir, 'getting-started', '_meta.json');
  const meta = readJson(filePath);
  if (!meta) return;

  const result = { 'index': { display: 'hidden' } };
  if (typeof meta['overview'] === 'string') {
    result['overview'] = meta['overview'];
  }

  writeJson(filePath, result);
}

/**
 * Fix platform-interfaces/_meta.json
 * Required structure:
 *   { "index": { "display": "hidden" }, "rtsurvey-cloud", "mobile-app", "web-app", "web-form" }
 */
function fixPlatformInterfaces(localeDir) {
  const filePath = path.join(localeDir, 'platform-interfaces', '_meta.json');
  const meta = readJson(filePath);
  if (!meta) return;

  const keys = ['rtsurvey-cloud', 'mobile-app', 'web-app', 'web-form'];
  const result = { 'index': { display: 'hidden' } };
  for (const key of keys) {
    if (typeof meta[key] === 'string') {
      result[key] = meta[key];
    }
  }

  writeJson(filePath, result);
}

/**
 * Fix platform-interfaces/rtsurvey-cloud/_meta.json
 * Required structure:
 *   { "overview", "dashboard-overview", "system-user", "manage-forms",
 *     "manage-submission", "manage-analysis", "manage-quality", "manage-users" }
 * For dashboard-overview and system-user: use label from getting-started/_meta.json
 * if present, otherwise fallback.
 */
function fixRtsurveyCloud(localeDir) {
  const filePath = path.join(localeDir, 'platform-interfaces', 'rtsurvey-cloud', '_meta.json');
  const meta = readJson(filePath);
  if (!meta) return;

  // Get fallback labels from getting-started
  const gsMeta = readJson(path.join(localeDir, 'getting-started', '_meta.json')) || {};
  const dashboardLabel = gsMeta['dashboard-overview'] || 'Dashboard Overview';
  const systemUserLabel = gsMeta['system-user'] || 'System & User';

  const keys = ['manage-forms', 'manage-submission', 'manage-analysis', 'manage-quality', 'manage-users'];
  const result = {};

  // overview
  result['overview'] = typeof meta['overview'] === 'string' ? meta['overview'] : 'Overview';
  // dashboard-overview and system-user
  result['dashboard-overview'] = typeof meta['dashboard-overview'] === 'string'
    ? meta['dashboard-overview'] : dashboardLabel;
  result['system-user'] = typeof meta['system-user'] === 'string'
    ? meta['system-user'] : systemUserLabel;

  for (const key of keys) {
    if (typeof meta[key] === 'string') {
      result[key] = meta[key];
    }
  }

  writeJson(filePath, result);
}

/**
 * Fix a generic _meta.json to ensure "index": { "display": "hidden" } is first,
 * only if an index.mdx exists in the directory.
 * If "index" is currently a string entry, replace it with the object form.
 * If no "index" key and index.mdx exists, prepend it.
 * If "index" is already { display: "hidden" }, leave as-is (but ensure it's first).
 */
function fixGenericWithHiddenIndex(metaFilePath) {
  const meta = readJson(metaFilePath);
  if (!meta) return;

  const dir = path.dirname(metaFilePath);
  const hasIndex = hasIndexMdx(dir);

  // Check current state of "index"
  const indexVal = meta['index'];
  const alreadyCorrect = indexVal && typeof indexVal === 'object' && indexVal.display === 'hidden';

  if (!hasIndex) {
    // No index.mdx — if there's an "index" key at all, remove it
    if ('index' in meta) {
      const result = {};
      for (const [k, v] of Object.entries(meta)) {
        if (k !== 'index') result[k] = v;
      }
      writeJson(metaFilePath, result);
    }
    return;
  }

  // Has index.mdx
  if (alreadyCorrect) {
    // Ensure it's first
    const keys = Object.keys(meta);
    if (keys[0] === 'index') return; // already first, no change needed
    const result = { 'index': { display: 'hidden' } };
    for (const [k, v] of Object.entries(meta)) {
      if (k !== 'index') result[k] = v;
    }
    writeJson(metaFilePath, result);
    return;
  }

  // Need to add/fix index as { display: 'hidden' } as first entry
  const result = { 'index': { display: 'hidden' } };
  for (const [k, v] of Object.entries(meta)) {
    if (k !== 'index') result[k] = v;
  }
  writeJson(metaFilePath, result);
}

/**
 * Fix survey-design/_meta.json — ensure "index": { display: hidden } is first
 * (same generic fix)
 */
function fixSurveyDesign(localeDir) {
  const filePath = path.join(localeDir, 'survey-design', '_meta.json');
  fixGenericWithHiddenIndex(filePath);
}

// Process each locale
let processedCount = 0;
for (const locale of LOCALES) {
  const localeDir = path.join(LOCALES_DIR, locale);

  fixDeployment(localeDir);
  fixGettingStarted(localeDir);
  fixPlatformInterfaces(localeDir);
  fixRtsurveyCloud(localeDir);
  fixSurveyDesign(localeDir);

  // Generic sections that need "index": { display: hidden } if index.mdx exists
  const genericSections = [
    'survey-design/question-types',
    'survey-design/advanced-features',
    'survey-design/operators-and-functions',
    'survey-design/logic',
    'platform-interfaces/mobile-app',
    'deployment/cloud-providers',
  ];

  for (const section of genericSections) {
    const metaPath = path.join(localeDir, section, '_meta.json');
    if (fs.existsSync(metaPath)) {
      fixGenericWithHiddenIndex(metaPath);
    }
  }

  processedCount++;
}

console.log(`Done. Processed ${processedCount} locales: ${LOCALES.join(', ')}`);
