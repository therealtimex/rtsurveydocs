---
title: "Uzlabotas paplašinājumi"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 289
---

Kolonna `appearance` rtSurvey ļauj pielāgot jautājumu vizuālo prezentāciju un uzvedību aptaujās. Šī funkcija uzlabo lietotāja pieredzi un var ievērojami uzlabot datu vākšanas efektivitāti. rtSurvey atbalsta standarta XLSForm izskata atribūtus un paplašina tos ar papildu iespējām.

## rtSurvey specifisko izskatu paplašinājumi

rtSurvey paplašina standarta izskata iespējas ar šādiem:

### Laika ievades pielāgošana

`text` tipa jautājumiem, ko izmanto laika ievadei:

- `appearance: inline` — Rāda pulksteni kā ikonu
- `appearance: inline-1line` — Rāda pulksteni vienas rindas formātā
- `appearance: inline-onlyresult` — Rāda pulksteņa ikonu, kas pazūd pēc atlases
- `appearance: inline-[FORMAT]` — Pielāgo laika formāta attēlojumu (piemēram, `[%H:%M]`, `[%h:%M:%S]`)

### Krāsas pielāgošana

rtSurvey ļauj pielāgot krāsas dažādiem izskatiem:

- `appearance: inline colors("0099FF")` — Pielāgo ikonas krāsu
- `appearance: inline-1line colors("0000FF","FFFF00")` — Pielāgo krāsas vienas rindiņas formātā

### Režģa izkārtojums

rtSurvey ievieš režģa izkārtojumu kompaktiem, tabulai līdzīgiem attēlojumiem:

- `appearance: grid` — Attiecas uz grupām, lai izveidotu režģa izkārtojumu

### Sakļaujamas grupas

- `appearance: collapsible` — Izveido paplašināmas/sakļaujamas grupas

## Labākā prakse izskata izmantošanai

1. **Konsekvence**: Izmantojiet izskata atribūtus konsekventi visā aptaujā vienotam izskatam.
2. **Mobilais pret tīmekli**: Apsveriet, kā izskati tiks renderēti dažādās ierīcēs un platformās.
3. **Veiktspēja**: Esiet uzmanīgi ar izskata atribūtiem, kas var palēnināt formas ielādi.
4. **Lietotāja pieredze**: Izvēlieties izskata variantus, kas atvieglo datu ievadi respondentiem.
5. **Testēšana**: Vienmēr pārbaudiet formu mērķa ierīcēs, lai nodrošinātu izskata pareizību.
