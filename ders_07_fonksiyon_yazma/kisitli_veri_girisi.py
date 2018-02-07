def arasındami(ilk,son):
 if ilk>son:
    ilk,son=son,ilk
 deger=int(input("Lütfen belirtilen aralıkta bir değer girin "+str(ilk)+ "..." +str(son)+ ": "))
 while deger<ilk or deger>son:
    print(deger, "Bu değerler arasında değil",ilk, "...",son)
    deger=int(input("Tekrar deneyin: "))
 return deger
def main():
 print(arasındami(10,20))
 print(arasındami(20,10))
 print(arasındami(5,8))
 print(arasındami(-100,100))
main()