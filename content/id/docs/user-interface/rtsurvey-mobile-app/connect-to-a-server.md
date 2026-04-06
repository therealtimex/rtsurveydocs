---
title: "Menghubungkan ke server"
description: "Pelajari cara menghubungkan aplikasi mobile rtSurvey ke server proyek Anda, mengakses fungsionalitas khusus peran, dan mulai berkolaborasi dalam survei di beberapa proyek."
icon: "cloud_sync"
date: "2023-05-22T00:34:57+01:00"
lastmod: "2023-05-22T00:34:57+01:00"
draft: false
weight: 313
---

Menghubungkan aplikasi rtSurvey ke server adalah langkah penting untuk mulai menggunakan aplikasi ini untuk pengumpulan, manajemen, dan analisis data. Proses ini memastikan bahwa semua peran survei dapat mengakses fungsionalitas dan data yang diperlukan secara real-time.

## Perbedaan Utama dari ODK Collect

rtSurvey menawarkan fungsionalitas yang ditingkatkan dibandingkan dengan ODK Collect, melayani berbagai peran survei:
- **Administrator**: Pesan, notifikasi pembaruan (kiriman data, laporan baru, akun baru), pengisian formulir, dan melihat laporan analisis.
- **Manajer Proyek**: Fungsionalitas serupa dengan Administrator, termasuk pengaturan dan manajemen proyek.
- **Perancang Survei**: Pesan, notifikasi, pengisian formulir, dan melihat laporan analisis.
- **Enumerator Lapangan**: Pengisian formulir, pesan, notifikasi, dan laporan kemajuan.
- **Analis Data**: Pesan, notifikasi, dan akses ke laporan analitik.

## Langkah-langkah Menghubungkan Aplikasi rtSurvey ke Server

### 1. Pastikan Anda Memiliki Akun

Untuk terhubung ke server, Anda memerlukan akun. Akun dapat dibuat oleh Administrator atau oleh staf menggunakan URL pembuatan akun yang disiapkan oleh Administrator.

### 2. Buka Aplikasi rtSurvey

Luncurkan aplikasi rtSurvey di perangkat mobile Anda. Jika Anda belum memasangnya, lihat halaman [Memasang Aplikasi rtSurvey](#installing-rtsurvey-app).

### 3. Akses Pengaturan Koneksi Server

1. Buka aplikasi dan navigasi ke menu pengaturan.
2. Pilih opsi untuk terhubung ke server.

### 4. Masukkan Detail Akun dan Pilih Proyek

Saat terhubung ke rtSurvey, prosesnya disederhanakan berdasarkan konfigurasi akun Anda:

- **Nama pengguna**: Masukkan nama pengguna akun Anda.
- **Kata sandi**: Masukkan kata sandi akun Anda.

Setelah memasukkan kredensial Anda:

- Jika akun Anda dikaitkan hanya dengan satu proyek survei:
  - Aplikasi akan otomatis masuk ke server proyek tersebut.
  - Anda tidak perlu memasukkan URL server atau memilih proyek secara manual.

- Jika akun Anda dikaitkan dengan beberapa proyek survei:
  - Setelah autentikasi berhasil, Anda akan melihat daftar proyek yang dapat Anda akses.
  - Pilih proyek yang ingin Anda kerjakan dari daftar ini.

### 5. Autentikasi

Setelah memasukkan detail server, ketuk tombol "Hubungkan" atau "Masuk". Aplikasi akan mengautentikasi kredensial Anda dan menjalin koneksi ke server.

```mermaid
flowchart TD
    A["📱 Mulai Aplikasi rtSurvey"] --> B["🔑 Masukkan Nama Pengguna<br>dan Kata Sandi"]
    style A fill:#4CAF50,stroke:#666666,stroke-width:3px,color:white
    style B fill:#2196F3,stroke:#666666,stroke-width:3px,color:white

    B --> C{"🌳 Beberapa<br>proyek?"}
    style C fill:#FFC107,stroke:#666666,stroke-width:3px,color:black

    C -->|Ya| D["📋 Tampilkan daftar<br>proyek"]
    C -->|Tidak| E["🔄 Hubungkan otomatis ke<br>proyek tunggal"]
    style D fill:#FF9800,stroke:#666666,stroke-width:3px,color:white
    style E fill:#009688,stroke:#666666,stroke-width:3px,color:white

    D --> F["👆 Pengguna memilih<br>proyek"]
    style F fill:#FF5722,stroke:#666666,stroke-width:3px,color:white

    E --> G["☁️ Terhubung ke server"]
    F --> G
    style G fill:#3F51B5,stroke:#666666,stroke-width:3px,color:white
    G --> H["👥 Akses fungsionalitas<br>khusus peran"]
    style H fill:#9C27B0,stroke:#666666,stroke-width:3px,color:white

    H --> I["👨‍💼 Administrator/<br>Manajer Proyek"]
    H --> J["🎨 Perancang Survei"]
    H --> K["📝 Enumerator Lapangan"]
    H --> L["📊 Analis Data"]
    style I fill:#E91E63,stroke:#666666,stroke-width:3px,color:white
    style J fill:#795548,stroke:#666666,stroke-width:3px,color:white
    style K fill:#607D8B,stroke:#666666,stroke-width:3px,color:white
    style L fill:#8BC34A,stroke:#666666,stroke-width:3px,color:white

    I --> M["💬 Pesan<br>🔔 Notifikasi<br>📄 Pengisian Formulir<br>📈 Melihat Laporan"]
    J --> N["💬 Pesan<br>🔔 Notifikasi<br>🧪 Pengujian Formulir<br>📈 Melihat Laporan"]
    K --> O["📝 Pengisian Formulir<br>💬 Pesan<br>🔔 Notifikasi<br>📊 Laporan Kemajuan"]
    L --> P["💬 Pesan<br>🔔 Notifikasi<br>📊 Laporan Analitik"]
    style M fill:#FF4081,stroke:#666666,stroke-width:3px,color:white
    style N fill:#9E9E9E,stroke:#666666,stroke-width:3px,color:white
    style O fill:#00BCD4,stroke:#666666,stroke-width:3px,color:white
    style P fill:#CDDC39,stroke:#666666,stroke-width:3px,color:white
```

## Pemecahan Masalah Koneksi

Jika Anda mengalami masalah saat menghubungkan ke server:

1. **Periksa Koneksi Internet**: Pastikan perangkat Anda terhubung ke internet.
2. **Konfirmasi Kredensial**: Pastikan nama pengguna dan kata sandi Anda benar.
3. **Restart Aplikasi**: Tutup dan buka kembali aplikasi rtSurvey.
4. **Hubungi Dukungan**: Jika masalah berlanjut, hubungi administrator sistem atau dukungan rtSurvey untuk bantuan.

## Kesimpulan

Menghubungkan aplikasi rtSurvey ke server adalah proses yang mudah yang memungkinkan Anda memanfaatkan kemampuan penuh aplikasi ini. Dengan mengikuti langkah-langkah yang diuraikan di atas, Anda dapat memastikan pengumpulan, manajemen, dan analisis data yang mulus sesuai dengan peran survei spesifik Anda.
