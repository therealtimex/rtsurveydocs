---
title: "Select_multiple"
description: "Select_multiple soruları, katılımcıların önceden tanımlanmış bir listeden bir veya daha fazla seçenek seçmesine olanak tanır."
icon: "check_box"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 225
---

`select_multiple` soru türü, katılımcının **bir veya daha fazla seçenek** belirleyebildiği bir liste görüntüler. Varsayılan olarak seçenekler onay kutusu olarak görüntülenir. Saklanan değer, seçilen tüm seçenek değerlerinin **boşlukla ayrılmış listesidir**.

## Temel XLSForm Tanımı

**survey çalışma sayfası:**

| type | name | label |
|------|------|-------|
| select_multiple crops | crops_grown | Hane hangi ürünleri yetiştiriyor? |

**choices çalışma sayfası:**

| list_name | name | label |
|-----------|------|-------|
| crops | maize | Mısır |
| crops | beans | Fasulye |
| crops | rice | Pirinç |
| crops | vegetables | Sebze |
| crops | other | Diğer |

Daha fazla ayrıntı için [XLSForm spesifikasyonuna](https://xlsform.org/en/#question-types) bakın.

## Saklanan veri biçimi

Dışa aktarılan sütun, seçilen değerlerin boşlukla ayrılmış listesini içerir:

```
maize beans vegetables
```

İfadelerde select_multiple değerlerini test ederken `=` değil `selected()` fonksiyonunu kullanın (aşağıya bakın).

## Kullanım Alanları

Select_multiple soruları şunlar için kullanılır:

1. Birden fazla geçerli yanıt toplama (örn. gelir kaynakları, yetiştirilen ürünler, semptomlar)
2. Onay kutusu tarzı anlaşma öğeleri (örn. "Geçerli olanları seçin")
3. Dil veya beceri envanterleri
4. Birden fazla yanıtın aynı anda geçerli olduğu herhangi bir soru

## Görünüm seçenekleri

{{< table >}}
| Görünüm | Açıklama |
|------------|-------------|
| *(yok)* | Varsayılan onay kutuları, her satırda bir tane |
| `minimal` | Açılır çoklu seçim widget'ı |
| `compact` | Kompakt ızgara, sütun sayısı ekran genişliğine göre ayarlanır |
| `compact-N` | N sütuna zorlanmış kompakt ızgara |
| `horizontal` | Yatay sırada düzenlenmiş seçenekler (web) |
| `horizontal-compact` | Yatay, kompakt aralık (web) |
| `label` | Yalnızca etiketleri gösterir, onay kutusu yok (`list-nolabel` ile birlikte kullanın) |
| `list-nolabel` | Yalnızca onay kutularını gösterir, etiket yok (`label` ile birlikte kullanın) |
| `columns(N)` | N sütunda görüntüle (rtSurvey uzantısı) |
{{< /table >}}

### Örnek: 3 sütunlu kompakt düzen

| type | name | label | appearance |
|------|------|-------|------------|
| select_multiple symptoms | symptoms | Gözlemlenen tüm semptomları seçin | compact-3 |

## İfadelerde `selected()` kullanımı

Saklanan değer boşlukla ayrılmış bir dize olduğundan, belirli bir seçeneğin seçilip seçilmediğini test etmek için **mutlaka** `selected()` kullanmalısınız. `=` kullanmak doğru çalışmaz.

### `relevant` içinde

Yalnızca "diğer" seçilmişse takip sorusunu göster:

| type | name | label | relevant |
|------|------|-------|----------|
| select_multiple crops | crops_grown | Hangi ürünler yetiştiriliyor? | |
| text | crops_other | Lütfen diğer ürünleri belirtin | `selected(${crops_grown}, 'other')` |

### `constraint` içinde

En az 2 seçim zorunlu kılın:

| type | name | constraint | constraint_message |
|------|------|------------|-------------------|
| select_multiple issues | issues | `count-selected(.) >= 2` | En az 2 sorun seçin |

En fazla 3 ile sınırlandırın:

| type | name | constraint | constraint_message |
|------|------|------------|-------------------|
| select_multiple priorities | priorities | `count-selected(.) <= 3` | En fazla 3 öncelik seçin |

### `calculate` içinde — seçilen etiketleri birleştirme

Okunabilir bir özet oluşturmak için `selected-at()`, `count-selected()` ve `choice-label()` birleştirin:

| type | name | calculation |
|------|------|-------------|
| calculate | crops_summary | join(', ', ${crops_grown}) |

## "Hiçbiri" / özel seçenek

Yaygın bir kalıp, bir seçeneği diğerleriyle karşılıklı dışlayıcı yapmaktır. Bunu uygulamak için `constraint` kullanın:

| type | name | label | constraint | constraint_message |
|------|------|-------|------------|-------------------|
| select_multiple issues | issues | Mevcut tüm sorunları seçin | `not(selected(., 'none') and count-selected(.) > 1)` | "Hiçbiri" diğer seçeneklerle birlikte seçilemez |

**choices:**

| list_name | name | label |
|-----------|------|-------|
| issues | water | Su sıkıntısı |
| issues | roads | Kötü yollar |
| issues | health | Sağlık hizmetleri eksikliği |
| issues | none | Hiçbiri |

## Seçimleri sayma ve özetleme

| Fonksiyon | Örnek | Sonuç |
|----------|---------|--------|
| `count-selected(field)` | `count-selected(${crops_grown})` | Seçilen seçenek sayısı |
| `selected(field, value)` | `selected(${crops_grown}, 'maize')` | doğru/yanlış |
| `selected-at(field, index)` | `selected-at(${crops_grown}, 0)` | Birinci seçilen değer |
| `choice-label(field, value)` | `choice-label(${crops_grown}, 'maize')` | Bir değerin etiketi |

## En İyi Uygulamalar

1. `relevant`, `constraint` ve `calculate` içinde her zaman `selected()` kullanın — asla `=` veya `!=` kullanmayın.
2. Soru tasarımı gerektiriyorsa maksimum seçim sayısını sınırlandırmak için kısıtlama ekleyin.
3. Sıfır seçim geçerli bir yanıt olduğunda "Hiçbiri" veya "Uygulanamaz" seçeneği ekleyin.
4. Uzun listeler için (15+ seçenek), aşırı kaydırmayı önlemek için `minimal` (çoklu seçim açılır listesi) kullanın.
5. Veriyi dışa aktarıp analiz aracınızda dize bölme kullanın — boşlukla ayrılmış biçim, pivot yapmadan önce bölme gerektirir.

## Sınırlamalar

- Select_multiple değerleri `=` ile doğrudan karşılaştırılamaz. Her zaman `selected()` kullanın.
- Kompakt görünüm çok uzun seçenek etiketleri için iyi görünmeyebilir.
- Seçenekleri `choice_filter` ile filtrelerken filtreleme tüm görüntülenen seçeneklere uygulanır, `select_one` ile aynı şekilde.
