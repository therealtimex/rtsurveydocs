---
weight: 2
title: "Linode (Akamai Cloud)"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-17T01:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "dns"
toc: true
description: "ఫారం-ఆధారిత కాన్ఫిగరేషన్ UI తో StackScripts ఉపయోగించి Linode లో rtCloud డిప్లాయ్ చేయండి."
---

Linode **StackScripts** ఉపయోగిస్తుంది — ఫారం-ఆధారిత UI తో స్క్రిప్ట్‌లు, ఇక్కడ మీరు ఏ కోడ్ సవరించకుండా నేరుగా Linode Manager లో కాన్ఫిగరేషన్ ఫీల్డ్‌లు నింపవచ్చు.

> Linode StackScripts అత్యంత సులభమైన డిప్లాయ్‌మెంట్ పద్ధతి. Linode సృష్టించేటప్పుడు ఫీల్డ్‌లు ఫారంగా కనిపిస్తాయి — స్క్రిప్ట్ సవరణ అవసరం లేదు.

---

## ఎంబెడెడ్ Keycloak (సిఫారసు)

### దశ 1 — StackScript కనుగొనండి

StackScript Linode community లో పబ్లిక్‌గా అందుబాటులో ఉంది — మాన్యువల్ సెటప్ అవసరం లేదు:

1. **Linodes** → **Create Linode** వెళ్ళండి
2. **Choose a Distribution** కింద, **StackScripts** → **Community StackScripts** ఎంచుకోండి
3. **`RTA rtSurvey - Self-Hosted with Keycloak SSO`** అని శోధించండి
4. దాన్ని ఎంచుకుని కాన్ఫిగరేషన్ ఫారం నింపండి:

> ప్రత్యామ్నాయంగా, [స్క్రిప్ట్ డౌన్‌లోడ్ చేయండి](/scripts/linode-stackscript-keycloak-embed.sh) మరియు **StackScripts** → **Create StackScript** కింద మీ స్వంత StackScript సృష్టించండి.

| ఫీల్డ్ | అవసరమైనదా | వివరణ |
|-------|----------|-------------|
| Project ID | లేదు | ప్రత్యేక గుర్తింపు (డిఫాల్ట్: `rtsurvey`). డేటాబేస్ పేరు మరియు Keycloak క్లైంట్ ID గా ఉపయోగించబడుతుంది. |
| Keycloak Admin Password | లేదు | Keycloak అడ్మిన్ కన్సోల్ మరియు యాప్ అడ్మిన్ లాగిన్ రెండింటికీ పాస్‌వర్డ్. `admin` కి డిఫాల్ట్ — **మొదటి లాగిన్ తర్వాత మార్చండి**. |
| Domain | అవును | మీ డొమైన్ పేరు. DNS A రికార్డ్ ఈ Linode యొక్క IP కి పాయింట్ చేయాలి. HTTPS మరియు Keycloak కోసం అవసరం. |
| Let's Encrypt Email | అవును | Let's Encrypt సర్టిఫికేట్ నోటిఫికేషన్‌ల కోసం ఇమెయిల్. |
| Docker Image Tag | లేదు | డిప్లాయ్ చేయవలసిన ఇమేజ్ (డిఫాల్ట్: `rtawebteam/rta-smartsurvey:survey-dockerize`). |

> **భద్రత:** అన్ని పాస్‌వర్డ్‌లు `admin` కి డిఫాల్ట్. మీ మొదటి లాగిన్ తర్వాత వాటిని వెంటనే మార్చండి.

5. ఇమేజ్‌గా **Ubuntu 22.04 LTS** ఎంచుకోండి
6. **Shared CPU 4 GB** ప్లాన్ లేదా పెద్దది ఎంచుకోండి
7. **Create Linode** క్లిక్ చేయండి

### దశ 2 — DNS రికార్డ్ జోడించండి

Linode బూట్ అవుతున్నప్పుడు, మీ DNS ప్రొవైడర్‌లో **A రికార్డ్** జోడించండి:

```
Type  : A
Name  : myapp          (లేదా రూట్ డొమైన్ కోసం @)
Value : <linode-ip>
TTL   : 300
```

### దశ 3 — పురోగతి పర్యవేక్షించండి

```bash
ssh root@<linode-ip>
tail -f /var/log/stackscript.log
```

స్క్రిప్ట్ ప్రారంభంలో మీ సర్వర్ IP ప్రింట్ చేస్తుంది — మీరు దాన్ని చూడగానే DNS రికార్డ్ జోడించండి.

### దశ 4 — యాప్ యాక్సెస్ చేయండి

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

వినియోగదారు పేరు `admin` మరియు పాస్‌వర్డ్ `admin` తో లాగిన్ అవండి, తర్వాత వెంటనే మీ పాస్‌వర్డ్ మార్చండి.

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

### లాగ్ తనిఖీ చేయండి

```bash
tail -200 /var/log/stackscript.log
```
