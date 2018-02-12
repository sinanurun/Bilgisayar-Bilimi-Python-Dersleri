def ListeKopyala(lst):
 result=[]
 for item in lst:
    result+=[item]
 return result
def main():
 a=[10,20,30,40]
 b=ListeKopyala(a) # b sıfırdan türetiliyor a listesinden türetilmiyor yani a!=b oluyor
 print("a =",a, " b =",b)
 print(a, "listesi ile ",b, "listesi değerleri eşit mi?",sep="",end="")
 print(a==b)
 print(a, " ile ",b, " listeleri aynı mı?",sep="",end="")
 print(a is b)
 b[2]=35
 print("a =",a, " b =",b)
 print(id(a))  # bellek adresleri
 print(id(b))
main()