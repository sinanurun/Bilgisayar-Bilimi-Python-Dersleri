# 10.000"e kadar olan asal sayıların adetini ve geçen zamanı bulan program
from time import clock
sonDeger = 10000
sayac = 0
zaman = clock() # Süre başlatılıyor
# En küçük asal sayı olan 2 den istenilen değere kadar döngü kuruluyor
for deger in range(2, sonDeger + 1): # Sırayla sayılar ele alınıyor
    kontrol = True  # Değerlerin kontrol edilmesi için ilk değer True veriliyor
# Asal olma özelliğinin kontrolü için bölenlerinin döngüsü kuruluyor
    for bolenSayi in range(2, deger):
        if deger % bolenSayi == 0:
            kontrol = False  # Tam bölme işlemi oluştuysa kontrol False yapılıyor
            break  # ve döngü sonlandırılıyor
    if kontrol:
        sayac += 1  # Asal olma özelliği sağlanmışsa sayac arttırılıyor
print()  # Yeni satır başı
gecenZaman = clock() - zaman  # İşlem tamamlandıktan sonra süre sonlandırılıyor
print("Adet:", sayac, " Geçen Zaman:", gecenZaman, " saniye")