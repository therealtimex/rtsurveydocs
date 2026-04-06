---
weight: 1
title: "DigitalOcean"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-17T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "water_drop"
toc: true
description: "Terapkan rtCloud pada DigitalOcean Droplet menggunakan skrip data pengguna otomatis."
---

DigitalOcean menggunakan skrip **Data Pengguna** yang berjalan otomatis saat boot pertama. Anda mengisi variabel konfigurasi di bagian atas skrip, lalu menempelkan seluruh skrip saat membuat Droplet.

> Tidak seperti Linode StackScripts, DigitalOcean tidak memiliki UI bentuk — Anda harus mengedit skrip secara langsung sebelum menempelkannya.

**Download script:** [digitalocean-droplet-keycloak-embed.sh](/scripts/digitalocean-droplet-keycloak-embed.sh)

---

## Keycloak Tertanam (Disarankan)

Gunakan `digitalocean-droplet-keycloak-embed.sh` untuk penyiapan paling sederhana dengan SSO bawaan.

### Langkah 1 — Isi konfigurasi

Buka skrip dan edit blok `CONFIGURATION` di bagian atas:

```bash
# --- Required ---
PROJECT_ID="rtsurvey"                  # Unique identifier for your project (no spaces)
ADMIN_PASSWORD="admin"                 # Password for app admin and Keycloak — change after first login

# --- Domain + SSL ---
DOMAIN="myapp.example.com"            # Your domain — DNS A record must point here
PROJECT_URL=""                         # Leave blank unless behind Cloudflare/proxy
LETSENCRYPT_EMAIL="admin@example.com" # Email for Let's Encrypt notifications

# --- Optional ---
STATA_ENABLED="false"
TZ="Asia/Ho_Chi_Minh"
```

| Bidang | Diperlukan | Deskripsi |
|-------|----------|-------------|
| `ID_PROJEK` | Ya | Digunakan sebagai nama database dan ID klien Keycloak. Huruf kecil, tanpa spasi. |
| `ADMIN_PASSWORD` | Tidak | Kata sandi untuk login admin aplikasi dan konsol admin Keycloak. Defaultnya adalah `admin` — **berubah setelah login pertama**. |
| `DOMAIN` | Ya | Nama domain Anda. DNS Catatan harus mengarah ke IP Tetesan. |
| `LETSENCRYPT_EMAIL` | Ya | Alamat email untuk notifikasi sertifikat Let's Encrypt. |
| `PROJECT_URL` | Tidak | Ganti URL publik. Biarkan kosong untuk menggunakan `DOMAIN`. Berguna di balik Cloudflare. |

> **Keamanan:** Semua kata sandi default adalah `admin`. Ubah segera setelah login pertama Anda.

### Langkah 2 — Buat Tetesan

In the [DigitalOcean control panel](https://cloud.digitalocean.com):

1. Klik **Buat** → **Tetesan**
2. Pilih **Ubuntu 22.04 LTS** sebagai gambar
3. Pilih **Basic, 4 GB RAM / 2 vCPUs** atau lebih besar
4. Gulir ke **Opsi Lanjutan** → centang **Tambahkan skrip Inisialisasi**
5. Tempelkan konten skrip lengkap ke dalam area teks
6. Klik **Buat Tetesan**

### Langkah 3 — Tambahkan data DNS

Saat Droplet melakukan booting, tambahkan **A record** di penyedia DNS Anda:

```
Type  : A
Name  : myapp          (or @ for root domain)
Value : <droplet-ip>
TTL   : 300
```

### Langkah 4 — Pantau kemajuan

SSH ke dalam Droplet dan perhatikan lognya:

```bash
ssh root@<droplet-ip>
tail -f /var/log/rtcloud-setup.log
```

Skrip mencetak IP server Anda di dekat awal — tambahkan data DNS segera setelah Anda melihatnya.

### Langkah 5 — Akses aplikasi

Saat penyiapan selesai, log menampilkan ringkasan:

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

Open `https://myapp.example.com` in your browser and log in with username `admin` and password `admin`.

> **Ubah kata sandi Anda** segera setelah login melalui **Pengaturan** di menu kanan atas.

---

## Setelah Penerapan

### Ubah kata sandi

SSH ke dalam Droplet, edit `.env`, dan mulai ulang container yang terpengaruh:

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Perbarui domainnya

Jika Anda menetapkan domain berbeda setelah penerapan, perbarui `PROJECT_URL` di `.env`:

```bash
nano /opt/rtcloud/.env   # update PROJECT_URL=
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Lihat semua kontainer

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```
