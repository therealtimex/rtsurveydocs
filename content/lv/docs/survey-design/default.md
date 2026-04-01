---
title: "Noklusējums"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 287
---

Noklusējuma vērtības rtSurvey ļauj iepriekš aizpildīt jautājumus ar atbildēm, kad respondents pirmo reizi saskaras ar tiem. Šī funkcija var ievērojami uzlabot aptaujas efektivitāti un datu kvalitāti, nodrošinot sākotnējās vērtības, kas ir vai nu bieži atlasītas, vai kalpo kā paredzamās ievades piemēri.

## Pamata lietojums

Lai iestatītu noklusējuma vērtību, izmantojiet XLSForm kolonnu `default`:

```
| type    | name        | label                         | default    |
|---------|-------------|-------------------------------|------------|
| date    | survey_date | Aptaujas datums               | 2024-07-04 |
| decimal | weight      | Respondenta svars? (kg)       | 51.3       |
```

Šajā piemērā aptaujas datums tiks sākotnēji aizpildīts ar 2024. gada 4. jūliju, un svara lauks sāksies ar 51.3 kg.

## Dinamiskie noklusējumi

rtSurvey atbalsta dinamiskās noklusējuma vērtības, izmantojot funkcijas:

```
| type | name | label                              | default  |
|------|------|------------------------------------| ---------|
| date | d    | Ievadiet datumu, kad notika notikums? | today()  |
```

Šeit funkcija `today()` automātiski iestata noklusējumu uz pašreizējo datumu.

## rtSurvey specifiskās funkcijas

### Kontekstjutīgi noklusējumi

rtSurvey paplašina noklusējuma funkcionalitāti ar kontekstjutīgiem noklusējumiem:

```
| type    | name     | label           | default            |
|---------|----------|-----------------|---------------------|
| text    | location | Pašreizējā atrašanās vieta | ${current_location} |
```

Tas izmanto rtSurvey mainīgo `${current_location}`, lai iepriekš aizpildītu atrašanās vietu, pamatojoties uz ierīces GPS.

### Kaskādes noklusējumi

rtSurvey ļauj noklusējumus, pamatojoties uz iepriekšējām atbildēm:

```
| type    | name     | label           | default         |
|---------|----------|-----------------|-----------------|
| text    | city     | Pilsēta         |                 |
| text    | district | Rajons          | ${city}-district|
```

Šeit rajona lauks tiek iepriekš aizpildīts, pamatojoties uz ievadīto pilsētu.

### Noklusējums atkārtojumos

Jautājumiem atkārtojumu grupas iekšā noklusējums tiek aprēķināts, kad atkārtojums tiek pievienots:

```
| type         | name      | label        | default                |
|--------------|-----------|--------------|------------------------|
| begin repeat | visits    | Klīnikas apmeklējumi |                  |
| date         | visit_date| Apmeklējuma datums | ${previous_visit_date} |
| end repeat   |           |              |                        |
```

Tas iestata noklusējuma apmeklējuma datumu uz iepriekšējā apmeklējuma datumu.

## Labākā prakse noklusējumu izmantošanā

1. **Izmantojiet taupīgi**: Izmantojiet noklusējumus tikai tur, kur tie ievērojami uzlabo efektivitāti vai datu kvalitāti.
2. **Nodrošiniet precizitāti**: Regulāri pārskatiet un atjauniniet statiskās noklusējuma vērtības.
3. **Rūpīgi testējiet**: Īpaši izmantojot dinamiskus vai aprēķinātus noklusējumus.
4. **Ņemiet vērā lietotāja pieredzi**: Nodrošiniet, ka noklusējumi nemaldina respondentus vai neievieto novirzes.
5. **Skaidri dokumentējiet**: Nodrošiniet, ka visi komandas locekļi saprot noklusējuma vērtību pamatojumu.

## Uzlabotas noklusējumu tehnikas

### Randomizēti noklusējumi

rtSurvey atbalsta randomizētus noklusējumus noteiktiem jautājumu tipiem:

```
| type              | name    | label        | default           |
|-------------------|---------|--------------|-------------------|
| select_one options| choice  | Atlasiet vienu: | random(options) |
```

Tas nejauši atlasa noklusējuma opciju no 'options' saraksta.

### Nosacījuma noklusējumi

Izmantojiet relevanci, lai iestatītu nosacījuma noklusējumus:

```
| type    | name     | label    | default | relevant        |
|---------|----------|----------|---------|-----------------|
| text    | other    | Precizējiet | N/A  | ${q1} = 'other' |
```

Šeit 'N/A' ir noklusējums tikai tad, kad iepriekšējā jautājumā ir atlasīts 'other'.

## Datu pārvaldības apsvērumi

- Noklusējuma vērtības ir iekļautas datu eksportā, parasti ar karodziņu, kas norāda, ka tās bija noklusējuma vērtības.
- rtSurvey audita izsekošanas funkcija izseko, kad respondenti maina noklusējuma vērtības.

## Mobilās lietotnes uzvedība

- rtSurvey mobilā lietotne atbalsta visas noklusējuma funkcionalitātes, ieskaitot dinamiskos un kontekstjutīgos noklusējumus.
- Bezsaistes režīms var ietekmēt dažus dinamiskos noklusējumus, kas paļaujas uz reāllaika datiem.

## Zināmie ierobežojumi

- Sarežģīti aprēķinātie noklusējumi var ietekmēt formas ielādes laiku, īpaši zemākas klases ierīcēs.
- Daži dinamiskie noklusējumi var nedarboties kā paredzēts priekšskatījuma režīmā.

## Noklusējuma vērtību problēmu novēršana

1. **Noklusējums neparādās**: Pārbaudiet sintakses kļūdas noklusējuma izteiksmē.
2. **Neparedzētas vērtības**: Pārbaudiet aprēķinu loģiku un testējiet ar dažādiem scenārijiem.
3. **Veiktspējas problēmas**: Optimizējiet sarežģītus noklusējuma aprēķinus vai apsveriet alternatīvas pieejas.
