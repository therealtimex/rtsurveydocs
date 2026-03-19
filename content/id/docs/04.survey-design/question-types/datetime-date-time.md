---
title: "Datetime, tanggal, waktu"
description: "Pertanyaan datetime memungkinkan responden memasukkan tanggal dan waktu dalam satu bidang."
icon: "event"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 226
---

Tipe pertanyaan datetime dalam XLSForm dan rtSurvey memungkinkan responden memasukkan tanggal dan waktu dalam satu bidang. Tipe pertanyaan ini berguna ketika Anda perlu menangkap momen tertentu dalam waktu, termasuk tanggal dan waktu yang tepat.

## Spesifikasi XLSForm Dasar

| type     | name           | label                           |
|----------|----------------|---------------------------------|
| datetime | event_datetime | Kapan peristiwa itu terjadi?    |

Untuk detail lebih lanjut tentang tipe pertanyaan datetime dasar, lihat [spesifikasi XLSForm](https://xlsform.org/en/#question-types).

## Penggunaan

Pertanyaan datetime umum digunakan untuk:

1. Merekam cap waktu peristiwa atau pengamatan
2. Menjadwalkan janji atau pertemuan
3. Mencatat waktu mulai dan berakhir dari aktivitas
4. Menangkap momen tepat untuk pengumpulan data yang sensitif terhadap waktu

## Ekstensi rtSurvey

rtSurvey memperluas fungsionalitas pertanyaan datetime dengan berbagai appearance dan opsi kustomisasi:

### Opsi Appearance

- `(default)`: Tampilkan kalender dan jam untuk memilih tanggal dan waktu
- `inline`: Tampilkan kalender dan jam sebagai ikon
- `inline-1line`: Tampilkan kalender dan jam untuk dipilih dalam format satu baris
- `inline-onlyresult`: Tampilkan kalender dan jam sebagai ikon di akhir baris; ikon menghilang setelah dipilih

### Kustomisasi Warna

Anda dapat menyesuaikan warna ikon kalender dan jam menggunakan fungsi `colors()`:

- `inline colors("0099FF")`: Tampilkan ikon dengan warna kustom
- `inline-1line-0000FF`: Tampilkan dalam format satu baris dengan warna kustom
- `inline-1line colors("0000FF","FFFF00")`: Tampilkan dalam format satu baris dengan beberapa warna kustom
- `inline-onlyresult colors("0099FF")`: Tampilkan ikon yang menghilang setelah dipilih, dengan warna kustom

### Format Tanggal dan Waktu Kustom

rtSurvey memungkinkan format tanggal dan waktu kustom menggunakan sintaks khusus:

- `inline-[%Y-%m-%d %H:%M:%S]`: Contoh format kustom (Tahun-Bulan-Hari Jam:Menit:Detik)
- `inline-[%d/%m/%Y %I:%M %p]`: Contoh format kustom (Hari/Bulan/Tahun Jam:Menit AM/PM)

## Contoh Penggunaan

Berikut adalah contoh cara menggunakan pertanyaan datetime dalam survei:

| type     | name           | label                                      | appearance                    |
|----------|----------------|--------------------------------------------|-------------------------------|
| datetime | incident_time  | Kapan insiden itu terjadi?                 | inline-[%d/%m/%Y %I:%M %p]   |

## Praktik Terbaik

1. Berikan instruksi yang jelas tentang format tanggal dan waktu yang diharapkan.
2. Pertimbangkan menggunakan appearance `inline` untuk tampilan yang lebih kompak.
3. Gunakan format kustom ketika Anda memerlukan komponen atau pemformatan tanggal dan waktu tertentu.
4. Perhatikan zona waktu saat mengumpulkan data datetime di berbagai wilayah.

## Keterbatasan

- Beberapa appearance atau format kustom mungkin tidak didukung di semua perangkat atau platform.
- Pengguna mungkin memerlukan panduan tentang cara memasukkan tanggal dan waktu dengan benar, terutama dengan format kustom.
- Perbedaan zona waktu dapat mempersulit analisis data jika tidak diperhitungkan dengan benar.
