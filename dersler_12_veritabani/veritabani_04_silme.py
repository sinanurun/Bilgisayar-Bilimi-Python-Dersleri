import os
import sqlite3 as sql
veritabani = 'kitaplik.sqlite'
dosya_mevcut = os.path.exists(veritabani)

vt = sql.connect(veritabani)
imlec = vt.cursor()
imlec.execute("DELETE FROM kitap_bilgisi WHERE okunma_durumu='hayır'")
vt.commit()
imlec.execute("SELECT * FROM kitap_bilgisi")
kitaplar = imlec.fetchall()
print(kitaplar)
for i in kitaplar:
    for k in i:
        print(k,end=" ")
    print("")
vt.commit()
vt.close()