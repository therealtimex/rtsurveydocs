import React, { useEffect, useState } from 'react';
import { DocsThemeConfig } from 'nextra-theme-docs';
import { useRouter } from 'next/router';

const LanguageSwitcher = () => {
  const { asPath } = useRouter();
  const [currentLocale, setCurrentLocale] = useState('en');
  const [isOpen, setIsOpen] = useState(false);

  useEffect(() => {
    const pathParts = asPath.split('/');
    if (pathParts[1] === 'vi') {
      setCurrentLocale('vi');
    } else {
      setCurrentLocale('en');
    }
  }, [asPath]);

  const switchLanguage = (locale: 'en' | 'vi') => {
    if (locale === currentLocale) {
      setIsOpen(false);
      return;
    }

    let newPath = '';
    if (locale === 'vi') {
      // Switch to VI: add /vi prefix
      newPath = `/vi${asPath === '/' ? '' : asPath}`;
    } else {
      // Switch to EN: remove /vi prefix
      newPath = asPath.replace(/^\/vi(\/|$)/, '/');
    }

    // Since each locale is a separate build, we redirect to the absolute root-based path.
    // We don't use basePath here because it's already included in the deployment structure.
    window.location.href = newPath;
  };

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
        {currentLocale === 'en' ? 'English' : 'Tiếng Việt'}
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
          minWidth: '120px',
          overflow: 'hidden'
        }}>
          <div
            onClick={() => switchLanguage('en')}
            style={{
              padding: '8px 12px',
              cursor: 'pointer',
              fontSize: '0.85rem',
              background: currentLocale === 'en' ? 'rgba(128,128,128,0.1)' : 'transparent',
              fontWeight: currentLocale === 'en' ? 600 : 400
            }}
            onMouseEnter={(e) => (e.currentTarget.style.background = 'rgba(128,128,128,0.1)')}
            onMouseLeave={(e) => (e.currentTarget.style.background = currentLocale === 'en' ? 'rgba(128,128,128,0.1)' : 'transparent')}
          >
            English
          </div>
          <div
            onClick={() => switchLanguage('vi')}
            style={{
              padding: '8px 12px',
              cursor: 'pointer',
              fontSize: '0.85rem',
              background: currentLocale === 'vi' ? 'rgba(128,128,128,0.1)' : 'transparent',
              fontWeight: currentLocale === 'vi' ? 600 : 400
            }}
            onMouseEnter={(e) => (e.currentTarget.style.background = 'rgba(128,128,128,0.1)')}
            onMouseLeave={(e) => (e.currentTarget.style.background = currentLocale === 'vi' ? 'rgba(128,128,128,0.1)' : 'transparent')}
          >
            Tiếng Việt
          </div>
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
        <a href="https://rtsurvey.com" target="_blank" rel="noopener noreferrer">
          rtSurvey
        </a>
        {' · '}
        <a href="mailto:support@rta.vn">support@rta.vn</a>
      </span>
    )
  },
  useNextSeoProps() {
    return {
      titleTemplate: '%s – rtSurvey Docs'
    }
  },
  sidebar: {
    defaultMenuCollapseLevel: 1,
    autoCollapse: true,
    toggleButton: true,
  },
  toc: {
    backToTop: true,
  },
  feedback: {
    content: null,
  },
  head: (
    <>
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <meta name="description" content="rtSurvey — Self-hosted mobile data collection and survey platform." />
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
