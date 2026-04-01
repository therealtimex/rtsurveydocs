---
title: "Dinamik Arama"
description: "Dinamik Arama, sayımcı yazarken gerçek zamanlı olarak uzak API'den seçenekler yükler; büyük veya sık güncellenen veri kümelerini mümkün kılar."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 293
---

**Dinamik Arama** (Arama API'si olarak da adlandırılır), bir `select_one`, `select_multiple` veya `text` alanının sayımcı yazarken seçeneklerini uzak bir web hizmetinden **çalışma zamanında** yüklemesine olanak tanır. Seçenek listeniz bir CSV dosyasına sığamayacak kadar büyükse, sık sık güncelleniyorsa veya canlı bir veritabanından geliyorsa bu doğru yaklaşımdır.

---

## `search-api()` görünümü

Dinamik arama, `search-api()` fonksiyonunu kullanarak `appearance` sütunu aracılığıyla yapılandırılır:

```
search-api(method, url, post_body, value_column, display, data_path, save_path)
```

### Parametreler

| Parametre | Açıklama |
|-----------|-------------|
| `method` | Her zaman `'POST'` kullanın |
| `url` | Sorgulanacak API uç noktası |
| `post_body` | API'ye gönderilen JSON gövdesi. Sayımcının geçerli arama metni için yer tutucu olarak `%__input__%` kullanın |
| `value_column` | Depolanan **değer** olarak kullanılacak yanıt nesnesindeki anahtar |
| `display` | Açılır menüde gösterilen **etiket** olarak kullanılacak anahtar (veya şablon). `##key##` yer tutucularını ve `@{func}` ifadelerini destekler |
| `data_path` | Yanıttaki sonuç nesneleri dizisine JSONPath (örn. `$.data`, `$.hits.hits.*._source`) |
| `save_path` | Ham yanıtın diğer alanlar tarafından kullanım için kaydedileceği ad |

---

## Temel örnek

Sayımcının tesis adının bir kısmını yazdığı sağlık tesisi araması:

| type | name | label | appearance |
|------|------|-------|------------|
| select_one | facility | Sağlık tesisini seçin | `search-api('POST', 'https://api.example.com/facilities/search', '{"query": "%__input__%"}', 'id', 'name', '$.results', 'facility_data')` |

API, sayımcı "nairo" yazdığında `{"query": "nairo"}` alır ve döndürür:

```json
{
  "results": [
    {"id": "HF001", "name": "Nairobi Merkez Kliniği"},
    {"id": "HF002", "name": "Nairobi Batı Hastanesi"}
  ]
}
```

Açılır menü `Nairobi Merkez Kliniği` ve `Nairobi Batı Hastanesi`'ni gösterir; depolanan değer `HF001` veya `HF002`'dir.

---

## Gelişmiş görüntüleme biçimlendirme

### `##key##` şablonlarını kullanma

Etikette birden fazla alanı göster:

```
search-api('POST', 'https://api.example.com/search', '{"q": "%__input__%"}', 'id', '##name## (##district##)', '$.data', 'res')
```

Şöyle görüntülenir: `Nairobi Merkez Kliniği (Nairobi)`.

### `@{func}` ifadelerini kullanma

Görüntüleme etiketinde koşullu mantık uygulayın:

```
search-api('POST', 'https://api.example.com/search', '{"q": "%__input__%"}', 'id',
  '@{if_else(eq("##status##", "active"), "✓ ##name##", "✗ ##name##")}',
  '$.data', 'res')
```

Aktif sonuçlar `✓ Klinik Adı` gösterir; inaktif sonuçlar `✗ Klinik Adı` gösterir.

---

## Varsayılan değer ayarlama: `search-default-api()`

Alanı ayrı bir API çağrısından yüklenen varsayılan bir seçimle önceden doldurmak için `search-api()`'den sonra `search-default-api()` kullanın (örn. mevcut bir kaydı düzenlerken):

```
appearance: search-api(...) search-default-api('POST', 'https://api.example.com/get', '{"id": "##saved_id##"}', 'id', 'name', '$.item')
```

---

## select_multiple için özel ayırıcı: `search-default-separator()`

`select_multiple` alanları için, birden fazla seçili değerin depolanan dizede nasıl birleştirileceğini belirtin:

```
appearance: search-api(...) search-default-separator(' || ')
```

Varsayılan ayırıcı bir boşluktur.

---

## Desteklenen soru türleri

| Soru türü | Kullanım durumu |
|---------------|----------|
| `select_one` | Arama sonuçlarından tek seçim |
| `select_multiple` | Arama sonuçlarından çoklu seçim |
| `text` | Otomatik tamamlama — sayımcı serbestçe yazar ama öneri seçebilir |

---

## Kaydedilmiş yanıt verilerini kullanma

`save_path`, tam API yanıt nesnesini verilen ad altında depolar. Diğer alanlar `pulldata()` ile buna referans verebilir:

| type | name | label | calculation |
|------|------|-------|-------------|
| select_one | facility | Tesis seçin | `search-api(..., 'facility_data')` |
| calculate | facility_district | | `pulldata('facility_data', 'district')` |
| calculate | facility_type | | `pulldata('facility_data', 'type')` |

---

## En İyi Uygulamalar

1. API uç noktasının 1–2 saniye içinde yanıt verdiğinden emin olun — yavaş API'ler aramayı yavaş hissettirirler.
2. API'nin yalnızca eşleşen sonuçları döndürmesi için `post_body`'de `%__input__%` kullanın; tüm veri kümesini değil.
3. Hızlı yanıtlar için sunucu tarafında arama alanını indeksleyin (örn. Elasticsearch, veritabanı tam metin indeksi).
4. Sorgu başına sonuçları 20–50 öğeyle sınırlandırın — binlerce sonuç döndürmek aramanın amacını ortadan kaldırır.
5. Tek karakterli girişlerde geniş sorguların tetiklenmesini önlemek için API'de minimum giriş uzunluğu gereksinimi ekleyin.

## Sınırlamalar

- Dinamik Arama, ağ bağlantısı gerektirir — çevrimdışı çalışmaz.
- `%__input__%` yer tutucusu olduğu gibi eklenir; enjeksiyon saldırılarını önlemek için sunucu tarafında girişleri temizleyin.
- Karmaşık `@{func}` görüntüleme ifadeleri tüm rtSurvey istemci sürümlerinde sınırlı desteğe sahip olabilir.
