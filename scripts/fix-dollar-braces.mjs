// Fix bare ${varname} patterns in MDX prose text
// MDX evaluates {varname} as JSX expressions; outside code blocks this causes ReferenceError
// Fix: wrap bare ${varname} in backticks to make them code spans
import { readFileSync, writeFileSync, readdirSync, statSync } from 'fs';
import { join, extname } from 'path';

const PAGES_DIR = new URL('../pages', import.meta.url).pathname;

function* walkMdx(dir) {
  for (const entry of readdirSync(dir)) {
    const full = join(dir, entry);
    if (statSync(full).isDirectory()) yield* walkMdx(full);
    else if (extname(entry) === '.mdx') yield full;
  }
}

// In a single part (outside backtick spans, outside code fences),
// wrap bare ${varname} with backtick code spans
function fixDollarBraces(text) {
  return text.replace(/\$\{([^}]*)\}/g, (match) => '`' + match + '`');
}

let fixed = 0;

for (const file of walkMdx(PAGES_DIR)) {
  const original = readFileSync(file, 'utf8');
  const lines = original.split('\n');
  let inFence = false;
  let changed = false;

  const processed = lines.map(line => {
    const trimmed = line.trimStart();
    if (trimmed.startsWith('```') || trimmed.startsWith('~~~')) {
      inFence = !inFence;
      return line;
    }
    if (inFence || !line.includes('${')) return line;

    // Split by backtick spans; only modify even-indexed parts (outside backticks)
    const parts = line.split('`');
    let lineChanged = false;
    for (let i = 0; i < parts.length; i += 2) {
      if (!parts[i].includes('${')) continue;
      const fixed2 = fixDollarBraces(parts[i]);
      if (fixed2 !== parts[i]) {
        parts[i] = fixed2;
        lineChanged = true;
      }
    }
    if (lineChanged) {
      changed = true;
      return parts.join('`');
    }
    return line;
  });

  if (changed) {
    writeFileSync(file, processed.join('\n'), 'utf8');
    fixed++;
  }
}

console.log(`Fixed: ${fixed} files`);
