---
weight: 4
title: "Google Cloud (GCP)"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-16T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "travel_explore"
toc: true
description: "Primenite rtCloud na Google Cloud Compute Engine-u koristeći gcp-compute.sh startup skriptu."
---

Koristite `gcp-compute.sh` kao **Startup script** pri kreiranju Compute Engine VM instance. Skripta se automatski izvršava pri prvom pokretanju.

**Preuzmite skriptu:** [gcp-compute.sh](/scripts/gcp-compute.sh)

---

## Korak 1 — Popunite konfiguraciju

Otvorite skriptu i uredite blok `CONFIGURATION` na vrhu:

```bash
# --- Obavezno ---
PROJECT_ID="rtsurvey"
ADMIN_PASSWORD="admin"                       # Promenite nakon prve prijave

# --- Domen + SSL ---
DOMAIN="myapp.example.com"
LETSENCRYPT_EMAIL="admin@example.com"

# --- Ugrađeni Keycloak ---
EMBED_KEYCLOAK="true"
KEYCLOAK_ADMIN_PASSWORD="${ADMIN_PASSWORD}"  # Podrazumevano na ADMIN_PASSWORD
```

| Polje | Obavezno | Opis |
|-------|----------|------|
| `PROJECT_ID` | Da | Koristi se kao naziv baze podataka i Keycloak ID klijenta. Mala slova, bez razmaka. |
| `ADMIN_PASSWORD` | Ne | Lozinka administratora aplikacije i Keycloak administratora. Podrazumevano `admin` — **promenite nakon prve prijave**. |
| `DOMAIN` | Ne | Vaš domen za HTTPS. Ostavite prazno za HTTP-only režim. |
| `LETSENCRYPT_EMAIL` | Da (ako je DOMAIN postavljen) | Email za Let's Encrypt obaveštenja. |
| `EMBED_KEYCLOAK` | Ne | `true` da primenite ugrađeni Keycloak (zahteva 4 GB RAM). |

> **Bezbednost:** Sve lozinke su podrazumevano `admin`. Promenite ih odmah nakon prve prijave.

---

## Korak 2 — Kreirajte VM instancu

Na [Google Cloud konzoli](https://console.cloud.google.com/compute):

1. Kliknite **Kreiraj instancu**
2. **Konfiguracija mašine:**
   - Serija: `E2`
   - Tip mašine: `e2-medium` (4 GB RAM) ili veći
3. **Boot disk:**
   - Operativni sistem: Ubuntu
   - Verzija: Ubuntu 22.04 LTS
   - Veličina: 40 GB ili više
4. **Firewall:** označite **Dozvoli HTTP saobraćaj** i **Dozvoli HTTPS saobraćaj**
5. **Napredne opcije** → **Upravljanje** → **Automatizacija** → **Startup script** → nalepite kompletan sadržaj skripte
6. Kliknite **Kreiraj**

---

## Korak 3 — Dodajte DNS zapis

Dok se VM pokreće, dodajte **A zapis** kod vašeg DNS pružaoca:

```
Tip   : A
Ime   : myapp
Vrednost : <spoljna-ip-vm>
TTL   : 300
```

Pronađite spoljnu IP adresu na listi VM instanci u konzoli.

---

## Korak 4 — Pratite napredak

Koristeći `gcloud` CLI:

```bash
gcloud compute ssh <ime-instance> -- tail -f /var/log/rtcloud-setup.log
```

Ili se direktno SSH-ujte:

```bash
ssh <korisnicko-ime>@<spoljna-ip-vm>
tail -f /var/log/rtcloud-setup.log
```

---

## Korak 5 — Pristupite aplikaciji

Kada se podešavanje završi, evidencija prikazuje rezime sa URL-om vaše aplikacije i akreditivima. Prijavite se sa korisničkim imenom `admin` i lozinkom `admin`, zatim odmah promenite lozinku.

---

## Pravila firewall-a

GCP potvrdna polja **Dozvoli HTTP/HTTPS** otvaraju portove 80 i 443. Da biste takođe dozvolili direktan pristup Shiny-u na portu 3838, dodajte pravilo firewall-a:

```bash
gcloud compute firewall-rules create allow-shiny \
  --allow tcp:3838 \
  --target-tags http-server
```

Ili dodajte putem konzole: **VPC mreža** → **Firewall** → **Kreiraj pravilo**.

> **Ne** otvarajte port 3306 (MySQL) — nikada ne sme biti javno dostupan.

---

## Statična IP adresa (opciono)

Podrazumevano, GCP dodeljuje privremenu spoljnu IP adresu koja se menja pri ponovnom pokretanju VM-a. Da biste zadržali stabilnu IP adresu:

1. Idite na **VPC mreža** → **IP adrese**
2. Kliknite **Rezerviši spoljnu statičnu adresu**
3. Dodelite je vašoj VM instanci

---

## Nakon primene

### Promenite lozinku

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Pogledajte sve kontejnere

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```
