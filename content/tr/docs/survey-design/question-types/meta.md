---
title: "Meta"
description: "Meta soru türleri, yanıtlayıcıdan herhangi bir giriş olmaksızın cihaz, sayımcı ve zamanlama bilgilerini otomatik olarak yakalar."
icon: "info"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 237
---

Meta soru türleri **otomatik olarak doldurulan** özel alanlardır — yanıtlayıcı bunları hiç görmez. Gönderim hakkında bağlam yakalarlar: ne zaman toplandığı, hangi cihazın kullanıldığı ve kimin topladığı. Bunları `survey` çalışma sayfasına diğer soru türleri gibi ekleyin; yalnızca ekranda görünmezler.

## Temel XLSForm Tanımı

| type | name | label |
|------|------|-------|
| start | start | |
| end | end | |
| deviceid | deviceid | |

Meta alanlar hiçbir zaman görüntülenmediğinden etiketler isteğe bağlıdır.

---

## Zamanlama meta alanları

### `start`

Formun **açıldığı tarih ve saati** kaydeder. ISO 8601 biçiminde saklanır (`YYYY-MM-DDTHH:MM:SS.sss+HH:MM`).

```
type    | name  | label
start   | start |
```

### `end`

Formun **gönderildiği tarih ve saati** kaydeder. `start` ile birlikte, formu doldurmak için harcanan süreyi hesaplayabilirsiniz:

```
type      | name          | calculation
calculate | duration_min  | (decimal-date-time(${end}) - decimal-date-time(${start})) * 1440
```

### `today`

**Geçerli tarihi** kaydeder (zaman bileşeni yok). `YYYY-MM-DD` olarak saklanır. Tam zaman damgası olmaksızın yalnızca tarihe ihtiyaç duyduğunuzda kullanışlıdır.

```
type  | name  | label
today | today |
```

---

## Cihaz meta alanları

### `deviceid`

Veri toplama için kullanılan **cihazın benzersiz tanımlayıcısını** kaydeder. Android'de bu genellikle IMEI veya Android ID'dir. Her formu hangi cihazın gönderdiğini takip etmek ve aynı cihazdan yinelenen gönderileri tespit etmek için kullanışlıdır.

```
type      | name     | label
deviceid  | deviceid |
```

### `devicephonenum`

Cihazdaki **SIM kartın telefon numarasını** kaydeder (varsa). Cihazda SIM kart yoksa veya numara SIM'de saklanmıyorsa boş olabilir.

```
type           | name          | label
devicephonenum | devicephonenum |
```

### `simserial`

**SIM kartın seri numarasını** (ICCID) kaydeder. Hangi SIM/operatörün kullanıldığını belirlemek için kullanışlıdır.

```
type      | name      | label
simserial | simserial |
```

### `subscriberid`

**IMSI (Uluslararası Mobil Abone Kimliği)** — SIM karttaki benzersiz abone tanımlayıcısını kaydeder.

```
type         | name        | label
subscriberid | subscriberid |
```

---

## Sayımcı meta alanları

### `username`

**Oturum açmış sayımcının kullanıcı adını** (rtSurvey uygulamasında kullanılan hesap) kaydeder. Her gönderimi kimin topladığını takip etmenin en güvenilir yoludur.

```
type     | name     | label
username | username |
```

### `email`

**Oturum açmış sayımcının e-posta adresini** kaydeder.

```
type  | name  | label
email | email |
```

### `phonenumber`

**Sayımcının hesabıyla ilişkili telefon numarasını** kaydeder (yapılandırılmışsa).

```
type        | name       | label
phonenumber | phonenumber |
```

---

## Denetim günlüğü

### `audit`

`audit` meta alanı **ayrıntılı denetim günlüğünü** etkinleştirir — sayımcının ziyaret ettiği her sorunun, her birinde harcanan sürenin ve (isteğe bağlı olarak) her adımdaki GPS konumunun zaman damgalı günlüğünü kaydeder. Denetim günlüğü, her gönderinin yanına ayrı bir `audit.csv` dosyası olarak kaydedilir.

```
type  | name  | parameters
audit | audit | location-priority=balanced location-min-interval=30 location-max-age=60
```

#### Denetim parametreleri

| Parametre | Açıklama |
|-----------|-------------|
| `location-priority` | GPS doğruluk düzeyi: `no-gps`, `low-power`, `balanced`, `high-accuracy` |
| `location-min-interval` | Konum yakalamaları arasındaki minimum saniye |
| `location-max-age` | Kabul edilecek önbelleğe alınmış bir konumun maksimum yaşı (saniye) |

Denetim günlüğü şunları yakalar:
- Soru adı ve olay türü (`question`, `form.start`, `form.exit`, `form.save`, `form.finalize`)
- Her olay için başlangıç ve bitiş zaman damgaları
- GPS koordinatları (`location-priority` ayarlıysa)

{{% alert icon=" " context="warning" %}}
`audit` alanı gönderim başına ayrı bir dosya oluşturur. Veri ardışık düzeninizin hem ana form verilerini hem de denetim CSV'sini işlediğinden emin olun.
{{% /alert %}}

---

## Tam örnek

Tipik bir hane anketi tüm zamanlama ve sayımcı meta alanlarını içerebilir:

| type | name | label |
|------|------|-------|
| start | start | |
| end | end | |
| today | today | |
| deviceid | deviceid | |
| username | username | |
| email | email | |
| audit | audit | |
| text | household_id | Hane Kimliği |
| ... | ... | ... |

---

## En İyi Uygulamalar

1. Her zaman `start` ve `end` ekleyin — bunlar ücretsiz, otomatik ve kalite izleme için paha biçilmezdir.
2. Sayımcıları takip etmek için her zaman `username` ekleyin.
3. Yinelenen gönderileri tespit etmek veya saha cihazlarını takip etmek istediğinizde `deviceid` ekleyin.
4. Her soruyu sayımcının gerçekten ziyaret ettiğini doğrulamanız gereken yüksek hesap verebilirlik anketlerinde `audit` kullanın.
5. SIM ile ilgili alanlar (`simserial`, `subscriberid`, `devicephonenum`) yalnızca aktif SIM kartlı Android cihazlarda güvenilirdir — yalnızca tablet dağıtımları için bunları atlayın.

---

## Sınırlamalar

- Tüm meta alanlar **salt okunur** — diğer hesaplamalar tarafından başvurulamaz veya değiştirilemez.
- `username` ve `email`, sayımcının oturum açmış olmasını gerektirir; anonim gönderiler için boş olacaktır.
- SIM/telefon meta alanları, izin kısıtlamaları nedeniyle yalnızca Wi-Fi tabletlerde ve bazı Android sürümlerinde boş değer döndürebilir.
