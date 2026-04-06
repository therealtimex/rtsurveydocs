---
weight: 1
title: "DigitalOcean"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-17T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "water_drop"
toc: true
description: "Примените ртЦлоуд на ДигиталОцеан Дроплет користећи аутоматизоване скрипте за корисничке податке."
---

ДигиталОцеан користи **Корисничке податке** скрипте које се покрећу аутоматски при првом покретању. Попуните променљиве конфигурације на врху скрипте, а затим налепите целу скрипту када креирате Дроплет.

> За разлику од Линоде СтацкСцриптс-а, ДигиталОцеан нема корисничко сучеље обрасца — морате да уредите скрипту директно пре лепљења.

**Download script:** [digitalocean-droplet-keycloak-embed.sh](/scripts/digitalocean-droplet-keycloak-embed.sh)

---

## Ембеддед Кеицлоак (препоручено)

Користите `дигиталоцеан-дроплет-кеицлоак-ембед.сх` за најједноставније подешавање са уграђеним ССО-ом.

### Корак 1 — Попуните конфигурацију

Отворите скрипту и уредите блок `ЦОНФИГУРАТИОН` на врху:

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

| Поље | Обавезно | Опис |
|-------|----------|------------|
| `ПРОЈЕЦТ_ИД` | Да | Користи се као име базе података и ИД клијента Кеицлоак. Мала слова, без размака. |
| `АДМИН_ПАССВОРД` | Не | Лозинка за пријаву администратора апликације и администраторску конзолу Кеицлоак. Подразумевано је `админ` — **промена након првог пријављивања**. |
| `ДОМАИН` | Да | Име вашег домена. ДНС Запис мора да указује на ИП адресу капљице. |
| `ЛЕТСЕНЦРИПТ_ЕМАИЛ` | Да | Адреса е-поште за обавештења о сертификатима Лет'с Енцрипт. |
| `ПРОЈЕЦТ_УРЛ` | Не | Замени јавни УРЛ. Оставите празно да бисте користили `ДОМАИН`. Корисно иза Цлоудфлареа. |

> **Безбедност:** Све лозинке су подразумеване на `админ`. Промените их одмах након првог пријављивања.

### Корак 2 — Креирајте капљицу

In the [DigitalOcean control panel](https://cloud.digitalocean.com):

1. Кликните на **Креирај** → **Капљице**
2. Изаберите **Убунту 22.04 ЛТС** као слику
3. Изаберите **Основни, 4 ГБ РАМ-а / 2 вЦПУ-а** или већи
4. Померите се до **Напредне опције** → означите **Додај скрипте за иницијализацију**
5. Paste the full script content into the text area
6. Кликните на **Креирај капљицу**

### Корак 3 — Додајте ДНС запис

Док се Дроплет покреће, додајте **А запис** у свој ДНС провајдер:

```
Type  : A
Name  : myapp          (or @ for root domain)
Value : <droplet-ip>
TTL   : 300
```

### Корак 4 — Пратите напредак

ССХ у Дроплет и погледајте дневник:

```bash
ssh root@<droplet-ip>
tail -f /var/log/rtcloud-setup.log
```

Скрипта штампа ИП вашег сервера близу почетка — додајте ДНС запис чим га видите.

### Корак 5 — Приступите апликацији

Када се подешавање заврши, дневник приказује резиме:

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

> **Промените своју лозинку** одмах након пријављивања преко **Подешавања** у горњем десном менију.

---

## Након распоређивања

### Промените лозинку

ССХ у Дроплет, уредите `.енв` и поново покрените погођени контејнер:

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Ажурирајте домен

Ако доделите други домен након примене, ажурирајте `ПРОЈЕЦТ_УРЛ` у `.енв`:

```bash
nano /opt/rtcloud/.env   # update PROJECT_URL=
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Погледај све контејнере

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```
