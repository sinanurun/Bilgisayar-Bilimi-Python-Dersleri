# Girilen değere göre "*" karakterinden ağaç çizen program
yukseklik = int(input("Çizilecek ağaçın yüksekliğini giriniz: "))
satir = 0
while satir < yukseklik:
    sayac = 0
    while sayac < yukseklik - satir:
        print(end=" ")
        sayac += 1
    sayac = 0
    while sayac < 2*satir + 1:
        print(end="*")
        sayac += 1
    print()
    satir += 1