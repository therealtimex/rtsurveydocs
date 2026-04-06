---
title: "App API"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 300
---

AppAPI lejon përdoruesit të ngarkojnë metadata të sistemit nga aplikacioni duke përdorur metoda të ndryshme në FormEngine dhe DMView. Ai siguron akses ndaj çelësave të ndryshëm të të dhënave për marrjen e informacioneve specifike nga aplikacioni.

Në xlsform, mund të përdorni funksionin `pulldata()` me sintaksën e mëposhtme:


{{< alert context="light" text="pulldata('app-api', 'data-key')" />}}

- `'app-api'`: Ky fjalë kyçe informon FormEngine-in të ngarkojë të dhënat nga App API.
- `'data-key'`: Ky është çelësi i të dhënave që dëshironi të ngarkoni nga App API.
- Nëse çelësi i të dhënave është i pavlefshëm ose nuk mbështetet, llogaritja do të kthejë "n/a".

Ja çelësat e të dhënave të mbështetura që mund të përdorni me App-API:

`osPlatform`: Kthen emrin aktual të OS (Android ose iOS) dhe versionin e OS. Platformat ueb do të kthejnë një vlerë bosh.

`appPlatform`: Kthen emrin e platformës së aplikacionit, që është `rtSurvey`.

`appVersion`: Kthen emrin e versionit të aplikacionit.

`getDisplayWidth`: Kthen gjerësinë e ekranit të pajisjes në piksel.

`getDisplayHeight`: Kthen lartësinë e ekranit të pajisjes në piksel.

`getScreenSize`: Kthen madhësinë e ekranit të pajisjes në inç.

`projectCode`: Kthen kodin aktual të projektit të faqes ku hyn përdoruesi.

`projectURL`: Kthen URL-n aktuale të projektit të faqes ku hyn përdoruesi. Vlera parazgjedhëse/rezervë është tekst bosh ("").

`startingPoint`: Kthen rrugën e pikës që fillon formularin. Referojuni "Pikës fillestare të formularit" për më shumë detaje.

`serverTime`: Kthen përafrimin më të mirë të disponueshëm të datës dhe orës në server.

`user.[attribute]`: Kthen atributet e përdoruesit aktual bazuar në çelësin e atributit të specifikuar. Referojuni tabelës "Atributet e Përdoruesit" për çelësat e disponueshëm të atributeve.

Kombinoni çelësat e atributeve të mëposhtme me "user." në parametrat `pulldata()` për të marrë informacionet e përdoruesit aktual. Për shembull, përdorni `user.username`, `user.email`, etj.

| Çelësi i Atributit | Përshkrimi |
|----------------------|--------------------------------------|
| username             | Emri i përdoruesit të përdoruesit    |
| name                 | Emri i plotë i përdoruesit           |
| staffCode            | Kodi i stafit të përdoruesit         |
| phone                | Numri i telefonit të përdoruesit     |
| email                | Adresa email e përdoruesit           |
| description          | Teksti i përshkrimit në informacionin e përdoruesit |
| organization_id      | ID-ja e organizatës së cilës i përket përdoruesi |
| organization_name    | Emri i organizatës së cilës i përket përdoruesi |
| team_id              | ID-ja e ekipit të cilit i përket përdoruesi |
| supervisor_id        | ID-ja e mbikëqyrësit të përdoruesit  |
| is_supervisor        | 1 nëse përdoruesi është mbikëqyrës, 0 nëse jo |

`instancePath`: Kthen rrugën aktuale të dosjes së instancës.

`appLanguage`: Kthen gjuhën aktuale të aplikacionit të caktuar në cilësimet e aplikacionit (p.sh., vi, en, sq).

`openArgs.[attribute]`: Kthen argumentin open-form të kaluar nga ActionButton (act_fill_form, act_get_instance). Vlera parazgjedhëse/rezervë është tekst bosh ("").

`primaryAppColor`: Merr ngjyrën kryesore të aplikacionit.

---

## Shembuj Përdorimi

### Ruani emrin e përdoruesit dhe organizatën e numëruesit

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | enumerator_name | | `pulldata('app-api', 'user.name')` |
| calculate | enumerator_org | | `pulldata('app-api', 'user.organization_name')` |
| calculate | enumerator_email | | `pulldata('app-api', 'user.email')` |

Përdorini këto në etiketat e shënimit për qëllime auditimi:
```
note | interviewer_info | Intervistruesi: ${enumerator_name} (${enumerator_org})
```

### Informacioni i pajisjes dhe ekranit

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | device_platform | | `pulldata('app-api', 'osPlatform')` |
| calculate | app_ver | | `pulldata('app-api', 'appVersion')` |
| calculate | screen_w | | `pulldata('app-api', 'getDisplayWidth')` |

I dobishëm për zgjidhjen e problemeve: eksportoni `device_platform` dhe `app_ver` krahas të dhënave tuaja për të identifikuar cilën version pajisje u përdor për çdo dorëzim.

### Ora e serverit në vend të orës së pajisjes

Orët e pajisjeve mund të jenë të pasakta. Përdorni `serverTime` për një shenjë kohore më të besueshme:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | server_ts | | `pulldata('app-api', 'serverTime')` |

### Logjikë e kushtëzuar bazuar në rolin e përdoruesit

Tregoni një seksion vetëm për mbikëqyrësin vetëm te mbikëqyrësit:

| type | name | label | relevant |
|------|------|-------|----------|
| calculate | is_supervisor | | `pulldata('app-api', 'user.is_supervisor')` |
| begin_group | supervisor_section | Rishikimi i mbikëqyrësit | `${is_supervisor} = '1'` |
| text | supervisor_notes | Shënime mbikëqyrësi | |
| end_group | | | |

### Kaloni argumentet nga një buton veprimi

Kur formulari hapet nga një buton veprimi `act_fill_form` me argumenta të personalizuar:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | passed_hh_id | | `pulldata('app-api', 'openArgs.household_id')` |
| calculate | passed_task | | `pulldata('app-api', 'openArgs.task_code')` |

Butoni i veprimit duhet të kalojë argumentet me çelësa përputhës (p.sh., `household_id`, `task_code`).

### Përdorimi i informacionit të projektit

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | project | | `pulldata('app-api', 'projectCode')` |
| calculate | project_url | | `pulldata('app-api', 'projectURL')` |

---

## Shënime

- Të gjitha thirrjet `pulldata('app-api', ...)` vlerësohen kur formulari hapet dhe nuk rivlerësohen dinamikisht gjatë sesionit (me përjashtim të `serverTime` dhe `now()`).
- Nëse një çelës nuk mbështetet ose të dhënat janë të padisponueshme, funksioni kthen `'n/a'` (jo varg bosh — testoni me `!= 'n/a'` në vend të `!= ''`).
- Vlerat `openArgs` janë të disponueshme vetëm kur formulari hapet nga një buton veprimi; ato kthejnë varg bosh ndryshe.
