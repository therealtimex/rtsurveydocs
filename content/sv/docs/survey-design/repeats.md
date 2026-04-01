---
title: "Upprepande frågor"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 260
---

Upprepningar är en kraftfull funktion i rtSurvey som låter dig samla in samma uppsättning information flera gånger i en enda undersökning. Detta är särskilt användbart för scenarier som hushållsundersökningar, där du kan behöva samla in data om flera hushållsmedlemmar.

## Grundläggande upprepningsstruktur

För att skapa en upprepning i rtSurvey, använd konstruktionen `begin repeat` och `end repeat`:

```
| type         | name         | label                |
|--------------|--------------|----------------------|
| begin repeat | child_repeat |                      |
| text         | name         | Barnets namn         |
| decimal      | birthweight  | Barnets födelsvikt   |
| select_one male_female | sex | Barnets kön         |
| end repeat   |              |                      |
```

I det här exemplet kan användaren samla in information om flera barn genom att lägga till nya upprepningar i formuläret.

## Namnge upprepningar

Även om kolumnen `label` är valfri för `begin repeat`, kan en etikett förbättra navigeringen:

```
| type         | name         | label                |
|--------------|--------------|----------------------|
| begin repeat | child_repeat | Barnuppgifter        |
| text         | name         | Barnets namn         |
| decimal      | birthweight  | Barnets födelsvikt   |
| select_one male_female | sex | Barnets kön         |
| end repeat   |              |                      |
```

rtSurvey visar "Barnuppgifter" som titel för varje upprepningsinstans.

## Fast antal upprepningar

För att ange ett fast antal upprepningar, använd kolumnen `repeat_count`:

```
| type         | name         | label                | repeat_count |
|--------------|--------------|----------------------|--------------|
| begin repeat | child_repeat | Barnuppgifter        | 3            |
| text         | name         | Barnets namn         |              |
| decimal      | birthweight  | Barnets födelsvikt   |              |
| end repeat   |              |                      |              |
```

Detta skapar exakt 3 barnupprepningar.

## Dynamiskt antal upprepningar

rtSurvey stöder dynamiska upprepningsantal baserade på tidigare svar:

```
| type     | name           | label                          | repeat_count       |
|----------|----------------|--------------------------------|--------------------|
| integer  | num_hh_members | Antal hushållsmedlemmar?       |                    |
| begin repeat | hh_member  | Hushållsmedlem                 | ${num_hh_members}  |
| text     | name           | Namn                           |                    |
| integer  | age            | Ålder                          |                    |
| end repeat |              |                                |                    |
```

## Villkorliga upprepningar

Du kan använda kolumnen `relevant` för att villkorligt visa upprepningar:

```
| type              | name        | label                     | relevant           |
|-------------------|-------------|---------------------------|---------------------|
| select_one yes_no | has_child   | Bor det några barn här?   |                     |
| begin repeat      | child_repeat| Barnuppgifter             | ${has_child} = 'yes'|
| text              | name        | Barnets namn              |                     |
| decimal           | birthweight | Barnets födelsvikt        |                     |
| end repeat        |             |                           |                     |
```

## rtSurvey-specifika funktioner

### Upprepningssammanfattning

rtSurvey tillhandahåller en sammanfattningsvy av upprepningar. För att anpassa sammanfattningen, använd en grupp inom upprepningen:

```
| type         | name         | label                                    |
|--------------|--------------|------------------------------------------|
| begin repeat | person_repeat|                                          |
| begin group  | person       | ${first_name} ${last_name} - ${age}      |
| text         | first_name   | Förnamn                                  |
| text         | last_name    | Efternamn                                |
| integer      | age          | Ålder                                    |
| end group    |              |                                          |
| end repeat   |              |                                          |
```

### Utseendealternativ för upprepningar

rtSurvey erbjuder ytterligare utseendealternativ för upprepningar:

- `appearance: field-list` - Visar alla frågor i en upprepning på en skärm
- `appearance: table-list` - Presenterar upprepningar i ett tabellformat

```
| type         | name         | label            | appearance  |
|--------------|--------------|-------------------|-------------|
| begin repeat | child_repeat | Barnuppgifter     | table-list  |
| text         | name         | Namn              |             |
| integer      | age          | Ålder             |             |
| end repeat   |              |                   |             |
```

### Kapslade upprepningar

rtSurvey stöder kapslade upprepningar för komplexa datastrukturer:

```
| type         | name           | label                |
|--------------|----------------|----------------------|
| begin repeat | household      | Hushåll              |
| text         | hh_name        | Hushållets namn      |
| begin repeat | hh_member      | Hushållsmedlem       |
| text         | member_name    | Medlemmens namn      |
| integer      | member_age     | Medlemmens ålder     |
| end repeat   |                |                      |
| end repeat   |                |                      |
```

## Bästa praxis för att använda upprepningar i rtSurvey

1. Använd meningsfulla namn och etiketter för upprepningar för att förbättra dataanalysen.
2. Överväg att använda dynamiska upprepningsantal för att minska datainmatningsfel.
3. Testa ditt formulär noggrant, särskilt när du använder komplexa kapslade upprepningar.
4. Använd sammanfattningsfunktionen för att hjälpa räknare att navigera i långa listor med upprepningar.
5. Var försiktig med stora antal upprepningar, eftersom de kan påverka formulärets prestanda.

## Hantera noll upprepningar

För att representera noll upprepningar i rtSurvey:

1. Träna räknare att ta bort den första upprepningen om den inte behövs.
2. Använd dynamiska upprepningsantal när det exakta antalet är känt.
3. Använd `relevant` för att villkorligt visa upprepningar.

## Överväganden vid dataexport

När du exporterar data från rtSurvey plattas upprepningsdata normalt ut. Varje upprepningsinstans blir en separat rad i de exporterade data, med formulärets överordnade data upprepat för varje instans.

## Överväganden för mobilappen

- Upprepningar i rtSurvey-mobilappen stöder datainsamling offline.
- Stora antal upprepningar kan påverka appens prestanda på lågspecificerade enheter.

Genom att effektivt använda upprepningar i rtSurvey kan du skapa flexibla och kraftfulla undersökningar som kan fånga komplexa, hierarkiska datastrukturer samtidigt som du upprätthåller ett användarvänligt gränssnitt för räknare.
