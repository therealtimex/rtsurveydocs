---
weight: 1
title: "DigitalOcean"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-17T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "water_drop"
toc: true
description: "Distribuisci rtCloud su un Droplet DigitalOcean usando script user-data automatizzati."
---

DigitalOcean usa script **User Data** che vengono eseguiti automaticamente al primo avvio. Compila le variabili di configurazione nella parte superiore dello script, poi incolla l'intero script durante la creazione di un Droplet.

> A differenza degli StackScript di Linode, DigitalOcean non ha un'interfaccia form — devi modificare lo script direttamente prima di incollarlo.

**Scarica lo script:** [digitalocean-droplet-keycloak-embed.sh](/scripts/digitalocean-droplet-keycloak-embed.sh)

---

## Keycloak integrato (consigliato)

Usa `digitalocean-droplet-keycloak-embed.sh` per la configurazione più semplice con SSO integrato.

### Passaggio 1 — Compila la configurazione

Apri lo script e modifica il blocco `CONFIGURATION` nella parte superiore:

```bash
# --- Obbligatorio ---
PROJECT_ID="rtsurvey"                  # Identificatore univoco per il tuo progetto (senza spazi)
ADMIN_PASSWORD="admin"                 # Password per l'admin dell'app e Keycloak — cambia dopo il primo accesso

# --- Dominio + SSL ---
DOMAIN="myapp.example.com"            # Il tuo dominio — il record A DNS deve puntare qui
PROJECT_URL=""                         # Lascia vuoto a meno che non sia dietro Cloudflare/proxy
LETSENCRYPT_EMAIL="admin@example.com" # Email per le notifiche di Let's Encrypt

# --- Opzionale ---
STATA_ENABLED="false"
TZ="Asia/Ho_Chi_Minh"
```

| Campo | Obbligatorio | Descrizione |
|-------|----------|-------------|
| `PROJECT_ID` | Sì | Usato come nome del database e ID client Keycloak. Minuscolo, senza spazi. |
| `ADMIN_PASSWORD` | No | Password per l'accesso admin dell'app e la console admin Keycloak. Predefinito a `admin` — **cambia dopo il primo accesso**. |
| `DOMAIN` | Sì | Il tuo nome di dominio. Il record A DNS deve puntare all'IP del Droplet. |
| `LETSENCRYPT_EMAIL` | Sì | Indirizzo email per le notifiche del certificato Let's Encrypt. |
| `PROJECT_URL` | No | Sovrascrive l'URL pubblico. Lascia vuoto per usare `DOMAIN`. Utile dietro Cloudflare. |

> **Sicurezza:** Tutte le password hanno `admin` come valore predefinito. Cambiale immediatamente dopo il tuo primo accesso.

### Passaggio 2 — Crea un Droplet

Nel [pannello di controllo DigitalOcean](https://cloud.digitalocean.com):

1. Fai clic su **Crea** → **Droplet**
2. Scegli **Ubuntu 22.04 LTS** come immagine
3. Seleziona **Basic, 4 GB RAM / 2 vCPU** o superiore
4. Scorri fino a **Opzioni avanzate** → seleziona **Aggiungi script di inizializzazione**
5. Incolla il contenuto completo dello script nell'area di testo
6. Fai clic su **Crea Droplet**

### Passaggio 3 — Aggiungi il record DNS

Mentre il Droplet si avvia, aggiungi un **record A** nel tuo provider DNS:

```
Tipo  : A
Nome  : myapp          (o @ per il dominio root)
Valore : <droplet-ip>
TTL   : 300
```

### Passaggio 4 — Monitora l'avanzamento

Accedi al Droplet via SSH e guarda il log:

```bash
ssh root@<droplet-ip>
tail -f /var/log/rtcloud-setup.log
```

Lo script stampa l'IP del tuo server all'inizio — aggiungi il record DNS non appena lo vedi.

### Passaggio 5 — Accedi all'app

Al completamento della configurazione, il log mostra un riepilogo:

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

Apri `https://myapp.example.com` nel tuo browser e accedi con nome utente `admin` e password `admin`.

> **Cambia la tua password** immediatamente dopo l'accesso tramite **Impostazioni** nel menu in alto a destra.

---

## Dopo il deployment

### Cambiare una password

Accedi al Droplet via SSH, modifica `.env` e riavvia il container interessato:

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Aggiornare il dominio

Se assegni un dominio diverso dopo il deployment, aggiorna `PROJECT_URL` in `.env`:

```bash
nano /opt/rtcloud/.env   # aggiorna PROJECT_URL=
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Visualizza tutti i container

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```
