---
weight: 2
title: "Nasazení"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "dns"
toc: true
description: "Nasaďte a spravujte vlastní instanci rtCloud pomocí Dockeru. Plná kontrola nad vašimi daty, infrastrukturou a konfigurací."
---

Spusťte rtCloud na vlastní infrastruktuře pomocí Docker Compose. Vlastní hosting vám dává úplné vlastnictví vašich dat, sítě a prostředí nasazení — ideální pro organizace s požadavky na umístění dat, sítě bez přístupu k internetu nebo vlastní infrastrukturní potřeby.

## Co je vlastní hosting rtCloud?

Vlastní hosting rtCloud je oficiální Docker obraz, který balí celou platformu rtCloud do přenosného kontejnerového zásobníku, který lze spustit na libovolném serveru Linux. Zásobník zahrnuje:

| Služba | Popis |
|---------|-------------|
| **Aplikace rtCloud** | Webová aplikace Apache 2.4 + PHP 7.4 s vestavěnou frontou na pozadí (Beanstalkd), analytickým serverem (Shiny) a plánovanými úlohami |
| **MySQL 8.0** | Relační databáze pro všechna aplikační a průzkumová data |
| **Keycloak** *(volitelné)* | Vložený server jednotného přihlášení pro správu podnikových identit |

## Kdy zvolit vlastní hosting

Vlastní hosting je správnou volbou, pokud:

- Požadujete **datovou suverenitu** — všechna data zůstávají ve vaší vlastní infrastruktuře
- Provozujete **síť bez přístupu k internetu nebo s omezeným přístupem** bez externího cloudového přístupu
- Máte **požadavky na dodržování předpisů** (GDPR, HIPAA, vládní datové politiky) nařizující ukládání dat na místě
- Potřebujete integraci s **interním poskytovatelem identit** (Active Directory, LDAP, SAML)
- Chcete **přizpůsobit prostředky** — přidělení CPU, RAM a úložiště podle svých podmínek

## V této sekci

| Stránka | Popis |
|------|-------------|
| [Rychlý start](quick-start) | Spuštění rtCloud na serveru za méně než 10 minut |
| [Referenční příručka konfigurace](configuration) | Úplný seznam všech proměnných prostředí a jejich výchozích hodnot |
| [Cloudové nasazení](cloud-deployment) | Automatizované skripty jedním kliknutím pro DigitalOcean, AWS, GCP a Linode |
| [SSO autentizace](sso-authentication) | Konfigurace Keycloak, externího OIDC nebo Azure AD |
| [Údržba](maintenance) | Upgradování, zálohování, obnovení a odstraňování problémů instance |

## Přehled architektury

Nasazení běží jako sada Docker kontejnerů propojených v interní síti:

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

Při povolení SSO běží vedle třetí kontejner:

```
┌─────────────────────────────────────────┐
│            rtcloud-keycloak             │
│  Keycloak (port 8080, internal only)    │
│  Admin UI (port 9000, internal only)    │
└─────────────────────────────────────────┘
```

Všechny kontejnery komunikují přes izolovanou Docker bridge síť. Na hostitele je vystavena pouze Port webové aplikace a (volitelně) analytický port Shiny.
