---
weight: 2
title: "Linode (Akamai Cloud)"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-17T01:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "dns"
toc: true
description: "Diekite rtCloud Linode naudodami StackScripts su formos pagrindu sukurta konfigūracijos sąsaja."
---

Linode naudoja **StackScripts** – scenarijus su formos pagrindu sukurta sąsaja, kurioje jūs užpildote konfigūracijos laukus tiesiogiai Linode tvarkytuve, neredaguodami jokio kodo.

> Linode StackScripts yra paprasčiausias diegimo būdas. Laukai rodomi kaip forma kuriant Linode – scenarijaus redaguoti nereikia.

---

## Integruotas Keycloak (rekomenduojama)

### 1 žingsnis — Raskite StackScript

StackScript viešai prieinamas Linode bendruomenėje – rankinio sąrankos nereikia:

1. Eikite į **Linodes** → **Kurti Linode**
2. Skiltyje **Pasirinkti paskirstymą** pasirinkite **StackScripts** → **Bendruomenės StackScripts**
3. Ieškokite **`RTA rtSurvey - Self-Hosted with Keycloak SSO`**
4. Pasirinkite jį ir užpildykite konfigūracijos formą:

> Arba [atsisiųskite scenarijų](/scripts/linode-stackscript-keycloak-embed.sh) ir sukurkite savo StackScript skiltyje **StackScripts** → **Kurti StackScript**.

| Laukas | Privalomas | Aprašymas |
|-------|----------|-------------|
| Projekto ID | Ne | Unikalus identifikatorius (numatytasis: `rtsurvey`). Naudojamas kaip duomenų bazės pavadinimas ir Keycloak kliento ID. |
| Keycloak administratoriaus slaptažodis | Ne | Slaptažodis Keycloak administratoriaus konsolei ir programos admin prisijungimui. Numatytasis – `admin` – **pakeiskite po pirmojo prisijungimo**. |
| Domenas | Taip | Jūsų domeno vardas. DNS A įrašas turi nukreipti į šio Linode IP. Reikalingas HTTPS ir Keycloak. |
| „Let's Encrypt" el. paštas | Taip | El. paštas „Let's Encrypt" sertifikato pranešimams. |
| Docker vaizdo žyma | Ne | Diegiamas vaizdas (numatytasis: `rtawebteam/rta-smartsurvey:survey-dockerize`). |

> **Saugumas:** visi slaptažodžiai pagal numatytuosius nustatymus yra `admin`. Pakeiskite juos iš karto po pirmojo prisijungimo.

5. Pasirinkite **Ubuntu 22.04 LTS** kaip vaizdą
6. Pasirinkite **Shared CPU 4 GB** planą arba didesnį
7. Spustelėkite **Kurti Linode**

### 2 žingsnis — Pridėkite DNS įrašą

Kol Linode paleidžiamas, pridėkite **A įrašą** savo DNS teikėjuje:

```
Tipas  : A
Vardas : myapp          (arba @ šakniniam domenui)
Reikšmė: <linode-ip>
TTL    : 300
```

### 3 žingsnis — Stebėkite eigą

```bash
ssh root@<linode-ip>
tail -f /var/log/stackscript.log
```

Scenarijus išveda jūsų serverio IP pradžioje – pridėkite DNS įrašą, kai tik jį pamatysite.

### 4 žingsnis — Pasiekite programą

Kai sąranka baigiama, žurnale rodoma santrauka:

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

Prisijunkite naudodami naudotojo vardą `admin` ir slaptažodį `admin`, tada iš karto pakeiskite slaptažodį.

---

## Po diegimo

### Slaptažodžio keitimas

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Visų konteinerių peržiūra

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```

### Žurnalo tikrinimas

```bash
tail -200 /var/log/stackscript.log
```
