---
weight: 5
title: "Login Pertama"
date: "2026-04-01T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "login"
toc: true
description: "Cara masuk ke instance rtSurvey Anda untuk pertama kali setelah deployment."
---

> **SSL harus dikonfigurasi sebelum masuk.** Jika Anda mengakses aplikasi melalui HTTP, Anda akan melihat peringatan keamanan dan SSO akan diblokir. Selesaikan [Pengaturan SSL](ssl-setup) terlebih dahulu.

Setelah SSL aktif, buka browser Anda di URL HTTPS Anda:

```
https://your-domain.com
```

---

## Layar login

<!-- SCREENSHOT NEEDED: login page over HTTPS — username/password form + SSO button -->

Halaman login menampilkan:

- Kolom **Nama Pengguna** dan **Kata Sandi**
- Tombol **Masuk**
- Tombol **Masuk dengan SSO** (di bawah pemisah) — untuk anggota tim dengan akun SSO

---

## Kredensial admin default

Masukkan kredensial default dan klik **Masuk**:

| Kolom | Nilai |
|-------|-------|
| Nama Pengguna | `admin` |
| Kata Sandi | `admin` |

> **Segera ubah kata sandi Anda setelah login pertama.**

---

## Jika Anda melihat peringatan keamanan

Jika Anda mengakses aplikasi melalui HTTP (sebelum SSL dikonfigurasi), Anda akan melihat:

- Spanduk peringatan kuning di bagian atas halaman login
- Modal saat mengklik **Masuk**, memperingatkan bahwa kredensial akan dikirim tidak terenkripsi

<!-- SCREENSHOT NEEDED: HTTP warning banner on login page -->
<!-- SCREENSHOT NEEDED: SSL warning modal with "Set up SSL" and "Continue anyway" buttons -->

Klik **Atur SSL** untuk mengonfigurasi HTTPS, atau **Lanjutkan saja** untuk masuk tanpa SSL (tidak disarankan).

Login SSO sepenuhnya diblokir melalui HTTP — mengklik **Masuk dengan SSO** akan menampilkan pemberitahuan alih-alih mengalihkan.

---

## Setelah login

Setelah masuk, Anda akan berada di dasbor. Dari sini:

1. **Ubah kata sandi admin** — pengaturan akun → ubah kata sandi
2. **Buat proyek pertama Anda** — Proyek → Proyek Baru
3. **Unggah atau buat formulir** — Formulir → Unggah XLSForm atau buka Form Builder
4. **Tambahkan pengguna** — Pengguna → Undang atau buat akun untuk tim Anda
