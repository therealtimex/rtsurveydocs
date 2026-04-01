---
weight: 2
title: "Deployment"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "dns"
toc: true
description: "Terapkan dan kelola instans rtCloud Anda sendiri menggunakan Docker. Kendali penuh atas data, infrastruktur, dan konfigurasi Anda."
---

Jalankan rtCloud di infrastruktur Anda sendiri menggunakan Docker Compose. Self-hosting memberi Anda kepemilikan penuh atas data, jaringan, dan lingkungan penerapan Anda — ideal untuk organisasi dengan persyaratan residensi data, jaringan yang terisolasi dari internet, atau kebutuhan infrastruktur khusus.

## Apa itu Self-Hosting rtCloud?

rtCloud Self-Hosting adalah image Docker resmi yang mengemas seluruh platform rtCloud ke dalam tumpukan container portabel yang dapat Anda jalankan di server Linux mana pun. Tumpukan ini mencakup:

| Layanan | Deskripsi |
|---------|------------|
| **Aplikasi rtCloud** | Aplikasi web Apache 2.4 + PHP 7.4 dengan antrian latar belakang bawaan (Beanstalkd), server analitik (Shiny), dan tugas terjadwal |
| **MySQL 8.0** | Database relasional untuk semua data aplikasi dan survei |
| **Keycloak** *(opsional)* | Server Single Sign-On tertanam untuk manajemen identitas perusahaan |

## Kapan Menggunakan Self-Hosting

Self-hosting adalah pilihan yang tepat ketika Anda:

- Memerlukan **kedaulatan data** — semua data tetap berada di infrastruktur Anda sendiri
- Beroperasi di **jaringan yang terisolasi atau terbatas** tanpa akses cloud eksternal
- Memiliki **persyaratan kepatuhan** (GDPR, HIPAA, kebijakan data pemerintah) yang mengharuskan penyimpanan di tempat
- Perlu berintegrasi dengan **penyedia identitas internal** (Active Directory, LDAP, SAML)
- Ingin **menyesuaikan sumber daya** — alokasi CPU, RAM, dan penyimpanan sesuai ketentuan Anda

## Dalam Bagian Ini

| Halaman | Deskripsi |
|---------|-----------|
| [Mulai Cepat](quick-start) | Jalankan rtCloud di server dalam waktu kurang dari 10 menit |
| [Referensi Konfigurasi](configuration) | Daftar lengkap semua variabel lingkungan dan nilai defaultnya |
| [Penerapan Cloud](cloud-deployment) | Skrip otomatis satu klik untuk DigitalOcean, AWS, GCP, dan Linode |
| [Autentikasi SSO](sso-authentication) | Konfigurasikan Keycloak, OIDC eksternal, atau Azure AD |
| [Pemeliharaan](maintenance) | Tingkatkan, cadangkan, pulihkan, dan pecahkan masalah instans Anda |

## Ikhtisar Arsitektur

Penerapan berjalan sebagai sekumpulan container Docker yang terhubung di jaringan internal:

```
┌────────────────────────────────────────┐
│            rtcloud-app                 │
│  Apache 2.4 (port 80)                  │
│  Aplikasi PHP 7.4                      │
│  Antrian Beanstalkd (internal)         │
│  Shiny Server (port 3838)              │
│  Penjadwal Cron                        │
└─────────────────┬──────────────────────┘
                  │ rtcloud-net (bridge)
┌─────────────────▼──────────────────────┐
│            rtcloud-mysql               │
│  MySQL 8.0 (port 3306, internal saja)  │
└────────────────────────────────────────┘
```

Ketika SSO diaktifkan, container ketiga berjalan bersamaan:

```
┌─────────────────────────────────────────┐
│            rtcloud-keycloak             │
│  Keycloak (port 8080, internal saja)    │
│  UI Admin (port 9000, internal saja)    │
└─────────────────────────────────────────┘
```

Semua container berkomunikasi melalui jaringan bridge Docker yang terisolasi. Hanya port aplikasi web dan (opsional) port analitik Shiny yang diekspos ke host.
