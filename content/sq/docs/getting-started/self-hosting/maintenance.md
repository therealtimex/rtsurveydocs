---
weight: 5
title: "Mirëmbajtja"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "build"
toc: true
description: "Mirëmbajtja e përditshme për një instancë vetjake rtCloud: përditësimi, rezervimi, restaurimi dhe zgjidhja e problemeve të zakonshme."
---

## Komandat e Zakonshme

Përdorni këto komanda rregullisht për të menaxhuar kontejnerët tuaj rtCloud. Ekzekutoni ato nga drejtoria që përmban `docker-compose.production.yml`.

```bash
# Kontrolloni statusin dhe shëndetin e të gjithë kontejnerëve
docker compose -f docker-compose.production.yml ps

# Shikoni regjistrat e drejtpërdrejta (të gjitha shërbimet)
docker compose -f docker-compose.production.yml logs -f

# Shikoni regjistrat vetëm të aplikacionit
docker compose -f docker-compose.production.yml logs -f rtcloud

# Rinisni një kontejner të vetëm
docker compose -f docker-compose.production.yml restart rtcloud

# Ndaloni të gjitha shërbimet
docker compose -f docker-compose.production.yml down

# Nisni të gjitha shërbimet
docker compose -f docker-compose.production.yml up -d

# Hapni një predhë brenda kontejnerit të aplikacionit
docker compose -f docker-compose.production.yml exec rtcloud bash
```

---

## Përditësimi

Përditësimet rtCloud shpërndahen si etiketa të reja imazhi Docker. Përditësimi tërheq imazhin e fundit dhe rikrijon kontejnerin e aplikacionit. Migrimet e bazës së të dhënave ekzekutohen automatikisht në nisje.

**1. Tërhiqni imazhin e fundit:**

```bash
docker compose -f docker-compose.production.yml pull
```

**2. Rikrijoni kontejnerin e aplikacionit:**

```bash
docker compose -f docker-compose.production.yml up -d
```

Docker zëvendëson vetëm kontejnerët imazhi i të cilëve ka ndryshuar. Kontejneri MySQL dhe të gjitha volumet e emëruara nuk preken.

### Fiksimi i një Versioni

Për të përditësuar në një version specifik në vend të `latest`, përditësoni `RTCLOUD_IMAGE` në `.env`:

```dotenv
RTCLOUD_IMAGE=rtawebteam/rta-smartsurvey:1.2.3
```

Pastaj ekzekutoni `docker compose pull` dhe `up -d` si më sipër.

### Degradimi

Degradimi zakonisht nuk rekomandohet, pasi migrimet e bazës së të dhënave nuk mund të kthehen. Nëse nevojitet degradim, restauroni nga një rezervim i bazës së të dhënave i marrë para përditësimit.

---

## Rezervimi dhe Restaurimi

### Rezervoni Bazën e të Dhënave

Ekzekutoni këtë komandë për të eksportuar bazën e të dhënave të aplikacionit në një skedar SQL:

```bash
docker compose -f docker-compose.production.yml exec mysql \
  mysqldump -u root -p"$(grep MYSQL_ROOT_PASSWORD .env | cut -d= -f2)" smartsurvey \
  > rezervimi-$(date +%Y%m%d-%H%M%S).sql
```

Skedari i rezervimit shkruhet në drejtorinë tuaj aktuale në host.

### Restauroni Bazën e të Dhënave

```bash
docker compose -f docker-compose.production.yml exec -T mysql \
  mysql -u root -p"$(grep MYSQL_ROOT_PASSWORD .env | cut -d= -f2)" smartsurvey \
  < rezervimi-20240101-120000.sql
```

### Rezervoni Skedarët e Ngarkuar

Dërgimet e sondazhit shpesh përfshijnë skedarë të ngarkuar (foto, audio, dokumente) të ruajtur në volume të emëruara Docker. Rezervojini ato veçmas nga baza e të dhënave:

```bash
# Rezervoni ngarkimet
docker run --rm \
  -v rtcloud_uploads:/data \
  -v "$(pwd):/backup" \
  alpine tar czf /backup/ngarkimet-$(date +%Y%m%d).tar.gz -C /data .

# Rezervoni regjistrat audio
docker run --rm \
  -v rtcloud_audios:/data \
  -v "$(pwd):/backup" \
  alpine tar czf /backup/audio-$(date +%Y%m%d).tar.gz -C /data .
```

Zëvendësoni `rtcloud_uploads` dhe `rtcloud_audios` me emrat aktualë të volumeve tuaja (prefiksuar nga `COMPOSE_PROJECT_NAME`) nëse keni ndryshuar parazgjedhjen.

### Restauroni Skedarët e Ngarkuar

```bash
docker run --rm \
  -v rtcloud_uploads:/data \
  -v "$(pwd):/backup" \
  alpine tar xzf /backup/ngarkimet-20240101.tar.gz -C /data
```

### Rezervimet e Automatizuara Ditore

Shtoni një detyrë cron në host për të ekzekutuar rezervimet automatikisht. Editoni crontab-in rrënjësor me `crontab -e`:

