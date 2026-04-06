---
title: "Select_multiple"
description: "Select_multiple jautājumi ļauj respondentiem izvēlēties vienu vai vairākas iespējas no iepriekš definēta saraksta."
icon: "check_box"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 225
---

Jautājuma tips `select_multiple` parāda sarakstu, kur respondents var izvēlēties **vienu vai vairākas iespējas**. Pēc noklusējuma izvēles tiek renderētas kā izvēles rūtiņas. Saglabātā vērtība ir **atstarpes atdalīts saraksts** ar visām izvēlētajām izvēles vērtībām.

## Pamata XLSForm specifikācija

| type | name | label |
|------|------|-------|
| select_multiple languages | spoken_languages | Kādas valodas jūs runājat? |

Choices darblapā:

| list_name | name | label |
|-----------|------|-------|
| languages | latvian | Latviešu |
| languages | english | Angļu |
| languages | russian | Krievu |
| languages | other | Cita |

## Izteiksmes ar select_multiple

Lai pārbaudītu, vai konkrēta izvēle ir atlasīta, izmantojiet `selected()` funkciju:

```
selected(${spoken_languages}, 'english')
```

Lai skaitītu atlasītās izvēles:

```
count-selected(${spoken_languages})
```

## Labākā prakse

1. Izmantojiet `select_multiple` tikai tad, kad ir nepieciešamas vairākas atbildes — tas sarežģī analīzi.
2. Apsveriet izvēļu skaita ierobežošanu ar `constraint`: `count-selected(.) <= 3`.
3. Iekļaujiet opciju "Nav" vai "Neviena", lai ļautu respondentiem izlaist jautājumu.
