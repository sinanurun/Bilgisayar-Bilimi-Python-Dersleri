from math import sqrt
sonDeger = int(input("Hangi sayıya kadar asal sayılar listelensin?"))
deger = 2 # En küçük asal sayı
while deger <= sonDeger: # İstenilen değere kadar dönmesi için döngü kuruluyor
    kontrol = True # Başlangıç aşamasında kontrol değişkeni True olarak belirlenir
# 2 ile -1 arasındaki tüm değerlerin kontrolünün yapılması
    geciciDeger= 2
    kok = sqrt(deger) # Döngüde sırası gelen değerin karakökü hesaplanıyor
    while geciciDeger <= kok:
        if deger % geciciDeger == 0:
            kontrol = False # Asal sayı özelliği yitiriliyor ve kontrol False oluyor
            break # Kontrol döngüsünden çıkılıyor.
        geciciDeger += 1 # Bir sonraki kontrol sayısına geçiş
    if kontrol:
            print(deger, end= " ") # Şarta uyan değer Asal olarak kabul edilip yazdırılıyor.
    deger += 1 # Asal sayı kontrolü için sonraki sayı
print() # Kursor bir sonraki satıra alınıyor
