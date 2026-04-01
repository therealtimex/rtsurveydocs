---
title: "Gambar lanjutan"
description: "Fitur gambar lanjutan di rtSurvey: watermark, tampilan grid media, dan anotasi gambar."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 300
---

Di luar tipe pertanyaan `image` standar, rtSurvey menyediakan ekstensi untuk **memberi watermark** pada foto yang diambil dan menampilkan beberapa gambar dalam **grid media**. Ini berguna untuk survei berbasis bukti di mana foto perlu ditandai dengan identitas enumerator atau metadata survei, dan untuk antarmuka tinjauan visual.

---

## Watermark

Fitur watermark melapisi teks atau gambar pada foto yang diambil sebelum disimpan. Ini digunakan untuk menandai foto lapangan dengan tanggal, nama enumerator, lokasi GPS, atau data survei lainnya — membuat foto yang sudah ada sebelumnya lebih sulit dijadikan bukti pengambilan baru.

### Pengaturan

Gunakan `watermark()` dalam kolom **`calculation`** dari bidang `image`, dikombinasikan dengan appearance `callapi`:

```
watermark(type, size, distance, color, shadow, rotate, blur)
```

| Parameter | Deskripsi |
|-----------|-----------|
| `type` | `'text'` untuk watermark teks; `'file'` untuk watermark gambar |
| `size` | Ukuran font dalam piksel (teks) atau ukuran watermark sebagai % dari lebar gambar (file) |
| `distance` | Jarak antara ubin watermark yang berulang (piksel) |
| `color` | Warna teks (warna CSS atau hex). Tidak digunakan untuk tipe `file` |
| `shadow` | Warna bayangan (warna CSS atau hex) |
| `rotate` | Sudut rotasi dalam derajat (misalnya, `45` untuk diagonal) |
| `blur` | Opasitas watermark (0 = tidak terlihat, 100 = sepenuhnya buram) |

### Contoh watermark teks

Lapisi nama enumerator dan tanggal hari ini secara diagonal di setiap foto yang diambil:

| type | name | label | appearance | calculation |
|------|------|-------|------------|-------------|
| calculate | wm_text | | | `concat(pulldata('app-api', 'user.name'), ' | ', format-date(today(), '%d/%m/%Y'))` |
| image | site_photo | Ambil foto lokasi | watermark | `watermark('text', 20, 60, '#ffffff', '#000000', 45, 40)` |

Teks watermark diambil dari `${wm_text}`. Tetapkan bidang teks watermark **sebelum** bidang gambar dalam formulir.

### Contoh watermark gambar/logo

Lapisi logo organisasi (dilampirkan sebagai file media bernama `logo.png`):

| type | name | label | appearance | calculation |
|------|------|-------|------------|-------------|
| image | evidence_photo | Ambil foto bukti | watermark | `watermark('file', 25, 80, '', '#000000', 0, 50)` |

### Undo/redo

Editor watermark mendukung undo dan redo — enumerator dapat mundur melalui riwayat pengeditan sebelum mengonfirmasi foto.

### Tiling watermark

Watermark berulang (tile) di seluruh gambar secara otomatis. Parameter `distance` mengontrol jarak antara ubin; `rotate` mengontrol sudut setiap ubin.

---

## Widget grid media

Widget grid media menampilkan kumpulan file media (gambar, audio, video) dalam tata letak grid, memungkinkan peninjau atau enumerator menelusuri file yang diambil secara visual.

Widget ini diaktifkan oleh appearance `mediagridwidget` dan biasanya digunakan pada bidang `note` atau `calculate` untuk menampilkan media yang sebelumnya diambil dari grup pengulangan.

### Contoh: Tampilkan semua foto dari pengulangan sebagai grid

| type | name | label | appearance | calculation |
|------|------|-------|------------|-------------|
| calculate | photo_list | | | `join(' ', ${site_photo})` |
| note | photo_review | Tinjau foto yang diambil | mediagridwidget | |

---

## Praktik Terbaik untuk foto dengan watermark

1. Selalu hitung teks watermark dalam bidang `calculate` **di atas** bidang gambar sehingga tersedia saat foto diambil.
2. Gunakan sudut rotasi (misalnya, 45°) untuk membuat watermark lebih sulit dipotong.
3. Tetapkan opasitas (`blur`) antara 30–60% — cukup tinggi untuk terbaca, cukup rendah agar tidak mengaburkan subjek foto.
4. Sertakan nama enumerator, tanggal, dan koordinat GPS dalam teks watermark untuk memaksimalkan nilai audit.
5. Uji rendering watermark pada perangkat dengan spesifikasi terendah dalam armada Anda — watermark berbasis canvas dapat lambat pada perangkat lama.

## Keterbatasan

- Watermark diterapkan sisi klien menggunakan HTML5 Canvas API — memerlukan browser atau WebView yang mampu.
- Foto resolusi sangat tinggi mungkin memerlukan beberapa detik untuk diberi watermark pada perangkat kelas bawah.
- Watermark tertanam dalam file gambar — tidak dapat dihapus setelah pengiriman tanpa pengeditan gambar.
- Tipe watermark `file` memerlukan gambar logo dilampirkan sebagai file media dengan nama file yang persis sesuai.
