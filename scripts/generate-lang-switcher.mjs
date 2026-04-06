import { readFileSync, writeFileSync } from 'fs';

const hugoToml = readFileSync('hugo.toml', 'utf8');
const languages = [];

// Match [languages.xx] and languageName = "..."
const langRegex = /\[languages\.([a-z-]+)\]\s+languageName\s*=\s*"(.*)"/g;
let match;
while ((match = langRegex.exec(hugoToml)) !== null) {
  languages.push({ code: match[1], name: match[2] });
}

// Ensure English is first
const en = languages.find(l => l.code === 'en');
const others = languages.filter(l => l.code !== 'en').sort((a, b) => a.name.localeCompare(b.name));
const allLangs = [en, ...others];

const component = `
const LanguageSwitcher = () => {
  const { asPath } = useRouter();
  const [currentLocale, setCurrentLocale] = useState('en');
  const [isOpen, setIsOpen] = useState(false);

  const ALL_LANGUAGES = ${JSON.stringify(allLangs, null, 2)};

  useEffect(() => {
    const pathParts = asPath.split('/');
    if (pathParts[1] && ALL_LANGUAGES.some(l => l.code === pathParts[1])) {
      setCurrentLocale(pathParts[1]);
    } else {
      setCurrentLocale('en');
    }
  }, [asPath]);

  const switchLanguage = (locale) => {
    if (locale === currentLocale) {
      setIsOpen(false);
      return;
    }

    let newPath = '';
    if (locale === 'en') {
      newPath = asPath.replace(/^\\/([a-z-]+)(\\/|$)/, '/');
    } else {
      // If currently not en, first remove old locale
      const pathWithoutLocale = currentLocale === 'en' ? asPath : asPath.replace(/^\\/([a-z-]+)(\\/|$)/, '/');
      newPath = \`/\${locale}\${pathWithoutLocale === '/' ? '' : pathWithoutLocale}\`;
    }

    window.location.href = newPath;
  };

  const currentLangName = ALL_LANGUAGES.find(l => l.code === currentLocale)?.name || 'English';

  return (
    <div style={{ position: 'relative', display: 'inline-block' }}>
      <button
        onClick={() => setIsOpen(!isOpen)}
        onBlur={() => setTimeout(() => setIsOpen(false), 200)}
        style={{
          padding: '0.4rem 0.8rem',
          borderRadius: '6px',
          fontSize: '0.85rem',
          fontWeight: 600,
          cursor: 'pointer',
          background: 'transparent',
          color: 'inherit',
          border: '1px solid rgba(128,128,128,0.2)',
          display: 'inline-flex',
          alignItems: 'center',
          gap: '6px',
          marginLeft: '8px',
          marginRight: '8px'
        }}
      >
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
          <circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>
        </svg>
        {currentLangName}
        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" style={{ marginLeft: '2px', transform: isOpen ? 'rotate(180deg)' : 'none', transition: 'transform 0.2s' }}>
          <path d="M6 9l6 6 6-6"/>
        </svg>
      </button>

      {isOpen && (
        <div style={{
          position: 'absolute',
          top: '100%',
          right: '8px',
          marginTop: '8px',
          background: 'var(--nextra-bg)',
          border: '1px solid rgba(128,128,128,0.2)',
          borderRadius: '6px',
          boxShadow: '0 4px 12px rgba(0,0,0,0.1)',
          zIndex: 1000,
          minWidth: '160px',
          maxHeight: '400px',
          overflowY: 'auto',
          overflowX: 'hidden'
        }}>
          {ALL_LANGUAGES.map(lang => (
            <div
              key={lang.code}
              onClick={() => switchLanguage(lang.code)}
              style={{
                padding: '8px 12px',
                cursor: 'pointer',
                fontSize: '0.85rem',
                background: currentLocale === lang.code ? 'rgba(128,128,128,0.1)' : 'transparent',
                fontWeight: currentLocale === lang.code ? 600 : 400,
                whiteSpace: 'nowrap'
              }}
              onMouseEnter={(e) => (e.currentTarget.style.background = 'rgba(128,128,128,0.1)')}
              onMouseLeave={(e) => (e.currentTarget.style.background = currentLocale === lang.code ? 'rgba(128,128,128,0.1)' : 'transparent')}
            >
              {lang.name}
            </div>
          ))}
        </div>
      )}
    </div>
  );
};
`;

console.log(component);
