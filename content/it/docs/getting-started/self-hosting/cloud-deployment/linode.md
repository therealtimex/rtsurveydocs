---
weight: 2
title: "Linode (cloud Akamai)"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "dns"
toc: true
description: "Distribuisci rtCloud su Linode utilizzando StackScript. Non è necessaria alcuna configurazione: basta creare il server e seguire i passaggi successivi alla distribuzione."
---

## Passaggio 1: avvia StackScript

**[Deploy rtSurvey on Linode →](https://cloud.linode.com/stackscripts/2049143)**

Si apre la pagina StackScript in Linode Cloud Manager. Click **Deploy New Linode**.

---

## Passaggio 2: compila il modulo di Linode

Compila il modulo standard di creazione del server Linode:

| Campo | Valore consigliato |
|-------|-----------------|
| **Immagine** | Ubuntu 22.04 LTS |
| **Regione** | Più vicino ai tuoi utenti |
| **Piano** | CPU condivisa 4 GB o superiore |
| **Password di root** | Imposta una password complessa |
| **Fuso orario** *(il nostro unico campo)* | Il fuso orario del tuo server (predefinito: `Asia/Ho_Chi_Minh`) |

Al termine, fai clic su **Crea Linode**.

---

## Passaggio 3: attendi il completamento della configurazione

Lo script viene eseguito automaticamente al primo avvio. Installa Docker, estrae l'immagine rtSurvey, inizializza il database e avvia tutti i servizi. L'operazione richiede **5-10 minuti**.

Puoi osservare i progressi direttamente in **Linode Cloud Manager** — non è richiesto SSH:

1. Go to your [Linode dashboard](https://cloud.linode.com/linodes)
2. Fai clic sul Linode appena creato
3. Fai clic su **Avvia console LISH** (in alto a destra nella pagina dei dettagli di Linode)

Si apre un terminale del browser che mostra il registro di avvio live: la scheda **Weblish** funziona direttamente nel tuo browser, non è necessario alcun client SSH.

![Lish Console showing rtSurvey StackScript running](/img/first-login/lish-console.png)

Aspetta finché non vedi:

```
============================================================
 rtSurvey deployment complete!
============================================================
 Server IP : <your-server-ip>

 App URL   : http://<your-server-ip>  (HTTP only until domain is set)
 Admin     : admin / admin
============================================================
```

Il registro mostra anche l'IP del tuo server: ti servirà per il passaggio successivo.

---

## Passaggio 4: configura SSL

Open your browser at `http://<server-ip>`. The app will redirect you to the SSL setup screen.

Segui la **[Guida alla configurazione di SSL →](../ssl-setup)** per configurare HTTPS. Il **sottodominio gratuito rtsurvey.com** è l'opzione più veloce: non è necessaria alcuna configurazione DNS.

---

## Passaggio 5: primo accesso

Una volta attivo SSL, segui la **[Guida al primo accesso →](../first-login)** per accedere all'account amministratore.

---

## Passaggio 6: modifica la password predefinita

Per impostazione predefinita tutte le password sono "admin". Modificateli subito dopo il primo accesso:

- **Password amministratore app**: impostazioni dell'account all'interno dell'app
- **Keycloak admin** — accessible at `https://your-domain.com/auth/admin` (login: `admin` / `admin`)

---

## Regole del firewall (Firewall Linode Cloud)

Se colleghi un Linode Cloud Firewall a questo server, utilizza le seguenti regole:

### In entrata

| Etichetta | Azione | Protocollo | Porto | Fonti | Note |
|-------|--------|----------|------|---------|-------|
| `accetta-in entrata-ssh` | Accetta | TCP | 22| Tutto IPv4, Tutto IPv6 | Accesso SSH |
| `accetta-in entrata-http` | Accetta | TCP | 80| Tutto IPv4, Tutto IPv6 | Nginx (sfida HTTP + ACME) |
| `accetta-in entrata-https` | Accetta | TCP | 443| Tutto IPv4, Tutto IPv6 | Nginx (HTTPS dopo la configurazione SSL) |
| `accetta-inbound-shiny` | Accetta | TCP | 3838| Tutto IPv4, Tutto IPv6 | Shiny Server (analisi R) |
| `accetta-inbound-icmp` | Accetta | ICMP | — | Tutto IPv4, Tutto IPv6 | Ping/diagnostica |
| Politica in entrata predefinita | **Goccia** | | | | Blocca tutto il resto |

### In uscita

| Etichetta | Azione | Note |
|-------|--------|-------|
| Politica in uscita predefinita | **Accetta** | Consenti tutto in uscita (pull Docker, certbot, API GoDaddy, ecc.) |

### Porte NON necessarie esternamente

Queste porte sono vincolate solo a "127.0.0.1" e non sono mai raggiungibili dall'esterno del server:

| Porto | Servizio | Motivo |
|------|---------|--------|
| 8080| Contenitore dell'app | Nginx lo proxy internamente |
| 8090 | Keycloak container | Nginx proxies to it internally |
| 3306| MySQL | Solo rete Docker interna |

---

## Risoluzione dei problemi

### Controlla il registro di configurazione

```bash
tail -200 /var/log/stackscript.log
```

### Controlla il registro SSL

```bash
tail -200 /var/log/rtsurvey-ssl.log
```

### Visualizza lo stato del contenitore

```bash
docker compose -f /opt/rtsurvey/docker-compose.production.yml ps
```
