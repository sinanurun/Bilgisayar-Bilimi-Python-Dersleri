import Kontrol
sayi = int(input("Bir sayı giriniz.: "))
if Kontrol.AsalKontrol(sayi):
    print(sayi, "sayısı ASAL sayıdır.") #num değil
else:
    print(sayi, "sayı ASAL değildir.")