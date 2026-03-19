---
weight: 4
title: "Google Cloud (GCP)"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-16T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "travel_explore"
toc: true
description: "gcp-compute.sh స్టార్టప్ స్క్రిప్ట్ ఉపయోగించి Google Cloud Compute Engine లో rtCloud డిప్లాయ్ చేయండి."
---

Compute Engine VM ఇన్‌స్టాన్స్ సృష్టించేటప్పుడు `gcp-compute.sh` ని **Startup script** గా ఉపయోగించండి. స్క్రిప్ట్ మొదటి బూట్‌లో స్వయంచాలకంగా నడుస్తుంది.

**స్క్రిప్ట్ డౌన్‌లోడ్ చేయండి:** [gcp-compute.sh](/scripts/gcp-compute.sh)

---

## దశ 1 — కాన్ఫిగరేషన్ నింపండి

స్క్రిప్ట్ తెరవండి మరియు పైభాగంలో `CONFIGURATION` బ్లాక్ సవరించండి:

```bash
# --- అవసరమైనవి ---
PROJECT_ID="rtsurvey"
ADMIN_PASSWORD="admin"                       # మొదటి లాగిన్ తర్వాత మార్చండి

# --- డొమైన్ + SSL ---
DOMAIN="myapp.example.com"
LETSENCRYPT_EMAIL="admin@example.com"

# --- ఎంబెడెడ్ Keycloak ---
EMBED_KEYCLOAK="true"
KEYCLOAK_ADMIN_PASSWORD="${ADMIN_PASSWORD}"  # ADMIN_PASSWORD కి డిఫాల్ట్
```

| ఫీల్డ్ | అవసరమైనదా | వివరణ |
|-------|----------|-------------|
| `PROJECT_ID` | అవును | డేటాబేస్ పేరు మరియు Keycloak క్లైంట్ ID గా ఉపయోగించబడుతుంది. చిన్న అక్షరాలు, ఖాళీలు లేవు. |
| `ADMIN_PASSWORD` | లేదు | యాప్ అడ్మిన్ పాస్‌వర్డ్ మరియు Keycloak అడ్మిన్ పాస్‌వర్డ్. `admin` కి డిఫాల్ట్ — **మొదటి లాగిన్ తర్వాత మార్చండి**. |
| `DOMAIN` | లేదు | HTTPS కోసం మీ డొమైన్. HTTP-only మోడ్ కోసం ఖాళీగా వదిలండి. |
| `LETSENCRYPT_EMAIL` | అవును (DOMAIN సెట్ చేస్తే) | Let's Encrypt నోటిఫికేషన్‌ల కోసం ఇమెయిల్. |
| `EMBED_KEYCLOAK` | లేదు | ఎంబెడెడ్ Keycloak డిప్లాయ్ చేయడానికి `true` (4 GB RAM అవసరం). |

> **భద్రత:** అన్ని పాస్‌వర్డ్‌లు `admin` కి డిఫాల్ట్. మీ మొదటి లాగిన్ తర్వాత వాటిని వెంటనే మార్చండి.

---

## దశ 2 — VM ఇన్‌స్టాన్స్ సృష్టించండి

[Google Cloud Console](https://console.cloud.google.com/compute) లో:

1. **Create instance** క్లిక్ చేయండి
2. **Machine configuration:**
   - Series: `E2`
   - Machine type: `e2-medium` (4 GB RAM) లేదా పెద్దది
3. **Boot disk:**
   - Operating system: Ubuntu
   - Version: Ubuntu 22.04 LTS
   - Size: 40 GB లేదా ఎక్కువ
4. **Firewall:** **Allow HTTP traffic** మరియు **Allow HTTPS traffic** చెక్ చేయండి
5. **Advanced options** → **Management** → **Automation** → **Startup script** → పూర్తి స్క్రిప్ట్ కంటెంట్ పేస్ట్ చేయండి
6. **Create** క్లిక్ చేయండి

---

## దశ 3 — DNS రికార్డ్ జోడించండి

VM బూట్ అవుతున్నప్పుడు, మీ DNS ప్రొవైడర్‌లో **A రికార్డ్** జోడించండి:

```
Type  : A
Name  : myapp
Value : <vm-external-ip>
TTL   : 300
```

కన్సోల్‌లో VM ఇన్‌స్టాన్స్‌ల జాబితాలో బాహ్య IP కనుగొనండి.

---

## దశ 4 — పురోగతి పర్యవేక్షించండి

`gcloud` CLI ఉపయోగించి:

```bash
gcloud compute ssh <instance-name> -- tail -f /var/log/rtcloud-setup.log
```

లేదా నేరుగా SSH:

```bash
ssh <username>@<vm-external-ip>
tail -f /var/log/rtcloud-setup.log
```

---

## దశ 5 — యాప్ యాక్సెస్ చేయండి

సెటప్ పూర్తయినప్పుడు, లాగ్ మీ యాప్ URL మరియు ఆధారపత్రాలతో సారాంశం చూపిస్తుంది. వినియోగదారు పేరు `admin` మరియు పాస్‌వర్డ్ `admin` తో లాగిన్ అవండి, తర్వాత వెంటనే మీ పాస్‌వర్డ్ మార్చండి.

---

## ఫైర్‌వాల్ నియమాలు

GCP యొక్క **Allow HTTP/HTTPS** చెక్‌బాక్స్‌లు పోర్ట్‌లు 80 మరియు 443 తెరుస్తాయి. పోర్ట్ 3838 లో నేరుగా Shiny యాక్సెస్ అనుమతించడానికి కూడా, ఫైర్‌వాల్ నియమం జోడించండి:

```bash
gcloud compute firewall-rules create allow-shiny \
  --allow tcp:3838 \
  --target-tags http-server
```

లేదా కన్సోల్ ద్వారా జోడించండి: **VPC Network** → **Firewall** → **Create rule**.

> పోర్ట్ 3306 (MySQL) **తెరవకండి** — ఇది ఎప్పుడూ పబ్లిక్‌గా యాక్సెస్ చేయబడకూడదు.

---

## స్టాటిక్ IP (ఐచ్ఛికం)

డిఫాల్ట్‌గా, GCP VM పునఃప్రారంభంపై మారే అస్థిర బాహ్య IP కేటాయిస్తుంది. స్థిరమైన IP ఉంచుకోవడానికి:

1. **VPC Network** → **IP addresses** వెళ్ళండి
2. **Reserve external static address** క్లిక్ చేయండి
3. మీ VM ఇన్‌స్టాన్స్‌కు కేటాయించండి

---

## డిప్లాయ్‌మెంట్ తర్వాత

### పాస్‌వర్డ్ మార్చండి

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### అన్ని కంటైనర్‌లు చూడండి

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```
