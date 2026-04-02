const withNextra = require('nextra')({
  theme: 'nextra-theme-docs',
  themeConfig: './theme.config.tsx',
});

// Support per-locale builds via NEXT_BASE_PATH env var
const basePath = process.env.NEXT_BASE_PATH || '';

module.exports = withNextra({
  output: 'export',
  trailingSlash: true,
  reactStrictMode: true,
  basePath,
  images: {
    unoptimized: true,
  },
});
