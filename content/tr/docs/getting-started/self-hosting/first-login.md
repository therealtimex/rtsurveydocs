---
weight: 5
title: "İlk Giriş"
date: "2026-04-01T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "login"
toc: true
description: "Dağıtımdan sonra rtSurvey örneğinize ilk kez nasıl giriş yapılır."
---

> **Giriş yapmadan önce SSL yapılandırılmalıdır.** Uygulamaya HTTP üzerinden erişirseniz bir güvenlik uyarısı görürsünüz ve SSO engellenecektir. Önce [SSL Kurulumu](ssl-setup) tamamlayın.

SSL etkin olduktan sonra, tarayıcınızı HTTPS URL'nizde açın:

```
https://your-domain.com
```

---

## Giriş ekranı

<!-- SCREENSHOT NEEDED: login page over HTTPS — username/password form + SSO button -->

Giriş sayfası şunları gösterir:

- **Kullanıcı Adı** ve **Şifre** alanları
- **Giriş Yap** düğmesi
- **SSO ile Giriş Yap** düğmesi (ayırıcının altında) — SSO hesapları olan ekip üyeleri için

---

## Varsayılan yönetici kimlik bilgileri

Varsayılan kimlik bilgilerini girin ve **Giriş Yap**'a tıklayın:

| Alan | Değer |
|------|-------|
| Kullanıcı Adı | `admin` |
| Şifre | `admin` |

> **İlk girişinizden hemen sonra şifrenizi değiştirin.**

---

## Güvenlik uyarısı görürseniz

Uygulamaya HTTP üzerinden erişirseniz (SSL yapılandırılmadan önce) şunları görürsünüz:

- Giriş sayfasının üstünde sarı bir uyarı banner'ı
- **Giriş Yap**'a tıkladığınızda kimlik bilgilerinin şifresiz gönderileceğini uyaran bir modal

<!-- SCREENSHOT NEEDED: HTTP warning banner on login page -->
<!-- SCREENSHOT NEEDED: SSL warning modal with "Set up SSL" and "Continue anyway" buttons -->

HTTPS yapılandırmak için **SSL Kur**'a tıklayın veya SSL olmadan giriş yapmak için **Yine de devam et**'e tıklayın (önerilmez).

SSO girişi HTTP üzerinden tamamen engellenmiştir — **SSO ile Giriş Yap**'a tıklamak yönlendirme yerine bir bildirim gösterecektir.

---

## Giriş yaptıktan sonra

İçeri girdikten sonra panoya gelirsiniz. Buradan:

1. **Yönetici şifresini değiştirin** — hesap ayarları → şifreyi değiştir
2. **İlk projenizi oluşturun** — Projeler → Yeni Proje
3. **Form yükleyin veya oluşturun** — Formlar → XLSForm Yükle veya Form Builder'ı aç
4. **Kullanıcı ekleyin** — Kullanıcılar → Ekibiniz için hesap davet edin veya oluşturun
