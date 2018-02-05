sonDeger = int(input("Kaça kadar asal sayıları görmek istersiniz? "))
sayi = 2
while sayi <= sonDeger:
    kontrol = True
    gecici = 2
    while gecici < sayi:
        if sayi % gecici == 0:
            kontrol = False
            break
        gecici += 1
    if kontrol:
        print(sayi, end= " ")
    sayi += 1
print()