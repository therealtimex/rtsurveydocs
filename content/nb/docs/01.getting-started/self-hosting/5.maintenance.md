---
weight: 5
title: "Vedlikehold"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "build"
toc: true
description: "Daglig vedlikehold for en selvdriftet rtCloud-instans: oppgradering, sikkerhetskopiering, gjenoppretting og feilsøking av vanlige problemer."
---

## Vanlige kommandoer

Bruk disse kommandoene jevnlig for å administrere rtCloud-containerne. Kjør dem fra katalogen som inneholder `docker-compose.production.yml`.

```bash
# Sjekk status og helse for alle containere
docker compose -f docker-compose.production.yml ps

# Se direktelogger (alle tjenester)
docker compose -f docker-compose.production.yml logs -f

# Se logger kun for appen
docker compose -f docker-compose.production.yml logs -f rtcloud

# Start en enkelt container på nytt
docker compose -f docker-compose.production.yml restart rtcloud

# Stopp alle tjenester
docker compose -f docker-compose.production.yml down

# Start alle tjenester
docker compose -f docker-compose.production.yml up -d

# Åpne et skall inne i app-containeren
docker compose -f docker-compose.production.yml exec rtcloud bash
```

---

## Oppgradering

rtCloud-oppdateringer distribueres som nye Docker-bildekoder. Oppgradering henter det nyeste bildet og gjenskaper app-containeren. Databasemigrasjoner kjøres automatisk ved oppstart.

**1. Hent det nyeste bildet:**

```bash
docker compose -f docker-compose.production.yml pull
```

**2. Gjenskapapp-containeren:**

```bash
docker compose -f docker-compose.production.yml up -d
```

Docker erstatter kun containere hvis bilde har endret seg. MySQL-containeren og alle navngitte volumer er upåvirket.

### Feste en versjon

For å oppgradere til en spesifikk versjon i stedet for `latest`, oppdater `RTCLOUD_IMAGE` i `.env`:

```dotenv
RTCLOUD_IMAGE=rtawebteam/rta-smartsurvey:1.2.3
```

Kjør deretter `docker compose pull` og `up -d` som ovenfor.

### Nedgradering

Nedgradering anbefales generelt ikke, siden databasemigrasjoner ikke kan reverseres. Hvis en nedgradering er nødvendig, gjenopprett fra en database-sikkerhetskopi tatt før oppgraderingen.

---

## Sikkerhetskopiering og gjenoppretting

### Sikkerhetskopier databasen

Kjør denne kommandoen for å eksportere applikasjonsdatabasen til en SQL-fil:

```bash
docker compose -f docker-compose.production.yml exec mysql \
  mysqldump -u root -p"$(grep MYSQL_ROOT_PASSWORD .env | cut -d= -f2)" smartsurvey \
  > backup-$(date +%Y%m%d-%H%M%S).sql
```

Sikkerhetskopifilen skrives til gjeldende katalog på verten.

### Gjenopprett databasen

```bash
docker compose -f docker-compose.production.yml exec -T mysql \
  mysql -u root -p"$(grep MYSQL_ROOT_PASSWORD .env | cut -d= -f2)" smartsurvey \
  < backup-20240101-120000.sql
```

### Sikkerhetskopier opplastede filer

Undersøkelsesinnsendinger inkluderer ofte opplastede filer (bilder, lyd, dokumenter) lagret i navngitte Docker-volumer. Sikkerhetskopier dem separat fra databasen:

```bash
# Sikkerhetskopier opplastinger
docker run --rm \
  -v rtcloud_uploads:/data \
  -v "$(pwd):/backup" \
  alpine tar czf /backup/uploads-$(date +%Y%m%d).tar.gz -C /data .

# Sikkerhetskopier lydopptak
docker run --rm \
  -v rtcloud_audios:/data \
  -v "$(pwd):/backup" \
  alpine tar czf /backup/audios-$(date +%Y%m%d).tar.gz -C /data .
```

Erstatt `rtcloud_uploads` og `rtcloud_audios` med dine faktiske volumnavn (prefikset av `COMPOSE_PROJECT_NAME`) hvis du endret standarden.

### Gjenopprett opplastede filer

```bash
docker run --rm \
  -v rtcloud_uploads:/data \
  -v "$(pwd):/backup" \
  alpine tar xzf /backup/uploads-20240101.tar.gz -C /data
```

### Automatiserte daglige sikkerhetskopier

Legg til en cron-jobb på verten for å kjøre sikkerhetskopier automatisk. Rediger root crontab med `crontab -e`:

