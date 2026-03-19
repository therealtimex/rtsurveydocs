---
weight: 1
title: "Avvio rapido"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "play_circle"
toc: true
description: "Metti in funzione rtCloud sul tuo server in meno di 10 minuti usando Docker Compose."
---

Questa guida ti accompagna nel deployment di un'istanza rtCloud self-hosted su un server Linux da zero. Al termine, avrai un rtCloud funzionante accessibile dal tuo browser.

## Prerequisiti

Assicurati che il tuo server soddisfi i seguenti requisiti prima di iniziare:

### Hardware

| Risorsa | Minimo | Consigliato |
|----------|---------|-------------|
| RAM | 2 GB | 4 GB |
| Disco | 10 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPU |

### Software

| Software | Versione |
|----------|---------|
| OS | Ubuntu 20.04 LTS o più recente (o qualsiasi Linux con supporto Docker) |
| Docker | 20.10 o più recente |
| Docker Compose | v2.x (`docker compose`) o v1.x (`docker-compose`) |

**Installa Docker su Ubuntu:**

```bash
curl -fsSL https://get.docker.com | sh
```

Verifica l'installazione:

```bash
docker --version
docker compose version
```

---

## Passaggio 1 — Ottieni i file

Clona il repository di deployment sul tuo server:

```bash
git clone ssh://git@rtgit.rta.vn:2224/rtlab/rtwebteam/rta-smart-survey-docker.git rtcloud
cd rtcloud
```

---

## Passaggio 2 — Configura l'ambiente

Copia il file di configurazione di esempio:

```bash
cp .env.production.sample .env
```

Apri `.env` in un editor di testo e compila i valori richiesti:

```dotenv
# Identificatore univoco per questo deployment (senza spazi, senza caratteri speciali)
PROJECT_ID=myproject

# Dominio o indirizzo IP dove gli utenti accederanno all'app
# Esempio: rtcloud.example.com  o  192.168.1.100
PROJECT_URL=rtcloud.example.com

# Protocollo: usa "https" se hai un dominio con SSL, "http" altrimenti
HTTP_PROTOCOL=https

# Password forti e uniche — cambia tutte e tre prima di avviare
MYSQL_PASSWORD=change_me_strong_password
MYSQL_ROOT_PASSWORD=change_me_root_password
ADMIN_PASSWORD=change_me_admin_password
```

> **Importante:** Solo `.env` viene letto automaticamente da Docker Compose. Non creare un file denominato `.env.production`, poiché causerebbe confusione. L'`ADMIN_PASSWORD` viene applicata solo al **primo avvio** di un database nuovo.

---

## Passaggio 3 — Avvia i container

Avvia tutti i servizi in background:

```bash
docker compose -f docker-compose.production.yml up -d
```

Il primo avvio richiede **3–5 minuti** mentre Docker:

1. Scarica l'immagine dell'applicazione rtCloud (~1 GB di download)
2. Inizializza il database MySQL
3. Carica lo schema di base
4. Esegue tutte le migrazioni del database in sospeso

Monitora l'avanzamento dell'avvio in tempo reale:

```bash
docker compose -f docker-compose.production.yml logs -f rtcloud
```

Attendi finché non vedi l'output che indica che l'applicazione è pronta. Puoi anche monitorare lo stato di salute del container:

```bash
watch docker compose -f docker-compose.production.yml ps
```

---

## Passaggio 4 — Accedi all'applicazione

Una volta che entrambi i container mostrano `Up (healthy)`, apri il tuo browser:

```
http://<PROJECT_URL>:8080
```

Accedi usando l'account amministratore:

| Campo | Valore |
|-------|-------|
| Nome utente | `admin` |
| Password | Il valore impostato per `ADMIN_PASSWORD` in `.env` |

> Cambia la password di amministratore immediatamente dopo il primo accesso dalla pagina delle impostazioni account.

---

## Passaggio 5 — Verifica tutti i servizi

Controlla che tutti i container siano in esecuzione e in buona salute:

```bash
docker compose -f docker-compose.production.yml ps
```

Output atteso:

```
NAME                    IMAGE                                   STATUS
rtcloud-app             rtawebteam/rta-smartsurvey:...          Up (healthy)
rtcloud-mysql           mysql:8.0                               Up (healthy)
```

Se un container mostra `Up (starting)` o `Up (unhealthy)`, attendi altri 30–60 secondi e ricontrolla. MySQL può richiedere fino a un minuto per inizializzarsi completamente al primo avvio.

---

## Riferimento porte

| Porta | Servizio | Descrizione |
|------|---------|-------------|
| `8080` | rtCloud App | Interfaccia web principale (configurabile tramite `APP_PORT`) |
| `3838` | Shiny Server | Analisi e visualizzazioni basate su R (configurabile tramite `SHINY_PORT`) |

MySQL (porta 3306) e qualsiasi servizio opzionale (Keycloak) sono solo interni e non esposti all'host per impostazione predefinita.

---

## Passaggi successivi

La tua istanza rtCloud è ora in esecuzione. Considera queste attività di follow-up:

- **Abilita HTTPS** — Punta un dominio al tuo server e configura SSL con Let's Encrypt. Vedi [Deployment su cloud](cloud-deployment) per la configurazione HTTPS automatizzata.
- **Rivedi tutte le impostazioni** — Sfoglia il [Riferimento configurazione](configuration) per ottimizzare il tuo deployment per la produzione.
- **Configura SSO** — Connetti un provider di identità per l'autenticazione centralizzata degli utenti. Vedi [Autenticazione SSO](sso-authentication).
- **Pianifica i backup** — Consulta la pagina [Manutenzione](maintenance) per le procedure di backup e aggiornamento.
