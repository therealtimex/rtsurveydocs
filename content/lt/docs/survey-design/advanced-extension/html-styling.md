---
title: "HTML stilizavimas"
description: "rtSurvey palaiko HTML žymes etiketėse ir patarimuose, leidžiančias formatuoti turtingą tekstą, nuorodas ir dinaminę spalvų tematiką."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 297
---

rtSurvey vaizduoja **etikečių** ir **patarimų** tekstą kaip HTML žiniatinklio formose. Tai reiškia, kad galite naudoti standartinius HTML žymas tekstui formatuoti, pridėti eilučių lūžius, kurti nuorodas ir taikyti spalvas. Tai ypač naudinga pastabų laukams, sekcijų instrukcijoms ir dinaminiams suvestinėms.

{{% alert icon=" " context="warning" %}}
HTML etiketėse atvaizduojamas **žiniatinklio formoje** ir rtSurvey mobiliose programose. Jis gali ne atvaizduotis visuose ODK suderintuose klientuose. Visada testuokite tikslinėje platformoje.
{{% /alert %}}

---

## Palaikomos HTML žymos

### Teksto formatavimas

| Žymė | Rezultatas |
|-----|--------|
| `<strong>tekstas</strong>` arba `<b>tekstas</b>` | **Paryškintas tekstas** |
| `<em>tekstas</em>` arba `<i>tekstas</i>` | *Kursyvinis tekstas* |
| `<u>tekstas</u>` | Pabrauktas tekstas |
| `<br>` | Eilutės lūžis |
| `<span style="...">tekstas</span>` | Inline stilizavimas |

### Nuorodos

```html
<a href="https://example.com" target="_blank">Spustelėkite čia</a>
```

Atidaro naujame skirtuke. Naudokite nuorodoms į atskaitos dokumentus, rekomendacijas ar išorinius išteklius, kurių surašytojas turėtų ieškoti.

### Spalvos

Naudokite `<span>` su inline stiliais:

```html
<span style="color: red;">Įspėjimas: reikšmė yra už diapazono ribų</span>
<span style="color: #009688;">Sekcija baigta</span>
```

---

## Spalvų temos kintamieji

rtSurvey palaiko **spalvų temos žetonus**, kurie prisitaiko prie sukonfigūruotos programos temos. Naudokite sintaksę `__COLOR_THEME_NAME__`:

```html
<span style="color: var(--color-theme-primary);">Pagrindinis spalvos tekstas</span>
```

Arba naudodami žetono trumpinį etikečių tekste:

```
<font color="var(--COLOR_THEME_PRIMARY)">Svarbi pastaba</font>
```

Tai automatiškai konvertuojama į atitinkamą `<span>` su CSS kintamuoju atvaizdavimo metu.

---

## Daugiakalbės etiketės

Apvyniokite turinį kalbų žymomis, kad palaikytumėte kelias kalbas viename etikečių laukelyje:

```
<en>Enter the household size</en><vi>Nhập quy mô hộ gia đình</vi>
```

rtSurvey išskiria turinį, atitinkantį dabartinę programos kalbą. Jei atitinkanti kalbų žymė nerasta, rodoma pilna eilutė tokia, kokia yra.

---

## Pavyzdžiai pastabų laukuose

### Sekcijos instrukcija su paryškintu tekstu ir eilutės lūžiu

| type | name | label |
|------|------|-------|
| note | section_intro | `<strong>3 sekcija: Žemės naudojimas</strong><br>Visus šios sekcijos klausimus užduokite tik namų ūkio vadovui.` |

### Dinaminis suvestinis su skaičiavimo nuoroda

| type | name | label |
|------|------|-------|
| calculate | total | | `${adults} + ${children}` |
| note | summary | `Bendras namų ūkio narių skaičius: <strong>${total}</strong><br><span style="color: gray;">Suaugusieji: ${adults} · Vaikai: ${children}</span>` |

### Perspėjimas raudonai

| type | name | label | relevant |
|------|------|-------|----------|
| note | age_warning | `<span style="color: red;"><strong>Įspėjimas:</strong> Įvestas amžius (${age}) yra neįprastai didelis. Prašome patikrinti.</span>` | `${age} > 100` |

### Nuoroda į atskaitos dokumentą

| type | name | label |
|------|------|-------|
| note | guidelines_link | `Prieš pradėdami šią sekciją, skaitykite <a href="https://docs.example.com/guidelines" target="_blank">Lauko rekomendacijas</a>.` |

---

## Specialios rtSurvey HTML žymos

### `<webbox src='url' title='pavadinimas'>...</webbox>`

Įterpia mygtuką, kuris atidaro URL formos viduje esančiame modaliame lange. Žr. [Webbox](webbox) daugiau informacijos.

### `<delete-repeat-current>etiketė</delete-repeat-current>`

Atvaizduoja mygtuką kartojimų grupės viduje, kuris ištrina dabartinį kartojimo egzempliorių, kai paspaudžiamas.

### `<delete-repeat-last>etiketė</delete-repeat-last>`

Atvaizduoja mygtuką, kuris ištrina paskutinį kartojimo egzempliorių.

Naudojimo pavyzdys kartojimų grupėje:

| type | name | label |
|------|------|-------|
| note | delete_btn | `<delete-repeat-current>Pašalinti šį narį</delete-repeat-current>` |

---

## Geriausios praktikos

1. Naudokite HTML taupiai — performatuotos etiketės yra sunkiau skaitomos, o ne lengviau.
2. Pirmenybę teikite `<strong>` paryškinimui ir `<em>` kursyvui vietoj pasenusių `<b>` ir `<i>`.
3. Laikykite spalvų naudojimą prasmingas — naudokite raudoną perspėjimams, o ne dekoracijai.
4. Visada testuokite HTML atvaizdavimą tiek mobiliojoje programoje, tiek žiniatinklio formoje, nes atvaizdavimas gali šiek tiek skirtis.
5. Venkite `<table>` žymų etiketėse — jos retai gerai atvaizduojamos mobiliuosiuose ekranuose.
6. Nenaudokite JavaScript (`<script>`) — jis bus pašalintas arba sukels klaidas.

## Apribojimai

- Sudėtingas HTML (lentelės, formos, skriptai) nepalaikomas ir gali sugadinti atvaizdavimą.
- Kai kurie senesni mobilieji klientai gali rodyti HTML žymas kaip pažodinį tekstą — testuokite visuose tikslinių įrenginiuose.
- `<a>` nuorodos atidaro naršyklėje arba WebView — surašytojas palieka formą, o tai gali būti trukdantis mobiliuosiuose.
