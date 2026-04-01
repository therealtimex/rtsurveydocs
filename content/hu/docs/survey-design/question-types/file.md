---
title: "Fájl"
description: "A fájlkérdések lehetővé teszik a válaszadók számára, hogy dokumentumokat és egyéb fájlokat töltsenek fel felmérési válaszuk részeként."
icon: "upload_file"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 230
---

A `file` kérdéstípus lehetővé teszi a válaszadók számára, hogy **bármilyen fájlt töltsenek fel** az eszközükről – dokumentumokat, táblázatokat, PDF-eket vagy más fájltípusokat. Az `image`, `audio` és `video` kérdéstípusokkal ellentétben, amelyek speciális rögzítő eszközöket nyitnak meg, a `file` általános célú fájlböngészőt nyit meg.

## Alapvető XLSForm-specifikáció

| type | name      | label                        |
|------|-----------|------------------------------|
| file | document  | Kérjük, töltse fel dokumentumát |

A standard file kérdéstípus részleteiről lásd az [XLSForm specifikációt](https://xlsform.org/en/#question-types).

## Felhasználási területek

A fájlkérdések általánosan használt területei:

1. Kísérő dokumentumok gyűjtése (nyugták, tanúsítványok, szerződések, jelentések)
2. Beszkennelt papíros nyomtatványok feltöltése
3. Más rendszerekből exportált táblázatok vagy adatok összegyűjtése
4. Bármilyen digitális fájltípus, amelyet az image/audio/video nem fed le

## Adatformátum

A feltöltött fájlok bináris mellékletekként kerülnek tárolásra:

- **Formátum:** Eredeti formátumban megőrizve (PDF, XLSX, DOCX stb.)
- **Elnevezés:** `{instanceID}-{mezőnév}.{kiterjesztés}`
- **Tárolás:** Feltöltve a szerver médiamappájába a beküldés mellé
- **Hozzáférés:** Letölthető a beküldések kezelési felületéről

## rtSurvey-bővítések

### Elfogadott fájltípusok

A `parameters` oszlop segítségével korlátozhatja, hogy milyen fájltípusok választhatók:

| type | name | label | parameters |
|------|------|-------|------------|
| file | report | Töltse fel az ellenőrzési jelentést | `accept=.pdf` |
| file | spreadsheet | Töltse fel az adatfájlt | `accept=.xlsx,.csv` |

Az `accept` paraméter standard fájlkiterjesztés szintaxist használ (vesszővel elválasztva).

### Fájlméret iránymutatás

Az rtSurvey nem kényszerít rá kemény fájlméret-korlátot a kérdés szintjén, de a szerver feltöltési korlátja érvényes. Közölje az elvárásokat a kérdezővel a `hint` segítségével:

| type | name | label | hint |
|------|------|-------|------|
| file | receipt | Töltse fel a fizetési nyugtát | Elfogadott: PDF vagy kép. Maximális fájlméret: 5 MB |

### Integráció az eszköz fájlrendszerével és felhőtárhellyel

Android és iOS rendszeren a `file` kérdés megnyitja az eszköz natív fájlböngészőjét, amely hozzáférést biztosíthat:
- Helyi eszköztárhelyhez
- SD-kártyához (Android)
- iCloud Drive-hoz (iOS)
- Google Drive-hoz, Dropboxhoz (ha telepítve van)

Weben a böngésző standard fájlfeltöltési párbeszédablakát nyitja meg.

## Példa

### Kötelező PDF feltöltés

| type | name | label | hint | required | required_message |
|------|------|-------|------|----------|-----------------|
| file | signed_consent | Töltse fel az aláírt beleegyező nyilatkozatot | Csak PDF, max. 2 MB | yes | Szükséges a beleegyező nyilatkozat |

### Feltételes dokumentumfeltöltés

| type | name | label | relevant |
|------|------|-------|----------|
| select_one yesno | has_land_title | Van a háztartásnak földtulajdoni lapja? | |
| file | land_title_doc | Töltse fel a földtulajdoni lap fotóját vagy szkennelését | `${has_land_title} = 'yes'` |

## Bevált módszerek

1. Használja az `accept` értéket a fájltípusok korlátozásához – ez megakadályozza, hogy a kérdezők véletlenül rossz fájlokat töltsenek fel.
2. Mindig adjon méret- és formátum-útmutatást a `hint` oszlopban.
3. Fotókhoz és képekhez használja az `image` típust – jobb tömörítést és egységes formátumkezelést kínál.
4. Fájlmellékleteket tartalmazó nagy felmérések esetén tervezze meg az adattárolást és a letöltési sávszélességet ennek megfelelően.
5. Tesztelje a fájlböngészőt a céleszköz típusán (Android vs. iOS vs. web) a telepítés előtt – a felhőtárhelyekhez való hozzáférés eltérő.

## Adatkezelési szempontok

- A fájlok eredeti formátumban kerülnek tárolásra; az rtSurvey nem konvertálja vagy tömöríti azokat.
- Elemezze a fájlokat letöltés után – az rtSurvey nem nyeri ki vagy indexeli a fájlok tartalmát.
- A nagy fájlmellékleteket tartalmazó felmérések esetén a teljes adathalmazon letöltéséhez szükséges idő jelentősen növekedhet.

## Korlátozások

- A fájlkérdések nem ellenőrzik a fájl tartalmát – csak a kiterjesztés-ellenőrzés érvényesül a felhasználói felületen az `accept` segítségével.
- A nagyon nagy fájlok (100 MB+) alacsony kapcsolati sebességű környezetben feltöltéskor időtúllépést okozhatnak.
- Az offline kérdezők csatolhatnak fájlokat, de azok nem töltődnek fel, amíg a kapcsolat helyre nem áll.
- Egyes eszközkonfigurációk korlátozzák bizonyos tárolási helyek elérését (pl. vállalati MDM-szabályzatok).
