---
title: "Mengelompokkan pertanyaan"
description: ""
icon: "auto_awesome"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 250
---

Grup dalam XLSForm memungkinkan Anda mengatur pertanyaan terkait bersama-sama, meningkatkan struktur survei Anda dan meningkatkan kemampuan analisis data. rtSurvey sepenuhnya mendukung grup XLSForm dan memperluas fungsionalitasnya dengan fitur tambahan.

## Struktur Grup Dasar

Untuk membuat grup pertanyaan, gunakan sintaks `begin_group` dan `end_group`:

```
| type         | name       | label                                    |
|--------------|------------|------------------------------------------|
| begin_group  | respondent | Informasi Responden                      |
| text         | name       | Masukkan nama responden                  |
| text         | position   | Masukkan posisi responden                |
| end_group    |            |                                          |
```

Poin-poin utama:
- Baris `begin_group` memerlukan `name` dan `label`.
- Baris `end_group` tidak memerlukan nama atau label.
- Pertanyaan antara `begin_group` dan `end_group` adalah bagian dari grup.

## Appearance Grup

rtSurvey mendukung berbagai opsi appearance untuk grup:

1. **field-list**: Menampilkan beberapa pertanyaan di layar yang sama.
   ```
   | type         | name       | label     | appearance |
   |--------------|------------|-----------|------------|
   | begin_group  | respondent | Responden | field-list |
   | text         | name       | Nama      |            |
   | text         | position   | Posisi    |            |
   | end_group    |            |           |            |
   ```

2. **grid**: Membuat tata letak kompak seperti tabel untuk grup (spesifik rtSurvey).
   ```
   | type         | name       | label     | appearance |
   |--------------|------------|-----------|------------|
   | begin_group  | household  | Rumah tangga | grid    |
   | text         | member_name| Nama      |            |
   | integer      | member_age | Usia      |            |
   | end_group    |            |           |            |
   ```

3. **collapsible**: Membuat grup yang dapat diperluas/diciutkan (spesifik rtSurvey).
   ```
   | type         | name       | label     | appearance  |
   |--------------|------------|-----------|-------------|
   | begin_group  | details    | Detail    | collapsible |
   | text         | address    | Alamat    |             |
   | text         | phone      | Telepon   |             |
   | end_group    |            |           |             |
   ```

## Grup Bersarang

Grup dapat bersarang di dalam grup lain untuk struktur yang lebih kompleks:

```
| type         | name       | label                                    |
|--------------|------------|------------------------------------------|
| begin_group  | hospital   | Informasi Rumah Sakit                    |
| text         | hosp_name  | Apa nama rumah sakit ini?                |
| begin_group  | medication | Ketersediaan Obat                        |
| select_one y_n| hiv_meds  | Apakah rumah sakit ini memiliki obat HIV? |
| end_group    |            |                                          |
| end_group    |            |                                          |
```

**Catatan**: Selalu akhiri grup yang paling baru dimulai terlebih dahulu untuk menjaga pengaluran yang tepat.

## Logika Lewati untuk Grup

Gunakan kolom `relevant` untuk mengimplementasikan logika lewati untuk seluruh grup:

```
| type         | name   | label                                        | relevant        |
|--------------|--------|----------------------------------------------|-----------------|
| integer      | age    | Berapa usia Anda?                            |                 |
| begin_group  | child  | Anak                                         | ${age} <= 5     |
| integer      | muac   | Catat lingkar lengan atas tengah anak        |                 |
| select_one y_n| mrdt  | Apakah tes diagnostik cepat anak positif?   |                 |
| end_group    |        |                                              |                 |
```

Dalam contoh ini, grup `child` hanya akan muncul jika usia responden 5 tahun atau lebih muda.

## Praktik Terbaik untuk Menggunakan Grup

1. Gunakan nama yang bermakna untuk grup guna meningkatkan analisis data.
2. Jaga agar grup tetap fokus pada pertanyaan terkait.
3. Gunakan grup bersarang dengan bijaksana untuk menghindari struktur yang terlalu kompleks.
4. Uji logika lewati secara menyeluruh saat menggunakan `relevant` pada grup.
5. Pertimbangkan menggunakan appearance `field-list` untuk grup pendek guna mengurangi pengguliran.
6. Manfaatkan tata letak grid rtSurvey untuk tampilan kompak informasi terkait.
7. Gunakan grup yang dapat diciutkan untuk formulir panjang guna meningkatkan navigasi.

## Fitur Khusus rtSurvey

1. **Tata Letak Grid**: Gunakan appearance `grid` untuk tampilan seperti tabel.
2. **Grup yang Dapat Diciutkan**: Implementasikan appearance `collapsible` untuk bagian yang dapat diperluas.
3. **Gaya Kustom**: Terapkan CSS kustom ke grup untuk desain visual yang unik.
4. **Perilaku Grup Dinamis**: Implementasikan logika lewati dan kalkulasi yang kompleks dalam grup.

## Dukungan Multibahasa

rtSurvey mendukung grup multibahasa. Gunakan kolom spesifik bahasa untuk label:

```
| type         | name       | label::English | label::French |
|--------------|------------|----------------|---------------|
| begin_group  | personal   | Info Pribadi   | Infos Personnelles |
| text         | name       | Nama           | Nom           |
| end_group    |            |                |               |
```

## Pertimbangan Aplikasi Mobile

- Grup dengan appearance `field-list` ditampilkan sebagai satu layar di aplikasi mobile.
- Grup yang dapat diciutkan dapat meningkatkan navigasi di layar yang lebih kecil.
- Tata letak grid mungkin menyesuaikan untuk visibilitas yang lebih baik di perangkat mobile.

## Keterbatasan yang Diketahui

- Pengaluran grup yang sangat dalam dapat memengaruhi kinerja di beberapa perangkat.
- Beberapa opsi gaya lanjutan mungkin tidak tersedia untuk grup di aplikasi mobile.

## Pemecahan Masalah Grup

1. Pastikan setiap `begin_group` memiliki `end_group` yang sesuai.
2. Periksa bahwa nama grup unik dalam formulir.
3. Verifikasi bahwa logika lewati mereferensikan nama pertanyaan yang benar.
4. Uji grup secara menyeluruh di antarmuka web dan mobile.

Dengan menggunakan grup secara efektif dalam XLSForm Anda dengan rtSurvey, Anda dapat membuat survei yang terorganisir dan efisien yang meningkatkan pengalaman pengumpulan data dan kualitas analisis data Anda.
