---
title: "Vetëm-lexueshëm"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 287
---

Fushat vetëm-lexueshëm në rtSurvey ju lejojnë të shfaqni informacione që nuk mund të edituhen nga i anketuari. Kjo veçori është veçanërisht e dobishme për shfaqjen e të dhënave të parapopulluara, rezultateve të llogaritura, ose informacioneve që duhet të mbetet konstante gjatë gjithë sondazhit.

## Përdorimi Bazë

Për ta bërë një fushë vetëm-lexueshëm, përdorni kolonën `read_only` në XLSForm tuaj:

```
| type    | name | label                 | read_only | default |
|---------|------|----------------------|-----------|---------|
| integer | num  | Numri i pacientit është: | yes  | 5       |
```

Në këtë shembull, numri i pacientit caktohet në 5 dhe nuk mund të ndryshohet nga i anketuari.

## Kombinimi i Vetëm-lexueshëm me Vlerat Parazgjedhëse

Fushat vetëm-lexueshëm shpesh përdoren në bashkëveprim me vlerat parazgjedhëse për të shfaqur informacione të paracaktuara ose të llogaritura:

```
| type    | name     | label               | read_only | default        |
|---------|----------|---------------------|-----------|----------------|
| text    | username | Përdoruesi i hyrë:  | yes       | ${current_user}|
| date    | today    | Data e sotme:       | yes       | today()        |
```

Këtu, emri i përdoruesit dhe data aktuale shfaqen por nuk mund të edituhen.

## Veçoritë Specifike rtSurvey

### Vetëm-lexueshëm me Kushte

rtSurvey zgjeron funksionalitetin vetëm-lexueshëm me logjikë të kushtëzuar:

```
| type    | name     | label           | read_only                |
|---------|----------|-----------------|--------------------------|
| integer | age      | Mosha:          | ${role} = 'viewer'       |
| text    | comments | Komentet:       | selected(${status}, 'closed') |
```

Në këto shembuj:
- Fusha 'age' është vetëm-lexueshëm vetëm nëse roli i përdoruesit është 'viewer'.
- Fusha 'comments' bëhet vetëm-lexueshëm nëse statusi është 'closed'.

### Statusi Dinamik Vetëm-lexueshëm

rtSurvey ju lejon të ndryshoni statusin vetëm-lexueshëm dinamikisht:

```
| type      | name     | label    | read_only              |
|-----------|----------|----------| ----------------------|
| text      | address  | Adresa:  | ${edit_mode} = 'false' |
```

Kjo ju lejon të kaloni midis mënyrave të edituesshme dhe vetëm-lexueshëm bazuar në kushte të caktuara ose veprime të përdoruesit.

## Praktikat Më të Mira për Përdorimin e Fushave Vetëm-lexueshëm

1. **Qartësia**: Tregoni qartë cilat fusha janë vetëm-lexueshëm nëpërmjet shenjave vizuale ose etiketave.
2. **Qëndrueshmëria**: Përdorni fushat vetëm-lexueshëm qëndrueshëm gjatë gjithë sondazhit tuaj.
3. **Validimi**: Edhe pse fushat vetëm-lexueshëm nuk mund të edituhen, përfshijini ato në procesin tuaj të validimit të të dhënave.
4. **Performanca**: Bëni kujdes me llogaritjet komplekse në fushat vetëm-lexueshëm, pasi mund të ndikojnë në kohën e ngarkimit të formularit.
5. **Aksesueshmëria**: Sigurohuni që fushat vetëm-lexueshëm janë shënuar siç duhet për lexuesit e ekranit.

## Teknikat e Avancuara

### Fushat Vetëm-lexueshëm të Llogaritura

Përdorni fushat vetëm-lexueshëm për të shfaqur llogaritjet bazuar në përgjigje të tjera:

```
| type      | name     | label           | read_only | calculation            |
|-----------|----------|-----------------|-----------|------------------------|
| calculate | bmi      | BMI:            | yes       | ${weight} / (${height} * ${height}) |
```

### Shfaqja e të Dhënave Historike

Fushat vetëm-lexueshëm mund të shfaqin të dhëna nga sondazhet e mëparshme ose burimet e jashtme:

```
| type    | name           | label                  | read_only | default                    |
|---------|----------------|------------------------|-----------|----------------------------|
| text    | last_visit_date| Data e vizitës të fundit: | yes    | ${pulldata('visits', 'date', 'id', ${patient_id})} |
```

## Konsideratat e Menaxhimit të të Dhënave

- Fushat vetëm-lexueshëm përfshihen në eksportet e të dhënave, zakonisht me një flamur që tregon statusin e tyre vetëm-lexueshëm.
- Kur përditësoni rekorde ekzistuese, fushat vetëm-lexueshëm ruajnë vlerat e tyre origjinale nëse nuk mbishkruhen shprehimisht nëpërmjet mbastës.

## Sjellja e Aplikacionit Celular

- Aplikacioni celular rtSurvey respekton cilësimet vetëm-lexueshëm, duke përfshirë logjikën e kushtëzuar vetëm-lexueshëm.
- Mënyra offline mbështet plotësisht funksionalitetin vetëm-lexueshëm, duke përfshirë fushat dinamike dhe të llogaritura vetëm-lexueshëm.

## Kufizimet e Njohura

- Disa kushte komplekse dinamike vetëm-lexueshëm mund të kenë një ndikim të vogël në performancë në pajisje të nivelit të ulët.
- Fushat vetëm-lexueshëm mund të mos parandalojnë të gjitha format e manipulimit të të dhënave në skedarët e eksportuar të të dhënave, kështu që validimi nga ana e serverit rekomandohet për të dhënat kritike.

## Zgjidhja e Problemeve me Fushat Vetëm-lexueshëm

1. **Fusha e Edituesshme në Mënyrë të Papritur**: Kontrolloni gabimet sintaksore në kolonën `read_only` ose logjikën e kushtëzuar.
2. **Vlerat e Llogaritura Nuk Përditësohen**: Verifikoni logjikën e llogaritjes dhe sigurohuni që të gjitha fushat e referuara janë emërtuar saktë.
3. **Probleme Performancë**: Optimizoni llogaritjet komplekse ose konsideroni qasje alternative për shfaqjen e të dhënave vetëm-lexueshëm.
