---
title: "Varsayılan"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 287
---

rtSurvey'deki varsayılan değerler, katılımcı bir soruyla ilk karşılaştığında soruları önceden yanıtlarla doldurmanıza olanak tanır. Bu özellik, yaygın olarak seçilen veya beklenen girişin örnekleri olarak hizmet eden başlangıç değerleri sağlayarak anket verimliliğini ve veri kalitesini önemli ölçüde artırabilir.

## Temel Kullanım

Varsayılan bir değer ayarlamak için XLSForm'unuzdaki `default` sütununu kullanın:

```
| type    | name        | label                         | default    |
|---------|-------------|-------------------------------|------------|
| date    | survey_date | Anket tarihi                   | 2024-07-04 |
| decimal | weight      | Katılımcının ağırlığı? (kg)    | 51.3       |
```

Bu örnekte, anket tarihi 4 Temmuz 2024 ile önceden doldurulacak ve ağırlık alanı 51.3 kg ile başlayacaktır.

## Dinamik Varsayılanlar

rtSurvey, fonksiyonları kullanarak dinamik varsayılan değerleri destekler:

```
| type | name | label                              | default  |
|------|------|------------------------------------| ---------|
| date | d    | Olayın gerçekleştiği tarihi girin? | today()  |
```

Burada `today()` fonksiyonu varsayılanı otomatik olarak geçerli tarihe ayarlar.

## rtSurvey'e Özgü Özellikler

### Bağlama Duyarlı Varsayılanlar

rtSurvey, varsayılan işlevselliği bağlama duyarlı varsayılanlarla genişletir:

```
| type    | name     | label           | default            |
|---------|----------|-----------------|---------------------|
| text    | location | Geçerli konum   | ${current_location} |
```

Bu, cihazın GPS'ine dayalı konumu önceden doldurmak için rtSurvey'in `${current_location}` değişkenini kullanır.

### Basamaklı Varsayılanlar

rtSurvey, önceki cevaplara dayalı varsayıanlara izin verir:

```
| type    | name     | label           | default         |
|---------|----------|-----------------|-----------------|
| text    | city     | Şehir            |                 |
| text    | district | İlçe             | ${city}-district|
```

Burada ilçe alanı, girilen şehre göre önceden doldurulur.

### Tekrarlardaki Varsayılan

Tekrar grubu içindeki sorular için, tekrar eklendiğinde varsayılan hesaplanır:

```
| type         | name      | label        | default                |
|--------------|-----------|--------------|------------------------|
| begin repeat | visits    | Klinik Ziyaretleri|                        |
| date         | visit_date| Ziyaret Tarihi   | ${previous_visit_date} |
| end repeat   |           |              |                        |
```

Bu, varsayılan ziyaret tarihini önceki ziyaretin tarihine ayarlar.

## Varsayılanları Kullanmak için En İyi Uygulamalar

1. **Dikkatli Kullanın**: Yalnızca verimliliği veya veri kalitesini önemli ölçüde artırdıkları yerde varsayılanları kullanın.
2. **Doğruluğu Sağlayın**: Statik varsayılan değerleri düzenli olarak gözden geçirin ve güncelleyin.
3. **Kapsamlı Test Edin**: Özellikle dinamik veya hesaplanmış varsayılanları kullanırken.
4. **Kullanıcı Deneyimini Göz Önünde Bulundurun**: Varsayılanların katılımcıları yanıltmamasını veya yanlılık oluşturmamasını sağlayın.
5. **Açıkça Belgeleyin**: Tüm ekip üyelerinin varsayılan değerlerin arkasındaki gerekçeyi anladığından emin olun.

## Gelişmiş Varsayılan Teknikler

### Rastgele Varsayılanlar

rtSurvey, belirli soru türleri için rastgele varsayılanları destekler:

```
| type              | name    | label        | default           |
|-------------------|---------|--------------|-------------------|
| select_one options| choice  | Birini seçin:  | random(options)   |
```

Bu, 'options' listesinden rastgele bir varsayılan seçenek seçer.

### Koşullu Varsayılanlar

Koşullu varsayılanlar ayarlamak için ilgililik kullanın:

```
| type    | name     | label    | default | relevant        |
|---------|----------|----------|---------|-----------------|
| text    | other    | Belirtin  | N/A     | ${q1} = 'other' |
```

Burada, 'N/A' yalnızca önceki soruda 'other' seçildiğinde varsayılandır.

## Veri Yönetimi Hususları

- Varsayılan değerler, genellikle varsayılan değerler olduklarını gösteren bir bayrakla birlikte veri dışa aktarmalarına dahil edilir.
- rtSurvey'in denetim izi özelliği, varsayılan değerlerin katılımcılar tarafından ne zaman değiştirildiğini izler.

## Mobil Uygulama Davranışı

- rtSurvey mobil uygulaması, dinamik ve bağlama duyarlı varsayılanlar dahil tüm varsayılan işlevleri destekler.
- Çevrimdışı mod, gerçek zamanlı verilere dayanan bazı dinamik varsayılanları etkileyebilir.

## Bilinen Sınırlamalar

- Karmaşık hesaplanmış varsayılanlar, özellikle düşük özellikli cihazlarda form yükleme süresini etkileyebilir.
- Bazı dinamik varsayılanlar önizleme modunda beklendiği gibi çalışmayabilir.

## Varsayılan Değerlerde Sorun Giderme

1. **Varsayılan Görünmüyor**: Varsayılan ifadede sözdizimi hatalarını kontrol edin.
2. **Beklenmedik Değerler**: Hesaplama mantığını doğrulayın ve çeşitli senaryolarla test edin.
3. **Performans Sorunları**: Karmaşık varsayılan hesaplamalarını optimize edin veya alternatif yaklaşımları değerlendirin.
