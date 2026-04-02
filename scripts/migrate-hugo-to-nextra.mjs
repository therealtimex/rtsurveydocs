#!/usr/bin/env node
/**
 * Hugo → Nextra MDX Migration Script
 * Uses only Node.js built-ins (fs, path)
 */

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const ROOT = path.resolve(__dirname, '..');
const CONTENT_DIR = path.join(ROOT, 'content');
const PAGES_DIR = path.join(ROOT, 'pages');

const ALL_LANGS = [
  'en', 'vi', 'fr', 'de', 'pt', 'es', 'zh-hans', 'ar', 'th', 'id', 'km',
  'hi', 'ru', 'zh-hant', 'ko', 'ja', 'it', 'nl', 'tr', 'uk', 'nb', 'da',
  'sv', 'fi', 'el', 'pl', 'cs', 'sk', 'hu', 'bg', 'sr', 'sq', 'lv', 'lt',
  'te', 'pt-br'
];

// For English, output to pages/ (no lang prefix); others get pages/{lang}/
function getLangOutputDir(lang) {
  return lang === 'en' ? PAGES_DIR : path.join(PAGES_DIR, lang);
}

// ─────────────────────────────────────────────
// Front matter conversion
// ─────────────────────────────────────────────
const STRIP_FIELDS = new Set(['weight', 'date', 'lastmod', 'draft', 'author', 'icon', 'toc']);

function convertFrontMatter(raw) {
  const lines = raw.split('\n');
  const kept = lines.filter(line => {
    const m = line.match(/^(\w[\w-]*):/);
    if (!m) return true; // keep non-field lines (e.g. blank, continuation)
    return !STRIP_FIELDS.has(m[1]);
  });
  return kept.join('\n').trim();
}

// ─────────────────────────────────────────────
// Shortcode conversion
// ─────────────────────────────────────────────
function convertShortcodes(body) {
  let result = body;

  // Remove {{< table >}} / {{< /table >}} wrappers
  result = result.replace(/\{\{<\s*table\s*>\}\}\n?/g, '');
  result = result.replace(/\{\{<\s*\/table\s*>\}\}\n?/g, '');

  // Block alert: {{% alert icon="..." context="TYPE" %}} ... {{% /alert %}}
  result = result.replace(
    /\{\{%\s*alert[^%]*context="([^"]+)"[^%]*%\}\}([\s\S]*?)\{\{%\s*\/alert\s*%\}\}/g,
    (match, context, content) => {
      const type = context === 'light' ? '' : context;
      const trimmed = content.trim();
      if (type) {
        return `<Callout type="${type}">\n${trimmed}\n</Callout>`;
      }
      return `<Callout>\n${trimmed}\n</Callout>`;
    }
  );

  // Inline alert with text attribute: {{< alert context="TYPE" text="..." />}}
  result = result.replace(
    /\{\{<\s*alert[^>]*context="([^"]+)"[^>]*text="([^"]*)"[^>]*\/>\}\}/g,
    (match, context, text) => {
      const type = context === 'light' ? '' : context;
      if (type) {
        return `<Callout type="${type}">${text}</Callout>`;
      }
      return `<Callout>${text}</Callout>`;
    }
  );

  // Also handle icon attribute before context
  result = result.replace(
    /\{\{<\s*alert[^>]*text="([^"]*)"[^>]*context="([^"]+)"[^>]*\/>\}\}/g,
    (match, text, context) => {
      const type = context === 'light' ? '' : context;
      if (type) {
        return `<Callout type="${type}">${text}</Callout>`;
      }
      return `<Callout>${text}</Callout>`;
    }
  );

  return result;
}

// ─────────────────────────────────────────────
// Parse and convert a Hugo MD file
// ─────────────────────────────────────────────
function convertFile(srcPath) {
  const raw = fs.readFileSync(srcPath, 'utf8');

  // Split front matter
  const fmMatch = raw.match(/^---\n([\s\S]*?)\n---\n?([\s\S]*)$/);
  if (!fmMatch) {
    // No front matter — treat whole file as body
    const body = convertShortcodes(raw);
    const usesCallout = body.includes('<Callout');
    const importLine = usesCallout ? "import { Callout } from 'nextra/components'\n\n" : '';
    return importLine + body;
  }

  const [, fm, bodyRaw] = fmMatch;
  const cleanedFm = convertFrontMatter(fm);
  const body = convertShortcodes(bodyRaw);
  const usesCallout = body.includes('<Callout');
  const importLine = usesCallout ? "\nimport { Callout } from 'nextra/components'\n" : '';

  return `---\n${cleanedFm}\n---\n${importLine}\n${body.trimStart()}`;
}

