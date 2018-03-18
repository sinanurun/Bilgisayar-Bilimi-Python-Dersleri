import sqlite3 as sql
vt = sql.connect('kitaplik_db.sqlite')
imlec = vt.cursor()

def ekle(kitap_adi="",kitap_yazari="",okunma_durumu="",begeni=""):
    imlec.execute(
        "CREATE TABLE IF NOT EXISTS kitaplik_tb (kitap_id INTEGER PRIMARY KEY  AUTOINCREMENT, kitap_adi,kitap_yazari,okunma_durumu,begeni)")
#    print(kitap_adi,kitap_yazari,okunma_durumu,begeni)
    kitap_girisi = "INSERT INTO kitaplik_tb (kitap_adi,kitap_yazari,okunma_durumu,begeni) VALUES ('"+kitap_adi+"','"+kitap_yazari+"','"+okunma_durumu+"','"+begeni+"')"
#    print(kitap_girisi)
    imlec.execute(kitap_girisi)
    vt.commit()
def listele():
    imlec.execute("SELECT * FROM kitaplik_tb")
    kitaplar = imlec.fetchall()
#    print(kitaplar)
    for i in kitaplar:
        for k in i:
            print(k, end=" ")
        print("")

def guncelle(guncellenecek):
    gkitap = input("Güncel kitap adını giriniz")
    gyazar = input("Güncel kitap yazarını")
    gokunma = input("Güncel kitap okunma durumunu giriniz")
    gbegeni = input("Güncel kitap beğeni değerini giriniz")
    guncelleme_kodu = "UPDATE kitaplik_tb SET kitap_adi='"+gkitap+"',kitap_yazari='"+gyazar+"',okunma_durumu='"+gokunma+"',begeni='"+gbegeni+"' WHERE kitap_id = '"+guncellenecek+"'"
    imlec.execute(guncelleme_kodu)
    vt.commit()
def sil(silinecek):
    silme_kodu="DELETE FROM kitaplik_tb WHERE kitap_id='"+silinecek+"'"
    imlec.execute(silme_kodu)
    vt.commit()
def cikis():
    vt.close()
    print("Çıkış Yapıldı İyi Günler")