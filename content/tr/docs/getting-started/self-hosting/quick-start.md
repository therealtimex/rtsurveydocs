---
weight: 1
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
title: "Hızlı Başlangıç"
icon: "play_circle"
toc: true
description: "Otomatik bir bulut betiği ile dakikalar içinde kendi sunucunuza rtCloud dağıtın."
---

Bu kılavuz, kendi sunucunuzda rtCloud'u çalıştırmanıza yardımcı olur. Otomatik betikler her şeyi halleder — Docker, SSL, veritabanı, güvenlik duvarı — tek bir çalıştırmayla.

## Gereksinimler

### Sunucu

| Kaynak | Minimum | Önerilen |
|--------|---------|---------|
| RAM | 2 GB | 4 GB (Keycloak SSO ile gerekli) |
| Disk | 25 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPUs |
| İşletim Sistemi | Ubuntu 22.04 LTS | Ubuntu 22.04 LTS |

### Alan Adı

Betiği çalıştırmadan önce **sunucunun IP'sine işaret eden A kaydına** sahip bir alan adına ihtiyacınız var. Let's Encrypt SSL sertifikası vermek için DNS çözümlemesi gerektirir.

---

## Bulut Sağlayıcınızı Seçin

Aşağıdan sağlayıcınızı seçin. Her birinin ilk açılışta çalışan ve **5–10 dakika** içinde kurulumu tamamlayan otomatik bir betiği vardır.

| Sağlayıcı | Kılavuz |
|---------|--------|
| Linode (Akamai) | [Linode'a Dağıt](../cloud-deployment/linode) — en kolay, StackScript üzerinden form tabanlı kurulum |
| DigitalOcean | [DigitalOcean'a Dağıt](../cloud-deployment/digitalocean) |
| AWS EC2 | [AWS'ye Dağıt](../cloud-deployment/aws) |
| Google Cloud | [GCP'ye Dağıt](../cloud-deployment/gcp) |

> **Çoğu kullanıcı için önerilir:** Linode ile başlayın — StackScript form tabanlı bir arayüz sunar, bu nedenle manuel olarak düzenlenecek hiçbir şey yoktur.
