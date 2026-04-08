---
title: "Select_one"
description: "Pertanyaan select_one memungkinkan responden memilih tepat satu opsi dari daftar pilihan yang telah ditentukan."
icon: "radio_button_checked"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 224
---

Tipe pertanyaan `select_one` mendorong responden untuk memilih **tepat satu opsi** dari daftar yang telah ditentukan. Secara default pilihan dirender sebagai tombol radio, tetapi berbagai opsi appearance tersedia untuk mengubah tata letak dan perilaku.

## Spesifikasi XLSForm Dasar

**Lembar kerja survey:**

| type | name | label |
|------|------|-------|
| select_one yesno | consent | Apakah responden memberikan persetujuan? |

**Lembar kerja choices:**

| list_name | name | label |
|-----------|------|-------|
| yesno | yes | Ya |
| yesno | no | Tidak |

`listname` dalam `select_one listname` harus cocok dengan kolom `list_name` dalam lembar kerja choices.

Untuk detail lebih lanjut lihat [spesifikasi XLSForm](https://xlsform.org/en/#question-types).

## Penggunaan

Pertanyaan select_one digunakan untuk:

1. Pertanyaan Ya/Tidak
2. Pilihan ganda jawaban tunggal (misalnya, tingkat pendidikan, jenis kelamin, status pernikahan)
3. Penilaian kategoris (misalnya, buruk / cukup / baik / sangat baik)
4. Pilihan bertingkat (tertaut) di mana pilihan difilter berdasarkan jawaban sebelumnya
5. Pemilihan negara, wilayah, kabupaten, atau satuan administratif lainnya

## Opsi appearance

Tentukan nilai dalam kolom `appearance` untuk mengubah cara pilihan ditampilkan:

{{< table >}}
| Appearance | Deskripsi |
|------------|-----------|
| *(tidak ada)* | Tombol radio default, satu per baris |
| `minimal` | Dropdown/spinner tunggal alih-alih tombol radio |
| `quick` | Otomatis melanjutkan ke pertanyaan berikutnya segera setelah pemilihan (hanya mobile) |
| `compact` | Grid pilihan kompak — jumlah kolom menyesuaikan lebar layar |
| `compact-N` | Grid kompak dipaksakan ke N kolom (misalnya, `compact-3`) |
| `quickcompact` | Menggabungkan `quick` dan `compact` |
| `quickcompact-N` | Menggabungkan `quick` dan `compact` dengan N kolom yang dipaksakan |
| `horizontal` | Pilihan disusun dalam baris horizontal (web) |
| `horizontal-compact` | Horizontal, jarak kompak (web) |
| `likert` | Baris skala Likert — label di atas, tombol radio di bawah |
| `label` | Hanya menampilkan label pilihan tanpa input (gunakan berpasangan dengan `list-nolabel`) |
| `list-nolabel` | Hanya menampilkan input tanpa label (gunakan berpasangan dengan `label`) |
| `columns(N)` | Tampilkan dalam N kolom (ekstensi rtSurvey, misalnya, `columns(3)`) |
| `distress` | Widget ikon emosional Kessler Psychological Distress (K10) |
| `search-api(...)` | Pencarian dinamis — memuat pilihan dari API saat runtime |
| `tagging` | Menampilkan pilihan sebagai chip tag yang dapat diklik alih-alih tombol radio |
| `boxtag` | Menampilkan pilihan sebagai kotak persegi panjang bergaya yang diketuk pengguna untuk memilih |
| `boxtag -search` | Tata letak Boxtag dengan input pencarian/filter di atas kotak |
| `duolingo-style1` | Tata letak kartu ala Duolingo — kartu besar yang dapat diketuk dengan ikon |
| `rating_box` | Kotak penilaian berbasis grid — terbaik untuk pilihan numerik atau skala |
| `star_rating` | Widget penilaian bintang — pilihan dirender sebagai 1–N bintang |
| `choices-noshow` | Menampilkan 10 pilihan pertama awalnya; mengungkap sisanya sesuai permintaan |
| `noshow` | Menyembunyikan daftar pilihan sepenuhnya; nilai diatur secara terprogram |
| `checkall` | Menambahkan opsi "Pilih semua" di bagian atas daftar |
| `max-items(N)` | Membatasi jumlah pilihan yang terlihat menjadi N (misalnya, max-items(5)) |
{{< /table >}}

### Contoh: Skala Likert

| type | name | label | appearance |
|------|------|-------|------------|
| select_one satisfaction | service_rating | Seberapa puas Anda dengan layanan ini? | likert |

### Contoh: Kompak 3 kolom

| type | name | label | appearance |
|------|------|-------|------------|
| select_one regions | region | Pilih wilayah | compact-3 |

## Pilihan bertingkat

Pilihan bertingkat (tertaut) memfilter pilihan berdasarkan nilai yang dipilih dalam pertanyaan sebelumnya. Gunakan kolom `choice_filter` dengan nama kolom dari lembar kerja choices Anda.

**survey:**

| type | name | label | choice_filter |
|------|------|-------|---------------|
| select_one province | province | Pilih provinsi | |
| select_one district | district | Pilih kabupaten | province_name = ${province} |

**choices:**

| list_name | name | label | province_name |
|-----------|------|-------|---------------|
| province | nairobi | Nairobi | |
| province | mombasa | Mombasa | |
| district | westlands | Westlands | nairobi |
| district | kasarani | Kasarani | nairobi |
| district | nyali | Nyali | mombasa |
| district | likoni | Likoni | mombasa |

Ketika responden memilih `nairobi`, hanya `Westlands` dan `Kasarani` yang muncul dalam daftar kabupaten.

{{% alert icon=" " context="warning" %}}
Nama kolom yang digunakan dalam `choice_filter` (misalnya, `province_name`) harus ada dalam lembar kerja choices. `${province}` mereferensikan bidang survei bernama `province`.
{{% /alert %}}

## Menggunakan nilai yang dipilih dalam ekspresi

Referensikan **nilai** yang dipilih (bukan label) dengan `${fieldname}`:

```
relevant: ${consent} = 'yes'
```

Untuk mendapatkan label pilihan alih-alih nilai, gunakan `choice-label()`:

```
calculate: choice-label(${education_level}, ${education_level})
```

## Opsi "Lainnya" dengan teks bebas

Pola umum adalah menyertakan opsi "lainnya" yang menampilkan bidang teks:

| type | name | label | relevant |
|------|------|-------|----------|
| select_one occupation | job | Apa pekerjaan Anda? | |
| text | job_other | Harap tentukan | `${job} = 'other'` |

**choices:**

| list_name | name | label |
|-----------|------|-------|
| occupation | farmer | Petani |
| occupation | trader | Pedagang |
| occupation | student | Pelajar |
| occupation | other | Lainnya (harap tentukan) |

## Praktik Terbaik

1. Jaga daftar tetap pendek dan saling eksklusif — jika responden mungkin menginginkan lebih dari satu, gunakan `select_multiple` sebagai gantinya.
2. Tempatkan jawaban yang paling umum terlebih dahulu, atau urutkan secara alfabetis untuk daftar panjang.
3. Selalu sertakan opsi "Tidak tahu" atau "Lebih memilih untuk tidak menjawab" jika relevan.
4. Gunakan `minimal` (dropdown) untuk daftar dengan lebih dari 7–8 pilihan di mobile untuk menghemat ruang layar.
5. Untuk pilihan bertingkat, tambahkan semua kolom filter dalam lembar kerja choices sebelum membangun formulir.

## Keterbatasan

- Responden hanya dapat memilih satu pilihan — gunakan `select_multiple` untuk pertanyaan multi-jawaban.
- Appearance `likert` paling baik dengan 5–7 pilihan yang muat dalam satu baris.
- Auto-lanjut `quick` hanya untuk mobile; tidak berpengaruh pada formulir web.
