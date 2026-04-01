---
title: "Meta"
description: "Tipe pertanyaan meta secara otomatis menangkap informasi perangkat, enumerator, dan waktu tanpa input apa pun dari responden."
icon: "info"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 237
---

Tipe pertanyaan meta adalah bidang khusus yang diisi **secara otomatis** — responden tidak pernah melihatnya. Mereka menangkap konteks tentang pengiriman: kapan dikumpulkan, perangkat mana yang digunakan, dan siapa yang mengumpulkannya. Tambahkan dalam lembar kerja `survey` seperti tipe pertanyaan lainnya; mereka tidak muncul di layar.

## Spesifikasi XLSForm Dasar

| type | name | label |
|------|------|-------|
| start | start | |
| end | end | |
| deviceid | deviceid | |

Label opsional untuk bidang meta karena tidak pernah ditampilkan.

---

## Bidang meta waktu

### `start`

Merekam **tanggal dan waktu saat formulir dibuka**. Disimpan dalam format ISO 8601 (`YYYY-MM-DDTHH:MM:SS.sss+HH:MM`).

```
type    | name  | label
start   | start |
```

### `end`

Merekam **tanggal dan waktu saat formulir dikirimkan**. Bersama dengan `start`, Anda dapat menghitung waktu yang dihabiskan untuk mengisi formulir:

```
type      | name          | calculation
calculate | duration_min  | (decimal-date-time(${end}) - decimal-date-time(${start})) * 1440
```

### `today`

Merekam **tanggal saat ini** (tanpa komponen waktu). Disimpan sebagai `YYYY-MM-DD`. Berguna ketika Anda hanya memerlukan tanggal tanpa cap waktu lengkap.

```
type  | name  | label
today | today |
```

---

## Bidang meta perangkat

### `deviceid`

Merekam **pengidentifikasi unik perangkat** yang digunakan untuk pengumpulan data. Di Android ini biasanya IMEI atau Android ID. Berguna untuk melacak perangkat mana yang mengirimkan setiap formulir dan mendeteksi pengiriman duplikat dari perangkat yang sama.

```
type      | name     | label
deviceid  | deviceid |
```

### `devicephonenum`

Merekam **nomor telepon kartu SIM** dalam perangkat (jika tersedia). Mungkin kosong jika perangkat tidak memiliki SIM atau jika nomor tidak disimpan di SIM.

```
type           | name          | label
devicephonenum | devicephonenum |
```

### `simserial`

Merekam **nomor seri kartu SIM** (ICCID). Berguna untuk mengidentifikasi SIM/operator mana yang digunakan.

```
type      | name      | label
simserial | simserial |
```

### `subscriberid`

Merekam **IMSI (International Mobile Subscriber Identity)** — pengidentifikasi pelanggan unik pada kartu SIM.

```
type         | name        | label
subscriberid | subscriberid |
```

---

## Bidang meta enumerator

### `username`

Merekam **nama pengguna enumerator yang masuk** (akun yang digunakan dalam aplikasi rtSurvey). Ini adalah cara paling andal untuk melacak siapa yang mengumpulkan setiap pengiriman.

```
type     | name     | label
username | username |
```

### `email`

Merekam **alamat email enumerator yang masuk**.

```
type  | name  | label
email | email |
```

### `phonenumber`

Merekam **nomor telepon yang terkait dengan akun enumerator** (jika dikonfigurasi).

```
type        | name       | label
phonenumber | phonenumber |
```

---

## Log audit

### `audit`

Bidang meta `audit` mengaktifkan **pencatatan audit terperinci** — merekam log cap waktu dari setiap pertanyaan yang dikunjungi enumerator, berapa lama mereka menghabiskan waktu untuk masing-masing, dan (secara opsional) lokasi GPS mereka di setiap langkah. Log audit disimpan sebagai file `audit.csv` terpisah bersama setiap pengiriman.

```
type  | name  | parameters
audit | audit | location-priority=balanced location-min-interval=30 location-max-age=60
```

#### Parameter audit

| Parameter | Deskripsi |
|-----------|-----------|
| `location-priority` | Tingkat akurasi GPS: `no-gps`, `low-power`, `balanced`, `high-accuracy` |
| `location-min-interval` | Detik minimum antara pengambilan lokasi |
| `location-max-age` | Usia maksimum (detik) dari lokasi yang di-cache untuk diterima |

Log audit menangkap:
- Nama pertanyaan dan jenis peristiwa (`question`, `form.start`, `form.exit`, `form.save`, `form.finalize`)
- Cap waktu mulai dan berakhir untuk setiap peristiwa
- Koordinat GPS (jika `location-priority` diatur)

{{% alert icon=" " context="warning" %}}
Bidang `audit` menghasilkan file terpisah per pengiriman. Pastikan pipeline data Anda memproses data formulir utama dan CSV audit.
{{% /alert %}}

---

## Contoh lengkap

Survei rumah tangga tipikal mungkin menyertakan semua bidang meta waktu dan enumerator:

| type | name | label |
|------|------|-------|
| start | start | |
| end | end | |
| today | today | |
| deviceid | deviceid | |
| username | username | |
| email | email | |
| audit | audit | |
| text | household_id | ID Rumah Tangga |
| ... | ... | ... |

---

## Praktik Terbaik

1. Selalu sertakan `start` dan `end` — gratis, otomatis, dan sangat berharga untuk pemantauan kualitas.
2. Selalu sertakan `username` untuk melacak enumerator.
3. Sertakan `deviceid` ketika Anda ingin mendeteksi pengiriman duplikat atau melacak perangkat lapangan.
4. Gunakan `audit` dalam survei yang sangat bertanggung jawab di mana Anda perlu memverifikasi bahwa enumerator benar-benar mengunjungi setiap pertanyaan.
5. Bidang terkait SIM (`simserial`, `subscriberid`, `devicephonenum`) hanya andal pada perangkat Android dengan kartu SIM aktif — lewati untuk penerapan hanya tablet.

---

## Keterbatasan

- Semua bidang meta **hanya-baca** — tidak dapat direferensikan atau dimodifikasi oleh kalkulasi lain.
- `username` dan `email` memerlukan enumerator untuk masuk; akan kosong untuk pengiriman anonim.
- Bidang meta SIM/telepon mungkin mengembalikan nilai kosong pada tablet hanya-Wi-Fi dan beberapa versi Android karena pembatasan izin.
