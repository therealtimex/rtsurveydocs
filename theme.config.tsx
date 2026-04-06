import React, { useEffect, useState } from 'react';
import { DocsThemeConfig } from 'nextra-theme-docs';
import { useRouter } from 'next/router';

const LanguageSwitcher = () => {
  const { asPath } = useRouter();
  const [currentLocale, setCurrentLocale] = useState('en');
  const [isOpen, setIsOpen] = useState(false);

  const ALL_LANGUAGES = [
  {
    "code": "en",
    "name": "English"
  },
  {
    "code": "id",
    "name": "Bahasa Indonesia"
  },
  {
    "code": "cs",
    "name": "Čeština"
  },
  {
    "code": "da",
    "name": "Dansk"
  },
  {
    "code": "de",
    "name": "Deutsch"
  },
  {
    "code": "es",
    "name": "Español"
  },
  {
    "code": "fr",
    "name": "Français"
  },
  {
    "code": "it",
    "name": "Italiano"
  },
  {
    "code": "lv",
    "name": "Latviešu"
  },
  {
    "code": "lt",
    "name": "Lietuvių"
  },
  {
    "code": "hu",
    "name": "Magyar"
  },
  {
    "code": "nl",
    "name": "Nederlands"
  },
  {
    "code": "nb",
    "name": "Norsk Bokmål"
  },
  {
    "code": "pl",
    "name": "Polski"
  },
  {
    "code": "pt",
    "name": "Português"
  },
  {
    "code": "pt-br",
    "name": "Português (Brasil)"
  },
  {
    "code": "sq",
    "name": "Shqip"
  },
  {
    "code": "sk",
    "name": "Slovenčina"
  },
  {
    "code": "sr",
    "name": "Srpski"
  },
  {
    "code": "fi",
    "name": "Suomi"
  },
  {
    "code": "sv",
    "name": "Svenska"
  },
  {
    "code": "vi",
    "name": "Tiếng Việt"
  },
  {
    "code": "tr",
    "name": "Türkçe"
  },
  {
    "code": "el",
    "name": "Ελληνικά"
  },
  {
    "code": "bg",
    "name": "Български"
  },
  {
    "code": "ru",
    "name": "Русский"
  },
  {
    "code": "uk",
    "name": "Українська"
  },
  {
    "code": "ar",
    "name": "العربية"
  },
  {
    "code": "hi",
    "name": "हिन्दी"
  },
  {
    "code": "te",
    "name": "తెలుగు"
  },
  {
    "code": "th",
    "name": "ไทย"
  },
  {
    "code": "km",
    "name": "ភាសាខ្មែរ"
  },
  {
    "code": "ko",
    "name": "한국어"
  },
  {
    "code": "ja",
    "name": "日本語"
  },
  {
    "code": "zh-hans",
    "name": "简体中文"
  },
  {
    "code": "zh-hant",
    "name": "繁體中文"
  }
];

  useEffect(() => {
    // Determine current locale from URL path
    const path = window.location.pathname;
    const pathParts = path.split('/');
    // Check if first part is a known locale (excluding empty string from leading slash)
    const firstPart = pathParts[1];
    if (firstPart && ALL_LANGUAGES.some(l => l.code === firstPart)) {
      setCurrentLocale(firstPart);
    } else {
      setCurrentLocale('en');
    }
  }, [asPath]);

  const switchLanguage = (locale: string) => {
    if (locale === currentLocale) {
      setIsOpen(false);
      return;
    }

    const currentPath = window.location.pathname;
    let newPath = '';

    // 1. Remove current locale prefix if it exists
    let cleanPath = currentPath;
    if (currentLocale !== 'en') {
      const regex = new RegExp(`^/${currentLocale}(/|$)`);
      cleanPath = currentPath.replace(regex, '/');
    }

    // 2. Add new locale prefix if not switching to English
    if (locale === 'en') {
      newPath = cleanPath;
    } else {
      newPath = `/${locale}${cleanPath === '/' ? '' : cleanPath}`;
    }

    // 3. Force absolute redirect to handle different static build roots
    // Ensure we don't have double slashes
    newPath = newPath.replace(/\/+/g, '/');
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

const config: DocsThemeConfig = {
  project: {
    link: 'https://github.com/therealtimex/rtsurvey',
  },
  chat: {
    link: 'https://twitter.com/RtSurvey',
    icon: (
      <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
        <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/>
      </svg>
    ),
  },
  navbar: {
    extraContent: <LanguageSwitcher />
  },
  docsRepositoryBase: 'https://github.com/therealtimex/rtsurvey/tree/main/docs',
  footer: {
    text: (
      <span>
        MIT {new Date().getFullYear()} ©{' '}
        <a href="https://rtsurvey.com" target="_blank">
          rtSurvey
        </a>
        .
      </span>
    ),
  },
  head: (
    <>
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <meta property="og:title" content="rtSurvey Docs" />
      <meta property="og:description" content="Official documentation for rtSurvey platform." />
      <link rel="icon" href="/favicon.ico" type="image/x-icon" />
    </>
  ),
  logo: (
    <span style={{ fontWeight: 700, fontSize: '1.1rem' }}>
      rtSurvey Docs
    </span>
  ),
}

export default config;
