---
weight: 10
date: "2026-03-04T00:00:00+00:00"
draft: false
title: "Irányítópult áttekintése"
icon: "home"
toc: true
description: "Az RT-CPMS rendszer irányítópultjának és projektfelügyeleti eszközeinek megismerése."
tags: ["Irányítópult", "Áttekintés", "Felügyelet"]
---

# A rendszer irányítópultja

Az irányítópult (`/cpms/cpmsDashBoard/indexNew`) a valós idejű felmérési platform (RT-CPMS) adminisztratív vezérlőközpontjaként és elsődleges nyitóoldalként szolgál.

![Rendszer irányítópult előnézete](/images/dashboard_overview.png)

Célja, hogy a felmérésmenedzserek azonnali áttekintést kapjanak az aktív projektekről, gyors hivatkozásokat biztosítson az alapvető eszközökhöz, és centralizált hubot nyújtson az összes fő platformmodul navigálásához.

## Főbb funkciók

### 1. Projekt és űrlap kiválasztása
A bal oldali panel tartalmazza az **Űrlapok és jelentések** navigátort. Ez a terület felsorolja a munkaterületen lévő összes aktív felmérést.
* Egy adott felmérés kiválasztásával (pl. *RTA - FELMÉRÉS 02*) az irányítópult a figyelést és a mutatókat kizárólag arra a projektre összpontosítja.

### 2. Vizualizáció és mutatószűrők
A projektlista felett több kritikus adatperspektíva között válthat a valós idejű terepi munkavégzés nyomon követéséhez:
* **Darabszám kezdési idő / befejezési idő szerint**: Nyomon követheti, mikor kezdik el és fejezik be a kérdezőbiztosok a felmérési munkameneteket.
* **Darabszám beküldési dátum szerint**: Figyeli a szerverre érkező adatok általános napi volumenét.
* **Darabszám felhasználónév szerint**: Értékeli az egyes kérdezőbiztosok termelékenységét és teljesítményét.
* **Interjúk térképe**: Megtekintheti a felmérési válaszok összegyűjtési helyeinek földrajzi (GIS) eloszlását, hogy biztosítsa a térbeli lefedettségi követelmények teljesülését.

### 3. Alkalmazásportálok
Az irányítópult közepén azonnali hozzáférés biztosított az adatgyűjtési felületekhez. A kérdezőbiztosok hardverétől függően elindíthatja vagy a következő felületekre irányíthatja őket:
* **Webalkalmazás**: Böngészőalapú adatgyűjtéshez.
* **Android alkalmazás**: Hivatkozás a Google Play Áruházra vagy az APK-ra.
* **iOS alkalmazás**: Hivatkozás az Apple App Store-ra.

### 4. Közvetlen modulhivatkozások
Három kiemelkedő műveleti gomb teszi lehetővé a gyors átváltást a leggyakrabban használt operatív modulokra:
* **Űrlap és adatbevitel**: Ugrás közvetlenül az összegyűjtött adatok kézi kezeléséhez.
* **Elemzés és jelentések**: Az üzleti intelligencia (BI) csomag megnyitása a felmérési válaszok kereszttáblázásához és diagramjaihoz.
* **Jogosultságkonfiguráció**: Annak beállítása, hogy kinek van hozzáférése az aktív felméréshez és milyen szerepkörrel rendelkezik.

### 5. Globális navigációs oldalsáv
Az összecsukható bal oldali oldalsáv hozzáférést biztosít az RT-CPMS háttérmodulok teljes ökoszisztémájához. Innen mélyebbre áshat a következőkben:
* **Beállítás**: Munkatársak és aktív eszközök kezelése.
* **Terepi munkavégzés kezelése**: Kérdezőbiztosok napi tevékenységének nyomon követése.
* **Minőségbiztosítás**: Minőségbiztosítási szabályok és jelzések megvalósítása és felülvizsgálata.
* **Végleges eredmények**: A megtisztított adatkészletek exportálása CSV-, PDF- vagy Stata-formátumba.
