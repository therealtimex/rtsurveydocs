import fs from 'fs';
import path from 'path';

const ROOT = '/Volumes/ExDisk/rtLab/webapp/doc.rtsurvey.com/.claude/worktrees/agent-aade13fd';
const LOCALES_DIR = path.join(ROOT, '_locales');

const locales = fs.readdirSync(LOCALES_DIR).filter(name => {
  const stat = fs.statSync(path.join(LOCALES_DIR, name));
  return stat.isDirectory();
});

console.log(`Processing ${locales.length} locales...\n`);

const results = {
  moved: [],
  deleted: [],
  skipped: [],
};

for (const locale of locales) {
  const base = path.join(LOCALES_DIR, locale);
  const destDir = path.join(base, 'platform-interfaces', 'rtsurvey-cloud');

  // Files to move: [src, dest]
  const moves = [
    [
      path.join(base, 'getting-started', 'dashboard-overview.mdx'),
      path.join(destDir, 'dashboard-overview.mdx'),
    ],
    [
      path.join(base, 'getting-started', 'system-user.mdx'),
      path.join(destDir, 'system-user.mdx'),
    ],
  ];

  // Files to delete
  const deletions = [
    path.join(base, 'getting-started', 'your-subscription.mdx'),
    path.join(base, 'deployment', 'first-login.mdx'),
  ];

  // Process moves
  for (const [src, dest] of moves) {
    if (fs.existsSync(src)) {
      // Ensure destination directory exists
      fs.mkdirSync(path.dirname(dest), { recursive: true });
      fs.renameSync(src, dest);
      results.moved.push(`${locale}: ${path.relative(base, src)} → ${path.relative(base, dest)}`);
    } else {
      results.skipped.push(`${locale}: MOVE src not found: ${path.relative(base, src)}`);
    }
  }

  // Process deletions
  for (const filePath of deletions) {
    if (fs.existsSync(filePath)) {
      fs.unlinkSync(filePath);
      results.deleted.push(`${locale}: deleted ${path.relative(base, filePath)}`);
    } else {
      results.skipped.push(`${locale}: DELETE not found: ${path.relative(base, filePath)}`);
    }
  }
}

console.log('=== MOVED ===');
results.moved.forEach(l => console.log(' ', l));

console.log('\n=== DELETED ===');
results.deleted.forEach(l => console.log(' ', l));

console.log('\n=== SKIPPED (not found) ===');
results.skipped.forEach(l => console.log(' ', l));

console.log(`\nDone. Moved: ${results.moved.length}, Deleted: ${results.deleted.length}, Skipped: ${results.skipped.length}`);
