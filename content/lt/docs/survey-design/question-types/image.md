---
title: "Vaizdas"
description: "Vaizdo klausimai leidžia respondentams fiksuoti ir pateikti nuotraukas kaip apklausos dalį."
icon: "image"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 227
---

XLSForm ir rtSurvey vaizdo klausimo tipas leidžia respondentams fiksuoti ir pateikti nuotraukas kaip savo apklausos atsakymų dalį. Ši funkcija ypač naudinga vizualiniams duomenims rinkti, stebėjimams dokumentuoti ar lauko apklausų įrodymams pateikti.

## Pagrindinė XLSForm specifikacija

| type  | name        | label                           |
|-------|-------------|--------------------------------|
| image | photo       | Nufotografuokite vietą          |

## Naudojimo atvejai

Vaizdo klausimai dažnai naudojami:

1. Lauko sąlygų ar stebėjimų dokumentavimui
2. Vizualinių įrodymų fiksavimui mokslinių tyrimų metu
3. Prieš ir po nuotraukų rinkimui poveikio vertinimuose
4. Užduočių atlikimo ar buvimo vietose patvirtinimui
5. Vizualinių duomenų rinkimui nuotolinei analizei

## Geriausios praktikos

1. Pateikite aiškias instrukcijas, ką reikia fotografuoti.
2. Atsižvelkite į privatumo pasekmes ir informuokite respondentus, kaip bus naudojamos jų nuotraukos.
3. Atkreipkite dėmesį į failų dydžius ir saugyklos apribojimus, ypač apklausoms vietovėse su ribotos interneto prieigos.
4. Užtikrinkite, kad įrenginyje yra pakankamai saugyklos vietos ir fotoaparato leidimai yra suteikti.

## Naudojimo pavyzdys

Štai pavyzdys, kaip galima naudoti vaizdo klausimą apklausoje:

| type  | name           | label                                      | hint                                        |
|-------|----------------|--------------------------------------------|--------------------------------------------|
| image | storefront     | Nufotografuokite parduotuvės įėjimą        | Užtikrinkite, kad parduotuvės pavadinimas yra aiškiai matomas |

## Duomenų tvarkymas

Per šį klausimo tipą surinkti vaizdai paprastai yra:

1. Išsaugomi bendrame vaizdo formate (pvz., JPG, PNG)
2. Saugomi kartu su kitais apklausos duomenimis, dažnai atskirame medijos aplanke
3. Prieinami peržiūrai ir analizei per apklausos valdymo platformą

## Analizės svarstymai

Naudojant vaizdo klausimus, atsižvelkite į:

1. Kaip vaizdai bus analizuojami (pvz., rankine peržiūra, automatine vaizdo analize)
2. Papildomą saugyklos vietą, reikalingą vaizdo failams
3. Privatumo ir duomenų apsaugos priemones nuotraukų saugojimui ir tvarkymui
4. Galimą poreikį vaizdo redagavimo ar organizavimo įrankiams analizės fazėje

## Apribojimai

- Vaizdo failai gali būti dideli, o tai gali turėti įtakos duomenų perkėlimui ir saugyklai.
- Ne visi įrenginiai gali turėti aukštos kokybės fotoaparatus ar pakankamai saugyklos vietos.
- Didelių vaizdų kiekio analizė gali būti daug laiko reikalaujanti.
- Fiksuojant vaizdus, ypač viešose vietose, gali kilti privatumo problemų.

## rtSurvey vaizdo plėtiniai

### watermark()

Išvaizdos variantas `watermark()` uždeda teksto vandens ženklą ant nuotraukų, užfiksuotų su šiuo lauku. Vandens ženklas paprastai yra metaduomenys, tokie kaip surašytojo vardas, data/laikas arba GPS koordinatės, antspauduotos tiesiai ant vaizdo prieš išsaugojimą.

| type | name | label | appearance |
|------|------|-------|------------|
| image | site_photo | Nufotografuokite objektą | `watermark("${enumerator_id} ${today()}")` |

`watermark()` argumentas yra XPath išraiška, įvertinta fiksavimo metu. Gauta eilutė atvaizduojama kaip vandens ženklo tekstas.

### editable

Išvaizdos variantas `editable` leidžia respondentui anotuoti arba piešti ant užfiksuotos nuotraukos po jos padarymo. Virš vaizdo atsiranda piešimo įrankių juosta.

| type | name | label | appearance |
|------|------|-------|------------|
| image | annotated_photo | Fotografuokite ir pažymėkite probleminias sritis | editable |

{{% alert icon=" " context="info" %}}
`editable` gali būti derinamas su `watermark()`: `appearance: editable watermark("${id}")`
{{% /alert %}}
