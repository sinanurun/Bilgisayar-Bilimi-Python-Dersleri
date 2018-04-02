def faktoriyel(k):
    if k ==1:
        return 1
    else:
        return k*faktoriyel(k-1)

f = int(input("hesaplanacak değeri giriniz"))
print(faktoriyel(f))