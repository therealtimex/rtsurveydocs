---
weight: 2
title: "कॉन्फ़िगरेशन संदर्भ"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "settings"
toc: true
description: "स्व-होस्टेड rtCloud डिप्लॉयमेंट को कॉन्फ़िगर करने के लिए उपयोग किए जाने वाले सभी पर्यावरण चरों का पूर्ण संदर्भ।"
---

सभी कॉन्फ़िगरेशन आपके डिप्लॉयमेंट डायरेक्टरी की जड़ में `.env` फ़ाइल में पर्यावरण चरों के माध्यम से किया जाता है। Docker Compose इस फ़ाइल को स्वचालित रूप से पढ़ता है — कोई `--env-file` फ्लैग की आवश्यकता नहीं है।

**आवश्यक** चिह्नित चर कंटेनर शुरू करने से पहले सेट किए जाने चाहिए। बाकी सभी के डिफ़ॉल्ट हैं और वैकल्पिक हैं।

---

## परियोजना

ये चर आपके rtCloud इंस्टेंस की पहचान और एक्सेस पॉइंट को परिभाषित करते हैं।

| चर | डिफ़ॉल्ट | आवश्यक | विवरण |
|----------|---------|----------|-------------|
| `PROJECT_ID` | — | **हां** | इस डिप्लॉयमेंट के लिए अद्वितीय पहचानकर्ता। कोई स्पेस या विशेष वर्ण नहीं। आंतरिक नामकरण के लिए उपसर्ग के रूप में उपयोग किया जाता है। |
| `PROJECT_URL` | — | **हां** | डोमेन नाम या IP पता जहाँ उपयोगकर्ता ऐप एक्सेस करते हैं (जैसे `rtcloud.example.com` या `192.168.1.100`)। |
| `PROJECT_TYPE` | `rtsurvey` | नहीं | सक्रिय करने के लिए प्लेटफ़ॉर्म वैरिएंट। विकल्प: `rtwork`, `rtsurvey`, `rthome`। |
| `PROJECT_PORT` | `80` | नहीं | वह पोर्ट जिस पर एप्लिकेशन कंटेनर के अंदर सुनता है। जब तक आप जानते न हों कि आप क्या कर रहे हैं, इसे न बदलें। |
| `HTTP_PROTOCOL` | `https` | नहीं | आंतरिक URL बनाने के लिए उपयोग किया जाने वाला प्रोटोकॉल। यदि आप SSL का उपयोग नहीं कर रहे हैं तो `http` पर सेट करें। |

---

## डेटाबेस

MySQL कनेक्शन क्रेडेंशियल। डेटाबेस MySQL कंटेनर द्वारा स्वचालित रूप से प्रबंधित किया जाता है — आपको केवल मजबूत पासवर्ड सेट करने की आवश्यकता है।

| चर | डिफ़ॉल्ट | आवश्यक | विवरण |
|----------|---------|----------|-------------|
| `MYSQL_DATABASE` | `smartsurvey` | नहीं | एप्लिकेशन डेटाबेस का नाम। |
| `MYSQL_USER` | `smartsurvey` | नहीं | एप्लिकेशन के लिए MySQL उपयोगकर्ता। |
| `MYSQL_PASSWORD` | — | **हां** | `MYSQL_USER` के लिए पासवर्ड। एक मजबूत, अद्वितीय मान का उपयोग करें। |
| `MYSQL_ROOT_PASSWORD` | — | **हां** | MySQL रूट पासवर्ड। डेटाबेस इनिशियलाइज़ेशन और admin ऑपरेशन के लिए आवश्यक। |
| `MYSQL_HOST` | `mysql` | नहीं | MySQL होस्टनाम। डिफ़ॉल्ट का उपयोग करें जब तक आप बाहरी डेटाबेस से कनेक्ट नहीं कर रहे। |
| `MYSQL_PORT` | `3306` | नहीं | MySQL पोर्ट। |

---

## Admin खाता

Admin खाता नए डेटाबेस के पहले बूट पर स्वचालित रूप से बनाया जाता है।

