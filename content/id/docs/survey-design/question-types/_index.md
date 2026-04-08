---
title: "Tipe pertanyaan"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 220
---

rtSurvey mendukung semua tipe pertanyaan XLSForm standar, ditambah beberapa ekstensi. Setiap tipe pertanyaan mengontrol jenis data apa yang dikumpulkan dan bagaimana widget input dirender pada perangkat.

Untuk mengatur tipe pertanyaan, masukkan nama tipe dalam kolom `type` dari lembar kerja **survey** dalam XLSForm Anda.

## Input teks

| Tipe | Deskripsi |
|------|-----------|
| [text](text) | Respons teks bebas — karakter apa pun diperbolehkan |
| [integer](integer) | Bilangan bulat (tanpa desimal) |
| [decimal](decimal) | Angka dengan tempat desimal |
| [range](range) | Angka yang dipilih dari slider dalam rentang min/maks yang ditentukan |

## Pilihan

| Tipe | Deskripsi |
|------|-----------|
| [select_one listname](select-one) | Pilih tepat satu opsi dari daftar |
| [select_multiple listname](select-multiple) | Pilih satu atau lebih opsi dari daftar |
| [rank listname](rank) | Urutkan pilihan berdasarkan preferensi atau prioritas |

## Tanggal dan Waktu

| Tipe | Deskripsi |
|------|-----------|
| [date](date) | Tanggal kalender (tahun, bulan, hari) |
| [time](time) | Waktu (jam, menit) |
| [datetime](datetime-date-time) | Tanggal dan waktu gabungan |

## Lokasi

| Tipe | Deskripsi |
|------|-----------|
| [geopoint](geopoint) | Koordinat GPS tunggal (lintang, bujur, ketinggian, akurasi) |
| [geotrace](geotrace) | Jalur — serangkaian titik GPS yang membentuk garis |
| [geoshape](geoshape) | Area — poligon tertutup dari titik-titik GPS |

## Media

| Tipe | Deskripsi |
|------|-----------|
| [image](image) | Pengambilan foto atau unggah gambar |
| [audio](audio) | Perekaman audio |
| [video](video) | Perekaman video |
| [file](file) | Unggahan file umum (PDF, dokumen, dll.) |

## Lainnya

| Tipe | Deskripsi |
|------|-----------|
| [barcode](barcode) | Pindai barcode atau kode QR |
| [note](note) | Teks tampilan hanya-baca — menampilkan instruksi atau ringkasan yang dihitung |
| [calculate](calculate) | Bidang tersembunyi yang menyimpan nilai yang dihitung |
| [hidden](hidden) | Bidang tersembunyi yang menyimpan nilai statis atau yang diisi sebelumnya |
| [trigger / acknowledge](trigger) | Kotak centang yang harus ditandai enumerator untuk mengkonfirmasi mereka telah membaca pernyataan |
| [meta](meta) | Metadata otomatis: cap waktu, ID perangkat, info enumerator |

## Ekstensi rtSurvey

Tipe-tipe ini khusus untuk rtSurvey dan bukan bagian dari spesifikasi XLSForm standar.

| Tipe | Deskripsi |
|------|-----------|
| [search-autocomplete](search-autocomplete) | Input teks dengan saran pelengkapan otomatis berbasis API secara real-time |
| [mentions](mentions) | Kolom teks dengan pelengkapan otomatis `@` untuk menandai entitas secara inline |
| [texttags](texttags) | Input tag — setiap entri menjadi chip yang dapat dihapus; disimpan sebagai string yang dipisahkan spasi |

Untuk grup pengulangan, lihat [Repeats](../advanced-extension/repeats)

## Bagaimana tipe dan appearance bekerja bersama

`type` menentukan **data apa yang dikumpulkan**. Kolom `appearance` mengontrol **bagaimana tampilan widget**. Banyak tipe mendukung beberapa appearance — misalnya `select_one` dapat muncul sebagai tombol radio, dropdown, skala Likert, atau grid kompak.

Lihat [Appearance](../appearance) untuk daftar lengkap opsi.
