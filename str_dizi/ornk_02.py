soz = "hayatta en hakiki mürşit ilimdir"
kelime = "denemea"
kgiris=input("bir harf giriniz")
deger = 0
for harf in soz:
    if kgiris == harf:
        deger+=1
print(deger)
tane = soz.count(kgiris)
print(tane)