// ─────────────────────────────────────────────
// File system helpers
// ─────────────────────────────────────────────
function ensureDir(dir) {
  fs.mkdirSync(dir, { recursive: true });
}

function writeFile(destPath, content) {
  ensureDir(path.dirname(destPath));
  fs.writeFileSync(destPath, content, 'utf8');
}

function writeJSON(destPath, obj) {
  ensureDir(path.dirname(destPath));
  fs.writeFileSync(destPath, JSON.stringify(obj, null, 2) + '\n', 'utf8');
}

// ─────────────────────────────────────────────
// Copy a directory of MD files → MDX
// ─────────────────────────────────────────────
function migrateDir(srcDir, destDir, skipFiles = new Set()) {
  if (!fs.existsSync(srcDir)) return 0;
  let count = 0;
  const entries = fs.readdirSync(srcDir);
  for (const entry of entries) {
    if (skipFiles.has(entry)) continue;
    const srcPath = path.join(srcDir, entry);
    const stat = fs.statSync(srcPath);
    if (stat.isDirectory()) continue; // subdirs handled separately
    if (!entry.endsWith('.md')) continue;

    let destName = entry === '_index.md' ? 'index.mdx' : entry.replace(/\.md$/, '.mdx');
    const destPath = path.join(destDir, destName);
    const content = convertFile(srcPath);
    writeFile(destPath, content);
    count++;
  }
  return count;
}

