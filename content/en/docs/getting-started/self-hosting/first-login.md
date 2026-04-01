---
weight: 4
title: "First Login"
date: "2026-04-01T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "login"
toc: true
description: "How to log in to your rtCloud instance for the first time after deployment."
---

> **SSL must be configured before you can log in.** If you access the app without SSL, you will see a warning and cannot proceed. Complete the [SSL setup step](cloud-deployment/linode#step-4--set-up-ssl) first.

After SSL is active, open your browser and navigate to your domain:

```
https://your-domain.com
```

You will see the **Real-Time Workspace** login screen with a single **"Log In or Register"** button.

---

## Understanding the login screen

![Login screen with SSO button](/img/first-login/login-sso-button.png)

Because the deployment uses **embedded Keycloak SSO**, the **"Log In or Register"** button redirects to the Keycloak identity provider by default. This is the normal path for end users who have SSO accounts.

To log in as the local **admin** account on first boot, you need to reveal the direct login form.

---

## How to access the direct login form

**Long-press** (hold down) the **"Log In or Register"** button for about 1–2 seconds.

- On **desktop**: hold the mouse button down on the button for 1–2 seconds
- On **mobile**: press and hold the button

The page will expand to reveal **Username** and **Password** fields directly above the SSO button.

![Direct login form after long-press](/img/first-login/login-direct-form.png)

---

## Default credentials

| Field | Value |
|-------|-------|
| Username | `admin` |
| Password | `admin` |

Enter these and click **Sign In**.

> **Change your password immediately after your first login.** Go to your account settings and set a strong password before doing anything else.

---

## After logging in

Once inside, you will land on the system dashboard. From here:

1. **Change the admin password** — account settings → change password
2. **Create your first project** — Projects → New Project
3. **Upload or build a form** — Forms → Upload XLSForm or open Form Builder
4. **Add users** — Users → Invite or create accounts for your team

For a full walkthrough of the dashboard, see [Dashboard Overview](../../dashboard-overview).
