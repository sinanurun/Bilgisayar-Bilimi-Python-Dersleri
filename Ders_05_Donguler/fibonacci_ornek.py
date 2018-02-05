# İstenilen sayıdaki Fibonacci Sayılarını Listeleyen Program
deger1=0
deger2=1
sayac=2
sonDeger=int(input("Listelemek istediğiniz Fibonacci Sayıları adetini giriniz..:"))
print(str(deger1) + " " +str(deger2),end=" ")
while sayac<=sonDeger:
    deger3=deger1+deger2
    print(deger3,end=" ")
    deger1=deger2
    deger2=deger3
    sayac+=1