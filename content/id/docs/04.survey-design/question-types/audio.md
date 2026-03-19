---
title: "Audio"
description: "Pertanyaan audio memungkinkan responden merekam dan mengirimkan file audio sebagai bagian dari survei."
icon: "mic"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 228
---

Tipe pertanyaan `audio` memungkinkan responden **merekam audio** atau mengunggah file audio yang sudah ada sebagai bagian dari respons survei mereka. Ini berguna untuk menangkap akun verbal, suara lingkungan, kesaksian, atau informasi apa pun yang lebih baik disampaikan melalui suara daripada teks.

## Spesifikasi XLSForm Dasar

| type  | name        | label                        |
|-------|-------------|------------------------------|
| audio | voice_note  | Harap rekam komentar Anda    |

Untuk detail lebih lanjut tentang tipe pertanyaan audio standar, lihat [spesifikasi XLSForm](https://xlsform.org/en/#question-types).

## Penggunaan

Pertanyaan audio umum digunakan untuk:

1. Menangkap respons verbal terbuka untuk mengurangi beban mengetik enumerator
2. Merekam kesaksian, cerita pribadi, atau sejarah lisan
3. Mendokumentasikan suara lingkungan (misalnya, tingkat kebisingan di dekat infrastruktur)
4. Mengumpulkan sampel suara untuk penelitian linguistik atau kesehatan
5. Memungkinkan responden menambahkan klarifikasi verbal ke jawaban numerik atau pilihan

## Format data

File audio disimpan sebagai lampiran biner bersama pengiriman formulir, biasanya:

- **Format:** MP3 atau AAC (perekaman mobile); WAV (perekaman berkualitas tinggi)
- **Penamaan:** `{instanceID}-{fieldname}.mp3` (atau yang setara)
- **Penyimpanan:** Diunggah ke folder media server dan ditautkan ke catatan pengiriman
- **Akses:** Dapat diputar dan diunduh dari antarmuka manajemen pengiriman

## Ekstensi rtSurvey

### Durasi maksimum

Gunakan kolom `parameters` untuk membatasi panjang perekaman:

| type | name | label | parameters |
|------|------|-------|------------|
| audio | interview | Rekam wawancara | `max-duration=120` |

`max-duration` dalam detik. Perekam berhenti secara otomatis pada batas.

### Pengaturan kualitas

Kualitas perekaman dapat diatur melalui `parameters`:

| type | name | label | parameters |
|------|------|-------|------------|
| audio | feedback | Rekam umpan balik | `quality=normal` |

Nilai yang didukung: `low`, `normal` (default), `voice-only`. `voice-only` mengoptimalkan untuk audio lisan dengan pengurangan kebisingan.

### Pemutaran sebelum pengiriman

Di mobile, enumerator dapat memutar ulang klip yang direkam sebelum melanjutkan. Ini diaktifkan secara default — tidak diperlukan konfigurasi.

### Integrasi perekam asli

Di Android dan iOS, `audio` meluncurkan aplikasi perekam asli perangkat. Di web, ia menggunakan API MediaRecorder bawaan browser.

## Contoh penggunaan

### Dengan durasi maksimum dan petunjuk

| type | name | label | hint | parameters |
|------|------|-------|------|------------|
| audio | story | Ceritakan tentang kejadian dengan kata-kata Anda sendiri | Bicaralah dengan jelas. Perekaman berhenti setelah 3 menit. | `max-duration=180` |

### Audio kondisional — hanya jika masalah dilaporkan

| type | name | label | relevant | required |
|------|------|-------|----------|----------|
| select_one yesno | issue_found | Apakah ditemukan masalah? | | |
| audio | issue_audio | Rekam deskripsi masalah | `${issue_found} = 'yes'` | `${issue_found} = 'yes'` |

## Praktik Terbaik

1. Nyatakan dengan jelas dalam `label` atau `hint` apa yang harus dikatakan enumerator dan berapa lama.
2. Gunakan `max-duration` untuk mencegah file yang terlalu besar di area dengan kecepatan unggah yang lambat.
3. Informasikan responden sebelum memulai perekaman — perekaman yang tidak terduga dapat menimbulkan kekhawatiran privasi.
4. Uji perekaman pada perangkat target dan kondisi jaringan sebelum penerapan.
5. Tetapkan `quality=voice-only` untuk perekaman gaya wawancara untuk mengurangi ukuran file tanpa kehilangan kejelasan.

## Keterbatasan

- File audio bisa besar (perekaman 2 menit dengan kualitas normal sekitar 2–4 MB) — pertimbangkan ini dalam estimasi paket data dan waktu unggah.
- Tidak semua browser mendukung API MediaRecorder — Chrome dan Firefox bekerja dengan andal; Safari pada versi iOS yang lebih lama mungkin memiliki masalah.
- Transkripsi respons audio memerlukan pemrosesan pasca tambahan (ucapan-ke-teks manual atau otomatis).
- Peraturan privasi mungkin membatasi perekaman suara — verifikasi persyaratan perlindungan data lokal.
