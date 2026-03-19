---
title: "Zgjedhja nga skedari"
description: "select_one_from_file dhe select_multiple_from_file ngarkojnë zgjedhjet dinamikisht nga një skedar i jashtëm CSV ose XML i bashkangjitur formulares."
icon: "file-earmark-spreadsheet"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 241
---

`select_one_from_file` dhe `select_multiple_from_file` funksionojnë si `select_one` dhe `select_multiple`, por në vend të përcaktimit të zgjedhjeve në **fletën choices**, zgjedhjet ngarkohen nga një **skedar i jashtëm CSV ose XML** i bashkangjitur formularit. Kjo është e dobishme kur lista e zgjedhjeve tuaja është shumë e gjatë, ndryshon shpesh, ose duhet të përditësohet pa rindërtuar të gjithë formularin.

## Specifikimi bazë XLSForm

| type | name | label |
|------|------|-------|
| select_one_from_file health_facilities.csv | facility | Zgjidhni objektin shëndetësor |
| select_multiple_from_file crops.csv | crops | Cilat kultura rriten nga familja? |

Emri i skedarit pas emrit të llojit duhet të përputhet me emrin e skedarit që bashkëngjitur kur ngarkoni formularin.

## Formati i skedarit CSV

Skedari juaj CSV duhet të ketë të paktën dy kolona: `name` (vlera e ruajtur) dhe `label` (teksti i shfaqur). Mund të shtoni çdo numër kolonash shtesë për filtrimin.

**health_facilities.csv:**

```
name,label,district,type
HF001,Klinika Qendrore e Nairobi,Nairobi,clinic
HF002,Qendra Shëndetësore Westlands,Nairobi,health_centre
HF003,Spitali i Rrethit Kisumu,Kisumu,hospital
```

## Filtrimi i zgjedhjeve

Përdorni kolonën `choice_filter` për të treguar vetëm zgjedhjet që përputhen me kontekstin aktual. Referojuni kolonave CSV me emrin e tyre direkt (pa `${}`):

| type | name | label | choice_filter |
|------|------|-------|---------------|
| select_one districts.csv | district | Zgjidhni rrethin | |
| select_one_from_file health_facilities.csv | facility | Zgjidhni objektin | district = ${district} |

Në këtë shembull, shfaqen vetëm objektet në rrethin e zgjedhur. `district` në `choice_filter` referon kolonën `district` në skedarin CSV; `${district}` referon fushën e formularit të quajtur `district`.

## Përdorimet

Pyetjet select-from-file përdoren zakonisht për:

1. **Lista të gjata zgjedhjesh** — objekte shëndetësore, shkolla, fshatra, lista të specieve (qindra ose mijëra artikuj)
2. **Lista të përditësuara shpesh** — kur lista kryesore ndryshon midis raundeve të sondazhit, përditësoni vetëm CSV pa rindërtuar formularin
3. **Të dhëna referuese të ndara** — një skedar CSV i përdorur nëpër formularë të shumtë
4. **Zgjedhjet e filtruara në kaskadë** — ngarkoni të gjitha rajonet/rrethet/fshatrat në një skedar, pastaj filtroni sipas zgjedhjes prind

## Bashkëngjitur skedarin

Kur ngarkoni formularin tuaj në rtSurvey, bashkëngjitur skedarin CSV si **bashkëngjitje media**. Emri i skedarit në përkufizimin e formularit duhet të përputhet saktësisht me emrin e skedarit të bashkëngjitjes.

{{% alert icon=" " context="warning" %}}
Emrat e skedarëve janë të ndjeshëm ndaj shkronjave. `Health_Facilities.csv` dhe `health_facilities.csv` trajtohen si skedarë të ndryshëm.
{{% /alert %}}

## Përdorimi i `choice-label()` me from-file

Për të shfaqur etiketën e zgjedhjes së zgjedhur në fushën note ose calculate:

| type | name | label | calculation |
|------|------|-------|-------------|
| select_one_from_file health_facilities.csv | facility | Zgjidhni objektin | |
| calculate | facility_label | | choice-label(${facility}, ${facility}) |
| note | summary | Objekti i zgjedhur: ${facility_label} | |

## Praktikat më të mira

1. Mbajini skedarët CSV nën 5,000 rreshta për performancë të mirë në pajisjet mobile.
2. Gjithmonë përfshini kolonën `name` dhe `label` — kolonat shtesë janë opsionale.
3. Për zgjedhjet në kaskadë, përdorni një CSV të vetëm me kolonë prind dhe filtroni me `choice_filter`.
4. Versiononi emrat e skedarëve CSV (p.sh., `facilities_v3.csv`) kur bëni ndryshime të mëdha në strukturën e kolonave.
5. Testoni me kujdes shprehjet e filtrimit — një gabim shkrimi në `choice_filter` do të tregojë fshehtazi asnjë zgjedhje.

## Kufizimet

- Skedarët CSV shumë të mëdhenj (10,000+ rreshta) mund të ngadalësojnë ngarkimin e formularit, veçanërisht në pajisjet e nivelit të ulët.
- Skedarët CSV duhet të ngarkohen bashkë me formularin — nuk mund të merren nga URL gjatë ekzekutimit (përdorni `search()` ose `pulldata()` për kërkime dinamike).
- `select_multiple_from_file` mbështetet më pak zakonisht nëpër klientë — verifikoni përputhshmërinë para përdorimit.

## Krahasimi me `search()`

| | `select_one_from_file` | Pamja `search()` |
|--|----------------------|----------------------|
| Burimi i zgjedhjeve | Skedar CSV/XML i bashkangjitur | Pyetje e bazës së të dhënave në anën e serverit |
| Funksionon offline | Po (skedari është i bashkuar) | Kërkon lidhje |
| Numri i zgjedhjeve | I kufizuar nga memoria e pajisjes | I pakufizuar (i faqosur) |
| Të dhëna në kohë reale | Jo | Po |

Për bashkësi të dhënash të mëdha, shpesh ndryshuar, ose të anës së serverit, shikoni [Kërkim dinamik](../advanced-extension/dynamic-search).
