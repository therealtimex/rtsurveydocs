---
weight: 2
title: "Yapılandırma Referansı"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "settings"
toc: true
description: "Kendi sunucunuzda barındırılan rtCloud dağıtımını yapılandırmak için kullanılan tüm ortam değişkenlerinin tam referansı."
---

Tüm yapılandırma, dağıtım dizininizin kökündeki `.env` dosyasındaki ortam değişkenleri aracılığıyla yapılır. Docker Compose bu dosyayı otomatik olarak okur — `--env-file` bayrağına gerek yoktur.

**Gerekli** olarak işaretlenen değişkenler, konteynerleri başlatmadan önce ayarlanmalıdır. Diğerlerinin varsayılanları vardır ve isteğe bağlıdır.

---

## Proje

Bu değişkenler, rtCloud örneğinizin kimliğini ve erişim noktasını tanımlar.

| Değişken | Varsayılan | Gerekli | Açıklama |
|----------|---------|----------|-------------|
| `PROJECT_ID` | — | **Evet** | Bu dağıtım için benzersiz tanımlayıcı. Boşluk veya özel karakter yok. Dahili adlandırma için ön ek olarak kullanılır. |
| `PROJECT_URL` | — | **Evet** | Kullanıcıların uygulamaya eriştiği alan adı veya IP adresi (örn. `rtcloud.example.com` veya `192.168.1.100`). |
| `PROJECT_TYPE` | `rtsurvey` | Hayır | Etkinleştirilecek platform varyantı. Seçenekler: `rtwork`, `rtsurvey`, `rthome`. |
| `PROJECT_PORT` | `80` | Hayır | Uygulamanın konteyner içinde dinlediği port. Ne yaptığınızı bilmiyorsanız değiştirmeyin. |
| `HTTP_PROTOCOL` | `https` | Hayır | Dahili URL'leri oluşturmak için kullanılan protokol. SSL kullanmıyorsanız `http` olarak ayarlayın. |

---

## Veritabanı

MySQL bağlantı kimlik bilgileri. Veritabanı MySQL konteyneri tarafından otomatik olarak yönetilir — yalnızca güçlü şifreler ayarlamanız gerekir.

| Değişken | Varsayılan | Gerekli | Açıklama |
|----------|---------|----------|-------------|
| `MYSQL_DATABASE` | `smartsurvey` | Hayır | Uygulama veritabanının adı. |
| `MYSQL_USER` | `smartsurvey` | Hayır | Uygulama için MySQL kullanıcısı. |
| `MYSQL_PASSWORD` | — | **Evet** | `MYSQL_USER` için şifre. Güçlü ve benzersiz bir değer kullanın. |
| `MYSQL_ROOT_PASSWORD` | — | **Evet** | MySQL root şifresi. Veritabanı başlatma ve yönetici işlemleri için gereklidir. |
| `MYSQL_HOST` | `mysql` | Hayır | MySQL ana bilgisayar adı. Harici bir veritabanına bağlanmıyorsanız varsayılanı kullanın. |
| `MYSQL_PORT` | `3306` | Hayır | MySQL portu. |

---

## Yönetici Hesabı

Yönetici hesabı, yeni bir veritabanının ilk açılışında otomatik olarak oluşturulur.

| Değişken | Varsayılan | Gerekli | Açıklama |
|----------|---------|----------|-------------|
| `ADMIN_PASSWORD` | `admin` | **Evet** | Yerleşik `admin` kullanıcısının şifresi. İlk açılıştan önce bunu ayarlayın. Veritabanı zaten mevcutsa etkisi yoktur. |

> İlk girişten sonra web arayüzündeki **Hesap Ayarları** sayfasından yönetici şifresini değiştirin.

---

## Portlar

Uygulamanın hangi ana bilgisayar portlarına bağlandığını kontrol edin.

| Değişken | Varsayılan | Açıklama |
|----------|---------|-------------|
| `APP_PORT` | `8080` | Ana web arayüzü için ana bilgisayar portu. Sunucunuzda 8080 portu zaten kullanılıyorsa bunu değiştirin. |
| `SHINY_PORT` | `3838` | Shiny analitik sunucusu için ana bilgisayar portu. |

---

## Çalışma Zamanı

