---
weight: 150
date: "2023-05-03T22:37:22+01:00"
draft: false
author: "RealTimeX"
title: "Raccolta dei dati"
icon: "rocket_launch"
toc: true
description: "Una guida rapida per condurre un sondaggio con rtSurvey"
publishdate: "2023-05-03T22:37:22+01:00"
tags: ["Beginners"]
---

Una volta che un modulo è stato distribuito e gli enumeratori sono stati assegnati, la raccolta dati può iniziare. **rtSurvey** supporta la raccolta dati senza interruzioni sia tramite browser web che tramite applicazioni mobili dedicate, garantendo flessibilità sia che il tuo team sia connesso a internet o lavori in ambienti remoti e offline.

## Scelta del metodo di raccolta appropriato

A seconda della geografia e della connettività del tuo progetto, puoi scegliere il metodo ottimale per i tuoi enumeratori:

- **Browser Web (Online):** Ideale per call center, immissione dati in ufficio, o rispondenti che compilano sondaggi pubblici autogestiti.
- **rtWork / App mobile rtSurvey (Online e Offline):** Ideale per operazioni sul campo, aree remote con internet instabile, e sondaggi che richiedono allegati media (foto, coordinate GPS, mappe offline).

---

## Metodo 1: Raccolta dati tramite browser web

L'utilizzo dell'interfaccia Webform consente agli enumeratori di iniziare a raccogliere dati immediatamente senza installare alcun software.

### 1. Accedi all'URL del Webform
Dal pannello **Gestione moduli** nel Pannello di controllo, individua il modulo di destinazione e fai clic sul pulsante **URL del Webform** per generare un link sicuro.

### 2. Compilazione del modulo
- Apri l'URL fornito in qualsiasi browser web moderno.
- Se il modulo richiede l'autenticazione, l'enumeratore deve accedere usando le proprie credenziali. Se è impostato su "Visibilità pubblica", può procedere direttamente.
- Compila le domande del sondaggio. L'interfaccia applicherà automaticamente la logica, i pattern di salto e le regole di validazione.
- **Acquisizione media:** Se il modulo include domande su immagini, audio o video, il browser web ti chiederà di caricare un file dal tuo computer o di utilizzare la webcam/microfono del dispositivo se disponibile.

### 3. Invio
Al raggiungimento della pagina finale, fai clic su **Invia**. Il browser richiede una connessione internet attiva per finalizzare l'invio. Una volta completato con successo, i dati si rifletteranno immediatamente nell'interfaccia **Gestione invii**.

---

## Metodo 2: Raccolta dati tramite app mobile (Offline)

Per una raccolta dati sul campo robusta, le applicazioni mobili forniscono piena capacità offline.

### 1. Installa e autentica
- Scarica l'applicazione **rtWork** (o **rtSurvey**) dal Google Play Store o dall'Apple App Store.
- Apri l'app e accedi usando le credenziali dell'enumeratore assegnato.

### 2. Scarica i moduli (Richiede internet)
- Vai alla sezione **Moduli** o **Attività** nell'app.
- Tocca l'icona **Sincronizza** o **Scarica** per recuperare i disegni del questionario più recenti dal server. Una volta scaricati, i moduli vengono archiviati localmente sul dispositivo.

### 3. Raccogli dati (Offline)
- Apri il modulo scaricato e inizia l'intervista.
- Puoi raccogliere dati in modo sicuro completamente offline.
- **Acquisizione media:** L'app mobile si integra nativamente con l'hardware del dispositivo. Puoi acquisire foto, registrare audio, registrare video e registrare coordinate GPS precise direttamente nell'app, anche senza connessione internet.
- Quando finisci un'intervista, finalizza il record. I record finalizzati vengono messi in coda in modo sicuro nella posta in uscita dell'app.

### 4. Sincronizza gli invii (Richiede internet)
- Una volta che l'enumeratore ritorna in un'area con accesso a internet (Wi-Fi o dati mobili), deve navigare all'interfaccia **Posta in uscita** o **Sincronizza**.
- Ordina all'app di inviare i moduli finalizzati. L'app trasmetterà in modo sicuro i record in coda e tutti i file media allegati al server, dopodiché appariranno nella griglia dati per la revisione.
