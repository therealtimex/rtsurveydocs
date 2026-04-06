import React, { useEffect, useState } from 'react';
import { DocsThemeConfig } from 'nextra-theme-docs';
import { useRouter } from 'next/router';

const LanguageSwitcher = () => {
  const { asPath, basePath } = useRouter();
  const [currentLocale, setCurrentLocale] = useState('en');

  useEffect(() => {
    // Determine current locale from path
    // If path starts with /vi/, locale is vi
    const pathParts = asPath.split('/');
    if (pathParts[1] === 'vi') {
      setCurrentLocale('vi');
    } else {
      setCurrentLocale('en');
    }
  }, [asPath]);

  const toggleLanguage = () => {
    const isVi = currentLocale === 'vi';
    let newPath = '';

    if (isVi) {
      // Switch from VI to EN: remove /vi prefix
      newPath = asPath.replace(/^\/vi(\/|$)/, '/');
    } else {
      // Switch from EN to VI: add /vi prefix
      newPath = `/vi${asPath === '/' ? '' : asPath}`;
    }

    // Since we are using static export with split builds,
    // we just redirect to the physical URL.
    window.location.href = `${basePath}${newPath}`;
  };

  return (
    <button
      onClick={toggleLanguage}
      style={{
        padding: '0.4rem 0.8rem',
        borderRadius: '6px',
        fontSize: '0.85rem',
        fontWeight: 500,
        cursor: 'pointer',
        background: 'var(--nextra-primary-hue)',
        color: 'white',
        border: 'none',
        display: 'flex',
        alignItems: 'center',
        gap: '6px',
        marginRight: '8px'
      }}
    >
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
        <circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>
      </svg>
      {currentLocale === 'en' ? 'Tiếng Việt' : 'English'}
    </button>
  );
};

const config: DocsThemeConfig = {
  project: {
    link: 'https://github.com/therealtimex/rtsurvey',
  },
  navbar: {
    extraContent: <LanguageSwitcher />
  },
  chat: {
    link: 'https://twitter.com/RtSurvey',
    icon: (
      <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
        <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/>
      </svg>
    ),
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
