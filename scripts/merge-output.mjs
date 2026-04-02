// Merges English (out/) and all locale builds (combined/{locale}/) into dist/
// dist/                     ← English pages (basePath: '')
// dist/{locale}/            ← Locale pages (basePath: '/{locale}')
//
// Usage: node scripts/merge-output.mjs

import { existsSync, mkdirSync, rmSync, readdirSync, copyFileSync, statSync } from 'fs';
import { join, resolve } from 'path';
import { fileURLToPath } from 'url';

const ROOT = resolve(fileURLToPath(import.meta.url), '../../');
const OUT = join(ROOT, 'out');
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

// English at root
if (!existsSync(OUT)) {
  console.error('out/ not found — run yarn build first');
  process.exit(1);
}
copyDir(OUT, DIST);
console.log('Copied English (out/) → dist/');

// Locales at dist/{locale}/
if (existsSync(COMBINED)) {
  for (const locale of readdirSync(COMBINED)) {
    const src = join(COMBINED, locale);
    if (!statSync(src).isDirectory()) continue;
    const dest = join(DIST, locale);
    copyDir(src, dest);
    console.log(`Copied ${locale} (combined/${locale}/) → dist/${locale}/`);
  }
}

console.log('\nDone. Merged output in dist/');
