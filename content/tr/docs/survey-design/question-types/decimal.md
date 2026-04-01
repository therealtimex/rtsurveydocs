---
title: "Ondalık"
description: "Ondalık sorular, anketinizde kesirli kısımlar içeren sayısal girişlere olanak tanır."
icon: "calculate"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 223
---

XLSForm'larda ve rtSurvey'de ondalık soru türü, kesirli kısımlar içerebilen sayısal yanıtları toplamak için kullanılır. Bu soru türü, ölçümler, fiyatlar veya yüzdeler gibi hassas sayısal verileri toplamak için gereklidir.

## Temel XLSForm Tanımı

| type    | name   | label                    |
|---------|--------|--------------------------|
| decimal | weight | Ağırlığınızı kg cinsinden girin  |

Temel ondalık soru türü hakkında daha fazla ayrıntı için [XLSForm spesifikasyonuna](https://xlsform.org/en/#question-types) bakın.

## Kullanım Alanları

Ondalık sorular yaygın olarak şunlar için kullanılır:

1. Ölçümler (örn. ağırlık, yükseklik, mesafe)
2. Finansal veriler (örn. fiyatlar, maaşlar)
3. Yüzdeler
4. Bilimsel veri toplama
5. Tam sayıların ötesinde hassasiyet gerektiren sayısal veriler

## En İyi Uygulamalar

1. Beklenen girişi ve ölçüm birimini belirtmek için açık ve kısa etiketler kullanın.
2. Gerçekçi olmayan veya hatalı girişleri önlemek için aralık kısıtlamaları uygulayın.
3. Örnekler sağlamak veya beklenen biçimi açıklamak için ipucu metni kullanmayı düşünün.
4. Hassasiyet önemliyse etiket veya ipucunda istenen ondalık basamak sayısını belirtin.

## Kısıtlamalar ve Doğrulama

Girilen değerin belirli bir aralıkta olmasını sağlamak için kısıtlamalar ekleyebilirsiniz:

| type    | name   | label                    | constraint        | constraint_message                    |
|---------|--------|--------------------------|-------------------|---------------------------------------|
| decimal | height | Boyunuzu metre cinsinden girin | .>0 and .<=3    | Boy 0 ile 3 metre arasında olmalıdır |

## Örnek Kullanım

Bir sağlık anketinde ondalık soruları nasıl kullanabileceğinize dair bir örnek:

| type    | name           | label                                     | constraint | constraint_message                |
|---------|----------------|-------------------------------------------|------------|-----------------------------------|
| decimal | weight         | Ağırlığınızı kg cinsinden girin           | .>0 and .<=500 | Ağırlık 0 ile 500 kg arasında olmalıdır |
| decimal | height         | Boyunuzu metre cinsinden girin            | .>0 and .<=3 | Boy 0 ile 3 metre arasında olmalıdır |
| decimal | body_temp      | Vücut ısınızı Celsius cinsinden girin     | .>=35 and .<=42 | Sıcaklık 35°C ile 42°C arasında olmalıdır |
| calculate | bmi          |                                           |            |                                   |

BMI için hesaplama satırında şunu kullanabilirsiniz:

```
calculation | ${weight} / (${height} * ${height})
```

Bu, girilen ağırlık ve boyu kullanarak BMI'yi hesaplar.

## rtSurvey Uzantıları

XLSForm için temel ondalık soru tanımı basit olmakla birlikte, rtSurvey ek özellikler veya özelleştirmeler sunabilir:

1. Hassasiyet kontrolü (ondalık basamak sayısı)
2. Özel giriş biçimleri (örn. yüzde, para birimi)
3. Gelişmiş doğrulama kuralları

## Sınırlamalar

- Ondalık sayıların hassasiyeti temel sistem veya veritabanı tarafından sınırlandırılabilir.
- Kullanıcıların yerel ayarlarına bağlı olarak beklenen ondalık ayırıcı (nokta veya virgül) konusunda rehberliğe ihtiyaçları olabilir.
- Büyük ondalık sayılar mobil cihazlarda okunması veya girilmesi zor olabilir.
