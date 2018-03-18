import sys
import veritabani_06 as baglanti

print("-"*56)
print("-"*10, "Kitaplık Programımıza Hoş Geldiniz", "-"*10)
print("-"*56)
while 1 == 1:
    print("-"*10, "Yapmak istediğiniz işlemi Seçiniz", "-"*10)
    print("-" * 10, "(E)klemek,(L)istelemek,(G)üncellemek,(S)ilmek,(Ç)ıkmak", "-" * 10)
    islem = input()
    if islem == "Ç" or islem == "ç":
        baglanti.cikis()
        sys.exit()
    elif islem == "E" or islem == "e":
        kitap = input("kitap adını giriniz")
        yazar = input("kitap yazarını")
        okunma = input("kitap okunma durumunu giriniz")
        begeni = input("kitap beğeni değerini giriniz")
        baglanti.ekle(kitap, yazar, okunma, begeni)
    elif islem == "L" or islem == "l":
        baglanti.listele()
    elif islem == "G" or islem == "g":
        baglanti.listele()
        guncellenecek = input("güncellemek istediğiniz kitabın id'sini giriniz")
        baglanti.guncelle(guncellenecek)
    elif islem == "S" or islem == "s":
        baglanti.listele()
        silinecek = input("silmek istediğiniz kitabın id'sini giriniz")
        baglanti.sil(silinecek)