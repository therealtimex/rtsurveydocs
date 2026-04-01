---
weight: 4
title: "Set Up SSL"
date: "2026-04-01T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "lock"
toc: true
description: "Configure HTTPS for your rtSurvey server. Required before you can log in."
---

SSL must be configured before you can log in. When you open the app for the first time, you will be redirected to the SSL setup screen automatically.

---

## SSL setup options

![SSL setup options](/img/ssl-setup/ssl-setup-options.png)

Choose one of three options:

| Option | When to use |
|--------|-------------|
| **Free rtsurvey.com subdomain** *(Recommended)* | No DNS setup needed. We create the record for you. Ready in 2–5 minutes. |
| **My own domain** | You already have a domain and its DNS points to this server. |
| **Install certificate manually** | Enterprise or custom CA. Requires SSH access. |

---

## Option 1 — Free rtsurvey.com subdomain *(Recommended)*

This is the fastest option. No domain registration or DNS changes required.

1. Click **Free rtsurvey.com subdomain** to expand the section
2. Type your desired subdomain name in the input field

   > Use lowercase letters, numbers, and hyphens. 3–30 characters.
   > Example: `myproject` → `myproject.rtsurvey.com`

3. Click **Create https://[subdomain].rtsurvey.com**

<!-- SCREENSHOT NEEDED: subdomain input filled in, before clicking Create -->

4. Wait 2–5 minutes while the certificate is issued

<!-- SCREENSHOT NEEDED: certificate being issued / progress state -->

5. Once the certificate is ready, you will be redirected to your new HTTPS URL automatically

<!-- SCREENSHOT NEEDED: success state / redirect to login -->

---

## Option 2 — My own domain

Use this if you have an existing domain and its DNS `A` record already points to this server's IP.

1. Click **My own domain** to expand the section
2. Enter your full domain name (e.g. `survey.myorganization.org`)
3. Click **Create certificate**

<!-- SCREENSHOT NEEDED: own domain input form -->

Let's Encrypt will verify your domain and issue a certificate. This requires DNS to be correctly pointed first — the request will fail otherwise.

---

## Option 3 — Install certificate manually

For enterprise environments or custom certificate authorities. Requires SSH access to the server.

<!-- SCREENSHOT NEEDED: manual certificate form -->

---

## Next step

Once SSL is active, proceed to [First Login](first-login).
