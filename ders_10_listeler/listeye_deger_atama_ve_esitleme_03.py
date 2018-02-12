a=[10,20,30,40]
b=[10,20,30,40]
print(a,"değeri ",b," değerine eşit mi?",sep="",end=" ")
print(a==b)
print(a,"değeri ",b," değeri ile aynı mı?",sep="",end=" ")
print(a is b)
print(id(a)) # bellek adresleri
print(id(b))
c=[100,200,300,400]
d=c
print(c,"değeri ",d," değerine eşit mi?",sep="",end=" ")
print(c==d)
print(c,"değeri ",d," değeri ile aynı ma?",sep="",end=" ")
print(c is d)
print(id(c)) # bellek adresleri
print(id(d))