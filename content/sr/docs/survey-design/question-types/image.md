---
title: "Image"
description: "Pitanja tipa image dozvoljavaju ispitanicima da snime i pošalju fotografije kao deo ankete."
icon: "image"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 227
---

Tip pitanja image u XLSForm-ovima i rtSurvey-u omogućava ispitanicima da snime i pošalju fotografije kao deo svojih odgovora na anketu. Ova funkcija je posebno korisna za prikupljanje vizuelnih podataka, dokumentovanje posmatranja ili pružanje dokaza u terenskim istraživanjima.

## Osnovna XLSForm specifikacija

| type  | name        | label                           |
|-------|-------------|--------------------------------|
| image | photo       | Fotografišite lokaciju          |

Za više detalja o osnovnom tipu pitanja image, pogledajte [XLSForm specifikaciju](https://xlsform.org/en/#question-types).

## Upotrebe

Pitanja tipa image se uobičajeno koriste za:

1. Dokumentovanje terenskih uslova ili posmatranja
2. Hvatanje vizuelnih dokaza u istraživačkim studijama
3. Prikupljanje fotografija pre i posle u procenama uticaja
4. Verifikaciju završetka zadataka ili prisustva na lokacijama
5. Prikupljanje vizuelnih podataka za daljinsku analizu

## Najbolje prakse

1. Pružite jasna uputstva o tome šta treba fotografisati.
2. Razmotrite implikacije privatnosti i informišite ispitanike o tome kako će se njihove fotografije koristiti.
3. Budite svesni veličina datoteka i ograničenja skladišta, posebno za ankete u područjima sa ograničenom internet vezom.
4. Osigurajte da uređaj ima dovoljno prostora za skladištenje i da su odobrene dozvole kamere.

## Primer upotrebe

Evo primera kako biste mogli koristiti pitanje tipa image u anketi:

| type  | name           | label                                      | hint                                        |
|-------|----------------|--------------------------------------------|--------------------------------------------|
| image | storefront     | Fotografišite ulaz u prodavnicu            | Osigurajte da je naziv prodavnice jasno vidljiv |

## rtSurvey proširenja

Dok je osnovna XLSForm specifikacija za pitanja tipa image jednostavna, rtSurvey može ponuditi dodatne funkcije ili prilagođavanja:

1. Podešavanja kvaliteta slike (npr. niska, srednja, visoka rezolucija)
2. Opcija dodavanja natpisa ili oznaka slikama
3. Snimanje više slika za jedno pitanje
4. Integracija sa nativnom aplikacijom kamere ili galerijom uređaja

## Rukovanje podacima

Slike prikupljene putem ovog tipa pitanja se obično:

1. Čuvaju u uobičajenom formatu slike (npr. JPG, PNG)
2. Skladište zajedno sa ostalim podacima ankete, često u zasebnoj medijskoj fascikli
3. Dostupne su za pregled i analizu putem platforme za upravljanje anketom

## Razmatranja za analizu

Kada koristite pitanja tipa image, razmotrite:

1. Kako će slike biti analizirane (npr. ručni pregled, automatska analiza slike)
2. Dodatni prostor za skladištenje koji zahtevaju datoteke slika
3. Mere privatnosti i zaštite podataka za čuvanje i rukovanje fotografijama
4. Potencijalnu potrebu za alatima za uređivanje ili organizaciju slika u fazi analize

## Ograničenja

- Datoteke slika mogu biti velike, što može uticati na prenos i skladištenje podataka.
- Ne moraju svi uređaji imati kamere visokog kvaliteta ili dovoljno prostora za skladištenje.
- Analiza velikog broja slika može biti vremenski zahtevna.
- Mogu postojati problemi sa privatnošću prilikom snimanja slika, posebno u javnim prostorima.

## rtSurvey proširenja za slike

### watermark()

Izgled `watermark()` prekriva tekstualni vodeni žig na fotografijama snimljenim ovim poljem. Vodeni žig obično sadrži metapodatke kao što su ime anketara, datum/vreme ili GPS koordinate, utisnute direktno na sliku pre čuvanja.

| type | name | label | appearance |
|------|------|-------|------------|
| image | site_photo | Fotografišite lokaciju | `watermark("${enumerator_id} ${today()}")` |

Argument za `watermark()` je XPath izraz koji se procenjuje u trenutku snimanja. Rezultujući niz se prikazuje kao tekst vodenog žiga.

### editable

Izgled `editable` dozvoljava ispitaniku da anotira ili crta na snimljenu fotografiju nakon snimanja. Traka sa alatkama za crtanje pojavljuje se iznad slike.

| type | name | label | appearance |
|------|------|-------|------------|
| image | annotated_photo | Fotografišite i označite oblasti od interesa | editable |

{{% alert icon=" " context="info" %}}
`editable` se može kombinovati sa `watermark()`: `appearance: editable watermark("${id}")`
{{% /alert %}}
