---
weight: 4
title: "Google Cloud (GCP)"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-16T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "travel_explore"
toc: true
description: "Nasazení rtCloud na Google Cloud Compute Engine pomocí spouštěcího skriptu gcp-compute.sh."
---

Použijte `gcp-compute.sh` jako **Startup script** při vytváření instance VM Compute Engine. Skript se automaticky spustí při prvním spuštění.

**Stáhnout skript:** [gcp-compute.sh](/scripts/gcp-compute.sh)

---

## Krok 1 — Vyplňte konfiguraci

Otevřete skript a upravte blok `CONFIGURATION` v horní části:

```bash
# --- Povinné ---
PROJECT_ID="rtsurvey"
ADMIN_PASSWORD="admin"                       # Změňte po prvním přihlášení

# --- Doména + SSL ---
DOMAIN="myapp.example.com"
LETSENCRYPT_EMAIL="admin@example.com"

# --- Vložený Keycloak ---
EMBED_KEYCLOAK="true"
KEYCLOAK_ADMIN_PASSWORD="${ADMIN_PASSWORD}"  # Výchozí je ADMIN_PASSWORD
```

| Pole | Povinné | Popis |
|-------|----------|-------------|
| `PROJECT_ID` | Ano | Používá se jako název databáze a ID klienta Keycloak. Malá písmena, bez mezer. |
| `ADMIN_PASSWORD` | Ne | Heslo admin aplikace a heslo admin Keycloak. Výchozí je `admin` — **změňte po prvním přihlášení**. |
| `DOMAIN` | Ne | Vaše doména pro HTTPS. Ponechte prázdné pro pouze HTTP režim. |
| `LETSENCRYPT_EMAIL` | Ano (pokud je nastavena DOMAIN) | E-mail pro oznámení Let's Encrypt. |
| `EMBED_KEYCLOAK` | Ne | `true` pro nasazení vloženého Keycloak (vyžaduje 4 GB RAM). |

> **Bezpečnost:** Všechna hesla mají výchozí hodnotu `admin`. Změňte je ihned po prvním přihlášení.

---

## Krok 2 — Vytvořte instanci VM

V [Google Cloud Console](https://console.cloud.google.com/compute):

1. Klikněte na **Vytvořit instanci**
2. **Konfigurace stroje:**
   - Série: `E2`
   - Typ stroje: `e2-medium` (4 GB RAM) nebo větší
3. **Boot disk:**
   - Operační systém: Ubuntu
   - Verze: Ubuntu 22.04 LTS
   - Velikost: 40 GB nebo více
4. **Firewall:** zaškrtněte **Povolit HTTP provoz** a **Povolit HTTPS provoz**
5. **Pokročilé možnosti** → **Správa** → **Automatizace** → **Startup script** → vložte celý obsah skriptu
6. Klikněte na **Vytvořit**

---

## Krok 3 — Přidejte DNS záznam

Zatímco VM startuje, přidejte **A záznam** u vašeho poskytovatele DNS:

```
Typ  : A
Název: myapp
Hodnota: <vm-external-ip>
TTL  : 300
```

Najděte externí IP v seznamu VM instancí v konzoli.

---

## Krok 4 — Sledujte průběh

Pomocí CLI `gcloud`:

```bash
gcloud compute ssh <instance-name> -- tail -f /var/log/rtcloud-setup.log
```

Nebo přes SSH přímo:

```bash
ssh <username>@<vm-external-ip>
tail -f /var/log/rtcloud-setup.log
```

---

## Krok 5 — Přístup k aplikaci

Po dokončení nastavení protokol zobrazí souhrn s URL aplikace a přihlašovacími údaji. Přihlaste se uživatelským jménem `admin` a heslem `admin`, poté ihned změňte heslo.

---

## Pravidla firewallu

Zaškrtávací políčka GCP **Povolit HTTP/HTTPS** otevírají porty 80 a 443. Pro povolení přímého přístupu Shiny na portu 3838 přidejte pravidlo firewallu:

```bash
gcloud compute firewall-rules create allow-shiny \
  --allow tcp:3838 \
  --target-tags http-server
```

Nebo přidejte přes konzoli: **VPC Network** → **Firewall** → **Vytvořit pravidlo**.

> **Neotevírejte** port 3306 (MySQL) — nikdy by neměl být veřejně přístupný.

---

## Statická IP (volitelné)

GCP ve výchozím nastavení přiřazuje dočasnou externí IP, která se mění při restartu VM. Pro zachování stabilní IP:

1. Přejděte na **VPC Network** → **IP adresy**
2. Klikněte na **Rezervovat externí statickou adresu**
3. Přiřaďte ji vaší instanci VM

---

## Po nasazení

### Změna hesla

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Zobrazení všech kontejnerů

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```
