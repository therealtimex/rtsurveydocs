---
title: "Mentions"
description: "Fushë teksti me plotësim automatik të @-mencioneve për etiketimin e përdoruesve ose entiteteve brenda tekstit."
icon: "alternate_email"
date: "2026-04-08T00:00:00+00:00"
lastmod: "2026-04-08T00:00:00+00:00"
draft: false
toc: true
weight: 262
---

Lloji i pyetjes `mentions` është një hyrje teksti që aktivizon një listë rënëse plotësimi automatik kur përdoruesi shtype `@`. Përdoret për të etiketuar përdorues, emra stafi, kode, ose çdo entitet inline brenda një përgjigje teksti të lirë.

## Specifikimi bazë XLSForm

| type | name | label |
|------|------|-------|
| mentions | note_text | Shkruani shënime vëzhgimi (përdorni @ për të etiketuar një anëtar stafi) |

## Sjellja

- Shtypja standarde prodhon tekst të zakonshëm.
- Shtypja e `@` e ndjekur nga karaktere nxit një kërkim plotësimi automatik kundrejt një liste të konfiguruar ose API-je.
- Zgjedhja e një sugjerimi fut tokenin e mencionit në tekst.
- Vlera e ruajtur është vargu i plotë i tekstit duke përfshirë çdo token mencionie të ngulitur.

## Përdorimet

1. Shënime cilësore që referojnë anëtarë specifike të stafit ose entitete me emër
2. Regjistrime vëzhgimi ku personat ose vendndodhje të shumëfishta duhet të etiketohen
3. Çdo fushë teksti të lirë ku referencat e kontrolluara inline përmirësojnë analizën e mëvonshme

## Mbështetja e platformës

Mbështetet në formularët web.

## Kufizimet

- Nuk është pjesë e specifikimit standard XLSForm — vetëm zgjerim rtSurvey.
- Burimi i listës së mencioneve (statike ose e drejtuar nga API) konfigurohet në nivel serveri, jo në XLSForm.
