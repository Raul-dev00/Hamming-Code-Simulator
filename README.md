# Hamming-Code-Simulator
SEC ve DED özelliklerini destekleyen bir python uygulamasıdır.

## Özellikler 
- 8, 16, 32 bit desteği
- PyQt5 tabanlı ergonomik arayüz
- Gerçek zamanlı Hamming kodu oluşturma ve gösterme
- Hata simülasyonu ve sendrom hesaplama
- Detaylı sonuç raporlama (Before/After sendrom + hata analizi)

## Gereksinimler
- Python 3.x
- PyQt5

## Kurulum
- Projeyi bilgisayarınıza klonlayın veya indirin.
- Python 3.x kurulu olduğundan emin olun.
- Gerekli kütüphaneleri yükleyin:
- ``pip install PyQt5``

## Kullanım
- Kodu çalıştırın
-   ``python main.py``
- Arayüz
-  Giriş ekranında kullanılacak bit seçimini yapın (8, 16, 32)
-  Veri giriş alanına seçilen bit sayısı kadar bitlik binary sayı girin 
-  ``Find Check Bits`` butonuna tıklayarak parite bitlerini hesaplatın
-  ``Bring Memory`` ile oluşturulan Hamming kodunu görüntüleyin
-  **Memory** kısmında hatalı bit(leri) isteğe bağlı olarak değiştirebilirsiniz (manuel hata simülasyonu için)
-  ``Control`` butonuna basarak hataları tespit edin ve raporunu görüntüleyin

##Çıktılar
-  Program şu bilgileri sağlar:
-  Orijinal veri
-  Oluşturulan Hamming kodu (memory)
-  Parite bitleri (check bits)
-  Hata sonrası sendrom kelimesi
-  Before / After parite bilgileri
-  Hata analizi:
  -    **"Data has not changed"** → kontrol bitlerinde hata var, veri değişmemiş
  -    **"Data has changed"** → veri kısmında hata var ve düzeltildi
  -    **"Double Error Detected"** → çift hata algılandı
  -    **"Nothing has changed"** → hiç hata yok

##Teknik Detaylar
Hamming Kod Hesaplama
-  Parite bitleri 2^n pozisyonlarında yer alır:
-    8-bit : pozisyon 1, 2, 4, 8
-    16-bit : pozisyon 1, 2, 4, 8, 16
-    32-bit : pozisyon 1, 2, 4, 8, 16, 32
-  Parite bitleri, kapsadıkları veri bitlerinin XOR'u alınarak hesaplanır.
