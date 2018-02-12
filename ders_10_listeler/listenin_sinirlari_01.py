# Değerleri 0 olan 100 elemanlı liste oluşturuluyor
v=[0]*100
x=int(input("Bir sayı giriniz: "))
# Girilen değer liste sınırları içerisinde mi?
if 0<=x<len(v):
    v[x]=1 # Girilen indis değeri 1 olarak değiştiriliyor
else:
    print("Girdiğiniz değer liste sınırları arasında değil")
print(v)