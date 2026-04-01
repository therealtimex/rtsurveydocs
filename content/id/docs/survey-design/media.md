---
title: "Media"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 286
---

rtSurvey mendukung integrasi media yang kaya dalam survei, memungkinkan Anda memperkaya kuesioner dengan gambar, audio, dan video. Fitur ini dapat secara signifikan meningkatkan pengalaman responden dan kualitas data yang dikumpulkan.

## Jenis Media yang Didukung

rtSurvey mendukung jenis media berikut:
- Gambar (jpg, png, gif)
- Audio (mp3, wav)
- Video (mp4, webm)

## Menambahkan Media ke Survei Anda

Untuk menyertakan media dalam formulir rtSurvey Anda, gunakan kolom-kolom berikut dalam XLSForm Anda:

- `image`: Untuk menampilkan gambar
- `audio`: Untuk memutar file audio
- `video`: Untuk memutar file video

Contoh:

```
| type | name          | label         | image        | audio       | video       |
|------|---------------|---------------|--------------|-------------|-------------|
| note | media_example | Contoh media  | example.jpg  | sound.mp3   | clip.mp4    |
```

## Manajemen File Media

### Survei berbasis web
Untuk survei berbasis web, rtSurvey menyediakan antarmuka manajemen media tempat Anda dapat mengunggah dan mengatur file media Anda. File-file ini kemudian tersedia secara otomatis untuk digunakan dalam survei Anda.

### Aplikasi mobile
Saat menggunakan aplikasi mobile rtSurvey:
1. Tempatkan file media Anda di folder `/rtSurvey/forms/[form-name]-media/` di perangkat Anda.
2. Referensikan nama file yang tepat dalam XLSForm Anda.

## Fitur Khusus rtSurvey

### Pemuatan Media Dinamis
rtSurvey mendukung pemuatan media dinamis berdasarkan respons survei:

```
| type         | name      | label              | image                    |
|--------------|-----------|--------------------|--------------------------| 
| select_one species | animal | Pilih hewan | ${animal}.jpg            |
```

### Media dalam Opsi Pilihan
rtSurvey memungkinkan Anda menggunakan media dalam opsi pilihan untuk pertanyaan select:

```
| type                | name    | label           | media::image |
|---------------------|---------|-----------------|--------------|
| select_one_from_file animals | Pilih hewan |              |
```

Dalam lembar choices:
```
| list_name | name  | label | media::image |
|-----------|-------|-------|--------------|
| animals   | dog   | Anjing| dog.jpg      |
| animals   | cat   | Kucing| cat.jpg      |
```

### Pengambilan Media
rtSurvey memperluas XLSForm dengan kemampuan pengambilan media:

```
| type  | name        | label               |
|-------|-------------|---------------------|
| image | photo       | Ambil foto          |
| audio | voice_note  | Rekam catatan suara |
| video | video_clip  | Rekam video         |
```

## Praktik Terbaik untuk Menggunakan Media

1. **Optimalkan ukuran file**: File media yang besar dapat memperlambat pemuatan dan pengiriman survei.
2. **Gunakan format yang sesuai**: Tetap gunakan format yang didukung secara luas (jpg untuk gambar, mp3 untuk audio, mp4 untuk video).
3. **Sediakan alternatif**: Selalu sertakan alternatif teks untuk aksesibilitas.
4. **Uji secara menyeluruh**: Pastikan media ditampilkan dengan benar di semua perangkat target.
5. **Pertimbangkan penggunaan offline**: Untuk survei yang mungkin dilakukan secara offline, pastikan semua media tersedia secara lokal.

## Dukungan Media Multibahasa

rtSurvey mendukung media spesifik bahasa. Gunakan akhiran `::language`:

```
| type | name  | label    | image::English | image::Spanish |
|------|-------|----------|----------------|----------------|
| note | intro | Selamat datang | welcome_en.jpg | welcome_es.jpg |
```

## Media dalam Ekspor Data

Saat mengekspor data dari rtSurvey:
- Untuk survei web, URL media disertakan dalam ekspor.
- Untuk survei aplikasi mobile, path file disertakan.

## Pertimbangan Aplikasi Mobile

- Pastikan ruang penyimpanan yang cukup di perangkat untuk survei yang banyak menggunakan media.
- Aplikasi mobile rtSurvey mendukung pemutaran dan pengambilan media offline.
- File media yang besar dapat memengaruhi kinerja aplikasi di perangkat kelas bawah.

## Keterbatasan yang Diketahui

- Beberapa browser lama mungkin tidak mendukung semua format media.
- File video yang sangat besar dapat menyebabkan masalah dalam situasi bandwidth rendah.

## Pemecahan Masalah Media

1. **Media tidak ditampilkan**: Periksa path dan nama file untuk keakuratan.
2. **Masalah pemutaran**: Pastikan format media didukung oleh perangkat target.
3. **Pemuatan lambat**: Pertimbangkan untuk mengoptimalkan ukuran file atau memuat media sebelumnya.

## Fitur Media Lanjutan

### Geotag
rtSurvey dapat secara otomatis men-geotag media yang diambil selama survei:

```
| type  | name        | label        | appearance |
|-------|-------------|--------------|------------|
| image | photo       | Ambil foto   | geotag     |
```

### Anotasi Media
Izinkan responden untuk memberi anotasi pada gambar:

```
| type  | name        | label        | appearance |
|-------|-------------|--------------|------------|
| image | photo       | Beri anotasi pada gambar | annotate |
```

Dengan menggunakan media secara efektif dalam formulir rtSurvey Anda, Anda dapat membuat survei yang lebih menarik, informatif, dan akurat. Ingat untuk menyeimbangkan manfaat penyertaan media dengan pertimbangan kinerja, terutama untuk survei yang diterapkan di area dengan konektivitas internet terbatas atau di perangkat kelas bawah.
