---
weight: 5
title: "Údržba"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "build"
toc: true
description: "Každodenní údržba vlastní instance rtCloud: upgrade, zálohování, obnova a řešení běžných problémů."
---

## Běžné příkazy

Tyto příkazy používejte pravidelně ke správě kontejnerů rtCloud. Spouštějte je z adresáře obsahujícího `docker-compose.production.yml`.

```bash
# Zkontrolujte stav a zdraví všech kontejnerů
docker compose -f docker-compose.production.yml ps

# Zobrazte živé protokoly (všechny služby)
docker compose -f docker-compose.production.yml logs -f

# Zobrazení protokolů pouze pro aplikaci
docker compose -f docker-compose.production.yml logs -f rtcloud

# Restart jednoho kontejneru
docker compose -f docker-compose.production.yml restart rtcloud

# Zastavení všech služeb
docker compose -f docker-compose.production.yml down

# Spuštění všech služeb
docker compose -f docker-compose.production.yml up -d

# Otevření shellu uvnitř kontejneru aplikace
docker compose -f docker-compose.production.yml exec rtcloud bash
```

---

## Upgrade

Aktualizace rtCloud jsou distribuovány jako nové Docker image tagy. Upgrade stáhne nejnovější obraz a znovu vytvoří kontejner aplikace. Databázové migrace se spouštějí automaticky při startu.

**1. Stáhněte nejnovější obraz:**

```bash
docker compose -f docker-compose.production.yml pull
```

**2. Znovu vytvořte kontejner aplikace:**

```bash
docker compose -f docker-compose.production.yml up -d
```

Docker nahradí pouze kontejnery, jejichž obraz se změnil. Kontejner MySQL a všechny pojmenované svazky jsou nedotčeny.

### Připnutí verze

Pro upgrade na konkrétní verzi namísto `latest` aktualizujte `RTCLOUD_IMAGE` v `.env`:

```dotenv
RTCLOUD_IMAGE=rtawebteam/rta-smartsurvey:1.2.3
```

Poté spusťte `docker compose pull` a `up -d` jak je uvedeno výše.

### Downgrade

Downgrade se obecně nedoporučuje, protože databázové migrace nelze vrátit zpět. Pokud je downgrade nezbytný, obnovte ze zálohy databáze pořízené před upgradem.

---

## Zálohování a obnova

### Záloha databáze

Spusťte tento příkaz pro export databáze aplikace do SQL souboru:

```bash
docker compose -f docker-compose.production.yml exec mysql \
  mysqldump -u root -p"$(grep MYSQL_ROOT_PASSWORD .env | cut -d= -f2)" smartsurvey \
  > backup-$(date +%Y%m%d-%H%M%S).sql
```

Soubor zálohy je zapsán do aktuálního adresáře na hostiteli.

### Obnova databáze

```bash
docker compose -f docker-compose.production.yml exec -T mysql \
  mysql -u root -p"$(grep MYSQL_ROOT_PASSWORD .env | cut -d= -f2)" smartsurvey \
  < backup-20240101-120000.sql
```

### Záloha nahraných souborů

Odeslané průzkumy často obsahují nahrané soubory (fotografie, zvuk, dokumenty) uložené v pojmenovaných Docker svazcích. Zálohujte je odděleně od databáze:

```bash
# Záloha nahraných souborů
docker run --rm \
  -v rtcloud_uploads:/data \
  -v "$(pwd):/backup" \
  alpine tar czf /backup/uploads-$(date +%Y%m%d).tar.gz -C /data .

# Záloha zvukových nahrávek
docker run --rm \
  -v rtcloud_audios:/data \
  -v "$(pwd):/backup" \
  alpine tar czf /backup/audios-$(date +%Y%m%d).tar.gz -C /data .
```

Nahraďte `rtcloud_uploads` a `rtcloud_audios` skutečnými názvy svazků (s předponou `COMPOSE_PROJECT_NAME`), pokud jste změnili výchozí.

### Obnova nahraných souborů

```bash
docker run --rm \
  -v rtcloud_uploads:/data \
  -v "$(pwd):/backup" \
  alpine tar xzf /backup/uploads-20240101.tar.gz -C /data
```

### Automatické denní zálohy

Přidejte cron úlohu na hostiteli pro automatické spouštění záloh. Upravte kořenový crontab pomocí `crontab -e`:

```cron
# Denní záloha databáze ve 2:00, uchovávejte 30 dní historii
0 2 * * * cd /opt/rtcloud && docker compose -f docker-compose.production.yml exec -T mysql \
  mysqldump -u root -p"$(grep MYSQL_ROOT_PASSWORD .env | cut -d= -f2)" smartsurvey \
  > /backups/db-$(date +\%Y\%m\%d).sql && \
  find /backups -name "db-*.sql" -mtime +30 -delete
```

