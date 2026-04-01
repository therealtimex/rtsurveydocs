---
weight: 2
title: "Deployment"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "dns"
toc: true
description: "Vendosni dhe menaxhoni instancën tuaj rtCloud duke përdorur Docker. Kontroll i plotë mbi të dhënat, infrastrukturën dhe konfigurimin tuaj."
---

Ekzekutoni rtCloud në infrastrukturën tuaj duke përdorur Docker Compose. Pritja vetjake ju jep pronësi të plotë mbi të dhënat, rrjetin dhe mjedisin e vendosjes — ideal për organizatat me kërkesa të rezidencës së të dhënave, rrjete të izoluara ose nevoja të infrastrukturës së personalizuar.

## Çfarë është Pritja Vetjake e rtCloud?

Pritja Vetjake rtCloud është një imazh zyrtar Docker që paketizon të gjithë platformën rtCloud në një grup kontejnerësh të lëvizshëm që mund të ekzekutoni në çdo server Linux. Grupi përfshin:

| Shërbimi | Përshkrimi |
|---------|-------------|
| **Aplikacioni rtCloud** | Aplikacion ueb Apache 2.4 + PHP 7.4 me radhë të integruar në sfond (Beanstalkd), server analitike (Shiny) dhe detyra të planifikuara |
| **MySQL 8.0** | Bazë të dhënash relacionale për të gjitha të dhënat e aplikacionit dhe sondazhit |
| **Keycloak** *(opsional)* | Server i integruar i Hyrjes së Vetme për menaxhimin e identitetit të ndërmarrjeve |

## Kur të Pritësh Vetë

Pritja vetjake është zgjedhja e duhur kur ju:

- Keni nevojë për **sovranitet të të dhënave** — të gjitha të dhënat qëndrojnë brenda infrastrukturës suaj
- Operoni në një **rrjet të izoluar ose të kufizuar** pa akses të jashtëm në cloud
- Keni **kërkesa pajtueshmërie** (GDPR, HIPAA, politikat qeveritare të të dhënave) që mandatojnë ruajtjen lokale
- Keni nevojë të integroheni me një **ofrues të brendshëm identiteti** (Active Directory, LDAP, SAML)
- Dëshironi të **personalizoni burimet** — shpërndarjen e CPU, RAM dhe hapësirës ruajtëse sipas kushteve tuaja

## Në Këtë Seksion

| Faqja | Përshkrimi |
|------|-------------|
| [Fillimi i Shpejtë](quick-start) | Ekzekutoni rtCloud në server në pak se 10 minuta |
| [Referenca e Konfigurimit](configuration) | Lista e plotë e të gjitha variablave të mjedisit dhe vlerat e tyre të paracaktuara |
| [Vendosja në Cloud](cloud-deployment) | Skripte të automatizuara me një klik për DigitalOcean, AWS, GCP dhe Linode |
| [Autentifikimi SSO](sso-authentication) | Konfiguroni Keycloak, OIDC të jashtme ose Azure AD |
| [Mirëmbajtja](maintenance) | Përditësoni, rezervoni, restauroni dhe zgjidhni problemet e instancës suaj |

## Pamja e Përgjithshme e Arkitekturës

Vendosja ekzekutohet si një grup kontejnerësh Docker të lidhur në një rrjet të brendshëm:

```
┌────────────────────────────────────────┐
│            rtcloud-app                 │
│  Apache 2.4 (porta 80)                 │
│  Aplikacioni PHP 7.4                   │
│  Radha Beanstalkd (e brendshme)        │
│  Serveri Shiny (porta 3838)            │
│  Planifikuesi cron                     │
└─────────────────┬──────────────────────┘
                  │ rtcloud-net (ura)
┌─────────────────▼──────────────────────┐
│            rtcloud-mysql               │
│  MySQL 8.0 (porta 3306, vetëm e brendshme) │
└────────────────────────────────────────┘
```

Kur SSO është aktivizuar, një kontejner i tretë ekzekutohet krahas:

```
┌─────────────────────────────────────────┐
│            rtcloud-keycloak             │
│  Keycloak (porta 8080, vetëm e brendshme) │
│  UI Administratori (porta 9000, vetëm e brendshme) │
└─────────────────────────────────────────┘
```

Të gjithë kontejnerët komunikojnë nëpërmjet një rrjeti të izoluar Docker. Vetëm porta e aplikacionit ueb dhe (opsionalisht) porta e analitikës Shiny ekspozohen ndaj hostit.
