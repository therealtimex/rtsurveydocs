---
title: "Gambar"
description: "Pertanyaan gambar memungkinkan responden mengambil dan mengirimkan foto sebagai bagian dari survei."
icon: "image"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 227
---

Tipe pertanyaan gambar dalam XLSForm dan rtSurvey memungkinkan responden mengambil dan mengirimkan foto sebagai bagian dari respons survei mereka. Fitur ini sangat berguna untuk mengumpulkan data visual, mendokumentasikan pengamatan, atau memberikan bukti dalam survei lapangan.

## Spesifikasi XLSForm Dasar

| type  | name        | label                           |
|-------|-------------|--------------------------------|
| image | photo       | Ambil foto lokasi               |

Untuk detail lebih lanjut tentang tipe pertanyaan gambar dasar, lihat [spesifikasi XLSForm](https://xlsform.org/en/#question-types).

## Penggunaan

Pertanyaan gambar umum digunakan untuk:

1. Mendokumentasikan kondisi atau pengamatan lapangan
2. Menangkap bukti visual dalam studi penelitian
3. Mengumpulkan foto sebelum dan sesudah dalam penilaian dampak
4. Memverifikasi penyelesaian tugas atau kehadiran di lokasi
5. Mengumpulkan data visual untuk analisis jarak jauh

## Praktik Terbaik

1. Berikan instruksi yang jelas tentang apa yang harus difoto.
2. Pertimbangkan implikasi privasi dan informasikan responden tentang bagaimana foto mereka akan digunakan.
3. Perhatikan ukuran file dan batasan penyimpanan, terutama untuk survei di area dengan konektivitas internet terbatas.
4. Pastikan perangkat memiliki ruang penyimpanan yang cukup dan izin kamera diberikan.

## Contoh Penggunaan

Berikut adalah contoh cara menggunakan pertanyaan gambar dalam survei:

| type  | name           | label                                      | hint                                        |
|-------|----------------|--------------------------------------------|--------------------------------------------|
| image | storefront     | Ambil foto pintu masuk toko                | Pastikan nama toko terlihat dengan jelas    |

## Ekstensi rtSurvey

Meskipun spesifikasi XLSForm dasar untuk pertanyaan gambar sederhana, rtSurvey mungkin menawarkan fitur atau kustomisasi tambahan:

1. Pengaturan kualitas gambar (misalnya, resolusi rendah, sedang, tinggi)
2. Opsi untuk menambahkan keterangan atau tag pada gambar
3. Pengambilan beberapa gambar untuk satu pertanyaan
4. Integrasi dengan aplikasi kamera asli atau galeri perangkat

## Penanganan Data

Gambar yang dikumpulkan melalui tipe pertanyaan ini biasanya:

1. Disimpan dalam format gambar umum (misalnya, JPG, PNG)
2. Disimpan bersama data survei lainnya, seringkali dalam folder media terpisah
3. Dapat diakses untuk dilihat dan dianalisis melalui platform manajemen survei

## Pertimbangan untuk Analisis

Saat menggunakan pertanyaan gambar, pertimbangkan:

1. Bagaimana gambar akan dianalisis (misalnya, tinjauan manual, analisis gambar otomatis)
2. Ruang penyimpanan tambahan yang diperlukan untuk file gambar
3. Tindakan privasi dan perlindungan data untuk menyimpan dan menangani foto
4. Potensi kebutuhan alat pengeditan atau pengorganisasian gambar dalam fase analisis

## Keterbatasan

- File gambar bisa besar, yang dapat memengaruhi transfer data dan penyimpanan.
- Tidak semua perangkat mungkin memiliki kamera berkualitas tinggi atau ruang penyimpanan yang cukup.
- Menganalisis sejumlah besar gambar bisa memakan waktu.
- Mungkin ada kekhawatiran privasi saat mengambil gambar, terutama di tempat umum.
