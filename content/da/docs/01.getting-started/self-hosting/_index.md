---
weight: 2
title: "Deployment"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "dns"
toc: true
description: "Implementer og administrer din egen rtCloud-instans ved hjælp af Docker. Fuld kontrol over dine data, infrastruktur og konfiguration."
---

Kør rtCloud på din egen infrastruktur ved hjælp af Docker Compose. Selvhosting giver dig fuldt ejerskab over dine data, dit netværk og dit implementeringsmiljø – ideelt til organisationer med krav om dataresidens, air-gappede netværk eller brugerdefinerede infrastrukturbehov.

## Hvad er rtCloud selvhosting?

rtCloud Selvhosting er et officielt Docker-image, der pakker hele rtCloud-platformen ind i en bærbar containerstak, du kan køre på enhver Linux-server. Stakken inkluderer:

| Tjeneste | Beskrivelse |
|---------|-------------|
| **rtCloud App** | Apache 2.4 + PHP 7.4-webapplikation med indbygget baggrundskø (Beanstalkd), analyseserver (Shiny) og planlagte opgaver |
| **MySQL 8.0** | Relationsdatabase til alle applikations- og undersøgelsesdata |
| **Keycloak** *(valgfrit)* | Indlejret Single Sign-On-server til virksomhedsidentitetsstyring |

## Hvornår skal du selvhoste?

Selvhosting er det rigtige valg, når du:

- Kræver **datasovereinitet** – alle data forbliver inden for din egen infrastruktur
- Opererer i et **air-gappet eller begrænset netværk** uden ekstern cloud-adgang
- Har **overholdelseskrav** (GDPR, HIPAA, offentlige datapolitikker), der kræver lokal lagring
- Har brug for at integrere med en **intern identitetsudbyder** (Active Directory, LDAP, SAML)
- Vil **tilpasse ressourcer** – CPU, RAM og lagerallokering på dine egne betingelser

## I dette afsnit

| Side | Beskrivelse |
|------|-------------|
| [Hurtigstart](quick-start) | Få rtCloud til at køre på en server på under 10 minutter |
| [Konfigurationsreference](configuration) | Komplet liste over alle miljøvariabler og deres standardværdier |
| [Cloud-implementering](cloud-deployment) | Automatiserede scripts til DigitalOcean, AWS, GCP og Linode med ét klik |
| [SSO-godkendelse](sso-authentication) | Konfigurer Keycloak, ekstern OIDC eller Azure AD |
| [Vedligeholdelse](maintenance) | Opgradering, sikkerhedskopiering, gendannelse og fejlfinding af din instans |

## Arkitekturoversigt

Implementeringen kører som et sæt Docker-containere forbundet på et internt netværk:

```
┌────────────────────────────────────────┐
│            rtcloud-app                 │
│  Apache 2.4 (port 80)                  │
│  PHP 7.4-applikation                   │
│  Beanstalkd-kø (intern)                │
│  Shiny Server (port 3838)              │
│  Cron-planlægger                       │
└─────────────────┬──────────────────────┘
                  │ rtcloud-net (bridge)
┌─────────────────▼──────────────────────┐
│            rtcloud-mysql               │
│  MySQL 8.0 (port 3306, kun intern)     │
└────────────────────────────────────────┘
```

Når SSO er aktiveret, kører en tredje container sideløbende:

```
┌─────────────────────────────────────────┐
│            rtcloud-keycloak             │
│  Keycloak (port 8080, kun intern)       │
│  Admin-UI (port 9000, kun intern)       │
└─────────────────────────────────────────┘
```

Alle containere kommunikerer over et isoleret Docker bridge-netværk. Kun webapplikationsporten og (valgfrit) Shiny-analyticsporten eksponeres til hosten.
