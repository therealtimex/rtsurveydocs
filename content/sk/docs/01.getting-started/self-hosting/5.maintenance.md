---
weight: 5
title: "Údržba"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "build"
toc: true
description: "Každodenná údržba vlastnej inštancie rtCloud: aktualizácia, zálohovanie, obnova a riešenie bežných problémov."
---

## Bežné príkazy

Tieto príkazy používajte pravidelne na správu kontajnerov rtCloud. Spúšťajte ich z adresára obsahujúceho `docker-compose.production.yml`.

```bash
# Skontrolujte stav a zdravie všetkých kontajnerov
docker compose -f docker-compose.production.yml ps

# Zobrazte živé protokoly (všetky služby)
docker compose -f docker-compose.production.yml logs -f

# Zobrazte protokoly iba pre aplikáciu
docker compose -f docker-compose.production.yml logs -f rtcloud

# Reštartujte jeden kontajner
docker compose -f docker-compose.production.yml restart rtcloud

# Zastavte všetky služby
docker compose -f docker-compose.production.yml down

# Spustite všetky služby
docker compose -f docker-compose.production.yml up -d

# Otvorte shell vo vnútri kontajnera aplikácie
docker compose -f docker-compose.production.yml exec rtcloud bash
```

---

## Aktualizácia

Aktualizácie rtCloud sú distribuované ako nové tagy Docker image. Aktualizácia stiahne najnovší image a znovu vytvorí kontajner aplikácie. Migrácie databázy sa spúšťajú automaticky pri štarte.

**1. Stiahnite najnovší image:**

```bash
docker compose -f docker-compose.production.yml pull
```

**2. Znovu vytvorte kontajner aplikácie:**

```bash
docker compose -f docker-compose.production.yml up -d
```

Docker nahradí iba kontajnery, ktorých image sa zmenil. Kontajner MySQL a všetky pomenované zväzky zostanú nedotknuté.

### Pripnutie verzie

Na aktualizáciu na konkrétnu verziu namiesto `latest` aktualizujte `RTCLOUD_IMAGE` v `.env`:

```dotenv
RTCLOUD_IMAGE=rtawebteam/rta-smartsurvey:1.2.3
```

Potom spustite `docker compose pull` a `up -d` ako vyššie.

### Downgrade

Downgrade sa vo všeobecnosti neodporúča, pretože migrácie databázy nie je možné vrátiť. Ak je potrebný downgrade, obnovte zo zálohy databázy vytvorenej pred aktualizáciou.

---

## Zálohovanie a obnova

### Zálohovanie databázy

Spustite tento príkaz na export databázy aplikácie do SQL súboru:

```bash
docker compose -f docker-compose.production.yml exec mysql \
  mysqldump -u root -p"$(grep MYSQL_ROOT_PASSWORD .env | cut -d= -f2)" smartsurvey \
  > backup-$(date +%Y%m%d-%H%M%S).sql
```

Záložný súbor sa zapíše do vášho aktuálneho adresára na hostiteľovi.

### Obnova databázy

```bash
docker compose -f docker-compose.production.yml exec -T mysql \
  mysql -u root -p"$(grep MYSQL_ROOT_PASSWORD .env | cut -d= -f2)" smartsurvey \
  < backup-20240101-120000.sql
```

### Zálohovanie nahraných súborov

Odoslania prieskumu často obsahujú nahrané súbory (fotografie, zvuk, dokumenty) uložené v pomenovaných Docker zväzkoch. Zálohujte ich oddelene od databázy:

```bash
# Zálohovanie nahraných súborov
docker run --rm \
  -v rtcloud_uploads:/data \
  -v "$(pwd):/backup" \
  alpine tar czf /backup/uploads-$(date +%Y%m%d).tar.gz -C /data .

# Zálohovanie zvukových nahrávok
docker run --rm \
  -v rtcloud_audios:/data \
  -v "$(pwd):/backup" \
  alpine tar czf /backup/audios-$(date +%Y%m%d).tar.gz -C /data .
```

Nahraďte `rtcloud_uploads` a `rtcloud_audios` skutočnými názvami zväzkov (s predponou `COMPOSE_PROJECT_NAME`), ak ste zmenili predvolenú hodnotu.

### Obnova nahraných súborov

```bash
docker run --rm \
  -v rtcloud_uploads:/data \
  -v "$(pwd):/backup" \
  alpine tar xzf /backup/uploads-20240101.tar.gz -C /data
```

### Automatizované denné zálohy

Pridajte cron úlohu na hostiteľovi na automatické vykonávanie záloh. Upravte crontab roota pomocou `crontab -e`:

