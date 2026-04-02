// Split-build script: builds each locale separately (~80 pages each)
// to avoid webpack OOM when all 2,884 MDX files compile at once.
//
// Usage:
//   node scripts/build-split.mjs                  → build ALL locales
//   node scripts/build-split.mjs vi fr de          → build specific locales
//
// Output: locale outputs in combined/{locale}/

import { execSync } from 'child_process';
import {
  existsSync, mkdirSync, rmSync, readdirSync, copyFileSync,
  renameSync, statSync
} from 'fs';
import { join, resolve } from 'path';
import { fileURLToPath } from 'url';

const ROOT = resolve(fileURLToPath(import.meta.url), '../../');
const PAGES = join(ROOT, 'pages');
const OUT = join(ROOT, 'out');
const COMBINED = join(ROOT, 'combined');

const ALL_LOCALES = [
  'vi','fr','de','pt','es','zh-hans','ar','th','id','km',
  'hi','ru','zh-hant','ko','ja','it','nl','tr','uk','nb',
  'da','sv','fi','el','pl','cs','sk','hu','bg','sr',
  'sq','lv','lt','te','pt-br'
];

// Locales to build: use CLI args or all
const targetLocales = process.argv.slice(2).length > 0 ? process.argv.slice(2) : ALL_LOCALES;

function run(cmd) {
  execSync(cmd, { cwd: ROOT, stdio: 'inherit' });
}

function copyDir(src, dest) {
  if (!existsSync(dest)) mkdirSync(dest, { recursive: true });
  for (const entry of readdirSync(src)) {
    const s = join(src, entry);
    const d = join(dest, entry);
    if (statSync(s).isDirectory()) copyDir(s, d);
    else copyFileSync(s, d);
  }
}

// Locale build: swap pages/{locale}/ to pages/ root, build with basePath, restore
async function buildLocale(locale) {
  console.log(`\n=== Building locale: ${locale} ===`);
  const localeDir = join(PAGES, locale);
  if (!existsSync(localeDir)) {
    console.log(`  No pages/${locale}/ found, skipping.`);
    return;
  }

  const STASH = join(ROOT, '.build-stash');
  if (!existsSync(STASH)) mkdirSync(STASH, { recursive: true });

  // English root page files/dirs to stash
  const ENGLISH_DIRS = ['getting-started','deployment','survey-design','platform-interfaces'];
  const ENGLISH_FILES = ['index.mdx','contact.mdx','support.mdx','sponsor.mdx','_meta.json'];

  // Stash all OTHER locale dirs
  const otherLocales = ALL_LOCALES.filter(l => l !== locale);
  for (const l of otherLocales) {
    const p = join(PAGES, l);
    if (existsSync(p)) renameSync(p, join(STASH, `loc_${l}`));
  }

  // Stash English root structure
  for (const d of ENGLISH_DIRS) {
    const p = join(PAGES, d);
    if (existsSync(p)) renameSync(p, join(STASH, `en_${d}`));
  }
  for (const f of ENGLISH_FILES) {
    const p = join(PAGES, f);
    if (existsSync(p)) renameSync(p, join(STASH, `en_${f}`));
  }

  // Move locale content to pages root
  for (const entry of readdirSync(localeDir)) {
    renameSync(join(localeDir, entry), join(PAGES, entry));
  }
  rmSync(localeDir, { recursive: true, force: true });

  if (existsSync(OUT)) rmSync(OUT, { recursive: true, force: true });

  let success = false;
  try {
    run(`NODE_OPTIONS='--max-old-space-size=6144' NEXT_BASE_PATH=/${locale} yarn build`);
    success = true;
  } catch (e) {
    console.error(`  Build failed for ${locale}: ${e.message}`);
  }

  // Restore: move pages root entries back to locale dir
  const SKIP_RESTORE = new Set([
    'node_modules','.next','out','.build-stash','combined','scripts',
    'public','content','layouts','assets','static','data','i18n',
    'exampleSite','resources','images',
    locale,  // skip the locale dir itself (just created empty)
    ...ALL_LOCALES,  // skip all locale dirs (they are stashed)
  ]);
  const SKIP_EXTENSIONS = new Set(['.js','.ts','.tsx','.toml','.mod','.sum','.lock','.yml','.yaml','.mjs']);
  const SKIP_FILES = new Set(['package.json','tsconfig.json','.prettierrc','yarn.lock','CNAME']);

  mkdirSync(localeDir, { recursive: true });
  for (const entry of readdirSync(PAGES)) {
    if (SKIP_RESTORE.has(entry) || entry.startsWith('.')) continue;
    const ext = entry.includes('.') ? entry.substring(entry.lastIndexOf('.')) : '';
    if (SKIP_EXTENSIONS.has(ext) || SKIP_FILES.has(entry)) continue;
    renameSync(join(PAGES, entry), join(localeDir, entry));
  }

  // Restore English root
  for (const d of ENGLISH_DIRS) {
    const stashed = join(STASH, `en_${d}`);
    if (existsSync(stashed)) renameSync(stashed, join(PAGES, d));
  }
  for (const f of ENGLISH_FILES) {
    const stashed = join(STASH, `en_${f}`);
    if (existsSync(stashed)) renameSync(stashed, join(PAGES, f));
  }

  // Restore other locales
  for (const l of otherLocales) {
    const stashed = join(STASH, `loc_${l}`);
    if (existsSync(stashed)) renameSync(stashed, join(PAGES, l));
  }

  rmSync(STASH, { recursive: true, force: true });

  if (success && existsSync(OUT)) {
    const dest = join(COMBINED, locale);
    if (existsSync(dest)) rmSync(dest, { recursive: true, force: true });
    copyDir(OUT, dest);
    console.log(`  Saved ${locale} to combined/${locale}/`);
  }
}

if (!existsSync(COMBINED)) mkdirSync(COMBINED, { recursive: true });

for (const locale of targetLocales) {
  await buildLocale(locale);
}

console.log(`\nDone. Locale outputs in combined/`);