| Değişken | Varsayılan | Açıklama |
|----------|---------|-------------|
| `RUN_ENV` | `prod` | Çalışma zamanı ortamı. Üretim dağıtımları için `prod`, yerel geliştirme için `dev` kullanın. |
| `RUN_MODE` | `admin` | Konteyner rolü. `admin` tam yığını (web + kuyruk + cron) çalıştırır. `worker` yalnızca arka plan işlemini çalıştırır (yatay ölçekleme için). |
| `TZ` | `Asia/Ho_Chi_Minh` | Sunucu saat dilimi. Günlük zaman damgalarını, cron zamanlamalarını ve tarih görüntüsünü etkiler. [TZ veritabanı adı](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) kullanın (örn. `UTC`, `America/New_York`, `Europe/London`). |
| `LOG_LEVEL` | `info` | Uygulama günlük ayrıntı düzeyi. Seçenekler: `debug`, `info`, `warning`, `error`. |
| `COMPOSE_PROJECT_NAME` | `rtcloud` | Tüm Docker konteyner ve birim adlarına uygulanan ön ek. Aynı ana bilgisayarda birden fazla rtCloud örneği çalıştırırken bunu değiştirin. |
| `RESTART_POLICY` | `unless-stopped` | Docker konteyner yeniden başlatma davranışı. Seçenekler: `no`, `always`, `on-failure`, `unless-stopped`. |
| `RTCLOUD_IMAGE` | `rtawebteam/rta-smartsurvey:survey-dockerize` | Kullanılacak Docker görüntüsü. Belirli bir sürümü sabitlemek için etiketi değiştirin. |
| `REQUIRE_LICENSE` | `false` | Başlangıçta lisans anahtarı doğrulamasını etkinleştirin. Lisans bilgileri için RTA ile iletişime geçin. |

---

## Güvenlik

| Değişken | Varsayılan | Açıklama |
|----------|---------|-------------|
| `CSRF_VALIDATION_ENABLED` | `true` | CSRF belirteci doğrulamasını etkinleştirin. Üretimde `true` tutun. Yalnızca `400 CSRF token could not be verified` hataları alırsanız yerel geliştirmede `false` olarak ayarlayın. |
| `GII_ENABLED` | `false` | Yii çerçevesi kod oluşturma aracını etkinleştirin. **Üretimde asla etkinleştirmeyin.** |

---

## SSO — Yerleşik Keycloak

Tam özellikli kurumsal SSO için paketlenmiş Keycloak konteynerini etkinleştirin. HTTPS'li bir alan adı gerektirir.

| Değişken | Varsayılan | Açıklama |
|----------|---------|-------------|
| `EMBED_KEYCLOAK` | `false` | Yerleşik Keycloak konteynerini başlatmak için `true` olarak ayarlayın. `embed-keycloak` Docker Compose profilini etkinleştirir. |
| `KEYCLOAK_URL` | — | Keycloak sunucusunun tam URL'si (örn. `https://rtcloud.example.com/auth`). |
| `KEYCLOAK_REALM` | — | Keycloak realm adı (örn. `rtsurvey`). |
| `KEYCLOAK_CLIENT_ID` | — | rtCloud uygulaması için Keycloak istemci kimliği. |
| `KEYCLOAK_CLIENT_SECRET` | — | Keycloak istemci sırrı. Bunu Keycloak yönetici konsolundan oluşturun. |
| `KEYCLOAK_ADMIN_USER` | `admin` | Keycloak yönetici kullanıcı adı. |
| `KEYCLOAK_ADMIN_PASSWORD` | — | Keycloak yönetici şifresi. |
| `KEYCLOAK_DB` | `keycloak` | Keycloak için veritabanı adı. İlk açılışta otomatik olarak oluşturulur. |
| `KEYCLOAK_DB_USER` | `keycloak` | Keycloak için veritabanı kullanıcısı. |
| `KEYCLOAK_DB_PASSWORD` | — | Keycloak kullanıcısı için veritabanı şifresi. |
| `KC_HOSTNAME` | — | Keycloak ön uç URL'si (örn. `https://rtcloud.example.com/auth`). |
| `KC_HOSTNAME_STRICT` | `false` | Katı ana bilgisayar adı eşleşmesini zorunlu kılın. Sabit bir alan adıyla üretimde `true` olarak ayarlayın. |

