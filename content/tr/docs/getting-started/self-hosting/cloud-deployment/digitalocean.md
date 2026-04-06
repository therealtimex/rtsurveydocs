---
weight: 1
title: "DigitalOcean"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-17T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "water_drop"
toc: true
description: "Otomatik kullanıcı verileri komut dosyalarını kullanarak rtCloud'u bir DigitalOcean Droplet'e dağıtın."
---

DigitalOcean, ilk açılışta otomatik olarak çalışan **Kullanıcı Verileri** komut dosyalarını kullanır. Komut dosyasının üst kısmındaki yapılandırma değişkenlerini doldurursunuz, ardından bir Damlacık oluştururken komut dosyasının tamamını yapıştırırsınız.

> Linode StackScript'lerden farklı olarak DigitalOcean'ın herhangi bir kullanıcı arayüzü yoktur; yapıştırmadan önce komut dosyasını doğrudan düzenlemeniz gerekir.

**Download script:** [digitalocean-droplet-keycloak-embed.sh](/scripts/digitalocean-droplet-keycloak-embed.sh)

---

## Gömülü Anahtarlık (Önerilen)

Yerleşik SSO ile en basit kurulum için `digitalocean-droplet-keycloak-embed.sh'yi kullanın.

### Adım 1 — Yapılandırmayı doldurun

Komut dosyasını açın ve üstteki `YAPILANDIRMA` bloğunu düzenleyin:

```bash
# --- Required ---
PROJECT_ID="rtsurvey"                  # Unique identifier for your project (no spaces)
ADMIN_PASSWORD="admin"                 # Password for app admin and Keycloak — change after first login

# --- Domain + SSL ---
DOMAIN="myapp.example.com"            # Your domain — DNS A record must point here
PROJECT_URL=""                         # Leave blank unless behind Cloudflare/proxy
LETSENCRYPT_EMAIL="admin@example.com" # Email for Let's Encrypt notifications

# --- Optional ---
STATA_ENABLED="false"
TZ="Asia/Ho_Chi_Minh"
```

| Alan | Gerekli | Açıklama |
|----------|----------|------------|
| `PROJECT_ID` | Evet | Veritabanı adı ve Keycloak istemci kimliği olarak kullanılır. Küçük harf, boşluk yok. |
| 'ADMIN_PASSWORD' | Hayır | Uygulama yöneticisi girişi ve Keycloak yönetici konsolu için şifre. Varsayılan olarak "yönetici" olur — **ilk oturum açmadan sonra değişir**. |
| `ALAN` | Evet | Alan adınız. DNS A kaydı Damlacık IP'sine işaret etmelidir. |
| `LETSENCRYPT_EMAIL` | Evet | Let's Encrypt sertifika bildirimleri için e-posta adresi. |
| `PROJECT_URL` | Hayır | Genel URL'yi geçersiz kılın. "DOMAIN" alanını kullanmak için boş bırakın. Cloudflare'in arkasında kullanışlıdır. |

> **Güvenlik:** Tüm şifreler varsayılan olarak "admin"dir. İlk girişinizden hemen sonra bunları değiştirin.

### Adım 2 — Bir Damlacık Oluşturun

In the [DigitalOcean control panel](https://cloud.digitalocean.com):

1. **Oluştur** → **Damlacıklar**'a tıklayın
2. Resim olarak **Ubuntu 22.04 LTS**'yi seçin
3. **Temel, 4 GB RAM / 2 vCPU** veya daha büyükünü seçin
4. **Gelişmiş Seçenekler** seçeneğine ilerleyin → **Başlatma komut dosyalarını ekle** seçeneğini işaretleyin
5. Komut dosyası içeriğinin tamamını metin alanına yapıştırın
6. **Damlacık Oluştur**'a tıklayın

### 3. Adım — DNS kaydını ekleyin

Droplet önyüklenirken DNS sağlayıcınıza bir **A kaydı** ekleyin:

```
Type  : A
Name  : myapp          (or @ for root domain)
Value : <droplet-ip>
TTL   : 300
```

### Adım 4 — İlerlemeyi izleyin

Droplet'e SSH ekleyin ve günlüğü izleyin:

```bash
ssh root@<droplet-ip>
tail -f /var/log/rtcloud-setup.log
```

Komut dosyası, sunucu IP'nizi başlangıca yakın bir zamanda yazdırır; DNS kaydını görür görmez ekleyin.

### Adım 5 — Uygulamaya erişin

Kurulum tamamlandığında günlükte bir özet gösterilir:

```
============================================================
 rtCloud deployment complete! (Embedded Keycloak)
============================================================
 App URL   : https://myapp.example.com
 Admin     : admin / admin
 Keycloak  : https://myapp.example.com/auth/admin

 !! SECURITY: All passwords default to 'admin'.
    Change them immediately after first login.
============================================================
```

Open `https://myapp.example.com` in your browser and log in with username `admin` and password `admin`.

> **Giriş yaptıktan hemen sonra sağ üst menüdeki **Ayarlar** aracılığıyla şifrenizi değiştirin**.

---

## Dağıtımdan Sonra

### Şifreyi değiştirin

Damlacıkta SSH'yi kullanın, `.env`yi düzenleyin ve etkilenen kapsayıcıyı yeniden başlatın:

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Alanı güncelleyin

Dağıtımdan sonra farklı bir alan atarsanız `.env'de `PROJECT_URL`yi güncelleyin:

```bash
nano /opt/rtcloud/.env   # update PROJECT_URL=
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### View all containers

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```
