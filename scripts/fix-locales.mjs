import { readFileSync, writeFileSync, readdirSync, existsSync } from 'fs';
import { join } from 'path';

const LOCALES_DIR = '_locales';
const CONTENT_DIR = 'content';

const locales = readdirSync(LOCALES_DIR).filter(f => !f.startsWith('.'));

const sectionMap = {
  'getting-started': 'getting-started',
  'deployment': 'getting-started/self-hosting',
  'survey-design': 'survey-design',
  'platform-interfaces': 'user-interface'
};

function extractTitle(filePath) {
  if (!existsSync(filePath)) return null;
  const content = readFileSync(filePath, 'utf8');
  const match = content.match(/title:\s*"(.*)"/);
  return match ? match[1] : null;
}

for (const lang of locales) {
  const metaPath = join(LOCALES_DIR, lang, '_meta.json');
  if (!existsSync(metaPath)) continue;

  let meta = JSON.parse(readFileSync(metaPath, 'utf8'));
  let changed = false;

  for (const [nextraKey, hugoPath] of Object.entries(sectionMap)) {
    const hugoIndex = join(CONTENT_DIR, lang, 'docs', hugoPath, '_index.md');
    const title = extractTitle(hugoIndex);
    if (title) {
      meta[nextraKey] = title;
      changed = true;
    }
  }

  // Also try to find titles for sub-pages if they exist in Hugo
  // Survey Design sub-sections
  const surveyDesignMetaPath = join(LOCALES_DIR, lang, 'survey-design', '_meta.json');
  if (existsSync(surveyDesignMetaPath)) {
    let sdMeta = JSON.parse(readFileSync(surveyDesignMetaPath, 'utf8'));
    let sdChanged = false;
    
    const sdSubMap = {
      'logic': 'logic',
      'question-types': 'question-types',
      'operators-and-functions': 'operators-and-functions',
      'advanced-features': 'advanced-extension'
    };

    for (const [key, path] of Object.entries(sdSubMap)) {
      const hugoIndex = join(CONTENT_DIR, lang, 'docs', 'survey-design', path, '_index.md');
      const title = extractTitle(hugoIndex);
      if (title) {
        sdMeta[key] = title;
        sdChanged = true;
      }
    }

    if (sdChanged) {
      writeFileSync(surveyDesignMetaPath, JSON.stringify(sdMeta, null, 2));
      console.log(`Updated survey-design meta for ${lang}`);
    }
  }

  if (changed) {
    writeFileSync(metaPath, JSON.stringify(meta, null, 2));
    console.log(`Updated root meta for ${lang}`);
  }
}