Tam kurulum kılavuzu için [SSO Kimlik Doğrulama](sso-authentication#embedded-keycloak) sayfasına bakın.

---

## SSO — Harici OIDC Sağlayıcısı

Mevcut bir OIDC uyumlu kimlik sağlayıcısına (Supabase, Auth0, Authentik, Okta vb.) bağlanın.

| Değişken | Varsayılan | Açıklama |
|----------|---------|-------------|
| `OIDC_ISSUER_URL` | — | OIDC veren keşif URL'si (örn. `https://accounts.google.com`). |
| `OIDC_CLIENT_ID` | — | Kimlik sağlayıcınızda kayıtlı istemci kimliği. |
| `OIDC_CLIENT_SECRET` | — | Kimlik sağlayıcınızdan alınan istemci sırrı. |
| `OIDC_SCOPE` | `openid profile email` | İstek için boşlukla ayrılmış OIDC kapsam listesi. |
| `OIDC_REDIRECT_URI` | — | Web uygulaması için geri arama URL'si (örn. `https://rtcloud.example.com/auth/callback`). |
| `OIDC_MOBILE_CLIENT_ID` | — | rtSurvey mobil uygulaması için ayrı istemci kimliği. |
| `OIDC_MOBILE_REDIRECT_URI` | — | Mobil uygulama geri arama URI'si (örn. `vn.rta.rtsurvey.auth://callback`). |
| `OPEN_REGISTRATION` | `false` | İlk kez OIDC aracılığıyla kimlik doğrulayan kullanıcılar için otomatik olarak rtCloud hesabı oluşturun. |
| `OIDC_AUTHORIZATION_ENDPOINT` | — | Yetkilendirme uç nokta URL'sini geçersiz kılın (keşif kullanmak için boş bırakın). |
| `OIDC_TOKEN_ENDPOINT` | — | Belirteç uç nokta URL'sini geçersiz kılın (keşif kullanmak için boş bırakın). |
| `OIDC_USERINFO_ENDPOINT` | — | Kullanıcı bilgisi uç nokta URL'sini geçersiz kılın (keşif kullanmak için boş bırakın). |

---

## SSO — Azure Active Directory

| Değişken | Açıklama |
|----------|-------------|
| `AZURE_CLIENT_ID` | Azure AD uygulama (istemci) kimliği. |
| `AZURE_TENANT_ID` | Azure AD dizin (kiracı) kimliği. |

---

## İsteğe Bağlı Entegrasyonlar

### Stata

| Değişken | Varsayılan | Açıklama |
|----------|---------|-------------|
| `STATA_ENABLED` | `false` | Veri analizi için Stata istatistiksel yazılım entegrasyonunu etkinleştirin. |
| `STATA_BIN_PATH` | `/usr/bin/stata` | Konteyner içindeki Stata ikili dosyasının mutlak yolu. |

### Elasticsearch

| Değişken | Açıklama |
|----------|-------------|
| `ES_HOST` | Elasticsearch ana bilgisayarı (örn. `http://elasticsearch:9200`). |
| `ES_PORT` | Elasticsearch portu. |

### Matomo Analitik

| Değişken | Açıklama |
|----------|-------------|
| `PIWIK_URL` | Matomo (Piwik) sunucu URL'si. |
| `PIWIK_ID` | Matomo site kimliği. |
| `PIWIK_SECRET` | Matomo kimlik doğrulama belirteci. |

### OpenCPU (R Hesaplama)

| Değişken | Açıklama |
|----------|-------------|
| `OCPU_HOST` | R tabanlı istatistiksel hesaplama için OpenCPU sunucu URL'si. |

### RtBox Entegrasyonu

| Değişken | Açıklama |
|----------|-------------|
| `RTBOX_HOST` | RtBox hizmet ana bilgisayar URL'si. |
| `RTBOX_USER_API` | RtBox kullanıcı API anahtarı. |
| `RTBOX_BASIC_AUTH` | RtBox için temel kimlik doğrulama kimlik bilgileri. |

### Matrix Mesajlaşma

| Değişken | Açıklama |
|----------|-------------|
| `MATRIX_HOMESERVER_HOST` | Matrix ana sunucu. |
| `MATRIX_HOMESERVER_PORT` | Matrix ana sunucu portu. |

---

## Veri Birimleri

Tüm uygulama verileri adlandırılmış Docker birimlerinde saklanır. Birimler ilk başlatmada otomatik olarak oluşturulur ve konteyner yeniden başlatmaları ile güncellemeler arasında kalıcıdır.

| Birim | Bağlama Noktası | İçerik |
|--------|-------------|----------|
| `rtcloud_mysql_data` | `/var/lib/mysql` | MySQL veritabanı dosyaları |
| `rtcloud_uploads` | `…/uploads` | Anket katılımcıları tarafından yüklenen dosyalar |
| `rtcloud_audios` | `…/audios` | Ses kayıtları |
| `rtcloud_downloads` | `…/downloads` | Oluşturulan dışa aktarma dosyaları |
| `rtcloud_gallery` | `…/gallery` | Galeri görüntüleri |
| `rtcloud_voicemail` | `…/voicemail` | Sesli mesaj kayıtları |
| `rtcloud_analytics` | `…/analytics` | Analitik verileri |
| `rtcloud_aggregate` | `…/aggregate` | Toplu anket sonuçları |
| `rtcloud_converter` | `…/converter` | Veri dönüştürme çıktıları |
| `rtcloud_shiny_data` | `/srv/shiny-server/smartsurvey` | Shiny sunucusu R betikleri |
| `rtcloud_shiny_logs` | `/var/log/shiny-server` | Shiny sunucusu günlükleri |
| `rtcloud_assets` | `…/assets` | Web varlıkları (CSS, JS) |
| `rtcloud_runtime` | `…/protected/runtime` | Uygulama çalışma zamanı önbelleği |
| `rtcloud_cache` | `…/cache` | Uygulama önbelleği |
| `rtcloud_tmp` | `…/tmp` | Geçici dosyalar |

Birim adları `COMPOSE_PROJECT_NAME` değeriyle (varsayılan: `rtcloud`) ön eklenmiştir.

Dağıtımınız için tüm birimleri listeleyin:

```bash
docker volume ls | grep rtcloud
```
