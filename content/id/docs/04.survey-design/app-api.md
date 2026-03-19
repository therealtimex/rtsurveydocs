---
title: "App API"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 300
---

AppAPI memungkinkan pengguna memuat metadata sistem dari aplikasi menggunakan berbagai metode di FormEngine dan DMView. Ini menyediakan akses ke berbagai kunci data untuk mengambil informasi spesifik dari aplikasi.

Dalam xlsform, Anda dapat menggunakan fungsi `pulldata()` dengan sintaks berikut:


{{< alert context="light" text="pulldata('app-api', 'data-key')" />}}

- `'app-api'`: Kata kunci ini memberi tahu FormEngine untuk memuat data dari App API.
- `'data-key'`: Ini adalah kunci data yang ingin Anda muat dari App API.
- Jika kunci data tidak valid atau tidak didukung, kalkulasi akan mengembalikan "n/a".

Berikut adalah kunci data yang didukung yang dapat Anda gunakan dengan App-API:

`osPlatform`: Mengembalikan nama OS saat ini (Android atau iOS) dan versi OS. Platform web akan mengembalikan nilai kosong.

`appPlatform`: Mengembalikan nama platform aplikasi, yaitu `rtSurvey`.

`appVersion`: Mengembalikan nama versi aplikasi.

`getDisplayWidth`: Mengembalikan lebar layar perangkat dalam piksel.

`getDisplayHeight`: Mengembalikan tinggi layar perangkat dalam piksel.

`getScreenSize`: Mengembalikan ukuran layar perangkat dalam inci.

`projectCode`: Mengembalikan kode proyek saat ini dari situs yang dimasuki pengguna.

`projectURL`: Mengembalikan URL proyek saat ini dari situs yang dimasuki pengguna. Nilai default/cadangan adalah teks kosong ("").

`startingPoint`: Mengembalikan path titik yang memulai formulir. Lihat "Titik awal formulir" untuk detail lebih lanjut.

`serverTime`: Mengembalikan perkiraan terbaik yang tersedia dari tanggal dan waktu di server.

`user.[attribute]`: Mengembalikan atribut pengguna saat ini berdasarkan kunci atribut yang ditentukan. Lihat tabel "Atribut pengguna" untuk kunci atribut yang tersedia.

Gabungkan kunci atribut di bawah ini dengan "user." dalam parameter `pulldata()` untuk mengambil informasi pengguna saat ini. Misalnya, gunakan `user.username`, `user.email`, dll.

| Kunci Atribut        | Deskripsi                          |
|----------------------|-------------------------------------|
| username             | Nama pengguna                       |
| name                 | Nama lengkap pengguna               |
| staffCode            | Kode staf pengguna                  |
| phone                | Nomor telepon pengguna              |
| email                | Alamat email pengguna               |
| description          | Teks deskripsi dalam informasi pengguna |
| organization_id      | ID organisasi tempat pengguna berada |
| organization_name    | Nama organisasi tempat pengguna berada |
| team_id              | ID tim tempat pengguna berada       |
| supervisor_id        | ID supervisor pengguna              |
| is_supervisor        | 1 jika pengguna adalah supervisor, 0 jika tidak |

`instancePath`: Mengembalikan path folder instans saat ini.

`appLanguage`: Mengembalikan bahasa aplikasi saat ini yang diatur dalam pengaturan aplikasi (misalnya, vi, en).

`openArgs.[attribute]`: Mengembalikan argumen buka-formulir yang dilewatkan dari ActionButton (act_fill_form, act_get_instance). Nilai default/cadangan adalah teks kosong ("").

`primaryAppColor`: Mengambil warna utama aplikasi.

---

## Contoh penggunaan

### Simpan nama pengguna dan organisasi enumerator

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | enumerator_name | | `pulldata('app-api', 'user.name')` |
| calculate | enumerator_org | | `pulldata('app-api', 'user.organization_name')` |
| calculate | enumerator_email | | `pulldata('app-api', 'user.email')` |

Gunakan dalam label note untuk tujuan audit:
```
note | interviewer_info | Pewawancara: ${enumerator_name} (${enumerator_org})
```

### Informasi perangkat dan layar

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | device_platform | | `pulldata('app-api', 'osPlatform')` |
| calculate | app_ver | | `pulldata('app-api', 'appVersion')` |
| calculate | screen_w | | `pulldata('app-api', 'getDisplayWidth')` |

Berguna untuk pemecahan masalah: ekspor `device_platform` dan `app_ver` bersamaan dengan data Anda untuk mengidentifikasi versi perangkat mana yang digunakan untuk setiap kiriman.

### Waktu server alih-alih waktu perangkat

Jam perangkat bisa salah. Gunakan `serverTime` untuk cap waktu yang lebih andal:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | server_ts | | `pulldata('app-api', 'serverTime')` |

### Logika kondisional berdasarkan peran pengguna

Tampilkan bagian khusus supervisor hanya kepada supervisor:

| type | name | label | relevant |
|------|------|-------|----------|
| calculate | is_supervisor | | `pulldata('app-api', 'user.is_supervisor')` |
| begin_group | supervisor_section | Tinjauan supervisor | `${is_supervisor} = '1'` |
| text | supervisor_notes | Catatan supervisor | |
| end_group | | | |

### Lewatkan argumen dari tombol aksi

Ketika formulir diluncurkan dari tombol aksi `act_fill_form` dengan argumen kustom:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | passed_hh_id | | `pulldata('app-api', 'openArgs.household_id')` |
| calculate | passed_task | | `pulldata('app-api', 'openArgs.task_code')` |

Tombol aksi harus melewatkan argumen dengan kunci yang cocok (misalnya, `household_id`, `task_code`).

### Menggunakan info proyek

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | project | | `pulldata('app-api', 'projectCode')` |
| calculate | project_url | | `pulldata('app-api', 'projectURL')` |

---

## Catatan

- Semua panggilan `pulldata('app-api', ...)` dievaluasi ketika formulir dibuka dan tidak dievaluasi ulang secara dinamis selama sesi (kecuali `serverTime` dan `now()`).
- Jika kunci tidak didukung atau data tidak tersedia, fungsi mengembalikan `'n/a'` (bukan string kosong — uji dengan `!= 'n/a'` bukan `!= ''`).
- Nilai `openArgs` hanya tersedia ketika formulir diluncurkan dari tombol aksi; mereka mengembalikan string kosong jika sebaliknya.
