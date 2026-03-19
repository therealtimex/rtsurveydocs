---
weight: 4
title: "SSO प्रमाणीकरण"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "lock"
toc: true
description: "एम्बेडेड Keycloak, बाहरी OIDC प्रदाता या Azure Active Directory का उपयोग करके स्व-होस्टेड rtCloud के लिए Single Sign-On कॉन्फ़िगर करें।"
---

rtCloud Single Sign-On (SSO) के लिए तीन दृष्टिकोणों का समर्थन करता है:

| विकल्प | के लिए सर्वोत्तम |
|--------|----------|
| [एम्बेडेड Keycloak](#embedded-keycloak) | ऐसे संगठन जो rtCloud के साथ बंडल किया गया पूरी तरह से स्व-युक्त SSO सर्वर चाहते हैं |
| [बाहरी OIDC प्रदाता](#external-oidc-provider) | ऐसे संगठन जो पहले से एक पहचान प्रदाता (Auth0, Authentik, Okta, Supabase, आदि) चला रहे हैं |
| [Azure Active Directory](#azure-active-directory) | ऐसे संगठन जो Microsoft 365 या Azure AD का उपयोग कर रहे हैं |

SSO कॉन्फ़िगर किए बिना, उपयोगकर्ता admin पैनल के माध्यम से प्रबंधित स्थानीय rtCloud खातों से लॉग इन करते हैं।

---

## एम्बेडेड Keycloak

डिप्लॉयमेंट में एक वैकल्पिक Keycloak कंटेनर शामिल है जो rtCloud के साथ चलता है। Keycloak rtSurvey realm के साथ पूर्व-कॉन्फ़िगर है और उपयोग के लिए तैयार है।

### आवश्यकताएं

- HTTPS के साथ एक डोमेन नाम (Keycloak को प्रोडक्शन में HTTPS की आवश्यकता है)
- सर्वर पर कम से कम 4 GB RAM (Keycloak ~512 MB मेमोरी उपयोग जोड़ता है)

### सेटअप

**1. `.env` में पर्यावरण चर कॉन्फ़िगर करें:**

```dotenv
# एम्बेडेड Keycloak कंटेनर सक्षम करें
EMBED_KEYCLOAK=true

# Keycloak URL — अपने वास्तविक डोमेन का उपयोग करें
KEYCLOAK_URL=https://rtcloud.example.com/auth
KC_HOSTNAME=https://rtcloud.example.com/auth
KC_HOSTNAME_STRICT=false

# Realm और क्लाइंट सेटिंग्स (आयातित realm JSON से मिलान करें)
KEYCLOAK_REALM=rtsurvey
KEYCLOAK_CLIENT_ID=rtsurvey-app
KEYCLOAK_CLIENT_SECRET=your-client-secret-here

# Keycloak admin क्रेडेंशियल
KEYCLOAK_ADMIN_USER=admin
KEYCLOAK_ADMIN_PASSWORD=change_me_keycloak_admin_password

# Keycloak डेटाबेस (स्वचालित रूप से बनाया जाता है)
KEYCLOAK_DB=keycloak
KEYCLOAK_DB_USER=keycloak
KEYCLOAK_DB_PASSWORD=change_me_keycloak_db_password

# Keycloak जिस पोर्ट पर सुनता है (होस्ट-साइड, Nginx द्वारा प्रॉक्सी)
KEYCLOAK_PORT=8091
```

**2. एम्बेडेड Keycloak प्रोफ़ाइल के साथ शुरू करें:**

```bash
docker compose -f docker-compose.production.yml --profile embed-keycloak up -d
```

**3. Keycloak स्वस्थ है, सत्यापित करें:**

```bash
docker compose -f docker-compose.production.yml ps
```

`rtcloud-keycloak` कंटेनर 2–3 मिनट के बाद `Up (healthy)` दिखाना चाहिए।

**4. Keycloak admin कंसोल एक्सेस करें:**

```
https://rtcloud.example.com/auth/admin
```

`KEYCLOAK_ADMIN_USER` और `KEYCLOAK_ADMIN_PASSWORD` से लॉग इन करें।

### क्या पूर्व-कॉन्फ़िगर है

एम्बेडेड Keycloak एक पूर्व-आयातित `rtsurvey` realm के साथ शुरू होता है जिसमें शामिल हैं:

- वेब एप्लिकेशन के लिए क्लाइंट कॉन्फ़िगरेशन
- डिफ़ॉल्ट उपयोगकर्ता भूमिकाएं (`admin`, `project_manager`, `enumerator`, `analyst`)
- rtSurvey के लिए अनुकूलित सत्र और टोकन सेटिंग्स

आप Keycloak admin कंसोल में सीधे उपयोगकर्ता जोड़ सकते हैं या Keycloak को एक अपस्ट्रीम पहचान प्रदाता (LDAP, SAML) से कनेक्ट कर सकते हैं।

### Nginx रूटिंग

क्लाउड डिप्लॉयमेंट स्क्रिप्ट का उपयोग करते समय, Nginx दोनों सेवाओं को प्रॉक्सी करने के लिए कॉन्फ़िगर किया जाता है:

| पथ | बैकएंड |
|------|---------|
| `/` | `127.0.0.1:8080` पर rtCloud ऐप |
| `/auth/` | `127.0.0.1:8090` पर Keycloak |

---

## बाहरी OIDC प्रदाता

rtCloud को किसी भी OpenID Connect-संगत पहचान प्रदाता से कनेक्ट करें। इस दृष्टिकोण में Keycloak कंटेनर की आवश्यकता नहीं है।

### समर्थित प्रदाता

कोई भी OIDC-अनुरूप प्रदाता काम करता है, जिसमें शामिल हैं:
- Authentik
- Auth0
- Okta
- Keycloak (बाहरी इंस्टेंस)
- Supabase
- Google (Google Workspace संगठनों के लिए)
- GitHub (OIDC एक्सटेंशन के साथ OAuth ऐप के माध्यम से)

### सेटअप

**1. अपने पहचान प्रदाता में rtCloud को एक OIDC क्लाइंट के रूप में पंजीकृत करें।**

आपको आवश्यकता होगी:
- एक **क्लाइंट ID** और **क्लाइंट सीक्रेट**
- **redirect URI** पंजीकृत करें: `https://rtcloud.example.com/auth/callback`
- मोबाइल ऐप समर्थन के लिए, यह भी पंजीकृत करें: `vn.rta.rtsurvey.auth://callback`

**2. `.env` में पर्यावरण चर कॉन्फ़िगर करें:**

```dotenv
# OIDC discovery URL (प्रदाता-विशिष्ट — अपने IdP दस्तावेज़ीकरण की जांच करें)
OIDC_ISSUER_URL=https://your-identity-provider.com

# आपके पहचान प्रदाता से क्लाइंट क्रेडेंशियल
OIDC_CLIENT_ID=rtcloud-app
OIDC_CLIENT_SECRET=your-client-secret-here

# अनुरोध करने के लिए स्कोप (openid, profile और email आमतौर पर पर्याप्त हैं)
OIDC_SCOPE=openid profile email

# आपके पहचान प्रदाता में पंजीकृत redirect URI
OIDC_REDIRECT_URI=https://rtcloud.example.com/auth/callback

# वैकल्पिक: अलग मोबाइल ऐप क्लाइंट
OIDC_MOBILE_CLIENT_ID=rtcloud-mobile
OIDC_MOBILE_REDIRECT_URI=vn.rta.rtsurvey.auth://callback

# नए OIDC उपयोगकर्ताओं के लिए स्वचालित रूप से rtCloud खाते बनाने के लिए true पर सेट करें
OPEN_REGISTRATION=false
```

**3. परिवर्तन लागू करने के लिए ऐप कंटेनर पुनः शुरू करें:**

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

### उपयोगकर्ता स्वत:-प्रावधान

जब `OPEN_REGISTRATION=true` हो, तो rtCloud स्वचालित रूप से एक स्थानीय खाता बनाता है जब कोई उपयोगकर्ता पहली बार OIDC के माध्यम से साइन इन करता है। खाता ID टोकन से उपयोगकर्ता के नाम और ईमेल से भरा जाता है।

जब `OPEN_REGISTRATION=false` (डिफ़ॉल्ट) हो, तो एक rtCloud administrator को पहले उपयोगकर्ता खाता बनाना होगा, और OIDC पहचान पहले लॉगिन पर लिंक की जाती है।

### कस्टम endpoints

यदि आपका प्रदाता OIDC discovery (`.well-known/openid-configuration`) का समर्थन नहीं करता है, तो आप endpoints मैन्युअल रूप से सेट कर सकते हैं:

```dotenv
OIDC_AUTHORIZATION_ENDPOINT=https://your-provider.com/oauth2/authorize
OIDC_TOKEN_ENDPOINT=https://your-provider.com/oauth2/token
OIDC_USERINFO_ENDPOINT=https://your-provider.com/oauth2/userinfo
```

---

## Azure Active Directory

rtCloud को अपने संगठन के Microsoft Azure AD टेनेंट के साथ एकीकृत करें।

### सेटअप

**1. [Azure Portal](https://portal.azure.com) में एक नया ऐप पंजीकृत करें:**

   - **Azure Active Directory** → **App registrations** → **New registration** पर जाएं
   - नाम: `rtCloud`
   - Redirect URI: `https://rtcloud.example.com/auth/callback` (Web प्रकार)
   - बनाने के बाद, **Application (client) ID** और **Directory (tenant) ID** नोट करें
   - **Certificates & secrets** के अंतर्गत, एक नया क्लाइंट सीक्रेट बनाएं

**2. `.env` में पर्यावरण चर कॉन्फ़िगर करें:**

```dotenv
AZURE_CLIENT_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
AZURE_TENANT_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

**3. ऐप कंटेनर पुनः शुरू करें:**

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

आपके Azure AD टेनेंट के उपयोगकर्ता अब अपने Microsoft क्रेडेंशियल का उपयोग करके rtCloud में लॉग इन कर सकते हैं।

---

## SSO अक्षम करना

स्थानीय प्रमाणीकरण पर वापस जाने के लिए, `.env` से सभी SSO-संबंधित चर हटाएं या उन पर टिप्पणी करें, फिर ऐप कंटेनर पुनः शुरू करें:

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

यदि आप एम्बेडेड Keycloak का उपयोग कर रहे थे, तो `--profile embed-keycloak` फ्लैग छोड़कर और प्रोफ़ाइल के बिना `docker compose down` के बाद `up -d` चलाकर इसे बंद करें।
