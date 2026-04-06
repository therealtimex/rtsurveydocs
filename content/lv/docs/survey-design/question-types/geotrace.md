---
title: "Ģeoceļš"
description: "Ģeoceļa jautājumi ļauj respondentiem uztvert savienotu punktu virkni kartē, veidojot līnijas vai ceļus aptaujas ietvaros."
icon: "timeline"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 234
---

Jautājuma tips geotrace XLSForms un rtSurvey ļauj respondentiem uztvert savienotu GPS punktu virkni kartē, veidojot līnijas vai ceļus. Šī funkcija ir īpaši noderīga maršrutu, robežu vai lineāru elementu kartēšanai telpiskajās aptaujās.

## Pamata XLSForm specifikācija

| type | name | label |
|------|------|-------|
| geotrace | road_trace | Izsekojiet ceļu vai robežu |
| geotrace | river_path | Kartējiet upes tecējumu |

## Datu formāts

Geotrace vērtība tiek glabāta kā GPS punktu saraksts, atdalīts ar semikolu:

`56.9460 24.1059 0 0; 56.9480 24.1080 0 0; 56.9500 24.1100 0 0`

## Attāluma aprēķins

Aprēķiniet ceļa kopējo garumu metros:

```
distance(${road_trace})
```

Konvertējiet uz kilometriem:

```
round(distance(${road_trace}) div 1000, 3)
```

## Labākā prakse

1. Iestatiet pietiekamu GPS precizitāti pirms sākšanas.
2. Pārbaudiet, vai ir pietiekami daudz GPS punktu, lai precīzi attēlotu ceļu.
3. Apsveriet, vai geoshape (slēgts daudzstūris) var būt piemērotāks jūsu gadījumam.
