# Kullanıcıdan alınan sayılardan liste oluşturan program
def ListeOlustur():
 sonuc = [] # sonuc adında bir liste oluşuturuldu
 girilenSayi = 0
 while girilenSayi >= 0:
    girilenSayi= int(input("Sayı giriniz ( Çıkış için -1): "))
    if girilenSayi>= 0:
        sonuc += [girilenSayi]
 return sonuc
def main():
 sutun = ListeOlustur()
 print(sutun)
main()