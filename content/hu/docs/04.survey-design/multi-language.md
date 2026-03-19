---
title: "Többnyelvű támogatás"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 285
---

Az rtSurvey erőteljes többnyelvű támogatást biztosít, lehetővé téve felmérések létrehozását több nyelven. Ez a funkció elengedhetetlen soknyelvű populációkon végzett kutatásokhoz vagy többnyelvű környezetekben végzett felmérésekhez.

## Többnyelvű felmérések beállítása

Többnyelvű felmérés létrehozásához az rtSurvey-ben nyelvspecifikus oszlopokat kell hozzáadni az XLSForm-hoz. A lépések:

1. **Felirat-fordítások**: Adjon hozzá oszlopokat minden nyelvhez a `label::Nyelv (kód)` formátumban.
2. **Súgófordítások**: Használja a `hint::Nyelv (kód)` formátumot a súgók fordításához.
3. **Médiafájl-fordítások**: Nyelvspecifikus médiához használja a `media::Nyelv (kód)` formátumot.

Példa:

```
| type    | name | label::English (en) | label::Magyar (hu) | hint::English (en) | hint::Magyar (hu) |
|---------|------|---------------------|---------------------|---------------------|---------------------|
| integer | age  | How old are you?    | Hány éves?          | Enter your age      | Adja meg korát      |
```

## Nyelvkódok

Ajánlott a hivatalos 2 karakteres nyelvkódokat (altagokat) használni a nyelv neve után. Ez megkönnyíti az űrlap nyelvének és a felhasználói felület nyelvének egyeztetését. A hivatalos kódokat [itt](https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry) találja.

## Alapértelmezett nyelv beállítása

Az adatgyűjtés alapértelmezett nyelvének beállításához használja az XLSForm `settings` munkalapját:

```
| form_id   | version | default_language |
|-----------|---------|-------------------|
| test_form | 101     | Magyar (hu)       |
```

## rtSurvey-specifikus funkciók

### Dinamikus nyelvváltás

Az rtSurvey lehetővé teszi a felhasználók számára, hogy az adatgyűjtés során dinamikusan válthassanak nyelvet:

- A webes felületen használja a felső navigációs sáv nyelvi legördülő menüjét.
- A mobilalkalmazásban a beállítások menüből érhetők el a nyelvi lehetőségek.

### Nyelvspecifikus ellenőrző üzenetek

Az rtSurvey kiterjeszti a többnyelvű támogatást az ellenőrzési üzenetekre is:

```
| type    | name | constraint | constraint_message::English (en) | constraint_message::Magyar (hu) |
|---------|------|------------|----------------------------------|----------------------------------|
| integer | age  | . <= 150   | Age must be 150 or less          | A kornak legfeljebb 150-nek kell lennie |
```

### RTL-nyelvek támogatása

Jobbról balra olvasható (RTL) nyelvek, például arab vagy héber esetén az rtSurvey automatikusan igazítja az elrendezést:

```
| type | name | label::English (en) | label::Arabic (ar) |
|------|------|---------------------|---------------------|
| text | name | Your name           | اسمك                |
```

### Nyelvspecifikus megjelenés

Az rtSurvey lehetővé teszi különböző megjelenések megadását különböző nyelvekhez:

```
| type | name | label::English (en) | label::Chinese (zh) | appearance::English (en) | appearance::Chinese (zh) |
|------|------|---------------------|---------------------|--------------------------|---------------------------|
| text | address | Address          | 地址                 | multiline                | textarea                  |
```

## Bevált módszerek többnyelvű felmérésekhez

1. **Következetes elnevezés**: Használjon következetes nyelvkódokat az egész űrlapon.
2. **Professzionális fordítás**: Alkalmazzon a felmérési kontextusban jártas professzionális fordítókat.
3. **Kontextusjegyzetek**: Adjon kontextusjegyzeteket a fordítóknak a pontos fordítás érdekében.
4. **Tesztelés**: Telepítés előtt tesztelje az űrlapot minden nyelven.
5. **Unicode-támogatás**: Győződjön meg arról, hogy az adatgyűjtő eszközök támogatják a Unicode-ot a latin betűkészleten kívüli írásrendszerekhez.
6. **Nyelvspecifikus média**: Minden nyelvhez kulturálisan megfelelő képeket vagy hangot használjon.
7. **Kerülje a szöveget a képekben**: Ha szöveget tartalmazó képeket használ, hozzon létre külön képeket minden nyelvhez.

## Különleges esetek kezelése

### Vegyes nyelvű válaszok

Az rtSurvey lehetővé teszi, hogy a válaszadók bármilyen írásrendszerben adjanak meg szöveget, függetlenül a kiválasztott űrlapnyelvtől. Ez hasznos nevek vagy cím eredeti írásrendszerben való rögzítésekor.

### Nyelvspecifikus kérdéstípusok

Egyes kérdéstípusok bizonyos nyelvekhez jobban megfelelhetnek. Az rtSurvey lehetővé teszi különböző kérdéstípusok használatát különböző nyelvekhez:

```
| type::English (en) | type::Japanese (ja) | name | label::English (en) | label::Japanese (ja) |
|--------------------|---------------------|------|---------------------|----------------------|
| text               | select_one kanji    | name | Enter your name     | 名前を選んでください    |
```

## Többnyelvű adatok exportálása

Az rtSurvey-ből adatok exportálásakor:

- Dönthet úgy, hogy egy adott nyelven exportál, vagy az összes nyelvi verziót belefoglalja.
- Az exportált adatokban szerepel a nyelvmetaadat, jelezve, hogy melyik nyelvet használták az egyes válaszoknál.

## Mobilalkalmazás szempontjai

- Az rtSurvey mobilalkalmazás támogatja az offline nyelvváltást.
- Offline üzemmódba lépés előtt győződjön meg arról, hogy az összes szükséges nyelvi fájl le van töltve.

## Ismert korlátozások

- Egyes haladó funkciók esetleg nem érhetők el minden nyelven.
- A nagyon hosszú fordítások kisebb képernyőkön befolyásolhatják az elrendezést.

Az rtSurvey többnyelvű lehetőségeinek kihasználásával inkluzív, hozzáférhető felméréseket hozhat létre, amelyek különféle populációkat érnek el, és minőségi, nyelvészetileg pontos adatokat nyújtanak.
