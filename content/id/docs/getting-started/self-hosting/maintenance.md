---
weight: 5
title: "Pemeliharaan"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "build"
toc: true
description: "Pemeliharaan sehari-hari untuk instans rtCloud yang di-hosting sendiri: peningkatan, pencadangan, pemulihan, dan pemecahan masalah umum."
---

## Perintah Umum

Gunakan perintah ini secara rutin untuk mengelola container rtCloud Anda. Jalankan dari direktori yang berisi `docker-compose.production.yml`.

```bash
# Periksa status dan kesehatan semua container
docker compose -f docker-compose.production.yml ps

# Lihat log langsung (semua layanan)
docker compose -f docker-compose.production.yml logs -f

# Lihat log hanya untuk aplikasi
docker compose -f docker-compose.production.yml logs -f rtcloud

# Restart satu container
docker compose -f docker-compose.production.yml restart rtcloud

# Hentikan semua layanan
docker compose -f docker-compose.production.yml down

# Mulai semua layanan
docker compose -f docker-compose.production.yml up -d

# Buka shell di dalam container aplikasi
docker compose -f docker-compose.production.yml exec rtcloud bash
```

---

## Peningkatan

Pembaruan rtCloud didistribusikan sebagai tag image Docker baru. Peningkatan menarik image terbaru dan membuat ulang container aplikasi. Migrasi database berjalan secara otomatis saat startup.

**1. Tarik image terbaru:**

```bash
docker compose -f docker-compose.production.yml pull
```

**2. Buat ulang container aplikasi:**

```bash
docker compose -f docker-compose.production.yml up -d
```

Docker hanya mengganti container yang imagenya telah berubah. Container MySQL dan semua volume bernama tidak terpengaruh.

### Menyematkan Versi

Untuk meningkatkan ke versi tertentu alih-alih `latest`, perbarui `RTCLOUD_IMAGE` di `.env`:

```dotenv
RTCLOUD_IMAGE=rtawebteam/rta-smartsurvey:1.2.3
```

Kemudian jalankan `docker compose pull` dan `up -d` seperti di atas.

### Penurunan Versi

Penurunan versi umumnya tidak direkomendasikan, karena migrasi database tidak dapat dibalik. Jika penurunan versi diperlukan, pulihkan dari cadangan database yang diambil sebelum peningkatan.

---

## Pencadangan dan Pemulihan

### Cadangkan Database

Jalankan perintah ini untuk mengekspor database aplikasi ke file SQL:

```bash
docker compose -f docker-compose.production.yml exec mysql \
  mysqldump -u root -p"$(grep MYSQL_ROOT_PASSWORD .env | cut -d= -f2)" smartsurvey \
  > backup-$(date +%Y%m%d-%H%M%S).sql
```

File cadangan ditulis ke direktori saat ini di host.

### Pulihkan Database

```bash
docker compose -f docker-compose.production.yml exec -T mysql \
  mysql -u root -p"$(grep MYSQL_ROOT_PASSWORD .env | cut -d= -f2)" smartsurvey \
  < backup-20240101-120000.sql
```

### Cadangkan File yang Diunggah

Kiriman survei sering menyertakan file yang diunggah (foto, audio, dokumen) yang disimpan dalam volume Docker bernama. Cadangkan secara terpisah dari database:

```bash
# Cadangkan unggahan
docker run --rm \
  -v rtcloud_uploads:/data \
  -v "$(pwd):/backup" \
  alpine tar czf /backup/uploads-$(date +%Y%m%d).tar.gz -C /data .

# Cadangkan rekaman audio
docker run --rm \
  -v rtcloud_audios:/data \
  -v "$(pwd):/backup" \
  alpine tar czf /backup/audios-$(date +%Y%m%d).tar.gz -C /data .
```

Ganti `rtcloud_uploads` dan `rtcloud_audios` dengan nama volume Anda yang sebenarnya (diawali oleh `COMPOSE_PROJECT_NAME`) jika Anda mengubah default.

### Pulihkan File yang Diunggah

```bash
docker run --rm \
  -v rtcloud_uploads:/data \
  -v "$(pwd):/backup" \
  alpine tar xzf /backup/uploads-20240101.tar.gz -C /data
```

### Pencadangan Harian Otomatis

Tambahkan cron job di host untuk menjalankan cadangan secara otomatis. Edit crontab root dengan `crontab -e`:

