---
title: "Tam Sayı"
description: "Tam sayı soruları, anketinizde tam sayı girişlerine olanak tanır."
icon: "123"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 222
---

XLSForm'larda ve rtSurvey'de tam sayı soru türü, tam sayı yanıtları toplamak için kullanılır. Bu soru türü, sayımlar, yaşlar veya yıllar gibi ondalık basamak olmaksızın sayısal veri toplamak için gereklidir.

## Temel XLSForm Tanımı

| type    | name  | label                 |
|---------|-------|------------------------|
| integer | age   | Yaşınızı yıl cinsinden girin |

Temel tam sayı soru türü hakkında daha fazla ayrıntı için [XLSForm spesifikasyonuna](https://xlsform.org/en/#question-types) bakın.

## Kullanım Alanları

Tam sayı soruları yaygın olarak şunlar için kullanılır:

1. Yaş girişleri
2. Öğe sayma (örn. çocuk sayısı, hane üyeleri)
3. Yıl girişleri (örn. doğum yılı)
4. Sayısal ölçekte derecelendirmeler
5. Tam sayı gerektiren herhangi bir sayısal veri toplama

## rtSurvey Uzantıları

XLSForm için temel tam sayı soru tanımı basit olmakla birlikte, rtSurvey ek özellikler veya özelleştirmeler sunabilir:

1. Aralık doğrulama
2. Özel hata mesajları
3. Sayı girişi için görünüm seçenekleri

## En İyi Uygulamalar

1. Beklenen girişi belirtmek için açık ve kısa etiketler kullanın.
2. Gerçekçi olmayan veya hatalı girişleri önlemek için aralık kısıtlamaları uygulayın.
3. Örnekler sağlamak veya beklenen biçimi açıklamak için ipucu metni kullanmayı düşünün.
4. Büyük sayılar için okunabilirliği artırmak amacıyla etikette virgül veya boşluk kullanmayı düşünün (örn. "Nüfusu girin (1.000.000'a kadar)").

## Kısıtlamalar ve Doğrulama

Girilen değerin belirli bir aralıkta olmasını sağlamak için kısıtlamalar ekleyebilirsiniz:

| type    | name  | label                 | constraint        | constraint_message                    |
|---------|-------|------------------------|-------------------|---------------------------------------|
| integer | age   | Yaşınızı yıl cinsinden girin | .>0 and .<=120    | Yaş 1 ile 120 yıl arasında olmalıdır |

## Örnek Kullanım

Bir hane anketinde tam sayı sorularını nasıl kullanabileceğinize dair bir örnek:

| type    | name           | label                                     | constraint | constraint_message                |
|---------|----------------|-------------------------------------------|------------|-----------------------------------|
| integer | household_size | Hanenizde kaç kişi yaşıyor?               | .>0        | Hane büyüklüğü en az 1 olmalıdır  |
| integer | num_children   | Hanede 18 yaşından küçük kaç çocuk var?   | .>=0       | Çocuk sayısı negatif olamaz       |
| integer | year_built     | Eviniz hangi yılda inşa edildi?           | .>1800 and .<=2023 | Yıl 1800 ile 2023 arasında olmalıdır |

## Tam Sayı Değerleriyle Hesaplama

Tam sayı değerleri hesaplamalarda kullanılabilir. İşte bir örnek:

| type    | name           | label                                     |
|---------|----------------|-------------------------------------------|
| integer | num_adults     | Hanedeki yetişkin sayısı                  |
| integer | num_children   | Hanedeki çocuk sayısı                     |
| calculate | total_members | |

Hesaplama satırında şunu kullanabilirsiniz:

```
calculation | ${num_adults} + ${num_children}
```

Bu, toplam hane üyelerini elde etmek için yetişkin ve çocuk sayılarını toplar.
