---
title: "Tampilan (Appearance)"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 288
---

Kolom `appearance` di rtSurvey memungkinkan Anda menyesuaikan presentasi visual dan perilaku pertanyaan dalam survei Anda. Fitur ini meningkatkan pengalaman pengguna dan dapat secara signifikan meningkatkan efisiensi pengumpulan data. rtSurvey mendukung atribut appearance XLSForm standar dan memperluasnya dengan opsi tambahan.

## Atribut Appearance XLSForm Standar

rtSurvey mendukung atribut appearance XLSForm standar berikut:

| Atribut Appearance | Jenis Pertanyaan | Deskripsi |
|-------------------|-----------------|-----------|
| multiline | text | Membuat kotak teks multi-baris (terbaik untuk klien web) |
| minimal | select_one, select_multiple | Menampilkan pilihan dalam menu dropdown |
| quick | select_one | Maju otomatis ke pertanyaan berikutnya setelah pemilihan (hanya mobile) |
| no-calendar | date | Menyembunyikan tampilan kalender (hanya mobile) |
| month-year | date | Memungkinkan pemilihan bulan dan tahun saja |
| year | date | Memungkinkan pemilihan tahun saja |
| horizontal-compact | select_one, select_multiple | Menampilkan pilihan secara horizontal (hanya web) |
| horizontal | select_one, select_multiple | Menampilkan pilihan secara horizontal dalam kolom (hanya web) |
| likert | select_one | Menyajikan pilihan sebagai skala Likert |
| compact | select_one, select_multiple | Menampilkan pilihan berdampingan dengan padding minimal |
| quickcompact | select_one | Menggabungkan tampilan kompak dengan maju otomatis (hanya mobile) |
| field-list | groups | Menampilkan seluruh grup di satu layar (hanya mobile) |
| label | select_one, select_multiple | Menampilkan label pilihan tanpa masukan |
| list-nolabel | select_one, select_multiple | Menampilkan masukan tanpa label (gunakan dengan `label`) |
| table-list | groups | Menampilkan pertanyaan dalam format tabel |
| signature | image | Mengaktifkan penangkapan tanda tangan (hanya mobile) |
| draw | image | Memungkinkan gambar tangan bebas (hanya mobile) |
| map, quick map | select_one, select_one_from_file | Mengaktifkan pemilihan dari fitur peta |

## Praktik Terbaik untuk Menggunakan Appearance

1. **Konsistensi**: Gunakan atribut appearance secara konsisten di seluruh survei Anda untuk tampilan yang seragam.
2. **Mobile vs. Web**: Pertimbangkan bagaimana appearance akan dirender di berbagai perangkat dan platform.
3. **Kinerja**: Berhati-hatilah dengan atribut appearance yang mungkin memperlambat pemuatan formulir (misalnya, `table-list` untuk grup besar).
4. **Pengalaman Pengguna**: Pilih appearance yang membuat entri data lebih mudah dan lebih intuitif bagi responden.
5. **Pengujian**: Selalu uji formulir Anda di perangkat target untuk memastikan appearance berfungsi seperti yang diharapkan.

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

## Atribut Appearance yang Diperluas rtSurvey

Selain appearance XLSForm standar, rtSurvey mendukung opsi khusus platform berikut:

### Kontrol data dan tampilan

| Atribut Appearance | Jenis Pertanyaan | Deskripsi |
|-------------------|-----------------|-----------|
| `invisible` | apa saja | Menyembunyikan bidang dari tampilan sambil tetap mengumpulkan atau menghitung nilainya. Berbeda dari tipe `hidden` — bidang masih berpartisipasi dalam logika. |
| `displaytitle` | apa saja | Memaksa tampilan label/judul bidang bahkan ketika seharusnya disembunyikan. |
| `autopull` | select_one, select_multiple | Secara otomatis mengambil data eksternal untuk mengisi pilihan saat formulir dimuat atau bidang pemicu berubah. |
| `floating_hint` | text, integer, decimal | Menampilkan teks petunjuk sebagai label mengambang di atas bidang masukan daripada di bawahnya. |
| `calculate-button` | calculate | Menambahkan tombol yang terlihat yang memicu kalkulasi ulang bidang sesuai permintaan, daripada menghitung secara otomatis. |

### Tata letak

| Atribut Appearance | Jenis Pertanyaan | Deskripsi |
|-------------------|-----------------|-----------|
| `1screen` | group | Memaksa seluruh grup untuk ditampilkan di satu layar terlepas dari ukuran grup. |
| `columns(n)` | select_one, select_multiple | Menampilkan pilihan dalam `n` kolom. Contoh: `columns(3)` menampilkan tiga kolom tombol radio. |
| `gridformat<row=R col=C colspan=S align=center>` | apa saja | Memposisikan bidang dalam tata letak CSS-grid pada baris `R`, kolom `C`, merentangkan `S` kolom. Digunakan dengan `advanced-extension/grid-layout`. |
| `ignore-simplify` | apa saja | Menginstruksikan renderer formulir untuk melewati penyederhanaan atau pemadatan otomatis tata letak bidang ini. |

### Widget

| Atribut Appearance | Jenis Pertanyaan | Deskripsi |
|-------------------|-----------------|-----------|
| `likert` | select_one | Menyajikan pilihan sebagai baris skala Likert (sudah ada di tabel standar di atas; dikonfirmasi didukung). |
| `distress` | select_one | Merender pilihan sebagai widget visual Kessler Psychological Distress Scale (K10) dengan ikon emosional. |

### Integrasi API

| Atribut Appearance | Jenis Pertanyaan | Deskripsi |
|-------------------|-----------------|-----------|
| `callapi` | text, integer, decimal, select_one | Mengaktifkan integrasi panggilan API untuk bidang ini. Kolom kalkulasi harus berisi ekspresi `callapi()`. Lihat [Call API](advanced-extension/call-api). |
| `callapi-verify(params)` | text, integer, decimal | Memicu panggilan verifikasi API menggunakan parameter statis. Formulir memblokir kemajuan hingga API mengonfirmasi nilai. |
| `callapi-verify(dynamicParams)` | text, integer, decimal | Sama seperti `callapi-verify` tetapi dengan parameter yang berasal dari nilai bidang lain saat runtime. |

### Format tanggal/waktu sebaris

Untuk bidang `date`, `time`, dan `datetime`, Anda dapat menentukan format tampilan kustom menggunakan string format yang ditambahkan ke appearance:

```
inline-[%d/%m/%Y]
inline-1line-[%d/%m/%Y %H:%M]
```

Token format sama seperti `format-date()` dan `format-date-time()`. Lihat [Fungsi — Fungsi tanggal dan waktu](operators-and-functions/functions#date-and-time-functions).

Contoh:

| type | name | label | appearance |
|------|------|-------|------------|
| datetime | event_time | Tanggal dan waktu acara | inline-[%d/%m/%Y %I:%M %p] |
| date | birth_date | Tanggal lahir | inline-[%d/%m/%Y] |

## Keterbatasan yang Diketahui

- Appearance yang kompleks mungkin tidak dirender identik di semua platform.
- Beberapa appearance rtSurvey lanjutan mungkin tidak didukung dalam mode offline.

## Pemecahan Masalah Appearance

1. **Appearance Tidak Diterapkan**: Periksa kesalahan ketik di kolom appearance.
2. **Rendering Tidak Konsisten**: Verifikasi kompatibilitas dengan jenis pertanyaan dan platform.
3. **Masalah Kinerja**: Pertimbangkan untuk menyederhanakan appearance yang kompleks, terutama untuk survei besar.
