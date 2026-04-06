---
title: "Immagini avanzate"
description: "Funzionalità avanzate per le immagini in rtSurvey: filigrana, visualizzazione griglia media e annotazioni sulle immagini."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 300
---

Oltre al tipo di domanda `image` standard, rtSurvey fornisce estensioni per la **filigrana** delle foto acquisite e la visualizzazione di più immagini in una **griglia multimediale**. Queste sono utili per i sondaggi basati su prove dove le foto devono essere contrassegnate con l'identità dell'intervistatore o i metadati del sondaggio, e per le interfacce di revisione visiva.

---

## Filigrana

La funzionalità filigrana sovrappone testo o un'immagine a una foto acquisita prima che venga archiviata. Viene usata per contrassegnare le foto sul campo con la data, il nome dell'intervistatore, la posizione GPS o qualsiasi altro dato del sondaggio — rendendo più difficile presentare foto preesistenti come prove acquisite di recente.

### Configurazione

Usa `watermark()` nella colonna **`calculation`** di un campo `image`, combinato con l'appearance `callapi`:

```
watermark(type, size, distance, color, shadow, rotate, blur)
```

| Parametro | Descrizione |
|-----------|-------------|
| `type` | `'text'` per una filigrana testuale; `'file'` per una filigrana immagine |
| `size` | Dimensione del font in pixel (testo) o dimensione della filigrana come % della larghezza dell'immagine (file) |
| `distance` | Spaziatura tra le tessere della filigrana ripetuta (pixel) |
| `color` | Colore del testo (colore CSS o hex). Non usato per il tipo `file` |
| `shadow` | Colore dell'ombra (colore CSS o hex) |
| `rotate` | Angolo di rotazione in gradi (es. `45` per diagonale) |
| `blur` | Opacità della filigrana (0 = invisibile, 100 = completamente opaca) |

### Esempio di filigrana testuale

Sovrapponi il nome dell'intervistatore e la data odierna diagonalmente su ogni foto acquisita:

| type | name | label | appearance | calculation |
|------|------|-------|------------|-------------|
| calculate | wm_text | | | `concat(pulldata('app-api', 'user.name'), ' | ', format-date(today(), '%d/%m/%Y'))` |
| image | site_photo | Scatta una foto del sito | watermark | `watermark('text', 20, 60, '#ffffff', '#000000', 45, 40)` |

Il testo della filigrana viene preso da `${wm_text}`. Imposta il campo del testo della filigrana **prima** del campo immagine nel modulo.

### Esempio di filigrana immagine/logo

Sovrapponi il logo di un'organizzazione (allegato come file multimediale denominato `logo.png`):

| type | name | label | appearance | calculation |
|------|------|-------|------------|-------------|
| image | evidence_photo | Scatta una foto della prova | watermark | `watermark('file', 25, 80, '', '#000000', 0, 50)` |

### Annulla/Ripristina

L'editor della filigrana supporta annulla e ripristina — gli intervistatori possono tornare indietro nella cronologia delle modifiche prima di confermare la foto.

### Tassellatura della filigrana

La filigrana si ripete (tassellatura) sull'intera immagine automaticamente. Il parametro `distance` controlla la spaziatura tra le tessere; `rotate` controlla l'angolo di ogni tessera.

---

## Widget griglia multimediale

Il widget griglia multimediale mostra una raccolta di file multimediali (immagini, audio, video) in un layout a griglia, consentendo ai revisori o agli intervistatori di sfogliare visivamente i file acquisiti.

Questo widget viene attivato dall'appearance `mediagridwidget` ed è tipicamente usato su campi `note` o `calculate` per mostrare i media precedentemente acquisiti da un gruppo di ripetizioni.

### Esempio: Mostra tutte le foto da una ripetizione come griglia

| type | name | label | appearance | calculation |
|------|------|-------|------------|-------------|
| calculate | photo_list | | | `join(' ', ${site_photo})` |
| note | photo_review | Rivedi le foto acquisite | mediagridwidget | |

---

## Best practice per le foto con filigrana

1. Calcola sempre il testo della filigrana in un campo `calculate` **sopra** il campo immagine in modo che sia disponibile quando viene scattata la foto.
2. Usa un angolo di rotazione (es. 45°) per rendere le filigrane più difficili da ritagliare.
3. Imposta l'opacità (`blur`) tra 30–60% — abbastanza alta da essere leggibile, abbastanza bassa da non oscurare il soggetto della foto.
4. Includi il nome dell'intervistatore, la data e le coordinate GPS nel testo della filigrana per massimizzare il valore di audit.
5. Testa il rendering della filigrana sul dispositivo con le specifiche più basse nella tua flotta — la filigrana basata su canvas può essere lenta su hardware più vecchio.

## Limitazioni

- La filigrana viene applicata lato client usando l'API Canvas HTML5 — richiede un browser o WebView capace.
- Le foto ad altissima risoluzione possono richiedere diversi secondi per essere filigranate su dispositivi di fascia bassa.
- Le filigrane sono incorporate nel file immagine — non possono essere rimosse dopo l'invio senza editing dell'immagine.
- Il tipo di filigrana `file` richiede che l'immagine del logo sia allegata come file multimediale con esattamente il nome del file previsto.
