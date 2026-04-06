---
title: "Vícejazyčná podpora"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 285
---

rtSurvey poskytuje robustní vícejazyčnou podporu, která vám umožňuje vytvářet průzkumy ve více jazycích. Tato funkce je klíčová pro provádění výzkumu v různých jazykových populacích nebo vícejazyčném prostředí.

## Nastavení vícejazyčných průzkumů

Pro vytvoření vícejazyčného průzkumu v rtSurvey musíte do XLSForm přidat sloupce specifické pro jazyk. Zde je postup:

1. **Překlady popisků**: Přidejte sloupce pro každý jazyk ve formátu `label::Language (code)`.
2. **Překlady nápovědy**: Použijte `hint::Language (code)` pro překlad nápovědy.
3. **Překlady mediálních souborů**: Pro média specifická pro jazyk použijte `media::Language (code)`.

Příklad:

```
| type    | name | label::English (en) | label::Czech (cs) | hint::English (en) | hint::Czech (cs) |
|---------|------|---------------------|-------------------|---------------------|------------------|
| integer | age  | How old are you?    | Kolik je vám let?  | Enter your age      | Zadejte svůj věk |
```

## Jazykové kódy

Doporučuje se používat oficiální 2-znakové jazykové kódy (subtags) za názvem jazyka. To usnadňuje shodu jazyka formuláře s jazykem uživatelského rozhraní. Oficiální kódy najdete [zde](https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry).

## Nastavení výchozího jazyka

Pro nastavení výchozího jazyka pro sběr dat použijte list `settings` ve vašem XLSForm:

```
| form_id   | version | default_language |
|-----------|---------|-------------------|
| test_form | 101     | Czech (cs)        |
```

## Funkce specifické pro rtSurvey

### Dynamické přepínání jazyků

rtSurvey umožňuje uživatelům dynamicky přepínat jazyky během sběru dat:

- Ve webovém rozhraní použijte rozevírací seznam jazyků v horní navigační liště.
- V mobilní aplikaci přistupte k možnostem jazyka přes nabídku nastavení.

### Vícejazyčné validační zprávy

rtSurvey rozšiřuje vícejazyčnou podporu na validační zprávy:

```
| type    | name | constraint | constraint_message::English (en) | constraint_message::Czech (cs) |
|---------|------|------------|----------------------------------|--------------------------------|
| integer | age  | . <= 150   | Age must be 150 or less          | Věk musí být 150 nebo méně     |
```

### Podpora jazyků RTL

Pro jazyky zprava doleva (RTL) jako arabština nebo hebrejština rtSurvey automaticky upraví rozvržení:

```
| type | name | label::English (en) | label::Arabic (ar) |
|------|------|---------------------|---------------------|
| text | name | Your name           | اسمك                |
```

## Osvědčené postupy

1. Vždy zahrnujte záložní jazyk (obvykle angličtinu) jako výchozí.
2. Používejte standardní jazykové kódy IANA pro kompatibilitu.
3. Testujte formulář v každém jazyce pro správné zobrazení znaků.
4. Zvažte délku textu v různých jazycích — překlady jsou často delší než originál.
5. Pro RTL jazyky zajistěte, aby UI bylo správně zrcadleno.

## Omezení

- Mediální soubory musí být duplikovány pro každý jazyk, pokud jsou odlišné.
- Výchozí jazyk, pokud není nastaven, je obvykle první definovaný jazyk ve formuláři.
- Některé starší klienty nemusí správně podporovat vícejazyčné formuláře.
