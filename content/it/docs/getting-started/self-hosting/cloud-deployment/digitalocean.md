---
weight: 1
title: "DigitalOcean"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-17T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "water_drop"
toc: true
description: "Distribuisci rtCloud su una droplet DigitalOcean utilizzando script automatizzati di dati utente."
---

DigitalOcean utilizza script **Dati utente** che vengono eseguiti automaticamente al primo avvio. Compila le variabili di configurazione nella parte superiore dello script, quindi incolla l'intero script durante la creazione di un Droplet.

> A differenza di Linode StackScripts, DigitalOcean non ha un'interfaccia utente del modulo: devi modificare lo script direttamente prima di incollarlo.

**Download script:** [digitalocean-droplet-keycloak-embed.sh](/scripts/digitalocean-droplet-keycloak-embed.sh)

---

## Keycloak incorporato (consigliato)

Utilizza `digitalocean-droplet-keycloak-embed.sh` per la configurazione più semplice con SSO integrato.

### Passaggio 1: compila la configurazione

Apri lo script e modifica il blocco "CONFIGURAZIONE" in alto:

```bash
# --- Required ---
PROJECT_ID="rtsurvey"                  # Unique identifier for your project (no spaces)
ADMIN_PASSWORD="admin"                 # Password for app admin and Keycloak — change after first login

# --- Domain + SSL ---
DOMAIN="myapp.example.com"            # Your domain — DNS A record must point here
PROJECT_URL=""                         # Leave blank unless behind Cloudflare/proxy
LETSENCRYPT_EMAIL="admin@example.com" # Email for Let's Encrypt notifications

# --- Optional ---
STATA_ENABLED="false"
TZ="Asia/Ho_Chi_Minh"
```

| Campo | Obbligatorio | Descrizione |
|-------|----------|-------------|
| `ID_PROGETTO` | Sì | Utilizzato come nome del database e ID client Keycloak. Minuscolo, senza spazi. |
| `PASSWORD_ADMIN` | No | Password per l'accesso all'amministratore dell'app e alla console di amministrazione Keycloak. Il valore predefinito è "admin" — **cambia dopo il primo accesso**. |
| `DOMINIO` | Sì | Il tuo nome di dominio. Il record DNS A deve puntare all'IP del Droplet. |
| `LETSENCRYPT_EMAIL` | Sì | Indirizzo e-mail per le notifiche dei certificati Let's Encrypt. |
| `URL_PROGETTO` | No | Sostituisci l'URL pubblico. Lascia vuoto per utilizzare "DOMINIO". Utile dietro Cloudflare. |

> **Sicurezza:** tutte le password sono impostate su "admin". Modificateli immediatamente dopo il primo accesso.

### Passaggio 2: crea una goccia

In the [DigitalOcean control panel](https://cloud.digitalocean.com):

1. Fare clic su **Crea** → **Droplet**
2. Scegli **Ubuntu 22.04 LTS** come immagine
3. Seleziona **Base, 4 GB RAM / 2 vCPU** o superiore
4. Scorri fino a **Opzioni avanzate** → seleziona **Aggiungi script di inizializzazione**
5. Incolla il contenuto completo dello script nell'area di testo
6. Fai clic su **Crea droplet**

### Passaggio 3: aggiungi il record DNS

Durante l'avvio del Droplet, aggiungi un **record A** nel tuo provider DNS:

```
Type  : A
Name  : myapp          (or @ for root domain)
Value : <droplet-ip>
TTL   : 300
```

### Passaggio 4: monitorare i progressi

SSH nel Droplet e guarda il registro:

```bash
ssh root@<droplet-ip>
tail -f /var/log/rtcloud-setup.log
```

Lo script stampa l'IP del tuo server all'inizio: aggiungi il record DNS non appena lo vedi.

### Passaggio 5: accedi all'app

Al termine della configurazione, il registro mostra un riepilogo:

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

Open `https://myapp.example.com` in your browser and log in with username `admin` and password `admin`.

> **Cambia la tua password** subito dopo aver effettuato l'accesso tramite **Impostazioni** nel menu in alto a destra.

---

## Dopo la distribuzione

### Cambia una password

SSH nel Droplet, modifica `.env` e riavvia il contenitore interessato:

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Aggiorna il dominio

Se assegni un dominio diverso dopo la distribuzione, aggiorna `PROJECT_URL` in `.env`:

```bash
nano /opt/rtcloud/.env   # update PROJECT_URL=
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Visualizza tutti i contenitori

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```
