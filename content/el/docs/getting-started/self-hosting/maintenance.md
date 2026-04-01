---
weight: 5
title: "Συντήρηση"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "build"
toc: true
description: "Καθημερινή συντήρηση αυτο-φιλοξενούμενης εγκατάστασης rtCloud: αναβάθμιση, δημιουργία αντιγράφων ασφαλείας, επαναφορά και αντιμετώπιση κοινών προβλημάτων."
---

## Κοινές εντολές

Χρησιμοποιήστε αυτές τις εντολές τακτικά για τη διαχείριση των κοντέινερ rtCloud. Εκτελέστε τις από τον κατάλογο που περιέχει το `docker-compose.production.yml`.

```bash
# Έλεγχος κατάστασης και υγείας όλων των κοντέινερ
docker compose -f docker-compose.production.yml ps

# Προβολή live αρχείων καταγραφής (όλες οι υπηρεσίες)
docker compose -f docker-compose.production.yml logs -f

# Προβολή αρχείων καταγραφής μόνο εφαρμογής
docker compose -f docker-compose.production.yml logs -f rtcloud

# Επανεκκίνηση ενός κοντέινερ
docker compose -f docker-compose.production.yml restart rtcloud

# Διακοπή όλων των υπηρεσιών
docker compose -f docker-compose.production.yml down

# Εκκίνηση όλων των υπηρεσιών
docker compose -f docker-compose.production.yml up -d

# Άνοιγμα κέλυφους εντός κοντέινερ εφαρμογής
docker compose -f docker-compose.production.yml exec rtcloud bash
```

---

## Αναβάθμιση

Οι ενημερώσεις rtCloud διανέμονται ως νέες ετικέτες εικόνας Docker. Η αναβάθμιση ανακτά την τελευταία εικόνα και ανδημιουργεί το κοντέινερ εφαρμογής. Οι μετεγκαταστάσεις βάσης δεδομένων εκτελούνται αυτόματα κατά την εκκίνηση.

**1. Ανάκτηση τελευταίας εικόνας:**

```bash
docker compose -f docker-compose.production.yml pull
```

**2. Ανδημιουργία κοντέινερ εφαρμογής:**

```bash
docker compose -f docker-compose.production.yml up -d
```

### Καρφίτσωμα έκδοσης

Για αναβάθμιση σε συγκεκριμένη έκδοση αντί για `latest`, ενημερώστε το `RTCLOUD_IMAGE` στο `.env`:

```dotenv
RTCLOUD_IMAGE=rtawebteam/rta-smartsurvey:1.2.3
```

---

## Δημιουργία αντιγράφων ασφαλείας και επαναφορά

### Δημιουργία αντιγράφου ασφαλείας βάσης δεδομένων

```bash
docker compose -f docker-compose.production.yml exec mysql \
  mysqldump -u root -p"$(grep MYSQL_ROOT_PASSWORD .env | cut -d= -f2)" smartsurvey \
  > backup-$(date +%Y%m%d-%H%M%S).sql
```

### Επαναφορά βάσης δεδομένων

```bash
docker compose -f docker-compose.production.yml exec -T mysql \
  mysql -u root -p"$(grep MYSQL_ROOT_PASSWORD .env | cut -d= -f2)" smartsurvey \
  < backup-20240101-120000.sql
```

### Δημιουργία αντιγράφου ασφαλείας μεταφορτωμένων αρχείων

```bash
# Δημιουργία αντιγράφου ασφαλείας μεταφορτώσεων
docker run --rm \
  -v rtcloud_uploads:/data \
  -v "$(pwd):/backup" \
  alpine tar czf /backup/uploads-$(date +%Y%m%d).tar.gz -C /data .

# Δημιουργία αντιγράφου ασφαλείας ηχογραφήσεων
docker run --rm \
  -v rtcloud_audios:/data \
  -v "$(pwd):/backup" \
  alpine tar czf /backup/audios-$(date +%Y%m%d).tar.gz -C /data .
```

### Επαναφορά μεταφορτωμένων αρχείων

