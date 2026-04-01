---
title: "Trigger / Acknowledge"
description: "Pertanyaan trigger menampilkan pernyataan yang harus secara eksplisit diakui enumerator sebelum melanjutkan."
icon: "check-circle"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 240
---

Tipe pertanyaan `trigger` (juga disebut `acknowledge`) menampilkan **pernyataan dengan kotak centang**. Enumerator harus mencentang kotak untuk mengkonfirmasi mereka telah membaca dan memahami pernyataan tersebut sebelum formulir mengizinkan mereka untuk melanjutkan. Tidak ada nilai data yang disimpan — hanya apakah kotak centang telah dicentang.

## Spesifikasi XLSForm Dasar

| type | name | label |
|------|------|-------|
| trigger | consent_ack | Responden telah memberikan persetujuan lisan yang diinformasikan. |

Atau menggunakan alias `acknowledge`:

| type | name | label |
|------|------|-------|
| acknowledge | consent_ack | Responden telah memberikan persetujuan lisan yang diinformasikan. |

Baik `trigger` maupun `acknowledge` setara — gunakan mana pun yang didokumentasikan platform Anda.

## Penggunaan

Pertanyaan trigger/acknowledge umum digunakan untuk:

1. **Persetujuan yang diinformasikan** — konfirmasi enumerator mendapatkan persetujuan sebelum merekam data sensitif
2. **Peringatan lunak** — peringatkan tentang nilai yang tidak biasa dan minta konfirmasi eksplisit sebelum melanjutkan
3. **Item daftar periksa** — konfirmasi pengamatan fisik telah selesai (misalnya, "Saya telah langsung mengamati sumber air")
4. **Instruksi** — paksa enumerator untuk mengakui instruksi tingkat bagian sebelum melanjutkan
5. **Pemeriksaan kualitas** — tandai nilai pencilan dan minta enumerator memverifikasinya

## Contoh Penggunaan

### Pengakuan persetujuan

| type | name | label | required |
|------|------|-------|----------|
| trigger | consent | Responden telah memberikan persetujuan lisan yang diinformasikan untuk berpartisipasi dalam survei ini. | yes |

### Peringatan lunak untuk nilai pencilan

Digunakan bersama dengan ekspresi `relevant` untuk hanya menampilkan trigger ketika nilai yang mencurigakan dimasukkan:

| type | name | label | relevant | required |
|------|------|-------|----------|----------|
| integer | children | Jumlah anak | | |
| trigger | children_confirm | Anda memasukkan ${children} anak. Harap verifikasi dengan responden dan ketuk OK untuk mengkonfirmasi. | `${children} > 10` | `${children} > 10` |

### Pengakuan instruksi di awal bagian

| type | name | label |
|------|------|-------|
| trigger | section_b_ack | Bagian B: Penggunaan Lahan Pertanian. Ajukan semua pertanyaan dalam bagian ini hanya kepada kepala rumah tangga. |

## Membuat trigger diperlukan

Tambahkan `required: yes` untuk mencegah melanjutkan sampai kotak dicentang:

| type | name | label | required | required_message |
|------|------|-------|----------|------------------|
| trigger | safety_check | Semua peralatan keselamatan ada dan berfungsi. | yes | Anda harus mengkonfirmasi sebelum melanjutkan. |

## Tampilan kondisional

Tampilkan trigger hanya ketika kondisi terpenuhi:

| type | name | label | relevant |
|------|------|-------|----------|
| select_one yesno | has_well | Apakah rumah tangga memiliki sumur? | |
| trigger | well_observation | Konfirmasi bahwa Anda telah langsung mengamati kondisi sumur. | `${has_well} = 'yes'` |

## Perbedaan dari `note`

| | `note` | `trigger` |
|--|--------|-----------|
| Menampilkan teks | Ya | Ya |
| Memerlukan interaksi | Tidak | Ya (harus mencentang) |
| Menyimpan data | Tidak | Tidak (hanya OK/tercentang) |
| Dapat memblokir kemajuan | Tidak | Ya (dengan `required`) |

## Praktik Terbaik

1. Jaga label trigger singkat dan dapat ditindaklanjuti — enumerator harus dapat membaca dan mengkonfirmasi dalam hitungan detik.
2. Selalu tambahkan `required: yes` ketika pengakuan bersifat wajib.
3. Gunakan trigger untuk persetujuan dan pemeriksaan keselamatan di mana Anda memerlukan jejak audit bahwa enumerator mengkonfirmasi.
4. Gabungkan dengan `relevant` untuk peringatan lunak kondisional sehingga trigger hanya muncul ketika nilai perlu diverifikasi.

## Keterbatasan

- Bidang trigger tidak menyimpan nilai data yang bermakna — mereka hanya mencatat bahwa kotak dicentang.
- Widget trigger dirender sebagai kotak centang/tombol sederhana pada sebagian besar klien; ini bukan tanda tangan elektronik penuh.
