---
weight: 2
title: "Linode (Akamai felhő)"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "dns"
toc: true
description: "Telepítse az rtCloud-ot a Linode-on StackScript használatával. Nincs szükség konfigurációra – csak hozza létre a kiszolgálót, és kövesse a telepítés utáni lépéseket."
---

## 1. lépés – Indítsa el a StackScriptet

**[Deploy rtSurvey on Linode →](https://cloud.linode.com/stackscripts/2049143)**

Ezzel megnyílik a StackScript oldal a Linode Cloud Managerben. Kattintson az **Új Linode telepítése** lehetőségre.

---

## 2. lépés – Töltse ki a Linode űrlapját

Töltse ki a Linode szabványos szerverlétrehozási űrlapját:

| Mező | Ajánlott érték |
|-------|-------------------|
| **Kép** | Ubuntu 22.04 LTS |
| **Régió** | Legközelebb a felhasználókhoz |
| **Terv** | Megosztott CPU 4 GB vagy nagyobb |
| **Root jelszó** | Állítson be erős jelszót |
| **Időzóna** *(egyetlen mezőnk)* | A szerver időzónája (alapértelmezett: `Ázsia/Ho_Chi_Minh`) |

Ha elkészült, kattintson a **Linode létrehozása** gombra.

---

## 3. lépés – Várja meg, amíg a beállítás befejeződik

A szkript automatikusan lefut az első rendszerindításkor. Telepíti a Dockert, lekéri az rtSurvey képfájlt, inicializálja az adatbázist, és elindítja az összes szolgáltatást. Ez **5–10 percet** vesz igénybe.

Közvetlenül a **Linode Cloud Managerben** követheti a folyamatot – nincs szükség SSH-ra:

1. Go to your [Linode dashboard](https://cloud.linode.com/linodes)
2. Kattintson az újonnan létrehozott Linode-jára
3. Kattintson a **A LISH Console indítása** elemre (a Linode részletes oldalának jobb felső sarkában).

Megnyílik egy böngészőterminál, amely az élő rendszerindítási naplót mutatja – a **Weblish** lap közvetlenül a böngészőben működik, nincs szükség SSH-kliensre.

![Lish Console showing rtSurvey StackScript running](/img/first-login/lish-console.png)

Várj, amíg meglátod:

```
============================================================
 rtSurvey deployment complete!
============================================================
 Server IP : <your-server-ip>

 App URL   : http://<your-server-ip>  (HTTP only until domain is set)
 Admin     : admin / admin
============================================================
```

A naplóban megjelenik a szerver IP-címe is – a következő lépéshez szüksége lesz rá.

---

## 4. lépés – Az SSL beállítása

Open your browser at `http://<server-ip>`. The app will redirect you to the SSL setup screen.

Kövesse az **[SSL beállítási útmutató →](../ssl-setup)** című részt a HTTPS konfigurálásához. Az ingyenes **rsurvey.com aldomain** a leggyorsabb lehetőség – nincs szükség DNS-beállításra.

---

## 5. lépés – Első bejelentkezés

Ha az SSL aktív, kövesse az **[Első bejelentkezési útmutató →](../first-login)** című részt az adminisztrátori fiók eléréséhez.

---

## 6. lépés – Módosítsa az alapértelmezett jelszót

Minden jelszó alapértelmezés szerint "admin". Módosítsa őket közvetlenül az első bejelentkezés után:

- **Alkalmazásadminisztrátori jelszó** - fiókbeállítások az alkalmazáson belül
- **Keycloak admin** — accessible at `https://your-domain.com/auth/admin` (login: `admin` / `admin`)

---

## Tűzfalszabályok (Linode Cloud Firewall)

Ha Linode Cloud Firewall-t csatol ehhez a szerverhez, kövesse a következő szabályokat:

### Bejövő

| Címke | Akció | Jegyzőkönyv | Kikötő | Források | Megjegyzések |
|-------|--------|----------|------|----------|-------|
| `accept-inbound-ssh` | Elfogadás | TCP | 22 | Mind IPv4, Mind IPv6 | SSH hozzáférés |
| `bejövő-http` | Elfogadás | TCP | 80 | Mind IPv4, Mind IPv6 | Nginx (HTTP + ACME kihívás) |
| `bejövő-https` | Elfogadás | TCP | 443 | Mind IPv4, Mind IPv6 | Nginx (HTTPS az SSL beállítása után) |
| `elfogad-bejövő-fényes` | Elfogadás | TCP | 3838 | Mind IPv4, Mind IPv6 | Shiny Server (R analytics) |
| `accept-inbound-icmp` | Elfogadás | ICMP | — | Mind IPv4, Mind IPv6 | Ping / diagnosztika |
| Alapértelmezett bejövő szabályzat | **Drop** | | | | Minden más letiltása |

### Kimenő

| Címke | Akció | Megjegyzések |
|-------|---------|-------|
| Alapértelmezett kimenő szabályzat | **Elfogadás** | Minden kimenő engedélyezése (Docker lehívások, certbot, GoDaddy API stb.) |

### Külsőleg NINCS szükség portokra

Ezek a portok csak a "127.0.0.1"-hez vannak kötve, és soha nem érhetők el a szerveren kívülről:

| Kikötő | Szolgáltatás | Ok |
|------|---------|--------|
| 8080 | Alkalmazástároló | Az Nginx belsőleg proxyt használ hozzá |
| 8090 | Kulcsköpeny konténer | Az Nginx belsőleg proxyt használ hozzá |
| 3306 | MySQL | Csak belső Docker-hálózat |

---

## Hibaelhárítás

### Ellenőrizze a beállítási naplót

```bash
tail -200 /var/log/stackscript.log
```

### Ellenőrizze az SSL-naplót

```bash
tail -200 /var/log/rtsurvey-ssl.log
```

### A tároló állapotának megtekintése

```bash
docker compose -f /opt/rtsurvey/docker-compose.production.yml ps
```
