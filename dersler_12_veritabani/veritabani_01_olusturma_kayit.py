# veritabanı oluşturmak
#sqlite3 modülünü dahil ediyoruz
import sqlite3 as sql

vt = sql.connect('kitaplik.sqlite') # bağlanacak olduğumuz veri tabanının adını yazıyoruz eğer sistemde adını yazdığımız veri tabanı yoksa yazılan adda bir veri tabanı oluşturuluyor

imlec = vt.cursor() # veri tabanı üzerinde işlem yapmak için imleç oluşturuyoruz

imlec.execute("CREATE TABLE IF NOT EXISTS kitap_bilgisi (kitap_adi,kitap_yazari,okunma_durumu,begeni)")


#kitap bilgisi adında içerisine bir tablşo oluşturuyoruz ilgili alanlar ile birlikte
# hata almamak için IF NOT EXISTS varlık kontrolü

kitap_girisi = "INSERT INTO kitap_bilgisi VALUES ('Suç ve Ceza', 'Dostoyevski', 'hayır','*****')"
#kitap_girisi_2="INSERT INTO kitap_bilgisi VALUES ('Beyaz Diş', 'Jack LONDON', 'evet','***')"
imlec.execute(kitap_girisi)
#imlec.execute(kitap_girisi_2)
imlec.execute("INSERT INTO kitap_bilgisi VALUES ('Beyaz Diş', 'Jack LONDON', 'evet','***')")

imlec.execute("INSERT INTO kitap_bilgisi VALUES ('Yunan Mitolojisi', 'Anna ve Louie', 'hayır','****')")

vt.commit() # veri tabanına hafızadaki bilgiyi kaydetmek için
vt.close() # veri tabanını kapatmak için
