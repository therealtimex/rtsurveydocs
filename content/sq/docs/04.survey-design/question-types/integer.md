---
title: "Integer"
description: "Pyetjet integer lejojnë hyrje të numrave të plotë në sondazhin tuaj."
icon: "123"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 222
---

Lloji i pyetjes integer në XLSForms dhe rtSurvey përdoret për të mbledhur përgjigje me numra të plotë. Ky lloj pyetjeje është thelbësor për mbledhjen e të dhënave numerike pa shifra decimale, si numërime, mosha, ose vite.

## Specifikimi bazë XLSForm

| type    | name  | label                 |
|---------|-------|------------------------|
| integer | age   | Shkruani moshën tuaj në vite |

Për më shumë detaje mbi llojin bazë të pyetjes integer, shikoni [specifikimin XLSForm](https://xlsform.org/en/#question-types).

## Përdorimet

Pyetjet integer përdoren zakonisht për:

1. Hyrjet e moshës
2. Numërimin e artikujve (p.sh., numri i fëmijëve, anëtarëve të familjes)
3. Hyrjet e vitit (p.sh., viti i lindjes)
4. Vlerësimet në shkallë numerike
5. Çdo mbledhje të dhënash me numra të plotë

## Zgjerime të rtSurvey

Ndërsa specifikimi bazë XLSForm për pyetjet integer është i thjeshtë, rtSurvey ofron veçori ose personalizime shtesë:

1. Validimi i diapazonit
2. Mesazhet e gabimit të personalizuara
3. Opsionet e pamjes për hyrjen e numrave

## Praktikat më të mira

1. Përdorni etiketa të qarta dhe të qarta për të specifikuar hyrjen e pritur.
2. Zbatoni kufizime diapazoni për të parandaluar hyrjet jorealike ose të gabuara.
3. Konsideroni përdorimin e tekstit hint për të dhënë shembuj ose sqaruar formatin e pritur.
4. Për numra të mëdhenj, konsideroni përdorimin e presjes ose hapësirave në etiketë për të përmirësuar lexueshmërinë.

## Kufizimet dhe validimi

Mund të shtoni kufizime për të siguruar që vlera e futur bie brenda një diapazoni specifik:

| type    | name  | label                 | constraint        | constraint_message                    |
|---------|-------|------------------------|-------------------|---------------------------------------|
| integer | age   | Shkruani moshën tuaj në vite | .>0 and .<=120 | Mosha duhet të jetë midis 1 dhe 120 vjetësh |

## Shembull i përdorimit

Ja një shembull se si mund të përdorni pyetjet integer në një sondazh shtëpie:

| type    | name           | label                                     | constraint | constraint_message                |
|---------|----------------|-------------------------------------------|------------|-----------------------------------|
| integer | household_size | Sa njerëz jetojnë në shtëpinë tuaj?      | .>0        | Madhësia e familjes duhet të jetë të paktën 1 |
| integer | num_children   | Sa fëmijë nën 18 vjeç ka familja?        | .>=0       | Numri i fëmijëve nuk mund të jetë negativ |
| integer | year_built     | Në cilin vit u ndërtua shtëpia juaj?     | .>1800 and .<=2023 | Viti duhet të jetë midis 1800 dhe 2023 |

## Llogaritja me vlerat integer

Vlerat integer mund të përdoren në llogaritje. Ja një shembull:

| type    | name           | label                                     |
|---------|----------------|-------------------------------------------|
| integer | num_adults     | Numri i të rriturve në familje           |
| integer | num_children   | Numri i fëmijëve në familje             |
| calculate | total_members | |

Në rreshtin calculate, mund të përdorni:

```
calculation | ${num_adults} + ${num_children}
```

Kjo do të mbledhë numrin e të rriturve dhe fëmijëve për të marrë numrin total të anëtarëve të familjes.
