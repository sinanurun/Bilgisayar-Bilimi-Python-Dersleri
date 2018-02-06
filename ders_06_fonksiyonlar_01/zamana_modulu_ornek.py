from time import clock
print("Adınızı Giriniz: ", end="")
baslangicZamani = clock()
ad = input()
zaman = clock() - baslangicZamani
print(ad, "bilgilerinizi", zaman, "zamanda girdiniz")