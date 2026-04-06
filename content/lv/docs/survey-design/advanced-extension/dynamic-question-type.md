---
title: "Dinamiskais jautājuma tips"
description: "Dinamiskais jautājuma tips ļauj lauka jautājuma tipam un logrīkam tikt noteiktam izpildlaikā, pamatojoties uz API atbildi vai aprēķinātu vērtību."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 301
---

Funkcija **Dinamiskais jautājuma tips** ļauj lauka ievades logrīkam un validācijas uzvedībai tikt noteiktam **izpildlaikā**, nevis formas projektēšanas laikā. Šis ir uzlabots rtSurvey paplašinājums, ko izmanto, kad savāktā datu tipa veids ir atkarīgs no servera puses konfigurācijas, API atbildes vai iepriekšējā lauka vērtības.

Izplatīts gadījums ir konfigurējama pārbaudes kontrolsaraksts, kur serveris nosaka, kuri lauki ir obligāti, kāda veida tie ir (text, integer, select u.c.) un kādas iespējas ir pieejamas — nepārbūvējot formu katrai konfigurācijai.

---

## Kā tas darbojas

Lauks, kas atzīmēts kā dinamiskais jautājuma tips, izmanto `callapi()`, lai iegūtu konfigurāciju no API. API atbilde nosaka:

- Renderējamo ievades tipu (text, integer, select_one u.c.)
- Pieejamās izvēles (atlases tipiem)
- Validācijas noteikumus

Lauks iekšēji tiek atzīmēts ar `specialFeature: isDynamicQuestionType`, kas norāda formas dzinējam izmantot API atbildi logrīka konstruēšanai, nevis statisko formas definīciju.

---

## Labākā prakse

1. Nodrošiniet, ka API atgriež konsekventu shēmu visiem lauku tipiem.
2. Pārbaudiet visus iespējamos dinamiskos tipus pirms izvietošanas.
3. Nodrošiniet bezsaistes rezerves gadījumam, ja API ir nepieejams.
4. Dokumentējiet API atbildes formātu komandas locekļiem.
