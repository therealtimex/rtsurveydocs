---
title: "Obrázek"
description: "Otázky image umožňují respondentům zachytit a odeslat fotografie jako součást průzkumu."
icon: "image"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 227
---

Typ otázky image v XLSForms a rtSurvey umožňuje respondentům zachytit a odeslat fotografie jako součást jejich odpovědí na průzkum. Tato funkce je zvláště užitečná pro sběr vizuálních dat, dokumentování pozorování nebo poskytování důkazů při terénních průzkumech.

## Základní specifikace XLSForm

| type  | name        | label                           |
|-------|-------------|--------------------------------|
| image | photo       | Vyfotografujte místo    |

## Použití

Otázky image se běžně používají pro:

1. Dokumentování terénních podmínek nebo pozorování
2. Zachycování vizuálních důkazů ve výzkumných studiích
3. Sběr fotografií před a po v hodnocení dopadu
4. Ověřování dokončení úkolů nebo přítomnosti na místech
5. Shromažďování vizuálních dat pro vzdálenou analýzu

## Osvědčené postupy

1. Poskytněte jasné pokyny o tom, co by mělo být fotografováno.
2. Zvažte důsledky pro soukromí a informujte respondenty o tom, jak budou jejich fotografie použity.
3. Buďte obeznámeni s velikostí souborů a omezeními úložiště, zejména pro průzkumy v oblastech s omezeným připojením k internetu.
4. Zajistěte, aby mělo zařízení dostatek místa v úložišti a aby byla udělena oprávnění ke kameře.

## Příklad použití

| type  | name           | label                                      | hint                                        |
|-------|----------------|--------------------------------------------|--------------------------------------------|
| image | storefront     | Vyfotografujte vchod do obchodu       | Ujistěte se, že název obchodu je jasně viditelný    |

## Zpracování dat

Obrázky shromážděné prostřednictvím tohoto typu otázky jsou obvykle:

1. Uloženy v běžném formátu obrázku (např. JPG, PNG)
2. Uloženy spolu s ostatními daty průzkumu, často v samostatné mediální složce
3. Přístupné pro prohlížení a analýzu prostřednictvím platformy správy průzkumu

## Omezení

- Soubory obrázků mohou být velké, což může ovlivnit přenos dat a úložiště.
- Ne všechna zařízení mohou mít vysokokvalitnlí kamery nebo dostatek místa v úložišti.
- Analýza velkého počtu obrázků může být časově náročná.
- Při pořizování obrázků, zejména na veřejných místech, mohou existovat obavy o soukromí.

## Rozšíření rtSurvey pro obrázky

### watermark()

Vzhled `watermark()` překryje textový vodoznak na fotografiích zachycených v tomto poli. Vodoznak obvykle obsahuje metadata jako jméno enumerátora, datum/čas nebo GPS souřadnice, razítko přímo na obrázek před uložením.

| type | name | label | appearance |
|------|------|-------|------------|
| image | site_photo | Vyfotografujte místo | `watermark("${enumerator_id} ${today()}")` |

Argument pro `watermark()` je výraz XPath vyhodnocený v době zachycení. Výsledný řetězec je vykreslen jako text vodoznaku.

### editable

Vzhled `editable` umožňuje respondentovi anotovat nebo kreslit na zachycenou fotografii po jejím pořízení. Nad obrázkem se zobrazí panel nástrojů pro kreslení.

| type | name | label | appearance |
|------|------|-------|------------|
| image | annotated_photo | Vyfotografujte a označte oblasti zájmu | editable |

{{% alert icon=" " context="info" %}}
`editable` lze kombinovat s `watermark()`: `appearance: editable watermark("${id}")`
{{% /alert %}}
