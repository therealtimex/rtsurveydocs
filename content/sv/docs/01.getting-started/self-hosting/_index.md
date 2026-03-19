---
weight: 115
title: "Självhosting"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "dns"
toc: true
description: "Driftsätt och hantera din egen rtCloud-instans med Docker. Full kontroll över dina data, infrastruktur och konfiguration."
---

Kör rtCloud på din egen infrastruktur med Docker Compose. Självhosting ger dig fullständigt ägarskap över dina data, nätverk och driftsättningsmiljö — idealiskt för organisationer med krav på datasuveränitet, luftgappade nätverk eller anpassade infrastrukturbehov.

## Vad är rtCloud självhosting?

rtCloud självhosting är en officiell Docker-avbild som paketerar hela rtCloud-plattformen i en portabel containerstack som du kan köra på vilken Linux-server som helst. Stacken inkluderar:

| Tjänst | Beskrivning |
|---------|-------------|
| **rtCloud App** | Apache 2.4 + PHP 7.4-webbapplikation med inbyggd bakgrundskö (Beanstalkd), analysserver (Shiny) och schemalagda uppgifter |
| **MySQL 8.0** | Relationsdatabas för alla applikations- och undersökningsdata |
| **Keycloak** *(valfritt)* | Inbäddad Single Sign-On-server för identitetshantering i företag |

## När bör du självhosta?

Självhosting är rätt val när du:

- Kräver **datasuveränitet** — alla data stannar inom din egen infrastruktur
- Verkar i ett **luftgappat eller begränsat nätverk** utan extern molnåtkomst
- Har **efterlevnadskrav** (GDPR, HIPAA, statliga datapolicyer) som kräver lokal lagring
- Behöver integrera med en **intern identitetsleverantör** (Active Directory, LDAP, SAML)
- Vill **anpassa resurser** — CPU-, RAM- och lagringsallokering enligt dina villkor

## I det här avsnittet

| Sida | Beskrivning |
|------|-------------|
| [Snabbstart](quick-start) | Kom igång med rtCloud på en server på under 10 minuter |
| [Konfigurationsreferens](configuration) | Fullständig lista över alla miljövariabler och deras standardvärden |
| [Molndriftsättning](cloud-deployment) | Enkelsklicksautomatiserade skript för DigitalOcean, AWS, GCP och Linode |
| [SSO-autentisering](sso-authentication) | Konfigurera Keycloak, extern OIDC eller Azure AD |
| [Underhåll](maintenance) | Uppgradera, säkerhetskopiera, återställ och felsök din instans |

## Arkitekturöversikt

Driftsättningen körs som en uppsättning Docker-containrar anslutna till ett internt nätverk:

```
┌────────────────────────────────────────┐
│            rtcloud-app                 │
│  Apache 2.4 (port 80)                  │
│  PHP 7.4-applikation                   │
│  Beanstalkd-kö (intern)                │
│  Shiny Server (port 3838)              │
│  Cron-schemaläggare                    │
└─────────────────┬──────────────────────┘
                  │ rtcloud-net (brygga)
┌─────────────────▼──────────────────────┐
│            rtcloud-mysql               │
│  MySQL 8.0 (port 3306, endast intern)  │
└────────────────────────────────────────┘
```

När SSO är aktiverat körs en tredje container parallellt:

```
┌─────────────────────────────────────────┐
│            rtcloud-keycloak             │
│  Keycloak (port 8080, endast intern)    │
│  Admin-UI (port 9000, endast intern)    │
└─────────────────────────────────────────┘
```

Alla containrar kommunicerar via ett isolerat Docker-bryggsnätverk. Endast webbapplikationsporten och (valfritt) Shiny-analyssportporten exponeras till värden.
