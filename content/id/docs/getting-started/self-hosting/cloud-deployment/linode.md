---
weight: 2
title: "Linode (Akamai Cloud)"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "dns"
toc: true
description: "Terapkan rtCloud pada Linode menggunakan StackScript. Tidak diperlukan konfigurasi — cukup buat server dan ikuti langkah-langkah pasca penerapan."
---

## Langkah 1 — Luncurkan StackScript

**[Deploy rtSurvey on Linode →](https://cloud.linode.com/stackscripts/2049143)**

Ini akan membuka halaman StackScript di Linode Cloud Manager. Klik **Terapkan Linode Baru**.

---

## Langkah 2 — Isi formulir Linode

Isi formulir pembuatan server standar Linode:

| Bidang | Nilai yang direkomendasikan |
|-------|------------------|
| **Gambar** | Ubuntu 22.04 LTS |
| **Wilayah** | Paling dekat dengan pengguna Anda |
| **Rencana** | CPU Bersama 4 GB atau lebih besar |
| **Kata Sandi Akar** | Tetapkan kata sandi yang kuat |
| **Firewall** | Tanpa Firewall *(disarankan)* |
| **Zona Waktu** *(satu-satunya bidang kami)* | Zona waktu server Anda (default: `Asia/Ho_Chi_Minh`) |

> **Mengapa tidak ada firewall?** Skrip pengaturan memerlukan akses internet keluar (tarikan Docker, Let's Encrypt). Memblokir port saat boot pertama dapat menyebabkan penerapan gagal. Anda dapat memasang firewall setelah penyiapan selesai — lihat [Aturan firewall](#firewall-rules-linode-cloud-firewall) di bawah untuk mengetahui aturan yang benar.

Click **Create Linode** when done.

---

## Langkah 3 — Tunggu hingga penyiapan selesai

Skrip berjalan secara otomatis pada boot pertama. Ia menginstal Docker, menarik image rtSurvey, menginisialisasi database, dan memulai semua layanan. Proses ini memerlukan waktu **5–10 menit**.

Anda dapat melihat kemajuannya langsung di **Linode Cloud Manager** — tidak memerlukan SSH:

1. Go to your [Linode dashboard](https://cloud.linode.com/linodes)
2. Klik Linode yang baru Anda buat
3. Klik **Luncurkan Konsol LISH** (kanan atas halaman detail Linode)

Terminal browser terbuka dan menampilkan log boot langsung — tab **Weblish** berfungsi langsung di browser Anda, tidak diperlukan klien SSH.

![Lish Console showing rtSurvey StackScript running](/img/first-login/lish-console.png)

Tunggu sampai Anda melihat:

```
============================================================
 rtSurvey deployment complete!
============================================================
 Server IP : <your-server-ip>

 App URL   : http://<your-server-ip>  (HTTP only until domain is set)
 Admin     : admin / admin
============================================================
```

Log juga menunjukkan IP server Anda — Anda akan memerlukannya untuk langkah berikutnya.

---

## Langkah 4 — Siapkan SSL

Open your browser at `http://<server-ip>`. The app will redirect you to the SSL setup screen.

Ikuti **[Panduan Konfigurasi SSL →](../ssl-setup)** untuk mengonfigurasi HTTPS. **Subdomain rtsurvey.com** gratis adalah opsi tercepat — tidak perlu penyiapan DNS.

---

## Langkah 5 — Ubah kata sandi default

Semua kata sandi default adalah `admin`. Ubah segera setelah login pertama Anda:

- **Kata sandi admin aplikasi** — pengaturan akun di dalam aplikasi
- **Keycloak admin** — accessible at `https://your-domain.com/auth/admin` (login: `admin` / `admin`)

---

## Aturan Firewall (Linode Cloud Firewall)

Jika Anda memasang Linode Cloud Firewall ke server ini, gunakan aturan berikut:

### Masuk

| Label | Aksi | Protokol | Pelabuhan | Sumber | Catatan |
|-------|--------|----------|------|---------|-------|
| `terima-masuk-ssh` | Terima | TCP | 22 | Semua IPv4, Semua IPv6 | Akses SSH |
| `terima-masuk-http` | Terima | TCP | 80 | Semua IPv4, Semua IPv6 | Nginx (tantangan HTTP + ACME) |
| `terima-masuk-https` | Terima | TCP | 443 | Semua IPv4, Semua IPv6 | Nginx (HTTPS setelah pengaturan SSL) |
| `terima-masuk-mengkilap` | Terima | TCP | 3838 | Semua IPv4, Semua IPv6 | Server Mengkilap (analisis R) |
| `terima-masuk-icmp` | Terima | ICMP | — | Semua IPv4, Semua IPv6 | Ping / diagnostik |
| Kebijakan masuk default | **Jatuhkan** | | | | Blokir yang lainnya |

### Keluar

| Label | Aksi | Catatan |
|-------|--------|-------|
| Kebijakan keluar default | **Terima** | Izinkan semua keluar (tarikan Docker, certbot, GoDaddy API, dll.) |

### Port TIDAK diperlukan secara eksternal

Port ini terikat hanya pada `127.0.0.1` dan tidak pernah dapat dijangkau dari luar server:

| Pelabuhan | Layanan | Alasan |
|------|---------|--------|
| 8080 | Wadah aplikasi | Nginx memproksinya secara internal |
| 8090 | Wadah Keycloak | Nginx memproksinya secara internal |
| 3306 | MySQL | Hanya jaringan internal Docker |

---

## Pemecahan masalah

### Periksa log pengaturan

```bash
tail -200 /var/log/stackscript.log
```

### Periksa log SSL

```bash
tail -200 /var/log/rtsurvey-ssl.log
```

### Lihat status penampung

```bash
docker compose -f /opt/rtsurvey/docker-compose.production.yml ps
```
