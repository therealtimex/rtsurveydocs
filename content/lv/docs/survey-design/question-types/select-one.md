---
title: "Select_one"
description: "Select_one jautājumi ļauj respondentiem izvēlēties tieši vienu iespēju no iepriekš definēta izvēļu saraksta."
icon: "radio_button_checked"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 224
---

Jautājuma tips `select_one` aicina respondentu izvēlēties **tieši vienu iespēju** no iepriekš definēta saraksta. Pēc noklusējuma izvēles tiek renderētas kā radio pogas, bet ir pieejams plašs izskata iespēju klāsts, lai mainītu izkārtojumu un uzvedību.

## Pamata XLSForm specifikācija

| type | name | label |
|------|------|-------|
| select_one gender | gender | Kāds ir respondenta dzimums? |
| select_one yes_no | satisfied | Vai esat apmierināts ar pakalpojumu? |

Choices darblapā:

| list_name | name | label |
|-----------|------|-------|
| gender | male | Vīrietis |
| gender | female | Sieviete |
| gender | other | Cits |
| yes_no | yes | Jā |
| yes_no | no | Nē |

## Biežākās izskata iespējas

| Izskats | Apraksts |
|---------|----------|
| *(nav)* | Radio pogas (noklusējums) |
| `minimal` | Nolaižamais saraksts |
| `likert` | Likerta skala |
| `horizontal` | Horizontālas radio pogas |
| `quick` | Automātiski pāriet uz nākamo jautājumu pēc atlases (tikai mobilais) |

## Labākā prakse

1. Saglabājiet izvēles sarakstus fokusētus un relevantas — pārāk daudz iespēju apgrūtina respondentus.
2. Apsveriet "Cits (lūdzu, precizējiet)" ar sekojošu teksta jautājumu.
3. Izmantojiet `minimal` izskata lielajiem sarakstiem, lai taupītu ekrāna vietu.
