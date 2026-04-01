---
weight: 3
title: "AWS EC2"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-16T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "cloud"
toc: true
description: "Wdrażaj rtCloud na instancji AWS EC2 przy użyciu skryptu user data aws-ec2.sh."
---

Użyj `aws-ec2.sh` jako skryptu **User Data** podczas uruchamiania instancji EC2. Skrypt uruchamia się automatycznie przy pierwszym rozruchu.

**Pobierz skrypt:** [aws-ec2.sh](/scripts/aws-ec2.sh)

---

## Krok 1 — Wypełnij konfigurację

Otwórz skrypt i edytuj blok `CONFIGURATION` na górze:

```bash
# --- Wymagane ---
PROJECT_ID="rtsurvey"
ADMIN_PASSWORD="admin"                       # Zmień po pierwszym logowaniu

# --- Domena + SSL ---
DOMAIN="myapp.example.com"
LETSENCRYPT_EMAIL="admin@example.com"

# --- Wbudowany Keycloak ---
EMBED_KEYCLOAK="true"
KEYCLOAK_ADMIN_PASSWORD="${ADMIN_PASSWORD}"  # Domyślnie ADMIN_PASSWORD
```

| Pole | Wymagane | Opis |
|-------|----------|-------------|
| `PROJECT_ID` | Tak | Używane jako nazwa bazy danych i ID klienta Keycloak. Małe litery, bez spacji. |
| `ADMIN_PASSWORD` | Nie | Hasło administratora aplikacji i Keycloak. Domyślnie `admin` — **zmień po pierwszym logowaniu**. |
| `DOMAIN` | Nie | Twoja domena dla HTTPS. Zostaw puste dla trybu tylko HTTP. |
| `LETSENCRYPT_EMAIL` | Tak (jeśli ustawiono DOMAIN) | Email do powiadomień Let's Encrypt. |
| `EMBED_KEYCLOAK` | Nie | `true`, aby wdrożyć wbudowany Keycloak (wymaga 4 GB RAM). |

> **Bezpieczeństwo:** Wszystkie hasła domyślnie mają wartość `admin`. Zmień je natychmiast po pierwszym logowaniu.

---

## Krok 2 — Uruchom instancję EC2

W [konsoli AWS EC2](https://console.aws.amazon.com/ec2):

1. Kliknij **Launch instance**
2. **AMI:** Ubuntu Server 22.04 LTS (64-bit x86)
3. **Typ instancji:** `t3.medium` (4 GB RAM) lub większy
4. **Para kluczy:** Wybierz lub utwórz dla dostępu SSH
5. **Ustawienia sieci:** Utwórz lub wybierz grupę zabezpieczeń (zob. poniżej)
6. **Szczegóły zaawansowane** → **Dane użytkownika** → wklej pełną zawartość skryptu
7. Kliknij **Launch instance**

---

## Krok 3 — Skonfiguruj grupę zabezpieczeń

Otwórz te porty w grupie zabezpieczeń instancji:

| Port | Protokół | Źródło | Cel |
|------|----------|--------|---------|
| 22 | TCP | Twoje IP | Dostęp SSH |
| 80 | TCP | 0.0.0.0/0 | HTTP (przekierowany do HTTPS przez Nginx) |
| 443 | TCP | 0.0.0.0/0 | HTTPS |
| 3838 | TCP | 0.0.0.0/0 | Bezpośredni dostęp do Shiny |

> **Nie** otwieraj portu 3306 (MySQL) — nigdy nie powinien być publicznie dostępny.

---

## Krok 4 — Dodaj rekord DNS

Podczas uruchamiania instancji dodaj **rekord A** u dostawcy DNS:

```
Type  : A
Name  : myapp
Value : <instance-public-ip>
TTL   : 300
```

---

## Krok 5 — Monitoruj postęp

```bash
ssh ubuntu@<instance-ip>
tail -f /var/log/rtcloud-setup.log
```

---

## Krok 6 — Dostęp do aplikacji

Po zakończeniu konfiguracji dziennik pokazuje podsumowanie z URL aplikacji i danymi uwierzytelniającymi. Zaloguj się używając nazwy użytkownika `admin` i hasła `admin`, a następnie natychmiast zmień hasło.

---

## Po wdrożeniu

### Zmień hasło

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Wyświetl wszystkie kontenery

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```

### Przypisz Elastic IP (opcjonalnie)

Jeśli zatrzymasz i uruchomisz instancję, publiczne IP zmieni się. Aby zachować stabilne IP, przydziel **Elastic IP** i powiąż go z instancją w konsoli EC2.
