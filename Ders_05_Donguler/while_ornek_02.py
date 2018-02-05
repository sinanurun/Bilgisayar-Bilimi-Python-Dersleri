sayi = 0
toplam = 0
print("Bir sayı giriniz, negatif sayı döngüyü sonlandırır : ")
while sayi >= 0:
    sayi= int(input())  # kullanıcının sayı girmesi sağlandı
    toplam += sayi      # toplam = toplam + sayı    girilen sayılar toplandı
print("Toplam=", toplam)