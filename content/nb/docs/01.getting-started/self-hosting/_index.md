---
weight: 2
title: "Deployment"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "dns"
toc: true
description: "Distribuer og administrer din egen rtCloud-instans med Docker. Full kontroll over dine data, infrastruktur og konfigurasjon."
---

Kjør rtCloud på din egen infrastruktur med Docker Compose. Selvdrifting gir deg fullt eierskap over data, nettverk og distribusjonsmiljø — ideelt for organisasjoner med krav til dataopphold, isolerte nettverk eller spesielle infrastrukturbehov.

## Hva er rtCloud selvdrifting?

rtCloud selvdrifting er et offisielt Docker-bilde som pakker hele rtCloud-plattformen inn i en bærbar containerstabel du kan kjøre på en hvilken som helst Linux-server. Stabelen inkluderer:

| Tjeneste | Beskrivelse |
|---------|-------------|
| **rtCloud App** | Apache 2.4 + PHP 7.4-nettapplikasjon med innebygd bakgrunnskø (Beanstalkd), analyseserver (Shiny) og planlagte oppgaver |
| **MySQL 8.0** | Relasjonsdatabase for alle applikasjons- og undersøkelsesdata |
| **Keycloak** *(valgfritt)* | Innebygd Single Sign-On-server for identitetsadministrasjon i bedrifter |

## Når bør du selvdrifte?

Selvdrifting er det rette valget når du:

- Krever **datasuverenittet** — alle data forblir innenfor din egen infrastruktur
- Opererer i et **isolert eller begrenset nettverk** uten tilgang til ekstern sky
- Har **samsvarskrav** (GDPR, HIPAA, offentlige datapolicyer) som krever lagring på egne servere
- Trenger å integrere med en **intern identitetsleverandør** (Active Directory, LDAP, SAML)
- Ønsker å **tilpasse ressurser** — CPU, RAM og lagringstildeling på egne premisser

## I denne seksjonen

| Side | Beskrivelse |
|------|-------------|
| [Hurtigstart](quick-start) | Få rtCloud kjørende på en server på under 10 minutter |
| [Konfigurasjonsreferanse](configuration) | Fullstendig liste over alle miljøvariabler og standardverdier |
| [Skydistribusjon](cloud-deployment) | Automatiserte skript for DigitalOcean, AWS, GCP og Linode |
| [SSO-autentisering](sso-authentication) | Konfigurer Keycloak, ekstern OIDC eller Azure AD |
| [Vedlikehold](maintenance) | Oppgrader, sikkerhetskopier, gjenopprett og feilsøk instansen din |

## Arkitekturoversikt

Distribusjonen kjører som et sett med Docker-containere koblet til et internt nettverk:

```
┌────────────────────────────────────────┐
│            rtcloud-app                 │
│  Apache 2.4 (port 80)                  │
│  PHP 7.4 application                   │
│  Beanstalkd queue (internal)           │
│  Shiny Server (port 3838)              │
│  Cron scheduler                        │
└─────────────────┬──────────────────────┘
                  │ rtcloud-net (bridge)
┌─────────────────▼──────────────────────┐
│            rtcloud-mysql               │
│  MySQL 8.0 (port 3306, internal only)  │
└────────────────────────────────────────┘
```

Når SSO er aktivert, kjører en tredje container ved siden av:

```
┌─────────────────────────────────────────┐
│            rtcloud-keycloak             │
│  Keycloak (port 8080, internal only)    │
│  Admin UI (port 9000, internal only)    │
└─────────────────────────────────────────┘
```

Alle containere kommuniserer over et isolert Docker-bro-nettverk. Kun nettapplikasjonsporten og (valgfritt) Shiny-analyseportens port eksponeres til verten.
