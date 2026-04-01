---
weight: 150
date: "2023-05-03T22:37:22+01:00"
draft: false
author: "RealTimeX"
title: "Adatgyűjtés"
icon: "rocket_launch"
toc: true
description: "Gyorsindítási útmutató felmérés futtatásához rtSurvey-vel"
publishdate: "2023-05-03T22:37:22+01:00"
tags: ["Kezdők"]
---

Miután az űrlapot telepítettük és a kérdezőbiztosokat hozzárendeltük, az adatgyűjtés megkezdődhet. Az **rtSurvey** zökkenőmentes adatgyűjtést tesz lehetővé mind webböngészőkön, mind dedikált mobilalkalmazásokon keresztül, rugalmasságot biztosítva attól függetlenül, hogy a csapat internet-kapcsolattal rendelkezik, vagy távoli, offline környezetben dolgozik.

## A megfelelő gyűjtési módszer kiválasztása

A projekt földrajzi elhelyezkedésétől és a kapcsolat minőségétől függően a kérdezőbiztosok számára optimális módszert választhatja:

- **Webböngésző (online):** A legjobb call centerekhez, irodai adatbevitelhez vagy önkitöltős nyilvános felmérésekhez.
- **rtWork / rtSurvey mobilalkalmazás (online és offline):** A legjobb terepi munkához, instabil internetes területeken, és médiamellékleteket (fotók, GPS-koordináták, offline térképek) igénylő felmérésekhez.

---

## 1. módszer: Adatgyűjtés webböngészőn keresztül

A Webform felület lehetővé teszi a kérdezőbiztosok számára, hogy szoftver telepítése nélkül azonnal megkezdjék az adatgyűjtést.

### 1. Hozzáférés a Webform URL-hez
A Vezérlőpult **Nyomtatványok kezelése** irányítópultján keresse meg a célzott nyomtatványt, majd kattintson a **Webform URL-je** gombra egy biztonságos hivatkozás generálásához.

### 2. Kérdőív kitöltése
- Nyissa meg a megadott URL-t bármely modern webböngészőben.
- Ha a nyomtatvány hitelesítést igényel, a kérdezőbiztosnak be kell jelentkeznie hitelesítő adataival. Ha „Nyilvános láthatóságra" van beállítva, közvetlenül folytathatja.
- Töltse ki a felmérési kérdéseket. A felület automatikusan érvényesíti a logikát, átugrási mintákat és az ellenőrzési szabályokat.
- **Médiarögzítés:** Ha a nyomtatvány tartalmaz kép-, hang- vagy videókérdéseket, a webböngésző kéri, hogy töltsön fel egy fájlt a számítógépéről, vagy ha elérhető, használja az eszköz webkameráját/mikrofonját.

### 3. Beküldés
Az utolsó oldal elérése után kattintson a **Beküldés** gombra. A böngészőnek aktív internet-kapcsolatra van szüksége a beküldés véglegesítéséhez. Sikeres beküldés után az adatok azonnal megjelennek a **Beküldések kezelése** felületen.

---

## 2. módszer: Adatgyűjtés mobilalkalmazáson keresztül (offline)

A robusztus terepi adatgyűjtéshez a mobilalkalmazások teljes offline képességeket biztosítanak.

### 1. Telepítés és hitelesítés
- Töltse le az **rtWork** (vagy **rtSurvey**) alkalmazást a Google Play Áruházból vagy az Apple App Store-ból.
- Nyissa meg az alkalmazást, és jelentkezzen be a hozzárendelt kérdezőbiztosi hitelesítő adatokkal.

### 2. Nyomtatványok letöltése (internet szükséges)
- Lépjen az alkalmazásban a **Nyomtatványok** vagy **Feladatok** részre.
- Koppintson a **Szinkronizálás** vagy **Letöltés** ikonra a legújabb kérdőív-tervek lekéréséhez a szerverről. A letöltés után a nyomtatványok helyben tárolódnak az eszközön.

### 3. Adatgyűjtés (offline)
- Nyissa meg a letöltött nyomtatványt, és kezdje el az interjút.
- Az adatok teljes egészében offline is gyűjthetők.
- **Médiarögzítés:** A mobilalkalmazás natívan integrálódik az eszköz hardverével. Közvetlenül az alkalmazásban rögzíthet fotókat, hangot, videót, és rögzíthet pontos GPS-koordinátákat, akár internet-kapcsolat nélkül is.
- Egy interjú befejezésekor véglegesítse a rekordot. A véglegesített rekordok biztonságosan az alkalmazás kimeneti mappájában kerülnek sorba.

### 4. Beküldések szinkronizálása (internet szükséges)
- Miután a kérdezőbiztos visszatér internet-eléréssel rendelkező területre (Wi-Fi vagy mobil adat), lépjen a **Kimeneti mappa** vagy **Szinkronizálás** felületre.
- Utasítsa az alkalmazást a véglegesített nyomtatványok elküldésére. Az alkalmazás biztonságosan továbbítja a sorban várakozó rekordokat és az összes csatolt médiafájlt a szerverre, amelyek ezt követően megjelennek az adatrácsban ellenőrzés céljából.
