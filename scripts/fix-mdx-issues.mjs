// Fix MDX compilation issues across all generated pages:
// 1. Convert HTML comments to MDX-style comments {nothing} (just remove them)
// 2. Escape bare <= outside backtick spans (MDX parses < as JSX tag start)
import { readFileSync, writeFileSync, readdirSync, statSync } from 'fs';
import { join, extname } from 'path';

const PAGES_DIR = new URL('../pages', import.meta.url).pathname;

function* walkMdx(dir) {
  for (const entry of readdirSync(dir)) {
    const full = join(dir, entry);
    if (statSync(full).isDirectory()) {
      yield* walkMdx(full);
    } else if (extname(entry) === '.mdx') {
      yield full;
    }
  }
}

// In a single line (not inside fenced code block),
// replace bare <= (outside backtick spans) with &lt;=
function escapeLtInLine(line) {
  const parts = line.split('`');
  for (let i = 0; i < parts.length; i += 2) {
    // Even indices are outside backticks
    parts[i] = parts[i].replace(/<=/g, '&lt;=');
  }
  return parts.join('`');
}

let fixed = 0;
let unchanged = 0;

for (const file of walkMdx(PAGES_DIR)) {
  const original = readFileSync(file, 'utf8');
  let content = original;

  // Step 1: Remove HTML comments (<!-- ... -->) - not valid in MDX
  content = content.replace(/<!--[\s\S]*?-->/g, '');

  // Step 2: Escape <= outside backtick spans, outside fenced code blocks
  const lines = content.split('\n');
  let inCodeFence = false;
  const processed = lines.map(line => {
    const trimmed = line.trimStart();
    if (trimmed.startsWith('```') || trimmed.startsWith('~~~')) {
      inCodeFence = !inCodeFence;
      return line;
    }
    if (inCodeFence) return line;
    if (line.includes('<=')) {
      return escapeLtInLine(line);
    }
    return line;
  });

  content = processed.join('\n');

  if (content !== original) {
    writeFileSync(file, content, 'utf8');
    fixed++;
  } else {
    unchanged++;
  }
}

console.log(`Fixed: ${fixed} files`);
console.log(`Unchanged: ${unchanged} files`);