---

## Řešení problémů

### Kontejner aplikace se nespustí

Zkontrolujte protokoly kontejneru pro chybové zprávy:

```bash
docker compose -f docker-compose.production.yml logs rtcloud
```

Běžné příčiny:
- Chybějící nebo neplatné proměnné prostředí v `.env`
- MySQL ještě není připraven (počkejte 60 sekund a zkontrolujte znovu)
- Konflikt portů — jiný proces již používá `APP_PORT`

### MySQL není zdravý

```bash
docker compose -f docker-compose.production.yml logs mysql
```

Běžné příčiny:
- `MYSQL_ROOT_PASSWORD` není nastaveno v `.env`
- Poškozený datový svazek (vzácné — zkontrolujte místo na disku pomocí `df -h`)

MySQL může trvat 30–60 sekund inicializace při úplně prvním spuštění. Počkejte a znovu zkontrolujte před předpokladem selhání.

### Port je již obsazen

Změňte `APP_PORT` nebo `SHINY_PORT` v `.env` na volný port, poté znovu vytvořte kontejnery:

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate
```

Pro zjištění, co používá port na hostiteli:

```bash
lsof -i :8080
```

### 400 CSRF Token nemohl být ověřen

Tato chyba se zobrazuje v lokálních nebo reverzní proxy prostředích, kde původ požadavku neodpovídá očekávanému hostiteli. Deaktivujte CSRF validaci pouze pro lokální vývoj:

```dotenv
CSRF_VALIDATION_ENABLED=false
```

Poté restartujte aplikaci:

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

> V produkci nedeaktivujte CSRF validaci. Pokud se tato chyba vyskytuje v produkci, ujistěte se, že vaše reverzní proxy předává správné hlavičky `Host` a `X-Forwarded-For`.

### Zapomenuté heslo administrátora

Resetujte heslo administrátora přímo v databázi. Připojte se ke kontejneru MySQL a aktualizujte hash hesla:

**Krok 1** — Vygenerujte hash nového hesla. Nahraďte `newpassword` svým požadovaným heslem:

```bash
docker compose -f docker-compose.production.yml exec rtcloud php -r "
  \$salt = trim(shell_exec(\"mysql -h mysql -u root -p\\\"\${MYSQL_ROOT_PASSWORD}\\\" \${MYSQL_DATABASE} -se \\\"SELECT salt FROM ss_user WHERE username='admin';\\\"\"));
  echo md5(\$salt . 'newpassword') . PHP_EOL;
"
```

**Krok 2** — Aktualizujte hash v databázi:

```bash
docker compose -f docker-compose.production.yml exec mysql \
  mysql -u root -p"${MYSQL_ROOT_PASSWORD}" smartsurvey \
  -e "UPDATE ss_user SET password='<hash_z_kroku_1>' WHERE username='admin';"
```

### Kontejner se stále restartuje

Zkontrolujte, zda kontrola zdravotního stavu selhává:

```bash
docker compose -f docker-compose.production.yml ps
docker inspect rtcloud-app --format '{{json .State.Health}}'
```

Kontrola zdravotního stavu aplikace volá endpoint `/health`. Pokud opakovaně selhává, zkontrolujte protokoly aplikace pro chyby při spuštění.

### Plný disk

Identifikujte, co spotřebovává místo:

```bash
# Zkontrolujte využití disku hostitele
df -h

# Zkontrolujte využití disku Dockerem (obrazy, kontejnery, svazky)
docker system df

# Odeberte nepoužívané obrazy a zastavené kontejnery (bezpečné spuštění)
docker system prune
```

Nepoužívejte `docker system prune --volumes`, protože by to smazalo data aplikace.

---

## Kontroly zdravotního stavu

Každá služba má automatickou kontrolu zdravotního stavu. Stav kontejneru odráží výsledek:

| Kontejner | Metoda kontroly | Počáteční period | Interval |
|-----------|-------------|-------------|----------|
| `rtcloud-app` | HTTP GET `/health` | 90 sekund | 30 sekund |
| `rtcloud-mysql` | `mysqladmin ping` | 30 sekund | 10 sekund |
| `rtcloud-keycloak` | HTTP GET `:9000/health/live` | 120 sekund | 30 sekund |

Kontejnery s neúspěšnou kontrolou zdravotního stavu jsou automaticky restartovány podle nastavení `RESTART_POLICY` (výchozí: `unless-stopped`).
