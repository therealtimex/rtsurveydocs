---
weight: 1
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
title: "Mulai Cepat"
icon: "play_circle"
toc: true
description: "Deploy rtCloud di server Anda sendiri dalam hitungan menit menggunakan skrip cloud otomatis."
---

Panduan ini membantu Anda menjalankan rtCloud di server sendiri. Skrip otomatis menangani segalanya — Docker, SSL, database, firewall — dalam satu kali jalankan.

## Persyaratan

### Server

| Sumber Daya | Minimum | Direkomendasikan |
|-------------|---------|-----------------|
| RAM | 2 GB | 4 GB (diperlukan jika menggunakan Keycloak SSO) |
| Disk | 25 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPUs |
| OS | Ubuntu 22.04 LTS | Ubuntu 22.04 LTS |

### Domain

Anda membutuhkan nama domain dengan **A record yang mengarah ke IP server** sebelum menjalankan skrip. Let's Encrypt memerlukan resolusi DNS untuk penerbitan sertifikat SSL.

---

## Pilih Penyedia Cloud Anda

Pilih penyedia di bawah ini. Masing-masing memiliki skrip otomatis yang berjalan saat boot pertama dan menyelesaikan pengaturan dalam **5–10 menit**.

| Penyedia | Panduan |
|---------|--------|
| Linode (Akamai) | [Deploy di Linode](../cloud-deployment/linode) — termudah, pengaturan berbasis formulir via StackScript |
| DigitalOcean | [Deploy di DigitalOcean](../cloud-deployment/digitalocean) |
| AWS EC2 | [Deploy di AWS](../cloud-deployment/aws) |
| Google Cloud | [Deploy di GCP](../cloud-deployment/gcp) |

> **Direkomendasikan untuk sebagian besar pengguna:** Mulai dengan Linode — StackScript memberikan UI berbasis formulir sehingga tidak perlu mengedit apa pun secara manual.
