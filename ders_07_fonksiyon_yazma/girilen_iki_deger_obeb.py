def gcd(sayi1,sayi2):# sayi1 değeri s1, sayi2 değeri s2
 min=sayi1 if sayi1<sayi2 else sayi2
 ebop=1
 for i in range(1,min+1):
    if sayi1 % i== 0 and sayi2 % i== 0:
        ebop=i # En büyük ortak bölen aktarılıyor
 return ebop
def SayiGir():
 return int(input("Lütfen bir sayı giriniz : "))
def main():
 s1=SayiGir()
 s2=SayiGir()
 print("gcd(",s1, ",",s2, ") = ",gcd(s1,s2),sep="")
main()