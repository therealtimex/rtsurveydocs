---
title: "Soruları Tekrarlama"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 260
---

Tekrarlar, rtSurvey'de tek bir anket içinde aynı bilgi setini birden fazla kez toplamanıza olanak tanıyan güçlü bir özelliktir. Bu, birden fazla hane üyesi hakkında veri toplamanız gerekebileceği hane anketleri gibi senaryolar için özellikle kullanışlıdır.

## Temel Tekrar Yapısı

rtSurvey'de bir tekrar oluşturmak için `begin repeat` ve `end repeat` yapısını kullanın:

```
| type         | name         | label                |
|--------------|--------------|----------------------|
| begin repeat | child_repeat |                      |
| text         | name         | Çocuğun adı         |
| decimal      | birthweight  | Çocuğun doğum ağırlığı |
| select_one male_female | sex | Çocuğun cinsiyeti  |
| end repeat   |              |                      |
```

Bu örnekte, kullanıcı forma yeni tekrarlar ekleyerek birden fazla çocuk hakkında bilgi toplayabilir.

## Tekrarları Etiketleme

`begin repeat` için `label` sütunu isteğe bağlı olsa da, bir etiket eklemek gezinmeyi iyileştirebilir:

```
| type         | name         | label                |
|--------------|--------------|----------------------|
| begin repeat | child_repeat | Çocuk Bilgisi    |
| text         | name         | Çocuğun adı         |
| decimal      | birthweight  | Çocuğun doğum ağırlığı |
| select_one male_female | sex | Çocuğun cinsiyeti  |
| end repeat   |              |                      |
```

rtSurvey, her tekrar örneği için "Çocuk Bilgisi"ni başlık olarak görüntüler.

## Sabit Tekrar Sayısı

Sabit sayıda tekrar belirtmek için `repeat_count` sütununu kullanın:

```
| type         | name         | label                | repeat_count |
|--------------|--------------|----------------------|--------------|
| begin repeat | child_repeat | Çocuk Bilgisi    | 3            |
| text         | name         | Çocuğun adı         |              |
| decimal      | birthweight  | Çocuğun doğum ağırlığı |              |
| end repeat   |              |                      |              |
```

Bu tam olarak 3 çocuk tekrarı oluşturacaktır.

## Dinamik Tekrar Sayıları

rtSurvey, önceki cevaplara dayalı dinamik tekrar sayılarını destekler:

```
| type     | name           | label                          | repeat_count       |
|----------|----------------|--------------------------------|--------------------|
| integer  | num_hh_members | Hane üyesi sayısı?             |                    |
| begin repeat | hh_member  | Hane Üyesi                     | ${num_hh_members}  |
| text     | name           | Ad                             |                    |
| integer  | age            | Yaş                            |                    |
| end repeat |              |                                |                    |
```

## Koşullu Tekrarlar

Tekrarları koşullu olarak görüntülemek için `relevant` sütununu kullanabilirsiniz:

```
| type              | name        | label                     | relevant           |
|-------------------|-------------|---------------------------|---------------------|
| select_one yes_no | has_child   | Burada herhangi bir çocuk yaşıyor mu?|                     |
| begin repeat      | child_repeat| Çocuk Bilgisi             | ${has_child} = 'yes'|
| text              | name        | Çocuğun adı               |                     |
| decimal           | birthweight | Çocuğun doğum ağırlığı    |                     |
| end repeat        |             |                           |                     |
```

## rtSurvey'e Özgü Özellikler

### Tekrar Özeti

rtSurvey, tekrarların özet görünümünü sağlar. Özeti özelleştirmek için tekrar içinde bir grup kullanın:

```
| type         | name         | label                                    |
|--------------|--------------|------------------------------------------|
| begin repeat | person_repeat|                                          |
| begin group  | person       | ${first_name} ${last_name} - ${age}      |
| text         | first_name   | Ad                               |
| text         | last_name    | Soyad                                |
| integer      | age          | Yaş                                      |
| end group    |              |                                          |
| end repeat   |              |                                          |
```

### Tekrar Görünüm Seçenekleri

rtSurvey, tekrarlar için ek görünüm seçenekleri sunar:

- `appearance: field-list` - Tekrardaki tüm soruları tek ekranda görüntüler
- `appearance: table-list` - Tekrarları tablo formatında sunar

```
| type         | name         | label            | appearance  |
|--------------|--------------|-------------------|-------------|
| begin repeat | child_repeat | Çocuk Bilgisi | table-list  |
| text         | name         | Ad                |             |
| integer      | age          | Yaş               |             |
| end repeat   |              |                   |             |
```

### İç İçe Tekrarlar

rtSurvey, karmaşık veri yapıları için iç içe tekrarları destekler:

```
| type         | name           | label                |
|--------------|----------------|----------------------|
| begin repeat | household      | Hane                 |
| text         | hh_name        | Hane Adı             |
| begin repeat | hh_member      | Hane Üyesi           |
| text         | member_name    | Üye Adı              |
| integer      | member_age     | Üye Yaşı             |
| end repeat   |                |                      |
| end repeat   |                |                      |
```

## rtSurvey'de Tekrar Kullanımı için En İyi Uygulamalar

1. Veri analizini iyileştirmek için tekrarlar için anlamlı adlar ve etiketler kullanın.
2. Veri giriş hatalarını azaltmak için dinamik tekrar sayılarını kullanmayı düşünün.
3. Özellikle karmaşık iç içe tekrarlar kullanırken formunuzu kapsamlı biçimde test edin.
4. Uzun tekrar listelerinde sayımcıların gezinmesine yardımcı olmak için özet özelliğini kullanın.
5. Çok sayıda tekrar konusunda dikkatli olun; form performansını etkileyebilir.

## Sıfır Tekrarı Ele Alma

rtSurvey'de sıfır tekrarı temsil etmek için:

1. Gerekmiyorsa sayımcıları ilk tekrarı silmeleri için eğitin.
2. Tam sayı bilindiğinde dinamik tekrar sayılarını kullanın.
3. Tekrarları koşullu olarak görüntülemek için `relevant` kullanın.

## Veri Dışa Aktarma Hususları

rtSurvey'den veri dışa aktarılırken, tekrar verisi genellikle düzleştirilir. Her tekrar örneği, dışa aktarılan veride ayrı bir satır haline gelir ve üst formun verisi her örnek için tekrarlanır.

## Mobil Uygulama Hususları

- rtSurvey mobil uygulamasındaki tekrarlar çevrimdışı veri toplamayı destekler.
- Çok sayıda tekrar, düşük özellikli cihazlarda uygulama performansını etkileyebilir.

rtSurvey'de tekrarları etkili biçimde kullanarak, sayımcılar için kullanıcı dostu bir arayüzü korurken karmaşık, hiyerarşik veri yapılarını yakalayabilen esnek ve güçlü anketler oluşturabilirsiniz.
