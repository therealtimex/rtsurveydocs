---
weight: 5
title: "Обслуживание"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "build"
toc: true
description: "Повседневное обслуживание самостоятельно размещённого экземпляра rtCloud: обновление, резервное копирование, восстановление и устранение распространённых проблем."
---

## Основные команды

Используйте эти команды регулярно для управления контейнерами rtCloud. Выполняйте их из каталога, содержащего `docker-compose.production.yml`.

```bash
# Проверить состояние и здоровье всех контейнеров
docker compose -f docker-compose.production.yml ps

# Просмотреть живые журналы (все сервисы)
docker compose -f docker-compose.production.yml logs -f

# Просмотреть журналы только приложения
docker compose -f docker-compose.production.yml logs -f rtcloud

# Перезапустить один контейнер
docker compose -f docker-compose.production.yml restart rtcloud

# Остановить все сервисы
docker compose -f docker-compose.production.yml down

# Запустить все сервисы
docker compose -f docker-compose.production.yml up -d

# Открыть оболочку внутри контейнера приложения
docker compose -f docker-compose.production.yml exec rtcloud bash
```

---

## Обновление

Обновления rtCloud распространяются как новые теги образов Docker. Обновление загружает последний образ и пересоздаёт контейнер приложения. Миграции базы данных запускаются автоматически при старте.

**1. Загрузите последний образ:**

```bash
docker compose -f docker-compose.production.yml pull
```

**2. Пересоздайте контейнер приложения:**

```bash
docker compose -f docker-compose.production.yml up -d
```

Docker заменяет только контейнеры, образ которых изменился. Контейнер MySQL и все именованные тома остаются нетронутыми.

### Фиксация версии

Для обновления до конкретной версии вместо `latest` обновите `RTCLOUD_IMAGE` в `.env`:

```dotenv
RTCLOUD_IMAGE=rtawebteam/rta-smartsurvey:1.2.3
```

Затем выполните `docker compose pull` и `up -d` как описано выше.

### Откат версии

Откат, как правило, не рекомендуется, так как миграции базы данных необратимы. При необходимости откатитесь, восстановив резервную копию базы данных, сделанную до обновления.

---

## Резервное копирование и восстановление

### Резервное копирование базы данных

Выполните эту команду для экспорта базы данных приложения в SQL-файл:

```bash
docker compose -f docker-compose.production.yml exec mysql \
  mysqldump -u root -p"$(grep MYSQL_ROOT_PASSWORD .env | cut -d= -f2)" smartsurvey \
  > backup-$(date +%Y%m%d-%H%M%S).sql
```

Файл резервной копии записывается в текущий каталог на хосте.

### Восстановление базы данных

```bash
docker compose -f docker-compose.production.yml exec -T mysql \
  mysql -u root -p"$(grep MYSQL_ROOT_PASSWORD .env | cut -d= -f2)" smartsurvey \
  < backup-20240101-120000.sql
```

### Резервное копирование загруженных файлов

Ответы на опросы часто включают загруженные файлы (фото, аудио, документы), хранящиеся в именованных томах Docker. Создавайте их резервные копии отдельно от базы данных:

```bash
# Резервное копирование загрузок
docker run --rm \
  -v rtcloud_uploads:/data \
  -v "$(pwd):/backup" \
  alpine tar czf /backup/uploads-$(date +%Y%m%d).tar.gz -C /data .

# Резервное копирование аудиозаписей
docker run --rm \
  -v rtcloud_audios:/data \
  -v "$(pwd):/backup" \
  alpine tar czf /backup/audios-$(date +%Y%m%d).tar.gz -C /data .
```

Замените `rtcloud_uploads` и `rtcloud_audios` на фактические имена томов (с префиксом `COMPOSE_PROJECT_NAME`), если вы изменили значение по умолчанию.

### Восстановление загруженных файлов

```bash
docker run --rm \
  -v rtcloud_uploads:/data \
  -v "$(pwd):/backup" \
  alpine tar xzf /backup/uploads-20240101.tar.gz -C /data
```

### Автоматическое ежедневное резервное копирование

Добавьте задание cron на хосте для автоматического резервного копирования. Отредактируйте crontab root с помощью `crontab -e`:

