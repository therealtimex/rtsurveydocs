---
weight: 3
title: "Penerapan Cloud"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-16T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "cloud_upload"
toc: true
description: "Terapkan rtCloud ke penyedia cloud utama dengan skrip otomatis untuk DigitalOcean, AWS EC2, Google Cloud, dan Linode."
---

Repositori deployment menyertakan skrip provisi otomatis untuk penyedia cloud utama. Setiap skrip berjalan saat boot pertama server Ubuntu 22.04 LTS baru dan melakukan pengaturan yang sepenuhnya otomatis:

- Installs Docker and Docker Compose
- Generates secure random passwords for all internal services
- Writes `docker-compose.production.yml` and `.env`
- Configures Nginx as a reverse proxy
- Obtains a free TLS certificate from Let's Encrypt (auto-retries until DNS resolves)
- Configures the UFW firewall
- Optionally deploys the embedded Keycloak SSO server
- Outputs a full deployment summary with all credentials

Setup completes in **5–10 minutes** on a standard instance.

---

## Choosing a Script

There are multiple script variants depending on your cloud provider and SSO setup:

| Script | Provider | SSO Mode | Best For |
|--------|----------|----------|----------|
| `digitalocean-droplet-keycloak-embed.sh` | DigitalOcean | Built-in Keycloak | Simple, self-contained SSO |
| `digitalocean-droplet.sh` | DigitalOcean | Keycloak or External OIDC | Full control |
| `linode-stackscript-keycloak-embed.sh` | Linode | Built-in Keycloak | Form-based setup, simplest |
| `linode-stackscript-oidc.sh` | Linode | External OIDC only | Existing identity provider |
| `linode-stackscript.sh` | Linode | Keycloak or External OIDC | Full control |
| `aws-ec2.sh` | AWS EC2 | Keycloak or External OIDC | AWS deployments |
| `gcp-compute.sh` | Google Cloud | Keycloak or External OIDC | GCP deployments |

> **Recommended for most users:** Use the `keycloak-embed` variant. It includes a built-in Keycloak identity server and requires the fewest configuration fields.

---

## Server Sizing Guide

| Use Case | RAM | Disk | Example |
|----------|-----|------|---------|
| Evaluation / development | 2 GB | 25 GB | DO Basic $18/mo, t3.small, e2-small |
| Small team (< 50 users) | 4 GB | 40 GB | DO Basic $24/mo, t3.medium, e2-medium |
| Production (> 50 users) | 8 GB | 80 GB | DO General $48/mo, t3.large, n2-standard-2 |

> Embedded Keycloak requires at least **4 GB RAM**. Use 2 GB only for evaluation without Keycloak.

---

## DNS Setup

All scripts require a domain with an **A record pointing to your server's IP** before Let's Encrypt can issue a certificate.

The script prints your server IP early in the setup process:

```
============================================================
 Server IP : 139.162.51.85
 Add this DNS A record now if you haven't already:
   myapp.example.com  ->  139.162.51.85
 The script will retry Certbot every 60s until DNS resolves.
============================================================
```

The script **automatically retries** Let's Encrypt every 60 seconds for up to 1 hour. Just add the DNS record and wait — no restart needed.

> **Rate limit:** Let's Encrypt allows a maximum of **5 certificates per domain per 7 days**. Avoid deploying and destroying servers repeatedly with the same domain. If you hit the limit, the script will display a `retry after` timestamp and stop immediately.

---

## Post-Deployment Checklist

- [ ] App opens at `https://your-domain.com`
- [ ] Log in with `admin` and the password you configured
- [ ] All containers are healthy: `docker compose -f /opt/rtcloud/docker-compose.production.yml ps`
- [ ] Let's Encrypt renewal works: `certbot renew --dry-run`
- [ ] MySQL port 3306 is **not** exposed: `ufw status`
- [ ] Set up a daily database backup (see [Maintenance](../maintenance))

---

## Troubleshooting

### Check the full setup log

```bash
# Linode
tail -200 /var/log/stackscript.log

# DigitalOcean / AWS / GCP
tail -200 /var/log/rtcloud-setup.log
```

### Let's Encrypt rate limit

If you see `too many certificates` in the log, you have hit the 5 certificates/7 days limit. The log shows the exact retry time:

```
[SSL] ERROR: Let's Encrypt rate limit hit. retry after 2026-03-15 16:22 UTC.
```

Wait until that time, then redeploy.

### Keycloak stays unhealthy

Ensure the server has at least 4 GB RAM, then check logs:

```bash
docker logs rtcloud-keycloak --tail 50
free -h
```

### SSL config not applied after certbot

If the certificate was issued but Nginx still shows HTTP only, check the log for the error line and manually reload Nginx:

```bash
nginx -t && systemctl reload nginx
```
