---
weight: 5
title: "Ylläpito"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "build"
toc: true
description: "Itse isännöidyn rtCloud-instanssin päivittäinen ylläpito: päivittäminen, varmuuskopiointi, palauttaminen ja yleisten ongelmien vianmääritys."
---

## Yleiset komennot

Käytä näitä komentoja säännöllisesti rtCloud-konttien hallintaan. Aja ne hakemistosta, joka sisältää `docker-compose.production.yml`:n.

```bash
# Tarkista kaikkien konttien tila ja terveys
docker compose -f docker-compose.production.yml ps

# Tarkastele reaaliaikaisia lokeja (kaikki palvelut)
docker compose -f docker-compose.production.yml logs -f

# Tarkastele vain sovelluksen lokeja
docker compose -f docker-compose.production.yml logs -f rtcloud

# Käynnistä yksittäinen kontti uudelleen
docker compose -f docker-compose.production.yml restart rtcloud

# Pysäytä kaikki palvelut
docker compose -f docker-compose.production.yml down

# Käynnistä kaikki palvelut
docker compose -f docker-compose.production.yml up -d

# Avaa komentotulkki sovelluskontissa
docker compose -f docker-compose.production.yml exec rtcloud bash
```

---

## Päivittäminen

rtCloud-päivitykset jaetaan uusina Docker-kuvatunnisteina. Päivittäminen hakee uusimman kuvan ja luo sovelluskonttin uudelleen. Tietokantamigraatiot ajetaan automaattisesti käynnistyksen yhteydessä.

**1. Hae uusin kuva:**

```bash
docker compose -f docker-compose.production.yml pull
```

**2. Luo sovelluskontit uudelleen:**

```bash
docker compose -f docker-compose.production.yml up -d
```

Docker korvaa vain ne kontit, joiden kuva on muuttunut. MySQL-kontti ja kaikki nimetyt taltiot pysyvät muuttumattomina.

### Version kiinnittäminen

Päivittääksesi tiettyyn versioon `latest`-version sijaan, päivitä `RTCLOUD_IMAGE` `.env`-tiedostossa:

```dotenv
RTCLOUD_IMAGE=rtawebteam/rta-smartsurvey:1.2.3
```

Sitten aja `docker compose pull` ja `up -d` kuten yllä.

### Alentaminen

Alentamista ei yleensä suositella, koska tietokantamigraatioita ei voi peruuttaa. Jos alentaminen on välttämätöntä, palauta ennen päivitystä otetusta tietokantavarmuuskopiosta.

---

## Varmuuskopiointi ja palauttaminen

### Varmuuskopioi tietokanta

Aja tämä komento viedäksesi sovellustietokannan SQL-tiedostoon:

```bash
docker compose -f docker-compose.production.yml exec mysql \
  mysqldump -u root -p"$(grep MYSQL_ROOT_PASSWORD .env | cut -d= -f2)" smartsurvey \
  > backup-$(date +%Y%m%d-%H%M%S).sql
```

Varmuuskopiotiedosto kirjoitetaan nykyiseen hakemistoosi isännällä.

### Palauta tietokanta

```bash
docker compose -f docker-compose.production.yml exec -T mysql \
  mysql -u root -p"$(grep MYSQL_ROOT_PASSWORD .env | cut -d= -f2)" smartsurvey \
  < backup-20240101-120000.sql
```

### Varmuuskopioi ladatut tiedostot

Kyselyn lähetykset sisältävät usein ladattuja tiedostoja (kuvia, ääntä, asiakirjoja), jotka on tallennettu nimettyihin Docker-taltioihin. Varmuuskopioi ne erikseen tietokannasta:

```bash
# Varmuuskopioi lataukset
docker run --rm \
  -v rtcloud_uploads:/data \
  -v "$(pwd):/backup" \
  alpine tar czf /backup/uploads-$(date +%Y%m%d).tar.gz -C /data .

# Varmuuskopioi ääninauhotteet
docker run --rm \
  -v rtcloud_audios:/data \
  -v "$(pwd):/backup" \
  alpine tar czf /backup/audios-$(date +%Y%m%d).tar.gz -C /data .
```

Korvaa `rtcloud_uploads` ja `rtcloud_audios` todellisilla taltioiden nimillä (joiden etuliitteenä on `COMPOSE_PROJECT_NAME`), jos olet muuttanut oletusta.

### Palauta ladatut tiedostot

```bash
docker run --rm \
  -v rtcloud_uploads:/data \
  -v "$(pwd):/backup" \
  alpine tar xzf /backup/uploads-20240101.tar.gz -C /data
```

### Automaattiset päivittäiset varmuuskopiot

Lisää cron-tehtävä isännälle ajamaan varmuuskopiot automaattisesti. Muokkaa root-crontabia komennolla `crontab -e`:

