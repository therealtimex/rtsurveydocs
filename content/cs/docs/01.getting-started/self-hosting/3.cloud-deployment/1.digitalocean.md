---
weight: 1
title: "DigitalOcean"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-17T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "water_drop"
toc: true
description: "Nasazení rtCloud na DigitalOcean Droplet pomocí automatizovaných skriptů user-data."
---

DigitalOcean používá **User Data** skripty, které se automaticky spouštějí při prvním spuštění. Konfigurační proměnné vyplníte v horní části skriptu, poté celý skript vložíte při vytváření Droplet.

> Na rozdíl od Linode StackScripts nemá DigitalOcean formulářové UI — skript musíte upravit přímo před vložením.

**Stáhnout skript:** [digitalocean-droplet-keycloak-embed.sh](/scripts/digitalocean-droplet-keycloak-embed.sh)

---

## Vložený Keycloak (doporučeno)

Použijte `digitalocean-droplet-keycloak-embed.sh` pro nejjednodušší nastavení s vestavěným SSO.

### Krok 1 — Vyplňte konfiguraci

Otevřete skript a upravte blok `CONFIGURATION` v horní části:

```bash
# --- Povinné ---
PROJECT_ID="rtsurvey"                  # Jedinečný identifikátor projektu (bez mezer)
ADMIN_PASSWORD="admin"                 # Heslo pro admin aplikace a Keycloak — změňte po prvním přihlášení

# --- Doména + SSL ---
DOMAIN="myapp.example.com"            # Vaše doména — DNS A záznam musí ukazovat sem
PROJECT_URL=""                         # Ponechte prázdné, pokud nejste za Cloudflare/proxy
LETSENCRYPT_EMAIL="admin@example.com" # E-mail pro oznámení Let's Encrypt

# --- Volitelné ---
STATA_ENABLED="false"
TZ="Asia/Ho_Chi_Minh"
```

| Pole | Povinné | Popis |
|-------|----------|-------------|
| `PROJECT_ID` | Ano | Používá se jako název databáze a ID klienta Keycloak. Malá písmena, bez mezer. |
| `ADMIN_PASSWORD` | Ne | Heslo pro přihlášení admin aplikace a administrátorskou konzoli Keycloak. Výchozí je `admin` — **změňte po prvním přihlášení**. |
| `DOMAIN` | Ano | Váš název domény. DNS A záznam musí ukazovat na IP adresy Droplet. |
| `LETSENCRYPT_EMAIL` | Ano | E-mailová adresa pro oznámení certifikátu Let's Encrypt. |
| `PROJECT_URL` | Ne | Přepsání veřejné URL. Ponechte prázdné pro použití `DOMAIN`. Užitečné za Cloudflare. |

> **Bezpečnost:** Všechna hesla mají výchozí hodnotu `admin`. Změňte je ihned po prvním přihlášení.

### Krok 2 — Vytvořte Droplet

V [ovládacím panelu DigitalOcean](https://cloud.digitalocean.com):

1. Klikněte na **Vytvořit** → **Droplety**
2. Vyberte **Ubuntu 22.04 LTS** jako obraz
3. Vyberte **Basic, 4 GB RAM / 2 vCPU** nebo větší
4. Přejděte na **Pokročilé možnosti** → zaškrtněte **Přidat inicializační skripty**
5. Vložte celý obsah skriptu do textového pole
6. Klikněte na **Vytvořit Droplet**

### Krok 3 — Přidejte DNS záznam

Zatímco Droplet startuje, přidejte **A záznam** u vašeho poskytovatele DNS:

```
Typ  : A
Název: myapp          (nebo @ pro kořenovou doménu)
Hodnota: <droplet-ip>
TTL  : 300
```

### Krok 4 — Sledujte průběh

Přihlaste se přes SSH do Dropletu a sledujte protokol:

```bash
ssh root@<droplet-ip>
tail -f /var/log/rtcloud-setup.log
```

Skript vypíše IP adresu serveru na začátku — přidejte DNS záznam, jakmile ji uvidíte.

### Krok 5 — Přístup k aplikaci

Po dokončení nastavení protokol zobrazí souhrn:

```
============================================================
 Nasazení rtCloud dokončeno! (Vložený Keycloak)
============================================================
 URL aplikace   : https://myapp.example.com
 Admin          : admin / admin
 Keycloak       : https://myapp.example.com/auth/admin

 !! BEZPEČNOST: Všechna hesla mají výchozí hodnotu 'admin'.
    Změňte je ihned po prvním přihlášení.
============================================================
```

Otevřete `https://myapp.example.com` v prohlížeči a přihlaste se uživatelským jménem `admin` a heslem `admin`.

> **Změňte heslo** ihned po přihlášení přes **Nastavení** v menu v pravém horním rohu.

---

## Po nasazení

### Změna hesla

Přihlaste se přes SSH do Dropletu, upravte `.env` a restartujte příslušný kontejner:

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Aktualizace domény

Pokud po nasazení přiřadíte jinou doménu, aktualizujte `PROJECT_URL` v `.env`:

```bash
nano /opt/rtcloud/.env   # aktualizujte PROJECT_URL=
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Zobrazení všech kontejnerů

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```
