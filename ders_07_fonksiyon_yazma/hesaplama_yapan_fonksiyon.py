def yardim():
 print("Topla : Girilen iki sayıyı toplar")
 print("Fark Al : Girilen iki sayının farkını alır")
 print("Yazdır : İşlem yapılan en son değeri ekrana yazdırır")
 print("Yardım : Bu ekranı görüntüler")
 print("Çıkış : Programdan çıkışı sağlar")
def menu():
    return input("=== (T)opla (F)ark Al (Y)azdır Y(A)rdım (Ç)ıkış ===")
def main():
    result = 0.0
    done = False
    while not done:
        secim = menu()
        if secim == "T" or secim == "t":
            sayi1 = float(input("Sayı 1: "))
            sayi2 = float(input("Sayı 2: "))
            sonuc = sayi1 + sayi2
            print(sonuc)
        elif secim == "F" or secim == "f":
            sayi1 = float(input("Sayı 1: "))
            sayi2 = float(input("Sayı 2: "))
            sonuc = sayi1 - sayi2
            print(sonuc)
        elif secim == "Y" or secim == "y":
            print(sonuc)
        elif secim == "A" or secim == "a":
            yardim()
        elif secim == "Ç" or secim == "ç":
            done = True
main()