```cron
# Päivittäinen tietokantavarmuuskopio klo 2:00, säilytä 30 päivän historia
0 2 * * * cd /opt/rtcloud && docker compose -f docker-compose.production.yml exec -T mysql \
  mysqldump -u root -p"$(grep MYSQL_ROOT_PASSWORD .env | cut -d= -f2)" smartsurvey \
  > /backups/db-$(date +\%Y\%m\%d).sql && \
  find /backups -name "db-*.sql" -mtime +30 -delete
```

---

## Vianmääritys

### Sovelluskontit ei käynnisty

Tarkista kontin lokit virheilmoitusten varalta:

```bash
docker compose -f docker-compose.production.yml logs rtcloud
```

Yleiset syyt:
- Puuttuvat tai virheelliset ympäristömuuttujat `.env`-tiedostossa
- MySQL ei ole vielä valmis (odota 60 sekuntia ja tarkista uudelleen)
- Porttikonflikti — toinen prosessi käyttää jo `APP_PORT`-porttia

### MySQL ei ole terve

```bash
docker compose -f docker-compose.production.yml logs mysql
```

Yleiset syyt:
- `MYSQL_ROOT_PASSWORD` ei ole asetettu `.env`-tiedostossa
- Vioittunut datataltio (harvinainen — tarkista levytila komennolla `df -h`)

MySQL voi kestää 30–60 sekuntia alustuakseen ensimmäisellä käynnistyksellä. Odota ja tarkista uudelleen ennen kuin olettaa epäonnistumisen.

### Portti on jo käytössä

Muuta `APP_PORT` tai `SHINY_PORT` `.env`-tiedostossa vapaalle portille, sitten luo kontit uudelleen:

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate
```

Selvittääksesi, mikä käyttää porttia isännällä:

```bash
lsof -i :8080
```

### 400 CSRF-tunnusta ei voitu vahvistaa

Tämä virhe esiintyy paikallisissa tai käänteisenvälityspalvelimen ympäristöissä, joissa pyynnön alkuperä ei vastaa odotettua isäntää. Poista CSRF-vahvistus käytöstä vain paikallisessa kehityksessä:

```dotenv
CSRF_VALIDATION_ENABLED=false
```

Sitten käynnistä sovellus uudelleen:

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

> Älä poista CSRF-vahvistusta käytöstä tuotannossa. Jos tämä virhe esiintyy tuotannossa, varmista, että käänteinen välityspalvelimesi välittää oikeat `Host`- ja `X-Forwarded-For`-otsikot.

### Järjestelmänvalvojan salasana unohtunut

Nollaa järjestelmänvalvojan salasana suoraan tietokannassa. Yhdistä MySQL-konttiin ja päivitä salasanan hash:

**Vaihe 1** — Luo uusi salasanan hash. Korvaa `newpassword` haluamallasi salasanalla:

```bash
docker compose -f docker-compose.production.yml exec rtcloud php -r "
  \$salt = trim(shell_exec(\"mysql -h mysql -u root -p\\\"\${MYSQL_ROOT_PASSWORD}\\\" \${MYSQL_DATABASE} -se \\\"SELECT salt FROM ss_user WHERE username='admin';\\\"\"));
  echo md5(\$salt . 'newpassword') . PHP_EOL;
"
```

**Vaihe 2** — Päivitä hash tietokantaan:

```bash
docker compose -f docker-compose.production.yml exec mysql \
  mysql -u root -p"${MYSQL_ROOT_PASSWORD}" smartsurvey \
  -e "UPDATE ss_user SET password='<hash_vaiheesta_1>' WHERE username='admin';"
```

### Kontti käynnistyy jatkuvasti uudelleen

Tarkista, epäonnistuuko terveystarkistus:

```bash
docker compose -f docker-compose.production.yml ps
docker inspect rtcloud-app --format '{{json .State.Health}}'
```

Sovelluksen terveystarkistus kutsuu `/health`-päätepistettä. Jos se epäonnistuu toistuvasti, tarkista sovelluslokit käynnistysvirheiden varalta.

### Levy on täynnä

Selvitä, mikä kuluttaa tilaa:

```bash
# Tarkista isännän levyn käyttö
df -h

# Tarkista Dockerin levyn käyttö (kuvat, kontit, taltiot)
docker system df

# Poista käyttämättömät kuvat ja pysäytetyt kontit (turvallista ajaa)
docker system prune
```

Älä käytä `docker system prune --volumes`, sillä se poistaa sovellustiedot.

---

## Terveystarkistukset

Jokaisella palvelulla on automaattinen terveystarkistus. Kontin tila heijastaa tulosta:

| Kontti | Tarkistusmenetelmä | Käynnistysaika | Intervalli |
|-----------|-------------|-------------|----------|
| `rtcloud-app` | HTTP GET `/health` | 90 sekuntia | 30 sekuntia |
| `rtcloud-mysql` | `mysqladmin ping` | 30 sekuntia | 10 sekuntia |
| `rtcloud-keycloak` | HTTP GET `:9000/health/live` | 120 sekuntia | 30 sekuntia |

Kontit, joiden terveystarkistus epäonnistuu, käynnistetään automaattisesti uudelleen `RESTART_POLICY`-asetuksen mukaisesti (oletus: `unless-stopped`).
