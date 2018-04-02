# veritabanı oluşturmak
#sqlite3 modülünü dahil ediyoruz
import sqlite3 as sql

vt = sql.connect('kitaplik.sqlite') # bağlanacak olduğumuz veri tabanının adını yazıyoruz eğer sistemde adını yazdığımız veri tabanı yoksa yazılan adda bir veri tabanı oluşturuluyor

imlec = vt.cursor() # veri tabanı üzerinde işlem yapmak için imleç oluşturuyoruz
try:
    imlec.execute("CREATE TABLE kitap_bilgisi (kitap_adi,kitap_yazari,okunma_durumu,begeni)")
except:
    print("veri tabanı tablo oluşturma hatası")
