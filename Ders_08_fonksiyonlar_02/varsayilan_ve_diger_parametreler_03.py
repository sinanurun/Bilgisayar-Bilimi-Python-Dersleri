def AralikTopla(n , m = 55): # Tek değer varsayılan atama
    toplam = 0
    for deger in range(n, m + 1):
        toplam += deger
    print(toplam)
# m değeri verilemediği için hata ile karşılaşılır
AralikTopla(5)