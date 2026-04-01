---
title: "Select_one"
description: "A select_one kérdések lehetővé teszik a válaszadók számára, hogy pontosan egy lehetőséget válasszanak egy előre meghatározott listából."
icon: "radio_button_checked"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 224
---

A `select_one` kérdéstípus a válaszadót arra kéri, hogy **pontosan egy lehetőséget** válasszon egy előre meghatározott listából. Alapértelmezés szerint a lehetőségek rádiógombokként jelennek meg, de számos megjelenési lehetőség érhető el az elrendezés és viselkedés módosításához.

## Alapvető XLSForm-specifikáció

**survey munkalap:**

| type | name | label |
|------|------|-------|
| select_one yesno | consent | A válaszadó megadta beleegyezését? |

**choices munkalap:**

| list_name | name | label |
|-----------|------|-------|
| yesno | yes | Igen |
| yesno | no | Nem |

A `select_one listanév` kifejezésben szereplő `listanév` megegyezik a choices munkalap `list_name` oszlopának értékével.

További részletekért lásd az [XLSForm specifikációt](https://xlsform.org/en/#question-types).

## Felhasználási területek

A select_one kérdések a következőkre használhatók:

1. Igen/Nem kérdések
2. Egyszeres választásos feleletválasztó kérdések (pl. iskolai végzettség, nem, családi állapot)
3. Kategoriális értékelések (pl. gyenge / közepes / jó / kiváló)
4. Kaszkád (összekapcsolt) kiválasztók, ahol a lehetőségek egy előző válasz alapján szűrnek
5. Ország, régió, körzet vagy más közigazgatási egység kiválasztása

## Megjelenési lehetőségek

Az `appearance` oszlopban adjon meg értéket a lehetőségek megjelenítésének módosításához:

{{< table >}}
| Megjelenés | Leírás |
|------------|--------|
| *(nincs)* | Alapértelmezett rádiógombok, soronként egy |
| `minimal` | Egyetlen legördülő lista / spinner rádiógombok helyett |
| `quick` | A következő kérdésre való automatikus ugrás a kiválasztás után (csak mobilon) |
| `compact` | Kompakt rács – az oszlopok száma a képernyő szélességéhez igazodik |
| `compact-N` | Kompakt rács, N oszlopra kényszerítve (pl. `compact-3`) |
| `quickcompact` | A `quick` és `compact` kombinációja |
| `quickcompact-N` | A `quick` és `compact` kombinációja N kényszerített oszloppal |
| `horizontal` | Vízszintesen elrendezett lehetőségek (web) |
| `horizontal-compact` | Vízszintes, kompakt elrendezés (web) |
| `likert` | Likert-skála sor – feliratok felül, rádiógombok alul |
| `label` | Csak lehetőség-feliratokat jelenít meg, beviteli elem nélkül (használja a `list-nolabel` mellé) |
| `list-nolabel` | Csak beviteli elemeket jelenít meg, feliratok nélkül (használja a `label` mellé) |
| `columns(N)` | Megjelenítés N oszlopban (rtSurvey-bővítés, pl. `columns(3)`) |
| `distress` | Kessler Pszichológiai Distressz (K10) érzelmi ikon widget |
| `search-api(...)` | Dinamikus keresés – futásidőben tölt be lehetőségeket egy API-ból |
{{< /table >}}

### Példa: Likert-skála

| type | name | label | appearance |
|------|------|-------|------------|
| select_one satisfaction | service_rating | Mennyire elégedett a szolgáltatással? | likert |

### Példa: Kompakt 3 oszlop

| type | name | label | appearance |
|------|------|-------|------------|
| select_one regions | region | Válasszon régiót | compact-3 |

## Kaszkád kiválasztók

A kaszkád (összekapcsolt) kiválasztó az előző kérdésben kiválasztott érték alapján szűri a lehetőségeket. Használja a `choice_filter` oszlopot a choices munkalap egyik oszlopának nevével.

**survey:**

| type | name | label | choice_filter |
|------|------|-------|---------------|
| select_one province | province | Válasszon tartományt | |
| select_one district | district | Válasszon körzetet | province_name = ${province} |

**choices:**

| list_name | name | label | province_name |
|-----------|------|-------|---------------|
| province | nairobi | Nairobi | |
| province | mombasa | Mombasa | |
| district | westlands | Westlands | nairobi |
| district | kasarani | Kasarani | nairobi |
| district | nyali | Nyali | mombasa |
| district | likoni | Likoni | mombasa |

Amikor a válaszadó a `nairobi` lehetőséget választja, a körzetek listáján csak `Westlands` és `Kasarani` jelenik meg.

{{% alert icon=" " context="warning" %}}
A `choice_filter` értékeként használt oszlopnév (pl. `province_name`) kötelezően szerepeljen a choices munkalapon. A `${province}` a `province` nevű felmérési mezőre hivatkozik.
{{% /alert %}}

## A kiválasztott érték felhasználása kifejezésekben

Hivatkozzon a kiválasztott **értékre** (ne a feliratra) a `${mezőnév}` szintaxissal:

```
relevant: ${consent} = 'yes'
```

A lehetőség feliratának lekérdezéséhez az érték helyett használja a `choice-label()` függvényt:

```
calculate: choice-label(${education_level}, ${education_level})
```

## „Egyéb" lehetőség szöveges bevitellel

Általános minta egy „egyéb" lehetőség beillesztése, amely megnyit egy szövegmezőt:

| type | name | label | relevant |
|------|------|-------|----------|
| select_one occupation | job | Mi a foglalkozása? | |
| text | job_other | Kérjük, pontosítsa | `${job} = 'other'` |

**choices:**

| list_name | name | label |
|-----------|------|-------|
| occupation | farmer | Mezőgazda |
| occupation | trader | Kereskedő |
| occupation | student | Tanuló |
| occupation | other | Egyéb (kérjük, pontosítsa) |

## Bevált módszerek

1. Tartsa rövidre és kölcsönösen kizáróra a listákat – ha a válaszadók egynél többet is szeretnének választani, használjon `select_multiple` típust.
2. Tegye első helyre a leggyakoribb választ, vagy rendezze ábécésorrendbe hosszú listák esetén.
3. Mindig foglalja bele a „Nem tudom" vagy „Nem kívánom megadni" lehetőséget, ahol ez releváns.
4. 7–8 lehetőségnél több esetén mobilon használjon `minimal` (legördülő) megjelenítést a képernyőterület megtakarítása érdekében.
5. Kaszkád kiválasztóknál adjon hozzá minden szűrési oszlopot a choices munkalapon az űrlap elkészítése előtt.

## Korlátozások

- A válaszadó csak egy lehetőséget választhat – több válaszos kérdésekhez használjon `select_multiple` típust.
- A `likert` megjelenítés 5–7 lehetőséggel működik a legjobban, amelyek elférnek egy sorban.
- A `quick` automatikus ugrás csak mobilon működik; web-formulákon nincs hatása.
