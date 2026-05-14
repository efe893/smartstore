#  SmartStore - Modüler Python Mağaza Otomasyonu

##  Proje Hakkında
SmartStore; kullanıcıların kayıt olabildiği, giriş yaparak mağazadaki ürünleri görüntüleyebildiği ve stok kontrolü eşliğinde alışveriş yapabildiği bir yazılımdır. [cite_start]Yazılımın temel amacı, teorik OOP bilgilerini (Kalıtım, Kapsülleme vb.) pratik bir yazılım ürününe dönüştürmektir[cite: 4, 5, 20].

##  Kullanılan Teknolojiler
* [cite_start]**Programlama Dili:** Python [cite: 14]
* **Arayüz Kütüphanesi:** PyQt5
* [cite_start]**Yazılım Mimarisi:** Nesne Tabanlı Programlama (OOP) ve Modüler Yapı [cite: 18, 20]

##  Modüler Yapı ve OOP Özellikleri
[cite_start]Proje, "spaghetti code" karmaşasından kaçınmak için 3 ana modüle ayrılmıştır[cite: 15, 18, 19]:

1. **`urun_modulu.py`:**
   - `Urun` ve `Magaza` sınıflarını içerir.
   - **Kapsülleme (Encapsulation):** `@property` ve `@setter` dekoratörleri kullanılarak fiyat ve stok verileri korunmuştur. Negatif değer girişleri engellenmiştir.

2. **`kullanici_modulu.py`:**
   - `Kullanici` ve `Musteri` sınıflarını içerir.
   - **Kalıtım (Inheritance):** `Musteri` sınıfı, `Kullanici` sınıfından miras alır ve `super()` metodu ile üst sınıfın özelliklerini devralır.

3. **`main_gui.py`:**
   - [cite_start]Yazılımın ana çalışma dosyasıdır (Main file)[cite: 19].
   - Diğer modülleri içe aktararak (import) PyQt5 arayüzü ile kullanıcı etkileşimini yönetir.

##  Kurulum ve Çalıştırma
Projenin çalıştırılabilmesi için bilgisayarınızda Python yüklü olmalıdır.

1. Gerekli kütüphaneyi kurun:
   ```bash
   pip install PyQt5
