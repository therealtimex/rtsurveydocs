---
weight: 5
title: "Manutenzione"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "build"
toc: true
description: "Manutenzione quotidiana per un'istanza rtCloud self-hosted: aggiornamento, backup, ripristino e risoluzione dei problemi comuni."
---

## Comandi comuni

Usa questi comandi regolarmente per gestire i tuoi container rtCloud. Eseguili dalla directory contenente `docker-compose.production.yml`.

```bash
# Controlla lo stato e la salute di tutti i container
docker compose -f docker-compose.production.yml ps

# Visualizza i log in tempo reale (tutti i servizi)
docker compose -f docker-compose.production.yml logs -f

# Visualizza i log solo per l'app
docker compose -f docker-compose.production.yml logs -f rtcloud

# Riavvia un singolo container
docker compose -f docker-compose.production.yml restart rtcloud

# Ferma tutti i servizi
docker compose -f docker-compose.production.yml down

# Avvia tutti i servizi
docker compose -f docker-compose.production.yml up -d

# Apri una shell all'interno del container dell'app
docker compose -f docker-compose.production.yml exec rtcloud bash
```

---

## Aggiornamento

Gli aggiornamenti di rtCloud vengono distribuiti come nuovi tag di immagine Docker. L'aggiornamento scarica l'ultima immagine e ricrea il container dell'app. Le migrazioni del database vengono eseguite automaticamente all'avvio.

**1. Scarica l'ultima immagine:**

```bash
docker compose -f docker-compose.production.yml pull
```

**2. Ricrea il container dell'app:**

```bash
docker compose -f docker-compose.production.yml up -d
```

Docker sostituisce solo i container la cui immagine è cambiata. Il container MySQL e tutti i volumi nominati non vengono modificati.

### Fissare una versione

Per aggiornare a una versione specifica invece che a `latest`, aggiorna `RTCLOUD_IMAGE` in `.env`:

```dotenv
RTCLOUD_IMAGE=rtawebteam/rta-smartsurvey:1.2.3
```

Poi esegui `docker compose pull` e `up -d` come sopra.

### Downgrade

Il downgrade non è generalmente consigliato, poiché le migrazioni del database non possono essere invertite. Se è necessario un downgrade, ripristina da un backup del database eseguito prima dell'aggiornamento.

---

## Backup e ripristino

### Backup del database

Esegui questo comando per esportare il database dell'applicazione in un file SQL:

```bash
docker compose -f docker-compose.production.yml exec mysql \
  mysqldump -u root -p"$(grep MYSQL_ROOT_PASSWORD .env | cut -d= -f2)" smartsurvey \
  > backup-$(date +%Y%m%d-%H%M%S).sql
```

Il file di backup viene scritto nella tua directory corrente sull'host.

### Ripristino del database

```bash
docker compose -f docker-compose.production.yml exec -T mysql \
  mysql -u root -p"$(grep MYSQL_ROOT_PASSWORD .env | cut -d= -f2)" smartsurvey \
  < backup-20240101-120000.sql
```

### Backup dei file caricati

Le risposte al sondaggio spesso includono file caricati (foto, audio, documenti) archiviati in volumi Docker nominati. Esegui il backup separatamente dal database:

```bash
# Backup uploads
docker run --rm \
  -v rtcloud_uploads:/data \
  -v "$(pwd):/backup" \
  alpine tar czf /backup/uploads-$(date +%Y%m%d).tar.gz -C /data .

# Backup registrazioni audio
docker run --rm \
  -v rtcloud_audios:/data \
  -v "$(pwd):/backup" \
  alpine tar czf /backup/audios-$(date +%Y%m%d).tar.gz -C /data .
```

Sostituisci `rtcloud_uploads` e `rtcloud_audios` con i tuoi nomi di volume effettivi (preceduti da `COMPOSE_PROJECT_NAME`) se hai cambiato il valore predefinito.

### Ripristino dei file caricati

```bash
docker run --rm \
  -v rtcloud_uploads:/data \
  -v "$(pwd):/backup" \
  alpine tar xzf /backup/uploads-20240101.tar.gz -C /data
```

### Backup giornalieri automatizzati

Aggiungi un cron job sull'host per eseguire i backup automaticamente. Modifica il crontab root con `crontab -e`:

