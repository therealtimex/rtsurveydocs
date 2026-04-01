---
title: "Default"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 287
---

Predvolené hodnoty v rtSurvey umožňujú predvyplniť otázky odpoveďami, keď s nimi respondent prvýkrát stretne. Táto funkcia môže výrazne zlepšiť efektivitu prieskumu a kvalitu dát poskytnutím počiatočných hodnôt, ktoré sú buď bežne vyberané alebo slúžia ako príklady očakávaného vstupu.

## Základné použitie

Na nastavenie predvolenej hodnoty použite stĺpec `default` vo vašom XLSForm:

```
| type    | name        | label                         | default    |
|---------|-------------|-------------------------------|------------|
| date    | survey_date | Dátum prieskumu                   | 2024-07-04 |
| decimal | weight      | Váha respondenta? (v kg)      | 51.3       |
```

V tomto príklade bude dátum prieskumu predvyplnený 4. júlom 2024 a pole pre váhu začne s hodnotou 51,3 kg.

## Dynamické predvolené hodnoty

rtSurvey podporuje dynamické predvolené hodnoty pomocou funkcií:

```
| type | name | label                              | default  |
|------|------|------------------------------------| ---------|
| date | d    | Zadajte dátum, kedy k udalosti došlo? | today()  |
```

Tu funkcia `today()` automaticky nastaví predvolenú hodnotu na aktuálny dátum.

## Funkcie špecifické pre rtSurvey

### Predvolené hodnoty zohľadňujúce kontext

rtSurvey rozširuje funkcionalitu predvolených hodnôt o predvolené hodnoty zohľadňujúce kontext:

```
| type    | name     | label           | default            |
|---------|----------|-----------------|---------------------|
| text    | location | Aktuálna poloha| ${current_location} |
```

Toto používa premennú `${current_location}` rtSurvey na predvyplnenie polohy na základe GPS zariadenia.

### Kaskádové predvolené hodnoty

rtSurvey umožňuje predvolené hodnoty na základe predchádzajúcich odpovedí:

```
| type    | name     | label           | default         |
|---------|----------|-----------------|-----------------|
| text    | city     | Mesto            |                 |
| text    | district | Okres        | ${city}-district|
```

Tu je pole okresu predvyplnené na základe zadaného mesta.

### Predvolené hodnoty v opakovaniach

Pre otázky vo vnútri skupiny opakovania je predvolená hodnota vypočítaná pri pridaní opakovania:

```
| type         | name      | label        | default                |
|--------------|-----------|--------------|------------------------|
| begin repeat | visits    | Návštevy kliniky|                        |
| date         | visit_date| Dátum návštevy   | ${previous_visit_date} |
| end repeat   |           |              |                        |
```

Toto nastavuje predvolený dátum návštevy na dátum predchádzajúcej návštevy.

## Najlepšie postupy pre používanie predvolených hodnôt

1. **Používajte striedmo**: Používajte predvolené hodnoty iba tam, kde výrazne zlepšujú efektivitu alebo kvalitu dát.
2. **Zabezpečte presnosť**: Pravidelne kontrolujte a aktualizujte statické predvolené hodnoty.
3. **Dôkladne testujte**: Najmä pri použití dynamických alebo vypočítaných predvolených hodnôt.
4. **Zvážte používateľský zážitok**: Uistite sa, že predvolené hodnoty neuvádzajú respondentov do omylu ani nezavádzajú skresľovanie.
5. **Jasne dokumentujte**: Uistite sa, že všetci členovia tímu rozumejú zdôvodneniu predvolených hodnôt.

## Pokročilé techniky predvolených hodnôt

### Náhodné predvolené hodnoty

rtSurvey podporuje náhodné predvolené hodnoty pre určité typy otázok:

```
| type              | name    | label        | default           |
|-------------------|---------|--------------|-------------------|
| select_one options| choice  | Vyberte jednu:  | random(options)   |
```

Toto náhodne vyberie predvolenú možnosť zo zoznamu „options".

### Podmienené predvolené hodnoty

Použite relevantnosť na nastavenie podmienených predvolených hodnôt:

```
| type    | name     | label    | default | relevant        |
|---------|----------|----------|---------|-----------------|
| text    | other    | Uveďte  | N/A     | ${q1} = 'other' |
```

Tu je „N/A" predvolenou hodnotou iba vtedy, keď je v predchádzajúcej otázke vybraté „other".

## Úvahy pri správe dát

- Predvolené hodnoty sú zahrnuté v exportoch dát, typicky s príznakom označujúcim, že išlo o predvolené hodnoty.
- Funkcia auditného záznamu rtSurvey sleduje, keď respondenti zmenia predvolené hodnoty.

## Správanie mobilnej aplikácie

- Mobilná aplikácia rtSurvey podporuje všetky funkcie predvolených hodnôt vrátane dynamických a kontextovo uvedomelých predvolených hodnôt.
- Offline režim môže ovplyvniť niektoré dynamické predvolené hodnoty, ktoré sa spoliehajú na dáta v reálnom čase.

## Známe obmedzenia

- Zložité vypočítané predvolené hodnoty môžu ovplyvniť čas načítavania formulára, najmä na zariadeniach nižšej triedy.
- Niektoré dynamické predvolené hodnoty nemusia fungovať podľa očakávaní v režime náhľadu.

## Riešenie problémov s predvolenými hodnotami

1. **Predvolená hodnota sa nezobrazuje**: Skontrolujte syntaktické chyby vo výraze predvolenej hodnoty.
2. **Neočakávané hodnoty**: Overte logiku výpočtu a testujte s rôznymi scenármi.
3. **Problémy s výkonom**: Optimalizujte zložité výpočty alebo zvážte alternatívne prístupy.
