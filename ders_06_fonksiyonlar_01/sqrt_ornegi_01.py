from math import sqrt
# Kullanıcıdan değer alınıyor
sayi = float(input("Sayı Giriniz: "))
# Karakök hesaplanarak kok değişkenine aktarılıyor
kok = sqrt(sayi) # kok değişkenine sqrt fonksiyonunun sonucu aktarılmış
print(sqrt(sayi))
# Sonuçlar yazdırılıyor
print(sayi," sayısının karekökü" "=", kok)