```cron
# Ежедневное резервное копирование базы данных в 2:00, хранение 30 дней
0 2 * * * cd /opt/rtcloud && docker compose -f docker-compose.production.yml exec -T mysql \
  mysqldump -u root -p"$(grep MYSQL_ROOT_PASSWORD .env | cut -d= -f2)" smartsurvey \
  > /backups/db-$(date +\%Y\%m\%d).sql && \
  find /backups -name "db-*.sql" -mtime +30 -delete
```

---

## Устранение неполадок

### Контейнер приложения не запускается

Проверьте журналы контейнера на наличие сообщений об ошибках:

```bash
docker compose -f docker-compose.production.yml logs rtcloud
```

Распространённые причины:
- Отсутствующие или недействительные переменные окружения в `.env`
- MySQL ещё не готов (подождите 60 секунд и проверьте снова)
- Конфликт портов — другой процесс уже использует `APP_PORT`

### MySQL не работает корректно

```bash
docker compose -f docker-compose.production.yml logs mysql
```

Распространённые причины:
- `MYSQL_ROOT_PASSWORD` не установлен в `.env`
- Повреждённый том данных (редко — проверьте место на диске с `df -h`)

MySQL может занять 30–60 секунд для инициализации при самом первом запуске. Подождите и проверьте снова, прежде чем делать вывод об ошибке.

### Порт уже используется

Измените `APP_PORT` или `SHINY_PORT` в `.env` на свободный порт, затем пересоздайте контейнеры:

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate
```

Чтобы узнать, что использует порт на хосте:

```bash
lsof -i :8080
```

### Ошибка 400 CSRF Token Could Not Be Verified

Эта ошибка появляется в локальных средах или средах с обратным прокси, где источник запроса не совпадает с ожидаемым хостом. Отключите проверку CSRF только для локальной разработки:

```dotenv
CSRF_VALIDATION_ENABLED=false
```

Затем перезапустите приложение:

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

> Не отключайте проверку CSRF в производственной среде. Если эта ошибка возникает в производственной среде, убедитесь, что обратный прокси правильно передаёт заголовки `Host` и `X-Forwarded-For`.

### Забыт пароль администратора

Сбросьте пароль администратора напрямую в базе данных. Подключитесь к контейнеру MySQL и обновите хеш пароля:

**Шаг 1** — Сгенерируйте новый хеш пароля. Замените `newpassword` желаемым паролем:

```bash
docker compose -f docker-compose.production.yml exec rtcloud php -r "
  \$salt = trim(shell_exec(\"mysql -h mysql -u root -p\\\"\${MYSQL_ROOT_PASSWORD}\\\" \${MYSQL_DATABASE} -se \\\"SELECT salt FROM ss_user WHERE username='admin';\\\"\"));
  echo md5(\$salt . 'newpassword') . PHP_EOL;
"
```

**Шаг 2** — Обновите хеш в базе данных:

```bash
docker compose -f docker-compose.production.yml exec mysql \
  mysql -u root -p"${MYSQL_ROOT_PASSWORD}" smartsurvey \
  -e "UPDATE ss_user SET password='<hash_from_step_1>' WHERE username='admin';"
```

### Контейнер постоянно перезапускается

Проверьте, не завершается ли проверка состояния с ошибкой:

```bash
docker compose -f docker-compose.production.yml ps
docker inspect rtcloud-app --format '{{json .State.Health}}'
```

Проверка состояния приложения обращается к конечной точке `/health`. При повторных сбоях проверьте журналы приложения на наличие ошибок запуска.

### Диск переполнен

Определите, что занимает место:

```bash
# Проверить использование диска хоста
df -h

# Проверить использование диска Docker (образы, контейнеры, тома)
docker system df

# Удалить неиспользуемые образы и остановленные контейнеры (безопасно)
docker system prune
```

Не используйте `docker system prune --volumes`, так как это удалит данные приложения.

---

## Проверки состояния

Каждый сервис имеет автоматическую проверку состояния. Статус контейнера отражает её результат:

| Контейнер | Метод проверки | Период запуска | Интервал |
|-----------|-------------|-------------|----------|
| `rtcloud-app` | HTTP GET `/health` | 90 секунд | 30 секунд |
| `rtcloud-mysql` | `mysqladmin ping` | 30 секунд | 10 секунд |
| `rtcloud-keycloak` | HTTP GET `:9000/health/live` | 120 секунд | 30 секунд |

Контейнеры с неудачной проверкой состояния автоматически перезапускаются в соответствии с настройкой `RESTART_POLICY` (по умолчанию: `unless-stopped`).
