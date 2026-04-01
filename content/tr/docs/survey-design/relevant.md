---
title: "Soruları Atlama"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 280
---

Atlama mantığı (dallanma veya koşullu mantık olarak da bilinir), katılımcıların cevaplarına uyum sağlayan dinamik anketler oluşturmanıza olanak tanır. rtSurvey'de atlama mantığı, XLSForm'unuzdaki `relevant` sütunu kullanılarak uygulanır.

## Temel Atlama Mantığı

Temel atlama mantığını uygulamak için bir koşul belirtmek üzere `relevant` sütununu kullanın:

```
| type           | name          | label                       | relevant            |
|----------------|---------------|-----------------------------|--------------------|
| select_one y_n | likes_pizza   | Pizzayı sever misiniz?          |                    |
| select_multiple pizza_toppings | favorite_topping | Favori malzemeler | ${likes_pizza} = 'yes' |
```

Bu örnekte, "Favori malzemeler" sorusu yalnızca katılımcı pizzayı sevdiğine "evet" yanıtı verirse görünür.

## Relevant İfadeleri için Sözdizimi

- Diğer soru değişkenlerine referans vermek için `${ }` kullanın.
- `select_one` soruları için doğrudan karşılaştırın: `${question_name} = 'answer'`
- `select_multiple` soruları için `selected()` fonksiyonunu kullanın.

## Gelişmiş Atlama Mantığı

### Birden Fazla Koşul

`and`, `or` ve parantezler kullanarak birden fazla koşulu birleştirebilirsiniz:

```
| type    | name  | label                   | relevant                                  |
|---------|-------|-------------------------|-------------------------------------------|
| integer | age   | Yaşınız nedir?          |                                           |
| text    | school| Hangi okula gidiyorsunuz? | ${age} < 18 and (${location} = 'urban' or ${location} = 'suburban') |
```

### select_multiple Sorularını Kullanma

`select_multiple` soruları için `selected()` fonksiyonunu kullanın:

```
| type           | name          | label                       | relevant                               |
|----------------|---------------|-----------------------------|-----------------------------------------|
| select_multiple pizza_toppings | favorite_topping | Favori malzemeler |                                         |
| text           | cheese_type   | Favori peynir türü     | selected(${favorite_topping}, 'cheese') |
```

### Çoktan Seçmelide "Diğer" Seçeneği

`relevant` kullanarak serbest metin "Diğer" seçeneği uygulayın:

```
| type           | name                  | label                               | relevant                               |
|----------------|----------------------|-------------------------------------|---------------------------------------|
| select_multiple pizza_toppings | favorite_toppings | Favori pizza malzemeleriniz neler? |                                       |
| text           | favorite_toppings_other | Başka hangi malzemeleri seversiniz?   | selected(${favorite_toppings}, 'other') |
```

Choices çalışma sayfanıza 'other' seçeneğini eklemeyi unutmayın.

## rtSurvey'e Özgü Özellikler

### Dinamik İlgililik

rtSurvey, hesaplanan alanlara dayalı dinamik ilgililiğe izin verir:

```
| type      | name       | label              | calculation                   |
|-----------|------------|--------------------|-----------------------------|
| calculate | total_score| Toplam Puan        | ${score1} + ${score2} + ${score3} |
| text      | feedback   | Geri Bildirim      | ${total_score} > 75             |
```

### Tekrarlarda İlgililik

rtSurvey, tekrar gruplarında ilgililiği destekler:

```
| type         | name         | label            | relevant               |
|--------------|--------------|------------------|------------------------|
| begin repeat | child_info   | Çocuk Bilgisi    |                        |
| integer      | child_age    | Çocuğun Yaşı     |                        |
| text         | school_name  | Okul Adı          | ${child_age} >= 5      |
| end repeat   |              |                  |                        |
```

### Basamaklı İlgililik

rtSurvey, basamaklı ilgililiği verimli şekilde ele alır; bir sorunun ilgililiğinin diğerine bağlı olduğu ve bunun da üçüncü birine bağlı olduğu durumlar:

```
| type           | name        | label                  | relevant               |
|----------------|-------------|------------------------|------------------------|
| select_one y_n | has_car     | Arabanız var mı?       |                        |
| select_one car_type | car_type | Araba türü nedir?    | ${has_car} = 'yes'     |
| text           | model       | Spesifik model         | ${car_type} = 'sedan'  |
```

## rtSurvey'de Atlama Mantığı için En İyi Uygulamalar

1. **Basit Tutun**: Mümkün olduğunda aşırı karmaşık ilgililik koşullarından kaçının.
2. **Kapsamlı Test Edin**: Anketiniz boyunca tüm olası yolları test etmek için rtSurvey'in önizleme özelliğini kullanın.
3. **Performansı Göz Önünde Bulundurun**: Çok karmaşık atlama mantığı, özellikle mobil cihazlarda anket performansını etkileyebilir.
4. **Net Değişken Adları Kullanın**: Bu, ilgililik ifadelerinizin okunmasını ve bakımını kolaylaştırır.
5. **Mantığınızı Belgeleyin**: Ekip işbirliği için özellikle karmaşık atlama kalıplarını açıklamak üzere notlar ekleyin.
6. **Veri Analizini Göz Önünde Bulundurun**: Atlanan sorular eksik verilerle sonuçlanacaktır. Analizinizi buna göre planlayın.

## Atlama Mantığında Sorun Giderme

- **Sözdizimi Hataları**: Tüm `${ }` işaretlerinin düzgün kapatıldığından ve doğru yazıldığından emin olun.
- **Döngüsel Referanslar**: Soruların birbirine bağımlı olduğu döngüler oluşturmaktan kaçının.
- **Büyük/Küçük Harf Duyarlılığı**: İlgililik ifadelerinde cevap seçeneklerinin büyük/küçük harf duyarlı olduğunu unutmayın.
- **Sayısal Karşılaştırmalar**: Sayısal karşılaştırmalar için uygun operatörleri kullanın (`<`, `>`, `=`).

## Sonuç

Atlama mantığının etkili kullanımı, rtSurvey projelerinizde katılımcı deneyimini ve veri kalitesini önemli ölçüde artırabilir. rtSurvey'in gelişmiş özelliklerinden yararlanarak ve en iyi uygulamaları izleyerek, her katılımcının benzersiz durumuna uyum sağlayan dinamik ve verimli anketler oluşturabilirsiniz.
