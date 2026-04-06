---
title: "Hang"
description: "A hangkérdések lehetővé teszik a válaszadók számára, hogy hangfájlokat rögzítsenek és küldjenek be a felmérés részeként."
icon: "mic"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 228
---

Az `audio` kérdéstípus lehetővé teszi a válaszadók számára, hogy **hangot rögzítsenek** vagy meglévő hangfájlt töltsenek fel felmérési válaszuk részeként. Hasznos szóbeli beszámolók, környezeti hangok, tanúvallomások és bármilyen hang formájában jobban közvetíthető információ rögzítéséhez.

## Alapvető XLSForm-specifikáció

| type  | name        | label                        |
|-------|-------------|------------------------------|
| audio | voice_note  | Kérjük, rögzítse megjegyzéseit |

A standard audio kérdéstípussal kapcsolatos további részletekért lásd az [XLSForm specifikációt](https://xlsform.org/en/#question-types).

## Felhasználási területek

A hangkérdések általánosan használt területei:

1. Nyílt végű szóbeli válaszok rögzítése a kérdező gépelési terhének csökkentésére
2. Tanúvallomások, személyes történetek vagy szóbeli hagyományok rögzítése
3. Környezeti hangok dokumentálása (pl. zajszintek infrastruktúra közelében)
4. Hangminták gyűjtése nyelvi vagy egészségügyi kutatásokhoz
5. Lehetőség a válaszadóknak, hogy szóbeli pontosításokat fűzzenek numerikus vagy kiválasztós válaszokhoz

## Adatformátum

A hangfájlok bináris mellékletekként kerülnek tárolásra a form beküldés mellett, általában:

- **Formátum:** MP3 vagy AAC (mobilos rögzítés); WAV (magas minőségű rögzítés)
- **Elnevezés:** `{instanceID}-{mezőnév}.mp3` (vagy egyenértékű)
- **Tárolás:** Feltöltve a szerver médiamappájába, és a beküldési rekordhoz csatolva
- **Hozzáférés:** Lejátszható és letölthető a beküldések kezelési felületéről

## rtSurvey-bővítések

### Maximális időtartam

A `parameters` oszlop segítségével korlátozhatja a felvétel hosszát:

| type | name | label | parameters |
|------|------|-------|------------|
| audio | interview | Az interjú rögzítése | `max-duration=120` |

A `max-duration` másodpercben értendő. A felvevő automatikusan megáll a korlát elérésekor.

### Minőségi beállítások

A felvétel minősége a `parameters` segítségével állítható be:

| type | name | label | parameters |
|------|------|-------|------------|
| audio | feedback | Visszajelzés rögzítése | `quality=normal` |

Támogatott értékek: `low`, `normal` (alapértelmezett), `voice-only`. A `voice-only` beállítás zajcsökkentéssel optimalizál a beszédhanghoz.

### Lejátszás beküldés előtt

Mobilon a kérdező a továbblépés előtt visszahallgathatja a felvételt. Ez alapértelmezés szerint engedélyezett – nincs szükség konfigurációra.

### Natív felvevő integráció

Android és iOS rendszeren az `audio` elindítja az eszköz natív felvevő alkalmazását. Weben a böngésző beépített MediaRecorder API-ját használja.

## Példa

### Maximális időtartammal és súgóval

| type | name | label | hint | parameters |
|------|------|-------|------|------------|
| audio | story | Mesélje el az eseményt a saját szavaival | Érthetően beszéljen. A felvétel 3 perc után leáll. | `max-duration=180` |

### Feltételes hang – csak probléma esetén

| type | name | label | relevant | required |
|------|------|-------|----------|----------|
| select_one yesno | issue_found | Találtak-e problémát? | | |
| audio | issue_audio | Rögzítsen leírást a problémáról | `${issue_found} = 'yes'` | `${issue_found} = 'yes'` |

## Bevált módszerek

1. Egyértelműen jelezze a feliratban vagy a súgóban, hogy a kérdezőnek mit és meddig kell mondania.
2. Használja a `max-duration` értéket, hogy megakadályozza a túlzottan nagy fájlokat lassú feltöltési sebességű területeken.
3. Értesítse a válaszadókat a felvétel megkezdése előtt – a váratlan felvétel adatvédelmi aggályokat vethet fel.
4. Tesztelje a felvételt a céleszközön és a hálózati feltételek mellett az üzembe helyezés előtt.
5. Interjú jellegű felvételekhez állítsa be a `quality=voice-only` értéket a fájlméret csökkentéséhez az érthetőség elvesztése nélkül.

## Korlátozások

- A hangfájlok nagyok lehetnek (egy 2 perces normál minőségű felvétel kb. 2–4 MB) – vegye figyelembe ezt az adatforgalmi tervnél és a feltöltési időszámításnál.
- Nem minden böngésző támogatja a MediaRecorder API-t – a Chrome és a Firefox megbízhatóan működik; a régebbi iOS verziókban a Safari esetleg problémás.
- A hangválaszok átírásához további utófeldolgozás szükséges (manuális vagy automatizált szöveg-hang átalakítás).
- Az adatvédelmi szabályozások korlátozhatják a hangfelvételt – ellenőrizze a helyi adatvédelmi követelményeket.
