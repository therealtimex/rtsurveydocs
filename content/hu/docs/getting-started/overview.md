---
weight: 1
date: "2026-04-01T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
title: "Áttekintés"
icon: "rocket_launch"
toc: false
description: "Mi az rtSurvey, hogyan működik és mire van szükség az indulás előtt."
---

Az rtSurvey egy saját szervereken futtatható platform, amellyel űrlapokat tervezhet, terepi adatokat gyűjthet és valós időben elemezheti az eredményeket. Saját szerverén futtatja — az adatai soha nem hagyják el az infrastruktúráját.

---

## Hogyan működik

| Lépés | Mit tesz |
|-------|---------|
| **1. Telepítés** | Indítson el egy szervert, és futtassa az rtSurvey-vermet egyetlen automatizált szkripttel |
| **2. Tervezés** | Hozzon létre űrlapokat XLSForm vagy a vizuális Form Builder segítségével |
| **3. Gyűjtés** | A terepi csapatok mobilalkalmazáson vagy böngészőn keresztül küldik be az adatokat — online vagy offline |
| **4. Elemzés** | Tekintse át a beküldéseket az irányítópulton, exportálja CSV/Stata formátumba, vagy csatlakozzon a Power BI / R-hez |

---

## Mielőtt elkezdi

Szüksége lesz:

- Egy **Linux szerverre** (vagy felhőfiókra Linode, DigitalOcean, AWS vagy GCP szolgáltatóknál)
- Egy **domainnevere**, amely a szerverére mutat
- Körülbelül **10 percre**

Nem szükséges Docker-ismeret — a telepítési szkript mindent elvégez.

---

## Készen áll?

**[Telepítse a szerverét →](self-hosting/quick-start)**
