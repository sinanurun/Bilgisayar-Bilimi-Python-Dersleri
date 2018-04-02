# Girilen 5 sayının ortalamasını alan program
# Negatif sayı girildiğinde program sonlandırılır
sayac = toplam = 0
print("Lütfen Ortalama hesaplamak için 5 pozitif sayı giriniz")
while sayac < 5:
    sayi = float(input("Sayı giriniz: "))
    if sayi < 0:
        print("Negatif sayılar kabul edilmemektedir. Çıkılıyor")
        break

    sayac += 1
    toplam += sayi
else:
    print("Ortalama =", toplam/sayac)