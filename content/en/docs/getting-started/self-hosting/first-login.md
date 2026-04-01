---
weight: 5
title: "First Login"
date: "2026-04-01T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "login"
toc: true
description: "How to log in to your rtSurvey instance for the first time after deployment."
---

> **SSL must be configured before logging in.** If you access the app over HTTP, you will see a security warning and SSO will be blocked. Complete [Set Up SSL](ssl-setup) first.

After SSL is active, open your browser at your HTTPS URL:

```
https://your-domain.com
```

---

## The login screen

<!-- SCREENSHOT NEEDED: login page over HTTPS — username/password form + SSO button -->

The login page shows:

- **Username** and **Password** fields
- A **Sign In** button
- A **Log In with SSO** button (below a divider) — for team members with SSO accounts

---

## Default admin credentials

Enter the default credentials and click **Sign In**:

| Field | Value |
|-------|-------|
| Username | `admin` |
| Password | `admin` |

> **Change your password immediately after your first login.**

---

## If you see a security warning

If you access the app over HTTP (before SSL is configured), you will see:

- A yellow warning banner at the top of the login page
- A modal when you click **Sign In**, warning that credentials will be sent unencrypted

<!-- SCREENSHOT NEEDED: HTTP warning banner on login page -->
<!-- SCREENSHOT NEEDED: SSL warning modal with "Set up SSL" and "Continue anyway" buttons -->

Click **Set up SSL** to configure HTTPS, or **Continue anyway** to log in without SSL (not recommended).

SSO login is blocked entirely over HTTP — clicking **Log In with SSO** will show a notice instead of redirecting.

---

## After logging in

Once inside, you will land on the dashboard. From here:

1. **Change the admin password** — account settings → change password
2. **Create your first project** — Projects → New Project
3. **Upload or build a form** — Forms → Upload XLSForm or open Form Builder
4. **Add users** — Users → Invite or create accounts for your team
