# PAX Veri Ayıklayıcı (Regex Extractor)

Bu proje, karmaşık metin dosyaları (`.txt`) içerisinden belirli bir düzene (pattern) sahip verileri ayıklayarak, aradaki gereksiz metinleri filtreleyen basit ve etkili bir Python betiğidir.

## 🚀 Proje Ne İşe Yarar?
Eğer elinizde uzun ve karmaşık cümleler içeren metinler varsa ve bu metinlerin içinden:
1. Sadece `PAX` kelimesi ile başlayan ve ardından 9 adet rakam gelen kodları,
2. Ve bu koda bağlı **BÜYÜK HARFLE** yazılmış özel isimleri çekmek istiyorsanız bu kodu kullanabilirsiniz.

**Önemli:** Proje, kodu ve büyük harfli ismi eşleştirirken aradaki gereksiz küçük harfli kelimeleri otomatik olarak filtreler ve temiz bir çıktı sunar. (Regex Gruplama yöntemi kullanılmıştır.)

## 🛠 Kullanılan Teknolojiler
* Python 3.x
* Regex (`re` kütüphanesi)

## 📂 Nasıl Kullanılır?

1. Projeyi bilgisayarınıza indirin.
2. Ayıklama yapmak istediğiniz metni `testing.txt` dosyasının içerisine yapıştırın.
3. Terminal veya komut satırında kodun bulunduğu dizine gidin ve şu komutu çalıştırın:

```bash
python main.py

