---
title: "Data ir laikas"
description: "Datos ir laiko klausimai leidžia respondentams viename lauke įvesti datą ir laiką."
icon: "event"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 226
---

XLSForm ir rtSurvey datos ir laiko klausimo tipas leidžia respondentams viename lauke įvesti ir datą, ir laiką. Šis klausimo tipas naudingas, kai reikia užfiksuoti konkretų laiko momentą, įskaitant datą ir tikslų laiką.

## Pagrindinė XLSForm specifikacija

| type     | name           | label                           |
|----------|----------------|--------------------------------|
| datetime | event_datetime | Kada įvyko įvykis?             |

## Naudojimo atvejai

Datos ir laiko klausimai dažnai naudojami:

1. Įvykių ar stebėjimų laiko žymoms įrašyti
2. Susitikimams ar posėdžiams planuoti
3. Veiklos pradžios ir pabaigos laikams registruoti
4. Tiksliems momentams fiksuoti laiko jautriems duomenų rinkimams

## rtSurvey plėtiniai

rtSurvey išplečia datos ir laiko klausimų funkcionalumą įvairiais išvaizdos ir tinkinimo parametrais:

### Išvaizdos parinktys

- `(numatytasis)`: Rodo kalendorių ir laikrodį datai ir laikui pasirinkti
- `inline`: Rodo kalendorių ir laikrodį kaip piktogramas
- `inline-1line`: Rodo kalendorių ir laikrodį pasirinkimui vienos eilutės formatu
- `inline-onlyresult`: Rodo kalendorių ir laikrodį kaip piktogramas eilutės gale; piktogramos dingsta po pasirinkimo

### Spalvų tinkinimas

Galite tinkinti kalendoriaus ir laikrodžio piktogramų spalvą naudodami funkciją `colors()`:

- `inline colors("0099FF")`: Rodo piktogramas su pasirinktine spalva
- `inline-1line-0000FF`: Rodo vienos eilutės formatu su pasirinktine spalva
- `inline-1line colors("0000FF","FFFF00")`: Rodo vienos eilutės formatu su keliomis pasirinktinėmis spalvomis
- `inline-onlyresult colors("0099FF")`: Rodo piktogramas, kurios dingsta po pasirinkimo, su pasirinktine spalva

### Pasirinktiniai datos ir laiko formatai

rtSurvey leidžia pasirinktinus datos ir laiko formatus naudojant specialią sintaksę:

- `inline-[%Y-%m-%d %H:%M:%S]`: Pasirinktinio formato pavyzdys (Metai-Mėnuo-Diena Valanda:Minutė:Sekundė)
- `inline-[%d/%m/%Y %I:%M %p]`: Pasirinktinio formato pavyzdys (Diena/Mėnuo/Metai Valanda:Minutė AM/PM)

## Naudojimo pavyzdys

Štai pavyzdys, kaip galima naudoti datos ir laiko klausimą apklausoje:

| type     | name           | label                                      | appearance                    |
|----------|----------------|--------------------------------------------|-----------------------------|
| datetime | incident_time  | Kada įvyko incidentas?                     | inline-[%d/%m/%Y %I:%M %p]  |

## Geriausios praktikos

1. Pateikite aiškias instrukcijas apie tikėtiną datos ir laiko formatą.
2. Apsvarstykite galimybę naudoti `inline` išvaizdą kompaktiškesniam rodymui.
3. Naudokite pasirinktinus formatus, kai reikia konkrečių datos ir laiko komponentų ar formatavimo.
4. Rinkdami datos ir laiko duomenis skirtinguose regionuose, atkreipkite dėmesį į laiko juostas.

## Apribojimai

- Kai kurios išvaizados ar pasirinktiniai formatai gali būti nepalaikomi visuose įrenginiuose ar platformose.
- Naudotojai gali reikėti nurodymo teisingai įvesti datą ir laiką, ypač naudojant pasirinktinus formatus.
- Laiko juostų skirtumai gali apsunkinti duomenų analizę, jei jie tinkamai neatsižvelgiami.