```cron
# Rezervim ditor i bazës së të dhënave në 2:00 paradite, mbajini 30 ditë historik
0 2 * * * cd /opt/rtcloud && docker compose -f docker-compose.production.yml exec -T mysql \
  mysqldump -u root -p"$(grep MYSQL_ROOT_PASSWORD .env | cut -d= -f2)" smartsurvey \
  > /backups/db-$(date +\%Y\%m\%d).sql && \
  find /backups -name "db-*.sql" -mtime +30 -delete
```

---

## Zgjidhja e Problemeve

### Kontejneri i aplikacionit nuk niset

Kontrolloni regjistrat e kontejnerit për mesazhe gabimi:

```bash
docker compose -f docker-compose.production.yml logs rtcloud
```

Shkaqet e zakonshme:
- Variabla të mjedisit të munguar ose të pavlefshme në `.env`
- MySQL ende jo gati (prisni 60 sekonda dhe kontrolloni sërish)
- Konflikt porte — një proces tjetër tashmë po përdor `APP_PORT`

### MySQL jo i shëndetshëm

```bash
docker compose -f docker-compose.production.yml logs mysql
```

Shkaqet e zakonshme:
- `MYSQL_ROOT_PASSWORD` nuk është caktuar në `.env`
- Volume i dhënash i korruptuar (i rrallë — kontrolloni hapësirën e diskut me `df -h`)

MySQL mund të marrë 30–60 sekonda për t'u inicializuar gjatë nisjes shumë të parë. Prisni dhe kontrolloni sërish para se të supozoni dështim.

### Porta tashmë në përdorim

Ndryshoni `APP_PORT` ose `SHINY_PORT` në `.env` në një portë të lirë, pastaj rikrijoni kontejnerët:

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate
```

Për të gjetur çfarë po përdor një portë në host:

```bash
lsof -i :8080
```

### 400 Shenja CSRF Nuk Mund të Verifikohet

Ky gabim shfaqet në mjedise lokale ose reverse-proxy ku origjina e kërkesës nuk përputhet me hostin e pritur. Çaktivizoni validimin CSRF vetëm për zhvillim lokal:

```dotenv
CSRF_VALIDATION_ENABLED=false
```

Pastaj rinisni aplikacionin:

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

> Mos çaktivizoni validimin CSRF në prodhim. Nëse ky gabim ndodh në prodhim, sigurohuni që reverse proxy juaj po dërgon korrektet kokëzat `Host` dhe `X-Forwarded-For`.

### Harruat Fjalëkalimin e Administratorit

Rivendosni fjalëkalimin e administratorit direkt në bazën e të dhënave. Lidhuni me kontejnerin MySQL dhe përditësoni hash-in e fjalëkalimit:

**Hapi 1** — Gjeneroni hash-in e fjalëkalimit të ri. Zëvendësoni `fjalëkalimi_i_ri` me fjalëkalimin tuaj të dëshiruar:

```bash
docker compose -f docker-compose.production.yml exec rtcloud php -r "
  \$salt = trim(shell_exec(\"mysql -h mysql -u root -p\\\"\${MYSQL_ROOT_PASSWORD}\\\" \${MYSQL_DATABASE} -se \\\"SELECT salt FROM ss_user WHERE username='admin';\\\"\"));
  echo md5(\$salt . 'fjalëkalimi_i_ri') . PHP_EOL;
"
```

**Hapi 2** — Përditësoni hash-in në bazën e të dhënave:

```bash
docker compose -f docker-compose.production.yml exec mysql \
  mysql -u root -p"${MYSQL_ROOT_PASSWORD}" smartsurvey \
  -e "UPDATE ss_user SET password='<hash_nga_hapi_1>' WHERE username='admin';"
```

### Kontejneri vazhdon të riniset

Kontrolloni nëse kontrolli i shëndetit po dështon:

```bash
docker compose -f docker-compose.production.yml ps
docker inspect rtcloud-app --format '{{json .State.Health}}'
```

Kontrolli i shëndetit të aplikacionit thërret pikën fundore `/health`. Nëse dështon vazhdimisht, kontrolloni regjistrat e aplikacionit për gabime nisje.

### Hapësira e diskut e mbushur

Identifikoni çfarë po konsumon hapësirë:

```bash
# Kontrolloni përdorimin e diskut të hostit
df -h

# Kontrolloni përdorimin e diskut Docker (imazhe, kontejnerë, volume)
docker system df

# Hiqni imazhet e papërdorura dhe kontejnerët e ndaluar (të sigurt për ekzekutim)
docker system prune
```

Mos përdorni `docker system prune --volumes` pasi kjo do të fshijë të dhënat e aplikacionit.

---

## Kontrollet e Shëndetit

Çdo shërbim ka një kontroll automatik shëndetit. Statusi i kontejnerit pasqyron rezultatin:

| Kontejneri | Metoda e Kontrollit | Periudha e Nisjes | Intervali |
|-----------|-------------|-------------|----------|
| `rtcloud-app` | HTTP GET `/health` | 90 sekonda | 30 sekonda |
| `rtcloud-mysql` | `mysqladmin ping` | 30 sekonda | 10 sekonda |
| `rtcloud-keycloak` | HTTP GET `:9000/health/live` | 120 sekonda | 30 sekonda |

Kontejnerët me kontroll shëndetit që dështon riniset automatikisht sipas cilësimit `RESTART_POLICY` (parazgjedhja: `unless-stopped`).
