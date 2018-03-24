class kedi():
    kuyruk="kuyruklu"
    ayak ="4"
    kulak="2"
    ses ="miyav"
    print("Bir kedi oluşturdunuz")
    def zipla(self):
        print("50 cm zıpladı")
    def ses_ciarkt(self):
        print(self.ses)

boncuk = kedi()
print(boncuk.kuyruk)
print(boncuk.ayak)
boncuk.ses_ciarkt()
boncuk.zipla()
boncuk.zipla()

findik = kedi()
print(findik.kuyruk)
findik.ses_ciarkt()
findik.zipla()