def main():
 toplam = 0.0
 girilecekSayiAdeti = 5
 sayilar = []
 print("Lütfen", girilecekSayiAdeti, " adet sayi giriniz :")
 for i in range(0, girilecekSayiAdeti):
     sayi = float(input(str(i+1) + " . sayıyı giriniz : "))
     sayilar += [sayi]
     toplam += sayi

 for sayi in sayilar:
     print(end="Girilen Sayılar: ")
     print(sayi, end="")
     print() # Alt satıra geçiş
 print("Ortalama :", toplam/girilecekSayiAdeti)
main()