```cron
# Backup giornaliero del database alle 2:00, conserva 30 giorni di cronologia
0 2 * * * cd /opt/rtcloud && docker compose -f docker-compose.production.yml exec -T mysql \
  mysqldump -u root -p"$(grep MYSQL_ROOT_PASSWORD .env | cut -d= -f2)" smartsurvey \
  > /backups/db-$(date +\%Y\%m\%d).sql && \
  find /backups -name "db-*.sql" -mtime +30 -delete
```

---

## Risoluzione dei problemi

### Il container dell'app non si avvia

Controlla i log del container per i messaggi di errore:

```bash
docker compose -f docker-compose.production.yml logs rtcloud
```

Cause comuni:
- Variabili d'ambiente mancanti o non valide in `.env`
- MySQL non ancora pronto (attendi 60 secondi e ricontrolla)
- Conflitto di porta — un altro processo sta già usando `APP_PORT`

### MySQL non è in salute

```bash
docker compose -f docker-compose.production.yml logs mysql
```

Cause comuni:
- `MYSQL_ROOT_PASSWORD` non impostato in `.env`
- Volume dati corrotto (raro — controlla lo spazio su disco con `df -h`)

MySQL può richiedere 30–60 secondi per inizializzarsi al primo avvio. Attendi e ricontrolla prima di presumere un fallimento.

### Porta già in uso

Cambia `APP_PORT` o `SHINY_PORT` in `.env` con una porta libera, poi ricrea i container:

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate
```

Per trovare cosa sta usando una porta sull'host:

```bash
lsof -i :8080
```

### 400 Token CSRF non verificato

Questo errore appare in ambienti locali o reverse-proxy dove l'origine della richiesta non corrisponde all'host previsto. Disabilita la validazione CSRF solo per lo sviluppo locale:

```dotenv
CSRF_VALIDATION_ENABLED=false
```

Poi riavvia l'app:

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

> Non disabilitare la validazione CSRF in produzione. Se questo errore si verifica in produzione, assicurati che il tuo reverse proxy stia trasmettendo gli header `Host` e `X-Forwarded-For` corretti.

### Password di amministratore dimenticata

Reimposta la password di amministratore direttamente nel database. Connettiti al container MySQL e aggiorna l'hash della password:

**Passaggio 1** — Genera il nuovo hash della password. Sostituisci `newpassword` con la password desiderata:

```bash
docker compose -f docker-compose.production.yml exec rtcloud php -r "
  \$salt = trim(shell_exec(\"mysql -h mysql -u root -p\\\"\${MYSQL_ROOT_PASSWORD}\\\" \${MYSQL_DATABASE} -se \\\"SELECT salt FROM ss_user WHERE username='admin';\\\"\"));
  echo md5(\$salt . 'newpassword') . PHP_EOL;
"
```

**Passaggio 2** — Aggiorna l'hash nel database:

```bash
docker compose -f docker-compose.production.yml exec mysql \
  mysql -u root -p"${MYSQL_ROOT_PASSWORD}" smartsurvey \
  -e "UPDATE ss_user SET password='<hash_from_step_1>' WHERE username='admin';"
```

### Il container continua a riavviarsi

Controlla se il controllo di salute sta fallendo:

```bash
docker compose -f docker-compose.production.yml ps
docker inspect rtcloud-app --format '{{json .State.Health}}'
```

Il controllo di salute dell'app chiama l'endpoint `/health`. Se fallisce ripetutamente, controlla i log dell'applicazione per gli errori di avvio.

### Spazio su disco esaurito

Identifica cosa sta consumando spazio:

```bash
# Controlla l'utilizzo del disco dell'host
df -h

# Controlla l'utilizzo del disco Docker (immagini, container, volumi)
docker system df

# Rimuovi immagini non utilizzate e container fermati (sicuro da eseguire)
docker system prune
```

Non usare `docker system prune --volumes` poiché questo eliminerà i dati dell'applicazione.

---

## Controlli di salute

Ogni servizio ha un controllo di salute automatico. Lo stato del container riflette il risultato:

| Container | Metodo di controllo | Periodo iniziale | Intervallo |
|-----------|-------------|-------------|----------|
| `rtcloud-app` | HTTP GET `/health` | 90 secondi | 30 secondi |
| `rtcloud-mysql` | `mysqladmin ping` | 30 secondi | 10 secondi |
| `rtcloud-keycloak` | HTTP GET `:9000/health/live` | 120 secondi | 30 secondi |

I container con un controllo di salute fallito vengono riavviati automaticamente in base all'impostazione `RESTART_POLICY` (predefinito: `unless-stopped`).
