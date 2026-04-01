---
title: "Hidden"
description: "Fushat e fshehura ruajnë vlera që nuk shfaqen kurrë te i anketuari — përdoren për të kaluar kontekst, parapredisur të dhëna, ose ruajtur rezultate ndërmjetëse."
icon: "eye-slash"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 239
---

Fusha `hidden` ruan një vlerë që **nuk shfaqet kurrë te i anketuari**. Ndryshe nga `calculate` (i cili llogarit një vlerë), `hidden` përdoret për të mbajtur një **vlerë të ofruar jashtë** — për shembull, ID e detyrës, ID e familjes kaluar nga sistemi tjetër, ose kodi i numëruesit i injektuar kur formulari ngarkohet.

## Specifikimi bazë XLSForm

| type | name | label |
|------|------|-------|
| hidden | household_id | |

Etiketat nuk kërkohen për fushat e fshehura pasi asgjë nuk paraqitet në ekran.

## Përdorimet

Fushat e fshehura përdoren zakonisht për:

1. Kalimi i një ID të paracaktuar nga sistemi i menaxhimit të sondazhit (p.sh., ID familje, numri i rastit, kodi i detyrës)
2. Ruajtja e versionit të formularit ose metadata e vendosjes
3. Injektimi i konfigurimit specifik të numëruesit kur formulari ngarkohet
4. Bartja e të dhënave nga formulari prind te formulari fëmijë në flukset e punës të lidhura
5. Ruajtja e vlerës së nxjerrë nga parametrat URL kur formulari hapet nëpërmjet lidhjes web

## Vendosja e vlerës parazgjedhëse

Modeli më i zakonshëm është të përdorni `hidden` me shprehje `default` kështu vlera caktohet kur hapet formulari:

| type | name | default |
|------|------|---------|
| hidden | deployment_code | 'ZONE_A_2024' |
| hidden | form_version | '3.1' |

## Referimi i fushës së fshehur në llogaritje

Vlerat e fshehura mund të referohen si çdo fushë tjetër duke përdorur `${fieldname}`:

| type | name | label | calculation |
|------|------|-------|-------------|
| hidden | zone_code | | |
| calculate | label_prefix | | concat('[', ${zone_code}, '] ') |
| note | intro | ${label_prefix} Mirë se vini në sondazhin e familjes | |

## Përdorimi i fushave të fshehura me parapredisje / parametra URL

Kur nisni formularin web nëpërmjet URL, mund të kaloni parametra që plotësojnë fushat e fshehura. Kjo ju lejon të parapredisni ID e familjes ose kodin e detyrës pa e shtypurin numëruesi:

```
https://your-server.com/form/FORMID?household_id=H00123&zone_code=NORTH
```

Fusha e quajtur `household_id` do të plotësohet automatikisht me `H00123`.

## Praktikat më të mira

1. Përdorni `hidden` (jo `calculate`) kur vlera **injektohet jashtë** dhe nuk duhet të rillogaritet.
2. Përdorni `calculate` kur vlera **nxirret nga fushat e tjera** në formular.
3. Gjithmonë vendosni `default` nëse fusha e fshehur duhet të ketë vlerë — fusha e fshehur pa parazgjedhje do të jetë bosh.
4. Emërtoni fushat e fshehura qartë për t'i dalluar (p.sh., parashtesë me `_hidden_` ose përdorni konventë të qëndrueshme emërtimi).

## Kufizimet

- Fushat e fshehura përfshihen në të dhënat e eksportuara si çdo fushë tjetër.
- Ato nuk mund të shfaqen me kusht — janë gjithmonë të pranishme (por të padukshme).
- Nëse keni nevojë për fushë që llogarit dinamikisht, përdorni `calculate` në vend.
