a=[10,20,30,40]
b=a
print("a =",a)
print("b =",b)
b[2]=35
a[3]=45
print("a =",a)
print("b =",b)
print(id(a)) # bellek adresleri
print(id(b))