```cron
# Daglig database-sikkerhetskopiering kl. 02:00, behold 30 dagers historikk
0 2 * * * cd /opt/rtcloud && docker compose -f docker-compose.production.yml exec -T mysql \
  mysqldump -u root -p"$(grep MYSQL_ROOT_PASSWORD .env | cut -d= -f2)" smartsurvey \
  > /backups/db-$(date +\%Y\%m\%d).sql && \
  find /backups -name "db-*.sql" -mtime +30 -delete
```

---

## Feilsøking

### App-container starter ikke

Sjekk containerloggene for feilmeldinger:

```bash
docker compose -f docker-compose.production.yml logs rtcloud
```

Vanlige årsaker:
- Manglende eller ugyldige miljøvariabler i `.env`
- MySQL ikke klar ennå (vent 60 sekunder og sjekk igjen)
- Portkonflik — en annen prosess bruker allerede `APP_PORT`

### MySQL ikke sunn

```bash
docker compose -f docker-compose.production.yml logs mysql
```

Vanlige årsaker:
- `MYSQL_ROOT_PASSWORD` ikke angitt i `.env`
- Skadet datavolum (sjeldent — sjekk diskplass med `df -h`)

MySQL kan ta 30–60 sekunder å initialisere ved aller første oppstart. Vent og sjekk igjen før du antar feil.

### Port allerede i bruk

Endre `APP_PORT` eller `SHINY_PORT` i `.env` til en ledig port, og gjenskapcontainerne:

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate
```

For å finne hva som bruker en port på verten:

```bash
lsof -i :8080
```

### 400 CSRF Token Could Not Be Verified

Denne feilen vises i lokale eller omvendt-proxy-miljøer der forespørselsopphavet ikke samsvarer med forventet vert. Deaktiver CSRF-validering kun for lokal utvikling:

```dotenv
CSRF_VALIDATION_ENABLED=false
```

Start deretter appen på nytt:

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

> Ikke deaktiver CSRF-validering i produksjon. Hvis denne feilen oppstår i produksjon, kontroller at den omvendte proxyen videresender riktige `Host`- og `X-Forwarded-For`-hoder.

### Glemt adminpassordet

Tilbakestill adminpassordet direkte i databasen. Koble til MySQL-containeren og oppdater passord-hashen:

**Trinn 1** — Generer den nye passord-hashen. Erstatt `newpassword` med ønsket passord:

```bash
docker compose -f docker-compose.production.yml exec rtcloud php -r "
  \$salt = trim(shell_exec(\"mysql -h mysql -u root -p\\\"\${MYSQL_ROOT_PASSWORD}\\\" \${MYSQL_DATABASE} -se \\\"SELECT salt FROM ss_user WHERE username='admin';\\\"\")); 
  echo md5(\$salt . 'newpassword') . PHP_EOL;
"
```

**Trinn 2** — Oppdater hashen i databasen:

```bash
docker compose -f docker-compose.production.yml exec mysql \
  mysql -u root -p"${MYSQL_ROOT_PASSWORD}" smartsurvey \
  -e "UPDATE ss_user SET password='<hash_fra_trinn_1>' WHERE username='admin';"
```

### Container fortsetter å starte på nytt

Sjekk om helsesjekken mislykkes:

```bash
docker compose -f docker-compose.production.yml ps
docker inspect rtcloud-app --format '{{json .State.Health}}'
```

App-helsesjekken kaller `/health`-endepunktet. Hvis den mislykkes gjentatte ganger, sjekk applikasjonsloggene for oppstartsfeil.

### Disk full

Identifiser hva som forbruker plass:

```bash
# Sjekk vertsdiskbruk
df -h

# Sjekk Docker-diskbruk (bilder, containere, volumer)
docker system df

# Fjern ubrukte bilder og stoppede containere (trygt å kjøre)
docker system prune
```

Ikke bruk `docker system prune --volumes`, da dette vil slette applikasjonsdata.

---

## Helsesjekker

Hver tjeneste har en automatisk helsesjekk. Containerstatus gjenspeiler resultatet:

| Container | Sjekkmetode | Startperiode | Intervall |
|-----------|-------------|-------------|----------|
| `rtcloud-app` | HTTP GET `/health` | 90 sekunder | 30 sekunder |
| `rtcloud-mysql` | `mysqladmin ping` | 30 sekunder | 10 sekunder |
| `rtcloud-keycloak` | HTTP GET `:9000/health/live` | 120 sekunder | 30 sekunder |

Containere med en mislykket helsesjekk startes automatisk på nytt i henhold til `RESTART_POLICY`-innstillingen (standard: `unless-stopped`).
