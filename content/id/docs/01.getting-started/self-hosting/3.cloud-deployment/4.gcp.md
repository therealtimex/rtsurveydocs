---
weight: 4
title: "Google Cloud (GCP)"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-16T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "travel_explore"
toc: true
description: "Terapkan rtCloud di Google Cloud Compute Engine menggunakan skrip startup gcp-compute.sh."
---

Gunakan `gcp-compute.sh` sebagai **Startup script** saat membuat instans VM Compute Engine. Skrip berjalan secara otomatis pada booting pertama.

**Unduh skrip:** [gcp-compute.sh](/scripts/gcp-compute.sh)

---

## Langkah 1 — Isi konfigurasi

Buka skrip dan edit blok `CONFIGURATION` di bagian atas:

```bash
# --- Diperlukan ---
PROJECT_ID="rtsurvey"
ADMIN_PASSWORD="admin"                       # Ubah setelah login pertama

# --- Domain + SSL ---
DOMAIN="myapp.example.com"
LETSENCRYPT_EMAIL="admin@example.com"

# --- Keycloak Tertanam ---
EMBED_KEYCLOAK="true"
KEYCLOAK_ADMIN_PASSWORD="${ADMIN_PASSWORD}"  # Default ke ADMIN_PASSWORD
```

| Bidang | Diperlukan | Deskripsi |
|--------|-----------|-----------|
| `PROJECT_ID` | Ya | Digunakan sebagai nama database dan ID klien Keycloak. Huruf kecil, tanpa spasi. |
| `ADMIN_PASSWORD` | Tidak | Kata sandi admin aplikasi dan kata sandi admin Keycloak. Default ke `admin` — **ubah setelah login pertama**. |
| `DOMAIN` | Tidak | Domain Anda untuk HTTPS. Biarkan kosong untuk mode HTTP saja. |
| `LETSENCRYPT_EMAIL` | Ya (jika DOMAIN ditetapkan) | Email untuk notifikasi Let's Encrypt. |
| `EMBED_KEYCLOAK` | Tidak | `true` untuk menerapkan Keycloak tertanam (memerlukan 4 GB RAM). |

> **Keamanan:** Semua kata sandi default ke `admin`. Ubah segera setelah login pertama Anda.

---

## Langkah 2 — Buat instans VM

Di [Google Cloud Console](https://console.cloud.google.com/compute):

1. Klik **Create instance**
2. **Konfigurasi mesin:**
   - Seri: `E2`
   - Jenis mesin: `e2-medium` (4 GB RAM) atau lebih besar
3. **Boot disk:**
   - Sistem operasi: Ubuntu
   - Versi: Ubuntu 22.04 LTS
   - Ukuran: 40 GB atau lebih
4. **Firewall:** centang **Allow HTTP traffic** dan **Allow HTTPS traffic**
5. **Opsi lanjutan** → **Management** → **Automation** → **Startup script** → tempel konten skrip lengkap
6. Klik **Create**

---

## Langkah 3 — Tambahkan A record DNS

Sementara VM melakukan booting, tambahkan **A record** di penyedia DNS Anda:

```
Type  : A
Name  : myapp
Value : <vm-external-ip>
TTL   : 300
```

Temukan IP eksternal di daftar instans VM di konsol.

---

## Langkah 4 — Pantau kemajuan

Menggunakan CLI `gcloud`:

```bash
gcloud compute ssh <instance-name> -- tail -f /var/log/rtcloud-setup.log
```

Atau SSH langsung:

```bash
ssh <username>@<vm-external-ip>
tail -f /var/log/rtcloud-setup.log
```

---

## Langkah 5 — Akses aplikasi

Ketika pengaturan selesai, log menampilkan ringkasan dengan URL aplikasi dan kredensial Anda. Masuk dengan nama pengguna `admin` dan kata sandi `admin`, lalu ubah kata sandi Anda segera.

---

## Aturan Firewall

Kotak centang **Allow HTTP/HTTPS** GCP membuka port 80 dan 443. Untuk juga mengizinkan akses Shiny langsung di port 3838, tambahkan aturan firewall:

```bash
gcloud compute firewall-rules create allow-shiny \
  --allow tcp:3838 \
  --target-tags http-server
```

Atau tambahkan melalui konsol: **VPC Network** → **Firewall** → **Create rule**.

> **Jangan** buka port 3306 (MySQL) — tidak boleh dapat diakses secara publik.

---

## IP Statis (opsional)

Secara default, GCP menetapkan IP eksternal sementara yang berubah saat VM di-restart. Untuk mempertahankan IP yang stabil:

1. Buka **VPC Network** → **IP addresses**
2. Klik **Reserve external static address**
3. Tetapkan ke instans VM Anda

---

## Setelah Penerapan

### Ubah kata sandi

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Lihat semua container

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```