| चर | डिफ़ॉल्ट | आवश्यक | विवरण |
|----------|---------|----------|-------------|
| `ADMIN_PASSWORD` | `admin` | **हां** | अंतर्निहित `admin` उपयोगकर्ता के लिए पासवर्ड। पहले बूट से पहले इसे सेट करें। यदि डेटाबेस पहले से मौजूद है तो इसका कोई प्रभाव नहीं होता। |

> पहले लॉगिन के बाद, वेब UI में **Account Settings** पेज से admin पासवर्ड बदलें।

---

## पोर्ट

नियंत्रित करें कि एप्लिकेशन किन होस्ट पोर्ट से बंधता है।

| चर | डिफ़ॉल्ट | विवरण |
|----------|---------|-------------|
| `APP_PORT` | `8080` | मुख्य वेब UI के लिए होस्ट पोर्ट। यदि आपके सर्वर पर पोर्ट 8080 पहले से उपयोग में है तो बदलें। |
| `SHINY_PORT` | `3838` | Shiny एनालिटिक्स सर्वर के लिए होस्ट पोर्ट। |

---

## रनटाइम

| चर | डिफ़ॉल्ट | विवरण |
|----------|---------|-------------|
| `RUN_ENV` | `prod` | रनटाइम परिवेश। प्रोडक्शन डिप्लॉयमेंट के लिए `prod`, स्थानीय विकास के लिए `dev` का उपयोग करें। |
| `RUN_MODE` | `admin` | कंटेनर भूमिका। `admin` पूरा स्टैक (वेब + क्यू + क्रॉन) चलाता है। `worker` केवल बैकग्राउंड प्रोसेसिंग चलाता है (क्षैतिज स्केलिंग के लिए)। |
| `TZ` | `Asia/Ho_Chi_Minh` | सर्वर टाइमज़ोन। लॉग टाइमस्टैम्प, क्रॉन शेड्यूल और तिथि प्रदर्शन को प्रभावित करता है। [TZ डेटाबेस नाम](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) का उपयोग करें (जैसे `UTC`, `America/New_York`, `Europe/London`)। |
| `LOG_LEVEL` | `info` | एप्लिकेशन लॉग विस्तार। विकल्प: `debug`, `info`, `warning`, `error`। |
| `COMPOSE_PROJECT_NAME` | `rtcloud` | सभी Docker कंटेनर और वॉल्यूम नामों पर लागू उपसर्ग। एक ही होस्ट पर कई rtCloud इंस्टेंस चलाते समय बदलें। |
| `RESTART_POLICY` | `unless-stopped` | Docker कंटेनर पुनरारंभ व्यवहार। विकल्प: `no`, `always`, `on-failure`, `unless-stopped`। |
| `RTCLOUD_IMAGE` | `rtawebteam/rta-smartsurvey:survey-dockerize` | उपयोग करने के लिए Docker इमेज। किसी विशिष्ट संस्करण को पिन करने के लिए टैग बदलें। |
| `REQUIRE_LICENSE` | `false` | स्टार्टअप पर लाइसेंस कुंजी सत्यापन सक्षम करें। लाइसेंस जानकारी के लिए RTA से संपर्क करें। |

---

## सुरक्षा

| चर | डिफ़ॉल्ट | विवरण |
|----------|---------|-------------|
| `CSRF_VALIDATION_ENABLED` | `true` | CSRF टोकन सत्यापन सक्षम करें। प्रोडक्शन में इसे `true` रखें। केवल स्थानीय विकास में `false` पर सेट करें यदि आपको `400 CSRF token could not be verified` त्रुटियां मिलती हैं। |
| `GII_ENABLED` | `false` | Yii फ्रेमवर्क कोड जेनरेटर टूल सक्षम करें। **प्रोडक्शन में कभी भी सक्षम न करें।** |

---

## SSO — एम्बेडेड Keycloak

पूर्ण-विशेषताओं वाले एंटरप्राइज़ SSO के लिए बंडल किए गए Keycloak कंटेनर को सक्षम करें। HTTPS के साथ डोमेन की आवश्यकता है।

