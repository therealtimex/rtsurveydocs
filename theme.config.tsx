import React from 'react';
import { DocsThemeConfig } from 'nextra-theme-docs';

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