// ─────────────────────────────────────────────
// Migrate one language
// ─────────────────────────────────────────────
function migrateLang(lang) {
  const srcBase = path.join(CONTENT_DIR, lang, 'docs');
  if (!fs.existsSync(srcBase)) {
    console.log(`  [SKIP] ${lang} — no docs directory`);
    return 0;
  }

  const outBase = getLangOutputDir(lang);
  let totalCount = 0;

  // ── getting-started ──
  const gsIn = path.join(srcBase, 'getting-started');
  const gsOut = path.join(outBase, 'getting-started');
  if (fs.existsSync(gsIn)) {
    // _index.md → index.mdx
    const idxSrc = path.join(gsIn, '_index.md');
    if (fs.existsSync(idxSrc)) {
      writeFile(path.join(gsOut, 'index.mdx'), convertFile(idxSrc));
      totalCount++;
    }
    for (const f of ['overview.md', 'dashboard-overview.md', 'system-user.md', 'your-subscription.md']) {
      const src = path.join(gsIn, f);
      if (fs.existsSync(src)) {
        writeFile(path.join(gsOut, f.replace(/\.md$/, '.mdx')), convertFile(src));
        totalCount++;
      }
    }
  }

  // ── deployment (self-hosting) ──
  const shIn = path.join(srcBase, 'getting-started', 'self-hosting');
  const depOut = path.join(outBase, 'deployment');
  if (fs.existsSync(shIn)) {
    const idxSrc = path.join(shIn, '_index.md');
    if (fs.existsSync(idxSrc)) {
      writeFile(path.join(depOut, 'index.mdx'), convertFile(idxSrc));
      totalCount++;
    }
    for (const f of ['quick-start.md', 'configuration.md', 'first-login.md', 'maintenance.md', 'ssl-setup.md', 'sso-authentication.md']) {
      const src = path.join(shIn, f);
      if (fs.existsSync(src)) {
        writeFile(path.join(depOut, f.replace(/\.md$/, '.mdx')), convertFile(src));
        totalCount++;
      }
    }
    // cloud-deployment → cloud-providers (only digitalocean and linode)
    const cdIn = path.join(shIn, 'cloud-deployment');
    const cpOut = path.join(depOut, 'cloud-providers');
    if (fs.existsSync(cdIn)) {
      for (const f of ['digitalocean.md', 'linode.md']) {
        const src = path.join(cdIn, f);
        if (fs.existsSync(src)) {
          writeFile(path.join(cpOut, f.replace(/\.md$/, '.mdx')), convertFile(src));
          totalCount++;
        }
      }
    }
  }

  // ── survey-design ──
  const sdIn = path.join(srcBase, 'survey-design');
  const sdOut = path.join(outBase, 'survey-design');
  if (fs.existsSync(sdIn)) {
    // Root files
    const idxSrc = path.join(sdIn, '_index.md');
    if (fs.existsSync(idxSrc)) {
      writeFile(path.join(sdOut, 'index.mdx'), convertFile(idxSrc));
      totalCount++;
    }
    for (const f of ['key-concepts.md', 'app-api.md', 'appearance.md', 'grouping-questions.md', 'media.md', 'multi-language.md', 'repeats.md']) {
      const src = path.join(sdIn, f);
      if (fs.existsSync(src)) {
        writeFile(path.join(sdOut, f.replace(/\.md$/, '.mdx')), convertFile(src));
        totalCount++;
      }
    }

    // Logic section
    const logicOut = path.join(sdOut, 'logic');
    for (const f of ['constraint.md', 'default.md', 'read-only.md', 'relevant.md']) {
      const src = path.join(sdIn, f);
      if (fs.existsSync(src)) {
        writeFile(path.join(logicOut, f.replace(/\.md$/, '.mdx')), convertFile(src));
        totalCount++;
      }
    }
    // Create logic/index.mdx if it doesn't exist
    const logicIdx = path.join(logicOut, 'index.mdx');
    if (!fs.existsSync(logicIdx)) {
      writeFile(logicIdx,
        `---\ntitle: "Logic & Expressions"\ndescription: "Logic expressions for controlling form behavior."\n---\n\n# Logic & Expressions\n\nControl form behavior using relevant, constraint, default, and read-only expressions.\n`
      );
      totalCount++;
    }

    // question-types/
    const qtIn = path.join(sdIn, 'question-types');
    const qtOut = path.join(sdOut, 'question-types');
    totalCount += migrateDir(qtIn, qtOut);

    // operators-and-functions/
    const oafIn = path.join(sdIn, 'operators-and-functions');
    const oafOut = path.join(sdOut, 'operators-and-functions');
    totalCount += migrateDir(oafIn, oafOut);

    // advanced-extension → advanced-features/
    const aeIn = path.join(sdIn, 'advanced-extension');
    const afOut = path.join(sdOut, 'advanced-features');
    totalCount += migrateDir(aeIn, afOut);
  }

  // ── platform-interfaces (user-interface) ──
  const uiIn = path.join(srcBase, 'user-interface');
  const piOut = path.join(outBase, 'platform-interfaces');
  if (fs.existsSync(uiIn)) {
    const idxSrc = path.join(uiIn, '_index.md');
    if (fs.existsSync(idxSrc)) {
      writeFile(path.join(piOut, 'index.mdx'), convertFile(idxSrc));
      totalCount++;
    }

    // rtsurvey-cloud → rtsurvey-cloud
    const rcIn = path.join(uiIn, 'rtsurvey-cloud');
    const rcOut = path.join(piOut, 'rtsurvey-cloud');
    totalCount += migrateDir(rcIn, rcOut);

    // rtsurvey-mobile-app → mobile-app
    const maIn = path.join(uiIn, 'rtsurvey-mobile-app');
    const maOut = path.join(piOut, 'mobile-app');
    totalCount += migrateDir(maIn, maOut);

    // rtsurvey-web-app → web-app
    const waIn = path.join(uiIn, 'rtsurvey-web-app');
    const waOut = path.join(piOut, 'web-app');
    const waIdx = path.join(waIn, '_index.md');
    if (fs.existsSync(waIdx)) {
      writeFile(path.join(waOut, 'index.mdx'), convertFile(waIdx));
      totalCount++;
    }

    // rtsurvey-web-form → web-form
    const wfIn = path.join(uiIn, 'rtsurvey-web-form');
    const wfOut = path.join(piOut, 'web-form');
    const wfIdx = path.join(wfIn, '_index.md');
    if (fs.existsSync(wfIdx)) {
      writeFile(path.join(wfOut, 'index.mdx'), convertFile(wfIdx));
      totalCount++;
    }
  }

  return totalCount;
}

