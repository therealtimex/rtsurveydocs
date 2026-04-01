---
title: "HTML stylování"
description: "rtSurvey podporuje HTML tagy v popisках a nápovědách, umožňující formátování textu, odkazy a dynamické barevné témata."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 297
---

rtSurvey vykresluje text **popisku** a **nápovědy** jako HTML ve webových formulářích. To znamená, že můžete používat standardní HTML tagy pro formátování textu, přidávání zalomení řádků, vytváření odkazů a aplikaci barev. To je zvláště užitečné pro pole poznámek, instrukce sekcí a dynamické souhrny.

{{% alert icon=" " context="warning" %}}
HTML v popisках je vykreslováno ve **webovém formuláři** a mobilních aplikacích rtSurvey. Nemusí se vykreslovat ve všech klientech kompatibilních s ODK. Vždy testujte na cílové platformě.
{{% /alert %}}

---

## Podporované HTML tagy

### Formátování textu

| Tag | Výsledek |
|-----|---------|
| `<strong>text</strong>` nebo `<b>text</b>` | **Tučný text** |
| `<em>text</em>` nebo `<i>text</i>` | *Kurzíva* |
| `<u>text</u>` | Podtržený text |
| `<br>` | Zalomení řádku |
| `<span style="...">text</span>` | Inline stylování |

### Odkazy

```html
<a href="https://example.com" target="_blank">Klikněte zde</a>
```

Otevírá se v nové záložce. Použijte pro referenční dokumenty, pokyny nebo externí zdroje, které by enumerátor měl konzultovat.

### Barvy

Použijte `<span>` s inline styly:

```html
<span style="color: red;">Varování: hodnota je mimo rozsah</span>
<span style="color: #009688;">Sekce dokončena</span>
```

---

## Proměnné barevného tématu

rtSurvey podporuje **tokeny barevného tématu**, které se přizpůsobují nakonfigurovanému tématu aplikace. Použijte syntaxi `__COLOR_THEME_NAME__`:

```html
<span style="color: var(--color-theme-primary);">Text primární barvy</span>
```

Nebo pomocí zkráceného tokenu v textu popisku:

```
<font color="var(--COLOR_THEME_PRIMARY)">Důležitá poznámka</font>
```

To je automaticky převedeno na ekvivalentní `<span>` s CSS proměnnou při vykreslování.

---

## Vícejazyčné popisky

Obalte obsah do jazykových tagů pro podporu více jazyků v jedné buňce popisku:

```
<en>Enter the household size</en><vi>Nhập quy mô hộ gia đình</vi>
```

rtSurvey extrahuje obsah odpovídající aktuálnímu jazyku aplikace. Pokud není nalezen odpovídající jazykový tag, zobrazí se celý řetězec tak, jak je.

---

## Příklady v polích poznámek

### Instrukce sekce s tučným textem a zalomením řádku

| type | name | label |
|------|------|-------|
| note | section_intro | `<strong>Sekce 3: Využití půdy</strong><br>Všechny otázky v této sekci pokládejte pouze vedoucímu domácnosti.` |

### Dynamický souhrn s odkazem na výpočet

| type | name | label |
|------|------|-------|
| calculate | total | | `${adults} + ${children}` |
| note | summary | `Celkový počet členů domácnosti: <strong>${total}</strong><br><span style="color: gray;">Dospělí: ${adults} · Děti: ${children}</span>` |

### Varování červenou barvou

| type | name | label | relevant |
|------|------|-------|----------|
| note | age_warning | `<span style="color: red;"><strong>Varování:</strong> Zadaný věk (${age}) je neobvykle vysoký. Prosím ověřte.</span>` | `${age} > 100` |

### Odkaz na referenční dokument

| type | name | label |
|------|------|-------|
| note | guidelines_link | `Před zahájením této sekce si přečtěte <a href="https://docs.example.com/guidelines" target="_blank">Terénní pokyny</a>.` |

---

## Speciální HTML tagy rtSurvey

### `<webbox src='url' title='title'>...</webbox>`

Vloží tlačítko, které otevře URL v modálním okně uvnitř formuláře. Viz [Webbox](webbox) pro podrobnosti.

### `<delete-repeat-current>popisek</delete-repeat-current>`

Vykreslí tlačítko uvnitř skupiny opakování, které smaže aktuální instanci opakování po klepnutí.

### `<delete-repeat-last>popisek</delete-repeat-last>`

Vykreslí tlačítko, které smaže poslední instanci opakování.

Příklad použití ve skupině opakování:

| type | name | label |
|------|------|-------|
| note | delete_btn | `<delete-repeat-current>Odebrat tohoto člena</delete-repeat-current>` |

---

## Osvědčené postupy

1. Používejte HTML střídmě — přeformátované popisky jsou těžší ke čtení, ne snazší.
2. Upřednostňujte `<strong>` pro tučný text a `<em>` pro kurzívu před zastaralými `<b>` a `<i>`.
3. Udržujte použití barev smysluplné — používejte červenou pro varování, nikoli pro dekoraci.
4. Vždy testujte vykreslování HTML na mobilní aplikaci i webovém formuláři, protože vykreslování se může mírně lišit.
5. Vyhněte se tagům `<table>` uvnitř popisků — na mobilních obrazovkách se zřídka vykreslují dobře.
6. Nepoužívejte JavaScript (`<script>`) — bude odstraněn nebo způsobí chyby.

## Omezení

- Komplexní HTML (tabulky, formuláře, skripty) není podporováno a může narušit vykreslování.
- Některé starší mobilní klienty mohou zobrazovat HTML tagy jako doslovný text — testujte na všech cílových zařízeních.
- Odkazy `<a>` se otevírají v prohlížeči nebo WebView — enumerátor opustí formulář, což může být rušivé na mobilních zařízeních.
