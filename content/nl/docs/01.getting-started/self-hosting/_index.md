---
weight: 115
title: "Zelf hosten"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "dns"
toc: true
description: "Implementeer en beheer uw eigen rtCloud-instantie met Docker. Volledige controle over uw gegevens, infrastructuur en configuratie."
---

Voer rtCloud uit op uw eigen infrastructuur met Docker Compose. Zelf hosten geeft u volledig eigenaarschap over uw gegevens, netwerk en implementatieomgeving — ideaal voor organisaties met vereisten voor gegevensresidentie, air-gapped netwerken of aangepaste infrastructuurbehoeften.

## Wat is rtCloud zelf hosten?

rtCloud Zelf Hosten is een officiële Docker-image die het volledige rtCloud-platform verpakt in een draagbare containerstapel die u op elke Linux-server kunt uitvoeren. De stapel bevat:

| Service | Beschrijving |
|---------|-------------|
| **rtCloud App** | Apache 2.4 + PHP 7.4-webapplicatie met ingebouwde achtergrondwachtrij (Beanstalkd), analyseserver (Shiny) en geplande taken |
| **MySQL 8.0** | Relationele database voor alle applicatie- en enquêtegegevens |
| **Keycloak** *(optioneel)* | Ingebedde Single Sign-On-server voor identiteitsbeheer op enterpriseniveau |

## Wanneer zelf hosten

Zelf hosten is de juiste keuze wanneer u:

- **Gegevenssoevereiniteit** vereist — alle gegevens blijven binnen uw eigen infrastructuur
- Actief bent in een **air-gapped of beperkt netwerk** zonder externe cloudtoegang
- **Nalevingsvereisten** heeft (AVG, HIPAA, overheidsgegevensbeleid) die opslag op locatie verplichten
- Wilt integreren met een **interne identiteitsprovider** (Active Directory, LDAP, SAML)
- **Resources wilt aanpassen** — CPU-, RAM- en opslagtoewijzing op uw eigen voorwaarden

## In deze sectie

| Pagina | Beschrijving |
|------|-------------|
| [Snelstart](quick-start) | rtCloud binnen 10 minuten op een server laten draaien |
| [Configuratiereferentie](configuration) | Volledige lijst van alle omgevingsvariabelen en hun standaardwaarden |
| [Cloudimplementatie](cloud-deployment) | Één-klik geautomatiseerde scripts voor DigitalOcean, AWS, GCP en Linode |
| [SSO-authenticatie](sso-authentication) | Keycloak, externe OIDC of Azure AD configureren |
| [Onderhoud](maintenance) | Uw instantie upgraden, back-uppen, herstellen en problemen oplossen |

## Architectuuroverzicht

De implementatie wordt uitgevoerd als een set Docker-containers verbonden op een intern netwerk:

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

Wanneer SSO is ingeschakeld, wordt een derde container naast de andere uitgevoerd:

```
┌─────────────────────────────────────────┐
│            rtcloud-keycloak             │
│  Keycloak (port 8080, internal only)    │
│  Admin UI (port 9000, internal only)    │
└─────────────────────────────────────────┘
```

Alle containers communiceren via een geïsoleerd Docker bridge-netwerk. Alleen de webapplicatiepoort en (optioneel) de Shiny-analysepoort worden blootgesteld aan de host.
