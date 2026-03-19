---
weight: 115
title: "Kendi Sunucunuzda Barındırma"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "dns"
toc: true
description: "Docker kullanarak kendi rtCloud örneğinizi dağıtın ve yönetin. Verileriniz, altyapınız ve yapılandırmanız üzerinde tam kontrol."
---

Docker Compose kullanarak rtCloud'u kendi altyapınızda çalıştırın. Kendi sunucunuzda barındırma, veri ikamet gereksinimleri, hava boşluklu ağlar veya özel altyapı ihtiyaçları olan kuruluşlar için ideal olan verileriniz, ağınız ve dağıtım ortamınız üzerinde tam sahiplik sağlar.

## rtCloud Kendi Sunucusunda Barındırma Nedir?

rtCloud Kendi Sunucusunda Barındırma, herhangi bir Linux sunucusunda çalıştırabileceğiniz taşınabilir bir konteyner yığınına tüm rtCloud platformunu paketleyen resmi bir Docker görüntüsüdür. Yığın şunları içermektedir:

| Hizmet | Açıklama |
|---------|-------------|
| **rtCloud Uygulaması** | Yerleşik arka plan kuyruğu (Beanstalkd), analitik sunucusu (Shiny) ve zamanlanmış görevleri olan Apache 2.4 + PHP 7.4 web uygulaması |
| **MySQL 8.0** | Tüm uygulama ve anket verileri için ilişkisel veritabanı |
| **Keycloak** *(isteğe bağlı)* | Kurumsal kimlik yönetimi için yerleşik Tek Oturum Açma sunucusu |

## Kendi Sunucunuzda Barındırmayı Ne Zaman Seçmeli

Kendi sunucunuzda barındırma şu durumlarda doğru seçimdir:

- **Veri egemenliği** gerektiğinde — tüm veriler kendi altyapınızda kalır
- Harici bulut erişimi olmayan **hava boşluklu veya kısıtlı ağlarda** faaliyet gösterildiğinde
- Yerel depolamayı zorunlu kılan **uyumluluk gereksinimleri** (GDPR, HIPAA, devlet veri politikaları) olduğunda
- **Dahili kimlik sağlayıcısıyla** (Active Directory, LDAP, SAML) entegrasyon gerektiğinde
- **Kaynakları özelleştirmek** istediğinizde — kendi şartlarınızda CPU, RAM ve depolama tahsisi

## Bu Bölümde

| Sayfa | Açıklama |
|------|-------------|
| [Hızlı Başlangıç](quick-start) | rtCloud'u 10 dakikadan kısa sürede bir sunucuda çalıştırın |
| [Yapılandırma Referansı](configuration) | Tüm ortam değişkenlerinin ve varsayılanlarının tam listesi |
| [Bulut Dağıtımı](cloud-deployment) | DigitalOcean, AWS, GCP ve Linode için tek tıklamalı otomatik betikler |
| [SSO Kimlik Doğrulama](sso-authentication) | Keycloak, harici OIDC veya Azure AD'yi yapılandırın |
| [Bakım](maintenance) | Örneğinizi yükseltin, yedekleyin, geri yükleyin ve sorun giderin |

## Mimari Genel Bakış

Dağıtım, dahili bir ağda bağlı bir dizi Docker konteyneri olarak çalışır:

```
┌────────────────────────────────────────┐
│            rtcloud-app                 │
│  Apache 2.4 (port 80)                  │
│  PHP 7.4 application                   │
│  Beanstalkd queue (internal)           │
│  Shiny Server (port 3838)              │
│  Cron scheduler                        │
└─────────────────┬──────────────────────┘
                  │ rtcloud-net (bridge)
┌─────────────────▼──────────────────────┐
│            rtcloud-mysql               │
│  MySQL 8.0 (port 3306, internal only)  │
└────────────────────────────────────────┘
```

SSO etkinleştirildiğinde, üçüncü bir konteyner yanında çalışır:

```
┌─────────────────────────────────────────┐
│            rtcloud-keycloak             │
│  Keycloak (port 8080, internal only)    │
│  Admin UI (port 9000, internal only)    │
└─────────────────────────────────────────┘
```

Tüm konteynerler izole bir Docker köprü ağı üzerinden iletişim kurar. Yalnızca web uygulama portu ve (isteğe bağlı olarak) Shiny analitik portu ana bilgisayara açıktır.
