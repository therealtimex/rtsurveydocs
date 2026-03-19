---
title: "Görsel"
description: "Görsel soruları, katılımcıların anketin bir parçası olarak fotoğraf çekmesine ve göndermesine olanak tanır."
icon: "image"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 227
---

XLSForm'larda ve rtSurvey'de görsel soru türü, katılımcıların anket yanıtlarının bir parçası olarak fotoğraf çekmesine ve göndermesine olanak tanır. Bu özellik, görsel veri toplamak, gözlemleri belgelemek veya saha anketlerinde kanıt sağlamak için özellikle kullanışlıdır.

## Temel XLSForm Tanımı

| type  | name        | label                           |
|-------|-------------|--------------------------------|
| image | photo       | Konumun fotoğrafını çekin       |

Temel görsel soru türü hakkında daha fazla ayrıntı için [XLSForm spesifikasyonuna](https://xlsform.org/en/#question-types) bakın.

## Kullanım Alanları

Görsel sorular yaygın olarak şunlar için kullanılır:

1. Saha koşullarını veya gözlemleri belgeleme
2. Araştırma çalışmalarında görsel kanıt yakalama
3. Etki değerlendirmelerinde önce/sonra fotoğrafları toplama
4. Görev tamamlanmasını veya konumda bulunmayı doğrulama
5. Uzaktan analiz için görsel veri toplama

## En İyi Uygulamalar

1. Neyin fotoğraflanması gerektiğine dair net talimatlar verin.
2. Gizlilik etkilerini göz önünde bulundurun ve katılımcıları fotoğraflarının nasıl kullanılacağı konusunda bilgilendirin.
3. Özellikle sınırlı internet bağlantısı olan bölgelerdeki anketler için dosya boyutlarına ve depolama sınırlamalarına dikkat edin.
4. Cihazın yeterli depolama alanına sahip olduğundan ve kamera izinlerinin verildiğinden emin olun.

## Örnek Kullanım

Bir ankette görsel sorusunu nasıl kullanabileceğinize dair bir örnek:

| type  | name           | label                                      | hint                                        |
|-------|----------------|--------------------------------------------|--------------------------------------------|
| image | storefront     | Mağazanın girişinin fotoğrafını çekin      | Mağaza adının açıkça görünür olduğundan emin olun |

## rtSurvey Uzantıları

XLSForm için temel görsel soru tanımı basit olmakla birlikte, rtSurvey ek özellikler veya özelleştirmeler sunabilir:

1. Görsel kalite ayarları (örn. düşük, orta, yüksek çözünürlük)
2. Görsellere altyazı veya etiket ekleme seçeneği
3. Tek bir soru için çoklu görsel yakalama
4. Cihazın yerel kamera uygulaması veya galeriyle entegrasyon

## Veri İşleme

Bu soru türü aracılığıyla toplanan görseller genellikle:

1. Yaygın bir görsel biçimde kaydedilir (örn. JPG, PNG)
2. Diğer anket verileriyle birlikte, genellikle ayrı bir medya klasöründe saklanır
3. Anket yönetim platformu aracılığıyla görüntüleme ve analiz için erişilebilir

## Analiz için Değerlendirmeler

Görsel soruları kullanırken şunları göz önünde bulundurun:

1. Görsellerin nasıl analiz edileceği (örn. manuel inceleme, otomatik görüntü analizi)
2. Görüntü dosyaları için gereken ek depolama alanı
3. Fotoğraf saklama ve işleme için gizlilik ve veri koruma önlemleri
4. Analiz aşamasında görüntü düzenleme veya düzenleme araçlarına potansiyel ihtiyaç

## Sınırlamalar

- Görüntü dosyaları büyük olabilir ve bu veri aktarımını ve depolamayı etkileyebilir.
- Tüm cihazlar yüksek kaliteli kameralara veya yeterli depolama alanına sahip olmayabilir.
- Çok sayıda görsel analiz etmek zaman alıcı olabilir.
- Özellikle kamusal alanlarda görsel yakalanırken gizlilik endişeleri olabilir.
