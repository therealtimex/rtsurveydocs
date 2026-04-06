---
title: "Jautājumu atkārtošana"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 260
---

Atkārtojumi ir spēcīga rtSurvey funkcija, kas ļauj vākt vienu un to pašu informāciju vairākas reizes vienas aptaujas ietvaros. Tas ir īpaši noderīgi scenārijiem, piemēram, mājsaimniecību aptaujās, kur var būt nepieciešams vākt datus par vairākiem mājsaimniecības locekļiem.

## Pamata atkārtojuma struktūra

Lai izveidotu atkārtojumu rtSurvey, izmantojiet konstrukciju `begin repeat` un `end repeat`:

```
| type         | name         | label                |
|--------------|--------------|----------------------|
| begin repeat | child_repeat |                      |
| text         | name         | Bērna vārds          |
| decimal      | birthweight  | Bērna dzimšanas svars |
| select_one male_female | sex | Bērna dzimums       |
| end repeat   |              |                      |
```

Šajā piemērā lietotājs var vākt informāciju par vairākiem bērniem, pievienojot jaunus atkārtojumus formā.

## Atkārtojumu apzīmēšana

Lai gan `label` kolonna `begin repeat` gadījumā nav obligāta, etiķetes pievienošana var uzlabot navigāciju:

```
| type         | name         | label                |
|--------------|--------------|----------------------|
| begin repeat | child_repeat | Bērna informācija    |
| text         | name         | Bērna vārds          |
| decimal      | birthweight  | Bērna dzimšanas svars |
| select_one male_female | sex | Bērna dzimums       |
| end repeat   |              |                      |
```

rtSurvey katrai atkārtojuma instancei rādīs "Bērna informācija" kā nosaukumu.

## Fiksēti atkārtojumu skaiti

Lai norādītu fiksētu atkārtojumu skaitu, izmantojiet kolonnu `repeat_count`:

```
| type         | name         | label                | repeat_count |
|--------------|--------------|----------------------|--------------|
| begin repeat | child_repeat | Bērna informācija    | 3            |
| text         | name         | Bērna vārds          |              |
| decimal      | birthweight  | Bērna dzimšanas svars |             |
| end repeat   |              |                      |              |
```

Tas izveidos tieši 3 bērnu atkārtojumus.

## Dinamiskie atkārtojumu skaiti

rtSurvey atbalsta dinamiskos atkārtojumu skaititus, pamatojoties uz iepriekšējām atbildēm:

```
| type     | name           | label                          | repeat_count       |
|----------|----------------|--------------------------------|--------------------|
| integer  | num_hh_members | Mājsaimniecības locekļu skaits? |                   |
| begin repeat | hh_member  | Mājsaimniecības loceklis       | ${num_hh_members}  |
| text     | name           | Vārds                          |                    |
| integer  | age            | Vecums                         |                    |
| end repeat |              |                                |                    |
```

## Nosacījuma atkārtojumi

Varat izmantot kolonnu `relevant`, lai nosacījuma kārtā rādītu atkārtojumus:

```
| type              | name        | label                     | relevant           |
|-------------------|-------------|---------------------------|---------------------|
| select_one yes_no | has_child   | Vai šeit dzīvo bērni?     |                     |
| begin repeat      | child_repeat| Bērna informācija         | ${has_child} = 'yes'|
| text              | name        | Bērna vārds               |                     |
| decimal           | birthweight | Bērna dzimšanas svars     |                     |
| end repeat        |             |                           |                     |
```

## rtSurvey specifiskās funkcijas

### Atkārtojumu kopsavilkums

rtSurvey nodrošina atkārtojumu kopsavilkuma skatu. Lai pielāgotu kopsavilkumu, izmantojiet grupu atkārtojuma iekšā:

```
| type         | name         | label                                    |
|--------------|--------------|------------------------------------------|
| begin repeat | person_repeat|                                          |
| begin group  | person       | ${first_name} ${last_name} - ${age}      |
| text         | first_name   | Vārds                                    |
| text         | last_name    | Uzvārds                                  |
| integer      | age          | Vecums                                   |
| end group    |              |                                          |
| end repeat   |              |                                          |
```

### Atkārtojumu izskata opcijas

rtSurvey piedāvā papildu izskata opcijas atkārtojumiem:

- `appearance: field-list` — rāda visus atkārtojuma jautājumus vienā ekrānā
- `appearance: table-list` — piedāvā atkārtojumus tabulas formātā

```
| type         | name         | label            | appearance  |
|--------------|--------------|-------------------|-------------|
| begin repeat | child_repeat | Bērna informācija | table-list  |
| text         | name         | Vārds             |             |
| integer      | age          | Vecums            |             |
| end repeat   |              |                   |             |
```

### Ligzdotie atkārtojumi

rtSurvey atbalsta ligzdotus atkārtojumus sarežģītām datu struktūrām:

```
| type         | name           | label                |
|--------------|----------------|----------------------|
| begin repeat | household      | Mājsaimniecība       |
| text         | hh_name        | Mājsaimniecības nosaukums |
| begin repeat | hh_member      | Mājsaimniecības loceklis |
| text         | member_name    | Locekļa vārds        |
| integer      | member_age     | Locekļa vecums       |
| end repeat   |                |                      |
| end repeat   |                |                      |
```

## Labākā prakse atkārtojumu izmantošanai rtSurvey

1. Izmantojiet jēgpilnus nosaukumus un etiķetes atkārtojumiem, lai uzlabotu datu analīzi.
2. Apsveriet dinamisku atkārtojumu skaitu izmantošanu, lai samazinātu datu ievades kļūdas.
3. Rūpīgi testējiet formu, īpaši izmantojot sarežģītus ligzdotus atkārtojumus.
4. Izmantojiet kopsavilkuma funkciju, lai palīdzētu enumeratoriem navigēt garus atkārtojumu sarakstus.
5. Esiet piesardzīgi ar lielu atkārtojumu skaitu, jo tas var ietekmēt formas veiktspēju.

## Nulles atkārtojumu apstrāde

Lai apzīmētu nulles atkārtojumus rtSurvey:

1. Apmāciet enumeratorus dzēst pirmo atkārtojumu, ja tas nav nepieciešams.
2. Izmantojiet dinamiskus atkārtojumu skaititus, kad precīzais skaits ir zināms.
3. Izmantojiet `relevant`, lai nosacījuma kārtā rādītu atkārtojumus.

## Datu eksporta apsvērumi

Eksportējot datus no rtSurvey, atkārtojumu dati parasti tiek saplakanāti. Katra atkārtojuma instance kļūst par atsevišķu rindu eksportētajos datos, ar mātes formas datiem, kas atkārtoti katrai instancei.

## Mobilās lietotnes apsvērumi

- Atkārtojumi rtSurvey mobilajā lietotnē atbalsta bezsaistes datu vākšanu.
- Liels atkārtojumu skaits var ietekmēt lietotnes veiktspēju zemākas klases ierīcēs.

Efektīvi izmantojot atkārtojumus rtSurvey, varat izveidot elastīgas un spēcīgas aptaujas, kas spēj tvert sarežģītas, hierarhiskas datu struktūras, saglabājot enumeratoriem draudzīgu saskarni.
