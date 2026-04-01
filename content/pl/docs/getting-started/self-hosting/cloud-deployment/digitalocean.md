---
weight: 1
title: "DigitalOcean"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-17T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "water_drop"
toc: true
description: "Wdrażaj rtCloud na Droplet DigitalOcean przy użyciu zautomatyzowanych skryptów user-data."
---

DigitalOcean używa skryptów **User Data**, które uruchamiają się automatycznie przy pierwszym rozruchu. Wypełniasz zmienne konfiguracyjne na górze skryptu, a następnie wklejasz cały skrypt podczas tworzenia Droplet.

> W przeciwieństwie do Linode StackScripts, DigitalOcean nie ma interfejsu formularza — musisz edytować skrypt bezpośrednio przed wklejeniem.

**Pobierz skrypt:** [digitalocean-droplet-keycloak-embed.sh](/scripts/digitalocean-droplet-keycloak-embed.sh)

---

## Wbudowany Keycloak (zalecany)

Użyj `digitalocean-droplet-keycloak-embed.sh` dla najprostszej konfiguracji z wbudowanym SSO.

### Krok 1 — Wypełnij konfigurację

Otwórz skrypt i edytuj blok `CONFIGURATION` na górze:

```bash
# --- Wymagane ---
PROJECT_ID="rtsurvey"                  # Unikalny identyfikator projektu (bez spacji)
ADMIN_PASSWORD="admin"                 # Hasło dla administratora aplikacji i Keycloak — zmień po pierwszym logowaniu

# --- Domena + SSL ---
DOMAIN="myapp.example.com"            # Twoja domena — rekord DNS A musi tu wskazywać
PROJECT_URL=""                         # Zostaw puste, chyba że jesteś za Cloudflare/proxy
LETSENCRYPT_EMAIL="admin@example.com" # Email do powiadomień Let's Encrypt

# --- Opcjonalne ---
STATA_ENABLED="false"
TZ="Asia/Ho_Chi_Minh"
```

| Pole | Wymagane | Opis |
|-------|----------|-------------|
| `PROJECT_ID` | Tak | Używane jako nazwa bazy danych i ID klienta Keycloak. Małe litery, bez spacji. |
| `ADMIN_PASSWORD` | Nie | Hasło do logowania administratora aplikacji i konsoli administratora Keycloak. Domyślnie `admin` — **zmień po pierwszym logowaniu**. |
| `DOMAIN` | Tak | Twoja nazwa domeny. Rekord DNS A musi wskazywać na IP Droplet. |
| `LETSENCRYPT_EMAIL` | Tak | Adres email do powiadomień o certyfikacie Let's Encrypt. |
| `PROJECT_URL` | Nie | Zastąp publiczny URL. Zostaw puste, aby używać `DOMAIN`. Przydatne za Cloudflare. |

> **Bezpieczeństwo:** Wszystkie hasła domyślnie mają wartość `admin`. Zmień je natychmiast po pierwszym logowaniu.

### Krok 2 — Utwórz Droplet

W [panelu sterowania DigitalOcean](https://cloud.digitalocean.com):

1. Kliknij **Create** → **Droplets**
2. Wybierz **Ubuntu 22.04 LTS** jako obraz
3. Wybierz **Basic, 4 GB RAM / 2 vCPU** lub większy
4. Przewiń do **Advanced Options** → zaznacz **Add Initialization scripts**
5. Wklej pełną zawartość skryptu do pola tekstowego
6. Kliknij **Create Droplet**

### Krok 3 — Dodaj rekord DNS

Podczas uruchamiania Droplet dodaj **rekord A** u dostawcy DNS:

```
Type  : A
Name  : myapp          (lub @ dla domeny głównej)
Value : <droplet-ip>
TTL   : 300
```

### Krok 4 — Monitoruj postęp

Połącz się przez SSH z Droplet i obserwuj dziennik:

```bash
ssh root@<droplet-ip>
tail -f /var/log/rtcloud-setup.log
```

Skrypt wyświetla IP serwera na początku — dodaj rekord DNS od razu po jego zobaczeniu.

### Krok 5 — Dostęp do aplikacji

Po zakończeniu konfiguracji dziennik pokazuje podsumowanie:

```
============================================================
 rtCloud deployment complete! (Embedded Keycloak)
============================================================
 App URL   : https://myapp.example.com
 Admin     : admin / admin
 Keycloak  : https://myapp.example.com/auth/admin

 !! SECURITY: All passwords default to 'admin'.
    Change them immediately after first login.
============================================================
```

Otwórz `https://myapp.example.com` w przeglądarce i zaloguj się używając nazwy użytkownika `admin` i hasła `admin`.

> **Zmień hasło** natychmiast po logowaniu przez **Ustawienia** w menu w prawym górnym rogu.

---

## Po wdrożeniu

### Zmień hasło

Połącz się przez SSH z Droplet, edytuj `.env` i uruchom ponownie kontener:

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Zaktualizuj domenę

Jeśli po wdrożeniu przypisujesz inną domenę, zaktualizuj `PROJECT_URL` w `.env`:

```bash
nano /opt/rtcloud/.env   # zaktualizuj PROJECT_URL=
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Wyświetl wszystkie kontenery

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```
