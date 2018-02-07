def tree(yukseklik):
 satir=0 # Ağacın çizilmesine başlanıyor
 while satir<yukseklik: # Girilen yükseklik değerine kadar döngü kuruluyor
    sayac=0
    while sayac<yukseklik-satir:
        print(end=" ")
        sayac+=1
    sayac=0
    while sayac<2*satir+1:
        print(end="*")
        sayac+=1
    print()
    satir+=1
def main():
 yukseklik=int(input("Ağacın yüksekliğini giriniz: "))
 tree(yukseklik)
main()