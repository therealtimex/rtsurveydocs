---
weight: 5
title: "Underhåll"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "build"
toc: true
description: "Dagligt underhåll för en självhostad rtCloud-instans: uppgradering, säkerhetskopiering, återställning och felsökning av vanliga problem."
---

## Vanliga kommandon

Använd dessa kommandon regelbundet för att hantera dina rtCloud-containrar. Kör dem från katalogen som innehåller `docker-compose.production.yml`.

```bash
# Kontrollera status och hälsa för alla containrar
docker compose -f docker-compose.production.yml ps

# Visa liveloggar (alla tjänster)
docker compose -f docker-compose.production.yml logs -f

# Visa loggar för enbart appen
docker compose -f docker-compose.production.yml logs -f rtcloud

# Starta om en enstaka container
docker compose -f docker-compose.production.yml restart rtcloud

# Stoppa alla tjänster
docker compose -f docker-compose.production.yml down

# Starta alla tjänster
docker compose -f docker-compose.production.yml up -d

# Öppna ett skal inuti appcontainern
docker compose -f docker-compose.production.yml exec rtcloud bash
```

---

## Uppgradering

rtCloud-uppdateringar distribueras som nya Docker-avbildstaggar. Uppgradering hämtar den senaste avbilden och återskapar appcontainern. Databasmigrationer körs automatiskt vid start.

**1. Hämta den senaste avbilden:**

```bash
docker compose -f docker-compose.production.yml pull
```

**2. Återskapa appcontainern:**

```bash
docker compose -f docker-compose.production.yml up -d
```

Docker ersätter bara containrarna vars avbild har ändrats. MySQL-containern och alla namngivna volymer påverkas inte.

### Fästa en version

För att uppgradera till en specifik version istället för `latest`, uppdatera `RTCLOUD_IMAGE` i `.env`:

```dotenv
RTCLOUD_IMAGE=rtawebteam/rta-smartsurvey:1.2.3
```

Kör sedan `docker compose pull` och `up -d` som ovan.

### Nedgradering

Nedgradering rekommenderas generellt inte, eftersom databasmigrationer inte kan återställas. Om en nedgradering är nödvändig, återställ från en databassäkerhetskopia tagen före uppgraderingen.

---

## Säkerhetskopiering och återställning

### Säkerhetskopiera databasen

Kör detta kommando för att exportera applikationsdatabasen till en SQL-fil:

```bash
docker compose -f docker-compose.production.yml exec mysql \
  mysqldump -u root -p"$(grep MYSQL_ROOT_PASSWORD .env | cut -d= -f2)" smartsurvey \
  > backup-$(date +%Y%m%d-%H%M%S).sql
```

Säkerhetskopian skrivs till din aktuella katalog på värden.

### Återställa databasen

```bash
docker compose -f docker-compose.production.yml exec -T mysql \
  mysql -u root -p"$(grep MYSQL_ROOT_PASSWORD .env | cut -d= -f2)" smartsurvey \
  < backup-20240101-120000.sql
```

### Säkerhetskopiera uppladdade filer

Undersökningsinlämningar inkluderar ofta uppladdade filer (foton, ljud, dokument) lagrade i namngivna Docker-volymer. Säkerhetskopiera dem separat från databasen:

```bash
# Säkerhetskopiera uppladdningar
docker run --rm \
  -v rtcloud_uploads:/data \
  -v "$(pwd):/backup" \
  alpine tar czf /backup/uploads-$(date +%Y%m%d).tar.gz -C /data .

# Säkerhetskopiera ljudinspelningar
docker run --rm \
  -v rtcloud_audios:/data \
  -v "$(pwd):/backup" \
  alpine tar czf /backup/audios-$(date +%Y%m%d).tar.gz -C /data .
```

Ersätt `rtcloud_uploads` och `rtcloud_audios` med dina faktiska volymnamn (prefixade med `COMPOSE_PROJECT_NAME`) om du ändrade standardvärdet.

### Återställa uppladdade filer

```bash
docker run --rm \
  -v rtcloud_uploads:/data \
  -v "$(pwd):/backup" \
  alpine tar xzf /backup/uploads-20240101.tar.gz -C /data
```

### Automatiserade dagliga säkerhetskopior

Lägg till ett cron-jobb på värden för att köra säkerhetskopior automatiskt. Redigera root-crontab med `crontab -e`:

