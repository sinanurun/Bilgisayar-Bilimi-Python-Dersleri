from Kontrol import AsalKontrol
# Kontrol dosyasındaki AsalKontrol fonksiyonu programa ekleniyor
sayi = int(input("Bir sayı giriniz.: "))
if AsalKontrol(sayi):
 print(sayi, "ASAL")
else:
 print(sayi, "ASAL değil")