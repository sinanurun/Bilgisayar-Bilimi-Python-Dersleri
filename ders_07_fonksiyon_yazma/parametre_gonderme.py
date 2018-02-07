def artir(x):
 print("Değişkenin artırılması yapılıyor, x =",x)
 x+=1
 print("Artırma sonucu değer, x =",x)
 return x
def main():
 x=5
 artir(x)
 print("Artırma sonrası, x =",x)
 print("Artırma sonrası, x =",artir())
 #print("Artırma sonrası, x =", artir(x))
main()