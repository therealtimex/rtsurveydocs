---
weight: 150
date: "2023-05-03T22:37:22+01:00"
draft: false
author: "RealTimeX"
title: "Veri Toplama"
icon: "rocket_launch"
toc: true
description: "rtSurvey ile anket yürütmeye hızlı başlangıç kılavuzu"
publishdate: "2023-05-03T22:37:22+01:00"
tags: ["Beginners"]
---

Bir form dağıtıldıktan ve sayımcılar atandıktan sonra veri toplama başlayabilir. **rtSurvey**, ekibinizin bağlı olup olmadığına veya uzak, çevrimdışı ortamlarda çalışıp çalışmadığına bakılmaksızın esneklik sağlayarak hem web tarayıcıları hem de özel mobil uygulamalar aracılığıyla sorunsuz veri toplama destekler.

## Doğru Toplama Yöntemini Seçme

Projenizin coğrafyasına ve bağlantı durumuna bağlı olarak sayımcılarınız için en uygun yöntemi seçebilirsiniz:

- **Web Tarayıcısı (Çevrimiçi):** Çağrı merkezleri, ofis tabanlı veri girişi veya katılımcıların kendi kendine dolduracağı kamuya açık anketler için en iyisi.
- **rtWork / rtSurvey Mobil Uygulama (Çevrimiçi ve Çevrimdışı):** Saha operasyonları, kararsız internet bağlantısı olan uzak bölgeler ve medya ekleri gerektiren anketler (fotoğraflar, GPS koordinatları, çevrimdışı haritalar) için en iyisi.

---

## Yöntem 1: Web Tarayıcısı Aracılığıyla Veri Toplama

Web formu arayüzü, sayımcıların herhangi bir yazılım yüklemeden hemen veri toplamaya başlamasına olanak tanır.

### 1. Web Formu URL'sine Erişim
Kontrol Panelindeki **Form Yönetimi** panosundan hedef formunuzu bulun ve güvenli bir bağlantı oluşturmak için **Web Formu URL'si** düğmesine tıklayın.

### 2. Form Girişi
- Sağlanan URL'yi herhangi bir modern web tarayıcısında açın.
- Form kimlik doğrulama gerektiriyorsa sayımcının kimlik bilgileriyle oturum açması gerekir. "Genel Görünürlük" olarak ayarlandıysa doğrudan ilerleyebilir.
- Anket sorularını doldurun. Arayüz, mantığı, atlama desenlerini ve doğrulama kurallarını otomatik olarak uygulayacaktır.
- **Medya Yakalama:** Form görsel, ses veya video soruları içeriyorsa web tarayıcısı bilgisayarınızdan dosya yüklemenizi veya varsa cihazınızın web kamerası/mikrofonunu kullanmanızı isteyecektir.

### 3. Gönderim
Son sayfaya ulaştığınızda **Gönder**'e tıklayın. Tarayıcı, gönderimi tamamlamak için aktif bir internet bağlantısı gerektirir. Başarılı olduğunda veriler **Gönderim Yönetimi** arayüzüne anında yansıyacaktır.

---

## Yöntem 2: Mobil Uygulama Aracılığıyla Veri Toplama (Çevrimdışı)

Güçlü saha verisi toplama için mobil uygulamalar tam çevrimdışı özellikler sunar.

### 1. Yükleme ve Kimlik Doğrulama
- Google Play Store veya Apple App Store'dan **rtWork** (veya **rtSurvey**) uygulamasını indirin.
- Uygulamayı açın ve atanmış sayımcı kimlik bilgileriyle oturum açın.

### 2. Form İndirme (İnternet Gerektirir)
- Uygulamadaki **Formlar** veya **Görevler** bölümüne gidin.
- En son anket tasarımlarını sunucudan almak için **Senkronize Et** veya **İndir** simgesine dokunun. İndirildikten sonra formlar cihazda yerel olarak saklanır.

### 3. Veri Toplama (Çevrimdışı)
- İndirilen formu açın ve görüşmeye başlayın.
- Tamamen çevrimdışı veri toplayabilirsiniz.
- **Medya Yakalama:** Mobil uygulama, cihazınızın donanımıyla doğal olarak entegre olur. İnternet bağlantısı olmadan bile uygulama içinde doğrudan fotoğraf çekebilir, ses kaydedebilir, video çekebilir ve hassas GPS koordinatlarını kaydedebilirsiniz.
- Bir görüşmeyi bitirdiğinizde kaydı tamamlayın. Tamamlanan kayıtlar, uygulamanın giden kutusunda güvenle sıraya alınır.

### 4. Gönderimleri Senkronize Etme (İnternet Gerektirir)
- Sayımcı internet erişimi olan bir alana geri döndüğünde (Wi-Fi veya hücresel veri), **Giden Kutusu** veya **Senkronize Et** arayüzüne gitmesi gerekir.
- Uygulamaya tamamlanan formları göndermesini söyleyin. Uygulama sıradaki kayıtları ve tüm ekli medya dosyalarını güvenli bir şekilde sunucuya iletecek ve ardından gözden geçirmek için veri ızgarasında görüneceklerdir.
