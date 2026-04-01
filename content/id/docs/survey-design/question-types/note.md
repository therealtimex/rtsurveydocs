---
title: "Catatan"
description: "Pertanyaan catatan menampilkan teks atau media hanya-baca untuk memberikan informasi atau instruksi dalam survei Anda."
icon: "info"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 255
---

Tipe pertanyaan catatan dalam XLSForm dan rtSurvey digunakan untuk menampilkan teks atau media hanya-baca kepada responden survei. Ini bukan pertanyaan yang memerlukan jawaban, melainkan cara untuk memberikan informasi, instruksi, atau konteks dalam survei.

## Spesifikasi XLSForm Dasar

| type | name | label |
|------|------|-------|
| note | info_text | Survei ini tentang kebiasaan membaca Anda. |

Untuk detail lebih lanjut tentang tipe pertanyaan catatan dasar, lihat [spesifikasi XLSForm](https://xlsform.org/en/#question-types).

## Penggunaan

Pertanyaan catatan umum digunakan untuk:

1. Memberikan instruksi atau konteks untuk pertanyaan berikutnya
2. Menampilkan hasil atau ringkasan yang dihitung
3. Menampilkan gambar atau media lainnya
4. Memisahkan bagian-bagian survei
5. Memberikan umpan balik berdasarkan respons sebelumnya

## Praktik Terbaik

1. Jaga teks catatan singkat dan jelas untuk mempertahankan keterlibatan responden.
2. Gunakan pemformatan (tebal, miring) untuk menekankan informasi penting.
3. Pertimbangkan menggunakan media (gambar, audio) untuk meningkatkan pemahaman jika sesuai.
4. Gunakan catatan secukupnya untuk menghindari penumpukan survei.

## Contoh Penggunaan

Berikut adalah contoh cara menggunakan pertanyaan catatan dalam survei:

| type | name | label |
|------|------|-------|
| note | intro | Selamat datang di survei kebiasaan membaca kami. Kami akan menanyakan preferensi dan frekuensi membaca Anda. |
| ... | ... | ... |
| calculate | books_per_month | ${fiction_books} + ${non_fiction_books} |
| note | reading_summary | Anda membaca sekitar ${books_per_month} buku per bulan. |

Dalam contoh ini, kami menggunakan catatan untuk memperkenalkan survei dan memberikan ringkasan hasil yang dihitung.

## Ekstensi rtSurvey

Meskipun spesifikasi XLSForm dasar untuk pertanyaan catatan sederhana, rtSurvey mungkin menawarkan fitur atau kustomisasi tambahan:

1. Format teks kaya
2. Dukungan untuk media yang disematkan (gambar, audio, video)
3. Konten dinamis berdasarkan respons sebelumnya
4. Opsi penataan kustom

## Penggunaan Lanjutan

### Tampilan Kondisional

Anda dapat menggunakan ekspresi relevansi untuk menampilkan catatan secara kondisional:

| type | name | label | relevant |
|------|------|-------|----------|
| note | high_reader_note | Anda pembaca yang rajin! | ${books_per_month} > 5 |

### Menyertakan Kalkulasi

Catatan dapat menyertakan kalkulasi untuk memberikan umpan balik dinamis:

| type | name | label |
|------|------|-------|
| note | reading_time | Berdasarkan respons Anda, Anda menghabiskan sekitar ${books_per_month * 5} jam membaca setiap bulan. |

## Keterbatasan

- Catatan tidak mengumpulkan data, sehingga tidak boleh digunakan ketika Anda perlu mengumpulkan informasi dari responden.
- Penggunaan catatan yang berlebihan dapat membuat survei terasa berantakan atau terlalu panjang.
- Beberapa opsi pemformatan atau media lanjutan mungkin tidak didukung di semua perangkat atau platform.
