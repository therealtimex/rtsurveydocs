---
weight: 1
title: "Mulai Cepat"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "play_circle"
toc: true
description: "Jalankan rtCloud di server Anda sendiri dalam waktu kurang dari 10 menit menggunakan Docker Compose."
---

Panduan ini memandu Anda dalam menerapkan instans rtCloud yang di-hosting sendiri di server Linux dari awal. Di akhir panduan, Anda akan memiliki rtCloud yang berjalan dan dapat diakses di browser Anda.

## Prasyarat

Pastikan server Anda memenuhi persyaratan berikut sebelum memulai:

### Perangkat Keras

| Sumber Daya | Minimum | Direkomendasikan |
|-------------|---------|------------------|
| RAM | 2 GB | 4 GB |
| Disk | 10 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPU |

### Perangkat Lunak

| Perangkat Lunak | Versi |
|-----------------|-------|
| OS | Ubuntu 20.04 LTS atau lebih baru (atau Linux apa pun dengan dukungan Docker) |
| Docker | 20.10 atau lebih baru |
| Docker Compose | v2.x (`docker compose`) atau v1.x (`docker-compose`) |

**Pasang Docker di Ubuntu:**

```bash
curl -fsSL https://get.docker.com | sh
```

Verifikasi instalasi:

```bash
docker --version
docker compose version
```

---

## Langkah 1 — Dapatkan File-file

Clone repositori penerapan ke server Anda:

```bash
git clone ssh://git@rtgit.rta.vn:2224/rtlab/rtwebteam/rta-smart-survey-docker.git rtcloud
cd rtcloud
```

---

## Langkah 2 — Konfigurasikan Lingkungan

Salin file konfigurasi sampel:

```bash
cp .env.production.sample .env
```

Buka `.env` di editor teks dan isi nilai yang diperlukan:

```dotenv
# Pengidentifikasi unik untuk penerapan ini (tanpa spasi, tanpa karakter khusus)
PROJECT_ID=myproject

# Domain atau alamat IP tempat pengguna mengakses aplikasi
# Contoh: rtcloud.example.com  atau  192.168.1.100
PROJECT_URL=rtcloud.example.com

# Protokol: gunakan "https" jika Anda memiliki domain dengan SSL, "http" jika tidak
HTTP_PROTOCOL=https

# Kata sandi yang kuat dan unik — ubah ketiganya sebelum memulai
MYSQL_PASSWORD=change_me_strong_password
MYSQL_ROOT_PASSWORD=change_me_root_password
ADMIN_PASSWORD=change_me_admin_password
```

> **Penting:** Hanya `.env` yang dibaca oleh Docker Compose secara otomatis. Jangan buat file bernama `.env.production`, karena itu akan menyebabkan kebingungan. `ADMIN_PASSWORD` hanya diterapkan pada **booting pertama** dari database baru.

---

## Langkah 3 — Mulai Container

Luncurkan semua layanan di latar belakang:

```bash
docker compose -f docker-compose.production.yml up -d
```

Startup pertama membutuhkan waktu **3–5 menit** sementara Docker:

1. Menarik image aplikasi rtCloud (~1 GB unduhan)
2. Menginisialisasi database MySQL
3. Memuat skema dasar
4. Menjalankan semua migrasi database yang tertunda

Pantau kemajuan startup secara real time:

```bash
docker compose -f docker-compose.production.yml logs -f rtcloud
```

Tunggu hingga Anda melihat output yang menunjukkan aplikasi siap. Anda juga dapat memantau status kesehatan container:

```bash
watch docker compose -f docker-compose.production.yml ps
```

---

## Langkah 4 — Akses Aplikasi

Setelah kedua container menampilkan `Up (healthy)`, buka browser Anda:

```
http://<PROJECT_URL>:8080
```

Masuk menggunakan akun administrator:

| Bidang | Nilai |
|--------|-------|
| Nama pengguna | `admin` |
| Kata sandi | Nilai yang Anda tetapkan untuk `ADMIN_PASSWORD` di `.env` |

> Ubah kata sandi admin segera setelah login pertama Anda dari halaman pengaturan akun.

---

## Langkah 5 — Verifikasi Semua Layanan

Periksa bahwa semua container berjalan dan sehat:

```bash
docker compose -f docker-compose.production.yml ps
```

Output yang diharapkan:

```
NAME                    IMAGE                                   STATUS
rtcloud-app             rtawebteam/rta-smartsurvey:...          Up (healthy)
rtcloud-mysql           mysql:8.0                               Up (healthy)
```

Jika container menampilkan `Up (starting)` atau `Up (unhealthy)`, tunggu 30–60 detik lagi dan periksa kembali. MySQL dapat membutuhkan waktu hingga satu menit untuk sepenuhnya diinisialisasi pada booting pertama.

---

## Referensi Port

| Port | Layanan | Deskripsi |
|------|---------|-----------|
| `8080` | Aplikasi rtCloud | UI web utama (dapat dikonfigurasi melalui `APP_PORT`) |
| `3838` | Shiny Server | Analitik dan visualisasi berbasis R (dapat dikonfigurasi melalui `SHINY_PORT`) |

MySQL (port 3306) dan layanan opsional apa pun (Keycloak) hanya bersifat internal dan tidak diekspos ke host secara default.

---

## Langkah Selanjutnya

Instans rtCloud Anda sekarang berjalan. Pertimbangkan tugas tindak lanjut berikut:

- **Aktifkan HTTPS** — Arahkan domain ke server Anda dan konfigurasikan SSL dengan Let's Encrypt. Lihat [Penerapan Cloud](cloud-deployment) untuk pengaturan HTTPS otomatis.
- **Tinjau semua pengaturan** — Telusuri [Referensi Konfigurasi](configuration) untuk menyesuaikan penerapan Anda untuk produksi.
- **Siapkan SSO** — Hubungkan penyedia identitas untuk autentikasi pengguna terpusat. Lihat [Autentikasi SSO](sso-authentication).
- **Rencanakan cadangan Anda** — Tinjau halaman [Pemeliharaan](maintenance) untuk prosedur cadangan dan peningkatan.
