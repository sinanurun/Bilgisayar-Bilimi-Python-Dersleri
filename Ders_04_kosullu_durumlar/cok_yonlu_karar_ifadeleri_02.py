# Klavyeden girilen 0-5 arasındaki sayıların yazı karşılığını veren
# program else ile if => elif
deger = int(input("Lütfen 0 – 5 arasında bir değer girin: "))
if deger < 0:
    print("çok küçük")
elif deger == 0:
    print("sıfır")
elif deger == 1:
    print("bir")
elif deger == 2:
    print("iki")
elif deger == 3:
    print("üç")
elif deger == 4:
    print("dört")
elif deger == 5:
    print("beş")
else:
    print("çok büyük")
print("Tamamlandı")