---
weight: 2
title: "Linode (Akamai Cloud)"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "dns"
toc: true
description: "StackScript का उपयोग करके Linode पर rtCloud तैनात करें। कोई कॉन्फ़िगरेशन नहीं — बस सर्वर बनाएं और तैनाती के बाद के चरणों का पालन करें।"
---

## Step 1 — Launch the StackScript

**[Deploy rtSurvey on Linode →](https://cloud.linode.com/stackscripts/2049143)**

This opens the StackScript page in Linode Cloud Manager. Click **Deploy New Linode**.

---

## Step 2 — Fill in Linode's form

Fill in Linode's standard server creation form:

| Field | Recommended value |
|-------|------------------|
| **Image** | Ubuntu 22.04 LTS |
| **Region** | Closest to your users |
| **Plan** | Shared CPU 4 GB or larger |
| **Root Password** | Set a strong password |
| **Timezone** *(our only field)* | Your server timezone (default: `Asia/Ho_Chi_Minh`) |

Click **Create Linode** when done.

---

## Step 3 — Wait for setup to complete

The script runs automatically on first boot. It installs Docker, pulls the rtSurvey image, initialises the database, and starts all services. This takes **5–10 minutes**.

You can watch progress directly in **Linode Cloud Manager** — no SSH required:

1. Go to your [Linode dashboard](https://cloud.linode.com/linodes)
2. Click on your newly created Linode
3. Click **Launch LISH Console** (top right of the Linode detail page)

A browser terminal opens showing the live boot log — the **Weblish** tab works directly in your browser, no SSH client needed.

![Lish Console showing rtSurvey StackScript running](/img/first-login/lish-console.png)

Wait until you see:

```
============================================================
 rtSurvey deployment complete!
============================================================
 Server IP : <your-server-ip>

 App URL   : http://<your-server-ip>  (HTTP only until domain is set)
 Admin     : admin / admin
============================================================
```

The log also shows your server IP — you will need it for the next step.

---

## Step 4 — Set up SSL

Open your browser at `http://<server-ip>`. The app will redirect you to the SSL setup screen.

Follow the **[Set Up SSL guide →](../ssl-setup)** to configure HTTPS. The free **rtsurvey.com subdomain** is the fastest option — no DNS setup needed.

---

## Step 5 — First login

Once SSL is active, follow the **[First Login guide →](../first-login)** to access the admin account.

---

## Step 6 — Change the default password

All passwords default to `admin`. Change them immediately after your first login:

- **App admin password** — account settings inside the app
- **Keycloak admin** — accessible at `https://your-domain.com/auth/admin` (login: `admin` / `admin`)

---

## फ़ायरवॉल नियम (Linode Cloud Firewall)

यदि आप इस सर्वर से Linode Cloud Firewall जोड़ते हैं, तो निम्नलिखित नियमों का उपयोग करें:

### आने वाला ट्रैफ़िक (Inbound)

| लेबल | कार्रवाई | प्रोटोकॉल | पोर्ट | स्रोत | नोट्स |
|------|---------|---------|------|-------|-------|
| `accept-inbound-ssh` | स्वीकार | TCP | 22 | All IPv4, All IPv6 | SSH पहुंच |
| `accept-inbound-http` | स्वीकार | TCP | 80 | All IPv4, All IPv6 | Nginx (HTTP + ACME चुनौती) |
| `accept-inbound-https` | स्वीकार | TCP | 443 | All IPv4, All IPv6 | Nginx (SSL सेटअप के बाद HTTPS) |
| `accept-inbound-shiny` | स्वीकार | TCP | 3838 | All IPv4, All IPv6 | Shiny Server (R विश्लेषण) |
| `accept-inbound-icmp` | स्वीकार | ICMP | — | All IPv4, All IPv6 | Ping / निदान |
| डिफ़ॉल्ट इनबाउंड नीति | **ड्रॉप** | | | | बाकी सब ब्लॉक करें |

### जाने वाला ट्रैफ़िक (Outbound)

| लेबल | कार्रवाई | नोट्स |
|------|---------|-------|
| डिफ़ॉल्ट आउटबाउंड नीति | **स्वीकार** | सभी आउटबाउंड ट्रैफ़िक की अनुमति दें (Docker, certbot, GoDaddy API, आदि) |

### बाहरी रूप से आवश्यक नहीं पोर्ट

ये पोर्ट केवल `127.0.0.1` से बंधे हैं और बाहर से कभी पहुंच योग्य नहीं हैं:

| पोर्ट | सेवा | कारण |
|------|------|------|
| 8080 | ऐप कंटेनर | Nginx आंतरिक रूप से प्रॉक्सी करता है |
| 8090 | Keycloak कंटेनर | Nginx आंतरिक रूप से प्रॉक्सी करता है |
| 3306 | MySQL | केवल आंतरिक Docker नेटवर्क |

---

## Troubleshooting

### Check the setup log

```bash
tail -200 /var/log/stackscript.log
```

### Check the SSL log

```bash
tail -200 /var/log/rtsurvey-ssl.log
```

### View container status

```bash
docker compose -f /opt/rtsurvey/docker-compose.production.yml ps
```
