---
weight: 1
title: "DigitalOcean"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-17T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "water_drop"
toc: true
description: "Deploy rtCloud on a DigitalOcean Droplet using automated user-data scripts."
---

DigitalOcean uses **User Data** scripts that run automatically on first boot. You fill in the configuration variables at the top of the script, then paste the entire script when creating a Droplet.

> На відміну від Linode StackScripts, DigitalOcean не має інтерфейсу користувача форми — ви повинні редагувати сценарій безпосередньо перед вставленням.

**Download script:** [digitalocean-droplet-keycloak-embed.sh](/scripts/digitalocean-droplet-keycloak-embed.sh)

---

## Вбудований Keycloak (рекомендовано)

Використовуйте `digitalocean-droplet-keycloak-embed.sh` для найпростішого налаштування з вбудованим SSO.

### Крок 1 — Заповніть конфігурацію

Відкрийте скрипт і відредагуйте блок `CONFIGURATION` у верхній частині:

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

| Поле | Необхідно | Опис |
|-------|----------|------------|
| `PROJECT_ID` | Так | Використовується як назва бази даних і ідентифікатор клієнта Keycloak. Малі літери, без пробілів. |
| `ПАРОЛЬ_АДМІНІСТРАТОРА` | Ні | Пароль для входу адміністратора програми та консолі адміністратора Keycloak. За замовчуванням `admin` — **змінити після першого входу**. |
| `ДОМЕН` | Так | Ваше доменне ім'я. Запис DNS має вказувати на IP-адресу Droplet. |
| `LETSENCRYPT_EMAIL` | Так | Електронна адреса для сповіщень про сертифікат Let's Encrypt. |
| `PROJECT_URL` | Ні | Перевизначте загальнодоступну URL-адресу. Залиште поле порожнім, щоб використовувати `DOMAIN`. Корисно поза Cloudflare. |

> **Безпека:** Усі паролі за замовчуванням `admin`. Змініть їх одразу після першого входу.

### Крок 2 — Створіть краплю

In the [DigitalOcean control panel](https://cloud.digitalocean.com):

1. Натисніть **Створити** → **Краплі**
2. Виберіть **Ubuntu 22.04 LTS** як зображення
3. Виберіть **Базовий, 4 ГБ оперативної пам’яті / 2 vCPU** або більше
4. Прокрутіть до **Додаткові параметри** → поставте прапорець **Додати сценарії ініціалізації**
5. Вставте повний вміст сценарію в текстову область
6. Натисніть **Create Droplet**

### Крок 3 — Додайте запис DNS

Під час завантаження Droplet додайте **запис** у вашому DNS-провайдері:

```
Type  : A
Name  : myapp          (or @ for root domain)
Value : <droplet-ip>
TTL   : 300
```

### Крок 4 — Відстежуйте прогрес

SSH у Droplet і подивіться журнал:

```bash
ssh root@<droplet-ip>
tail -f /var/log/rtcloud-setup.log
```

Сценарій друкує IP-адресу вашого сервера на початку — додайте запис DNS, щойно ви його побачите.

### Крок 5 — Доступ до програми

Після завершення налаштування в журналі відобразиться підсумок:

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

> **Змініть свій пароль** відразу після входу через **Налаштування** у верхньому правому меню.

---

## Після розгортання

### Змінити пароль

SSH у Droplet, відредагуйте `.env` і перезапустіть уражений контейнер:

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Оновіть домен

Якщо ви призначаєте інший домен після розгортання, оновіть `PROJECT_URL` у `.env`:

```bash
nano /opt/rtcloud/.env   # update PROJECT_URL=
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Переглянути всі контейнери

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```
