---
weight: 5
title: "Bakım"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "build"
toc: true
description: "Kendi barındırdığınız rtCloud örneği için günlük bakım: yükseltme, yedekleme, geri yükleme ve yaygın sorunları giderme."
---

## Yaygın Komutlar

rtCloud konteynerlerinizi yönetmek için bu komutları düzenli olarak kullanın. Bunları `docker-compose.production.yml` dosyasını içeren dizinden çalıştırın.

```bash
# Tüm konteynerlerin durumunu ve sağlığını kontrol et
docker compose -f docker-compose.production.yml ps

# Canlı günlükleri görüntüle (tüm hizmetler)
docker compose -f docker-compose.production.yml logs -f

# Yalnızca uygulama için günlükleri görüntüle
docker compose -f docker-compose.production.yml logs -f rtcloud

# Tek bir konteyneri yeniden başlat
docker compose -f docker-compose.production.yml restart rtcloud

# Tüm hizmetleri durdur
docker compose -f docker-compose.production.yml down

# Tüm hizmetleri başlat
docker compose -f docker-compose.production.yml up -d

# Uygulama konteyneri içinde bir kabuk aç
docker compose -f docker-compose.production.yml exec rtcloud bash
```

---

## Yükseltme

rtCloud güncellemeleri yeni Docker görüntü etiketleri olarak dağıtılır. Yükseltme, en son görüntüyü çeker ve uygulama konteynerini yeniden oluşturur. Veritabanı geçişleri başlangıçta otomatik olarak çalışır.

**1. En son görüntüyü çekin:**

```bash
docker compose -f docker-compose.production.yml pull
```

**2. Uygulama konteynerini yeniden oluşturun:**

```bash
docker compose -f docker-compose.production.yml up -d
```

Docker yalnızca görüntüsü değişen konteynerleri değiştirir. MySQL konteyneri ve tüm adlandırılmış birimler etkilenmez.

### Sürümü Sabitleme

`latest` yerine belirli bir sürüme yükseltmek için `.env` dosyasındaki `RTCLOUD_IMAGE`'ı güncelleyin:

```dotenv
RTCLOUD_IMAGE=rtawebteam/rta-smartsurvey:1.2.3
```

Ardından yukarıdaki gibi `docker compose pull` ve `up -d` komutlarını çalıştırın.

### Sürüm Düşürme

Veritabanı geçişleri geri alınamayacağından, sürüm düşürme genellikle önerilmez. Sürüm düşürme gerekirse, yükseltmeden önce alınan bir veritabanı yedeğinden geri yükleyin.

---

## Yedekleme ve Geri Yükleme

### Veritabanını Yedekleme

Uygulama veritabanını bir SQL dosyasına dışa aktarmak için bu komutu çalıştırın:

```bash
docker compose -f docker-compose.production.yml exec mysql \
  mysqldump -u root -p"$(grep MYSQL_ROOT_PASSWORD .env | cut -d= -f2)" smartsurvey \
  > backup-$(date +%Y%m%d-%H%M%S).sql
```

Yedek dosyası, ana bilgisayardaki geçerli dizininize yazılır.

### Veritabanını Geri Yükleme

```bash
docker compose -f docker-compose.production.yml exec -T mysql \
  mysql -u root -p"$(grep MYSQL_ROOT_PASSWORD .env | cut -d= -f2)" smartsurvey \
  < backup-20240101-120000.sql
```

### Yüklenen Dosyaları Yedekleme

Anket gönderimleri genellikle adlandırılmış Docker birimlerinde saklanan yüklenmiş dosyaları (fotoğraflar, ses, belgeler) içerir. Bunları veritabanından ayrı olarak yedekleyin:

```bash
# Yüklemeleri yedekle
docker run --rm \
  -v rtcloud_uploads:/data \
  -v "$(pwd):/backup" \
  alpine tar czf /backup/uploads-$(date +%Y%m%d).tar.gz -C /data .

# Ses kayıtlarını yedekle
docker run --rm \
  -v rtcloud_audios:/data \
  -v "$(pwd):/backup" \
  alpine tar czf /backup/audios-$(date +%Y%m%d).tar.gz -C /data .
```

Varsayılanı değiştirdiyseniz `rtcloud_uploads` ve `rtcloud_audios`'u gerçek birim adlarınızla değiştirin (`COMPOSE_PROJECT_NAME` ile ön eklenmiş).

### Yüklenen Dosyaları Geri Yükleme

```bash
docker run --rm \
  -v rtcloud_uploads:/data \
  -v "$(pwd):/backup" \
  alpine tar xzf /backup/uploads-20240101.tar.gz -C /data
```

### Otomatik Günlük Yedeklemeler

Yedeklemeleri otomatik olarak çalıştırmak için ana bilgisayara bir cron görevi ekleyin. Root crontab'ı `crontab -e` ile düzenleyin:

