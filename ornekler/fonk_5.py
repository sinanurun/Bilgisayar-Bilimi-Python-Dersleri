def faktoriyel(k):
    hesap=1
    for a in range (1,k+1):
        hesap=hesap*a
    return hesap
f = int(input("hesaplanacak değeri giriniz"))
print(faktoriyel(f))