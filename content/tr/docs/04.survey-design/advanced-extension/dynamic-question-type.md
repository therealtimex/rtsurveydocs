---
title: "Dinamik Soru Türü"
description: "Dinamik soru türü, bir alanın soru türünün ve widget'ının form tasarım zamanında değil çalışma zamanında bir API yanıtına veya hesaplanmış değere göre belirlenmesine olanak tanır."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 301
---

**Dinamik Soru Türü** özelliği, bir alanın giriş widget'ının ve doğrulama davranışının form tasarım zamanında değil **çalışma zamanında** belirlenmesine olanak tanır. Bu, toplanacak veri türünün sunucu tarafı yapılandırmasına, API yanıtına veya önceki alan değerine bağlı olduğu durumlarda kullanılan gelişmiş bir rtSurvey uzantısıdır.

Yaygın bir kullanım durumu, sunucunun hangi alanların gerekli olduğunu, bunların türünün ne olduğunu (text, integer, select, vb.) ve hangi seçeneklerin mevcut olduğunu tanımladığı — her yapılandırma için formu yeniden oluşturmaya gerek kalmaksızın — yapılandırılabilir bir denetim listesidir.

---

## Nasıl çalışır

Dinamik soru türü olarak işaretlenen bir alan, yapılandırmasını bir API'den almak için `callapi()` kullanır. API yanıtı şunları tanımlar:

- Oluşturulacak giriş türü (text, integer, select_one, vb.)
- Mevcut seçenekler (select türleri için)
- Doğrulama kuralları

Alan dahili olarak `specialFeature: isDynamicQuestionType` ile işaretlenir; bu, form motoruna statik form tanımı yerine widget'ı oluşturmak için API yanıtını kullanmasını söyler.

---

## Kurulum

### Adım 1: Alan yapılandırmasını getir

Dinamik yapılandırmayı almak için `callapi()` içeren bir `calculate` alanı kullanın:

| type | name | label | appearance | calculation |
|------|------|-------|------------|-------------|
| calculate | field_config | | callapi | `callapi('POST', 'https://api.example.com/field-config', 1, 2, 0, '$.config', 10000, 0, '', '', '{"form_id": "##form_id##", "field_id": "inspection_result"}')` |

### Adım 2: Dinamik alanda yapılandırmaya referans ver

Dinamik alan, getirilen yapılandırmaya bağlanmak için `appearance` veya `constraint` içinde `callapi-verify()` kullanır:

| type | name | label | appearance |
|------|------|-------|------------|
| text | inspection_result | Denetim sonucu | `callapi-verify(dynamicParams)` |

Form motoru `field_config`'i okur ve `inspection_result`'ı `text`, `integer` veya `select_one` alanı olarak oluşturup oluşturmayacağını dinamik olarak belirler.

---

## API yanıt formatı

API, alan yapılandırmasını açıklayan bir JSON nesnesi döndürmelidir. Tipik bir yanıt:

```json
{
  "config": {
    "type": "select_one",
    "choices": [
      {"value": "pass", "label": "Geçti"},
      {"value": "fail", "label": "Başarısız"},
      {"value": "na", "label": "Geçerli Değil"}
    ],
    "required": true,
    "constraint": ". != ''"
  }
}
```

---

## Örnek: Yapılandırılabilir denetim formu

Kontrol listesi öğelerinin ve cevap türlerinin denetim kategorisine göre sunucudan getirildiği bir denetim formu:

| type | name | label | appearance | calculation |
|------|------|-------|------------|-------------|
| select_one inspection_type | insp_type | Denetim türü | | |
| calculate | checklist_config | | callapi | `callapi('POST', 'https://api.example.com/checklist', 1, 2, 0, '$.items', 10000, 0, '', '', '{"type": "##insp_type##"}')` |
| text | item_1 | Öğe 1 | `callapi-verify(dynamicParams)` | |
| text | item_2 | Öğe 2 | `callapi-verify(dynamicParams)` | |
| text | item_3 | Öğe 3 | `callapi-verify(dynamicParams)` | |

Sunucu, `insp_type`'a göre her öğe için doğru widget türünü, etiketi, seçenekleri ve doğrulamayı döndürür.

---

## En İyi Uygulamalar

1. Dinamik soru türlerini yalnızca alan yapısı çalışma zamanında gerçekten değiştiğinde kullanın — statik formlar için standart soru türlerini kullanın.
2. Yapılandırma API'sinin hızlı yanıt verdiğinden emin olun (2 saniyenin altında) ve saha ağında mevcut olduğundan emin olun.
3. API'ye ulaşılamadığı durum için her zaman formda mantıklı bir yedek tanımlayın — not içeren basit bir `text` alanı, bozuk bir widget'tan iyidir.
4. API yanıt şemasını sürümlendirin — yanıt formatındaki değişiklikler bu uç noktayı kullanan tüm aktif formları etkileyecektir.
5. Dağıtımdan önce API'nin döndürebileceği her alan türü kombinasyonunu test edin.

## Sınırlamalar

- Dinamik soru türleri, yapılandırmayı getirmek için ağ bağlantısı gerektirir.
- Dinamik olarak mevcut widget türlerinin tam aralığı rtSurvey istemci sürümüne bağlıdır — hedef sürümünüzü test edin.
- Bu, standart XLSForm spesifikasyonunda karşılığı olmayan gelişmiş bir rtSurvey uzantısıdır.
- Alan tanımı kısmen formda ve kısmen API yanıtında yaşadığından hata ayıklamak daha zordur.
