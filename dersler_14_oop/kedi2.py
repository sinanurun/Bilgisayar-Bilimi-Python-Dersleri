class kedi2():
    ayak = 4
    kuyruk = "var"
    sesi = "miyav "
    def ses_cikart(self):
        ses = self.sesi
        print(ses*2)
    def zipla(self):
        print("kedi zıpladı")

cingoz = kedi2()
print("cingoz ayak sayısı",cingoz.ayak)
cingoz.ses_cikart()
boncuk = kedi2()
boncuk.ayak=5
print("boncuk ayak sayısı",boncuk.ayak)
print(boncuk.ayak,cingoz.ayak)