| चर | डिफ़ॉल्ट | विवरण |
|----------|---------|-------------|
| `EMBED_KEYCLOAK` | `false` | एम्बेडेड Keycloak कंटेनर शुरू करने के लिए `true` पर सेट करें। `embed-keycloak` Docker Compose प्रोफ़ाइल सक्रिय करता है। |
| `KEYCLOAK_URL` | — | Keycloak सर्वर का पूर्ण URL (जैसे `https://rtcloud.example.com/auth`)। |
| `KEYCLOAK_REALM` | — | Keycloak realm नाम (जैसे `rtsurvey`)। |
| `KEYCLOAK_CLIENT_ID` | — | rtCloud एप्लिकेशन के लिए Keycloak क्लाइंट ID। |
| `KEYCLOAK_CLIENT_SECRET` | — | Keycloak क्लाइंट सीक्रेट। इसे Keycloak admin कंसोल से जेनरेट करें। |
| `KEYCLOAK_ADMIN_USER` | `admin` | Keycloak administrator उपयोगकर्ता नाम। |
| `KEYCLOAK_ADMIN_PASSWORD` | — | Keycloak administrator पासवर्ड। |
| `KEYCLOAK_DB` | `keycloak` | Keycloak के लिए डेटाबेस नाम। पहले बूट पर स्वचालित रूप से बनाया जाता है। |
| `KEYCLOAK_DB_USER` | `keycloak` | Keycloak के लिए डेटाबेस उपयोगकर्ता। |
| `KEYCLOAK_DB_PASSWORD` | — | Keycloak उपयोगकर्ता के लिए डेटाबेस पासवर्ड। |
| `KC_HOSTNAME` | — | Keycloak फ्रंटएंड URL (जैसे `https://rtcloud.example.com/auth`)। |
| `KC_HOSTNAME_STRICT` | `false` | सख्त होस्टनाम मिलान लागू करें। निश्चित डोमेन के साथ प्रोडक्शन में `true` पर सेट करें। |

