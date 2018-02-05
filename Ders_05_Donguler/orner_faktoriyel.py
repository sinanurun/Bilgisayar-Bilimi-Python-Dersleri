# Program girilen sayının faktöriyelini hesaplar
faktoriyel=1
sayac=1
sayi=int(input("Lütfen bir sayı giriniz.."))
while sayac<=sayi:
    faktoriyel*=sayac # faktoriyel = faktoriyel * sayac
    print(sayac,"=>",faktoriyel)
    sayac+=1
print(sayi," sayısının foktöriyeli:",faktoriyel)