import struct
d1 = 1.11 - 1.10
d2 = 2.11 - 2.10
print("d1 =", d1, " d2 =", d2)
if d1 == d2:
    print("Aynı")
else:
    print("Farklı")
    print(d1,d2)

    #print("binary", bin(d1))
d3 = 25-10
d4 = 55-40
print("d3 =", d3, " d4 =", d4)
if d3 == d4:
    print("Aynı")
else:
    print("Farklı")

#neden farklı ?
print(d1-d2)
print(id(d1))
print(id(d2))
print(id(d3))
print(id(d4))
