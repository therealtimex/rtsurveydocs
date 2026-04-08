---
title: "Typy otázok"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 220
---

rtSurvey podporuje všetky štandardné typy otázok XLSForm plus niekoľko rozšírení. Každý typ otázky kontroluje, aký druh dát sa zbiera a ako sa vstupný widget vykreslí na zariadení.

Na nastavenie typu otázky zadajte názov typu do stĺpca `type` hárku **survey** vo vašom XLSForm.

## Textový vstup

| Typ | Popis |
|------|-------------|
| [text](text) | Voľná textová odpoveď — povolené akékoľvek znaky |
| [integer](integer) | Celé číslo (bez desatinných miest) |
| [decimal](decimal) | Číslo s desatinnými miestami |
| [range](range) | Číslo vybrané posuvníkom v rámci definovaného rozsahu min/max |

## Výber

| Typ | Popis |
|------|-------------|
| [select_one listname](select-one) | Výber práve jednej možnosti zo zoznamu |
| [select_multiple listname](select-multiple) | Výber jednej alebo viacerých možností zo zoznamu |
| [rank listname](rank) | Zoradenie možností podľa preferencie alebo priority |

## Dátum a čas

| Typ | Popis |
|------|-------------|
| [date](date) | Kalendárny dátum (rok, mesiac, deň) |
| [time](time) | Čas dňa (hodiny, minúty) |
| [datetime](datetime-date-time) | Kombinovaný dátum a čas |

## Poloha

| Typ | Popis |
|------|-------------|
| [geopoint](geopoint) | Jedna GPS súradnica (zemepisná šírka, zemepisná dĺžka, nadmorská výška, presnosť) |
| [geotrace](geotrace) | Trasa — séria GPS bodov tvoriacich čiaru |
| [geoshape](geoshape) | Oblasť — uzavretý polygón GPS bodov |

## Médiá

| Typ | Popis |
|------|-------------|
| [image](image) | Zachytenie fotografie alebo nahratie obrázka |
| [audio](audio) | Zvuková nahrávka |
| [video](video) | Video nahrávka |
| [file](file) | Všeobecné nahratie súboru (PDF, dokument atď.) |

## Ostatné

| Typ | Popis |
|------|-------------|
| [barcode](barcode) | Skenovanie čiarového kódu alebo QR kódu |
| [note](note) | Text iba na čítanie — zobrazuje pokyny alebo vypočítané súhrny |
| [calculate](calculate) | Skryté pole, ktoré ukladá vypočítanú hodnotu |
| [hidden](hidden) | Skryté pole, ktoré ukladá statickú alebo vopred vyplnenú hodnotu |
| [trigger / acknowledge](trigger) | Zaškrtávacie políčko, ktoré musí anketár označiť na potvrdenie, že prečítal vyhlásenie |
| [meta](meta) | Automatické metadáta: časové pečiatky, ID zariadenia, informácie o anketárovi |

## Rozšírenia rtSurvey

Tieto typy sú špecifické pre rtSurvey a nie sú súčasťou štandardnej špecifikácie XLSForm.

| Typ | Popis |
|-----|-------|
| [search-autocomplete](search-autocomplete) | Textový vstup s návrhmi automatického dopĺňania na základe API v reálnom čase |
| [mentions](mentions) | Textové pole s automatickým dopĺňaním `@`-spomienok na označovanie entít inline |
| [texttags](texttags) | Pole na zadávanie tagov — každý záznam sa stane odstrániteľným chipom; uložené ako reťazec oddelený medzerami |

Pre skupiny opakovania pozri [Repeats](../advanced-extension/repeats)

## Ako type a appearance spolupracujú

`type` určuje **aké dáta sa zbierajú**. Stĺpec `appearance` kontroluje **ako widget vyzerá**. Mnohé typy podporujú viacero vzhľadov — napríklad `select_one` môže byť zobrazený ako prepínače, rozbaľovací zoznam, Likertova škála alebo kompaktná mriežka.

Pozrite si [Vzhľad](../appearance) pre úplný zoznam možností.