```cron
# Daglig databassäkerhetskopiering kl. 02:00, behåll 30 dagars historik
0 2 * * * cd /opt/rtcloud && docker compose -f docker-compose.production.yml exec -T mysql \
  mysqldump -u root -p"$(grep MYSQL_ROOT_PASSWORD .env | cut -d= -f2)" smartsurvey \
  > /backups/db-$(date +\%Y\%m\%d).sql && \
  find /backups -name "db-*.sql" -mtime +30 -delete
```

---

## Felsökning

### Appcontainern startar inte

Kontrollera containerloggarna för felmeddelanden:

```bash
docker compose -f docker-compose.production.yml logs rtcloud
```

Vanliga orsaker:
- Saknade eller ogiltiga miljövariabler i `.env`
- MySQL är inte redo ännu (vänta 60 sekunder och kontrollera igen)
- Portkollision — en annan process använder redan `APP_PORT`

### MySQL är inte frisk

```bash
docker compose -f docker-compose.production.yml logs mysql
```

Vanliga orsaker:
- `MYSQL_ROOT_PASSWORD` är inte angett i `.env`
- Skadad datavolym (sällsynt — kontrollera diskutrymme med `df -h`)

MySQL kan ta 30–60 sekunder att initialisera vid allra första starten. Vänta och kontrollera igen innan du antar att det är ett fel.

### Porten används redan

Ändra `APP_PORT` eller `SHINY_PORT` i `.env` till en ledig port och återskapa sedan containrarna:

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate
```

För att hitta vad som använder en port på värden:

```bash
lsof -i :8080
```

### 400 CSRF-token kunde inte verifieras

Det här felet uppstår i lokala eller omvänd proxy-miljöer där begärans ursprung inte matchar den förväntade värden. Inaktivera CSRF-validering enbart för lokal utveckling:

```dotenv
CSRF_VALIDATION_ENABLED=false
```

Starta sedan om appen:

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

> Inaktivera inte CSRF-validering i produktion. Om det här felet uppstår i produktion, se till att din omvända proxy vidarebefordrar korrekta `Host`- och `X-Forwarded-For`-huvuden.

### Glömt adminlösenordet

Återställ adminlösenordet direkt i databasen. Anslut till MySQL-containern och uppdatera lösenordshash:

**Steg 1** — Generera den nya lösenordshash. Ersätt `nyttlösenord` med ditt önskade lösenord:

```bash
docker compose -f docker-compose.production.yml exec rtcloud php -r "
  \$salt = trim(shell_exec(\"mysql -h mysql -u root -p\\\"\${MYSQL_ROOT_PASSWORD}\\\" \${MYSQL_DATABASE} -se \\\"SELECT salt FROM ss_user WHERE username='admin';\\\"\"));
  echo md5(\$salt . 'nyttlösenord') . PHP_EOL;
"
```

**Steg 2** — Uppdatera hashen i databasen:

```bash
docker compose -f docker-compose.production.yml exec mysql \
  mysql -u root -p"${MYSQL_ROOT_PASSWORD}" smartsurvey \
  -e "UPDATE ss_user SET password='<hash_från_steg_1>' WHERE username='admin';"
```

### Containern startar om kontinuerligt

Kontrollera om hälsokontrollen misslyckas:

```bash
docker compose -f docker-compose.production.yml ps
docker inspect rtcloud-app --format '{{json .State.Health}}'
```

Appens hälsokontroll anropar slutpunkten `/health`. Om den misslyckas upprepade gånger, kontrollera applikationsloggarna för startfel.

### Diskutrymmet är fullt

Identifiera vad som förbrukar utrymme:

```bash
# Kontrollera värdens diskanvändning
df -h

# Kontrollera Dockers diskanvändning (avbilder, containrar, volymer)
docker system df

# Ta bort oanvända avbilder och stoppade containrar (säkert att köra)
docker system prune
```

Använd inte `docker system prune --volumes` eftersom det raderar applikationsdata.

---

## Hälsokontroller

Varje tjänst har en automatisk hälsokontroll. Containerstatus återspeglar resultatet:

| Container | Kontrollmetod | Startperiod | Intervall |
|-----------|-------------|-------------|----------|
| `rtcloud-app` | HTTP GET `/health` | 90 sekunder | 30 sekunder |
| `rtcloud-mysql` | `mysqladmin ping` | 30 sekunder | 10 sekunder |
| `rtcloud-keycloak` | HTTP GET `:9000/health/live` | 120 sekunder | 30 sekunder |

Containrar med en misslyckad hälsokontroll startas automatiskt om enligt inställningen `RESTART_POLICY` (standard: `unless-stopped`).
