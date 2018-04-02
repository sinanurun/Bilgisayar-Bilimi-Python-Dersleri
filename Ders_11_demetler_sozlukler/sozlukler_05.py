yemekler = {"çorbalar":{"etli": ["işkembe", "kelle paça", "tavuk suyu"],
                         "etsiz": ["mercimek", "ezo gelin"],
                         "sebze": ["domates", "brokoli"]},
           "Kebaplar": {"acılı": ["adana", "beyti"],
                        "acısız": ["urfa","mardin"],
                        "dürümler":["ciger","adana"]}
            }
yemekler["çorbalar"]["etli"].append("kavurma")
#print(yemekler["Kebaplar"].keys())
#print(yemekler)
for a in yemekler:
    print(a)
    for b in yemekler[a]:
        print("\t",b)
        for c in yemekler[a][b]:
            print("\t"*2,c)
#del yemekler
yemekler.clear()
print(yemekler)
#print(yemekler["Kebaplar"])
#print(yemekler["Kebaplar"]["dürümler"])
#print(yemekler["Kebaplar"]["dürümler"][0])