```cron
# Sabah 2:00'de günlük veritabanı yedeklemesi, 30 günlük geçmiş tutun
0 2 * * * cd /opt/rtcloud && docker compose -f docker-compose.production.yml exec -T mysql \
  mysqldump -u root -p"$(grep MYSQL_ROOT_PASSWORD .env | cut -d= -f2)" smartsurvey \
  > /backups/db-$(date +\%Y\%m\%d).sql && \
  find /backups -name "db-*.sql" -mtime +30 -delete
```

---

## Sorun Giderme

### Uygulama konteyneri başlamıyor

Hata mesajları için konteyner günlüklerini kontrol edin:

```bash
docker compose -f docker-compose.production.yml logs rtcloud
```

Yaygın nedenler:
- `.env` dosyasında eksik veya geçersiz ortam değişkenleri
- MySQL henüz hazır değil (60 saniye bekleyin ve tekrar kontrol edin)
- Port çakışması — başka bir işlem `APP_PORT`'u zaten kullanıyor

### MySQL sağlıklı değil

```bash
docker compose -f docker-compose.production.yml logs mysql
```

Yaygın nedenler:
- `.env` dosyasında `MYSQL_ROOT_PASSWORD` ayarlanmamış
- Bozuk veri birimi (nadir — disk alanını `df -h` ile kontrol edin)

MySQL ilk açılışta başlatılması 30–60 saniye sürebilir. Başarısız olduğunu varsaymadan önce bekleyin ve tekrar kontrol edin.

### Port zaten kullanımda

`.env` dosyasında `APP_PORT` veya `SHINY_PORT`'u boş bir porta değiştirin, ardından konteynerleri yeniden oluşturun:

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate
```

Ana bilgisayarda bir portu neyin kullandığını bulmak için:

```bash
lsof -i :8080
```

### 400 CSRF Belirteci Doğrulanamadı

Bu hata, istek kaynağının beklenen ana bilgisayarla eşleşmediği yerel veya ters proxy ortamlarında görünür. CSRF doğrulamasını yalnızca yerel geliştirme için devre dışı bırakın:

```dotenv
CSRF_VALIDATION_ENABLED=false
```

Ardından uygulamayı yeniden başlatın:

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

> Üretimde CSRF doğrulamasını devre dışı bırakmayın. Bu hata üretimde oluşursa, ters proxy'nizin doğru `Host` ve `X-Forwarded-For` başlıklarını ilettiğinden emin olun.

### Yönetici Şifresini Unuttum

Yönetici şifresini doğrudan veritabanında sıfırlayın. MySQL konteynerine bağlanın ve şifre karmasını güncelleyin:

**Adım 1** — Yeni şifre karmasını oluşturun. `newpassword`'ü istediğiniz şifreyle değiştirin:

```bash
docker compose -f docker-compose.production.yml exec rtcloud php -r "
  \$salt = trim(shell_exec(\"mysql -h mysql -u root -p\\\"\${MYSQL_ROOT_PASSWORD}\\\" \${MYSQL_DATABASE} -se \\\"SELECT salt FROM ss_user WHERE username='admin';\\\"\"));
  echo md5(\$salt . 'newpassword') . PHP_EOL;
"
```

**Adım 2** — Veritabanındaki karmayı güncelleyin:

```bash
docker compose -f docker-compose.production.yml exec mysql \
  mysql -u root -p"${MYSQL_ROOT_PASSWORD}" smartsurvey \
  -e "UPDATE ss_user SET password='<hash_from_step_1>' WHERE username='admin';"
```

### Konteyner sürekli yeniden başlıyor

Sağlık kontrolünün başarısız olup olmadığını kontrol edin:

```bash
docker compose -f docker-compose.production.yml ps
docker inspect rtcloud-app --format '{{json .State.Health}}'
```

Uygulama sağlık kontrolü `/health` uç noktasını çağırır. Defalarca başarısız olursa, başlatma hataları için uygulama günlüklerini kontrol edin.

### Disk alanı doldu

Neyin alan tükettiğini belirleyin:

```bash
# Ana bilgisayar disk kullanımını kontrol et
df -h

# Docker disk kullanımını kontrol et (görüntüler, konteynerler, birimler)
docker system df

# Kullanılmayan görüntüleri ve durdurulan konteynerleri kaldır (güvenli çalıştırılabilir)
docker system prune
```

`docker system prune --volumes` kullanmayın, çünkü bu uygulama verilerini siler.

---

## Sağlık Kontrolleri

Her hizmetin otomatik bir sağlık kontrolü vardır. Konteyner durumu sonucu yansıtır:

| Konteyner | Kontrol Yöntemi | Başlangıç Süresi | Aralık |
|-----------|-------------|-------------|----------|
| `rtcloud-app` | HTTP GET `/health` | 90 saniye | 30 saniye |
| `rtcloud-mysql` | `mysqladmin ping` | 30 saniye | 10 saniye |
| `rtcloud-keycloak` | HTTP GET `:9000/health/live` | 120 saniye | 30 saniye |

Başarısız sağlık kontrolüne sahip konteynerler, `RESTART_POLICY` ayarına (varsayılan: `unless-stopped`) göre otomatik olarak yeniden başlatılır.