```bash
docker run --rm \
  -v rtcloud_uploads:/data \
  -v "$(pwd):/backup" \
  alpine tar xzf /backup/uploads-20240101.tar.gz -C /data
```

### Αυτόματα ημερήσια αντίγραφα ασφαλείας

Προσθέστε εργασία cron στον κεντρικό υπολογιστή. Επεξεργαστείτε το root crontab με `crontab -e`:

```cron
# Ημερήσιο αντίγραφο ασφαλείας βάσης δεδομένων στις 2:00 π.μ., διατήρηση 30 ημερών ιστορικού
0 2 * * * cd /opt/rtcloud && docker compose -f docker-compose.production.yml exec -T mysql \
  mysqldump -u root -p"$(grep MYSQL_ROOT_PASSWORD .env | cut -d= -f2)" smartsurvey \
  > /backups/db-$(date +\%Y\%m\%d).sql && \
  find /backups -name "db-*.sql" -mtime +30 -delete
```

---

## Αντιμετώπιση προβλημάτων

### Το κοντέινερ εφαρμογής δεν εκκινεί

Ελέγξτε τα αρχεία καταγραφής κοντέινερ για μηνύματα σφάλματος:

```bash
docker compose -f docker-compose.production.yml logs rtcloud
```

Κοινές αιτίες:
- Ελλείπουσες ή μη έγκυρες μεταβλητές περιβάλλοντος στο `.env`
- Η MySQL δεν είναι ακόμα έτοιμη (αναμείνετε 60 δευτερόλεπτα και ελέγξτε ξανά)
- Σύγκρουση θύρας — άλλη διαδικασία χρησιμοποιεί ήδη το `APP_PORT`

### Η MySQL δεν είναι υγιής

```bash
docker compose -f docker-compose.production.yml logs mysql
```

Κοινές αιτίες:
- `MYSQL_ROOT_PASSWORD` δεν έχει οριστεί στο `.env`
- Κατεστραμμένος τόμος δεδομένων (σπάνιο — ελέγξτε χώρο δίσκου με `df -h`)

### Θύρα ήδη σε χρήση

Αλλάξτε `APP_PORT` ή `SHINY_PORT` στο `.env` σε ελεύθερη θύρα, στη συνέχεια ανδημιουργήστε τα κοντέινερ:

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate
```

### 400 Αδυναμία επαλήθευσης CSRF Token

Απενεργοποιήστε την επαλήθευση CSRF μόνο για τοπική ανάπτυξη:

```dotenv
CSRF_VALIDATION_ENABLED=false
```

Στη συνέχεια επανεκκινήστε την εφαρμογή:

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

> Μην απενεργοποιείτε την επαλήθευση CSRF στην παραγωγή.

### Ξεχάσατε τον κωδικό διαχειριστή

Επαναφέρετε τον κωδικό διαχειριστή απευθείας στη βάση δεδομένων. Συνδεθείτε στο κοντέινερ MySQL και ενημερώστε το hash κωδικού.

### Το κοντέινερ επανεκκινείται συνεχώς

Ελέγξτε εάν ο έλεγχος υγείας αποτυγχάνει:

```bash
docker compose -f docker-compose.production.yml ps
docker inspect rtcloud-app --format '{{json .State.Health}}'
```

### Ο δίσκος είναι γεμάτος

Εντοπίστε τι καταναλώνει χώρο:

```bash
df -h
docker system df
docker system prune
```

Μην χρησιμοποιείτε `docker system prune --volumes` καθώς θα διαγράψει δεδομένα εφαρμογής.

---

## Έλεγχοι υγείας

| Κοντέινερ | Μέθοδος ελέγχου | Περίοδος εκκίνησης | Διάστημα |
|-----------|-------------|-------------|----------|
| `rtcloud-app` | HTTP GET `/health` | 90 δευτερόλεπτα | 30 δευτερόλεπτα |
| `rtcloud-mysql` | `mysqladmin ping` | 30 δευτερόλεπτα | 10 δευτερόλεπτα |
| `rtcloud-keycloak` | HTTP GET `:9000/health/live` | 120 δευτερόλεπτα | 30 δευτερόλεπτα |