// ─────────────────────────────────────────────
// Create _meta.json files
// ─────────────────────────────────────────────
function createMetaFiles() {
  // Root pages/_meta.json
  const rootMeta = {
    index: { title: 'Home', theme: { breadcrumb: false, toc: false } },
    'getting-started': 'Getting Started',
    deployment: 'Deployment',
    'survey-design': 'Survey Design',
    'platform-interfaces': 'Platform Interfaces',
    contact: 'Contact Us',
    support: 'Support',
    sponsor: 'Sponsor',
  };
  // Add all non-en locales as hidden
  for (const lang of ALL_LANGS) {
    if (lang !== 'en') {
      rootMeta[lang] = { display: 'hidden' };
    }
  }
  writeJSON(path.join(PAGES_DIR, '_meta.json'), rootMeta);

  // Subsection metas that apply to every language (and root for en)
  const subMetas = {
    'getting-started/_meta.json': {
      index: 'Overview',
      overview: 'Overview',
      'dashboard-overview': 'Dashboard Overview',
      'system-user': 'System & User',
      'your-subscription': 'Your Subscription',
    },
    'deployment/_meta.json': {
      index: 'Deployment',
      'quick-start': 'Quick Start',
      configuration: 'Configuration',
      'first-login': 'First Login',
      maintenance: 'Maintenance',
      'ssl-setup': 'SSL Setup',
      'sso-authentication': 'SSO Authentication',
      'cloud-providers': 'Cloud Providers',
    },
    'deployment/cloud-providers/_meta.json': {
      digitalocean: 'DigitalOcean',
      linode: 'Linode (Akamai)',
    },
    'survey-design/_meta.json': {
      index: 'Survey Design',
      'key-concepts': 'Key Concepts',
      'app-api': 'Application API',
      appearance: 'Appearance',
      'grouping-questions': 'Grouping Questions',
      media: 'Media',
      'multi-language': 'Multi-Language',
      repeats: 'Repeats',
      logic: 'Logic & Expressions',
      'question-types': 'Question Types',
      'operators-and-functions': 'Operators & Functions',
      'advanced-features': 'Advanced Features',
    },
    'survey-design/logic/_meta.json': {
      relevant: 'Relevant (Skip Logic)',
      constraint: 'Constraint',
      calculate: 'Calculate',
      default: 'Default',
      'read-only': 'Read-Only',
    },
    'survey-design/question-types/_meta.json': {
      index: 'Question Types',
      text: 'text',
      integer: 'integer',
      decimal: 'decimal',
      'select-one': 'select_one',
      'select-multiple': 'select_multiple',
      'select-one-from-file': 'select_one_from_file',
      'datetime-date-time': 'date / time / datetime',
      image: 'image',
      audio: 'audio',
      video: 'video',
      file: 'file',
      geopoint: 'geopoint',
      geotrace: 'geotrace',
      geoshape: 'geoshape',
      barcode: 'barcode',
      range: 'range',
      rank: 'rank',
      note: 'note',
      hidden: 'hidden',
      calculate: 'calculate',
      trigger: 'trigger',
      meta: 'meta',
    },
    'survey-design/operators-and-functions/_meta.json': {
      index: 'Overview',
      operators: 'Operators',
      functions: 'Functions',
      references: 'References',
    },
    'survey-design/advanced-features/_meta.json': {
      index: 'Overview',
      'call-api': 'Call API',
      'dynamic-question-type': 'Dynamic Question Type',
      'dynamic-search': 'Dynamic Search',
      exams: 'Exams',
      'grid-layout': 'Grid Layout',
      'html-styling': 'HTML Styling',
      images: 'Images',
      repeats: 'Advanced Repeats',
      webbox: 'WebBox',
    },
    'platform-interfaces/_meta.json': {
      index: 'Platform Interfaces',
      'rtsurvey-cloud': 'rtSurvey Cloud',
      'mobile-app': 'Mobile App',
      'web-app': 'Web App',
      'web-form': 'Web Form',
    },
    'platform-interfaces/rtsurvey-cloud/_meta.json': {
      index: 'Overview',
      overview: 'Overview',
      'manage-forms': 'Manage Forms',
      'manage-submission': 'Manage Submissions',
      'manage-analysis': 'Analysis',
      'manage-quality': 'Quality Control',
      'manage-users': 'Manage Users',
    },
    'platform-interfaces/mobile-app/_meta.json': {
      index: 'Overview',
      overview: 'Overview',
      'installing-rtsurvey': 'Installation',
      'connect-to-a-server': 'Connect to Server',
      'configuring-rtsurvey': 'Configuration',
      'rtsurvey-functionalities': 'Functionalities',
    },
  };

  // Write for English root (pages/) and all other langs
  const langDirs = [PAGES_DIR, ...ALL_LANGS.filter(l => l !== 'en').map(l => path.join(PAGES_DIR, l))];

  for (const langDir of langDirs) {
    // Skip if no content was written here (lang dir doesn't exist and is not root)
    if (langDir !== PAGES_DIR && !fs.existsSync(langDir)) continue;

    // Per-lang root meta (not for the pages/ root itself)
    if (langDir !== PAGES_DIR) {
      const langMeta = {
        index: 'Home',
        'getting-started': 'Getting Started',
        deployment: 'Deployment',
        'survey-design': 'Survey Design',
        'platform-interfaces': 'Platform Interfaces',
        contact: 'Contact Us',
        support: 'Support',
        sponsor: 'Sponsor',
      };
      writeJSON(path.join(langDir, '_meta.json'), langMeta);
    }

    // Sub-section metas
    for (const [rel, meta] of Object.entries(subMetas)) {
      const destPath = path.join(langDir, rel);
      const destDir = path.dirname(destPath);
      // Only write if the directory has content
      if (fs.existsSync(destDir)) {
        writeJSON(destPath, meta);
      }
    }
  }
}

