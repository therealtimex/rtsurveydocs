---
title: "Operatörler ve Fonksiyonlar"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 290
---

rtSurvey'deki ifadeler, JavaRosa/ODK fonksiyonları ve özel rtSurvey fonksiyonlarıyla genişletilmiş **XPath 1.0**'ın bir alt kümesiyle yazılır. XLSForm'unuzdaki `calculate`, `constraint`, `relevant`, `required` ve `default` sütunlarında ifadeler kullanırsınız.

## Alan değerlerine referans verme

Başka bir alana referans vermek için `${fieldname}` kullanın:

```
${age} > 18
```

**Geçerli alanın değerine** referans vermek için `.` (tek bir nokta) kullanın — genellikle `constraint` ifadelerinde kullanılır:

```
. >= 0 and . <= 100
```

Üst gruba referans vermek için `..` kullanın (tekrarlarda gelişmiş kullanım).

## İfade sözdizimi

İfadeler standart XPath kurallarını takip eder:

- **Dizeler** tek tırnak içinde olmalıdır: `'yes'`
- **Sayılar** olduğu gibi yazılır: `42`, `3.14`
- **Boolean** sonuçlar `relevant`, `required` ve `constraint` için kullanılır — boş olmayan, sıfırdan farklı her değer doğrudur
- Operatörlerin etrafındaki boşluk görmezden gelinir

{{% alert icon=" " context="warning" %}}
Her zaman düz tırnak (`'` veya `"`) kullanın — asla "akıllı tırnak" (kıvrımlı tırnak) kullanmayın. Zengin metin düzenleyiciler genellikle tırnakları otomatik olarak dönüştürür ve ifadelerinizi bozar.
{{% /alert %}}

## Bu bölümdeki başlıklar

- **[Operatörler](operators)** — karşılaştırma operatörleri (`=`, `!=`, `>`, `<`, `>=`, `<=`) ve mantıksal operatörler (`and`, `or`, `not()`)
- **[Fonksiyonlar](functions)** — dize, seçim, sayı, tarih/saat, boolean, coğrafi ve yardımcı fonksiyonlar
- **[Referanslar](references)** — alanlara ve bağlam değerlerine nasıl referans verilir

## Hızlı örnekler

| Kullanım durumu | İfade |
|----------|------------|
| Yaş 18'den büyükse göster | `${age} > 18` |
| Yalnızca "yes" seçildiyse göster | `${consent} = 'yes'` |
| Başka bir alan boş değilse zorunlu kıl | `${name} != ''` |
| Toplam hesapla | `${adults} + ${children}` |
| İsmi birleştir | `concat(${first_name}, ' ', ${last_name})` |
| Bugünün tarihi | `today()` |
| Seçenek seçilip seçilmediğini kontrol et | `selected(${interests}, 'sports')` |
