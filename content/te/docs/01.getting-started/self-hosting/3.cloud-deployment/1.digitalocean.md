---
weight: 1
title: "DigitalOcean"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-17T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "water_drop"
toc: true
description: "స్వయంచాలిత user-data స్క్రిప్ట్‌లు ఉపయోగించి DigitalOcean Droplet లో rtCloud డిప్లాయ్ చేయండి."
---

DigitalOcean **User Data** స్క్రిప్ట్‌లు ఉపయోగిస్తుంది, ఇవి మొదటి బూట్‌లో స్వయంచాలకంగా నడుస్తాయి. స్క్రిప్ట్ పైభాగంలో కాన్ఫిగరేషన్ వేరియబుల్‌లు నింపి, Droplet సృష్టించేటప్పుడు మొత్తం స్క్రిప్ట్ పేస్ట్ చేయండి.

> Linode StackScripts వలా కాకుండా, DigitalOcean లో ఫారం UI లేదు — పేస్ట్ చేయడానికి ముందు స్క్రిప్ట్‌ను నేరుగా సవరించాలి.

**స్క్రిప్ట్ డౌన్‌లోడ్ చేయండి:** [digitalocean-droplet-keycloak-embed.sh](/scripts/digitalocean-droplet-keycloak-embed.sh)

---

## ఎంబెడెడ్ Keycloak (సిఫారసు)

అంతర్నిర్మిత SSO తో అత్యంత సరళమైన సెటప్ కోసం `digitalocean-droplet-keycloak-embed.sh` ఉపయోగించండి.

### దశ 1 — కాన్ఫిగరేషన్ నింపండి

స్క్రిప్ట్ తెరవండి మరియు పైభాగంలో `CONFIGURATION` బ్లాక్ సవరించండి:

```bash
# --- అవసరమైనవి ---
PROJECT_ID="rtsurvey"                  # మీ ప్రాజెక్ట్ కోసం ప్రత్యేక గుర్తింపు (ఖాళీలు లేవు)
ADMIN_PASSWORD="admin"                 # యాప్ అడ్మిన్ మరియు Keycloak కోసం పాస్‌వర్డ్ — మొదటి లాగిన్ తర్వాత మార్చండి

# --- డొమైన్ + SSL ---
DOMAIN="myapp.example.com"            # మీ డొమైన్ — DNS A రికార్డ్ ఇక్కడ పాయింట్ చేయాలి
PROJECT_URL=""                         # Cloudflare/proxy వెనుక ఉంటే తప్ప ఖాళీగా వదిలండి
LETSENCRYPT_EMAIL="admin@example.com" # Let's Encrypt నోటిఫికేషన్‌ల కోసం ఇమెయిల్

# --- ఐచ్ఛికం ---
STATA_ENABLED="false"
TZ="Asia/Ho_Chi_Minh"
```

| ఫీల్డ్ | అవసరమైనదా | వివరణ |
|-------|----------|-------------|
| `PROJECT_ID` | అవును | డేటాబేస్ పేరు మరియు Keycloak క్లైంట్ ID గా ఉపయోగించబడుతుంది. చిన్న అక్షరాలు, ఖాళీలు లేవు. |
| `ADMIN_PASSWORD` | లేదు | యాప్ అడ్మిన్ లాగిన్ మరియు Keycloak అడ్మిన్ కన్సోల్ కోసం పాస్‌వర్డ్. `admin` కి డిఫాల్ట్ — **మొదటి లాగిన్ తర్వాత మార్చండి**. |
| `DOMAIN` | అవును | మీ డొమైన్ పేరు. DNS A రికార్డ్ Droplet IP కి పాయింట్ చేయాలి. |
| `LETSENCRYPT_EMAIL` | అవును | Let's Encrypt సర్టిఫికేట్ నోటిఫికేషన్‌ల కోసం ఇమెయిల్ చిరునామా. |
| `PROJECT_URL` | లేదు | పబ్లిక్ URL ఓవర్‌రైడ్ చేయండి. `DOMAIN` ఉపయోగించాలంటే ఖాళీగా వదిలండి. Cloudflare వెనుక ఉపయోగకరం. |

> **భద్రత:** అన్ని పాస్‌వర్డ్‌లు `admin` కి డిఫాల్ట్. మీ మొదటి లాగిన్ తర్వాత వాటిని వెంటనే మార్చండి.

### దశ 2 — Droplet సృష్టించండి

[DigitalOcean కంట్రోల్ ప్యానెల్](https://cloud.digitalocean.com) లో:

1. **Create** → **Droplets** క్లిక్ చేయండి
2. ఇమేజ్‌గా **Ubuntu 22.04 LTS** ఎంచుకోండి
3. **Basic, 4 GB RAM / 2 vCPUs** లేదా పెద్దది ఎంచుకోండి
4. **Advanced Options** వరకు స్క్రోల్ చేయండి → **Add Initialization scripts** చెక్ చేయండి
5. టెక్స్ట్ ఏరియాలో పూర్తి స్క్రిప్ట్ కంటెంట్ పేస్ట్ చేయండి
6. **Create Droplet** క్లిక్ చేయండి

### దశ 3 — DNS రికార్డ్ జోడించండి

Droplet బూట్ అవుతున్నప్పుడు, మీ DNS ప్రొవైడర్‌లో **A రికార్డ్** జోడించండి:

```
Type  : A
Name  : myapp          (లేదా రూట్ డొమైన్ కోసం @)
Value : <droplet-ip>
TTL   : 300
```

### దశ 4 — పురోగతి పర్యవేక్షించండి

Droplet లో SSH చేసి లాగ్ చూడండి:

```bash
ssh root@<droplet-ip>
tail -f /var/log/rtcloud-setup.log
```

స్క్రిప్ట్ ప్రారంభంలో మీ సర్వర్ IP ప్రింట్ చేస్తుంది — మీరు దాన్ని చూడగానే DNS రికార్డ్ జోడించండి.

### దశ 5 — యాప్ యాక్సెస్ చేయండి

సెటప్ పూర్తయినప్పుడు, లాగ్ సారాంశం చూపిస్తుంది:

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

మీ బ్రౌజర్‌లో `https://myapp.example.com` తెరవండి మరియు వినియోగదారు పేరు `admin` మరియు పాస్‌వర్డ్ `admin` తో లాగిన్ అవండి.

> లాగిన్ తర్వాత వెంటనే పైకుడి మెనులో **Settings** ద్వారా **మీ పాస్‌వర్డ్ మార్చండి**.

---

## డిప్లాయ్‌మెంట్ తర్వాత

### పాస్‌వర్డ్ మార్చండి

Droplet లో SSH చేయండి, `.env` సవరించండి మరియు ప్రభావితమైన కంటైనర్‌ను పునఃప్రారంభించండి:

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### డొమైన్ అప్‌డేట్ చేయండి

డిప్లాయ్‌మెంట్ తర్వాత వేర్వేరు డొమైన్ కేటాయిస్తే, `.env` లో `PROJECT_URL` అప్‌డేట్ చేయండి:

```bash
nano /opt/rtcloud/.env   # PROJECT_URL= అప్‌డేట్ చేయండి
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### అన్ని కంటైనర్‌లు చూడండి

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```
