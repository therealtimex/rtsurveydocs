---
weight: 4
title: "Google Cloud (GCP)"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-16T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "travel_explore"
toc: true
description: "Distribuisci rtCloud su Google Cloud Compute Engine usando lo script di avvio gcp-compute.sh."
---

Usa `gcp-compute.sh` come **Script di avvio** quando crei un'istanza VM di Compute Engine. Lo script viene eseguito automaticamente al primo avvio.

**Scarica lo script:** [gcp-compute.sh](/scripts/gcp-compute.sh)

---

## Passaggio 1 — Compila la configurazione

Apri lo script e modifica il blocco `CONFIGURATION` nella parte superiore:

```bash
# --- Obbligatorio ---
PROJECT_ID="rtsurvey"
ADMIN_PASSWORD="admin"                       # Cambia dopo il primo accesso

# --- Dominio + SSL ---
DOMAIN="myapp.example.com"
LETSENCRYPT_EMAIL="admin@example.com"

# --- Keycloak integrato ---
EMBED_KEYCLOAK="true"
KEYCLOAK_ADMIN_PASSWORD="${ADMIN_PASSWORD}"  # Predefinito a ADMIN_PASSWORD
```

| Campo | Obbligatorio | Descrizione |
|-------|----------|-------------|
| `PROJECT_ID` | Sì | Usato come nome del database e ID client Keycloak. Minuscolo, senza spazi. |
| `ADMIN_PASSWORD` | No | Password admin dell'app e password admin Keycloak. Predefinito a `admin` — **cambia dopo il primo accesso**. |
| `DOMAIN` | No | Il tuo dominio per HTTPS. Lascia vuoto per la modalità solo HTTP. |
| `LETSENCRYPT_EMAIL` | Sì (se DOMAIN è impostato) | Email per le notifiche di Let's Encrypt. |
| `EMBED_KEYCLOAK` | No | `true` per distribuire Keycloak integrato (richiede 4 GB di RAM). |

> **Sicurezza:** Tutte le password hanno `admin` come valore predefinito. Cambiale immediatamente dopo il tuo primo accesso.

---

## Passaggio 2 — Crea un'istanza VM

Nella [Console Google Cloud](https://console.cloud.google.com/compute):

1. Fai clic su **Crea istanza**
2. **Configurazione macchina:**
   - Serie: `E2`
   - Tipo di macchina: `e2-medium` (4 GB RAM) o superiore
3. **Disco di avvio:**
   - Sistema operativo: Ubuntu
   - Versione: Ubuntu 22.04 LTS
   - Dimensione: 40 GB o più
4. **Firewall:** seleziona **Consenti traffico HTTP** e **Consenti traffico HTTPS**
5. **Opzioni avanzate** → **Gestione** → **Automazione** → **Script di avvio** → incolla il contenuto completo dello script
6. Fai clic su **Crea**

---

## Passaggio 3 — Aggiungi il record DNS

Mentre la VM si avvia, aggiungi un **record A** nel tuo provider DNS:

```
Tipo  : A
Nome  : myapp
Valore : <vm-external-ip>
TTL   : 300
```

Trova l'IP esterno nell'elenco delle istanze VM nella console.

---

## Passaggio 4 — Monitora l'avanzamento

Usando la CLI `gcloud`:

```bash
gcloud compute ssh <instance-name> -- tail -f /var/log/rtcloud-setup.log
```

O via SSH direttamente:

```bash
ssh <username>@<vm-external-ip>
tail -f /var/log/rtcloud-setup.log
```

---

## Passaggio 5 — Accedi all'app

Al completamento della configurazione, il log mostra un riepilogo con l'URL dell'app e le credenziali. Accedi con nome utente `admin` e password `admin`, poi cambia subito la tua password.

---

## Regole firewall

Le caselle di controllo **Consenti HTTP/HTTPS** di GCP aprono le porte 80 e 443. Per consentire anche l'accesso diretto a Shiny sulla porta 3838, aggiungi una regola firewall:

```bash
gcloud compute firewall-rules create allow-shiny \
  --allow tcp:3838 \
  --target-tags http-server
```

Oppure aggiungila tramite la console: **Rete VPC** → **Firewall** → **Crea regola**.

> **Non** aprire la porta 3306 (MySQL) — non deve mai essere accessibile pubblicamente.

---

## IP statico (opzionale)

Per impostazione predefinita, GCP assegna un IP esterno temporaneo che cambia al riavvio della VM. Per mantenere un IP stabile:

1. Vai su **Rete VPC** → **Indirizzi IP**
2. Fai clic su **Prenota indirizzo statico esterno**
3. Assegnalo alla tua istanza VM

---

## Dopo il deployment

### Cambiare una password

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Visualizza tutti i container

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```
