from math import pow,pi
# c_alan() fonkisyonu tanımlandı
#ön tanımlı parametre kullanımı örneği
def c_alan(r=10,*varint):
    alan = pow(r,2)*pi
#    print("2 birimlik çemberin alanı")
#    print(alan)
    return alan
# c_alan() fonkisyonu bitti
#parametre girsekte girmesekte çalışıyor
print(c_alan())