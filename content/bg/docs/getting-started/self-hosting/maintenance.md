---
weight: 5
title: "Поддръжка"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "build"
toc: true
description: "Ежедневна поддръжка на самостоятелно хостван инстанс на rtCloud: надграждане, архивиране, възстановяване и отстраняване на чести проблеми."
---

## Чести команди

Използвайте тези команди редовно за управление на вашите rtCloud контейнери. Изпълнявайте ги от директорията, съдържаща `docker-compose.production.yml`.

```bash
# Проверка на статуса и здравето на всички контейнери
docker compose -f docker-compose.production.yml ps

# Преглед на логове в реално време (всички услуги)
docker compose -f docker-compose.production.yml logs -f

# Преглед на логове само на приложението
docker compose -f docker-compose.production.yml logs -f rtcloud

# Рестартиране на единичен контейнер
docker compose -f docker-compose.production.yml restart rtcloud

# Спиране на всички услуги
docker compose -f docker-compose.production.yml down

# Стартиране на всички услуги
docker compose -f docker-compose.production.yml up -d

# Отваряне на командна обвивка вътре в контейнера на приложението
docker compose -f docker-compose.production.yml exec rtcloud bash
```

---

## Надграждане

Актуализациите на rtCloud се разпространяват като нови тагове на Docker образи. Надграждането изтегля последния образ и пресъздава контейнера на приложението. Миграциите на базата данни се изпълняват автоматично при стартиране.

**1. Изтеглете последния образ:**

```bash
docker compose -f docker-compose.production.yml pull
```

**2. Пресъздайте контейнера на приложението:**

```bash
docker compose -f docker-compose.production.yml up -d
```

Docker заменя само контейнерите, чийто образ се е променил. MySQL контейнерът и всички именувани томове не се засягат.

### Закрепване на версия

За надграждане до конкретна версия вместо `latest`, актуализирайте `RTCLOUD_IMAGE` в `.env`:

```dotenv
RTCLOUD_IMAGE=rtawebteam/rta-smartsurvey:1.2.3
```

След това стартирайте `docker compose pull` и `up -d` както по-горе.

### Понижаване на версия

Понижаването на версия обикновено не се препоръчва, тъй като миграциите на базата данни не могат да бъдат обърнати. Ако е необходимо понижаване, възстановете от архив на базата данни, направен преди надграждането.

---

## Архивиране и възстановяване

### Архивиране на базата данни

Изпълнете тази команда, за да експортирате базата данни на приложението в SQL файл:

```bash
docker compose -f docker-compose.production.yml exec mysql \
  mysqldump -u root -p"$(grep MYSQL_ROOT_PASSWORD .env | cut -d= -f2)" smartsurvey \
  > backup-$(date +%Y%m%d-%H%M%S).sql
```

Файлът с архива се записва в текущата директория на хоста.

### Възстановяване на базата данни

```bash
docker compose -f docker-compose.production.yml exec -T mysql \
  mysql -u root -p"$(grep MYSQL_ROOT_PASSWORD .env | cut -d= -f2)" smartsurvey \
  < backup-20240101-120000.sql
```

### Архивиране на качени файлове

Подаванията на анкети често включват качени файлове (снимки, аудио, документи), съхранявани в именувани Docker томове. Архивирайте ги отделно от базата данни:

```bash
# Архивиране на качените файлове
docker run --rm \
  -v rtcloud_uploads:/data \
  -v "$(pwd):/backup" \
  alpine tar czf /backup/uploads-$(date +%Y%m%d).tar.gz -C /data .

# Архивиране на аудио записи
docker run --rm \
  -v rtcloud_audios:/data \
  -v "$(pwd):/backup" \
  alpine tar czf /backup/audios-$(date +%Y%m%d).tar.gz -C /data .
```

Заменете `rtcloud_uploads` и `rtcloud_audios` с действителните имена на томовете (с префикс от `COMPOSE_PROJECT_NAME`), ако сте променили стойностите по подразбиране.

### Възстановяване на качени файлове

```bash
docker run --rm \
  -v rtcloud_uploads:/data \
  -v "$(pwd):/backup" \
  alpine tar xzf /backup/uploads-20240101.tar.gz -C /data
```

### Автоматизирани ежедневни архиви

Добавете cron задание на хоста за автоматично извършване на архиви. Редактирайте root crontab с `crontab -e`:

