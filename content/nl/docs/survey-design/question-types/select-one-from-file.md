---
title: "Selecteer uit bestand"
description: "select_one_from_file en select_multiple_from_file laden keuzes dynamisch vanuit een extern CSV- of XML-bestand dat bij het formulier is bijgevoegd."
icon: "file-earmark-spreadsheet"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 241
---

`select_one_from_file` en `select_multiple_from_file` werken zoals `select_one` en `select_multiple`, maar in plaats van keuzes te definiëren in het **choices-werkblad**, worden de keuzes geladen vanuit een **extern CSV- of XML-bestand** dat bij het formulier is bijgevoegd. Dit is nuttig wanneer uw keuzelijst erg lang is, regelmatig verandert, of moet worden bijgewerkt zonder het gehele formulier opnieuw te bouwen.

## Basis XLSForm-specificatie

| type | name | label |
|------|------|-------|
| select_one_from_file health_facilities.csv | facility | Selecteer de zorginstelling |
| select_multiple_from_file crops.csv | crops | Welke gewassen verbouwt het huishouden? |

De bestandsnaam na de typenaam moet overeenkomen met de naam van het bestand dat u bijvoegt bij het uploaden van het formulier.

## CSV-bestandsformaat

Uw CSV-bestand moet minimaal twee kolommen hebben: `name` (de opgeslagen waarde) en `label` (de weergegeven tekst). U kunt een willekeurig aantal extra kolommen toevoegen voor filteren.

**health_facilities.csv:**

```
name,label,district,type
HF001,Nairobi Central Clinic,Nairobi,clinic
HF002,Westlands Health Centre,Nairobi,health_centre
HF003,Kisumu District Hospital,Kisumu,hospital
```

## Keuzes filteren

Gebruik de kolom `choice_filter` om alleen de keuzes te tonen die overeenkomen met de huidige context. Verwijs rechtstreeks naar CSV-kolommen met hun kolomnaam (geen `${}`):

| type | name | label | choice_filter |
|------|------|-------|---------------|
| select_one districts.csv | district | Selecteer district | |
| select_one_from_file health_facilities.csv | facility | Selecteer instelling | district = ${district} |

In dit voorbeeld worden alleen instellingen in het geselecteerde district weergegeven. Het `district` in `choice_filter` verwijst naar de kolom `district` in het CSV-bestand; `${district}` verwijst naar het formulierveld genaamd `district`.

## Toepassingen

Selecteer-uit-bestand-vragen worden veelgebruikt voor:

1. **Lange keuzelijsten** — zorginstellingen, scholen, dorpen, soortlijsten (honderden of duizenden items)
2. **Frequent bijgewerkte lijsten** — wanneer de hoofdlijst verandert tussen enquêteronden, werk alleen de CSV bij zonder het formulier opnieuw te bouwen
3. **Gedeelde referentiegegevens** — één CSV-bestand gebruikt in meerdere formulieren
4. **Gefilterde cascaderende selecties** — laad alle regio's/districten/dorpen in één bestand, filter dan op de bovenliggende selectie

## Het bestand bijvoegen

Wanneer u uw formulier uploadt naar rtSurvey, voegt u het CSV-bestand bij als een **mediabijlage**. De bestandsnaam in de formulierformulering moet exact overeenkomen met de bestandsnaam van de bijlage.

{{% alert icon=" " context="warning" %}}
Bestandsnamen zijn hoofdlettergevoelig. `Health_Facilities.csv` en `health_facilities.csv` worden behandeld als verschillende bestanden.
{{% /alert %}}

## `choice-label()` gebruiken met from-file

Om het label van een geselecteerde keuze weer te geven in een notitie- of berekeningsveld:

| type | name | label | calculation |
|------|------|-------|-------------|
| select_one_from_file health_facilities.csv | facility | Selecteer instelling | |
| calculate | facility_label | | choice-label(${facility}, ${facility}) |
| note | summary | Geselecteerde instelling: ${facility_label} | |

## Aanbevolen werkwijzen

1. Houd uw CSV-bestanden onder 5.000 rijen voor goede prestaties op mobiele apparaten.
2. Neem altijd een kolom `name` en `label` op — extra kolommen zijn optioneel.
3. Gebruik voor cascaderende selecties één CSV met een bovenliggende kolom en filter met `choice_filter`.
4. Versieer uw CSV-bestandsnamen (bijv. `facilities_v3.csv`) bij het maken van ingrijpende wijzigingen aan de kolomstructuur.

## Beperkingen

- Zeer grote CSV-bestanden (10.000+ rijen) kunnen het laden van formulieren vertragen, vooral op apparaten aan de onderkant van de markt.
- CSV-bestanden moeten worden geüpload samen met het formulier — ze kunnen niet worden opgehaald van een URL bij uitvoering.
- `select_multiple_from_file` wordt minder vaak ondersteund in clients — verifieer compatibiliteit voor gebruik.
