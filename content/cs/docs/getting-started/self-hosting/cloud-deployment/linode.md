---
weight: 2
title: "Linode (Akamai Cloud)"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-17T01:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "dns"
toc: true
description: "Nasazení rtCloud na Linode pomocí StackScripts s formulářovým UI pro konfiguraci."
---

Linode používá **StackScripts** — skripty s formulářovým UI, kde vyplníte konfigurační pole přímo v Linode Manageru bez úpravy kódu.

> Linode StackScripts jsou nejjednodušší metodou nasazení. Pole se zobrazí jako formulář při vytváření Linodu — není potřeba úprava skriptu.

---

## Vložený Keycloak (doporučeno)

### Krok 1 — Najděte StackScript

StackScript je veřejně dostupný v komunitě Linode — není potřeba ruční nastavení:

1. Přejděte na **Linodes** → **Vytvořit Linode**
2. Pod **Vybrat distribuci** vyberte **StackScripts** → **Komunitní StackScripts**
3. Vyhledejte **`RTA rtSurvey - Self-Hosted with Keycloak SSO`**
4. Vyberte ho a vyplňte konfigurační formulář:

> Případně si [stáhněte skript](/scripts/linode-stackscript-keycloak-embed.sh) a vytvořte vlastní StackScript pod **StackScripts** → **Vytvořit StackScript**.

| Pole | Povinné | Popis |
|-------|----------|-------------|
| Project ID | Ne | Jedinečný identifikátor (výchozí: `rtsurvey`). Používá se jako název databáze a ID klienta Keycloak. |
| Keycloak Admin Password | Ne | Heslo pro administrátorskou konzoli Keycloak i přihlášení do admin aplikace. Výchozí je `admin` — **změňte po prvním přihlášení**. |
| Domain | Ano | Název vaší domény. DNS A záznam musí ukazovat na IP adresu tohoto Linodu. Vyžadováno pro HTTPS a Keycloak. |
| Let's Encrypt Email | Ano | E-mail pro oznámení certifikátu Let's Encrypt. |
| Docker Image Tag | Ne | Obraz k nasazení (výchozí: `rtawebteam/rta-smartsurvey:survey-dockerize`). |

> **Bezpečnost:** Všechna hesla mají výchozí hodnotu `admin`. Změňte je ihned po prvním přihlášení.

5. Vyberte **Ubuntu 22.04 LTS** jako obraz
6. Vyberte plán **Shared CPU 4 GB** nebo větší
7. Klikněte na **Vytvořit Linode**

### Krok 2 — Přidejte DNS záznam

Zatímco Linode startuje, přidejte **A záznam** u vašeho poskytovatele DNS:

```
Typ  : A
Název: myapp          (nebo @ pro kořenovou doménu)
Hodnota: <linode-ip>
TTL  : 300
```

### Krok 3 — Sledujte průběh

```bash
ssh root@<linode-ip>
tail -f /var/log/stackscript.log
```

Skript vypíše IP adresu serveru na začátku — přidejte DNS záznam, jakmile ji uvidíte.

### Krok 4 — Přístup k aplikaci

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

Přihlaste se uživatelským jménem `admin` a heslem `admin`, poté ihned změňte heslo.

---

## Po nasazení

### Změna hesla

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Zobrazení všech kontejnerů

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```

### Kontrola protokolu

```bash
tail -200 /var/log/stackscript.log
```
