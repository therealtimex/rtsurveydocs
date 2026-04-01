---
title: "Operatorer och funktioner"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 290
---

Uttryck i rtSurvey skrivs i en delmängd av **XPath 1.0**, utökad med JavaRosa/ODK-funktioner och anpassade rtSurvey-funktioner. Du använder uttryck i kolumnerna `calculate`, `constraint`, `relevant`, `required` och `default` i ditt XLSForm.

## Referera till fältvärden

Använd `${fieldname}` för att referera till värdet av ett annat fält:

```
${age} > 18
```

Använd `.` (en enda punkt) för att referera till **det aktuella fältets värde** — används vanligtvis i `constraint`-uttryck:

```
. >= 0 and . <= 100
```

Använd `..` för att referera till den överordnade gruppen (avancerad användning i upprepningar).

## Uttryckssyntax

Uttryck följer standard-XPath-regler:

- **Strängar** måste omges med enkla citationstecken: `'yes'`
- **Tal** skrivs som de är: `42`, `3.14`
- **Boolean**-resultat används för `relevant`, `required` och `constraint` — alla värden som inte är tomma och inte är noll är sanna
- Blanksteg ignoreras runt operatorer

{{% alert icon=" " context="warning" %}}
Använd alltid raka citationstecken (`'` eller `"`) — aldrig "smarta citationstecken" (böjda). Textredigerare konverterar ofta citationstecken automatiskt och bryter dina uttryck.
{{% /alert %}}

## Avsnitt i detta kapitel

- **[Operatorer](operators)** — jämförelseoperatorer (`=`, `!=`, `>`, `<`, `>=`, `<=`) och logiska operatorer (`and`, `or`, `not()`)
- **[Funktioner](functions)** — sträng-, urvals-, tal-, datum/tid-, boolean-, geo- och verktygsfunktioner
- **[Referenser](references)** — hur man refererar till fält och kontextvärden

## Snabba exempel

| Användningsfall | Uttryck |
|-----------------|---------|
| Visa om ålder är över 18 | `${age} > 18` |
| Visa bara om "yes" valdes | `${consent} = 'yes'` |
| Kräv om ett annat fält inte är tomt | `${name} != ''` |
| Beräkna totalt | `${adults} + ${children}` |
| Sammansätt namn | `concat(${first_name}, ' ', ${last_name})` |
| Dagens datum | `today()` |
| Kontrollera om alternativ valdes | `selected(${interests}, 'sports')` |
