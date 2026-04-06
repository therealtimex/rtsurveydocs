---
title: "Välj från fil"
description: "select_one_from_file och select_multiple_from_file laddar alternativ dynamiskt från en extern CSV- eller XML-fil bifogad till formuläret."
icon: "file-earmark-spreadsheet"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 241
---

`select_one_from_file` och `select_multiple_from_file` fungerar som `select_one` och `select_multiple`, men istället för att definiera alternativ i kalkylbladet **choices** laddas alternativen från en **extern CSV- eller XML-fil** bifogad till formuläret. Detta är användbart när din alternativlista är mycket lång, ändras ofta eller behöver uppdateras utan att bygga om hela formuläret.

## Grundläggande XLSForm-specifikation

| type | name | label |
|------|------|-------|
| select_one_from_file health_facilities.csv | facility | Välj hälsoinrättning |
| select_multiple_from_file crops.csv | crops | Vilka grödor odlar hushållet? |

Filnamnet efter typnamnet måste matcha namnet på filen du bifogar när du laddar upp formuläret.

## CSV-filformat

Din CSV-fil måste ha minst två kolumner: `name` (det lagrade värdet) och `label` (den visade texten). Du kan lägga till valfritt antal extra kolumner för filtrering.

**health_facilities.csv:**

```
name,label,district,type
HF001,Nairobi Central Clinic,Nairobi,clinic
HF002,Westlands Health Centre,Nairobi,health_centre
HF003,Kisumu District Hospital,Kisumu,hospital
```

## Filtrera alternativ

Använd kolumnen `choice_filter` för att bara visa alternativ som matchar det aktuella sammanhanget. Referera till CSV-kolumner med deras kolumnnamn direkt (utan `${}`):

| type | name | label | choice_filter |
|------|------|-------|---------------|
| select_one districts.csv | district | Välj distrikt | |
| select_one_from_file health_facilities.csv | facility | Välj inrättning | district = ${district} |

I det här exemplet visas bara inrättningar i det valda distriktet. `district` i `choice_filter` refererar till kolumnen `district` i CSV-filen; `${district}` refererar till formulärfältet med namnet `district`.

## Användningsområden

Select-from-file-frågor används vanligtvis för:

1. **Långa alternativlistor** — hälsoinrättningar, skolor, byar, artlistor (hundratals eller tusentals objekt)
2. **Ofta uppdaterade listor** — när masterlistan ändras mellan undersökningsomgångar, uppdatera bara CSV-filen utan att bygga om formuläret
3. **Delade referensdata** — en CSV-fil används i flera formulär
4. **Filtrerade kaskaderande val** — ladda alla regioner/distrikt/byar i en fil, filtrera sedan efter det överordnade valet

## Bifoga filen

När du laddar upp ditt formulär till rtSurvey, bifoga CSV-filen som en **mediabilaga**. Filnamnet i formulärdefinitionen måste exakt matcha filnamnet på bilagan.

{{% alert icon=" " context="warning" %}}
Filnamn är skiftlägeskänsliga. `Health_Facilities.csv` och `health_facilities.csv` behandlas som olika filer.
{{% /alert %}}

## Använda `choice-label()` med from-file

För att visa etiketten för ett valt alternativ i ett note- eller calculate-fält:

| type | name | label | calculation |
|------|------|-------|-------------|
| select_one_from_file health_facilities.csv | facility | Välj inrättning | |
| calculate | facility_label | | choice-label(${facility}, ${facility}) |
| note | summary | Vald inrättning: ${facility_label} | |

## Bästa praxis

1. Håll dina CSV-filer under 5 000 rader för god prestanda på mobila enheter.
2. Inkludera alltid kolumnerna `name` och `label` — ytterligare kolumner är valfria.
3. För kaskaderande val, använd en enda CSV med en överordnad kolumn och filtrera med `choice_filter`.
4. Versionshantera dina CSV-filnamn (t.ex. `facilities_v3.csv`) vid större ändringar av kolumnstrukturen.
5. Testa filtreringsuttryck noggrant — ett stavfel i `choice_filter` visar tyst inga alternativ.

## Begränsningar

- Mycket stora CSV-filer (10 000+ rader) kan sakta ned formulärladdning, särskilt på lågspecificerade enheter.
- CSV-filer måste laddas upp tillsammans med formuläret — de kan inte hämtas från en URL vid körning.
- `select_multiple_from_file` stöds mer sällan av klienter — verifiera kompatibilitet innan användning.

## Jämförelse med `search()`

| | `select_one_from_file` | `search()` utseende |
|--|----------------------|----------------------|
| Alternativkälla | Bifogad CSV/XML-fil | Serversidesbaserad databasfråga |
| Fungerar offline | Ja (filen är paketerad) | Kräver anslutning |
| Antal alternativ | Begränsat av enhetens minne | Obegränsat (paginerat) |
| Realtidsdata | Nej | Ja |

För stora, ofta ändrade eller serverbaserade datamängder, se [Dynamisk sökning](../advanced-extension/dynamic-search).
