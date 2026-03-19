---
weight: 4
title: "SSO-аутентифікація"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "lock"
toc: true
description: "Налаштуйте єдиний вхід (SSO) для самостійного rtCloud за допомогою вбудованого Keycloak, зовнішнього постачальника OIDC або Azure Active Directory."
---

rtCloud підтримує три підходи до єдиного входу (SSO):

| Варіант | Найкраще для |
|--------|----------|
| [Вбудований Keycloak](#embedded-keycloak) | Організації, яким потрібен повністю автономний SSO-сервер, вбудований у rtCloud |
| [Зовнішній постачальник OIDC](#external-oidc-provider) | Організації, що вже використовують постачальника ідентифікаційних даних (Auth0, Authentik, Okta, Supabase тощо) |
| [Azure Active Directory](#azure-active-directory) | Організації, що використовують Microsoft 365 або Azure AD |

Без налаштованого SSO користувачі входять за допомогою локальних облікових записів rtCloud, що управляються через панель адміністратора.

---

## Вбудований Keycloak

Розгортання включає необов'язковий контейнер Keycloak, що запускається поруч з rtCloud. Keycloak попередньо налаштований з realm rtSurvey та готовий до використання.

### Вимоги

- Доменне ім'я з HTTPS (Keycloak потребує HTTPS у виробництві)
- Щонайменше 4 ГБ RAM на сервері (Keycloak додає ~512 МБ використання пам'яті)

### Налаштування

**1. Налаштуйте змінні середовища в `.env`:**

```dotenv
# Увімкнути вбудований контейнер Keycloak
EMBED_KEYCLOAK=true

# URL Keycloak — використовуйте ваш реальний домен
KEYCLOAK_URL=https://rtcloud.example.com/auth
KC_HOSTNAME=https://rtcloud.example.com/auth
KC_HOSTNAME_STRICT=false

# Налаштування realm та клієнта (відповідають імпортованому realm JSON)
KEYCLOAK_REALM=rtsurvey
KEYCLOAK_CLIENT_ID=rtsurvey-app
KEYCLOAK_CLIENT_SECRET=your-client-secret-here

# Облікові дані адміністратора Keycloak
KEYCLOAK_ADMIN_USER=admin
KEYCLOAK_ADMIN_PASSWORD=change_me_keycloak_admin_password

# База даних Keycloak (створюється автоматично)
KEYCLOAK_DB=keycloak
KEYCLOAK_DB_USER=keycloak
KEYCLOAK_DB_PASSWORD=change_me_keycloak_db_password

# Порт, на якому Keycloak прослуховує (на стороні хосту, проксується Nginx)
KEYCLOAK_PORT=8091
```

**2. Запустіть з профілем вбудованого Keycloak:**

```bash
docker compose -f docker-compose.production.yml --profile embed-keycloak up -d
```

**3. Переконайтеся, що Keycloak здоровий:**

```bash
docker compose -f docker-compose.production.yml ps
```

Контейнер `rtcloud-keycloak` повинен показати `Up (healthy)` через 2–3 хвилини.

**4. Отримайте доступ до консолі адміністратора Keycloak:**

```
https://rtcloud.example.com/auth/admin
```

Увійдіть з `KEYCLOAK_ADMIN_USER` та `KEYCLOAK_ADMIN_PASSWORD`.

### Що попередньо налаштовано

Вбудований Keycloak запускається з попередньо імпортованим realm `rtsurvey`, що включає:

- Конфігурацію клієнта для веб-застосунку
- Ролі користувачів за замовчуванням (`admin`, `project_manager`, `enumerator`, `analyst`)
- Налаштування сесії та токена, оптимізовані для rtSurvey

Ви можете додавати користувачів безпосередньо в консолі адміністратора Keycloak або підключити Keycloak до постачальника ідентифікаційних даних (LDAP, SAML).

### Маршрутизація Nginx

При використанні скриптів хмарного розгортання Nginx налаштований для проксування обох сервісів:

| Шлях | Бекенд |
|------|---------|
| `/` | Застосунок rtCloud на `127.0.0.1:8080` |
| `/auth/` | Keycloak на `127.0.0.1:8090` |

---

## Зовнішній постачальник OIDC

Підключіть rtCloud до будь-якого постачальника ідентифікаційних даних, сумісного з OpenID Connect. Цей підхід не потребує контейнера Keycloak.

### Підтримувані постачальники

Будь-який сумісний з OIDC постачальник, включаючи:
- Authentik
- Auth0
- Okta
- Keycloak (зовнішній екземпляр)
- Supabase
- Google (для організацій Google Workspace)
- GitHub (через OAuth apps з розширенням OIDC)

### Налаштування

**1. Зареєструйте rtCloud як OIDC-клієнт у вашому постачальнику ідентифікаційних даних.**

Вам знадобляться:
- **Ідентифікатор клієнта** та **секрет клієнта**
- Реєстрація **URI перенаправлення**: `https://rtcloud.example.com/auth/callback`
- Для підтримки мобільного додатку також зареєструйте: `vn.rta.rtsurvey.auth://callback`

**2. Налаштуйте змінні середовища в `.env`:**

```dotenv
# URL виявлення OIDC (специфічний для постачальника — перевірте документацію вашого IdP)
OIDC_ISSUER_URL=https://your-identity-provider.com

# Облікові дані клієнта від вашого постачальника ідентифікаційних даних
OIDC_CLIENT_ID=rtcloud-app
OIDC_CLIENT_SECRET=your-client-secret-here

# Запитувані permissions (openid, profile та email зазвичай достатньо)
OIDC_SCOPE=openid profile email

# URI перенаправлення, зареєстрований у вашому постачальнику ідентифікаційних даних
OIDC_REDIRECT_URI=https://rtcloud.example.com/auth/callback

# Необов'язково: окремий клієнт мобільного додатку
OIDC_MOBILE_CLIENT_ID=rtcloud-mobile
OIDC_MOBILE_REDIRECT_URI=vn.rta.rtsurvey.auth://callback

# Встановіть true для автоматичного створення облікових записів rtCloud для нових OIDC-користувачів
OPEN_REGISTRATION=false
```

**3. Перезапустіть контейнер застосунку для застосування змін:**

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

### Автоматичне провізіонування користувачів

Коли `OPEN_REGISTRATION=true`, rtCloud автоматично створює локальний обліковий запис при першому вході користувача через OIDC. Обліковий запис заповнюється іменем та email користувача з ID-токена.

Коли `OPEN_REGISTRATION=false` (за замовчуванням), адміністратор rtCloud повинен спочатку створити обліковий запис, а ідентифікатор OIDC зв'язується при першому вході.

### Користувацькі кінцеві точки

Якщо ваш постачальник не підтримує виявлення OIDC (`.well-known/openid-configuration`), ви можете встановити кінцеві точки вручну:

```dotenv
OIDC_AUTHORIZATION_ENDPOINT=https://your-provider.com/oauth2/authorize
OIDC_TOKEN_ENDPOINT=https://your-provider.com/oauth2/token
OIDC_USERINFO_ENDPOINT=https://your-provider.com/oauth2/userinfo
```

---

## Azure Active Directory

Інтегруйте rtCloud з тенантом Microsoft Azure AD вашої організації.

### Налаштування

**1. Зареєструйте новий застосунок на [Порталі Azure](https://portal.azure.com):**

   - Перейдіть до **Azure Active Directory** → **App registrations** → **New registration**
   - Назва: `rtCloud`
   - URI перенаправлення: `https://rtcloud.example.com/auth/callback` (тип Web)
   - Після створення запишіть **Application (client) ID** та **Directory (tenant) ID**
   - У розділі **Certificates & secrets** створіть новий секрет клієнта

**2. Налаштуйте змінні середовища в `.env`:**

```dotenv
AZURE_CLIENT_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
AZURE_TENANT_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

**3. Перезапустіть контейнер застосунку:**

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

Користувачі у вашому тенанті Azure AD тепер можуть входити в rtCloud за допомогою своїх облікових даних Microsoft.

---

## Вимкнення SSO

Щоб повернутися до локальної аутентифікації, видаліть або закоментуйте всі змінні, пов'язані з SSO, у `.env`, потім перезапустіть контейнер застосунку:

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

Якщо ви використовували вбудований Keycloak, зупиніть його, опустивши прапор `--profile embed-keycloak` та запустивши `docker compose down`, а потім `up -d` без профілю.
