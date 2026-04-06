---
weight: 4
title: "SSL'yi Ayarla"
date: "2026-04-01T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "lock"
toc: true
description: "rtSurvey sunucunuz için HTTPS'yi yapılandırın. Oturum açabilmeniz için gereklidir."
---

Giriş yapabilmeniz için SSL'nin yapılandırılması gerekmektedir. Uygulamayı ilk açtığınızda otomatik olarak SSL kurulum ekranına yönlendirileceksiniz.

---

## SSL kurulum seçenekleri

![SSL kurulum seçenekleri](/img/ssl-setup/ssl-setup-options.png)

Üç seçenekten birini seçin:

| Seçenek | Ne zaman kullanılmalı |
|--------|-------------|
| **Ücretsiz rtsurvey.com alt alan adı** *(Tavsiye edilen)* | DNS kurulumuna gerek yok. Kayıtları sizin için oluşturuyoruz. 2-5 dakika içinde hazır. |
| **Kendi etki alanım** | Zaten bir etki alanınız var ve DNS'si bu sunucuyu işaret ediyor. |
| **Sertifikayı manuel olarak yükleyin** | Kurumsal veya özel CA. SSH erişimi gerektirir. |

---

## Seçenek 1 — Ücretsiz rtsurvey.com alt alan adı (Önerilen)

Bu en hızlı seçenektir. Etki alanı kaydı veya DNS değişikliği gerekmez.

1. Bölümü genişletmek için Ücretsiz rtsurvey.com alt alan adına tıklayın
2. İstediğiniz alt alan adını giriş alanına yazın

   > Küçük harfler, sayılar ve kısa çizgiler kullanın. 3–30 karakter.
   > Örnek: `myproject` → `myproject.rtsurvey.com`

3. Oluştur'a tıklayın **https://[subdomain].rtsurvey.com**

<!-- SCREENSHOT NEEDED: subdomain input filled in, before clicking Create -->

4. Sertifika verilirken 2-5 dakika bekleyin

<!-- SCREENSHOT NEEDED: certificate being issued / progress state -->

5. Sertifika hazır olduğunda otomatik olarak yeni HTTPS URL'nize yönlendirileceksiniz.

<!-- SCREENSHOT NEEDED: success state / redirect to login -->

---

## Option 2 — My own domain

Mevcut bir etki alanınız varsa ve DNS A kaydı zaten bu sunucunun IP'sini işaret ediyorsa bunu kullanın.

1. Bölümü genişletmek için Kendi etki alanım'ı tıklayın
2. Tam alan adınızı girin (e.g. `survey.myorganization.org`)
3. Sertifika oluştur'a tıklayın

<!-- SCREENSHOT NEEDED: own domain input form -->

Let's Encrypt alan adınızı doğrulayacak ve bir sertifika verecektir. Bunun için önce DNS'nin doğru şekilde yönlendirilmesi gerekir; aksi halde istek başarısız olur.

---

## Seçenek 3 — Sertifikayı manuel olarak yükleyin

Özel veya dahili CA kullanan kurumsal ortamlar için. Sertifika dosyalarınızı SSH üzerinden sunucuya yerleştirecek, ardından uygulamaya alan adınızı gireceksiniz.

### Önkoşullar

- Sunucuya SSH erişimi
- Alan adınız için geçerli bir sertifika ve özel anahtar (PEM formatı)

### Adım 1 – Sunucuya SSH

```bash
ssh root@<server-ip>
```

### Adım 2 — Sertifika dosyalarınızı yerleştirin

Dizini oluşturun ve dosyalarınızı kopyalayın:

```bash
mkdir -p /etc/letsencrypt/live/<your-domain>
```

Dosyalarınızı tam olarak şu adlarla bu dizine kopyalayın:

| Dosya | Tanım |
|------|-------------|
| `fullchain.pem` | Sertifikanız + tüm ara CA sertifikaları (birleştirilmiş) |
| `privkey.pem` | Özel anahtarınız |

Örnek:

```bash
# Yerel makinenizden kopyalayın (bunu sunucuda değil, yerel olarak çalıştırın)
scp fullchain.pem root@<server-ip>:/etc/letsencrypt/live/<your-domain>/fullchain.pem
scp privkey.pem  root@<server-ip>:/etc/letsencrypt/live/<your-domain>/privkey.pem
```

Doğru izinleri ayarlayın:

```bash
chmod 644 /etc/letsencrypt/live/<your-domain>/fullchain.pem
chmod 600 /etc/letsencrypt/live/<your-domain>/privkey.pem
```

### 3. Adım — Alan adınızı uygulamaya girin

<!-- SCREENSHOT NEEDED: manual certificate form -->

1. SSL kurulum ekranında Sertifikayı manuel olarak yükle'ye tıklayın.
2. Alan adınızı girin (sertifikanın Ortak Adı veya SAN'ıyla eşleşmelidir)
3. Uygula'yı tıklayın

Sunucu, Nginx'i sertifikanızla yapılandıracak ve otomatik olarak yeniden yükleyecektir.

---

## Sonraki adım

SSL aktif hale geldikten sonra İlk Giriş'e geçin [first-login](first-login).
