---
weight: 2
title: "Linode (Akamai Cloud)"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-17T01:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "dns"
toc: true
description: "Αναπτύξτε το rtCloud στο Linode χρησιμοποιώντας StackScripts με διεπαφή διαμόρφωσης βάσει φόρμας."
---

Το Linode χρησιμοποιεί **StackScripts** — σενάρια με διεπαφή βάσει φόρμας όπου συμπληρώνετε τα πεδία διαμόρφωσης απευθείας στο Linode Manager χωρίς επεξεργασία κώδικα.

> Τα StackScripts Linode είναι η ευκολότερη μέθοδος ανάπτυξης. Τα πεδία εμφανίζονται ως φόρμα κατά τη δημιουργία Linode — δεν απαιτείται επεξεργασία σεναρίου.

---

## Ενσωματωμένο Keycloak (Συνιστάται)

### Βήμα 1 — Εύρεση του StackScript

Το StackScript είναι δημόσια διαθέσιμο στην κοινότητα Linode — δεν απαιτείται χειροκίνητη ρύθμιση:

1. Μεταβείτε στο **Linodes** → **Δημιουργία Linode**
2. Στο **Επιλογή διανομής**, επιλέξτε **StackScripts** → **StackScripts κοινότητας**
3. Αναζητήστε **`RTA rtSurvey - Self-Hosted with Keycloak SSO`**
4. Επιλέξτε το και συμπληρώστε τη φόρμα διαμόρφωσης:

> Εναλλακτικά, [κατεβάστε το σενάριο](/scripts/linode-stackscript-keycloak-embed.sh) και δημιουργήστε δικό σας StackScript στο **StackScripts** → **Δημιουργία StackScript**.

| Πεδίο | Απαιτείται | Περιγραφή |
|-------|----------|-------------|
| Project ID | Όχι | Μοναδικό αναγνωριστικό (προεπιλογή: `rtsurvey`). Χρησιμοποιείται ως όνομα βάσης δεδομένων και ID πελάτη Keycloak. |
| Κωδικός διαχειριστή Keycloak | Όχι | Κωδικός για κονσόλα διαχείρισης Keycloak και σύνδεση διαχειριστή εφαρμογής. Προεπιλογή `admin` — **αλλάξτε μετά την πρώτη σύνδεση**. |
| Domain | Ναι | Το όνομα τομέα σας. Η εγγραφή DNS A πρέπει να δείχνει στη διεύθυνση IP αυτού του Linode. Απαιτείται για HTTPS και Keycloak. |
| Email Let's Encrypt | Ναι | Email για ειδοποιήσεις πιστοποιητικού Let's Encrypt. |
| Docker Image Tag | Όχι | Εικόνα για ανάπτυξη (προεπιλογή: `rtawebteam/rta-smartsurvey:survey-dockerize`). |

> **Ασφάλεια:** Όλοι οι κωδικοί ορίζονται σε `admin` από προεπιλογή. Αλλάξτε τους αμέσως μετά την πρώτη σύνδεση.

5. Επιλέξτε **Ubuntu 22.04 LTS** ως εικόνα
6. Επιλέξτε πλάνο **Shared CPU 4 GB** ή μεγαλύτερο
7. Κάντε κλικ στο **Δημιουργία Linode**

### Βήμα 2 — Προσθήκη εγγραφής DNS

Ενώ το Linode εκκινεί, προσθέστε **εγγραφή A** στον πάροχο DNS σας:

```
Τύπος  : A
Όνομα  : myapp          (ή @ για ριζικό τομέα)
Τιμή   : <linode-ip>
TTL    : 300
```

### Βήμα 3 — Παρακολούθηση προόδου

```bash
ssh root@<linode-ip>
tail -f /var/log/stackscript.log
```

### Βήμα 4 — Πρόσβαση στην εφαρμογή

Όταν η ρύθμιση ολοκληρωθεί, το αρχείο καταγραφής εμφανίζει σύνοψη. Συνδεθείτε με όνομα χρήστη `admin` και κωδικό `admin`, στη συνέχεια αλλάξτε τον κωδικό σας αμέσως.

---

## Μετά την ανάπτυξη

### Αλλαγή κωδικού

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Προβολή όλων των κοντέινερ

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```

### Έλεγχος αρχείου καταγραφής

```bash
tail -200 /var/log/stackscript.log
```
