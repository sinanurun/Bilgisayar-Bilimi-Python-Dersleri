from time import clock
toplam = 0 # Toplam değişkeni tanımlanıp ilk değer olarak 0 veriliyor
basla = clock() # İşlem süresinin hesaplanması için süre başlatılıyor
for n in range(1, 1000001): # Toplamı alınacak sayılar için 1.000.000’e kadar döngü kuruluyor
 toplam += n #toplam = toplam + n
gecenZaman = clock() - basla # Geçen zaman hesaplanıyor
print("Toplam:", toplam, "Geçen Süre:", gecenZaman) # Sonuçlar  yazdırılıyor