---
weight: 15
date: "2026-03-04T00:00:00+00:00"
draft: false
title: "Rendszerfelhasználó"
icon: "people"
toc: true
description: "Szerepkörök, jogosultságok és bevezetési folyamatok kezelése az összes platformrésztvevő számára."
tags: ["Felhasználók", "Hozzáférés-szabályozás", "Bevezetés", "Szerepkörök"]
---

# Rendszerfelhasználó-kezelés

A **Rendszerfelhasználó** modul (`/cpms/cpmsSystemUser/admin`) egy átfogó kezelési felület annak szabályozásához, hogy ki férhet hozzá a valós idejű felmérési platformhoz (RT-CPMS) és milyen műveleteket hajthat végre.

![Rendszerfelhasználói felület](/images/system_user.png)

## Egységesített kezelési megközelítés

Az RT-CPMS-ben a **kérdezőbiztos** egyszerűen egy rendszerfelhasználóhoz rendelt szerepkör. Nincs külön „kérdezőbiztos" adatbázis. Akár magas szintű rendszergazdáról van szó, aki a webes portált felügyeli, akár terepi kérdezőbiztosról, aki mobilalkalmazáson keresztül gyűjt adatokat, mindannyiukat ugyanebben az egységes rendszerben kezelik.

## Főbb funkciók

### 1. Felhasználói könyvtár és rácsnézet
A fő felület lapozható listát jelenít meg a munkaterülethez kapcsolódó összes felhasználóról. A főbb jellemzők:
* **Szervezeti azonosító és név**: A felhasználók logikai csoportosítása meghatározott szervezeti egységek szerint (pl. `rta`, `partner_org`).
* **Szerepkör**: A felhasználó jogosultsági szintjét határozza meg (pl. `Rendszergazda`, `Vezető csapat`, `Kérdezőbiztos`).
* **Csoport**: Térbeli vagy logikai csoportosítási hozzárendelések (pl. meghatározott körzetek vagy operatív csapatok).
* **Szinkronizált**: Jelzi, hogy a fiók sikeresen integrálódott-e a központi egyszeri bejelentkezési (SSO) rendszerrel.
* **Állapot**: Vizuális jelzők, amelyek megerősítik, hogy egy fiók `Aktív`, `Inaktív`, `Törölt` vagy `Blokkolt`.

**Globális műveletek:**
* **Rendszerfelhasználó hozzáadása**: Egyéni profil kézi létrehozása.
* **Rendszerfelhasználó importálása**: Tömeges fióklétrehozás Excel-sablon segítségével. Az ütközések kezelése `Kihagyás` vagy `Csere` módban, és közvetlen szinkronizálás az SSO-val.
* **Tömeges törlés**: Többszörös kijelölés támogatása tömeges fióktörléshez.

### 2. Hozzáférés-szabályozás és biztonság
Felhasználói profil létrehozásakor vagy szerkesztésekor számos kritikus biztonsági és munkafolyamat-mező áll rendelkezésre:
* **Felhasználói kód**: Egyedi azonosító, amely összeköti a helyi CPMS-fiókot a központi SSO-tárolóval.
* **Eszközcsere-kód**: Robusztus biztonsági token, amelyre akkor van szükség, ha egy kérdezőbiztosnak a mobileszközét kell cserélnie.
* **Jogosultsági szint**: Részletes prioritás/hozzáférési skála 0-tól (legalacsonyabb) 20-ig (legmagasabb) terjedően.
* **Felügyelői váltó**: Egy jelölőnégyzet, amely azonnal magasabb szintű menedzsmentállapotba emeli a normál felhasználót.
* **Munkafolyamat-automatizálás**: A „Szerkesztési kérések automatikus jóváhagyása" lehetőség, amely egyszerűsíti a megbízható felhasználók adattisztítási és -ellenőrzési folyamatát.

### 3. Kódkezelés (Automatizált bevezetés)
A „Kód" alfülön található, ez a funkció hash-alapú regisztrációs és meghívóhivatkozásokat kezel, egyszerűsítve a nagy csapatok bevezetési folyamatát.

* **Regisztráció vs. meghívás**: Válassza ki, hogy a felhasználók saját magukat regisztrálhatnak-e egy elosztott hivatkozás segítségével, vagy közvetlen rendszergazdai meghívásra van szükségük.
* **Lejárati dátumok**: A bevezetés meghatározott időablakokra korlátozása.
* **Használati korlátok**: Az egyetlen generált kóddal csatlakozni képes felhasználók számának korlátozása.
* **Előre kiosztott szerepkörök**: Az ezeken a kódokon keresztül csatlakozó felhasználók automatikusan öröklik az előre meghatározott szerepkört és jogosultsági szintet, így azonnal munkára készen állnak, manuális rendszergazdai beavatkozás nélkül.
