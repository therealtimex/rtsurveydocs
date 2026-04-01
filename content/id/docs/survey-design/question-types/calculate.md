---
title: "Kalkulasi"
description: ""
icon: "calculate"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 235
---

Pertanyaan kalkulasi dalam XLSForm dan rtSurvey digunakan untuk melakukan komputasi berdasarkan bidang atau nilai lain dalam formulir Anda. Pertanyaan-pertanyaan ini tidak ditampilkan kepada pengguna tetapi berjalan di latar belakang, menyimpan hasilnya untuk digunakan nanti atau dikirimkan.

## Sintaks

Dalam XLSForm, pertanyaan kalkulasi didefinisikan sebagai berikut:

| type      | name     | label | calculation |
|-----------|----------|-------|-------------|
| calculate | calc_q1  |       | ${q1} + ${q2} |

- **type**: Selalu "calculate" untuk tipe pertanyaan ini.
- **name**: Nama unik untuk pertanyaan kalkulasi.
- **label**: Biasanya dikosongkan karena pertanyaan kalkulasi tidak ditampilkan kepada pengguna.
- **calculation**: Rumus yang akan dievaluasi.

## Penggunaan

Pertanyaan kalkulasi umum digunakan untuk:

1. Melakukan operasi aritmatika
2. Menggabungkan string
3. Menerapkan logika atau fungsi yang kompleks
4. Menyimpan hasil antara untuk digunakan nanti

## Contoh

### Aritmatika Dasar

```
| type      | name     | calculation |
|-----------|----------|-------------|
| calculate | total    | ${price} * ${quantity} |
```

### Penggabungan String

```
| type      | name     | calculation |
|-----------|----------|-------------|
| calculate | full_name| concat(${first_name}, ' ', ${last_name}) |
```

### Menggunakan Fungsi

```
| type      | name     | calculation |
|-----------|----------|-------------|
| calculate | age      | int((today() - ${date_of_birth}) / 365.25) |
```

## Penggunaan Lanjutan di rtSurvey

### Fungsi pulldata()

rtSurvey mendukung fungsi `pulldata()` dalam bidang kalkulasi, memungkinkan Anda mengambil data dari file CSV eksternal:

```
| type      | name     | calculation |
|-----------|----------|-------------|
| calculate | city     | pulldata('cities', 'city_name', 'zip_code', ${zip_input}) |
```

#### Sintaks

Sintaks dasar untuk pulldata() adalah:

```
pulldata('csv_filename', 'column_to_return', 'key_column', ${matching_value})
```

- 'csv_filename': Nama file CSV (tanpa ekstensi .csv)
- 'column_to_return': Nama kolom yang berisi data yang ingin Anda ambil
- 'key_column': Nama kolom untuk dicocokkan
- ${matching_value}: Nilai yang akan dicari dalam kolom kunci (seringkali variabel dari formulir)

#### Catatan Penting

1. File CSV harus diunggah bersama XLSForm Anda saat menerapkan survei.
2. Gunakan koma sebagai pemisah dalam file CSV Anda, bukan titik koma.
3. Hindari koma dalam bidang data CSV Anda, karena dapat menyebabkan masalah penguraian.
4. pulldata() hanya mendukung hubungan 1-ke-1. Jika beberapa kecocokan ditemukan, hanya mengembalikan yang pertama.
5. Mungkin ada batasan panjang teks yang dapat ditarik (sekitar 76 karakter).
6. Anda dapat menggunakan pulldata() dalam constraint untuk memvalidasi entri terhadap data CSV.

### Kalkulasi Kondisional

Anda dapat menggunakan pernyataan if() untuk kalkulasi kondisional:

```
| type      | name     | calculation |
|-----------|----------|-------------|
| calculate | discount | if(${total} > 1000, ${total} * 0.1, 0) |
```

## Praktik Terbaik

1. Gunakan nama yang bermakna untuk bidang kalkulasi untuk meningkatkan keterbacaan formulir.
2. Hindari kalkulasi yang terlalu kompleks dalam satu bidang; pecah jika perlu.
3. Uji kalkulasi Anda secara menyeluruh, terutama saat menggunakan rumus yang kompleks atau data eksternal.
4. Ingat bahwa bidang kalkulasi berjalan setiap kali formulir dievaluasi, yang dapat memengaruhi kinerja untuk kalkulasi yang sangat kompleks atau banyak.
5. Saat menggunakan pulldata(), pastikan file CSV Anda diformat dengan benar dan uji secara menyeluruh dengan data dan struktur formulir spesifik Anda.

## Keterbatasan

- Bidang kalkulasi tidak dapat langsung diedit oleh pengguna.
- Hasil bidang kalkulasi tidak langsung terlihat kecuali direferensikan dalam bidang tampilan atau digunakan dalam logika formulir.
