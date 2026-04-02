---
weight: 1
title: "ЦифровойОкеан"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-17T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "water_drop"
toc: true
description: "Разверните rtCloud в дроплете DigitalOcean с помощью автоматизированных сценариев пользовательских данных."
---

DigitalOcean использует сценарии **Пользовательские данные**, которые запускаются автоматически при первой загрузке. Вы заполняете переменные конфигурации в верхней части скрипта, а затем вставляете весь скрипт при создании капли.

> В отличие от Linode StackScripts, DigitalOcean не имеет пользовательского интерфейса формы — вам необходимо отредактировать скрипт непосредственно перед вставкой.

**Download script:** [digitalocean-droplet-keycloak-embed.sh](/scripts/digitalocean-droplet-keycloak-embed.sh)

---

## Встроенный Keycloak (рекомендуется)

Используйте «digitalocean-droplet-keycloak-embed.sh» для простейшей настройки со встроенным единым входом.

### Шаг 1 — Заполняем конфигурацию

Откройте скрипт и отредактируйте блок `CONFIGURATION` вверху:

```bash
# --- Required ---
PROJECT_ID="rtsurvey"                  # Unique identifier for your project (no spaces)
ADMIN_PASSWORD="admin"                 # Password for app admin and Keycloak — change after first login

# --- Domain + SSL ---
DOMAIN="myapp.example.com"            # Your domain — DNS A record must point here
PROJECT_URL=""                         # Leave blank unless behind Cloudflare/proxy
LETSENCRYPT_EMAIL="admin@example.com" # Email for Let's Encrypt notifications

# --- Optional ---
STATA_ENABLED="false"
TZ="Asia/Ho_Chi_Minh"
```

| Поле | Требуется | Описание |
|-------|----------|-------------|
| `PROJECT_ID` | Да | Используется в качестве имени базы данных и идентификатора клиента Keycloak. Строчные буквы, без пробелов. |
| `ADMIN_PASSWORD` | Нет | Пароль для входа в систему администратора приложения и консоли администратора Keycloak. По умолчанию «admin» — **изменяется после первого входа**. |
| `ДОМЕН` | Да | Ваше доменное имя. DNS-запись должна указывать на IP-адрес капли. |
| `LETSENCRYPT_EMAIL` | Да | Адрес электронной почты для уведомлений о сертификатах Let's Encrypt. |
| `PROJECT_URL` | Нет | Переопределить общедоступный URL-адрес. Оставьте пустым, чтобы использовать «ДОМЕН». Полезно после Cloudflare. |

> **Безопасность:** Все пароли по умолчанию — «admin». Измените их сразу после первого входа в систему.

### Шаг 2 — Создайте дроплет

In the [DigitalOcean control panel](https://cloud.digitalocean.com):

1. Нажмите **Создать** → **Капли**.
2. Выберите **Ubuntu 22.04 LTS** в качестве изображения.
3. Выберите **Базовый, 4 ГБ ОЗУ / 2 виртуальных ЦП** или больше.
4. Прокрутите до пункта **Дополнительные параметры** → установите флажок **Добавить сценарии инициализации**.
5. Вставьте полное содержимое скрипта в текстовую область.
6. Нажмите **Создать дроплет**.

### Шаг 3 — Добавьте запись DNS

Пока дроплет загружается, добавьте запись **A** в свой DNS-провайдер:

```
Type  : A
Name  : myapp          (or @ for root domain)
Value : <droplet-ip>
TTL   : 300
```

### Шаг 4. Отслеживайте прогресс

Подключитесь к дроплету по SSH и посмотрите журнал:

```bash
ssh root@<droplet-ip>
tail -f /var/log/rtcloud-setup.log
```

Скрипт печатает IP-адрес вашего сервера в начале — добавьте запись DNS, как только увидите ее.

### Шаг 5 — Доступ к приложению

По завершении установки в журнале отображается сводная информация:

```
============================================================
 rtCloud deployment complete! (Embedded Keycloak)
============================================================
 App URL   : https://myapp.example.com
 Admin     : admin / admin
 Keycloak  : https://myapp.example.com/auth/admin

 !! SECURITY: All passwords default to 'admin'.
    Change them immediately after first login.
============================================================
```

Open `https://myapp.example.com` in your browser and log in with username `admin` and password `admin`.

> **Измените свой пароль** сразу после входа в систему через **Настройки** в правом верхнем углу.

---

## После развертывания

### Сменить пароль

SSH into the Droplet, edit `.env`, and restart the affected container:

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Обновите домен

Если вы назначаете другой домен после развертывания, обновите PROJECT_URL в .env:

```bash
nano /opt/rtcloud/.env   # update PROJECT_URL=
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Просмотреть все контейнеры

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```
