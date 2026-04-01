---
title: "Kulcsfogalmak"
description: "Űrlaptervezés áttekintése"
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 210
---

## Mi az az XLSForm?
Az rtSurvey az [XLSForm](https://xlsform.org/) szabvány kiterjesztett verzióját használja az űrlaptervezéshez, hatékony funkciókat kínálva kifinomult felmérések létrehozásához. Ez az útmutató bemutatja az rtSurvey-beli űrlaptervezés kulcsfogalmait az alapvető XLSForm-struktúrától az rtSurvey-specifikus haladó funkciókig.

Az XLSForm-ok segítségével emberek által olvasható formátumban, a jól ismert Excel eszközzel készíthetők űrlapok, így szinte mindenki számára elérhetők.
Ez a szabvány megkönnyíti az űrlapkészítés megosztását és közös munkáját.

Bár az XLSForm-ok kezdők számára is barátak, tapasztalt felhasználók összetett űrlapokat is készíthetnek velük.

Az rtSurvey egységes módot biztosít haladó funkciók – például az ugrási logika – beépítésére a különböző web- és mobilos adatgyűjtési platformokon.

## XLSForm struktúra
Egy XLSForm általában két fő munkalapból áll:

1. **survey**: Meghatározza az űrlap struktúráját és tartalmát.
2. **choices**: Megadja a feleletválasztós kérdések válaszlehetőségeit.

Az opcionális **settings** munkalap további űrlapszintű specifikációkat tartalmazhat.

Fontos megjegyezni, hogy a survey és choices munkalapok kötelező oszlopainak jelen kell lenniük az űrlap helyes működéséhez. Az opcionális oszlopok tovább szabályozzák az egyes bejegyzések viselkedését, de nem nélkülözhetetlenek.

Az Excel-munkafüzet oszlopai bármilyen sorrendben megjelenhetnek, az opcionális oszlopok üresen hagyhatók. Azonban elengedhetetlen a pontos szintaxis és az XLSForm dokumentációban meghatározott elnevezési konvenciók betartása.

### A survey munkalap
A **survey munkalap** az a hely, ahol meghatározza az űrlap szerkezetét és tartalmát. Minden sor egy kérdést vagy elemet jelöl az űrlapban. Az alábbi oszlopok kötelezőek:

- `type`: Megadja a kérdésre várt beviteli típust.
- `name`: Megadja az egyedi változónevet. A névnek betűvel vagy aláhúzással kell kezdődnie, és csak betűket, számjegyeket, kötőjeleket, aláhúzásokat és pontokat tartalmazhat. A nevek megkülönböztetik a kis- és nagybetűket.
- `label`: Az űrlapon a kérdésnél megjelenő tényleges szöveg.

| type                | name     | label                |
| ------------------- | -------- | -------------------- |
| today               | today    |                      |
| select_one gender   | gender   | Válaszadó neme?      |
| integer             | age      | Válaszadó kora?      |

### A choices munkalap
A **`choices`** munkalap a feleletválasztós kérdések válaszlehetőségeit tartalmazza.
Minden sor egy válaszlehetőséget jelöl. Az alábbi oszlopok kötelezőek:

- **`list_name`**: Összetartozó válaszlehetőségek csoportosítása.
- **`name`**: Az adott válaszlehetőség egyedi változóneve.
- **`label`**: A válaszlehetőség szövege, ahogy az űrlapon megjelenik.

| list_name           | name        | label                |
| ------------------- | ----------- | -------------------- |
| gender              | transgender | Transznemű           |
| gender              | female      | Nő                   |
| gender              | male        | Férfi                |
| gender              | other       | Egyéb                |

A kötelező vagy opcionális oszlopok bármilyen sorrendben szerepelhetnek. Az olvashatóság érdekében üresen hagyhatók sorok és oszlopok, de 20 egymást követő üres sor vagy oszlop utáni adatokat a rendszer nem dolgoz fel. Az .xlsx fájlformázás figyelmen kívül marad, így elválasztó vonalak, árnyékolás és egyéb betűformázás használható az olvashatóság javítására.

Fontos, hogy az Excel-ben való űrlapkészítés során a szintaxisnak pontosnak kell lennie. Például ha **Choices** vagy **choice** helyett **choices**-t ír, az űrlap nem fog működni.

### A settings munkalap

A settings munkalap nem kötelező, de lehetővé teszi űrlapszintű metaadatok és viselkedés megadását. A settings munkalap általános oszlopai:

| Oszlop | Leírás |
|--------|--------|
| form_title | Az űrlap felhasználók számára megjelenő neve |
| form_id | Az űrlap egyedi azonosítója, adatkezelésben és API-hívásokban használatos |
| default_language | A többnyelvű űrlap alapértelmezett nyelvi kódja (pl. 'en' az angolhoz) |
| version | Az űrlap verziószáma, változások nyomon követésére hasznos |
| instance_name | Kifejezés minden beküldés egyedi nevének generálásához |
| generation | Egész szám, amely jelzi az űrlap generációját. Strukturális változásoknál növelendő |
| family | Azonosító a strukturális változásokon átívelő kapcsolódó űrlapok csoportosítására |

Az rtSurvey settings munkalapja rtSurvey-specifikus konfigurációkat is tartalmazhat. A támogatott beállítások teljes listájáért tekintse meg az rtSurvey dokumentációját.

## A Survey munkalap főbb összetevői

A survey munkalap az űrlaptervezés alapja. Főbb összetevőinek áttekintése:

| Összetevő | Leírás |
|-----------|--------|
| [type](#kérdéstípusok) | A kérdés típusát adja meg (pl. text, integer, select_one) |
| [name](#elnevezési-konvenciók) | A kérdés egyedi azonosítója |
| [label](#feliratok-és-fordítások) | A válaszadónak megjelenő szöveg |
| [hint](#súgó-és-tippek) | További útmutatás a válaszadónak |
| [appearance](#megjelenési-lehetőségek) | A kérdés megjelenítését módosítja |
| [relevant](#relevancia-és-ugrási-logika) | Meghatározza, mikor jelenjen meg a kérdés (ugrási logika) |
| [constraint](#korlátozások-és-ellenőrzés) | Ellenőrzi a választ |
| [calculation](#számítások) | Más válaszok alapján számított értékeket ad meg |
| [required](#kötelező-mezők) | Meghatározza, hogy kötelező-e megválaszolni |

### Kérdéstípusok
Az XLSForm számos kérdéstípust támogat. Néhány lehetőség a **`survey`** munkalap **`type`** oszlopában:

| Kérdéstípus               | Beviteli módszer                                                                              |
| ------------------------- | --------------------------------------------------------------------------------------------- |
| integer                   | Egész szám bevitele.                                                                          |
| decimal                   | Tizedes szám bevitele.                                                                        |
| range                     | Tartomány bevitele (értékelést is beleértve)                                                  |
| text                      | Szabad szöveges válasz.                                                                       |
| select_one [options]      | Feleletválasztós kérdés; csak egy válasz választható.                                         |
| select_multiple [options] | Feleletválasztós kérdés; több válasz is választható.                                          |
| select_one_from_file [file]| Fájlból töltött feleletválasztó; csak egy válasz választható.                                |
| select_multiple_from_file [file]| Fájlból töltött feleletválasztó; több válasz is választható.                           |
| rank [options]            | Rangsorolás; rendezzen egy listát sorrendbe.                                                  |
| note                      | Megjelenít egy megjegyzést, nem fogad bevitelt. Rövidítés: type=text és readonly=true.        |
| geopoint                  | Egyetlen GPS-koordináta rögzítése.                                                            |
| geotrace                  | Két vagy több GPS-koordinátából álló vonal rögzítése.                                         |
| geoshape                  | Több GPS-koordinátából álló sokszög rögzítése; az utolsó pont megegyezik az elsővel.          |
| date                      | Dátum bevitele.                                                                               |
| time                      | Időpont bevitele.                                                                             |
| dateTime                  | Dátum és időpont együttes bevitele.                                                           |
| image                     | Fénykép készítése vagy képfájl feltöltése.                                                    |
| audio                     | Hangfelvétel készítése vagy hangfájl feltöltése.                                             |
| background-audio          | Hang felvétele a háttérben az űrlap kitöltése közben.                                         |
| video                     | Videófelvétel készítése vagy videófájl feltöltése.                                           |
| file                      | Általános fájlbevitel (txt, pdf, xls, xlsx, doc, docx, rtf, zip)                             |
| barcode                   | Vonalkód beolvasása, vonalkód-olvasó alkalmazás szükséges.                                    |
| calculate                 | Számítás elvégzése; lásd a Számítás szakaszt.                                                 |
| acknowledge               | Visszaigazolási felszólítás, amely "OK" értéket állít be, ha kijelölik.                       |
| hidden                    | Nem jelenik meg a felületen; állandó értékek tárolására használható.                          |
| xml-external              | Hivatkozást ad hozzá egy külső XML adatfájlhoz.                                               |

### Feliratok

A feliratok a válaszadóknak minden kérdésnél megjelenő szövegek. Alapvető szerepük van a felmérések egyértelmű kommunikációjában.

- **Alap használat**: A `label` oszlopban adja meg a kérdés szövegét.
- **Több nyelv**: Használjon további oszlopokat, például `label::Magyar` és `label::Angol` a többnyelvű felmérésekhez.
- **Formázás**: Az rtSurvey alapvető HTML-formázást támogat a feliratokban.

Példa:
```
| type | name | label | label::French |
|------|------|-------|---------------|
| text | name | Mi a neve? | Quel est votre nom? |
```

### Súgók

A súgók további útmutatást adnak a válaszadóknak a fő kérdés szövegének zsúfolása nélkül.

- **Használat**: Adjon meg súgókat a `hint` oszlopban.
- **Láthatóság**: A súgók általában a fő kérdés szövege alatt jelennek meg.
- **Többnyelvű**: A feliratokhoz hasonlóan súgók is megadhatók több nyelvhez a `hint::Nyelv` oszlopokkal.

Példa:
```
| type | name | label | hint |
|------|------|-------|------|
| integer | age | Hány éves? | Adja meg korát években |
```

### Megjelenés

Az rtSurvey `appearance` oszlopa lehetővé teszi a kérdések megjelenítésének testreszabását.

- **Szabványos lehetőségek**: Pl. 'multiline' a szövegmezőkhöz, 'horizontal' a kiválasztós kérdésekhez.
- **rtSurvey-bővítések**: 
  - Időbevitel: Különféle óramegjelenítési lehetőségek (pl. `inline`, `inline-1line`)
  - Színek testreszabása: A `colors()` függvénnyel módosíthatók az ikon színei.

Példa:
```
| type | name | label | appearance |
|------|------|-------|------------|
| text | time | Adja meg az időpontot | inline-[%H:%M] |
```

### Relevancia

A `relevant` oszlop valósítja meg az ugrási logikát, meghatározva, mikor jelenjen meg egy kérdés.

- **Szintaxis**: XPath-kifejezéseket használ a feltételek megadásához.
- **Változók**: Más kérdések neveire `${kérdés_neve}` formában hivatkozhat.

Példa:
```
| type | name | label | relevant |
|------|------|-------|----------|
| text | allergies | Sorolja fel az allergiáit | ${has_allergies} = 'yes' |
```

### Kötelező

A `required` oszlop meghatározza, hogy egy kérdést kötelező-e megválaszolni.

- **Alap használat**: A kötelezőséghez 'yes' vagy 'true' értéket használjon.
- **Haladó**: Feltételes kötelezőség kifejezésekkel is megadható.

Példa:
```
| type | name | label | required |
|------|------|-------|----------|
| text | email | E-mail cím | yes |
```

### Ismétlések

Az ismétlések lehetővé teszik, hogy egy kérdéscsoport többször is megválaszolható legyen.

- **Használat**: A `begin repeat` és `end repeat` sorokkal definiálhat ismétlődő csoportot.
- **Elnevezés**: Adjon egyedi nevet minden ismétlőcsoportnak.

Példa:
```
| type | name | label |
|------|------|-------|
| begin repeat | household_member | Háztartás tagja |
| text | member_name | Név |
| integer | member_age | Kor |
| end repeat | | |
```

### Média

Az rtSurvey különféle médiatípusokat támogat a felmérésekben: képeket, hangot és videót.

- **Kérdéstípusok**: Az type oszlopban használja az 'image', 'audio' vagy 'video' típusokat.
- **Média a feliratokban**: HTML-tagekkel hivatkozhat médiafájlokra.

Példa:
```
| type | name | label |
|------|------|-------|
| image | house_photo | Készítsen fényképet a házról |
| note | | <img src="logo.jpg" /> Üdvözli a felmérés |
```

### Csak olvasható

A csak olvasható kérdések felhasználói bevitel engedélyezése nélkül jelenítenek meg információkat.

- **Használat**: Adja hozzá a 'readonly' értéket az `appearance` oszlophoz.
- **Számítások**: Gyakran a calculate típussal együtt használják számított értékek megjelenítésére.

Példa:
```
| type | name | label | appearance | calculation |
|------|------|-------|------------|-------------|
| calculate | bmi | BMI | readonly | ${weight} / (${height} * ${height}) |
```

## rtSurvey-bővítések

Az rtSurvey az XLSForm szabványt további lehetőségekkel egészíti ki, például `rácsszerű elrendezéssel`, `HTML-formázással` és számos új `widgettel`.

### Rácsszerű elrendezés
Az rtSurvey lehetővé teszi, hogy az űrlap hasonlítson a hagyományos papíros felmérésekhez azáltal, hogy több kérdést egy sorba tömörít.

### Űrlap beállítások

### Adatbeállítások

### Typeform stílus

### A pulldata() kiterjesztése

### Megjelenés alapú bővítések

### Webbox-bővítések
