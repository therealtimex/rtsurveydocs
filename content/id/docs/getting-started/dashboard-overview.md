---
weight: 10
date: "2026-03-04T00:00:00+00:00"
draft: false
title: "Ikhtisar Dasbor"
icon: "home"
toc: true
description: "Memahami Dasbor Sistem RT-CPMS dan alat pemantauan proyek."
tags: ["Dasbor", "Ikhtisar", "Pemantauan"]
---

# Dasbor Sistem

Dasbor (`/cpms/cpmsDashBoard/indexNew`) berfungsi sebagai pusat komando administratif dan halaman arahan utama untuk platform Real-Time Survey (RT-CPMS).

![Pratinjau Dasbor Sistem](/images/dashboard_overview.png)

Dasbor ini dirancang untuk memberikan manajer survei gambaran langsung tentang proyek aktif, tautan cepat ke alat penting, dan pusat terpusat untuk menavigasi semua modul platform utama.

## Fitur Utama

### 1. Pemilihan Proyek & Formulir
Panel kiri berisi navigator **Formulir dan Laporan**. Area ini mencantumkan semua survei aktif di ruang kerja Anda.
* Dengan memilih survei tertentu (misalnya, *RTA - SURVEY 02*), Anda mengarahkan dasbor untuk memfokuskan pemantauan dan metrik hanya pada proyek tersebut.

### 2. Visualisasi & Filter Metrik
Di atas daftar proyek, Anda dapat beralih antara beberapa perspektif data kritis untuk memantau kemajuan pekerjaan lapangan secara real-time:
* **Hitung berdasarkan waktu mulai / waktu selesai**: Lacak kapan enumerator memulai dan menyelesaikan sesi survei mereka.
* **Hitung berdasarkan tanggal kiriman**: Pantau volume data harian keseluruhan yang masuk ke server.
* **Hitung berdasarkan nama pengguna**: Evaluasi produktivitas dan kinerja enumerator individual.
* **Peta wawancara**: Lihat distribusi geografis (GIS) tempat respons survei dikumpulkan untuk memastikan persyaratan cakupan spasial terpenuhi.

### 3. Portal Aplikasi
Bagian tengah dasbor menyediakan akses langsung ke antarmuka pengumpulan data. Tergantung pada perangkat keras enumerator Anda, Anda dapat meluncurkan atau mengarahkan mereka ke:
* **Aplikasi Web**: Untuk pengumpulan data berbasis browser.
* **Aplikasi Android**: Tautan ke Google Play Store atau APK.
* **Aplikasi iOS**: Tautan ke Apple App Store.

### 4. Pintasan Modul Langsung
Tiga tombol aksi yang menonjol memungkinkan transisi cepat ke modul operasional yang paling sering digunakan:
* **Entri Formulir & Data**: Langsung ke pengelolaan data yang dikumpulkan secara manual.
* **Analitik & Laporan**: Buka suite Business Intelligence (BI) untuk tabulasi silang dan bagan jawaban survei.
* **Konfigurasi Izin**: Sesuaikan siapa yang memiliki akses ke survei aktif dan peran apa yang mereka pegang.

### 5. Bilah Navigasi Global
Bilah kiri yang dapat diciutkan menyediakan akses ke ekosistem lengkap modul backend RT-CPMS. Dari sini, Anda dapat masuk lebih dalam ke:
* **Pengaturan**: Mengelola staf dan perangkat aktif.
* **Manajemen Pekerjaan Lapangan**: Melacak aktivitas harian enumerator.
* **Jaminan Kualitas**: Menerapkan dan meninjau aturan dan tanda QA.
* **Hasil Akhir**: Mengekspor dataset yang telah dibersihkan ke CSV, PDF, atau Stata.
