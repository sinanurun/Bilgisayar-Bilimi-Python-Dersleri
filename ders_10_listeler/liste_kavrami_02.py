def main():
 toplam=0.0
 girilecekSayıAdeti=5
 print("Lütfen ",girilecekSayıAdeti, " adet sayı giriniz: ")
 for i in range(0, girilecekSayıAdeti):
    sayi=float(input("Lütfen " +str(i+1)+ ". sayıyı giriniz: "))
    toplam+=sayi
 print("Ortalama :",toplam/girilecekSayıAdeti)
 print(sayi)
main()