---
title: "Gruppering af spørgsmål"
description: ""
icon: "auto_awesome"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 250
---

Grupper i XLSForm giver dig mulighed for at organisere relaterede spørgsmål sammen, hvilket forbedrer undersøgelsens struktur og styrker mulighederne for dataanalyse. rtSurvey understøtter fuldt ud XLSForm-grupper og udvider deres funktionalitet med yderligere funktioner.

## Grundlæggende gruppestruktur

For at oprette en gruppe af spørgsmål skal du bruge syntaksen `begin_group` og `end_group`:

```
| type         | name       | label                                    |
|--------------|------------|------------------------------------------|
| begin_group  | respondent | Respondentoplysninger                    |
| text         | name       | Indtast respondentens navn               |
| text         | position   | Indtast respondentens stilling           |
| end_group    |            |                                          |
```

Nøglepunkter:
- Rækken `begin_group` kræver et `name` og `label`.
- Rækken `end_group` behøver ikke et navn eller label.
- Spørgsmål mellem `begin_group` og `end_group` er en del af gruppen.

## Gruppeappearance

rtSurvey understøtter forskellige appearance-muligheder til grupper:

1. **field-list**: Viser flere spørgsmål på den samme skærm.
   ```
   | type         | name       | label       | appearance |
   |--------------|------------|-------------|------------|
   | begin_group  | respondent | Respondent  | field-list |
   | text         | name       | Navn        |            |
   | text         | position   | Stilling    |            |
   | end_group    |            |             |            |
   ```

2. **grid**: Opretter et kompakt, tabelagtigt layout til grupper (rtSurvey-specifikt).

3. **collapsible**: Opretter udvidelige/sammenklappelige grupper (rtSurvey-specifikt).

## Indlejrede grupper

Grupper kan indlejres inden for andre grupper til mere komplekse strukturer:

```
| type         | name       | label                                    |
|--------------|------------|------------------------------------------|
| begin_group  | hospital   | Hospitalsoplysninger                     |
| text         | hosp_name  | Hvad er hospitalets navn?                |
| begin_group  | medication | Medicintilgængelighed                    |
| select_one y_n| hiv_meds  | Har dette hospital HIV-medicin?          |
| end_group    |            |                                          |
| end_group    |            |                                          |
```

**Bemærk**: Afslut altid den senest påbegyndte gruppe først for at opretholde korrekt indlejring.

## Spring-logik for grupper

Brug kolonnen `relevant` til at implementere spring-logik for hele grupper:

```
| type         | name   | label                                        | relevant        |
|--------------|--------|----------------------------------------------|-----------------|
| integer      | age    | Hvor gammel er du?                           |                 |
| begin_group  | child  | Barn                                         | ${age} <= 5     |
| integer      | muac   | Registrér barnets midtarmomkreds             |                 |
| select_one y_n| mrdt  | Er barnets hurtige diagnostiske test positiv?|                |
| end_group    |        |                                              |                 |
```

I dette eksempel vises gruppen `child` kun, hvis respondentens alder er 5 eller yngre.

## Bedste praksis for brug af grupper

1. Brug meningsfulde navne til grupper for at forbedre dataanalysen.
2. Hold grupper fokuseret på relaterede spørgsmål.
3. Brug indlejrede grupper med omtanke for at undgå alt for komplekse strukturer.
4. Test spring-logik grundigt, når du bruger `relevant` på grupper.
5. Overvej at bruge `field-list`-appearance til korte grupper for at reducere rulning.
6. Udnyt rtSurveys grid-layout til kompakt visning af relaterede oplysninger.
7. Brug sammenklappelige grupper til lange formularer for at forbedre navigationen.

## rtSurvey-specifikke funktioner

1. **Grid-layout**: Brug `grid`-appearance til tabelagtige visninger.
2. **Sammenklappelige grupper**: Implementér `collapsible`-appearance til udvidelige sektioner.
3. **Brugerdefineret styling**: Anvend brugerdefineret CSS på grupper til unikke visuelle designs.
4. **Dynamisk gruppeadfærd**: Implementér kompleks spring-logik og beregninger inden for grupper.

## Flersproglig understøttelse

rtSurvey understøtter flersproglige grupper. Brug sprogspecifikke kolonner til labels:

```
| type         | name       | label::Dansk | label::Engelsk |
|--------------|------------|--------------|----------------|
| begin_group  | personal   | Personlige oplysninger | Personal Info |
| text         | name       | Navn         | Name           |
| end_group    |            |              |                |
```

## Kendte begrænsninger

- Ekstremt dyb indlejring af grupper kan påvirke ydeevnen på visse enheder.
- Visse avancerede styling-muligheder er muligvis ikke tilgængelige for grupper i mobilappen.

## Fejlfinding af grupper

1. Sørg for, at hver `begin_group` har en tilsvarende `end_group`.
2. Kontrollér, at gruppenavne er unikke inden for formularen.
3. Bekræft, at spring-logik refererer til korrekte spørgsmålsnavne.
4. Test grupper grundigt på både web- og mobilgrænseflader.
