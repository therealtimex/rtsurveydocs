---
title: "Geotrace"
description: "Geotrace klausimai leidžia respondentams žemėlapyje fiksuoti sujungtų taškų seriją, kuriant linijas ar maršrutus kaip apklausos dalį."
icon: "timeline"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 234
---

XLSForm ir rtSurvey geotrace klausimo tipas leidžia respondentams žemėlapyje fiksuoti sujungtų taškų seriją, kuriant linijas ar maršrutus. Ši funkcija ypač naudinga maršrutų žemėlapiams sudaryti, ribų atsekimui ar linijinių požymių žymėjimui erdvinėse apklausose.

## Pagrindinė XLSForm specifikacija

| type     | name        | label                           |
|----------|-------------|--------------------------------|
| geotrace | river_path  | Nubrėžkite upės maršrutą        |

## Naudojimo atvejai

Geotrace klausimai dažnai naudojami:

1. Lauko tyrimų metu nueintų maršrutų žemėlapiams sudaryti
2. Linijinių požymių, tokių kaip keliai, upės ar ribos, atsekimui
3. Linijinės infrastruktūros apimties fiksavimui (pvz., vamzdynai, elektros linijos)
4. Kelionių maršrutų įrašymui transporto tyrimuose
5. Transektų apibrėžimui ekologiniuose tyrimuose

## Geriausios praktikos

1. Užtikrinkite, kad įrenginyje yra įjungtos vietos paslaugos ir suteikti leidimai.
2. Pateikite aiškias instrukcijas, kaip atsekti maršrutą ir kokie požymiai turėtų būti įtraukti.
3. Apsvarstykite galimybę naudoti palydovinę nuotrauką ar pagrindus žemėlapius, kad padėtumėte respondentams tiksliai atsekti maršrutus.
4. Atkreipkite dėmesį į galimą atsekimų sudėtingumą ir jo poveikį duomenų dydžiui ir apdorojimui.

## Naudojimo pavyzdys

Štai pavyzdys, kaip galima naudoti geotrace klausimą apklausoje:

| type     | name           | label                                      | hint                                        |
|----------|----------------|--------------------------------------------|--------------------------------------------|
| geotrace | hiking_trail   | Nubrėžkite pėsčiųjų tako maršrutą         | Pradėkite nuo tako pradžios ir baikite viršūnėje |

## Duomenų formatas

Geotrace duomenys paprastai saugomi kaip tarpais atskirtų koordinačių porų eilutė, panaši į geoshape, bet be uždarymo taško:

```
lat1 lon1; lat2 lon2; lat3 lon3; ... latN lonN
```

## Analizės svarstymai

Naudojant geotrace klausimus, atsižvelkite į:

1. Kaip geografiniai duomenys bus vizualizuojami ir analizuojami (pvz., GIS programinė įranga)
2. Galimą poreikį valyti duomenis ar supaprastinti sudėtingus atsekimus
3. Privatumo ir duomenų apsaugos priemones tvarkant išsamius erdvinius duomenis
4. Integraciją su kitais erdviniais duomenų šaltiniais išsamiai analizei

## Apribojimai

- Tikslių maršrutų atsekimas mažuose mobiliųjų ekranuose gali būti sudėtingas.
- Sudėtingi atsekimai gali reikalauti didelės saugyklos ir apdorojimo pajėgumų.
- Nuolatinis GPS naudojimas automatiniam atsekimui gali greitai išeikvoti įrenginio bateriją.
- Su išsamių maršruto duomenų rinkimu gali būti susijusios privatumo problemos.
