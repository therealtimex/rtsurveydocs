---
title: "Validimi i përgjigjeve"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 270
---

Një mënyrë për të garantuar cilësinë e të dhënave është shtimi i kufizimeve në fushat e të dhënave të formularit tuaj. Kufizimet ndihmojnë në parandalimin e futjes së përgjigjeve të pavlefshme ose të pamundura nga përdoruesit. Për shembull, kur pyesni për të ardhurat e një personi, dëshironi të shmangni vlera të pareale, si numrat negativë ose vlerat jashtëzakonisht të larta. Shtimi i kufizimeve të të dhënave në formularin tuaj është i lehtë për t'u bërë. Thjesht ndiqni hapat e mëposhtëm:

1. Shtoni një kolonë të re të quajtur "constraint" në formularin tuaj.
2. Në kolonën "constraint", futni një formulë që specifikon kufijtë në përgjigje.

### Shembull

Le të konsiderojmë një shembull ku dëshirojmë të shtojmë një kufizim për të ardhurat e personit. Kufizimi kërkon që të ardhurat të jenë midis $0 dhe $1,000,000. Ja si mund të konfiguroni kufizimin:

{{< table >}}
| `name`      | `constraint`                  |
|---------------|-----------------------------|
| Income        | . >= 0 & . <= 1000000      |
{{< /table >}}

Në shembullin e mësipërm, "." në formulë i referohet variablit të pyetjes, i cili përfaqëson vlerën e futur nga përdoruesi për pyetjen "Income". Kufizimi ". >= 0 && . <= 1000000" garanton që të ardhurat e futura janë më të mëdha ose të barabarta me 0 dhe më të vogla ose të barabarta me 1,000,000.


### Kufizimi i fortë

Një **kufizim i fortë** bllokon plotësisht dorëzimin e formularit nëse vlera e futur nuk plotëson shprehjen. Numëruesi nuk mund të vazhdojë derisa të fusë një vlerë të vlefshme.

Për të shtuar një kufizim të fortë, futni shprehjen tuaj në kolonën `constraint`. Opsionalisht shtoni një mesazh të lexueshëm nga njerëzit në `constraint_message`:

{{< table >}}
| `type` | `name` | `label` | `constraint` | `constraint_message` |
|--------|--------|---------|--------------|----------------------|
| integer | age | Mosha e të anketuarit | `. > 0 and . <= 120` | Mosha duhet të jetë midis 1 dhe 120 |
| decimal | temperature | Temperatura e trupit (°C) | `. >= 35 and . <= 42` | Temperatura duhet të jetë midis 35°C dhe 42°C |
| text | phone | Numri i telefonit | `regex(., '^[0-9]{10}$')` | Futni një numër telefoni me 10 shifra |
{{< /table >}}

#### Kushte të shumëfishta

Kombinoni kushtet me `and` / `or`:

```
. >= 0 and . <= 100
```

```
. = 'yes' or . = 'no'
```

#### Përdorimi i `regex()` për validimin e modelit

Funksioni `regex(value, pattern)` teston një vlerë kundrejt një shprehjeje të rregullt:

{{< table >}}
| `type` | `name` | `label` | `constraint` | `constraint_message` |
|--------|--------|---------|--------------|----------------------|
| text | email | Adresa email | `regex(., '^[^@]+@[^@]+\.[^@]+$')` | Futni një adresë email të vlefshme |
| text | zip_code | Kodi ZIP | `regex(., '^[0-9]{5}$')` | Futni një kod ZIP me 5 shifra |
{{< /table >}}

#### Referimi i fushave të tjera në kufizim

Përdorni `${fieldname}` për të referuar vlerat nga pyetje të tjera:

{{< table >}}
| `type` | `name` | `label` | `constraint` | `constraint_message` |
|--------|--------|---------|--------------|----------------------|
| integer | end_year | Viti i mbarimit | `. >= ${start_year}` | Viti i mbarimit duhet të jetë pas vitit të fillimit |
| decimal | loan_repaid | Shuma e shlyer | `. <= ${loan_amount}` | Nuk mund të shlyhet më shumë se shuma e kredisë |
{{< /table >}}

### Sinjalizimi i butë

Një **sinjalizim i butë** (i quajtur edhe kufizim i butë ose paralajmërim) paralajmëron numëruesin se një vlerë duket e pazakontë, por ende i lejon të vazhdojë. Kjo është e dobishme kur një vlerë është teknikisht e vlefshme por statistikisht e pamundshme.

rtSurvey mbështet sinjalizimet e buta duke përdorur kolonën `constraint` me një qasje të veçantë `constraint_type`, ose nëpërmjet pamjes `soft` të kombinuar me një fushë shënim.

Modeli më i zakonshëm është të përdoret një **shënim** me një shprehje `relevant` që sinjalizon vlerën e dyshimtë, e çiftuar me një pyetje **acknowledge** për konfirmim:

{{< table >}}
| `type` | `name` | `label` | `relevant` |
|--------|--------|---------|------------|
| integer | children | Numri i fëmijëve | |
| note | children_warning | Paralajmërim: Keni futur ${children} fëmijë. Ju lutemi konfirmoni që kjo është e saktë. | `. > 15` |
| trigger | children_confirm | Konfirmoni që numri i fëmijëve është i saktë | `${children} > 15` |
{{< /table >}}

#### Sinjalizim i butë vetëm me constraint_message

Për një paralajmërim të thjeshtë të butë, mund ta formuloni kufizimin që të paralajmërojë për vlera ekstreme por ende të lejojë një gamë të gjerë:

{{< table >}}
| `type` | `name` | `label` | `constraint` | `constraint_message` |
|--------|--------|---------|--------------|----------------------|
| integer | children | Numri i fëmijëve | `. >= 0 and . <= 30` | Kjo vlerë duket shumë e lartë. Ju lutemi verifikoni. |
{{< /table >}}

{{% alert icon=" " context="warning" %}}
Dallimi midis kufizimeve të forta dhe të buta ka rëndësi për cilësinë e të dhënave. Përdorni **kufizime të forta** për vlera logjikisht të pamundura (mosha negative, temperatura mbi 100°C). Përdorni **sinjalizime të buta** për vlera statistikisht të pamundshme por jo të pamundura — nuk dëshironi të bllokoni rastet legjitime kufitare.
{{% /alert %}}
