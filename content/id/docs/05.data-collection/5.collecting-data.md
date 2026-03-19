---
weight: 150
date: "2023-05-03T22:37:22+01:00"
draft: false
author: "RealTimeX"
title: "Mengumpulkan Data"
icon: "rocket_launch"
toc: true
description: "Panduan memulai cepat untuk menjalankan survei dengan rtSurvey"
publishdate: "2023-05-03T22:37:22+01:00"
tags: ["Beginners"]
---

Setelah formulir diterapkan dan enumerator ditugaskan, pengumpulan data dapat dimulai. **rtSurvey** mendukung pengumpulan data yang mulus di seluruh browser web dan aplikasi mobile khusus, memastikan fleksibilitas apakah tim Anda terhubung ke internet atau bekerja di lingkungan terpencil yang offline.

## Memilih Metode Pengumpulan yang Tepat

Tergantung pada geografi dan konektivitas proyek Anda, Anda dapat memilih metode optimal untuk enumerator Anda:

- **Browser Web (Online):** Terbaik untuk pusat panggilan, entri data berbasis kantor, atau responden yang mengisi survei mandiri publik.
- **Aplikasi Mobile rtWork / rtSurvey (Online & Offline):** Terbaik untuk operasi lapangan, area terpencil dengan internet tidak stabil, dan survei yang memerlukan lampiran media (foto, koordinat GPS, peta offline).

---

## Metode 1: Mengumpulkan Data melalui Browser Web

Menggunakan antarmuka Webform memungkinkan enumerator mulai mengumpulkan data segera tanpa menginstal perangkat lunak apa pun.

### 1. Akses URL Webform
Dari dasbor **Manage Forms** di Panel Kontrol, temukan formulir target Anda dan klik tombol **URL Webform** untuk menghasilkan tautan yang aman.

### 2. Entri Formulir
- Buka URL yang diberikan di browser web modern mana pun.
- Jika formulir memerlukan autentikasi, enumerator harus masuk menggunakan kredensial mereka. Jika diatur ke "Visibilitas Publik", mereka dapat langsung melanjutkan.
- Isi pertanyaan survei. Antarmuka akan secara otomatis menerapkan logika, pola lewati, dan aturan validasi.
- **Pengambilan Media:** Jika formulir mencakup pertanyaan gambar, audio, atau video, browser web akan meminta Anda mengunggah file dari komputer Anda atau menggunakan webcam/mikrofon perangkat jika tersedia.

### 3. Pengiriman
Setelah mencapai halaman terakhir, klik **Kirim**. Browser memerlukan koneksi internet aktif untuk menyelesaikan pengiriman. Setelah berhasil, data akan langsung tercermin di antarmuka **Manage Submissions**.

---

## Metode 2: Mengumpulkan Data melalui Aplikasi Mobile (Offline)

Untuk pengumpulan data lapangan yang tangguh, aplikasi mobile menyediakan kemampuan offline penuh.

### 1. Instal dan Autentikasi
- Unduh aplikasi **rtWork** (atau **rtSurvey**) dari Google Play Store atau Apple App Store.
- Buka aplikasi dan masuk menggunakan kredensial enumerator yang ditetapkan.

### 2. Unduh Formulir (Memerlukan Internet)
- Navigasikan ke bagian **Forms** atau **Tasks** dalam aplikasi.
- Ketuk ikon **Sync** atau **Download** untuk mengambil desain kuesioner terbaru dari server. Setelah diunduh, formulir disimpan secara lokal di perangkat.

### 3. Kumpulkan Data (Offline)
- Buka formulir yang diunduh dan mulai wawancara.
- Anda dapat mengumpulkan data sepenuhnya secara offline dengan aman.
- **Pengambilan Media:** Aplikasi mobile secara asli berintegrasi dengan perangkat keras perangkat Anda. Anda dapat mengambil foto, merekam audio, merekam video, dan mencatat koordinat GPS yang tepat langsung dalam aplikasi, bahkan tanpa koneksi internet.
- Ketika Anda selesai wawancara, finalisasi catatan. Catatan yang difinalisasi diantrekan dengan aman di kotak keluar aplikasi.

### 4. Sinkronisasi Pengiriman (Memerlukan Internet)
- Setelah enumerator kembali ke area dengan akses internet (Wi-Fi atau data seluler), mereka harus menavigasi ke antarmuka **Outbox** atau **Sync**.
- Instruksikan aplikasi untuk mengirim formulir yang difinalisasi. Aplikasi akan mentransmisikan catatan yang diantrekan dan semua file media yang dilampirkan dengan aman ke server, setelah itu mereka akan muncul dalam kisi data untuk ditinjau.
