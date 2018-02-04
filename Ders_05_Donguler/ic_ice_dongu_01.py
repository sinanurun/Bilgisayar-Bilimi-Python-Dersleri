# Hem satır hem de sütun oluşturmak için :
sayi = int(input("Lütfen tablo ölçüsünü giriniz: "))
for satir in range(1, sayi + 1):
 for sutun in range(1, sayi + 1):
    deger = satir*sutun
    print("{0:3}".format(deger), end=" ")
 print()