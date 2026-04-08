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

{{< table >}}
| Izskats | Apraksts |
|---------|----------|
| *(nav)* | Radio pogas (noklusējums) |
| `minimal` | Nolaižamais saraksts |
| `likert` | Likerta skala |
| `horizontal` | Horizontālas radio pogas |
| `quick` | Automātiski pāriet uz nākamo jautājumu pēc atlases (tikai mobilais) |
| `tagging` | Parāda izvēles kā noklikšķināmus pill formas tagu čipsus |
| `boxtag` | Parāda izvēles kā stilizētus taisnstūrveida lodziņus, kurus lietotājs pieskaras |
| `boxtag -search` | Boxtag izkārtojums ar dzīvas meklēšanas/filtrēšanas ievadi virs lodziņiem |
| `duolingo-style1` | Duolingo iedvesmots karšu izkārtojums — lielas pieskaramās kartes ar ikonām |
| `rating_box` | Tīklveida vērtēšanas lodziņi — vislabākais skaitliskiem vai skalas jautājumiem |
| `star_rating` | Zvaigžņu vērtēšanas logrīks — izvēles tiek renderētas kā 1–N zvaigznes |
| `choices-noshow` | Sākotnēji rāda tikai pirmās 10 izvēles; pārējās atklāj pēc pieprasījuma |
| `noshow` | Pilnīgi slēpj izvēļu sarakstu; vērtību iestata programmatiski |
| `checkall` | Pievieno opciju "Atlasīt visas" saraksta augšdaļā |
| `max-items(N)` | Ierobežo redzamo izvēļu skaitu līdz N (piemēram, `max-items(5)`) |
{{< /table >}}

## Labākā prakse

1. Saglabājiet izvēles sarakstus fokusētus un relevantas — pārāk daudz iespēju apgrūtina respondentus.
2. Apsveriet "Cits (lūdzu, precizējiet)" ar sekojošu teksta jautājumu.
3. Izmantojiet `minimal` izskata lielajiem sarakstiem, lai taupītu ekrāna vietu.
