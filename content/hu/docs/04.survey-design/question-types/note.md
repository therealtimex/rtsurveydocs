---
title: "Note"
description: "A note kérdések csak olvasható szöveget vagy médiát jelenítenek meg, hogy információt vagy utasításokat adjanak a felmérésben."
icon: "info"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 255
---

Az XLSForm és az rtSurvey note kérdéstípusa csak olvasható szöveg vagy média megjelenítésére szolgál a felmérés válaszadója számára. Nem adatbevitelt igénylő kérdés, hanem inkább információ, utasítás vagy kontextus nyújtásának eszköze a felmérésben.

## Alapvető XLSForm-specifikáció

| type | name | label |
|------|------|-------|
| note | info_text | Ez a felmérés az olvasási szokásaival foglalkozik. |

A note kérdéstípus alapvető részleteiről lásd az [XLSForm specifikációt](https://xlsform.org/en/#question-types).

## Felhasználási területek

A note kérdések általánosan használt területei:

1. Utasítások vagy kontextus megadása a következő kérdések előtt
2. Számított eredmények vagy összefoglalók megjelenítése
3. Képek vagy egyéb média megjelenítése
4. Felmérési szakaszok elválasztása
5. Visszajelzés adása az előző válaszok alapján

## Bevált módszerek

1. Tartsa tömörre és egyértelműre a note szövegét a válaszadók figyelmének megőrzéséhez.
2. Használjon formázást (félkövér, dőlt) a fontos információk kiemelésére.
3. Szükség esetén médiával (képek, hang) fokozza a megértést.
4. Mértékletesen használjon note elemeket a felmérés zsúfoltságának elkerüléséhez.

## Példa

Íme egy példa arra, hogyan lehet note kérdéseket felhasználni egy felmérésben:

| type | name | label |
|------|------|-------|
| note | intro | Üdvözöljük olvasási szokásaink felmérésén. Kérdezni fogunk az olvasási preferenciákról és gyakoriságról. |
| ... | ... | ... |
| calculate | books_per_month | ${fiction_books} + ${non_fiction_books} |
| note | reading_summary | Havonta körülbelül ${books_per_month} könyvet olvas. |

Ebben a példában note elemeket használunk a felmérés bevezetéséhez és a számított eredmények összefoglalásához.

## rtSurvey-bővítések

Bár az alapvető XLSForm-specifikáció egyszerű a note kérdéseknél, az rtSurvey további funkciókat kínálhat:

1. Rich text formázás
2. Beágyazott média (képek, hang, videó) támogatása
3. Dinamikus tartalom az előző válaszok alapján
4. Egyéni stílusbeállítások

## Speciális felhasználás

### Feltételes megjelenítés

A relevance kifejezések segítségével feltételesen jelenítheti meg a note elemeket:

| type | name | label | relevant |
|------|------|-------|----------|
| note | high_reader_note | Ön szenvedélyes olvasó! | ${books_per_month} > 5 |

### Számítások beillesztése

A note elemek számításokat is tartalmazhatnak dinamikus visszajelzés nyújtásához:

| type | name | label |
|------|------|-------|
| note | reading_time | Válaszai alapján havonta körülbelül ${books_per_month * 5} órát tölt olvasással. |

## Korlátozások

- A note elemek nem gyűjtenek adatokat, ezért nem használhatók, ha információt kell gyűjteni a válaszadóktól.
- A note elemek túlzott használata zsúfolttá vagy hosszúvá teheti a felmérést.
- Egyes speciális formázási vagy média-lehetőségek nem feltétlenül támogatottak minden eszközön vagy platformon.
