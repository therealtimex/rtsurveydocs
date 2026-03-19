---
weight: 1
title: "DigitalOcean"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-17T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "water_drop"
toc: true
description: "Terapkan rtCloud di DigitalOcean Droplet menggunakan skrip user-data otomatis."
---

DigitalOcean menggunakan skrip **User Data** yang berjalan otomatis pada booting pertama. Anda mengisi variabel konfigurasi di bagian atas skrip, lalu menempel seluruh skrip saat membuat Droplet.

> Tidak seperti StackScript Linode, DigitalOcean tidak memiliki UI formulir — Anda harus mengedit skrip secara langsung sebelum menempel.

**Unduh skrip:** [digitalocean-droplet-keycloak-embed.sh](/scripts/digitalocean-droplet-keycloak-embed.sh)

---

## Keycloak Tertanam (Direkomendasikan)

Gunakan `digitalocean-droplet-keycloak-embed.sh` untuk pengaturan paling sederhana dengan SSO bawaan.

### Langkah 1 — Isi konfigurasi

Buka skrip dan edit blok `CONFIGURATION` di bagian atas:

```bash
# --- Diperlukan ---
PROJECT_ID="rtsurvey"                  # Pengidentifikasi unik untuk proyek Anda (tanpa spasi)
ADMIN_PASSWORD="admin"                 # Kata sandi untuk admin aplikasi dan Keycloak — ubah setelah login pertama

# --- Domain + SSL ---
DOMAIN="myapp.example.com"            # Domain Anda — A record DNS harus mengarah ke sini
PROJECT_URL=""                         # Biarkan kosong kecuali di belakang Cloudflare/proxy
LETSENCRYPT_EMAIL="admin@example.com" # Email untuk notifikasi Let's Encrypt

# --- Opsional ---
STATA_ENABLED="false"
TZ="Asia/Ho_Chi_Minh"
```

| Bidang | Diperlukan | Deskripsi |
|--------|-----------|-----------|
| `PROJECT_ID` | Ya | Digunakan sebagai nama database dan ID klien Keycloak. Huruf kecil, tanpa spasi. |
| `ADMIN_PASSWORD` | Tidak | Kata sandi untuk login admin aplikasi dan konsol admin Keycloak. Default ke `admin` — **ubah setelah login pertama**. |
| `DOMAIN` | Ya | Nama domain Anda. A record DNS harus mengarah ke IP Droplet. |
| `LETSENCRYPT_EMAIL` | Ya | Alamat email untuk notifikasi sertifikat Let's Encrypt. |
| `PROJECT_URL` | Tidak | Timpa URL publik. Biarkan kosong untuk menggunakan `DOMAIN`. Berguna di belakang Cloudflare. |

> **Keamanan:** Semua kata sandi default ke `admin`. Ubah segera setelah login pertama Anda.

### Langkah 2 — Buat Droplet

Di [panel kontrol DigitalOcean](https://cloud.digitalocean.com):

1. Klik **Create** → **Droplets**
2. Pilih **Ubuntu 22.04 LTS** sebagai image
3. Pilih **Basic, 4 GB RAM / 2 vCPU** atau lebih besar
4. Gulir ke **Advanced Options** → centang **Add Initialization scripts**
5. Tempel konten skrip lengkap ke area teks
6. Klik **Create Droplet**

### Langkah 3 — Tambahkan A record DNS

Sementara Droplet melakukan booting, tambahkan **A record** di penyedia DNS Anda:

```
Type  : A
Name  : myapp          (atau @ untuk domain root)
Value : <droplet-ip>
TTL   : 300
```

### Langkah 4 — Pantau kemajuan

SSH ke Droplet dan pantau log:

```bash
ssh root@<droplet-ip>
tail -f /var/log/rtcloud-setup.log
```

Skrip mencetak IP server Anda di dekat awal — tambahkan A record DNS segera setelah Anda melihatnya.

### Langkah 5 — Akses aplikasi

Ketika pengaturan selesai, log menampilkan ringkasan:

```
============================================================
 rtCloud deployment complete! (Embedded Keycloak)
============================================================
 App URL   : https://myapp.example.com
 Admin     : admin / admin
 Keycloak  : https://myapp.example.com/auth/admin

 !! SECURITY: All passwords default to 'admin'.
    Change them immediately after first login.
============================================================
```

Buka `https://myapp.example.com` di browser Anda dan masuk dengan nama pengguna `admin` dan kata sandi `admin`.

> **Ubah kata sandi Anda** segera setelah login melalui **Pengaturan** di menu kanan atas.

---

## Setelah Penerapan

### Ubah kata sandi

SSH ke Droplet, edit `.env`, dan restart container yang terpengaruh:

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Perbarui domain

Jika Anda menetapkan domain yang berbeda setelah penerapan, perbarui `PROJECT_URL` di `.env`:

```bash
nano /opt/rtcloud/.env   # perbarui PROJECT_URL=
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Lihat semua container

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```
