---
title: "Geoshape"
description: "Pertanyaan geoshape memungkinkan responden menggambar bentuk pada peta, menangkap data geografis yang kompleks sebagai bagian dari survei."
icon: "map"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 233
---

Tipe pertanyaan geoshape dalam XLSForm dan rtSurvey memungkinkan responden menggambar bentuk (poligon) pada peta, menangkap data geografis yang kompleks. Fitur ini sangat berguna untuk memetakan area, mendefinisikan batas, atau menandai wilayah yang diminati dalam survei spasial.

## Spesifikasi XLSForm Dasar

| type     | name        | label                           |
|----------|-------------|--------------------------------|
| geoshape | field_area  | Gambar batas ladang             |

Untuk detail lebih lanjut tentang tipe pertanyaan geoshape dasar, lihat [spesifikasi XLSForm](https://xlsform.org/en/#question-types).

## Penggunaan

Pertanyaan geoshape umum digunakan untuk:

1. Pemetaan batas ladang dalam survei pertanian
2. Mendefinisikan area dampak lingkungan
3. Menandai zona dalam studi perencanaan perkotaan
4. Menguraikan wilayah untuk survei geologi
5. Menangkap fitur geografis yang kompleks untuk analisis spasial

## Praktik Terbaik

1. Pastikan layanan lokasi perangkat diaktifkan dan izin diberikan.
2. Berikan instruksi yang jelas tentang cara menggambar bentuk dan area apa yang harus disertakan.
3. Pertimbangkan menggunakan citra satelit atau peta dasar untuk membantu responden menggambar bentuk secara akurat.
4. Perhatikan potensi kompleksitas bentuk dan dampaknya pada ukuran dan pemrosesan data.

## Contoh Penggunaan

Berikut adalah contoh cara menggunakan pertanyaan geoshape dalam survei:

| type     | name           | label                                      | hint                                        |
|----------|----------------|--------------------------------------------|--------------------------------------------|
| geoshape | forest_area    | Gambarkan batas patch hutan                | Gunakan setidaknya 3 titik untuk membuat bentuk tertutup |

## Ekstensi rtSurvey

Meskipun spesifikasi XLSForm dasar untuk pertanyaan geoshape sederhana, rtSurvey mungkin menawarkan fitur atau kustomisasi tambahan:

1. Integrasi dengan peta offline untuk area terpencil
2. Opsi untuk mengatur jumlah minimum dan maksimum titik untuk bentuk
3. Kemampuan untuk mengedit atau menyempurnakan bentuk setelah penggambaran awal
4. Dukungan untuk berbagai tipe bentuk (misalnya, persegi panjang, lingkaran) selain poligon bebas

## Format Data

Data geoshape biasanya disimpan sebagai string pasangan koordinat yang dipisahkan spasi, diapit dalam tanda kurung:

```
(lat1 lon1; lat2 lon2; lat3 lon3; ... latN lonN)
```

Contoh:
```
(38.253094215699576 21.756382658677467; 38.25021274773806 21.756382658677467; 38.25007793942195 21.763892843919166; 38.25290886154963 21.763935759263404; 38.253094215699576 21.756382658677467)
```

## Pertimbangan untuk Analisis

Saat menggunakan pertanyaan geoshape, pertimbangkan:

1. Bagaimana data geografis akan divisualisasikan dan dianalisis (misalnya, perangkat lunak GIS)
2. Potensi kebutuhan pembersihan data atau penyederhanaan bentuk yang kompleks
3. Tindakan privasi dan perlindungan data untuk menangani data spasial yang terperinci
4. Integrasi dengan sumber data spasial lain untuk analisis yang komprehensif

## Keterbatasan

- Menggambar bentuk yang akurat di layar mobile yang kecil bisa menjadi tantangan.
- Bentuk yang kompleks mungkin memerlukan kapasitas penyimpanan dan pemrosesan yang signifikan.
- Pertanyaan geoshape mungkin tidak cocok untuk semua jenis survei atau responden.
- Mungkin ada kekhawatiran privasi terkait pengumpulan data spasial yang terperinci.