// ─────────────────────────────────────────────
// Create static stub pages (contact, support, sponsor)
// ─────────────────────────────────────────────
function createStubPages() {
  writeFile(path.join(PAGES_DIR, 'contact.mdx'),
    `---\ntitle: "Contact Us"\ndescription: "Get in touch with the rtSurvey team."\n---\n\n# Contact Us\n\nFor support and inquiries, please reach out to us.\n`
  );
  writeFile(path.join(PAGES_DIR, 'support.mdx'),
    `---\ntitle: "Support"\ndescription: "Get help with rtSurvey."\n---\n\n# Support\n\nFind answers, documentation, and community help for rtSurvey.\n`
  );
  writeFile(path.join(PAGES_DIR, 'sponsor.mdx'),
    `---\ntitle: "Sponsor"\ndescription: "Support rtSurvey development."\n---\n\n# Sponsor rtSurvey\n\nrtSurvey is an open-source project. Consider supporting its development.\n`
  );
}

// ─────────────────────────────────────────────
// Create pages/index.mdx
// ─────────────────────────────────────────────
function createIndexPage() {
  writeFile(path.join(PAGES_DIR, 'index.mdx'),
    `---\ntitle: "rtSurvey Documentation"\ndescription: "Official documentation for rtSurvey — a self-hosted mobile data collection and survey platform."\n---\n\n# rtSurvey Documentation\n\nWelcome to the official documentation for **rtSurvey** — a self-hosted platform for designing forms, collecting data in the field, and analyzing results in real time.\n\n## Quick Links\n\n- [Getting Started](/getting-started/overview)\n- [Deploy Your Server](/deployment/quick-start)\n- [Survey Design](/survey-design/key-concepts)\n- [Platform Interfaces](/platform-interfaces)\n`
  );
}

// ─────────────────────────────────────────────
// Main
// ─────────────────────────────────────────────
let totalFiles = 0;
const errors = [];

console.log('Starting Hugo → Nextra migration...\n');

// Ensure pages/ directory exists
ensureDir(PAGES_DIR);

// Create index page
createIndexPage();
totalFiles++;
console.log('Created pages/index.mdx');

// Create stub pages
createStubPages();
totalFiles += 3;
console.log('Created stub pages (contact, support, sponsor)');

// Migrate all languages
for (const lang of ALL_LANGS) {
  try {
    const count = migrateLang(lang);
    console.log(`  [${lang}] Migrated ${count} files`);
    totalFiles += count;
  } catch (err) {
    console.error(`  [${lang}] ERROR: ${err.message}`);
    errors.push({ lang, error: err.message });
  }
}

// Create all _meta.json files
createMetaFiles();
console.log('\nCreated _meta.json files');

console.log('\n────────────────────────────────────────');
console.log(`Total MDX files created: ${totalFiles}`);
if (errors.length > 0) {
  console.log(`\nErrors (${errors.length}):`);
  for (const e of errors) {
    console.log(`  ${e.lang}: ${e.error}`);
  }
} else {
  console.log('No errors encountered.');
}

// Report directory structure
console.log('\nTop-level pages/ directories:');
const topLevel = fs.readdirSync(PAGES_DIR).filter(f => {
  return fs.statSync(path.join(PAGES_DIR, f)).isDirectory();
});
for (const d of topLevel.sort()) {
  console.log(`  pages/${d}/`);
}
