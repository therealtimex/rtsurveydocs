---
weight: 3
title: "Bulut Dağıtımı"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-16T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "cloud_upload"
toc: true
description: "DigitalOcean, AWS EC2, Google Cloud ve Linode için otomatik betiklerle rtCloud'u büyük bulut sağlayıcılarına dağıtın."
---

Dağıtım deposu, büyük bulut sağlayıcıları için otomatik sağlama betikleri içermektedir. Her betik, yeni bir **Ubuntu 22.04 LTS** sunucusunun ilk açılışında çalışır ve tamamen katılımsız bir kurulum gerçekleştirir:

- Docker ve Docker Compose'u yükler
- Tüm dahili hizmetler için güvenli rastgele şifreler oluşturur
- `docker-compose.production.yml` ve `.env` dosyalarını yazar
- Nginx'i ters proxy olarak yapılandırır
- Let's Encrypt'ten ücretsiz TLS sertifikası alır (DNS çözümlenene kadar otomatik olarak yeniden dener)
- UFW güvenlik duvarını yapılandırır
- İsteğe bağlı olarak yerleşik Keycloak SSO sunucusunu dağıtır
- Tüm kimlik bilgileriyle birlikte tam dağıtım özeti çıktılar

Kurulum, standart bir örnekte **5–10 dakika** içinde tamamlanır.

---

## Betik Seçimi

Bulut sağlayıcınıza ve SSO kurulumunuza bağlı olarak birden fazla betik varyantı mevcuttur:

| Betik | Sağlayıcı | SSO Modu | En İyi Kullanım |
|--------|----------|----------|----------|
| `digitalocean-droplet-keycloak-embed.sh` | DigitalOcean | Yerleşik Keycloak | Basit, kendi kendine yeten SSO |
| `digitalocean-droplet.sh` | DigitalOcean | Keycloak veya Harici OIDC | Tam kontrol |
| `linode-stackscript-keycloak-embed.sh` | Linode | Yerleşik Keycloak | Form tabanlı kurulum, en basit |
| `linode-stackscript-oidc.sh` | Linode | Yalnızca Harici OIDC | Mevcut kimlik sağlayıcısı |
| `linode-stackscript.sh` | Linode | Keycloak veya Harici OIDC | Tam kontrol |
| `aws-ec2.sh` | AWS EC2 | Keycloak veya Harici OIDC | AWS dağıtımları |
| `gcp-compute.sh` | Google Cloud | Keycloak veya Harici OIDC | GCP dağıtımları |

> **Çoğu kullanıcı için öneri:** `keycloak-embed` varyantını kullanın. Yerleşik bir Keycloak kimlik sunucusu içerir ve en az yapılandırma alanı gerektirir.

---

## Sunucu Boyutlandırma Kılavuzu

| Kullanım Durumu | RAM | Disk | Örnek |
|----------|-----|------|---------|
| Değerlendirme / geliştirme | 2 GB | 25 GB | DO Basic $18/ay, t3.small, e2-small |
| Küçük ekip (< 50 kullanıcı) | 4 GB | 40 GB | DO Basic $24/ay, t3.medium, e2-medium |
| Üretim (> 50 kullanıcı) | 8 GB | 80 GB | DO General $48/ay, t3.large, n2-standard-2 |

> Yerleşik Keycloak en az **4 GB RAM** gerektirir. Keycloak olmadan değerlendirme için yalnızca 2 GB kullanın.

---

## DNS Kurulumu

Tüm betikler, Let's Encrypt'in sertifika verebilmesi için **sunucunuzun IP'sine işaret eden bir A kaydına sahip** bir alan adı gerektirir.

Betik, kurulum sürecinin başlarında sunucu IP'nizi yazdırır:

```
============================================================
 Server IP : 139.162.51.85
 Add this DNS A record now if you haven't already:
   myapp.example.com  ->  139.162.51.85
 The script will retry Certbot every 60s until DNS resolves.
============================================================
```

Betik, 1 saate kadar her 60 saniyede bir Let's Encrypt'i **otomatik olarak yeniden dener**. DNS kaydını ekleyin ve bekleyin — yeniden başlatma gerekmez.

> **Oran sınırı:** Let's Encrypt, alan adı başına 7 günde en fazla **5 sertifikaya** izin verir. Aynı alan adıyla sunucuları tekrar tekrar dağıtıp yok etmekten kaçının. Sınıra ulaşırsanız betik bir `yeniden deneme sonrası` zaman damgası görüntüler ve hemen durur.

---

## Dağıtım Sonrası Kontrol Listesi

- [ ] Uygulama `https://your-domain.com` adresinde açılıyor
- [ ] `admin` ve yapılandırdığınız şifreyle giriş yapın
- [ ] Tüm konteynerler sağlıklı: `docker compose -f /opt/rtcloud/docker-compose.production.yml ps`
- [ ] Let's Encrypt yenileme çalışıyor: `certbot renew --dry-run`
- [ ] MySQL portu 3306 **açık değil**: `ufw status`
- [ ] Günlük veritabanı yedeklemesi kurun (bkz. [Bakım](../maintenance))

---

## Sorun Giderme

### Tam kurulum günlüğünü kontrol edin

```bash
# Linode
tail -200 /var/log/stackscript.log

# DigitalOcean / AWS / GCP
tail -200 /var/log/rtcloud-setup.log
```

### Let's Encrypt oran sınırı

Günlükte `too many certificates` görürseniz, 5 sertifika/7 gün sınırına ulaştınız. Günlük tam yeniden deneme süresini gösterir:

```
[SSL] ERROR: Let's Encrypt rate limit hit. retry after 2026-03-15 16:22 UTC.
```

O zamana kadar bekleyin, ardından yeniden dağıtın.

### Keycloak sağlıksız kalıyor

Sunucunun en az 4 GB RAM'e sahip olduğundan emin olun, ardından günlükleri kontrol edin:

```bash
docker logs rtcloud-keycloak --tail 50
free -h
```

### Certbot'tan sonra SSL yapılandırması uygulanmadı

Sertifika verildi ancak Nginx hâlâ yalnızca HTTP gösteriyorsa, günlükte hata satırını kontrol edin ve Nginx'i manuel olarak yeniden yükleyin:

```bash
nginx -t && systemctl reload nginx
```
