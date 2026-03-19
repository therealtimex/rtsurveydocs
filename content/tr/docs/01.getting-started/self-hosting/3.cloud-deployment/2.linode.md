---
weight: 2
title: "Linode (Akamai Cloud)"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-17T01:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "dns"
toc: true
description: "Form tabanlı yapılandırma arayüzüyle StackScript'ler kullanarak Linode üzerine rtCloud dağıtın."
---

Linode, herhangi bir kodu düzenlemeden Linode Manager'da doğrudan yapılandırma alanlarını doldurduğunuz form tabanlı bir arayüze sahip betikler olan **StackScript'leri** kullanır.

> Linode StackScript'leri en kolay dağıtım yöntemidir. Linode oluştururken alanlar bir form olarak görünür — betik düzenleme gerekmez.

---

## Yerleşik Keycloak (Önerilen)

### Adım 1 — StackScript'i Bulun

StackScript, Linode topluluğunda herkese açık olarak mevcuttur — manuel kurulum gerekmez:

1. **Linodes** → **Linode Oluştur** seçeneğine gidin
2. **Dağıtım Seç** altında **StackScript'ler** → **Topluluk StackScript'leri** seçeneğini seçin
3. **`RTA rtSurvey - Self-Hosted with Keycloak SSO`** için arama yapın
4. Seçin ve yapılandırma formunu doldurun:

> Alternatif olarak, [betiği indirin](/scripts/linode-stackscript-keycloak-embed.sh) ve **StackScript'ler** → **StackScript Oluştur** altında kendi StackScript'inizi oluşturun.

| Alan | Gerekli | Açıklama |
|-------|----------|-------------|
| Proje Kimliği | Hayır | Benzersiz tanımlayıcı (varsayılan: `rtsurvey`). Veritabanı adı ve Keycloak istemci kimliği olarak kullanılır. |
| Keycloak Yönetici Şifresi | Hayır | Hem Keycloak yönetici konsolu hem de uygulama yöneticisi girişi için şifre. Varsayılan `admin` — **ilk girişten sonra değiştirin**. |
| Alan Adı | Evet | Alan adınız. DNS A kaydı bu Linode'un IP'sine işaret etmelidir. HTTPS ve Keycloak için gereklidir. |
| Let's Encrypt E-postası | Evet | Let's Encrypt sertifika bildirimleri için e-posta. |
| Docker Görüntü Etiketi | Hayır | Dağıtılacak görüntü (varsayılan: `rtawebteam/rta-smartsurvey:survey-dockerize`). |

> **Güvenlik:** Tüm şifreler varsayılan olarak `admin`'dir. İlk girişinizden hemen sonra değiştirin.

5. Görüntü olarak **Ubuntu 22.04 LTS** seçin
6. **Paylaşımlı CPU 4 GB** planı veya daha büyük seçin
7. **Linode Oluştur**'a tıklayın

### Adım 2 — DNS kaydını ekleyin

Linode açılırken DNS sağlayıcınıza bir **A kaydı** ekleyin:

```
Tür  : A
Ad   : myapp          (veya kök etki alanı için @)
Değer: <linode-ip>
TTL  : 300
```

### Adım 3 — İlerlemeyi izleyin

```bash
ssh root@<linode-ip>
tail -f /var/log/stackscript.log
```

Betik sunucu IP'nizi başlangıçta yazdırır — görür görmez DNS kaydını ekleyin.

### Adım 4 — Uygulamaya erişin

Kurulum tamamlandığında günlük bir özet gösterir:

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

`admin` kullanıcı adı ve `admin` şifresiyle giriş yapın, ardından hemen şifrenizi değiştirin.

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

### Günlüğü kontrol etme

```bash
tail -200 /var/log/stackscript.log
```
