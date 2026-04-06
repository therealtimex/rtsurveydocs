---
title: "Tipo di domanda dinamico"
description: "Il tipo di domanda dinamico consente di determinare il tipo di domanda e il widget di un campo in fase di esecuzione in base a una risposta API o a un valore calcolato."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 301
---

La funzionalità **Tipo di domanda dinamico** consente al widget di input di un campo e al suo comportamento di validazione di essere determinati **in fase di esecuzione** piuttosto che al momento della progettazione del modulo. Questa è un'estensione avanzata di rtSurvey usata quando il tipo di dati da raccogliere dipende da una configurazione lato server, dalla risposta API o dal valore di un campo precedente.

Un caso d'uso comune è una checklist di ispezione configurabile dove il server definisce quali campi sono richiesti, che tipo sono (testo, integer, select, ecc.) e quali opzioni sono disponibili — senza ricostruire il modulo per ogni configurazione.

---

## Come funziona

Un campo contrassegnato come tipo di domanda dinamico usa `callapi()` per recuperare la sua configurazione da un'API. La risposta API definisce:

- Il tipo di input da renderizzare (text, integer, select_one, ecc.)
- Le scelte disponibili (per i tipi di selezione)
- Le regole di validazione

Il campo è contrassegnato con `specialFeature: isDynamicQuestionType` internamente, il che dice al motore del modulo di usare la risposta API per costruire il widget piuttosto che la definizione statica del modulo.

---

## Configurazione

### Passaggio 1: Recupera la configurazione del campo

Usa un campo `calculate` con `callapi()` per recuperare la configurazione dinamica:

| type | name | label | appearance | calculation |
|------|------|-------|------------|-------------|
| calculate | field_config | | callapi | `callapi('POST', 'https://api.example.com/field-config', 1, 2, 0, '$.config', 10000, 0, '', '', '{"form_id": "##form_id##", "field_id": "inspection_result"}')` |

### Passaggio 2: Fai riferimento alla configurazione nel campo dinamico

Il campo dinamico usa `callapi-verify()` nella sua `appearance` o `constraint` per collegarsi alla configurazione recuperata:

| type | name | label | appearance |
|------|------|-------|------------|
| text | inspection_result | Risultato ispezione | `callapi-verify(dynamicParams)` |

Il motore del modulo legge `field_config` e determina dinamicamente se renderizzare `inspection_result` come campo `text`, `integer` o `select_one`.

---

## Formato della risposta API

L'API dovrebbe restituire un oggetto JSON che descrive la configurazione del campo. Una risposta tipica:

```json
{
  "config": {
    "type": "select_one",
    "choices": [
      {"value": "pass", "label": "Superato"},
      {"value": "fail", "label": "Non superato"},
      {"value": "na", "label": "N/A"}
    ],
    "required": true,
    "constraint": ". != ''"
  }
}
```

---

## Esempio: Modulo di ispezione configurabile

Un modulo di ispezione in cui le voci della checklist e i loro tipi di risposta vengono recuperati da un server in base alla categoria di ispezione:

| type | name | label | appearance | calculation |
|------|------|-------|------------|-------------|
| select_one inspection_type | insp_type | Tipo di ispezione | | |
| calculate | checklist_config | | callapi | `callapi('POST', 'https://api.example.com/checklist', 1, 2, 0, '$.items', 10000, 0, '', '', '{"type": "##insp_type##"}')` |
| text | item_1 | Voce 1 | `callapi-verify(dynamicParams)` | |
| text | item_2 | Voce 2 | `callapi-verify(dynamicParams)` | |
| text | item_3 | Voce 3 | `callapi-verify(dynamicParams)` | |

Il server restituisce il tipo di widget corretto, l'etichetta, le scelte e la validazione per ogni voce in base a `insp_type`.

---

## Best practice

1. Usa i tipi di domanda dinamici solo quando la struttura del campo varia genuinamente in fase di esecuzione — per i moduli statici, usa i tipi di domanda standard.
2. Assicurati che l'API di configurazione risponda rapidamente (entro 2 secondi) e sia disponibile sulla rete del campo.
3. Definisci sempre un fallback ragionevole nel modulo per il caso in cui l'API non sia raggiungibile — un campo `text` semplice con una nota è meglio di un widget rotto.
4. Versiona lo schema della risposta API — i cambiamenti al formato della risposta influenzeranno tutti i moduli attivi che usano quell'endpoint.
5. Testa ogni combinazione di tipi di campo che l'API potrebbe restituire prima del deployment.

## Limitazioni

- I tipi di domanda dinamici richiedono connettività di rete per recuperare la configurazione.
- La gamma completa di tipi di widget disponibili dinamicamente dipende dalla versione del client rtSurvey — testa la tua versione di destinazione.
- Questa è un'estensione avanzata di rtSurvey senza equivalente nella specifica XLSForm standard.
- Gli errori di debug sono più difficili da tracciare poiché la definizione del campo si trova in parte nel modulo e in parte nella risposta API.
