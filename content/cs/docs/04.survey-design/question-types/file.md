---
title: "Soubor"
description: "Otázky file umožňují respondentům nahrávat dokumenty a jiné soubory jako součást jejich odpovědí na průzkum."
icon: "upload_file"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 230
---

Typ otázky `file` umožňuje respondentům **nahrát jakýkoli soubor** ze svého zařízení — dokumenty, tabulky, PDF nebo jiné typy souborů. Na rozdíl od `image`, `audio` a `video`, které spouštějí specifické nástroje pro zachycení, `file` otevírá obecný výběr souborů.

## Základní specifikace XLSForm

| type | name      | label                        |
|------|-----------|------------------------------|
| file | document  | Prosím nahrajte svůj dokument  |

## Použití

Otázky file se běžně používají pro:

1. Sběr podpůrných dokumentů (účtenky, certifikáty, smlouvy, zprávy)
2. Nahrávání vyplněných papírových formulářů, které byly naskenovány
3. Shromažďování tabulek nebo datových exportů z jiných systémů
4. Jakýkoli typ digitálního souboru, který image/audio/video nepokrývá

## Formát dat

Nahrané soubory jsou uloženy jako binární přílohy:

- **Formát:** Zachován v původním formátu (PDF, XLSX, DOCX atd.)
- **Pojmenování:** `{instanceID}-{fieldname}.{extension}`
- **Úložiště:** Nahráno do mediální složky serveru spolu s odesláním
- **Přístup:** Ke stažení z rozhraní správy odeslání

## Rozšíření rtSurvey

### Přijímané typy souborů

Použijte sloupec `parameters` pro omezení výběru typů souborů:

| type | name | label | parameters |
|------|------|-------|------------|
| file | report | Nahrajte inspekční zprávu | `accept=.pdf` |
| file | spreadsheet | Nahrajte datový soubor | `accept=.xlsx,.csv` |

Parametr `accept` používá standardní syntaxi přípon souborů (oddělené čárkami).

### Pokyny k velikosti souboru

rtSurvey nevynucuje pevný limit velikosti souboru na úrovni otázky, ale platí limit nahrání serveru. Používejte `hint` pro sdělení očekávání enumerátorovi:

| type | name | label | hint |
|------|------|-------|------|
| file | receipt | Nahrajte potvrzení o platbě | Přijímáno: PDF nebo obrázek. Maximální velikost souboru: 5 MB |

## Příklad použití

### Povinné nahrání PDF

| type | name | label | hint | required | required_message |
|------|------|-------|------|----------|-----------------|
| file | signed_consent | Nahrajte podepsaný formulář souhlasu | Pouze PDF, max 2 MB | yes | Je vyžadován formulář souhlasu |

### Podmíněné nahrání dokumentu

| type | name | label | relevant |
|------|------|-------|----------|
| select_one yesno | has_land_title | Má domácnost pozemkový titul? | |
| file | land_title_doc | Nahrajte fotografii nebo sken pozemkového titulu | `${has_land_title} = 'yes'` |

## Osvědčené postupy

1. Použijte `accept` pro omezení typů souborů — zabraňuje enumerátorům náhodně nahrát nesprávné soubory.
2. Vždy zahrňte pokyny k velikosti a formátu do sloupce `hint`.
3. Pro fotografie a obrázky používejte typ `image` — nabízí lepší kompresi a konzistentní zpracování formátu.
4. Pro velké průzkumy s přílohami souborů plánujte ukládání dat a šířku pásma pro stahování.
5. Testujte výběr souborů na cílovém typu zařízení (Android vs. iOS vs. web) před nasazením.

## Omezení

- Otázky file nevalidují obsah souboru — pouze kontrola přípony souboru přes `accept` je vynucena na úrovni UI.
- Velmi velké soubory (100 MB+) mohou při nahrávání v prostředí s nízkým připojením vypršet.
- Offline enumerátoři mohou soubory připojit, ale nebudou nahrány, dokud není obnoveno připojení.
- Některé konfigurace zařízení omezují přístup k určitým místům úložiště.
