---
title: "Hesaplama"
description: ""
icon: "calculate"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 235
---

XLSForm'larda ve rtSurvey'de hesaplama soruları, formdaki diğer alanlara veya değerlere dayalı hesaplamalar yapmak için kullanılır. Bu sorular kullanıcıya görüntülenmez, bunun yerine arka planda çalışarak sonuçlarını daha sonra kullanılmak veya gönderilmek üzere saklar.

## Sözdizimi

XLSForm'da bir hesaplama sorusu şu şekilde tanımlanır:

| type      | name     | label | calculation |
|-----------|----------|-------|-------------|
| calculate | calc_q1  |       | ${q1} + ${q2} |

- **type**: Bu soru türü için her zaman "calculate".
- **name**: Hesaplama sorusu için benzersiz bir ad.
- **label**: Hesaplama soruları kullanıcılara görüntülenmediğinden genellikle boş bırakılır.
- **calculation**: Değerlendirilecek formül.

## Kullanım Alanları

Hesaplama soruları yaygın olarak şunlar için kullanılır:

1. Aritmetik işlemler yapma
2. Dizeleri birleştirme
3. Karmaşık mantık veya fonksiyonlar uygulama
4. Daha sonra kullanılmak üzere ara sonuçları saklama

## Örnekler

### Temel Aritmetik

```
| type      | name     | calculation |
|-----------|----------|-------------|
| calculate | total    | ${price} * ${quantity} |
```

### Dize Birleştirme

```
| type      | name     | calculation |
|-----------|----------|-------------|
| calculate | full_name| concat(${first_name}, ' ', ${last_name}) |
```

### Fonksiyon Kullanımı

```
| type      | name     | calculation |
|-----------|----------|-------------|
| calculate | age      | int((today() - ${date_of_birth}) / 365.25) |
```

## rtSurvey'de Gelişmiş Kullanım

### pulldata() Fonksiyonu

rtSurvey, hesaplama alanlarında `pulldata()` fonksiyonunu destekler ve harici CSV dosyalarından veri almanıza olanak tanır:

```
| type      | name     | calculation |
|-----------|----------|-------------|
| calculate | city     | pulldata('cities', 'city_name', 'zip_code', ${zip_input}) |
```

#### Sözdizimi

pulldata() için temel sözdizimi:

```
pulldata('csv_dosyaadi', 'dondurilecek_sutun', 'anahtar_sutun', ${eslesen_deger})
```

- 'csv_dosyaadi': CSV dosyasının adı (.csv uzantısı olmadan)
- 'dondurilecek_sutun': Almak istediğiniz veriyi içeren sütun adı
- 'anahtar_sutun': Karşılaştırılacak sütun adı
- ${eslesen_deger}: Anahtar sütunda aranacak değer (genellikle formdaki bir değişken)

#### Önemli Notlar

1. CSV dosyası, anketi dağıtırken XLSForm'unuzla birlikte yüklenmelidir.
2. CSV dosyanızda ayırıcı olarak virgül kullanın, noktalı virgül değil.
3. CSV'nin veri alanlarındaki virgüllerden kaçının, bunlar ayrıştırma sorunlarına neden olabilir.
4. pulldata() yalnızca 1-1 ilişkileri destekler. Birden fazla eşleşme bulunursa yalnızca ilkini döndürür.
5. Çekilebilecek metin uzunluğunda sınırlamalar olabilir (yaklaşık 76 karakter).
6. Girişleri CSV verilerine göre doğrulamak için kısıtlamalarda pulldata() kullanabilirsiniz.

### Koşullu Hesaplamalar

Koşullu hesaplamalar için if() ifadelerini kullanabilirsiniz:

```
| type      | name     | calculation |
|-----------|----------|-------------|
| calculate | discount | if(${total} > 1000, ${total} * 0.1, 0) |
```

## En İyi Uygulamalar

1. Form okunabilirliğini artırmak için hesaplama alanlarına anlamlı adlar verin.
2. Tek bir alanda aşırı karmaşık hesaplamalardan kaçının; gerekirse bunları parçalara ayırın.
3. Özellikle karmaşık formüller veya harici veriler kullanırken hesaplamalarınızı kapsamlı şekilde test edin.
4. Hesaplama alanlarının form her değerlendirildiğinde çalıştığını unutmayın; bu çok karmaşık veya çok sayıda hesaplama için performansı etkileyebilir.
5. pulldata() kullanırken CSV dosyalarınızın doğru biçimlendirildiğinden emin olun ve belirli veri ve form yapınızla kapsamlı testler yapın.

## Sınırlamalar

- Hesaplama alanları kullanıcılar tarafından doğrudan düzenlenemez.
- Bir hesaplama alanının sonucu, bir görüntü alanında başvurulmadığı veya form mantığında kullanılmadığı sürece hemen görünmez.
