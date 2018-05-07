from time import sleep, clock
baslangic = clock()
for sayac in range(10, -1, -1): # Range 10, 9, 8, ..., 0
    print(sayac) # Sayac yazdırılıyor
    sleep(1) # 1 saniye bekleme işlemi yapılıyor
print(clock()-baslangic)
"""
bu araya yorum yazılabilir
"""