```cron
# Cadangan database harian pukul 02.00, simpan 30 hari riwayat
0 2 * * * cd /opt/rtcloud && docker compose -f docker-compose.production.yml exec -T mysql \
  mysqldump -u root -p"$(grep MYSQL_ROOT_PASSWORD .env | cut -d= -f2)" smartsurvey \
  > /backups/db-$(date +\%Y\%m\%d).sql && \
  find /backups -name "db-*.sql" -mtime +30 -delete
```

---

## Pemecahan Masalah

### Container aplikasi tidak dapat dimulai

Periksa log container untuk pesan kesalahan:

```bash
docker compose -f docker-compose.production.yml logs rtcloud
```

Penyebab umum:
- Variabel lingkungan yang hilang atau tidak valid di `.env`
- MySQL belum siap (tunggu 60 detik dan periksa lagi)
- Konflik port — proses lain sudah menggunakan `APP_PORT`

### MySQL tidak sehat

```bash
docker compose -f docker-compose.production.yml logs mysql
```

Penyebab umum:
- `MYSQL_ROOT_PASSWORD` tidak ditetapkan di `.env`
- Volume data rusak (jarang — periksa ruang disk dengan `df -h`)

MySQL dapat membutuhkan waktu 30–60 detik untuk diinisialisasi pada booting pertama. Tunggu dan periksa lagi sebelum menganggap gagal.

### Port sudah digunakan

Ubah `APP_PORT` atau `SHINY_PORT` di `.env` ke port yang bebas, lalu buat ulang container:

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate
```

Untuk menemukan apa yang menggunakan port di host:

```bash
lsof -i :8080
```

### 400 CSRF Token Could Not Be Verified

Kesalahan ini muncul di lingkungan lokal atau reverse-proxy di mana asal permintaan tidak cocok dengan host yang diharapkan. Nonaktifkan validasi CSRF hanya untuk pengembangan lokal:

```dotenv
CSRF_VALIDATION_ENABLED=false
```

Kemudian restart aplikasi:

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

> Jangan nonaktifkan validasi CSRF di produksi. Jika kesalahan ini terjadi di produksi, pastikan reverse proxy Anda meneruskan header `Host` dan `X-Forwarded-For` yang benar.

### Lupa Kata Sandi Admin

Reset kata sandi admin langsung di database. Hubungkan ke container MySQL dan perbarui hash kata sandi:

**Langkah 1** — Buat hash kata sandi baru. Ganti `newpassword` dengan kata sandi yang Anda inginkan:

```bash
docker compose -f docker-compose.production.yml exec rtcloud php -r "
  \$salt = trim(shell_exec(\"mysql -h mysql -u root -p\\\"\${MYSQL_ROOT_PASSWORD}\\\" \${MYSQL_DATABASE} -se \\\"SELECT salt FROM ss_user WHERE username='admin';\\\"\"));
  echo md5(\$salt . 'newpassword') . PHP_EOL;
"
```

**Langkah 2** — Perbarui hash di database:

```bash
docker compose -f docker-compose.production.yml exec mysql \
  mysql -u root -p"${MYSQL_ROOT_PASSWORD}" smartsurvey \
  -e "UPDATE ss_user SET password='<hash_from_step_1>' WHERE username='admin';"
```

### Container terus me-restart

Periksa apakah pemeriksaan kesehatan gagal:

```bash
docker compose -f docker-compose.production.yml ps
docker inspect rtcloud-app --format '{{json .State.Health}}'
```

Pemeriksaan kesehatan aplikasi memanggil endpoint `/health`. Jika gagal berulang kali, periksa log aplikasi untuk kesalahan startup.

### Ruang disk penuh

Identifikasi apa yang menggunakan ruang:

```bash
# Periksa penggunaan disk host
df -h

# Periksa penggunaan disk Docker (image, container, volume)
docker system df

# Hapus image yang tidak digunakan dan container yang dihentikan (aman untuk dijalankan)
docker system prune
```

Jangan gunakan `docker system prune --volumes` karena ini akan menghapus data aplikasi.

---

## Pemeriksaan Kesehatan

Setiap layanan memiliki pemeriksaan kesehatan otomatis. Status container mencerminkan hasilnya:

| Container | Metode Pemeriksaan | Periode Mulai | Interval |
|-----------|-------------------|---------------|----------|
| `rtcloud-app` | HTTP GET `/health` | 90 detik | 30 detik |
| `rtcloud-mysql` | `mysqladmin ping` | 30 detik | 10 detik |
| `rtcloud-keycloak` | HTTP GET `:9000/health/live` | 120 detik | 30 detik |

Container dengan pemeriksaan kesehatan yang gagal secara otomatis di-restart sesuai pengaturan `RESTART_POLICY` (default: `unless-stopped`).
