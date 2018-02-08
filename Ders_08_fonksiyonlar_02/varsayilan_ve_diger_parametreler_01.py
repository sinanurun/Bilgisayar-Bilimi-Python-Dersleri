def AralikTopla(n, m=100): # Tek değer varsayılan atama
    toplam = 0
    for deger in range(n, m + 1):
        toplam += deger
    print(toplam)
AralikTopla(6,10)