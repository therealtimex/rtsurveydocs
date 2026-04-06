---
title: "Opakujúce sa otázky"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 260
---

Opakovania sú výkonnou funkciou v rtSurvey, ktorá vám umožňuje zbierať rovnakú sadu informácií viackrát v rámci jedného prieskumu. Je to obzvlášť užitočné pre scenáre ako prieskumy domácností, kde možno budete musieť zbierať dáta o viacerých členoch domácnosti.

## Základná štruktúra opakovania

Na vytvorenie opakovania v rtSurvey použite konštrukciu `begin repeat` a `end repeat`:

```
| type         | name         | label                |
|--------------|--------------|----------------------|
| begin repeat | child_repeat |                      |
| text         | name         | Meno dieťaťa         |
| decimal      | birthweight  | Pôrodná hmotnosť dieťaťa  |
| select_one male_female | sex | Pohlavie dieťaťa         |
| end repeat   |              |                      |
```

V tomto príklade môže používateľ zbierať informácie o viacerých deťoch pridávaním nových opakovaní vo formulári.

## Označovanie opakovaní

Hoci stĺpec `label` je pre `begin repeat` voliteľný, pridanie popisku môže zlepšiť navigáciu:

```
| type         | name         | label                |
|--------------|--------------|----------------------|
| begin repeat | child_repeat | Informácie o dieťati    |
| text         | name         | Meno dieťaťa         |
| decimal      | birthweight  | Pôrodná hmotnosť dieťaťa  |
| select_one male_female | sex | Pohlavie dieťaťa         |
| end repeat   |              |                      |
```

rtSurvey zobrazí „Informácie o dieťati" ako názov pre každú inštanciu opakovania.

## Pevný počet opakovaní

Na zadanie pevného počtu opakovaní použite stĺpec `repeat_count`:

```
| type         | name         | label                | repeat_count |
|--------------|--------------|----------------------|--------------|
| begin repeat | child_repeat | Informácie o dieťati    | 3            |
| text         | name         | Meno dieťaťa         |              |
| decimal      | birthweight  | Pôrodná hmotnosť dieťaťa  |              |
| end repeat   |              |                      |              |
```

Toto vytvorí presne 3 opakovania dieťaťa.

## Dynamický počet opakovaní

rtSurvey podporuje dynamický počet opakovaní na základe predchádzajúcich odpovedí:

```
| type     | name           | label                          | repeat_count       |
|----------|----------------|--------------------------------|--------------------|
| integer  | num_hh_members | Počet členov domácnosti?   |                    |
| begin repeat | hh_member  | Člen domácnosti               | ${num_hh_members}  |
| text     | name           | Meno                           |                    |
| integer  | age            | Vek                            |                    |
| end repeat |              |                                |                    |
```

## Podmienené opakovania

Môžete použiť stĺpec `relevant` na podmienené zobrazovanie opakovaní:

```
| type              | name        | label                     | relevant           |
|-------------------|-------------|---------------------------|---------------------|
| select_one yes_no | has_child   | Žijú tu nejaké deti?|                     |
| begin repeat      | child_repeat| Informácie o dieťati         | ${has_child} = 'yes'|
| text              | name        | Meno dieťaťa              |                     |
| decimal           | birthweight | Pôrodná hmotnosť dieťaťa       |                     |
| end repeat        |             |                           |                     |
```

## Funkcie špecifické pre rtSurvey

### Súhrn opakovania

rtSurvey poskytuje súhrnný pohľad na opakovania. Na prispôsobenie súhrnu použite skupinu vo vnútri opakovania:

```
| type         | name         | label                                    |
|--------------|--------------|------------------------------------------|
| begin repeat | person_repeat|                                          |
| begin group  | person       | ${first_name} ${last_name} - ${age}      |
| text         | first_name   | Krstné meno                               |
| text         | last_name    | Priezvisko                                |
| integer      | age          | Vek                                      |
| end group    |              |                                          |
| end repeat   |              |                                          |
```

### Možnosti vzhľadu opakovania

rtSurvey ponúka ďalšie možnosti vzhľadu pre opakovania:

- `appearance: field-list` - Zobrazí všetky otázky v opakovaní na jednej obrazovke
- `appearance: table-list` - Prezentuje opakovania v tabuľkovom formáte

```
| type         | name         | label            | appearance  |
|--------------|--------------|-------------------|-------------|
| begin repeat | child_repeat | Informácie o dieťati | table-list  |
| text         | name         | Meno              |             |
| integer      | age          | Vek               |             |
| end repeat   |              |                   |             |
```

### Vnorené opakovania

rtSurvey podporuje vnorené opakovania pre komplexné dátové štruktúry:

```
| type         | name           | label                |
|--------------|----------------|----------------------|
| begin repeat | household      | Domácnosť            |
| text         | hh_name        | Názov domácnosti       |
| begin repeat | hh_member      | Člen domácnosti     |
| text         | member_name    | Meno člena          |
| integer      | member_age     | Vek člena           |
| end repeat   |                |                      |
| end repeat   |                |                      |
```

## Najlepšie postupy pre používanie opakovaní v rtSurvey

1. Používajte zmysluplné názvy a popisky pre opakovania na zlepšenie analýzy dát.
2. Zvážte používanie dynamického počtu opakovaní na zníženie chýb pri zadávaní dát.
3. Dôkladne testujte váš formulár, najmä pri použití komplexných vnorených opakovaní.
4. Používajte funkciu súhrnu na pomoc anketárom orientovať sa v dlhých zoznamoch opakovaní.
5. Buďte opatrní pri veľkom počte opakovaní, pretože môžu ovplyvniť výkon formulára.

## Spracovanie nulového počtu opakovaní

Na zobrazenie nulového počtu opakovaní v rtSurvey:

1. Naučte anketárov vymazať prvé opakovanie, ak nie je potrebné.
2. Používajte dynamický počet opakovaní, keď je presný počet známy.
3. Používajte `relevant` na podmienené zobrazovanie opakovaní.

## Úvahy pri exporte dát

Pri exporte dát z rtSurvey sú dáta opakovania typicky sploštené. Každá inštancia opakovania sa stáva samostatným riadkom v exportovaných dátach, pričom dáta nadradeného formulára sú opakované pre každú inštanciu.

## Úvahy pre mobilnú aplikáciu

- Opakovania v mobilnej aplikácii rtSurvey podporujú offline zber dát.
- Veľký počet opakovaní môže ovplyvniť výkon aplikácie na zariadeniach nižšej triedy.

Efektívnym používaním opakovaní v rtSurvey môžete vytvárať flexibilné a výkonné prieskumy schopné zachytávať komplexné, hierarchické dátové štruktúry pri súčasnom zachovaní používateľsky prívetivého rozhrania pre anketárov.
