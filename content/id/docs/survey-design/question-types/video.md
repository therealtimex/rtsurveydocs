---
title: "Video"
description: "Pertanyaan video memungkinkan responden merekam dan mengirimkan file video sebagai bagian dari survei."
icon: "videocam"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 229
---

Tipe pertanyaan `video` memungkinkan responden **merekam video** atau mengunggah file video yang sudah ada sebagai bagian dari respons survei mereka. Ini berguna untuk menangkap bukti visual, demonstrasi, kondisi lingkungan, atau informasi apa pun yang diuntungkan dari gerakan dan audio bersama.

## Spesifikasi XLSForm Dasar

| type  | name        | label                              |
|-------|-------------|-------------------------------------|
| video | demo_video  | Harap rekam demonstrasi singkat     |

Untuk detail lebih lanjut tentang tipe pertanyaan video standar, lihat [spesifikasi XLSForm](https://xlsform.org/en/#question-types).

## Penggunaan

Pertanyaan video umum digunakan untuk:

1. Mendokumentasikan kondisi lapangan — kerusakan jalan, kondisi infrastruktur, kesehatan tanaman
2. Merekam demonstrasi produk atau pemeriksaan kepatuhan prosedur
3. Mengumpulkan kesaksian video dari responden
4. Menangkap bukti yang memerlukan konteks spasial (misalnya, ukuran dan cakupan area masalah)
5. Dokumentasi sebelum/sesudah untuk survei pemantauan dan evaluasi

## Format data

File video disimpan sebagai lampiran biner:

- **Format:** MP4 atau MOV (perekaman mobile)
- **Penamaan:** `{instanceID}-{fieldname}.mp4` (atau yang setara)
- **Penyimpanan:** Diunggah ke folder media server dan ditautkan ke catatan pengiriman
- **Akses:** Dapat diputar dan diunduh dari antarmuka manajemen pengiriman

## Ekstensi rtSurvey

### Durasi maksimum

Gunakan kolom `parameters` untuk membatasi panjang perekaman:

| type | name | label | parameters |
|------|------|-------|------------|
| video | site_visit | Rekam kondisi lokasi | `max-duration=60` |

`max-duration` dalam detik. Perekaman berhenti secara otomatis pada batas.

### Kualitas / resolusi

Kontrol resolusi perekaman melalui `parameters`:

| type | name | label | parameters |
|------|------|-------|------------|
| video | evidence | Rekam bukti video | `quality=low` |

Nilai yang didukung: `low` (unggah lebih cepat), `normal` (default), `high`. Gunakan `low` di area dengan konektivitas terbatas.

### Unggah video yang ada

Di mobile, responden dapat memilih untuk **mengunggah video yang ada** dari galeri perangkat daripada merekam yang baru. Ini diaktifkan secara default dalam integrasi kamera/galeri asli.

### Pemutaran sebelum pengiriman

Di mobile, klip yang direkam dapat ditinjau sebelum melanjutkan. Tidak diperlukan konfigurasi tambahan.

## Contoh penggunaan

### Video inspeksi lokasi dengan batas

| type | name | label | hint | parameters |
|------|------|-------|------|------------|
| video | site_video | Rekam titik air | Berjalan keliling fasilitas. Maks 90 detik. | `max-duration=90 quality=normal` |

### Video kondisional — hanya jika kerusakan dilaporkan

| type | name | label | relevant | required |
|------|------|-------|----------|----------|
| select_one yesno | damage_found | Apakah ditemukan kerusakan? | | |
| video | damage_video | Rekam video kerusakan | `${damage_found} = 'yes'` | `${damage_found} = 'yes'` |

## Praktik Terbaik

1. Tetapkan `max-duration` — perekaman video tanpa batas dapat dengan mudah melebihi 100 MB dan gagal diunggah pada koneksi yang lemah.
2. Gunakan `quality=low` untuk survei pemantauan di mana bukti visual diperlukan tetapi detail halus tidak — ini secara drastis mengurangi ukuran file.
3. Tulis instruksi perekaman yang spesifik dalam kolom `hint` (misalnya, "Berjalan keliling seluruh bangunan, pegang kamera dengan stabil").
4. Pertimbangkan apakah video benar-benar diperlukan — foto (`image`) biasanya cukup untuk bukti statis dan menghasilkan file yang jauh lebih kecil.
5. Uji kinerja unggah pada jaringan lapangan yang sebenarnya sebelum penerapan.

## Keterbatasan

- File video sangat besar — video 1 menit dengan kualitas normal biasanya 20–60 MB tergantung pada perangkat.
- Mengunggah file video besar memerlukan koneksi jaringan yang baik; pertimbangkan untuk mewajibkan sinkronisasi Wi-Fi untuk formulir yang banyak video.
- Tidak semua browser web mendukung perekaman video melalui MediaRecorder — Chrome adalah yang paling andal.
- Analisis respons video bersifat manual dan memakan waktu; gunakan secukupnya dan hanya ketika konten video menambahkan nilai unik.
