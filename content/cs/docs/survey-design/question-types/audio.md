---
title: "Audio"
description: "Otázky audio umožňují respondentům nahrávat a odesílat zvukové soubory jako součást průzkumu."
icon: "mic"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 228
---

Typ otázky `audio` umožňuje respondentům **nahrávat zvuk** nebo nahrát existující zvukový soubor jako součást jejich odpovědi na průzkum. Je užitečný pro zachycení verbálních vysvětlení, zvuků prostředí, svědectví nebo jakýchkoli informací, které jsou lépe předávány hlasem než textem.

## Základní specifikace XLSForm

| type  | name        | label                        |
|-------|-------------|------------------------------|
| audio | voice_note  | Prosím nahrajte své komentáře  |

## Použití

Zvukové otázky se běžně používají pro:

1. Zachycení otevřených verbálních odpovědí pro snížení zátěže psaní enumerátora
2. Nahrávání svědectví, osobních příběhů nebo ústní historie
3. Dokumentování zvuků prostředí (např. úrovně hluku v blízkosti infrastruktury)
4. Sběr hlasových vzorků pro lingvistický nebo zdravotní výzkum
5. Umožnění respondentům přidat verbální upřesnění k číselným nebo výběrovým odpovědím

## Formát dat

Zvukové soubory jsou uloženy jako binární přílohy spolu s odesláním formuláře:

- **Formát:** MP3 nebo AAC (mobilní nahrávání); WAV (vysoká kvalita)
- **Pojmenování:** `{instanceID}-{fieldname}.mp3` (nebo ekvivalent)
- **Úložiště:** Nahráno do mediální složky serveru a propojeno se záznamem odeslání
- **Přístup:** Přehratelné a ke stažení z rozhraní správy odeslání

## Rozšíření rtSurvey

### Maximální délka

Použijte sloupec `parameters` pro omezení délky záznamu:

| type | name | label | parameters |
|------|------|-------|------------|
| audio | interview | Nahrajte rozhovor | `max-duration=120` |

`max-duration` je v sekundách. Záznam se automaticky zastaví po dosažení limitu.

### Nastavení kvality

Kvalita záznamu může být nastavena přes `parameters`:

| type | name | label | parameters |
|------|------|-------|------------|
| audio | feedback | Nahrajte zpětnou vazbu | `quality=normal` |

Podporované hodnoty: `low`, `normal` (výchozí), `voice-only`. `voice-only` optimalizuje pro mluvený zvuk s redukcí šumu.

## Příklad použití

### S maximální délkou a nápovědou

| type | name | label | hint | parameters |
|------|------|-------|------|------------|
| audio | story | Vyprávějte nám o incidentu svými slovy | Mluvte jasně. Nahrávání se zastaví po 3 minutách. | `max-duration=180` |

### Podmíněné audio — pouze pokud byl nahlášen problém

| type | name | label | relevant | required |
|------|------|-------|----------|----------|
| select_one yesno | issue_found | Byl nalezen problém? | | |
| audio | issue_audio | Nahrajte popis problému | `${issue_found} = 'yes'` | `${issue_found} = 'yes'` |

## Osvědčené postupy

1. Jasně uveďte v `label` nebo `hint`, co by měl enumerátor říci a jak dlouho.
2. Používejte `max-duration` pro prevenci příliš velkých souborů v oblastech s pomalým připojením.
3. Informujte respondenty před zahájením nahrávání — neočekávané nahrávání může vyvolat obavy o soukromí.
4. Testujte nahrávání na cílovém zařízení a síťových podmínkách před nasazením.
5. Nastavte `quality=voice-only` pro nahrávání ve stylu rozhovoru pro snížení velikosti souboru bez ztráty srozumitelnosti.

## Omezení

- Zvukové soubory mohou být velké (2minutový záznam při normální kvalitě je ~2–4 MB).
- Ne všechny prohlížeče podporují MediaRecorder API — Chrome a Firefox fungují spolehlivě; Safari na starších verzích iOS může mít problémy.
- Přepis zvukových odpovědí vyžaduje dodatečné zpracování (ruční nebo automatizovaný převod řeči na text).
- Předpisy o ochraně soukromí mohou omezovat nahrávání hlasů — ověřte místní požadavky na ochranu dat.
