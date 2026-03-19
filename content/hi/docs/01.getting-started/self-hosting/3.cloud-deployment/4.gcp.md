---
weight: 4
title: "Google Cloud (GCP)"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-16T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "travel_explore"
toc: true
description: "gcp-compute.sh स्टार्टअप स्क्रिप्ट का उपयोग करके Google Cloud Compute Engine पर rtCloud तैनात करें।"
---

Compute Engine VM इंस्टेंस बनाते समय **Startup script** के रूप में `gcp-compute.sh` का उपयोग करें। स्क्रिप्ट पहले बूट पर स्वचालित रूप से चलती है।

**स्क्रिप्ट डाउनलोड करें:** [gcp-compute.sh](/scripts/gcp-compute.sh)

---

## चरण 1 — कॉन्फ़िगरेशन भरें

स्क्रिप्ट खोलें और शीर्ष पर `CONFIGURATION` ब्लॉक संपादित करें:

```bash
# --- आवश्यक ---
PROJECT_ID="rtsurvey"
ADMIN_PASSWORD="admin"                       # पहले लॉगिन के बाद बदलें

# --- डोमेन + SSL ---
DOMAIN="myapp.example.com"
LETSENCRYPT_EMAIL="admin@example.com"

# --- एम्बेडेड Keycloak ---
EMBED_KEYCLOAK="true"
KEYCLOAK_ADMIN_PASSWORD="${ADMIN_PASSWORD}"  # ADMIN_PASSWORD पर डिफ़ॉल्ट
```

| फ़ील्ड | आवश्यक | विवरण |
|-------|----------|-------------|
| `PROJECT_ID` | हां | डेटाबेस नाम और Keycloak क्लाइंट ID के रूप में उपयोग किया जाता है। लोअरकेस, कोई स्पेस नहीं। |
| `ADMIN_PASSWORD` | नहीं | ऐप admin पासवर्ड और Keycloak admin पासवर्ड। डिफ़ॉल्ट `admin` — **पहले लॉगिन के बाद बदलें**। |
| `DOMAIN` | नहीं | HTTPS के लिए आपका डोमेन। केवल HTTP मोड के लिए खाली छोड़ें। |
| `LETSENCRYPT_EMAIL` | हां (यदि DOMAIN सेट है) | Let's Encrypt सूचनाओं के लिए ईमेल। |
| `EMBED_KEYCLOAK` | नहीं | एम्बेडेड Keycloak तैनात करने के लिए `true` (4 GB RAM की आवश्यकता है)। |

> **सुरक्षा:** सभी पासवर्ड डिफ़ॉल्ट रूप से `admin` हैं। पहले लॉगिन के तुरंत बाद उन्हें बदलें।

---

## चरण 2 — एक VM इंस्टेंस बनाएं

[Google Cloud Console](https://console.cloud.google.com/compute) में:

1. **Create instance** पर क्लिक करें
2. **Machine configuration:**
   - Series: `E2`
   - Machine type: `e2-medium` (4 GB RAM) या बड़ा
3. **Boot disk:**
   - Operating system: Ubuntu
   - Version: Ubuntu 22.04 LTS
   - Size: 40 GB या अधिक
4. **Firewall:** **Allow HTTP traffic** और **Allow HTTPS traffic** चेक करें
5. **Advanced options** → **Management** → **Automation** → **Startup script** → पूरी स्क्रिप्ट सामग्री पेस्ट करें
6. **Create** पर क्लिक करें

---

## चरण 3 — DNS रिकॉर्ड जोड़ें

VM बूट होते समय, अपने DNS प्रदाता में एक **A रिकॉर्ड** जोड़ें:

```
Type  : A
Name  : myapp
Value : <vm-external-ip>
TTL   : 300
```

कंसोल में VM इंस्टेंस सूची में बाहरी IP ढूंढें।

---

## चरण 4 — प्रगति मॉनिटर करें

`gcloud` CLI का उपयोग करके:

```bash
gcloud compute ssh <instance-name> -- tail -f /var/log/rtcloud-setup.log
```

या सीधे SSH करें:

```bash
ssh <username>@<vm-external-ip>
tail -f /var/log/rtcloud-setup.log
```

---

## चरण 5 — ऐप एक्सेस करें

सेटअप पूरी होने पर, लॉग आपके ऐप URL और क्रेडेंशियल के साथ एक सारांश दिखाता है। उपयोगकर्ता नाम `admin` और पासवर्ड `admin` से लॉग इन करें, फिर तुरंत अपना पासवर्ड बदलें।

---

## फ़ायरवॉल नियम

GCP के **Allow HTTP/HTTPS** चेकबॉक्स पोर्ट 80 और 443 खोलते हैं। पोर्ट 3838 पर सीधे Shiny एक्सेस की अनुमति देने के लिए, एक फ़ायरवॉल नियम जोड़ें:

```bash
gcloud compute firewall-rules create allow-shiny \
  --allow tcp:3838 \
  --target-tags http-server
```

या कंसोल के माध्यम से जोड़ें: **VPC Network** → **Firewall** → **Create rule**।

> पोर्ट 3306 (MySQL) **न खोलें** — यह कभी भी सार्वजनिक रूप से सुलभ नहीं होना चाहिए।

---

## स्थैतिक IP (वैकल्पिक)

डिफ़ॉल्ट रूप से, GCP एक ephemeral बाहरी IP असाइन करता है जो VM पुनरारंभ पर बदलता है। स्थिर IP बनाए रखने के लिए:

1. **VPC Network** → **IP addresses** पर जाएं
2. **Reserve external static address** पर क्लिक करें
3. इसे अपने VM इंस्टेंस के साथ असाइन करें

---

## डिप्लॉयमेंट के बाद

### पासवर्ड बदलें

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### सभी कंटेनर देखें

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```