```cron
# Ежедневен архив на базата данни в 2:00 ч., съхранение за 30 дни
0 2 * * * cd /opt/rtcloud && docker compose -f docker-compose.production.yml exec -T mysql \
  mysqldump -u root -p"$(grep MYSQL_ROOT_PASSWORD .env | cut -d= -f2)" smartsurvey \
  > /backups/db-$(date +\%Y\%m\%d).sql && \
  find /backups -name "db-*.sql" -mtime +30 -delete
```

---

## Отстраняване на неизправности

### Контейнерът на приложението не стартира

Проверете логовете на контейнера за съобщения за грешки:

```bash
docker compose -f docker-compose.production.yml logs rtcloud
```

Чести причини:
- Липсващи или невалидни променливи на средата в `.env`
- MySQL все още не е готов (изчакайте 60 секунди и проверете отново)
- Конфликт на портове — друг процес вече използва `APP_PORT`

### MySQL не е здрав

```bash
docker compose -f docker-compose.production.yml logs mysql
```

Чести причини:
- `MYSQL_ROOT_PASSWORD` не е зададен в `.env`
- Повреден том с данни (рядко — проверете дисковото пространство с `df -h`)

MySQL може да отнеме 30–60 секунди за инициализация при самото първо стартиране. Изчакайте и проверете отново преди да приемете, че е грешка.

### Портът вече е зает

Сменете `APP_PORT` или `SHINY_PORT` в `.env` с свободен порт, след което пресъздайте контейнерите:

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate
```

За да намерите какво използва порт на хоста:

```bash
lsof -i :8080
```

### 400 CSRF Token Could Not Be Verified

Тази грешка се появява в локална или обратно-проксирана среда, където произходът на заявката не съответства на очаквания хост. Деактивирайте CSRF валидирането само за локална разработка:

```dotenv
CSRF_VALIDATION_ENABLED=false
```

След това рестартирайте приложението:

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

> Не деактивирайте CSRF валидирането в производствена среда. Ако тази грешка се появи в производствена среда, уверете се, че обратният прокси препраща правилните хедъри `Host` и `X-Forwarded-For`.

### Забравена парола за администратор

Нулирайте паролата на администратора директно в базата данни. Свържете се с MySQL контейнера и актуализирайте хеша на паролата:

**Стъпка 1** — Генерирайте новия хеш на паролата. Заменете `newpassword` с желаната парола:

```bash
docker compose -f docker-compose.production.yml exec rtcloud php -r "
  \$salt = trim(shell_exec(\"mysql -h mysql -u root -p\\\"\${MYSQL_ROOT_PASSWORD}\\\" \${MYSQL_DATABASE} -se \\\"SELECT salt FROM ss_user WHERE username='admin';\\\"\"));
  echo md5(\$salt . 'newpassword') . PHP_EOL;
"
```

**Стъпка 2** — Актуализирайте хеша в базата данни:

```bash
docker compose -f docker-compose.production.yml exec mysql \
  mysql -u root -p"${MYSQL_ROOT_PASSWORD}" smartsurvey \
  -e "UPDATE ss_user SET password='<hash_from_step_1>' WHERE username='admin';"
```

### Контейнерът продължава да се рестартира

Проверете дали проверката на здравето се проваля:

```bash
docker compose -f docker-compose.production.yml ps
docker inspect rtcloud-app --format '{{json .State.Health}}'
```

Проверката на здравето на приложението извиква крайната точка `/health`. Ако се проваля многократно, проверете логовете на приложението за грешки при стартиране.

### Дискът е запълнен

Идентифицирайте какво изразходва пространство:

```bash
# Проверка на използването на диска на хоста
df -h

# Проверка на използването на диска от Docker (образи, контейнери, томове)
docker system df

# Премахване на неизползвани образи и спрени контейнери (безопасно за изпълнение)
docker system prune
```

Не използвайте `docker system prune --volumes`, тъй като това ще изтрие данните на приложението.

---

## Проверки на здравето

Всяка услуга има автоматична проверка на здравето. Статусът на контейнера отразява резултата:

| Контейнер | Метод на проверка | Начален период | Интервал |
|-----------|-------------|-------------|----------|
| `rtcloud-app` | HTTP GET `/health` | 90 секунди | 30 секунди |
| `rtcloud-mysql` | `mysqladmin ping` | 30 секунди | 10 секунди |
| `rtcloud-keycloak` | HTTP GET `:9000/health/live` | 120 секунди | 30 секунди |

Контейнерите с неуспешна проверка на здравето се рестартират автоматично съгласно настройката `RESTART_POLICY` (по подразбиране: `unless-stopped`).
