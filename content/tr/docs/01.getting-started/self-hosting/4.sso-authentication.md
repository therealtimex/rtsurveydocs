---
weight: 4
title: "SSO Kimlik Doğrulama"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "lock"
toc: true
description: "Yerleşik Keycloak, harici bir OIDC sağlayıcısı veya Azure Active Directory kullanarak kendi barındırdığınız rtCloud için Tek Oturum Açma'yı yapılandırın."
---

rtCloud, Tek Oturum Açma (SSO) için üç yaklaşımı destekler:

| Seçenek | En İyi Kullanım |
|--------|----------|
| [Yerleşik Keycloak](#embedded-keycloak) | rtCloud ile paketlenmiş tamamen kendi kendine yeten bir SSO sunucusu isteyen kuruluşlar |
| [Harici OIDC Sağlayıcısı](#external-oidc-provider) | Halihazırda bir kimlik sağlayıcısı çalıştıran kuruluşlar (Auth0, Authentik, Okta, Supabase vb.) |
| [Azure Active Directory](#azure-active-directory) | Microsoft 365 veya Azure AD kullanan kuruluşlar |

SSO yapılandırılmadan kullanıcılar, yönetici paneli aracılığıyla yönetilen yerel rtCloud hesaplarıyla giriş yapar.

---

## Yerleşik Keycloak {#embedded-keycloak}

Dağıtım, rtCloud'un yanında çalışan isteğe bağlı bir Keycloak konteyneri içermektedir. Keycloak, bir rtSurvey realm'ı ile önceden yapılandırılmış ve kullanıma hazır durumdadır.

### Gereksinimler

- HTTPS'li bir alan adı (Keycloak, üretimde HTTPS gerektirir)
- Sunucuda en az 4 GB RAM (Keycloak ~512 MB bellek ekler)

### Kurulum

**1. `.env` dosyasında ortam değişkenlerini yapılandırın:**

```dotenv
# Yerleşik Keycloak konteynerini etkinleştir
EMBED_KEYCLOAK=true

# Keycloak URL'leri — gerçek alan adınızı kullanın
KEYCLOAK_URL=https://rtcloud.example.com/auth
KC_HOSTNAME=https://rtcloud.example.com/auth
KC_HOSTNAME_STRICT=false

# Realm ve istemci ayarları (içe aktarılan realm JSON ile eşleşmeli)
KEYCLOAK_REALM=rtsurvey
KEYCLOAK_CLIENT_ID=rtsurvey-app
KEYCLOAK_CLIENT_SECRET=your-client-secret-here

# Keycloak yönetici kimlik bilgileri
KEYCLOAK_ADMIN_USER=admin
KEYCLOAK_ADMIN_PASSWORD=change_me_keycloak_admin_password

# Keycloak veritabanı (otomatik olarak oluşturulur)
KEYCLOAK_DB=keycloak
KEYCLOAK_DB_USER=keycloak
KEYCLOAK_DB_PASSWORD=change_me_keycloak_db_password

# Keycloak'ın dinlediği port (ana bilgisayar tarafı, Nginx tarafından proxy'lenir)
KEYCLOAK_PORT=8091
```

**2. Yerleşik Keycloak profiliyle başlatın:**

```bash
docker compose -f docker-compose.production.yml --profile embed-keycloak up -d
```

**3. Keycloak'ın sağlıklı olduğunu doğrulayın:**

```bash
docker compose -f docker-compose.production.yml ps
```

`rtcloud-keycloak` konteyneri 2–3 dakika sonra `Up (healthy)` göstermelidir.

**4. Keycloak yönetici konsoluna erişin:**

```
https://rtcloud.example.com/auth/admin
```

`KEYCLOAK_ADMIN_USER` ve `KEYCLOAK_ADMIN_PASSWORD` ile giriş yapın.

### Önceden Yapılandırılmış Olanlar

Yerleşik Keycloak, şunları içeren önceden içe aktarılmış bir `rtsurvey` realm'ı ile başlar:

- Web uygulaması için istemci yapılandırması
- Varsayılan kullanıcı rolleri (`admin`, `project_manager`, `enumerator`, `analyst`)
- rtSurvey için optimize edilmiş oturum ve belirteç ayarları

Keycloak yönetici konsolunda doğrudan kullanıcı ekleyebilir veya Keycloak'ı bir üst kimlik sağlayıcısına (LDAP, SAML) bağlayabilirsiniz.

### Nginx Yönlendirme

Bulut dağıtım betikleri kullanılırken Nginx her iki hizmeti proxy olarak yapılandırır:

| Yol | Arka Uç |
|------|---------|
| `/` | `127.0.0.1:8080` üzerindeki rtCloud uygulaması |
| `/auth/` | `127.0.0.1:8090` üzerindeki Keycloak |

---

## Harici OIDC Sağlayıcısı {#external-oidc-provider}

rtCloud'u herhangi bir OpenID Connect uyumlu kimlik sağlayıcısına bağlayın. Bu yaklaşım Keycloak konteynerini gerektirmez.

### Desteklenen Sağlayıcılar

OIDC uyumlu herhangi bir sağlayıcı çalışır, bunlar dahil:
- Authentik
- Auth0
- Okta
- Keycloak (harici örnek)
- Supabase
- Google (Google Workspace kuruluşları için)
- GitHub (OIDC uzantısıyla OAuth uygulamaları aracılığıyla)

### Kurulum

**1. rtCloud'u kimlik sağlayıcınıza OIDC istemcisi olarak kaydedin.**

İhtiyacınız olacaklar:
- Bir **istemci kimliği** ve **istemci sırrı**
- **Yeniden yönlendirme URI'sini** kaydetmek için: `https://rtcloud.example.com/auth/callback`
- Mobil uygulama desteği için ayrıca kaydedin: `vn.rta.rtsurvey.auth://callback`

**2. `.env` dosyasında ortam değişkenlerini yapılandırın:**

```dotenv
# OIDC keşif URL'si (sağlayıcıya özgü — IdP belgelerinizi kontrol edin)
OIDC_ISSUER_URL=https://your-identity-provider.com

# Kimlik sağlayıcınızdan istemci kimlik bilgileri
OIDC_CLIENT_ID=rtcloud-app
OIDC_CLIENT_SECRET=your-client-secret-here

# İstenecek kapsamlar (openid, profile ve email genellikle yeterlidir)
OIDC_SCOPE=openid profile email

# Kimlik sağlayıcınıza kayıtlı yeniden yönlendirme URI'si
OIDC_REDIRECT_URI=https://rtcloud.example.com/auth/callback

# İsteğe bağlı: ayrı mobil uygulama istemcisi
OIDC_MOBILE_CLIENT_ID=rtcloud-mobile
OIDC_MOBILE_REDIRECT_URI=vn.rta.rtsurvey.auth://callback

# Yeni OIDC kullanıcıları için otomatik rtCloud hesabı oluşturmak için true olarak ayarlayın
OPEN_REGISTRATION=false
```

**3. Değişiklikleri uygulamak için uygulama konteynerini yeniden başlatın:**

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

### Kullanıcıları Otomatik Sağlama

`OPEN_REGISTRATION=true` olduğunda rtCloud, bir kullanıcı ilk kez OIDC aracılığıyla giriş yaptığında otomatik olarak yerel bir hesap oluşturur. Hesap, ID belirtecinden kullanıcının adı ve e-postasıyla doldurulur.

`OPEN_REGISTRATION=false` (varsayılan) olduğunda, bir rtCloud yöneticisinin önce kullanıcı hesabını oluşturması gerekir ve OIDC kimliği ilk girişte bağlanır.

### Özel Uç Noktalar

Sağlayıcınız OIDC keşifini (`.well-known/openid-configuration`) desteklemiyorsa, uç noktaları manuel olarak ayarlayabilirsiniz:

```dotenv
OIDC_AUTHORIZATION_ENDPOINT=https://your-provider.com/oauth2/authorize
OIDC_TOKEN_ENDPOINT=https://your-provider.com/oauth2/token
OIDC_USERINFO_ENDPOINT=https://your-provider.com/oauth2/userinfo
```

---

## Azure Active Directory {#azure-active-directory}

rtCloud'u kuruluşunuzun Microsoft Azure AD kiracısıyla entegre edin.

### Kurulum

**1. [Azure Portal](https://portal.azure.com)'da yeni bir uygulama kaydedin:**

   - **Azure Active Directory** → **Uygulama kayıtları** → **Yeni kayıt**'a gidin
   - Ad: `rtCloud`
   - Yeniden yönlendirme URI: `https://rtcloud.example.com/auth/callback` (Web türü)
   - Oluşturulduktan sonra **Uygulama (istemci) kimliği** ve **Dizin (kiracı) kimliği**'ni not edin
   - **Sertifikalar ve sırlar** altında yeni bir istemci sırrı oluşturun

**2. `.env` dosyasında ortam değişkenlerini yapılandırın:**

```dotenv
AZURE_CLIENT_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
AZURE_TENANT_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

**3. Uygulama konteynerini yeniden başlatın:**

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

Azure AD kiracınızdaki kullanıcılar artık Microsoft kimlik bilgilerini kullanarak rtCloud'a giriş yapabilir.

---

## SSO'yu Devre Dışı Bırakma

Yerel kimlik doğrulamaya geri dönmek için `.env` dosyasından tüm SSO ile ilgili değişkenleri kaldırın veya yorum satırına alın, ardından uygulama konteynerini yeniden başlatın:

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

Yerleşik Keycloak kullanıyorsanız, `--profile embed-keycloak` bayrağını atlayarak ve profil olmadan `docker compose down` ardından `up -d` çalıştırarak durdurun.
