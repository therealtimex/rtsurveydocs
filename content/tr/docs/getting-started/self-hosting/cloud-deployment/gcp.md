---
weight: 4
title: "Google Cloud (GCP)"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-16T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "travel_explore"
toc: true
description: "gcp-compute.sh başlangıç betiğini kullanarak Google Cloud Compute Engine üzerine rtCloud dağıtın."
---

Compute Engine VM örneği oluştururken `gcp-compute.sh` dosyasını **Başlangıç betiği** olarak kullanın. Betik, ilk açılışta otomatik olarak çalışır.

**Betiği indirin:** [gcp-compute.sh](/scripts/gcp-compute.sh)

---

## Adım 1 — Yapılandırmayı doldurun

Betiği açın ve üstteki `CONFIGURATION` bloğunu düzenleyin:

```bash
# --- Gerekli ---
PROJECT_ID="rtsurvey"
ADMIN_PASSWORD="admin"                       # İlk girişten sonra değiştirin

# --- Alan Adı + SSL ---
DOMAIN="myapp.example.com"
LETSENCRYPT_EMAIL="admin@example.com"

# --- Yerleşik Keycloak ---
EMBED_KEYCLOAK="true"
KEYCLOAK_ADMIN_PASSWORD="${ADMIN_PASSWORD}"  # ADMIN_PASSWORD varsayılan değerine sahiptir
```

| Alan | Gerekli | Açıklama |
|-------|----------|-------------|
| `PROJECT_ID` | Evet | Veritabanı adı ve Keycloak istemci kimliği olarak kullanılır. Küçük harf, boşluk yok. |
| `ADMIN_PASSWORD` | Hayır | Uygulama yöneticisi şifresi ve Keycloak yönetici şifresi. Varsayılan `admin` — **ilk girişten sonra değiştirin**. |
| `DOMAIN` | Hayır | HTTPS için alan adınız. Yalnızca HTTP modu için boş bırakın. |
| `LETSENCRYPT_EMAIL` | Evet (DOMAIN ayarlanmışsa) | Let's Encrypt bildirimleri için e-posta. |
| `EMBED_KEYCLOAK` | Hayır | Yerleşik Keycloak dağıtmak için `true` (4 GB RAM gerektirir). |

> **Güvenlik:** Tüm şifreler varsayılan olarak `admin`'dir. İlk girişinizden hemen sonra değiştirin.

---

## Adım 2 — VM örneği oluşturun

[Google Cloud Konsolunda](https://console.cloud.google.com/compute):

1. **Örnek oluştur**'a tıklayın
2. **Makine yapılandırması:**
   - Seri: `E2`
   - Makine türü: `e2-medium` (4 GB RAM) veya daha büyük
3. **Başlangıç diski:**
   - İşletim sistemi: Ubuntu
   - Sürüm: Ubuntu 22.04 LTS
   - Boyut: 40 GB veya daha fazla
4. **Güvenlik duvarı:** **HTTP trafiğine izin ver** ve **HTTPS trafiğine izin ver** seçeneklerini işaretleyin
5. **Gelişmiş seçenekler** → **Yönetim** → **Otomasyon** → **Başlangıç betiği** → betiğin tam içeriğini yapıştırın
6. **Oluştur**'a tıklayın

---

## Adım 3 — DNS kaydını ekleyin

VM açılırken DNS sağlayıcınıza bir **A kaydı** ekleyin:

```
Tür  : A
Ad   : myapp
Değer: <vm-harici-ip>
TTL  : 300
```

Harici IP'yi konsolda VM örnekleri listesinde bulabilirsiniz.

---

## Adım 4 — İlerlemeyi izleyin

`gcloud` CLI kullanarak:

```bash
gcloud compute ssh <instance-name> -- tail -f /var/log/rtcloud-setup.log
```

Veya doğrudan SSH ile:

```bash
ssh <username>@<vm-external-ip>
tail -f /var/log/rtcloud-setup.log
```

---

## Adım 5 — Uygulamaya erişin

Kurulum tamamlandığında günlük, uygulama URL'nizi ve kimlik bilgilerinizi içeren bir özet gösterir. `admin` kullanıcı adı ve `admin` şifresiyle giriş yapın, ardından hemen şifrenizi değiştirin.

---

## Güvenlik Duvarı Kuralları

GCP'nin **HTTP/HTTPS'ye izin ver** onay kutuları 80 ve 443 portlarını açar. 3838 portu üzerinden doğrudan Shiny erişimine de izin vermek için bir güvenlik duvarı kuralı ekleyin:

```bash
gcloud compute firewall-rules create allow-shiny \
  --allow tcp:3838 \
  --target-tags http-server
```

Veya konsol üzerinden ekleyin: **VPC Ağı** → **Güvenlik Duvarı** → **Kural oluştur**.

> Port 3306'yı (MySQL) **açmayın** — asla genel erişime açık olmamalıdır.

---

## Statik IP (isteğe bağlı)

Varsayılan olarak GCP, VM yeniden başlatmada değişen geçici bir harici IP atar. Kararlı bir IP tutmak için:

1. **VPC Ağı** → **IP adresleri**'ne gidin
2. **Harici statik adres ayır**'a tıklayın
3. VM örneğinize atayın

---

## Dağıtım Sonrası

### Şifre değiştirme

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Tüm konteynerleri görüntüleme

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```
