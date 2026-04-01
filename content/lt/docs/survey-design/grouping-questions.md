---
title: "Klausimų grupavimas"
description: ""
icon: "auto_awesome"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 250
---

XLSForm grupės leidžia organizuoti susijusius klausimus kartu, gerinant apklausos struktūrą ir duomenų analizės galimybes. rtSurvey visiškai palaiko XLSForm grupes ir praplečia jų funkcionalumą papildomomis funkcijomis.

## Pagrindinė grupės struktūra

Norėdami sukurti klausimų grupę, naudokite `begin_group` ir `end_group` sintaksę:

```
| type         | name       | label                                    |
|--------------|------------|------------------------------------------|
| begin_group  | respondent | Respondento informacija                  |
| text         | name       | Įveskite respondento vardą               |
| text         | position   | Įveskite respondento pareigas            |
| end_group    |            |                                          |
```

Pagrindiniai punktai:
- Eilutė `begin_group` reikalauja `name` ir `label`.
- Eilutei `end_group` nereikia pavadinimo ar etiketės.
- Klausimai tarp `begin_group` ir `end_group` yra grupės dalis.

## Grupės išvaizda

rtSurvey palaiko įvairias grupių išvaizdos parinktis:

1. **field-list**: Rodo kelis klausimus viename ekrane.
   ```
   | type         | name       | label       | appearance |
   |--------------|------------|-------------|------------|
   | begin_group  | respondent | Respondentas| field-list |
   | text         | name       | Vardas      |            |
   | text         | position   | Pareigos    |            |
   | end_group    |            |             |            |
   ```

2. **grid**: Sukuria kompaktišką, lentelei panašų grupių išdėstymą (specifinis rtSurvey).
   ```
   | type         | name       | label       | appearance |
   |--------------|------------|-------------|------------|
   | begin_group  | household  | Namų ūkis   | grid       |
   | text         | member_name| Vardas      |            |
   | integer      | member_age | Amžius      |            |
   | end_group    |            |             |            |
   ```

3. **collapsible**: Sukuria išskleidžiamas/sulankstomas grupes (specifinis rtSurvey).
   ```
   | type         | name       | label       | appearance  |
   |--------------|------------|-------------|-------------|
   | begin_group  | details    | Detalės     | collapsible |
   | text         | address    | Adresas     |             |
   | text         | phone      | Telefonas   |             |
   | end_group    |            |             |             |
   ```

## Įdėtos grupės

Grupės gali būti įdėtos kitose grupėse sudėtingesnėms struktūroms:

```
| type         | name       | label                                    |
|--------------|------------|------------------------------------------|
| begin_group  | hospital   | Ligoninės informacija                    |
| text         | hosp_name  | Koks šios ligoninės pavadinimas?         |
| begin_group  | medication | Vaistų prieinamumas                      |
| select_one y_n| hiv_meds  | Ar ši ligoninė turi ŽIV vaistų?          |
| end_group    |            |                                          |
| end_group    |            |                                          |
```

**Pastaba**: Visada pirmiausia užbaikite neseniai pradėtą grupę, kad išlaikytumėte tinkamą įdėjimą.

## Praleidimo logika grupėms

Naudokite stulpelį `relevant`, kad įgyvendintumėte praleidimo logiką visoms grupėms:

```
| type         | name   | label                                        | relevant        |
|--------------|--------|----------------------------------------------|-----------------|
| integer      | age    | Kiek jums metų?                              |                 |
| begin_group  | child  | Vaikas                                       | ${age} <= 5     |
| integer      | muac   | Įrašykite vaiko vidurio žasto apimtį         |                 |
| select_one y_n| mrdt  | Ar vaiko greito diagnostikos testas teigiamas?|                |
| end_group    |        |                                              |                 |
```

Šiame pavyzdyje grupė `child` rodoma tik tuo atveju, kai respondento amžius yra 5 metai ar jaunesnis.

## Geriausios praktikos grupių naudojimui

1. Naudokite prasmingus grupių pavadinimus duomenų analizei pagerinti.
2. Laikykite grupes susitelkusias ties susijusiais klausimais.
3. Naudokite įdėtas grupes apgalvotai, kad išvengtumėte pernelyg sudėtingų struktūrų.
4. Išsamiai testuokite praleidimo logiką naudodami `relevant` grupėse.
5. Apsvarstykite `field-list` išvaizdos naudojimą trumpoms grupėms, kad sumažintumėte slinkimą.
6. Naudokite rtSurvey tinklelio išdėstymą kompaktiškam susijusios informacijos atvaizdavimui.
7. Naudokite sulankstomas grupes ilgoms formoms, kad pagerintumėte naršymą.

## rtSurvey specifinės funkcijos

1. **Tinklelio išdėstymas**: Naudokite `grid` išvaizdą lentelei panašiems atvaizdavimams.
2. **Sulankstamos grupės**: Įgyvendinkite `collapsible` išvaizdą išskleidžiamoms sekcijoms.
3. **Pasirinktinis stilizavimas**: Taikykite pasirinktinį CSS grupėms unikaliam vizualiniam dizainui.
4. **Dinamiškas grupių elgesys**: Grupėse įgyvendinkite sudėtingą praleidimo logiką ir skaičiavimus.

## Daugiakalbis palaikymas

rtSurvey palaiko daugiakalbines grupes. Etiketėms naudokite konkrečios kalbos stulpelius:

```
| type         | name       | label::English | label::French |
|--------------|------------|----------------|---------------|
| begin_group  | personal   | Personal Info  | Infos Personnelles |
| text         | name       | Name           | Nom           |
| end_group    |            |                |               |
```

## Mobiliosios programos svarstymai

- Grupės su `field-list` išvaizda mobiliojoje programoje rodomos kaip vienas ekranas.
- Sulankstamos grupės gali pagerinti naršymą mažesniuose ekranuose.
- Tinklelio išdėstymai gali prisitaikyti, kad geriau matytųsi mobiliuosiuose įrenginiuose.

## Žinomos apribojimas

- Labai gilus grupių įdėjimas kai kuriuose įrenginiuose gali paveikti veikimą.
- Kai kurios pažangios stilizavimo parinktys mobiliojoje programoje gali būti neprieinamos grupėms.

## Grupių trikčių šalinimas

1. Įsitikinkite, kad kiekviena `begin_group` turi atitinkamą `end_group`.
2. Patikrinkite, kad grupių pavadinimai yra unikalūs formoje.
3. Patikrinkite, ar praleidimo logika nurodo teisingus klausimų pavadinimus.
4. Išsamiai testuokite grupes tiek žiniatinklio, tiek mobiliosios sąsajose.

Efektyviai naudodami grupes XLSFormose su rtSurvey, galite sukurti gerai organizuotas, efektyvias apklausas, gerinančias tiek duomenų rinkimo patirtį, tiek duomenų analizės kokybę.
