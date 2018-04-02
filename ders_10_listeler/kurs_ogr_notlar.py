ogrenci1=list(range(0,3))
ogrenci2=list(range(0,3))
ogrenci3=list(range(0,3))
listem = [ogrenci1,ogrenci2,ogrenci3]
#d=0
for i in listem:
#    d += 1
    for k in range(3):
#        print("{}. Öğrencinin {}. Notunu Gir :\t".format(d,k+1), end="")
        i[k]=input()
print(listem)
