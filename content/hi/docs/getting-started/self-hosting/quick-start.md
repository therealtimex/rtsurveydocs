---
weight: 1
title: "त्वरित प्रारंभ"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "play_circle"
toc: true
description: "Docker Compose का उपयोग करके 10 मिनट से कम में अपने स्वयं के सर्वर पर rtCloud चलाएं।"
---

यह मार्गदर्शिका आपको स्क्रैच से Linux सर्वर पर एक स्व-होस्टेड rtCloud इंस्टेंस तैनात करने के माध्यम से ले जाती है। अंत में, आपके पास एक चलता हुआ rtCloud होगा जो आपके ब्राउज़र में सुलभ होगा।

## पूर्वापेक्षाएं

शुरू करने से पहले सुनिश्चित करें कि आपका सर्वर निम्नलिखित आवश्यकताओं को पूरा करता है:

### हार्डवेयर

| संसाधन | न्यूनतम | अनुशंसित |
|----------|---------|-------------|
| RAM | 2 GB | 4 GB |
| Disk | 10 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPUs |

### सॉफ़्टवेयर

| सॉफ़्टवेयर | संस्करण |
|----------|---------|
| OS | Ubuntu 20.04 LTS या नया (या Docker समर्थन के साथ कोई भी Linux) |
| Docker | 20.10 या नया |
| Docker Compose | v2.x (`docker compose`) या v1.x (`docker-compose`) |

**Ubuntu पर Docker इंस्टॉल करें:**

```bash
curl -fsSL https://get.docker.com | sh
```

इंस्टॉलेशन सत्यापित करें:

```bash
docker --version
docker compose version
```

---

## चरण 1 — फ़ाइलें प्राप्त करें

डिप्लॉयमेंट रिपॉज़िटरी अपने सर्वर पर क्लोन करें:

```bash
git clone ssh://git@rtgit.rta.vn:2224/rtlab/rtwebteam/rta-smart-survey-docker.git rtcloud
cd rtcloud
```

---

## चरण 2 — पर्यावरण कॉन्फ़िगर करें

सैंपल कॉन्फ़िगरेशन फ़ाइल कॉपी करें:

```bash
cp .env.production.sample .env
```

`.env` को टेक्स्ट एडिटर में खोलें और आवश्यक मान भरें:

```dotenv
# इस डिप्लॉयमेंट के लिए अद्वितीय पहचानकर्ता (कोई स्पेस नहीं, कोई विशेष वर्ण नहीं)
PROJECT_ID=myproject

# डोमेन या IP पता जहाँ उपयोगकर्ता ऐप एक्सेस करेंगे
# उदाहरण: rtcloud.example.com  या  192.168.1.100
PROJECT_URL=rtcloud.example.com

# प्रोटोकॉल: यदि आपके पास SSL के साथ डोमेन है तो "https" का उपयोग करें, अन्यथा "http"
HTTP_PROTOCOL=https

# मजबूत, अद्वितीय पासवर्ड — शुरू करने से पहले तीनों बदलें
MYSQL_PASSWORD=change_me_strong_password
MYSQL_ROOT_PASSWORD=change_me_root_password
ADMIN_PASSWORD=change_me_admin_password
```

> **महत्वपूर्ण:** केवल `.env` Docker Compose द्वारा स्वचालित रूप से पढ़ा जाता है। `.env.production` नामक फ़ाइल न बनाएं, क्योंकि इससे भ्रम होगा। `ADMIN_PASSWORD` केवल नए डेटाबेस के **पहले बूट** पर लागू होता है।

---

## चरण 3 — कंटेनर शुरू करें

सभी सेवाओं को बैकग्राउंड में लॉन्च करें:

```bash
docker compose -f docker-compose.production.yml up -d
```

पहली स्टार्टअप में **3–5 मिनट** लगती है जबकि Docker:

1. rtCloud एप्लिकेशन इमेज पुल करता है (~1 GB डाउनलोड)
2. MySQL डेटाबेस शुरू करता है
3. बेस स्कीमा लोड करता है
4. सभी लंबित डेटाबेस माइग्रेशन चलाता है

रियल टाइम में स्टार्टअप प्रगति मॉनिटर करें:

```bash
docker compose -f docker-compose.production.yml logs -f rtcloud
```

जब तक आपको यह न दिखे कि एप्लिकेशन तैयार है तब तक प्रतीक्षा करें। आप कंटेनर हेल्थ स्थिति भी देख सकते हैं:

```bash
watch docker compose -f docker-compose.production.yml ps
```

---

## चरण 4 — एप्लिकेशन एक्सेस करें

एक बार दोनों कंटेनर `Up (healthy)` दिखाएं, अपना ब्राउज़र खोलें:

```
http://<PROJECT_URL>:8080
```

administrator खाते का उपयोग करके लॉग इन करें:

| फ़ील्ड | मान |
|-------|-------|
| उपयोगकर्ता नाम | `admin` |
| पासवर्ड | `.env` में `ADMIN_PASSWORD` के लिए सेट किया गया मान |

> पहले लॉगिन के बाद account settings पेज से admin पासवर्ड तुरंत बदलें।

---

## चरण 5 — सभी सेवाएं सत्यापित करें

जांचें कि सभी कंटेनर चल रहे हैं और स्वस्थ हैं:

```bash
docker compose -f docker-compose.production.yml ps
```

अपेक्षित आउटपुट:

```
NAME                    IMAGE                                   STATUS
rtcloud-app             rtawebteam/rta-smartsurvey:...          Up (healthy)
rtcloud-mysql           mysql:8.0                               Up (healthy)
```

यदि कोई कंटेनर `Up (starting)` या `Up (unhealthy)` दिखाता है, तो 30–60 और सेकंड प्रतीक्षा करें और फिर से जांचें। MySQL को पहले बूट पर पूरी तरह से शुरू होने में एक मिनट तक लग सकता है।

---

## पोर्ट संदर्भ

| पोर्ट | सेवा | विवरण |
|------|---------|-------------|
| `8080` | rtCloud App | मुख्य वेब UI (`APP_PORT` के माध्यम से कॉन्फ़िगर करने योग्य) |
| `3838` | Shiny Server | एनालिटिक्स और R-आधारित विज़ुअलाइज़ेशन (`SHINY_PORT` के माध्यम से कॉन्फ़िगर करने योग्य) |

MySQL (पोर्ट 3306) और कोई भी वैकल्पिक सेवाएं (Keycloak) केवल आंतरिक हैं और डिफ़ॉल्ट रूप से होस्ट के सामने उजागर नहीं हैं।

---

## अगले चरण

आपका rtCloud इंस्टेंस अब चल रहा है। इन फॉलो-अप कार्यों पर विचार करें:

- **HTTPS सक्षम करें** — अपने सर्वर पर एक डोमेन पॉइंट करें और Let's Encrypt के साथ SSL कॉन्फ़िगर करें। स्वचालित HTTPS सेटअप के लिए [Cloud Deployment](cloud-deployment) देखें।
- **सभी सेटिंग्स की समीक्षा करें** — प्रोडक्शन के लिए अपनी डिप्लॉयमेंट ट्यून करने के लिए [Configuration Reference](configuration) ब्राउज़ करें।
- **SSO सेटअप करें** — केंद्रीकृत उपयोगकर्ता प्रमाणीकरण के लिए एक पहचान प्रदाता कनेक्ट करें। [SSO Authentication](sso-authentication) देखें।
- **बैकअप की योजना बनाएं** — बैकअप और अपग्रेड प्रक्रियाओं के लिए [Maintenance](maintenance) पेज की समीक्षा करें।
