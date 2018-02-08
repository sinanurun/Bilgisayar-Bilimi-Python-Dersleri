# Kullanıcı seçimine göre Toplama ve Çıkarma işlemi yapan program kodları
def Yardim():
 print("Topla : Girilen iki sayıyı toplar")
 print("Fark Al : Girilen iki sayının farkını alır")
 print("Yazdır : İşlem yapılan en son değeri ekrana yazdırır")
 print("Yardım : Bu ekranı görüntüler")
 print("Çıkış : Programdan çıkışı sağlar")
def Menu():
 return input("=== (T)opla (F)ark Al (Y)azdır Y(A)rdım (Ç)ıkış ===")
# Programda kullanılmak üzere global değişken tanımlanması
sonuc = 0.0
sayi1 = 0.0
sayi2 = 0.0
def SayiGir():
 global sayi1, sayi2 # sayi1 ve sayi2 nin global değişken olarak bildirilmesi
 sayi1 = float(input("Sayı Giriniz #1: "))
 sayi2 = float(input("Sayı Giriniz #2: "))
def Yazdir():
 print(sonuc)
def Topla():
    global sonuc
    sonuc = sayi1 + sayi2
def FarkAl():
    global sonuc
    sonuc = sayi1 - sayi2
def main():
    durum = False
    while not durum:
        secim = Menu()  # İşlem yapılacak Menü Tasarımı
        if secim == "T" or secim == "t":  # Toplama
            SayiGir()
            Topla()
            Yazdir()
        elif secim == "F" or secim == "f":  # Çıkarma
            SayiGir()
            FarkAl()
            Yazdir()
        elif secim == "Y" or secim == "y":  # Yazdırma
            Yazdir()
        elif secim == "A" or secim == "a":  # Yardım
            Yardim()
        elif secim == "Ç" or secim == "ç":  # Çıkış
            durum = True
main()