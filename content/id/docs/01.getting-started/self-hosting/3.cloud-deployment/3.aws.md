---
weight: 3
title: "AWS EC2"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-16T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "cloud"
toc: true
description: "Terapkan rtCloud di instans AWS EC2 menggunakan skrip user data aws-ec2.sh."
---

Gunakan `aws-ec2.sh` sebagai skrip **User Data** saat meluncurkan instans EC2. Skrip berjalan secara otomatis pada booting pertama.

**Unduh skrip:** [aws-ec2.sh](/scripts/aws-ec2.sh)

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

## Langkah 2 — Luncurkan instans EC2

Di [konsol AWS EC2](https://console.aws.amazon.com/ec2):

1. Klik **Launch instance**
2. **AMI:** Ubuntu Server 22.04 LTS (64-bit x86)
3. **Jenis instans:** `t3.medium` (4 GB RAM) atau lebih besar
4. **Pasangan kunci:** Pilih atau buat satu untuk akses SSH
5. **Pengaturan jaringan:** Buat atau pilih Security Group (lihat di bawah)
6. **Detail lanjutan** → **User data** → tempel konten skrip lengkap
7. Klik **Launch instance**

---

## Langkah 3 — Konfigurasikan Security Group

Buka port berikut di Security Group instans:

| Port | Protokol | Sumber | Tujuan |
|------|----------|--------|--------|
| 22 | TCP | IP Anda | Akses SSH |
| 80 | TCP | 0.0.0.0/0 | HTTP (dialihkan ke HTTPS oleh Nginx) |
| 443 | TCP | 0.0.0.0/0 | HTTPS |
| 3838 | TCP | 0.0.0.0/0 | Akses langsung Shiny |

> **Jangan** buka port 3306 (MySQL) — tidak boleh dapat diakses secara publik.

---

## Langkah 4 — Tambahkan A record DNS

Sementara instans melakukan booting, tambahkan **A record** di penyedia DNS Anda:

```
Type  : A
Name  : myapp
Value : <instance-public-ip>
TTL   : 300
```

---

## Langkah 5 — Pantau kemajuan

```bash
ssh ubuntu@<instance-ip>
tail -f /var/log/rtcloud-setup.log
```

---

## Langkah 6 — Akses aplikasi

Ketika pengaturan selesai, log menampilkan ringkasan dengan URL aplikasi dan kredensial Anda. Masuk dengan nama pengguna `admin` dan kata sandi `admin`, lalu ubah kata sandi Anda segera.

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

### Tetapkan Elastic IP (opsional)

Jika Anda menghentikan dan memulai instans, IP publik akan berubah. Untuk mempertahankan IP yang stabil, alokasikan **Elastic IP** dan kaitkan dengan instans di konsol EC2.
