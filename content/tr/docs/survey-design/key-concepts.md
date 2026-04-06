---
title: "Temel Kavramlar"
description: "Form tasarımına genel bakış"
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 210
---

## XLSForm Nedir?
rtSurvey, karmaşık anketler oluşturmak için güçlü özellikler sunan [XLSForm](https://xlsform.org/) standardının genişletilmiş bir sürümünü form tasarımı için kullanır. Bu kılavuz, temel XLSForm yapısından gelişmiş rtSurvey'e özgü özelliklere kadar rtSurvey'de form tasarımının temel kavramlarını tanıtacaktır.

XLSForm'larla tanıdık Excel aracını kullanarak insan tarafından okunabilir biçimde formlar oluşturabilirsiniz; bu da onu neredeyse herkese erişilebilir kılar. Bu standart, form oluşturmada kolay paylaşım ve işbirliğini mümkün kılar.

XLSForm'lar başlangıç dostu olmakla birlikte, deneyimli kullanıcıların da karmaşık formlar oluşturmasına olanak tanır.

rtSurvey, çeşitli web ve mobil veri toplama platformlarında formlara atlama mantığı gibi gelişmiş işlevleri dahil etmenin tutarlı bir yolunu sağlar.

## XLSForm Yapısı
Bir XLSForm genellikle iki ana çalışma sayfasından oluşur:

1. **survey**: Formunuzun yapısını ve içeriğini tanımlar.
2. **choices**: Çoktan seçmeli sorular için cevap seçeneklerini belirtir.

İsteğe bağlı bir **settings** çalışma sayfası ek form özellikleri sağlayabilir.

Survey ve choices çalışma sayfalarındaki zorunlu sütunların formun düzgün çalışması için mevcut olması gerektiğini unutmamak önemlidir. Her iki çalışma sayfasındaki isteğe bağlı sütunlar, formdaki her giriş davranışı üzerinde daha fazla kontrol sağlar ancak zorunlu değildir.

Excel çalışma kitabınızdaki sütunlar herhangi bir sırayla görünebilir ve isteğe bağlı sütunlar boş bırakılabilir. Ancak formun doğru çalışması için XLSForm belgelerinde belirtilen kesin sözdizimi ve adlandırma kurallarını kullanmak çok önemlidir.

### Survey çalışma sayfası
**Survey çalışma sayfası**, formunuzun yapısını tanımladığınız ve içeriği sağladığınız yerdir. Survey çalışma sayfasındaki her satır, formunuzdaki bir soruyu veya öğeyi temsil eder. Aşağıdaki sütunlar survey çalışma sayfasında zorunludur:

- `type`: Soru için beklediğiniz giriş türünü belirtir.
- `name`: Bu giriş için benzersiz değişken adı belirtir. İsimler bir harf veya alt çizgi ile başlamalı ve yalnızca harf, rakam, tire, alt çizgi ve nokta içerebilir. İsimler büyük/küçük harf duyarlıdır.
- `label`: Formdaki soru için gördüğünüz gerçek metni içerir.

| type                | name     | label                |
| ------------------- | -------- | -------------------- |
| today               | today    |                      |
| select_one gender   | gender   | Katılımcının cinsiyeti? |
| integer             | age      | Katılımcının yaşı?    |

### Choices çalışma sayfası
**`choices`** çalışma sayfası, çoktan seçmeli sorular için cevap seçeneklerini belirtmek için kullanılır. Her satır bir cevap seçeneğini temsil eder. Aşağıdaki sütunlar choices çalışma sayfasında zorunludur:

- **`list_name`**: İlgili cevap seçeneklerini bir araya toplar.
- **`name`**: Bu cevap seçeneği için benzersiz değişken adı belirtir.
- **`label`**: Cevap seçeneğini formda tam olarak görünmesini istediğiniz şekilde gösterir.

| list_name           | name        | label                |
| ------------------- | ----------- | -------------------- |
| gender              | transgender | Transgender          |
| gender              | female      | Kadın                |
| gender              | male        | Erkek                |
| gender              | other       | Diğer                |

Excel çalışma kitabınıza eklediğiniz sütunlar, ister zorunlu ister isteğe bağlı olsun, herhangi bir sırayla görünebilir. İsteğe bağlı sütunlar tamamen çıkarılabilir. Satırlar veya sütunlar okunabilirliği artırmak için boş bırakılabilir; ancak bir sayfada 20 bitişik boş sütun veya satırdan sonraki veriler işlenmeyecektir. Tüm .xlsx dosya biçimlendirmesi yoksayılır; bu nedenle formu daha okunabilir hale getirmek için ayırıcı çizgiler, gölgelendirme ve diğer yazı tipi biçimlendirmelerini kullanabilirsiniz.

Excel'de form oluştururken dikkat edilmesi gereken bir şey, kullandığınız sözdiziminin kesin olması gerektiğidir. Örneğin, **choices** yerine **Choices** veya **choice** yazarsanız form çalışmaz.

### Settings çalışma sayfası

Settings çalışma sayfası isteğe bağlıdır ancak form düzeyi meta verileri ve davranışı belirtmenize olanak tanır. Settings çalışma sayfasındaki yaygın sütunlar şunları içerir:

| Sütun | Açıklama |
|--------|-------------|
| form_title | Kullanıcılara göründüğü şekliyle formun başlığı |
| form_id | Veri yönetiminde ve API çağrılarında kullanılan, form için benzersiz tanımlayıcı |
| default_language | Çok dilli formlar için varsayılan dil kodu (örn. İngilizce için 'en') |
| version | Değişiklikleri izlemek için kullanışlı olan formun sürüm numarası |
| instance_name | Her form gönderimi için benzersiz bir ad oluşturmak üzere ifade |
| generation | Formun nesil sayısını işaretleyen tam sayı. Yapısal değişiklikler için artırın |
| family | İlgili formları yapısal değişiklikler boyunca gruplamak için tanımlayıcı |

rtSurvey'deki settings çalışma sayfası ayrıca rtSurvey'in genişletilmiş işlevlerine özgü ek yapılandırmalar içerebilir. Desteklenen ayarların tam listesi için rtSurvey belgelerine bakın.

## Survey Çalışma Sayfasının Temel Bileşenleri

Survey çalışma sayfası form tasarımınızın çekirdeğidir. İşte temel bileşenlerine genel bir bakış:

| Bileşen | Açıklama |
|-----------|-------------|
| [type](#question-types) | Soru türünü belirtir (örn. text, integer, select_one) |
| [name](#naming-conventions) | Soru için benzersiz tanımlayıcı |
| [label](#labels-and-translations) | Katılımcıya görüntülenen metin |
| [hint](#hints-and-help-text) | Katılımcı için ek rehberlik |
| [appearance](#appearance-options) | Sorunun nasıl görüntüleneceğini değiştirir |
| [relevant](#relevance-and-skip-logic) | Sorunun ne zaman sorulması gerektiğini belirler (atlama mantığı) |
| [constraint](#constraints-and-validation) | Yanıtı doğrular |
| [calculation](#calculations) | Diğer yanıtlara göre değerler hesaplar |
| [required](#required-fields) | Sorunun yanıtlanıp yanıtlanmaması gerektiğini belirtir |


Bu bileşenlerin her biri, etkili ve verimli anketler oluşturmada kritik bir rol oynar. Her bileşen hakkında daha fazla bilgi edinmek için "Ayrıntılı Bölüm" sütunundaki bağlantılara tıklayın.

### Soru türleri
XLSForm bir dizi soru türünü destekler. Bunlar, XLSForm'unuzdaki **`survey`** çalışma sayfasındaki **`type`** sütununa girebileceğiniz seçeneklerden yalnızca bazılarıdır:

| Soru türü             | Cevap girişi                                                                                 |
| ------------------------- | -------------------------------------------------------------------------------------------- |
| integer                   | Tam sayı girişi.                                                                          |
| decimal                   | Ondalık giriş.                                                                               |
| range                     | [Aralık](#range) girişi (derecelendirme dahil)                                                     |
| text                      | Serbest metin yanıtı.                                                                          |
| select_one [options]      | [Çoktan seçmeli](#multiple-choice) soru; yalnızca bir cevap seçilebilir.               |
| select_multiple [options] | [Çoktan seçmeli](#multiple-choice) soru; birden fazla cevap seçilebilir.              |
| select_one_from_file [file]| [Dosyadan çoktan seçmeli](#multiple-choice-from-file); yalnızca bir cevap seçilebilir.      |
| select_multiple_from_file [file]| [Dosyadan çoktan seçmeli](#multiple-choice-from-file); birden fazla cevap seçilebilir.|
| rank [options]            | [Sıralama](#rank) sorusu; bir listeyi sıralayın.                                                        |
| note                      | Ekranda bir not görüntüler, giriş almaz. readonly=true olan text türü için kısayol.    |
| geopoint                  | [Tek bir GPS koordinatı](#gps) toplayın.                                                     |
| geotrace                  | [İki veya daha fazla GPS koordinatından oluşan bir çizgi](#gps) kaydedin.                                                |
| geoshape                  | [Birden fazla GPS koordinatından oluşan bir poligon](#gps) kaydedin; son nokta ilk noktayla aynıdır. |
| date                      | Tarih girişi.                                                                                  |
| time                      | Saat girişi.                                                                                  |
| dateTime                  | Tarih ve saat girişi kabul eder.                                                             |
| image                     | Fotoğraf çekin veya bir [görüntü dosyası](#image) yükleyin.                                            |
| audio                     | Ses kaydı yapın veya ses dosyası yükleyin.                                             |
| background-audio          | Form doldurulurken arka planda ses kaydedilir.                                  |
| video                     | Video kaydı yapın veya video dosyası yükleyin.                                               |
| file                      | Genel dosya girişi (txt, pdf, xls, xlsx, doc, docx, rtf, zip)                                |
| barcode                   | Barkod tarayın; barkod tarayıcı uygulamasının yüklü olması gerekir.                            |
| calculate                 | Hesaplama yapın; aşağıdaki [Hesaplama](#calculation) bölümüne bakın.                    |
| acknowledge               | Seçildiğinde değeri "OK" olarak ayarlayan onay istemi.                                      |
| hidden                    | İlişkili UI öğesi olmayan ve sabit bir değeri depolamak için kullanılabilen alan                  |
| xml-external              | Bir [harici XML verisi](#external-xml-data) dosyasına referans ekler                         |

### Etiketler

Etiketler, her soru için katılımcılara görüntülenen metindir. Anketlerde net iletişim için kritik öneme sahiptirler.

- **Temel kullanım**: `label` sütununa soru metnini girin.
- **Birden fazla dil**: Çok dilli anketler için `label::English` ve `label::French` gibi ek sütunlar kullanın.
- **Biçimlendirme**: rtSurvey, etiketlerde vurgu veya yapı için temel HTML biçimlendirmesini destekler.

Örnek:
```
| type | name | label | label::French |
|------|------|-------|---------------|
| text | name | Adınız nedir? | Quel est votre nom? |
```

### İpuçları

İpuçları, ana soru metnini karmaşık hale getirmeden katılımcılara ek rehberlik sağlar.

- **Kullanım**: İpuçlarını `hint` sütununa ekleyin.
- **Görünürlük**: İpuçları genellikle ana soru metninin altında görüntülenir.
- **Çok dilli**: Etiketler gibi, ipuçları da `hint::Language` sütunları kullanılarak birden fazla dil için belirtilebilir.

Örnek:
```
| type | name | label | hint |
|------|------|-------|------|
| integer | age | Kaç yaşındasınız? | Lütfen yaşınızı yıl olarak girin |
```

### Görünüm

rtSurvey'deki `appearance` sütunu, soruların nasıl görüntüleneceğinin özelleştirilmesine olanak tanır.

- **Standart seçenekler**: Metin için 'multiline', seçme soruları için 'horizontal' dahildir.
- **rtSurvey uzantıları**:
  - Saat girişi: Çeşitli saat görüntüleme seçenekleri (örn. `inline`, `inline-1line`)
  - Renk özelleştirmesi: Simge renklerini değiştirmek için `colors()` fonksiyonunu kullanın

Örnek:
```
| type | name | label | appearance |
|------|------|-------|------------|
| text | time | Saati girin | inline-[%H:%M] |
```

### Relevant

`relevant` sütunu atlama mantığı uygular; bir sorunun ne zaman görüntülenmesi gerektiğini belirler.

- **Sözdizimi**: Koşulları tanımlamak için XPath ifadelerini kullanın.
- **Değişkenler**: Diğer soru adlarını `${question_name}` kullanarak referans alın.

Örnek:
```
| type | name | label | relevant |
|------|------|-------|----------|
| text | allergies | Alerjileri listeleyin | ${has_allergies} = 'yes' |
```

### Required

`required` sütunu, bir sorunun yanıtlanıp yanıtlanmaması gerektiğini belirtir.

- **Temel kullanım**: Bir soruyu zorunlu yapmak için 'yes' veya 'true' kullanın.
- **Gelişmiş**: Koşullu gereklilik için ifadeler kullanılabilir.

Örnek:
```
| type | name | label | required |
|------|------|-------|----------|
| text | email | E-posta adresi | yes |
```

### Tekrarlar

Tekrarlar, bir grup sorunun birden fazla kez yanıtlanmasına olanak tanır.

- **Kullanım**: Tekrarlayan bir grubu tanımlamak için `begin repeat` ve `end repeat` satırlarını kullanın.
- **Adlandırma**: Her tekrar grubuna benzersiz bir ad verin.

Örnek:
```
| type | name | label |
|------|------|-------|
| begin repeat | household_member | Hane üyesi |
| text | member_name | Ad |
| integer | member_age | Yaş |
| end repeat | | |
```

### Medya

rtSurvey anketlerde görüntüler, ses ve video dahil çeşitli medya türlerini destekler.

- **Soru türleri**: Tür sütununda 'image', 'audio' veya 'video' kullanın.
- **Etiketlerdeki medya**: HTML etiketleri kullanarak etiketlerdeki medya dosyalarına referans verin.

Örnek:
```
| type | name | label |
|------|------|-------|
| image | house_photo | Evin fotoğrafını çekin |
| note | | <img src="logo.jpg" /> Ankete hoş geldiniz |
```

### Salt Okunur

Salt okunur sorular, kullanıcı girişine izin vermeden bilgi görüntüler.

- **Kullanım**: `appearance` sütununa 'readonly' ekleyin.
- **Hesaplamalar**: Hesaplanan değerleri görüntülemek için genellikle calculate türüyle birlikte kullanılır.

Örnek:
```
| type | name | label | appearance | calculation |
|------|------|-------|------------|-------------|
| calculate | bmi | VKİ | readonly | ${weight} / (${height} * ${height}) |
```

## rtSurvey Uzantıları

rtSurvey, `grid layout`, `html format` ve birçok yeni `widget` gibi ek yetenekleri destekleyerek XLSForm standardını genişletir.

### Izgara düzeni
rtSurvey, formunuzun birden fazla soruyu tek bir satırda sıkıştırarak geleneksel kağıt anketlerin görünümünü taklit etmesine olanak tanır.

### Form ayarları

### Veri ayarları

### Typeform Stili

### pulldata() Uzantısı

### Görünüme dayalı uzantılar

### Webbox Uzantıları
