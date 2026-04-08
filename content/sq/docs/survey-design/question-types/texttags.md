---
title: "Text Tags"
description: "Fushë e hyrjes së etiketave — të anketuarit shkruajnë dhe shtyjnë Enter për të krijuar shenja etiketash të veçanta."
icon: "label"
date: "2026-04-08T00:00:00+00:00"
lastmod: "2026-04-08T00:00:00+00:00"
draft: false
toc: true
weight: 264
---

Lloji i pyetjes `texttags` (i quajtur gjithashtu `text_tags`) renderueson një hyrje ku çdo vlerë e futur nga përdoruesi bëhet një **token etikete** i veçantë. Përdoruesit shtypin një vlerë, shtyjnë Enter ose një tast kufizues, dhe vlera shtohet si chip i heqshëm. Mund të shtohen etiketa të shumëfishta në një përgjigje të vetme.

## Specifikimi bazë XLSForm

| type | name | label |
|------|------|-------|
| texttags | keywords | Shkruani fjalë kyçe (shtypni Enter pas secilës) |

## Sjellja

- Çdo hyrje e konfirmuar bëhet etiketë e shfaqur si pill/chip brenda fushës.
- Etiketat mund të hiqen individualisht duke klikuar × në chip.
- Vlera e ruajtur është një varg i ndarë me hapësira i të gjitha etiketave të futura.

## Përdorimet

1. Mbledhja e fjalëve kyçe ose kodeve të shumëfishta me tekst të lirë pa listë të paracaktuar
2. Fushat e etiketimit ose kategorizimit ku grupi i vlerave është i hapur
3. Çdo hyrje teksti me shumë vlera ku `select_multiple` është shumë i ngurtë

## Formati i të dhënave

Etiketat ruhen si varg i vetëm i ndarë me hapësira. Për shembull, nëse përdoruesi fut `malaria`, `ethe`, dhe `kollë`, vlera e ruajtur është `malaria ethe kollë`.

## Mbështetja e platformës

Mbështetet në formularët web.

## Kufizimet

- Nuk është pjesë e specifikimit standard XLSForm — vetëm zgjerim rtSurvey.
- Meqenëse vlerat janë tekst i lirë, analiza e mëvonshme kërkon ndarjen e vargut me hapësira.