पूर्ण सेटअप गाइड के लिए [SSO Authentication](sso-authentication#embedded-keycloak) देखें।

---

## SSO — बाहरी OIDC प्रदाता

किसी मौजूदा OIDC-संगत पहचान प्रदाता (Supabase, Auth0, Authentik, Okta, आदि) से कनेक्ट करें।

| चर | डिफ़ॉल्ट | विवरण |
|----------|---------|-------------|
| `OIDC_ISSUER_URL` | — | OIDC issuer discovery URL (जैसे `https://accounts.google.com`)। |
| `OIDC_CLIENT_ID` | — | आपके पहचान प्रदाता में पंजीकृत क्लाइंट ID। |
| `OIDC_CLIENT_SECRET` | — | आपके पहचान प्रदाता से क्लाइंट सीक्रेट। |
| `OIDC_SCOPE` | `openid profile email` | अनुरोध करने के लिए OIDC स्कोप की स्पेस-अलग सूची। |
| `OIDC_REDIRECT_URI` | — | वेब ऐप के लिए कॉलबैक URL (जैसे `https://rtcloud.example.com/auth/callback`)। |
| `OIDC_MOBILE_CLIENT_ID` | — | rtSurvey मोबाइल ऐप के लिए अलग क्लाइंट ID। |
| `OIDC_MOBILE_REDIRECT_URI` | — | मोबाइल ऐप कॉलबैक URI (जैसे `vn.rta.rtsurvey.auth://callback`)। |
| `OPEN_REGISTRATION` | `false` | उन उपयोगकर्ताओं के लिए स्वचालित रूप से rtCloud खाते बनाएं जो पहली बार OIDC के माध्यम से प्रमाणित होते हैं। |
| `OIDC_AUTHORIZATION_ENDPOINT` | — | authorization endpoint URL ओवरराइड करें (discovery का उपयोग करने के लिए खाली छोड़ें)। |
| `OIDC_TOKEN_ENDPOINT` | — | token endpoint URL ओवरराइड करें (discovery का उपयोग करने के लिए खाली छोड़ें)। |
| `OIDC_USERINFO_ENDPOINT` | — | userinfo endpoint URL ओवरराइड करें (discovery का उपयोग करने के लिए खाली छोड़ें)। |

---

## SSO — Azure Active Directory

| चर | विवरण |
|----------|-------------|
| `AZURE_CLIENT_ID` | Azure AD एप्लिकेशन (क्लाइंट) ID। |
| `AZURE_TENANT_ID` | Azure AD डायरेक्टरी (टेनेंट) ID। |

---

## वैकल्पिक एकीकरण

### Stata

| चर | डिफ़ॉल्ट | विवरण |
|----------|---------|-------------|
| `STATA_ENABLED` | `false` | डेटा विश्लेषण के लिए Stata सांख्यिकीय सॉफ़्टवेयर एकीकरण सक्षम करें। |
| `STATA_BIN_PATH` | `/usr/bin/stata` | कंटेनर के अंदर Stata बाइनरी का पूर्ण पथ। |

### Elasticsearch

| चर | विवरण |
|----------|-------------|
| `ES_HOST` | Elasticsearch होस्ट (जैसे `http://elasticsearch:9200`)। |
| `ES_PORT` | Elasticsearch पोर्ट। |

### Matomo Analytics

| चर | विवरण |
|----------|-------------|
| `PIWIK_URL` | Matomo (Piwik) सर्वर URL। |
| `PIWIK_ID` | Matomo साइट ID। |
| `PIWIK_SECRET` | Matomo प्रमाणीकरण टोकन। |

### OpenCPU (R Computation)

| चर | विवरण |
|----------|-------------|
| `OCPU_HOST` | R-आधारित सांख्यिकीय गणना के लिए OpenCPU सर्वर URL। |

### RtBox Integration

| चर | विवरण |
|----------|-------------|
| `RTBOX_HOST` | RtBox सेवा होस्ट URL। |
| `RTBOX_USER_API` | RtBox उपयोगकर्ता API कुंजी। |
| `RTBOX_BASIC_AUTH` | RtBox के लिए बेसिक प्रमाणीकरण क्रेडेंशियल। |

### Matrix Messaging

| चर | विवरण |
|----------|-------------|
| `MATRIX_HOMESERVER_HOST` | Matrix homeserver होस्ट। |
| `MATRIX_HOMESERVER_PORT` | Matrix homeserver पोर्ट। |

---

## डेटा वॉल्यूम

सभी एप्लिकेशन डेटा नामित Docker वॉल्यूम में संग्रहीत है। वॉल्यूम पहले स्टार्टअप पर स्वचालित रूप से बनाए जाते हैं और कंटेनर पुनरारंभ और अपडेट के दौरान बने रहते हैं।

| वॉल्यूम | माउंट पॉइंट | सामग्री |
|--------|-------------|----------|
| `rtcloud_mysql_data` | `/var/lib/mysql` | MySQL डेटाबेस फ़ाइलें |
| `rtcloud_uploads` | `…/uploads` | सर्वेक्षण उत्तरदाताओं द्वारा अपलोड की गई फ़ाइलें |
| `rtcloud_audios` | `…/audios` | ऑडियो रिकॉर्डिंग |
| `rtcloud_downloads` | `…/downloads` | जेनरेट की गई निर्यात फ़ाइलें |
| `rtcloud_gallery` | `…/gallery` | गैलरी छवियां |
| `rtcloud_voicemail` | `…/voicemail` | वॉयसमेल रिकॉर्डिंग |
| `rtcloud_analytics` | `…/analytics` | एनालिटिक्स डेटा |
| `rtcloud_aggregate` | `…/aggregate` | एकत्रित सर्वेक्षण परिणाम |
| `rtcloud_converter` | `…/converter` | डेटा रूपांतरण आउटपुट |
| `rtcloud_shiny_data` | `/srv/shiny-server/smartsurvey` | Shiny सर्वर R स्क्रिप्ट |
| `rtcloud_shiny_logs` | `/var/log/shiny-server` | Shiny सर्वर लॉग |
| `rtcloud_assets` | `…/assets` | वेब एसेट (CSS, JS) |
| `rtcloud_runtime` | `…/protected/runtime` | एप्लिकेशन रनटाइम कैश |
| `rtcloud_cache` | `…/cache` | एप्लिकेशन कैश |
| `rtcloud_tmp` | `…/tmp` | अस्थायी फ़ाइलें |

वॉल्यूम नाम `COMPOSE_PROJECT_NAME` के मान (डिफ़ॉल्ट: `rtcloud`) से उपसर्गित हैं।

अपनी डिप्लॉयमेंट के लिए सभी वॉल्यूम सूचीबद्ध करें:

```bash
docker volume ls | grep rtcloud
```