```cron
# Denná záloha databázy o 2:00 ráno, uchovávajte 30 dní histórie
0 2 * * * cd /opt/rtcloud && docker compose -f docker-compose.production.yml exec -T mysql \
  mysqldump -u root -p"$(grep MYSQL_ROOT_PASSWORD .env | cut -d= -f2)" smartsurvey \
  > /backups/db-$(date +\%Y\%m\%d).sql && \
  find /backups -name "db-*.sql" -mtime +30 -delete
```

---

## Riešenie problémov

### Kontajner aplikácie sa nespúšťa

Skontrolujte protokoly kontajnera na chybové správy:

```bash
docker compose -f docker-compose.production.yml logs rtcloud
```

Bežné príčiny:
- Chýbajúce alebo neplatné premenné prostredia v `.env`
- MySQL ešte nie je pripravený (počkajte 60 sekúnd a znovu skontrolujte)
- Konflikt portov — iný proces už používa `APP_PORT`

### MySQL nie je zdravý

```bash
docker compose -f docker-compose.production.yml logs mysql
```

Bežné príčiny:
- `MYSQL_ROOT_PASSWORD` nie je nastavené v `.env`
- Poškodený zväzok dát (zriedkavé — skontrolujte miesto na disku pomocou `df -h`)

MySQL môže trvať 30–60 sekúnd na inicializáciu pri úplne prvom spustení. Počkajte a znovu skontrolujte pred predpokladom zlyhania.

### Port je už používaný

Zmeňte `APP_PORT` alebo `SHINY_PORT` v `.env` na voľný port, potom znovu vytvorte kontajnery:

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate
```

Na zistenie, čo používa port na hostiteľovi:

```bash
lsof -i :8080
```

### 400 CSRF Token Could Not Be Verified

Táto chyba sa objavuje v lokálnych alebo reverzne-proxy prostrediach, kde pôvod požiadavky nezodpovedá očakávanému hostiteľovi. Zakážte overenie CSRF iba pre lokálny vývoj:

```dotenv
CSRF_VALIDATION_ENABLED=false
```

Potom reštartujte aplikáciu:

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

> Nezakázajte overenie CSRF v produkcii. Ak k tejto chybe dôjde v produkcii, uistite sa, že váš reverzný proxy správne preposiela hlavičky `Host` a `X-Forwarded-For`.

### Zabudnuté heslo správcu

Resetujte heslo správcu priamo v databáze. Pripojte sa ku kontajneru MySQL a aktualizujte hash hesla:

**Krok 1** — Vygenerujte hash nového hesla. Nahraďte `newpassword` požadovaným heslom:

```bash
docker compose -f docker-compose.production.yml exec rtcloud php -r "
  \$salt = trim(shell_exec(\"mysql -h mysql -u root -p\\\"\${MYSQL_ROOT_PASSWORD}\\\" \${MYSQL_DATABASE} -se \\\"SELECT salt FROM ss_user WHERE username='admin';\\\"\"));
  echo md5(\$salt . 'newpassword') . PHP_EOL;
"
```

**Krok 2** — Aktualizujte hash v databáze:

```bash
docker compose -f docker-compose.production.yml exec mysql \
  mysql -u root -p"${MYSQL_ROOT_PASSWORD}" smartsurvey \
  -e "UPDATE ss_user SET password='<hash_z_kroku_1>' WHERE username='admin';"
```

### Kontajner sa neustále reštartuje

Skontrolujte, či kontrola zdravia zlyhava:

```bash
docker compose -f docker-compose.production.yml ps
docker inspect rtcloud-app --format '{{json .State.Health}}'
```

Kontrola zdravia aplikácie volá koncový bod `/health`. Ak opakovane zlyhava, skontrolujte protokoly aplikácie na chyby pri štarte.

### Disk je plný

Identifikujte, čo spotrebúva miesto:

```bash
# Skontrolujte využitie disku hostiteľa
df -h

# Skontrolujte využitie disku Docker (images, kontajnery, zväzky)
docker system df

# Odstráňte nepoužívané images a zastavené kontajnery (bezpečné na spustenie)
docker system prune
```

Nepoužívajte `docker system prune --volumes`, pretože tým vymažete dáta aplikácie.

---

## Kontroly zdravia

Každá služba má automatickú kontrolu zdravia. Stav kontajnera odráža výsledok:

| Kontajner | Metóda kontroly | Počiatočné obdobie | Interval |
|-----------|-------------|-------------|----------|
| `rtcloud-app` | HTTP GET `/health` | 90 sekúnd | 30 sekúnd |
| `rtcloud-mysql` | `mysqladmin ping` | 30 sekúnd | 10 sekúnd |
| `rtcloud-keycloak` | HTTP GET `:9000/health/live` | 120 sekúnd | 30 sekúnd |

Kontajnery s neúspešnou kontrolou zdravia sa automaticky reštartujú podľa nastavenia `RESTART_POLICY` (predvolené: `unless-stopped`).
