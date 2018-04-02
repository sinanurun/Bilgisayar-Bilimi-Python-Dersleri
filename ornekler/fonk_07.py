def toplama(k):
    girilen = int(input("bir sayı giriniz"))
    if k == 1:
        return girilen
    else:
        return girilen+toplama(k-1)
adet = int(input("kaç tane sayı toplansın"))
print(toplama(adet))