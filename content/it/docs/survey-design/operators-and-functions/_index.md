---
title: "Operatori e Funzioni"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 290
---

Le espressioni in rtSurvey sono scritte in un sottoinsieme di **XPath 1.0**, esteso con funzioni JavaRosa/ODK e funzioni personalizzate di rtSurvey. Le espressioni vengono utilizzate nelle colonne `calculate`, `constraint`, `relevant`, `required` e `default` del tuo XLSForm.

## Riferimento ai valori dei campi

Usa `${fieldname}` per fare riferimento al valore di un altro campo:

```
${age} > 18
```

Usa `.` (un singolo punto) per fare riferimento al **valore del campo corrente** — comunemente usato nelle espressioni `constraint`:

```
. >= 0 and . <= 100
```

Usa `..` per fare riferimento al gruppo padre (utilizzo avanzato nei repeat).

## Sintassi delle espressioni

Le espressioni seguono le regole standard di XPath:

- Le **stringhe** devono essere racchiuse tra virgolette singole: `'yes'`
- I **numeri** vengono scritti così come sono: `42`, `3.14`
- I risultati **booleani** vengono usati per `relevant`, `required` e `constraint` — qualsiasi valore non vuoto e non zero è considerato vero
- Gli spazi bianchi vengono ignorati intorno agli operatori

{{% alert icon=" " context="warning" %}}
Usa sempre virgolette diritte (`'` o `"`) — mai "smart quotes" (virgolette curve). Gli editor di testo formattato spesso convertono automaticamente le virgolette e romperanno le tue espressioni.
{{% /alert %}}

## Sezioni di questo capitolo

- **[Operatori](operators)** — operatori di confronto (`=`, `!=`, `>`, `<`, `>=`, `<=`) e operatori logici (`and`, `or`, `not()`)
- **[Funzioni](functions)** — funzioni stringa, selezione, numero, data/ora, booleane, geografiche e di utilità
- **[Riferimenti](references)** — come fare riferimento ai campi e ai valori di contesto

## Esempi rapidi

| Caso d'uso | Espressione |
|----------|------------|
| Mostra se l'età è superiore a 18 | `${age} > 18` |
| Mostra solo se è stato selezionato "sì" | `${consent} = 'yes'` |
| Richiesto se un altro campo non è vuoto | `${name} != ''` |
| Calcola il totale | `${adults} + ${children}` |
| Concatena il nome | `concat(${first_name}, ' ', ${last_name})` |
| Data odierna | `today()` |
| Controlla se un'opzione è stata selezionata | `selected(${interests}, 'sports')` |
