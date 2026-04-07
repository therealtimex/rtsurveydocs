// Merges English (combined/en/) and all locale builds (combined/{locale}/) into dist/
// dist/                     ← English pages (basePath: '')
// dist/{locale}/            ← Locale pages (basePath: '/{locale}')
//
// English source: combined/en/ (saved by build.sh after yarn build, before locale builds overwrite out/)
//
// Usage: node scripts/merge-output.mjs

import { existsSync, mkdirSync, rmSync, readdirSync, copyFileSync, statSync } from 'fs';
import { join, resolve } from 'path';
import { fileURLToPath } from 'url';

const ROOT = resolve(fileURLToPath(import.meta.url), '../../');
const COMBINED = join(ROOT, 'combined');
const DIST = join(ROOT, 'dist');

function copyDir(src, dest) {
  if (!existsSync(dest)) mkdirSync(dest, { recursive: true });
  for (const entry of readdirSync(src)) {
    const s = join(src, entry);
    const d = join(dest, entry);
    if (statSync(s).isDirectory()) copyDir(s, d);
    else copyFileSync(s, d);
  }
}

if (existsSync(DIST)) rmSync(DIST, { recursive: true, force: true });
mkdirSync(DIST, { recursive: true });

// English at root — use combined/en/ (locale builds overwrite out/, so out/ is unreliable)
const englishSrc = join(COMBINED, 'en');
if (!existsSync(englishSrc)) {
  console.error('combined/en/ not found — run ./build.sh first (it saves English output there)');
  process.exit(1);
}
copyDir(englishSrc, DIST);
console.log('Copied English (combined/en/) → dist/');

// Locales at dist/{locale}/
for (const locale of readdirSync(COMBINED)) {
  if (locale === 'en') continue; // already copied above
  const src = join(COMBINED, locale);
  if (!statSync(src).isDirectory()) continue;
  const dest = join(DIST, locale);
  copyDir(src, dest);
  console.log(`Copied ${locale} (combined/${locale}/) → dist/${locale}/`);
}

console.log('\nDone. Merged output in dist/');
