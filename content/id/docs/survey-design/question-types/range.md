---
title: "Rentang"
description: "Pertanyaan rentang memungkinkan responden memilih angka dengan menyeret slider antara nilai minimum dan maksimum yang ditentukan."
icon: "sliders"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 238
---

Tipe pertanyaan `range` menampilkan **slider** (atau input yang setara) yang memungkinkan responden memilih angka dalam rentang minimum dan maksimum yang ditentukan. Ini ideal untuk mengumpulkan penilaian, skor kepuasan, atau nilai numerik apa pun di mana Anda ingin membatasi rentang secara visual daripada mengandalkan input teks dengan constraint.

## Spesifikasi XLSForm Dasar

| type | name | label | parameters |
|------|------|-------|------------|
| range | satisfaction | Seberapa puas Anda dengan layanan ini? | start=1 end=5 step=1 |

Kolom `parameters` mendefinisikan batas slider dan ukuran langkah:

| Parameter | Deskripsi | Default |
|-----------|-----------|---------|
| `start` | Nilai minimum (inklusif) | 0 |
| `end` | Nilai maksimum (inklusif) | 10 |
| `step` | Kenaikan antara nilai yang valid | 1 |

Untuk detail lebih lanjut tentang tipe pertanyaan rentang standar, lihat [spesifikasi XLSForm](https://xlsform.org/en/#question-types).

## Penggunaan

Pertanyaan rentang umum digunakan untuk:

1. Skala kepuasan atau penilaian (misalnya, 1–5 atau 0–10)
2. Skala numerik gaya Likert
3. Mengumpulkan pengukuran di mana hanya nilai diskrit yang valid
4. Rentang usia atau rentang skor di mana slider meningkatkan kegunaan dibandingkan bidang teks

## Contoh Penggunaan

### Skala penilaian dasar

| type | name | label | parameters |
|------|------|-------|------------|
| range | overall_rating | Penilaian keseluruhan (0–10) | start=0 end=10 step=1 |

### Langkah desimal

| type | name | label | parameters |
|------|------|-------|------------|
| range | weight_kg | Berat (kg) | start=0 end=200 step=0.5 |

### Menggunakan nilai dalam kalkulasi

| type | name | label | parameters | calculation |
|------|------|-------|------------|-------------|
| range | score | Skor tes (0–100) | start=0 end=100 step=5 | |
| calculate | grade | | | if(${score} >= 90, 'A', if(${score} >= 80, 'B', if(${score} >= 70, 'C', 'F'))) |
| note | grade_note | Nilai Anda adalah: ${grade} | | |

## Appearance

Tipe `range` dirender sebagai slider secara default. Tidak diperlukan nilai appearance tambahan untuk penggunaan dasar. Anda dapat menggabungkannya dengan `horizontal` untuk tata letak yang lebih lebar pada formulir web:

| type | name | label | parameters | appearance |
|------|------|-------|------------|------------|
| range | nps | Seberapa besar kemungkinan Anda merekomendasikan kami? (0–10) | start=0 end=10 step=1 | horizontal |

## Praktik Terbaik

1. Selalu tetapkan nilai `start`, `end`, dan `step` yang bermakna — jangan mengandalkan default.
2. Beri label ujung skala Anda dalam kolom `hint` (misalnya, `hint: 0 = Sangat tidak puas, 10 = Sangat puas`) untuk memberi konteks kepada responden.
3. Untuk skala Likert 5 poin, gunakan `start=1 end=5 step=1` daripada 0–4, karena responden mengharapkan "1" berarti yang terendah.
4. Gunakan `range` daripada `integer` + constraint ketika sifat terbatas dari input adalah bagian dari desain pertanyaan (slider mengkomunikasikan skala secara visual).

## Keterbatasan

- Widget slider mungkin tidak ideal untuk rentang yang sangat lebar (misalnya, 0–10000) — `integer` teks dengan constraint lebih ramah pengguna dalam kasus tersebut.
- Pada perangkat mobile, nilai langkah yang halus (misalnya, `step=0.1`) bisa sulit dikontrol secara tepat dengan slider sentuh.
