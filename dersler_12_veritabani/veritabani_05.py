import sqlite3 as sql
vt = sql.connect('kitaplik.sqlite')
imlec = vt.cursor()
imlec.execute("CREATE TABLE IF NOT EXISTS kitap_bilgisi(kitap_adi,kitap_yazari,okunma_durumu,begeni)")
def ekle(kitap_adi="",kitap_yazari="",okunma_durumu="",begeni=""):
    print(kitap_adi,kitap_yazari,okunma_durumu,begeni)
    kitap_girisi = "INSERT INTO kitap_bilgisi VALUES ('"+kitap_adi+"','"+kitap_yazari+"','"+okunma_durumu+"','"+begeni+"')"
    print(kitap_girisi)
    imlec.execute(kitap_girisi)
    vt.commit()
def listele():
    imlec.execute("SELECT * FROM kitap_bilgisi")
    kitaplar = imlec.fetchall()
    print(kitaplar)
    for i in kitaplar:
        for k in i:
            print(k, end=" ")
        print("")



    vt.close()