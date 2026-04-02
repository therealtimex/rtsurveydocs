import React from 'react';
import { DocsThemeConfig } from 'nextra-theme-docs';

const config: DocsThemeConfig = {
  project: {
    link: 'https://github.com/rtSurvey',
  },
  docsRepositoryBase: 'https://github.com/rtSurvey/docs',
  footer: {
    text: (
      <span>
        MIT {new Date().getFullYear()} © rtSurvey
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
