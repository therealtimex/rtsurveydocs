---
weight: 3
title: "AWS EC2"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-16T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "cloud"
toc: true
description: "Розгортайте rtCloud на екземплярі AWS EC2 за допомогою скрипту user data aws-ec2.sh."
---

Використовуйте `aws-ec2.sh` як скрипт **User Data** при запуску екземпляру EC2. Скрипт запускається автоматично при першому завантаженні.

**Завантажити скрипт:** [aws-ec2.sh](/scripts/aws-ec2.sh)

---

## Крок 1 — Заповніть конфігурацію

Відкрийте скрипт та відредагуйте блок `CONFIGURATION` у верхній частині:

```bash
# --- Обов'язково ---
PROJECT_ID="rtsurvey"
ADMIN_PASSWORD="admin"                       # Змініть після першого входу

# --- Домен + SSL ---
DOMAIN="myapp.example.com"
LETSENCRYPT_EMAIL="admin@example.com"

# --- Вбудований Keycloak ---
EMBED_KEYCLOAK="true"
KEYCLOAK_ADMIN_PASSWORD="${ADMIN_PASSWORD}"  # За замовчуванням ADMIN_PASSWORD
```

| Поле | Обов'язково | Опис |
|-------|----------|-------------|
| `PROJECT_ID` | Так | Використовується як назва бази даних та ідентифікатор клієнта Keycloak. Лише малі літери, без пробілів. |
| `ADMIN_PASSWORD` | Ні | Пароль адміністратора застосунку та пароль адміністратора Keycloak. За замовчуванням `admin` — **змініть після першого входу**. |
| `DOMAIN` | Ні | Ваш домен для HTTPS. Залиште порожнім для режиму лише HTTP. |
| `LETSENCRYPT_EMAIL` | Так (якщо DOMAIN встановлено) | Email для сповіщень Let's Encrypt. |
| `EMBED_KEYCLOAK` | Ні | `true` для розгортання вбудованого Keycloak (потребує 4 ГБ RAM). |

> **Безпека:** Усі паролі за замовчуванням `admin`. Змініть їх негайно після першого входу.

---

## Крок 2 — Запустіть екземпляр EC2

У [консолі AWS EC2](https://console.aws.amazon.com/ec2):

1. Натисніть **Launch instance**
2. **AMI:** Ubuntu Server 22.04 LTS (64-bit x86)
3. **Instance type:** `t3.medium` (4 ГБ RAM) або більший
4. **Key pair:** Виберіть або створіть для доступу через SSH
5. **Network settings:** Створіть або виберіть Security Group (дивіться нижче)
6. **Advanced details** → **User data** → вставте повний вміст скрипту
7. Натисніть **Launch instance**

---

## Крок 3 — Налаштуйте Security Group

Відкрийте ці порти в Security Group екземпляру:

| Порт | Протокол | Джерело | Призначення |
|------|----------|--------|---------|
| 22 | TCP | Ваш IP | Доступ через SSH |
| 80 | TCP | 0.0.0.0/0 | HTTP (перенаправляється на HTTPS через Nginx) |
| 443 | TCP | 0.0.0.0/0 | HTTPS |
| 3838 | TCP | 0.0.0.0/0 | Прямий доступ до Shiny |

> **Не відкривайте** порт 3306 (MySQL) — він ніколи не повинен бути публічно доступним.

---

## Крок 4 — Додайте DNS-запис

Поки екземпляр завантажується, додайте **A-запис** у вашому постачальнику DNS:

```
Type  : A
Name  : myapp
Value : <instance-public-ip>
TTL   : 300
```

---

## Крок 5 — Відстежуйте прогрес

```bash
ssh ubuntu@<instance-ip>
tail -f /var/log/rtcloud-setup.log
```

---

## Крок 6 — Отримайте доступ до застосунку

Коли налаштування завершиться, журнал покаже підсумок з URL вашого застосунку та обліковими даними. Увійдіть з іменем користувача `admin` та паролем `admin`, потім негайно змініть свій пароль.

---

## Після розгортання

### Змінити пароль

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Переглянути всі контейнери

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```

### Призначити Elastic IP (необов'язково)

Якщо ви зупиняєте та запускаєте екземпляр, публічний IP змінюється. Щоб зберегти стабільний IP, виділіть **Elastic IP** та зв'яжіть його з екземпляром у консолі EC2.
