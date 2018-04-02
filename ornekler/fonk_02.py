from math import pow,pi
# c_alan() fonkisyonu tanımlandı
def c_alan(r,*varint):
    alan = pow(r,2)*pi
#    print("2 birimlik çemberin alanı")
#    print(alan)
    return alan
# c_alan() fonkisyonu bitti

print(c_alan(5))