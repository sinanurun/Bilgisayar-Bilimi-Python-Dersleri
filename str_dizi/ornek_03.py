site1 = "www.google.com"
site2 = "www.istihza.com"
site3 = "www.yahoo.com"
deger = d = 0
for isim in site1, 125, site3:
    print(isim)
    #d+=isim.count("w")
    for harf in isim:
        if harf == "o":
            deger+=1
print(deger)