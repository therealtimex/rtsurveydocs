---
weight: 2
title: "Wdrożenie"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "dns"
toc: true
description: "Wdrażaj własną instancję rtCloud i zarządzaj nią przy użyciu Docker. Pełna kontrola nad danymi, infrastrukturą i konfiguracją."
---

Uruchom rtCloud na własnej infrastrukturze przy użyciu Docker Compose. Samodzielny hosting daje Ci pełną własność danych, sieci i środowiska wdrożeniowego — idealny dla organizacji z wymaganiami dotyczącymi przechowywania danych, sieci izolowanych od Internetu lub niestandardowych potrzeb infrastrukturalnych.

## Czym jest rtCloud Self-Hosting?

rtCloud Self-Hosting to oficjalny obraz Docker pakujący całą platformę rtCloud w przenośny stos kontenerów, który można uruchomić na dowolnym serwerze Linux. Stos zawiera:

| Usługa | Opis |
|---------|-------------|
| **rtCloud App** | Aplikacja webowa Apache 2.4 + PHP 7.4 z wbudowaną kolejką w tle (Beanstalkd), serwerem analitycznym (Shiny) i zaplanowanymi zadaniami |
| **MySQL 8.0** | Relacyjna baza danych dla wszystkich danych aplikacji i ankiet |
| **Keycloak** *(opcjonalny)* | Wbudowany serwer Single Sign-On do zarządzania tożsamościami korporacyjnymi |

## Kiedy wdrożyć samodzielny hosting

Samodzielny hosting to właściwy wybór, gdy:

- Wymagasz **suwerenności danych** — wszystkie dane pozostają w Twojej własnej infrastrukturze
- Działasz w **sieci izolowanej lub z ograniczeniami** bez zewnętrznego dostępu do chmury
- Masz **wymagania dotyczące zgodności** (RODO, HIPAA, rządowe polityki danych) nakazujące przechowywanie na miejscu
- Musisz zintegrować się z **wewnętrznym dostawcą tożsamości** (Active Directory, LDAP, SAML)
- Chcesz **dostosować zasoby** — przydział CPU, RAM i przestrzeni dyskowej według własnych warunków

## W tej sekcji

| Strona | Opis |
|------|-------------|
| [Szybki start](quick-start) | Uruchom rtCloud na serwerze w mniej niż 10 minut |
| [Dokumentacja konfiguracji](configuration) | Pełna lista wszystkich zmiennych środowiskowych i ich wartości domyślnych |
| [Wdrożenie w chmurze](cloud-deployment) | Jednoklikalnie zautomatyzowane skrypty dla DigitalOcean, AWS, GCP i Linode |
| [Uwierzytelnianie SSO](sso-authentication) | Konfiguracja Keycloak, zewnętrznego OIDC lub Azure AD |
| [Konserwacja](maintenance) | Aktualizacja, tworzenie kopii zapasowych, przywracanie i rozwiązywanie problemów z instancją |

## Przegląd architektury

Wdrożenie działa jako zestaw kontenerów Docker połączonych w wewnętrznej sieci:

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

Gdy SSO jest włączone, trzeci kontener działa równolegle:

```
┌─────────────────────────────────────────┐
│            rtcloud-keycloak             │
│  Keycloak (port 8080, internal only)    │
│  Admin UI (port 9000, internal only)    │
└─────────────────────────────────────────┘
```

Wszystkie kontenery komunikują się przez izolowaną sieć bridge Docker. Tylko port aplikacji webowej i (opcjonalnie) port analityczny Shiny są udostępniane hostowi.
