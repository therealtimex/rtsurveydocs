---
title: "Validering av svar"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 270
---

En måte å sikre datakvalitet på er å legge til begrensninger på datafeltene i skjemaet. Begrensninger bidrar til å hindre brukere fra å skrive inn ugyldige eller umulige svar. For eksempel, når du spør om en persons inntekt, ønsker du å unngå urealistiske verdier, som negative tall eller ekstremt høye verdier. Det er enkelt å legge til databegrensninger i skjemaet. Følg bare trinnene nedenfor:

1. Legg til en ny kolonne kalt "constraint" i skjemaet.
2. I "constraint"-kolonnen skriver du inn en formel som angir grensene for svaret.

### Eksempel

La oss se på et eksempel der vi ønsker å legge til en begrensning for personens inntekt. Begrensningen krever at inntekten er mellom $0 og $1 000 000. Slik kan du sette opp begrensningen:

{{< table >}}
| `name`      | `constraint`                  |
|---------------|-----------------------------|
| Income        | . >= 0 & . <= 1000000      |
{{< /table >}}

I eksemplet ovenfor refererer "." i formelen tilbake til spørsmålsvariabelen, som representerer verdien som brukeren angav for "Income"-spørsmålet. Begrensningen ". >= 0 && . <= 1000000" sikrer at den angitte inntekten er større enn eller lik 0 og mindre enn eller lik 1 000 000.


### Hard begrensning

En **hard begrensning** blokkerer skjemainnsending helt dersom den angitte verdien ikke oppfyller uttrykket. Telleren kan ikke gå videre før en gyldig verdi er angitt.

For å legge til en hard begrensning, skriv inn uttrykket i `constraint`-kolonnen. Du kan eventuelt legge til en menneskevennlig melding i `constraint_message`:

{{< table >}}
| `type` | `name` | `label` | `constraint` | `constraint_message` |
|--------|--------|---------|--------------|----------------------|
| integer | age | Respondentens alder | `. > 0 and . <= 120` | Alderen må være mellom 1 og 120 |
| decimal | temperature | Kroppstemperatur (°C) | `. >= 35 and . <= 42` | Temperaturen må være mellom 35°C og 42°C |
| text | phone | Telefonnummer | `regex(., '^[0-9]{10}$')` | Skriv inn et 10-sifret telefonnummer |
{{< /table >}}

#### Flere betingelser

Kombiner betingelser med `and` / `or`:

```
. >= 0 and . <= 100
```

```
. = 'yes' or . = 'no'
```

#### Bruke `regex()` for mønstervalidering

Funksjonen `regex(value, pattern)` tester en verdi mot et regulært uttrykk:

{{< table >}}
| `type` | `name` | `label` | `constraint` | `constraint_message` |
|--------|--------|---------|--------------|----------------------|
| text | email | E-postadresse | `regex(., '^[^@]+@[^@]+\.[^@]+$')` | Skriv inn en gyldig e-postadresse |
| text | zip_code | Postnummer | `regex(., '^[0-9]{5}$')` | Skriv inn et 5-sifret postnummer |
{{< /table >}}

#### Referere til andre felt i en begrensning

Bruk `${feltnavn}` for å referere til verdier fra andre spørsmål:

{{< table >}}
| `type` | `name` | `label` | `constraint` | `constraint_message` |
|--------|--------|---------|--------------|----------------------|
| integer | end_year | Sluttår | `. >= ${start_year}` | Sluttåret må være etter startåret |
| decimal | loan_repaid | Tilbakebetalt beløp | `. <= ${loan_amount}` | Kan ikke tilbakebetale mer enn lånebeløpet |
{{< /table >}}

### Myk varsling

En **myk varsling** (også kalt myk begrensning eller advarsel) advarer telleren om at en verdi ser uvanlig ut, men lar dem fortsatt gå videre. Dette er nyttig når en verdi er teknisk gyldig, men statistisk usannsynlig.

rtSurvey støtter myke varsler ved å bruke `constraint`-kolonnen med en spesiell `constraint_type`-tilnærming, eller via utseendet `soft` kombinert med et note-felt.

Det vanligste mønsteret er å bruke en **note** med et `relevant`-uttrykk som flagger den mistenkelige verdien, kombinert med et **acknowledge**-spørsmål for å bekrefte:

{{< table >}}
| `type` | `name` | `label` | `relevant` |
|--------|--------|---------|------------|
| integer | children | Antall barn | |
| note | children_warning | Advarsel: Du angav ${children} barn. Bekreft at dette er korrekt. | `. > 15` |
| trigger | children_confirm | Bekreft at antall barn er korrekt | `${children} > 15` |
{{< /table >}}

#### Myk varsling med constraint_message

For en enklere myk advarsel kan du utforme begrensningen til å advare om ekstreme verdier, men fortsatt tillate et bredt område:

{{< table >}}
| `type` | `name` | `label` | `constraint` | `constraint_message` |
|--------|--------|---------|--------------|----------------------|
| integer | children | Antall barn | `. >= 0 and . <= 30` | Denne verdien virker veldig høy. Vennligst verifiser. |
{{< /table >}}

{{% alert icon=" " context="warning" %}}
Skillet mellom harde og myke begrensninger er viktig for datakvaliteten. Bruk **harde begrensninger** for logisk umulige verdier (negative aldre, temperaturer over 100°C). Bruk **myke varsler** for statistisk usannsynlige, men ikke umulige verdier — du ønsker ikke å blokkere legitime kanttilfeller.
{{% /alert %}}
