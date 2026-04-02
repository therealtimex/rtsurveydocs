---
weight: 2
title: "Linode (Akamai Cloud)"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "dns"
toc: true
description: "StackScript kullanarak rtCloud'i Linode'e dağıtın. Yapılandırma gerekmez; yalnızca sunucuyu oluşturun ve dağıtım sonrası adımları izleyin."
---

## Adım 1 — StackScript'i başlatın

**[Deploy rtSurvey on Linode →](https://cloud.linode.com/stackscripts/2049143)**

Bu, Linode Bulut Yöneticisinde StackScript sayfasını açar. **Yeni Linode Dağıt**'a tıklayın.

---

## Adım 2 — Linode formunu doldurun

Linode'in standart sunucu oluşturma formunu doldurun:

| Alan | Önerilen değer |
|----------|----------|
| **Resim** | Ubuntu 22,04 LTS |
| **Bölge** | Kullanıcılarınıza en yakın |
| **Plan** | Paylaşılan CPU 4 GB veya daha büyük |
| **Kök Şifresi** | Güçlü bir şifre belirleyin |
| **Firewall** | No Firewall *(recommended)* |
| **Timezone** *(our only field)* | Your server timezone (default: `Asia/Ho_Chi_Minh`) |

> **Neden güvenlik duvarı yok?** Kurulum komut dosyasının giden internet erişimine ihtiyacı vardır (Docker çeker, Let's Encrypt). İlk önyükleme sırasında bağlantı noktalarının engellenmesi dağıtımın başarısız olmasına neden olabilir. Kurulum tamamlandıktan sonra bir güvenlik duvarı ekleyebilirsiniz. Doğru kurallar için aşağıdaki [Güvenlik duvarı kuralları](#firewall-rules-linode-cloud-firewall) konusuna bakın.

İşiniz bittiğinde **Linode Oluştur**'a tıklayın.

---

## Adım 3 — Kurulumun tamamlanmasını bekleyin

Komut dosyası ilk açılışta otomatik olarak çalışır. Docker'i yükler, rtSurvey görüntüsünü çeker, veritabanını başlatır ve tüm hizmetleri başlatır. Bu **5–10 dakika** sürer.

İlerlemeyi doğrudan **Linode Bulut Yöneticisi**'nde izleyebilirsiniz; SSH gerekmez:

1. Go to your [Linode dashboard](https://cloud.linode.com/linodes)
2. Yeni oluşturulan Linode'inize tıklayın
3. **LISH Konsolunu Başlat**'a tıklayın (Linode ayrıntı sayfasının sağ üst kısmında)

Canlı önyükleme günlüğünü gösteren bir tarayıcı terminali açılır — **Weblish** sekmesi doğrudan tarayıcınızda çalışır, SSH istemcisine gerek yoktur.

![Lish Console showing rtSurvey StackScript running](/img/first-login/lish-console.png)

Şunu görene kadar bekleyin:

```
============================================================
 rtSurvey deployment complete!
============================================================
 Server IP : <your-server-ip>

 App URL   : http://<your-server-ip>  (HTTP only until domain is set)
 Admin     : admin / admin
============================================================
```

Günlük aynı zamanda sunucu IP'nizi de gösterir; bir sonraki adım için buna ihtiyacınız olacak.

---

## Adım 4 — SSL'yi ayarlayın

Open your browser at `http://<server-ip>`. The app will redirect you to the SSL setup screen.

HTTPS'yi yapılandırmak için **[SSL Kurulum kılavuzunu →](../ssl-setup)** izleyin. Ücretsiz **rtsurvey.com alt alan adı** en hızlı seçenektir; DNS kurulumu gerekmez.

---

## Adım 5 — İlk oturum açma

SSL etkinleştirildikten sonra yönetici hesabına erişmek için **[İlk Giriş kılavuzu →](../first-login)** kılavuzunu izleyin.

---

## Adım 6 — Varsayılan şifreyi değiştirin

Tüm şifreler varsayılan olarak "admin"dir. İlk girişinizden hemen sonra bunları değiştirin:

- **Uygulama yöneticisi şifresi** — uygulama içindeki hesap ayarları
- **Keycloak admin** — accessible at `https://your-domain.com/auth/admin` (login: `admin` / `admin`)

---

## Güvenlik duvarı kuralları (Linode Bulut Güvenlik Duvarı)

Bu sunucuya bir Linode Bulut Güvenlik Duvarı eklerseniz aşağıdaki kuralları kullanın:

### Gelen

| Etiket | Eylem | Protokol | Liman | Kaynaklar | Notlar |
|----------|-----------|----------|------|------------|-------|
| `gelen-ssh'yi kabul et' | Kabul et | TCP | 22 | Tüm IPv4, Tüm IPv6 | SSH erişimi |
| 'gelen-http'yi kabul et' | Kabul et | TCP | 80 | Tüm IPv4, Tüm IPv6 | Nginx (HTTP + ACME mücadelesi) |
| `gelen-https'yi kabul et` | Kabul et | TCP | 443 | Tüm IPv4, Tüm IPv6 | Nginx (SSL kurulumundan sonra HTTPS) |
| `gelen-parlak kabul' | Kabul et | TCP | 3838 | Tüm IPv4, Tüm IPv6 | Parlak Sunucu (R analitiği) |
| 'gelen-icmp'yi kabul et' | Kabul et | ICMP | — | Tüm IPv4, Tüm IPv6 | Ping / teşhis |
| Varsayılan gelen politikası | **Bırak** | | | | Diğer her şeyi engelle |

### Giden

| Etiket | Eylem | Notlar |
|----------|-----------|-------|
| Varsayılan giden politikası | **Kabul et** | Tüm gidenlere izin ver (Docker çekmeleri, sertifika botu, GoDaddy API, vb.) |

### Bağlantı noktalarına harici olarak gerek DEĞİLDİR

Bu bağlantı noktaları yalnızca "127.0.0.1"e bağlıdır ve sunucunun dışından hiçbir zaman erişilemez:

| Liman | Hizmet | Nedeni |
|------|------------|--------|
| 8080 | Uygulama kapsayıcısı | Nginx dahili olarak proxy'ler |
| 8090 | Keycloak konteyneri | Nginx dahili olarak proxy'ler |
| 3306 | MySQL | Yalnızca dahili Docker ağı |

---

## Sorun Giderme

### Kurulum günlüğünü kontrol edin

```bash
tail -200 /var/log/stackscript.log
```

### SSL günlüğünü kontrol edin

```bash
tail -200 /var/log/rtsurvey-ssl.log
```

### Konteyner durumunu görüntüle

```bash
docker compose -f /opt/rtsurvey/docker-compose.production.yml ps
```
