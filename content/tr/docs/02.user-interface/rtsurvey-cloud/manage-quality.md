---
title: "Kalite Yönetimi"
description: "Veri toplama ilerlemesini izleyin, görüşme haritalarını görüntüleyin ve sayımcı performansını analiz edin."
icon: "cloud"
date: "2023-05-22T00:34:57+01:00"
lastmod: "2023-05-22T00:34:57+01:00"
draft: false
weight: 316
---

**Kalite Yönetimi** modülü (Gösterge Paneli aracılığıyla erişilebilir), veri toplama ilerlemesini ve sayımcı performansını izlemek için gerçek zamanlı analitik ve mekansal görselleştirmeler sağlar. Proje yöneticilerine bireysel anket formları ve özelleştirilmiş analitik raporlar arasında hızla geçiş yapabilecekleri bölünmüş görünüm bir arayüz sunar.

![Kalite Yönetimi Gösterge Paneli](/images/manage_quality.png)

## Gösterge Paneli Genel Bakışı

Kalite Yönetimi gösterge paneli iki birincil navigasyon sekmesine ayrılmıştır: **Formlar** ve **Raporlar**. Bu yan menü, kullanıcıların analiz etmek istedikleri belirli veri kümesini veya raporu verimli biçimde aramasına ve seçmesine olanak tanır.

### Form Analizi

Listeden belirli bir form seçildiğinde gösterge paneli, gönderim kalitesini ve sıklığını izlemek için birden fazla yerleşik görselleştirme aracı sağlar:

- **Başlangıç saatine göre sayım:** Bir zaman çizelgesi üzerinde başlatılan görüşmelerin sıklığını görselleştiren çubuk grafik.
- **Bitiş saatine göre sayım:** Görüşmelerin ne zaman tamamlandığını görselleştiren çubuk grafik.
- **Gönderim tarihine göre sayım:** Sunucuyla senkronize edilen günlük veri hacmini takip eder.
- **Kullanıcı adına göre sayım:** Toplam gönderim sayılarına göre en iyi performans gösteren sayımcıları belirleyen çubuk grafik.
- **Görüşmelerin haritası:** Her gönderimin gerçekleştiği GPS koordinatlarını görüntüleyen coğrafi dağılım grafiği (Leaflet tarafından desteklenir); yöneticilerin saha çalışması konumlarını doğrulamasına olanak tanır.

### Özel Raporlar

**Raporlar** sekmesi, önceden yapılandırılmış R Markdown analitik tasarımlarına ve diğer özelleştirilmiş istatistiklere erişim sağlar. Bir rapor seçildiğinde ana görünüm alanı, toplanan verilerin daha derin istatistiksel doğrulamasını sağlayan yerleşik bir görüntüleyici aracılığıyla oluşturulan analizi dinamik olarak yükler.

## Arama ve Filtreleme

Kenar çubuğu listesinin üzerinde hızlı arama çubuğu mevcuttur; kullanıcıların belirli form veya raporları ada göre hızla bulmasına olanak tanır.
