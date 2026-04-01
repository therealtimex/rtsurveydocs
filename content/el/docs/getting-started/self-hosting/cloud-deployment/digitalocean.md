---
weight: 1
title: "DigitalOcean"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-17T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "water_drop"
toc: true
description: "Αναπτύξτε το rtCloud σε DigitalOcean Droplet χρησιμοποιώντας αυτοματοποιημένα σενάρια user-data."
---

Το DigitalOcean χρησιμοποιεί σενάρια **User Data** που εκτελούνται αυτόματα κατά την πρώτη εκκίνηση. Συμπληρώνετε τις μεταβλητές διαμόρφωσης στην κορυφή του σεναρίου, στη συνέχεια επικολλάτε ολόκληρο το σενάριο κατά τη δημιουργία ενός Droplet.

> Σε αντίθεση με τα StackScripts Linode, το DigitalOcean δεν έχει διεπαφή φόρμας — πρέπει να επεξεργαστείτε το σενάριο απευθείας πριν την επικόλληση.

**Λήψη σεναρίου:** [digitalocean-droplet-keycloak-embed.sh](/scripts/digitalocean-droplet-keycloak-embed.sh)

---

## Ενσωματωμένο Keycloak (Συνιστάται)

Χρησιμοποιήστε το `digitalocean-droplet-keycloak-embed.sh` για την απλούστερη ρύθμιση με ενσωματωμένο SSO.

### Βήμα 1 — Συμπλήρωση της διαμόρφωσης

Ανοίξτε το σενάριο και επεξεργαστείτε το μπλοκ `CONFIGURATION` στην κορυφή:

```bash
# --- Απαιτούμενα ---
PROJECT_ID="rtsurvey"                  # Μοναδικό αναγνωριστικό για το έργο σας (χωρίς κενά)
ADMIN_PASSWORD="admin"                 # Κωδικός για διαχειριστή εφαρμογής και Keycloak — αλλάξτε μετά την πρώτη σύνδεση

# --- Τομέας + SSL ---
DOMAIN="myapp.example.com"            # Ο τομέας σας — η εγγραφή DNS A πρέπει να δείχνει εδώ
PROJECT_URL=""                         # Αφήστε κενό εκτός αν βρίσκεστε πίσω από Cloudflare/proxy
LETSENCRYPT_EMAIL="admin@example.com" # Email για ειδοποιήσεις Let's Encrypt

# --- Προαιρετικά ---
STATA_ENABLED="false"
TZ="Asia/Ho_Chi_Minh"
```

| Πεδίο | Απαιτείται | Περιγραφή |
|-------|----------|-------------|
| `PROJECT_ID` | Ναι | Χρησιμοποιείται ως όνομα βάσης δεδομένων και ID πελάτη Keycloak. Πεζά, χωρίς κενά. |
| `ADMIN_PASSWORD` | Όχι | Κωδικός σύνδεσης διαχειριστή εφαρμογής και κονσόλας διαχείρισης Keycloak. Προεπιλογή `admin` — **αλλάξτε μετά την πρώτη σύνδεση**. |
| `DOMAIN` | Ναι | Το όνομα τομέα σας. Η εγγραφή DNS A πρέπει να δείχνει στη διεύθυνση IP του Droplet. |
| `LETSENCRYPT_EMAIL` | Ναι | Διεύθυνση email για ειδοποιήσεις πιστοποιητικού Let's Encrypt. |
| `PROJECT_URL` | Όχι | Παράκαμψη δημόσιου URL. Αφήστε κενό για χρήση `DOMAIN`. Χρήσιμο πίσω από Cloudflare. |

> **Ασφάλεια:** Όλοι οι κωδικοί ορίζονται σε `admin` από προεπιλογή. Αλλάξτε τους αμέσως μετά την πρώτη σύνδεση.

### Βήμα 2 — Δημιουργία Droplet

Στον [πίνακα ελέγχου DigitalOcean](https://cloud.digitalocean.com):

1. Κάντε κλικ στο **Δημιουργία** → **Droplets**
2. Επιλέξτε **Ubuntu 22.04 LTS** ως εικόνα
3. Επιλέξτε **Basic, 4 GB RAM / 2 vCPUs** ή μεγαλύτερο
4. Μεταβείτε στις **Επιλογές για προχωρημένους** → επιλέξτε **Προσθήκη σεναρίων αρχικοποίησης**
5. Επικολλήστε το πλήρες περιεχόμενο σεναρίου στο πεδίο κειμένου
6. Κάντε κλικ στο **Δημιουργία Droplet**

### Βήμα 3 — Προσθήκη εγγραφής DNS

Ενώ το Droplet εκκινεί, προσθέστε **εγγραφή A** στον πάροχο DNS σας:

```
Τύπος  : A
Όνομα  : myapp          (ή @ για ριζικό τομέα)
Τιμή   : <droplet-ip>
TTL    : 300
```

### Βήμα 4 — Παρακολούθηση προόδου

Συνδεθείτε μέσω SSH στο Droplet και παρακολουθήστε το αρχείο καταγραφής:

```bash
ssh root@<droplet-ip>
tail -f /var/log/rtcloud-setup.log
```

### Βήμα 5 — Πρόσβαση στην εφαρμογή

Όταν η ρύθμιση ολοκληρωθεί, το αρχείο καταγραφής εμφανίζει σύνοψη:

```
============================================================
 rtCloud deployment complete! (Embedded Keycloak)
============================================================
 App URL   : https://myapp.example.com
 Admin     : admin / admin
 Keycloak  : https://myapp.example.com/auth/admin

 !! SECURITY: All passwords default to 'admin'.
    Change them immediately after first login.
============================================================
```

Ανοίξτε `https://myapp.example.com` στο πρόγραμμα περιήγησής σας και συνδεθείτε με όνομα χρήστη `admin` και κωδικό `admin`.

> **Αλλάξτε τον κωδικό σας** αμέσως μετά τη σύνδεση μέσω **Ρυθμίσεων** στο μενού επάνω δεξιά.

---

## Μετά την ανάπτυξη

### Αλλαγή κωδικού

Συνδεθείτε μέσω SSH στο Droplet, επεξεργαστείτε το `.env` και επανεκκινήστε το επηρεαζόμενο κοντέινερ:

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Ενημέρωση τομέα

```bash
nano /opt/rtcloud/.env   # ενημερώστε PROJECT_URL=
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Προβολή όλων των κοντέινερ

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```
