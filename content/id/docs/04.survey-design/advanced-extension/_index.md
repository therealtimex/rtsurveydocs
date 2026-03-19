---
title: "Ekstensi lanjutan"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 289
---

Kolom `appearance` di rtSurvey memungkinkan Anda menyesuaikan presentasi visual dan perilaku pertanyaan dalam survei Anda. Fitur ini meningkatkan pengalaman pengguna dan dapat secara signifikan meningkatkan efisiensi pengumpulan data. rtSurvey mendukung atribut appearance XLSForm standar dan memperluasnya dengan opsi tambahan.

## Ekstensi Appearance Khusus rtSurvey

rtSurvey memperluas opsi appearance standar dengan yang berikut:

### Kustomisasi Input Waktu

Untuk pertanyaan tipe `text` yang digunakan untuk input waktu:

- `appearance:` - Menampilkan jam untuk memilih jam dan menit
- `appearance: inline` - Menampilkan jam sebagai ikon
- `appearance: inline-1line` - Menampilkan jam dalam format satu baris
- `appearance: inline-onlyresult` - Menampilkan ikon jam, menghilang setelah pilihan
- `appearance: inline-[FORMAT]` - Menyesuaikan tampilan format waktu (misalnya, `[%H:%M]`, `[%h:%M:%S]`)

### Kustomisasi Warna

rtSurvey memungkinkan kustomisasi warna untuk berbagai appearance:

- `appearance: inline colors("0099FF")` - Menyesuaikan warna ikon
- `appearance: inline-1line colors("0000FF","FFFF00")` - Menyesuaikan warna dalam format satu baris

### Tata Letak Grid

rtSurvey memperkenalkan tata letak grid untuk tampilan kompak seperti tabel:

- `appearance: grid` - Diterapkan pada grup untuk membuat tata letak grid

### Grup yang Dapat Dilipat

- `appearance: collapsible` - Membuat grup yang dapat diperluas/dilipat

## Praktik Terbaik untuk Menggunakan Appearance

1. **Konsistensi**: Gunakan atribut appearance secara konsisten di seluruh survei Anda untuk tampilan yang seragam.
2. **Mobile vs. Web**: Pertimbangkan bagaimana appearance akan dirender pada perangkat dan platform yang berbeda.
3. **Kinerja**: Berhati-hatilah dengan atribut appearance yang mungkin memperlambat pemuatan formulir (misalnya, `table-list` untuk grup besar).
4. **Pengalaman Pengguna**: Pilih appearance yang membuat entri data lebih mudah dan lebih intuitif bagi responden.
5. **Pengujian**: Selalu uji formulir Anda di perangkat target untuk memastikan appearance bekerja seperti yang diharapkan.

## Teknik Lanjutan

### Menggabungkan Appearance

Beberapa atribut appearance dapat digabungkan untuk tata letak yang lebih kompleks:

```
| type | name | label | appearance |
|------|------|-------|------------|
| select_one options | choice | Pilih satu: | minimal compact |
```

### Appearance Dinamis

rtSurvey memungkinkan perubahan appearance dinamis berdasarkan logika formulir:

```
| type | name | label | appearance | relevant |
|------|------|-------|------------|----------|
| text | time | Masukkan waktu: | inline-[%H:%M] | ${show_time} = 'yes' |
```

## Pertimbangan Aplikasi Mobile

- Beberapa appearance (misalnya, `quick`, `signature`) khusus untuk perangkat mobile.
- Uji secara menyeluruh di Android dan iOS untuk memastikan perilaku yang konsisten.

## Keterbatasan yang Diketahui

- Appearance yang kompleks mungkin tidak dirender secara identik di semua platform.
- Beberapa appearance rtSurvey lanjutan mungkin tidak didukung dalam mode offline.

## Pemecahan Masalah Appearance

1. **Appearance Tidak Diterapkan**: Periksa kesalahan pengetikan dalam kolom appearance.
2. **Rendering Tidak Konsisten**: Verifikasi kompatibilitas dengan tipe pertanyaan dan platform.
3. **Masalah Kinerja**: Pertimbangkan menyederhanakan appearance yang kompleks, terutama untuk survei besar.
