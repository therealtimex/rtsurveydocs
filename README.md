# rtSurvey Documentation

Official documentation site for [rtSurvey](https://rtsurvey.com) — a powerful mobile data collection and survey platform.

Live site: [https://docs.rtsurvey.com](https://docs.rtsurvey.com)

## Overview

This site is built with [Hugo](https://gohugo.io/) using the [Lotus Docs](https://github.com/colinwilson/lotusdocs) theme and deployed to GitHub Pages.

## Features

- Multilingual support (36+ languages)
- Full-text search powered by FlexSearch
- Dark mode
- Responsive design

## Local Development

### Requirements

- Hugo Extended (minimum v0.128.0)
- Go (minimum v1.21)
- Git

### Run locally

```bash
hugo server -D
```

Navigate to `http://localhost:1313/docs/`

## Deployment

Pushes to the `release` branch automatically trigger a GitHub Actions build and deploy to GitHub Pages at [https://docs.rtsurvey.com](https://docs.rtsurvey.com).

## Contributing

Content lives in the `content/` directory, organized by language code (e.g. `content/en/`, `content/vi/`, `content/fr/`).

Each page uses Hugo front matter:

```yaml
---
title: "Page Title"
description: "Short description"
icon: "article"
draft: false
toc: true
weight: 100
---
```

## License

Copyright © rtSurvey. All rights reserved.
