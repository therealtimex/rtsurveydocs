---
title: "File"
description: "Pyetjet file lejojnë të anketuarit të ngarkojnë dokumente dhe skedarë të tjerë si pjesë të përgjigjeve të tyre të sondazhit."
icon: "upload_file"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 230
---

Lloji i pyetjes `file` lejon të anketuarit të **ngarkojnë çdo skedar** nga pajisja e tyre — dokumente, spreadsheet, PDF, ose lloje të tjera skedarësh. Ndryshe nga `image`, `audio`, dhe `video` që nisin mjete specifike kapjeje, `file` hap zgjedhësin e skedarit me qëllim të përgjithshëm.

## Specifikimi bazë XLSForm

| type | name      | label                        |
|------|-----------|------------------------------|
| file | document  | Ju lutemi ngarkoni dokumentin tuaj |

Për më shumë detaje mbi llojin standard të pyetjes file, shikoni [specifikimin XLSForm](https://xlsform.org/en/#question-types).

## Përdorimet

Pyetjet file përdoren zakonisht për:

1. Mbledhja e dokumenteve mbështetëse (faturat, certifikatat, kontratat, raportet)
2. Ngarkimi i formularëve të letrës të plotësuara që u skanuan
3. Mbledhja e spreadsheet-eve ose eksporteve të të dhënave nga sisteme të tjera
4. Çdo lloj skedari dixhital që image/audio/video nuk mbulojnë

## Formati i të dhënave

Skedarët e ngarkuar ruhen si bashkëngjitje binare:

- **Formati:** I ruajtur në formatin origjinal (PDF, XLSX, DOCX, etj.)
- **Emërtimi:** `{instanceID}-{fieldname}.{extension}`
- **Ruajtja:** Ngarkuar në dosjen media të serverit krahas dorëzimit
- **Aksesi:** I shkarkueshëm nga ndërfaqja e menaxhimit të dorëzimeve

## Zgjerime të rtSurvey

### Llojet e pranuara të skedarëve

Përdorni kolonën `parameters` për të kufizuar se cilat lloje skedarësh mund të zgjidhen:

| type | name | label | parameters |
|------|------|-------|------------|
| file | report | Ngarkoni raportin e inspektimit | `accept=.pdf` |
| file | spreadsheet | Ngarkoni skedarin e të dhënave | `accept=.xlsx,.csv` |

Parametri `accept` përdor sintaksën standarde të shtesës së skedarit (të ndarë me presje).

### Udhëzimi i madhësisë së skedarit

rtSurvey nuk zbaton kufizim të fortë të madhësisë së skedarit në nivel pyetjeje, por kufizimet e ngarkimit të serverit zbatohen. Përdorni `hint` për të komunikuar pritshmëritë me numëruesin:

| type | name | label | hint |
|------|------|-------|------|
| file | receipt | Ngarkoni faturën e pagesës | Pranuar: PDF ose imazh. Madhësia maksimale e skedarit: 5 MB |

### Integrimi me sistemin e skedarëve të pajisjes dhe ruajtjen cloud

Në Android dhe iOS, pyetja `file` hap zgjedhësin nativ të skedarëve të pajisjes, i cili mund të përfshijë akses në:
- Ruajtjen lokale të pajisjes
- Kartën SD (Android)
- iCloud Drive (iOS)
- Google Drive, Dropbox (nëse janë instaluar)

Në web, hap dialogun standard të ngarkimit të skedarit të shfletuesit.

## Shembull i përdorimit

### Ngarkimi i detyrueshëm i PDF

| type | name | label | hint | required | required_message |
|------|------|-------|------|----------|-----------------|
| file | signed_consent | Ngarkoni formularin e firmosur të pëlqimit | Vetëm PDF, maks 2MB | yes | Kërkohet formular pëlqimi |

### Ngarkimi i dokumentit i kushtëzuar

| type | name | label | relevant |
|------|------|-------|----------|
| select_one yesno | has_land_title | A ka familja titull toke? | |
| file | land_title_doc | Ngarkoni foto ose skanim të titullit të tokës | `${has_land_title} = 'yes'` |

## Praktikat më të mira

1. Përdorni `accept` për të kufizuar llojet e skedarëve — kjo parandalon numëruesit të ngarkojnë aksidentalisht skedarë të gabuar.
2. Gjithmonë përfshini udhëzime madhësie dhe formati në kolonën `hint`.
3. Për fotografi dhe imazhe, përdorni llojin `image` — ofron kompresim më të mirë dhe trajtim të qëndrueshëm të formatit.
4. Për sondazhet e mëdha me bashkëngjitje skedarësh, planifikoni ruajtjen e të dhënave dhe gjerësinë e brezit të shkarkimit.
5. Testoni zgjedhësin e skedarëve në llojin e synuar të pajisjes (Android vs. iOS vs. web) para vendosjes — aksesi në drejtoritë cloud ndryshon.

## Konsideratat e trajtimit të të dhënave

- Skedarët ruhen në formatin e tyre origjinal; nuk konvertohen ose kompresohen nga rtSurvey.
- Analizoni skedarët pas shkarkimit — rtSurvey nuk nxjerr ose indekson përmbajtjen e skedarëve.
- Bashkëngjitjet e mëdha skedarësh rrisin ndjeshëm kohën e nevojshme për të shkarkuar bashkësi të dhënash të plota.

## Kufizimet

- Pyetjet file nuk validojnë përmbajtjen e skedarëve — vetëm kontrolli i shtesës së skedarit nëpërmjet `accept` zbatohet në nivel UI.
- Skedarët shumë të mëdhenj (100 MB+) mund të kalojnë afatin kohor gjatë ngarkimit në mjedise me lidhje të dobët.
- Numëruesit offline mund të bashkëngjissin skedarë, por nuk do të ngarkohen deri sa të rikthehet lidhja.
- Disa konfigurime pajisje kufizojnë aksesin në vendndodhje të caktuara ruajtjeje (p.sh., politikat e MDM të korporatave).
