---
weight: 1
title: "Szybki start"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "play_circle"
toc: true
description: "Uruchom rtCloud na własnym serwerze w mniej niż 10 minut przy użyciu Docker Compose."
---

Ten przewodnik przeprowadza Cię przez wdrożenie własnej instancji rtCloud na serwerze Linux od podstaw. Po zakończeniu będziesz mieć działający rtCloud dostępny w przeglądarce.

## Wymagania wstępne

Przed rozpoczęciem upewnij się, że serwer spełnia następujące wymagania:

### Sprzęt

| Zasób | Minimalne | Zalecane |
|----------|---------|-------------|
| RAM | 2 GB | 4 GB |
| Dysk | 10 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPU |

### Oprogramowanie

| Oprogramowanie | Wersja |
|----------|---------|
| System operacyjny | Ubuntu 20.04 LTS lub nowszy (lub dowolny Linux z obsługą Docker) |
| Docker | 20.10 lub nowszy |
| Docker Compose | v2.x (`docker compose`) lub v1.x (`docker-compose`) |

**Instalacja Docker na Ubuntu:**

```bash
curl -fsSL https://get.docker.com | sh
```

Weryfikacja instalacji:

```bash
docker --version
docker compose version
```

---

## Krok 1 — Pobierz pliki

Sklonuj repozytorium wdrożeniowe na serwer:

```bash
git clone ssh://git@rtgit.rta.vn:2224/rtlab/rtwebteam/rta-smart-survey-docker.git rtcloud
cd rtcloud
```

---

## Krok 2 — Skonfiguruj środowisko

Skopiuj przykładowy plik konfiguracyjny:

```bash
cp .env.production.sample .env
```

Otwórz `.env` w edytorze tekstu i uzupełnij wymagane wartości:

```dotenv
# Unikalny identyfikator tego wdrożenia (bez spacji, bez znaków specjalnych)
PROJECT_ID=myproject

# Domena lub adres IP, pod którym użytkownicy będą uzyskiwać dostęp do aplikacji
# Przykład: rtcloud.example.com  lub  192.168.1.100
PROJECT_URL=rtcloud.example.com

# Protokół: użyj "https" jeśli masz domenę z SSL, "http" w przeciwnym razie
HTTP_PROTOCOL=https

# Silne, unikalne hasła — zmień wszystkie trzy przed uruchomieniem
MYSQL_PASSWORD=change_me_strong_password
MYSQL_ROOT_PASSWORD=change_me_root_password
ADMIN_PASSWORD=change_me_admin_password
```

> **Ważne:** Tylko `.env` jest automatycznie odczytywany przez Docker Compose. Nie twórz pliku o nazwie `.env.production`, ponieważ spowodowałoby to zamieszanie. `ADMIN_PASSWORD` jest stosowane tylko przy **pierwszym uruchomieniu** świeżej bazy danych.

---

## Krok 3 — Uruchom kontenery

Uruchom wszystkie usługi w tle:

```bash
docker compose -f docker-compose.production.yml up -d
```

Pierwsze uruchomienie trwa **3–5 minut**, podczas gdy Docker:

1. Pobiera obraz aplikacji rtCloud (~1 GB do pobrania)
2. Inicjalizuje bazę danych MySQL
3. Ładuje bazowy schemat
4. Wykonuje wszystkie oczekujące migracje bazy danych

Monitoruj postęp uruchomienia w czasie rzeczywistym:

```bash
docker compose -f docker-compose.production.yml logs -f rtcloud
```

Poczekaj, aż zobaczysz komunikat wskazujący, że aplikacja jest gotowa. Możesz też obserwować status zdrowia kontenera:

```bash
watch docker compose -f docker-compose.production.yml ps
```

---

## Krok 4 — Dostęp do aplikacji

Gdy oba kontenery pokażą `Up (healthy)`, otwórz przeglądarkę:

```
http://<PROJECT_URL>:8080
```

Zaloguj się przy użyciu konta administratora:

| Pole | Wartość |
|-------|-------|
| Nazwa użytkownika | `admin` |
| Hasło | Wartość ustawiona dla `ADMIN_PASSWORD` w `.env` |

> Zmień hasło administratora natychmiast po pierwszym logowaniu ze strony ustawień konta.

---

## Krok 5 — Weryfikacja wszystkich usług

Sprawdź, czy wszystkie kontenery działają i są zdrowe:

```bash
docker compose -f docker-compose.production.yml ps
```

Oczekiwane wyjście:

```
NAME                    IMAGE                                   STATUS
rtcloud-app             rtawebteam/rta-smartsurvey:...          Up (healthy)
rtcloud-mysql           mysql:8.0                               Up (healthy)
```

Jeśli kontener pokazuje `Up (starting)` lub `Up (unhealthy)`, poczekaj 30–60 sekund i sprawdź ponownie. MySQL może potrzebować do minuty na pełną inicjalizację przy pierwszym uruchomieniu.

---

## Informacje o portach

| Port | Usługa | Opis |
|------|---------|-------------|
| `8080` | rtCloud App | Główny interfejs webowy (konfigurowalny przez `APP_PORT`) |
| `3838` | Shiny Server | Wizualizacje analityczne i oparte na R (konfigurowalny przez `SHINY_PORT`) |

MySQL (port 3306) i wszelkie opcjonalne usługi (Keycloak) są tylko wewnętrzne i domyślnie nie są udostępniane hostowi.

---

## Następne kroki

Twoja instancja rtCloud jest teraz uruchomiona. Rozważ następujące zadania uzupełniające:

- **Włącz HTTPS** — Wskaż domenę na serwer i skonfiguruj SSL z Let's Encrypt. Zobacz [Wdrożenie w chmurze](cloud-deployment) dla zautomatyzowanej konfiguracji HTTPS.
- **Przejrzyj wszystkie ustawienia** — Przeglądaj [Dokumentację konfiguracji](configuration), aby dostosować wdrożenie do środowiska produkcyjnego.
- **Skonfiguruj SSO** — Połącz dostawcę tożsamości dla scentralizowanego uwierzytelniania użytkowników. Zobacz [Uwierzytelnianie SSO](sso-authentication).
- **Zaplanuj kopie zapasowe** — Przejrzyj stronę [Konserwacja](maintenance) dla procedur tworzenia kopii zapasowych i aktualizacji.
