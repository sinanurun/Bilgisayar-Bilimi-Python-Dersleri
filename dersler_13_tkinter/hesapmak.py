from tkinter import *

pencere = Tk()
kasa = []
def alan_guncelle(sayi):
    icerik = hesap_alani.get() + sayi
    hesap_alani.delete(0, END)
    hesap_alani.insert(0, icerik)
    return icerik


def islem_yap(islem):
    icerik = hesap_alani.get()

    if len(kasa) == 0:
        kasa.append(alan_guncelle(""))
        kasa.append(islem)
        hesap_alani.delete(0, END)
#        print(kasa)
    elif icerik == "" and len(kasa) == 2 and (islem == "+" or islem == "*" or islem == "-" or islem == "/"):
        kasa[1]=islem
        hesap_alani.delete(0, END)
    elif icerik != "" and len(kasa) == 2 and (islem == "+" or islem == "*" or islem == "-" or islem == "/"):
        sayi1, sayi2 = float(kasa[0]),float(icerik)
        if islem == "+":
            sonuc = sayi1 + sayi2
        elif islem == "-":
            sonuc = sayi1 - sayi2
        elif islem == "*":
            sonuc = sayi1 * sayi2
        elif islem == "/":
            if sayi2 !=0 or sayi2 !=00 or sayi2 !=000:
                sonuc = sayi1 / sayi2
            else:
                sonuc = sayi2
                print(" Sıfra Bölme Hatası")
        kasa[0], kasa[1] = str(sayi2), islem
        hesap_alani.delete(0, END)
        hesap_alani.insert(0, sonuc)
        print(kasa)
        return sonuc
    if islem == "=":

        return sonuc_goster(islem_yap(kasa[1]))
def sonuc_goster(sayi):
    hesap_alani.delete(0, END)
    hesap_alani.insert(0, sayi)


hesap_alani = Entry(pencere)
hesap_alani.insert(0, "")
hesap_alani.grid(row=0, columnspan=5)


buton_01 = Button(pencere, text = "1",command=lambda: alan_guncelle(str(1)))
buton_01.grid(row=1, column=0)
buton_02 = Button(pencere, text="2", command=lambda: alan_guncelle(str(2)))
buton_02.grid(row=1, column=1)
buton_03 = Button(pencere, text="3", command=lambda: alan_guncelle(str(3)))
buton_03.grid(row=1, column=2)
buton_topla = Button(pencere, text = "+", command=lambda: islem_yap(str("+")))
buton_topla.grid(row=1, column=3)
buton_esittir = Button(pencere, text = "=",command= lambda: islem_yap(str("=")))
buton_esittir.grid(rowspan=4, column=4, sticky=W+E+N+S)

buton_04 = Button(pencere, text="4", command=lambda: alan_guncelle(str(4)))
buton_04.grid(row = 2, column=0)
buton_05 = Button(pencere, text = "5",command= lambda: alan_guncelle(str(5)))
buton_05.grid(row = 2, column=1)
buton_06 = Button(pencere, text = "6",command= lambda: alan_guncelle(str(6)))
buton_06.grid(row = 2, column=2)
buton_cikart = Button(pencere, text = "-",command= lambda: islem_yap(str("-")))
buton_cikart.grid(row = 2, column=3)

buton_07 = Button(pencere, text = "7", command=lambda: alan_guncelle(str(7)))
buton_07.grid(row = 3, column=0)
buton_08 = Button(pencere, text = "8", command=lambda: alan_guncelle(str(8)))
buton_08.grid(row = 3, column=1)
buton_09 = Button(pencere, text = "9",command=lambda: alan_guncelle(str(9)))
buton_09.grid(row = 3, column=2)
buton_carp = Button(pencere, text = "*",command=lambda: islem_yap(str("*")))
buton_carp.grid(row = 3, column=3)

buton_0 = Button(pencere, text = "0",command=lambda: alan_guncelle(str("0")))
buton_0.grid(row = 4, column=0)
buton_00 = Button(pencere, text = "00",command=lambda: alan_guncelle(str("00")))
buton_00.grid(row = 4, column=1)
buton_000 = Button(pencere, text = "000",command=lambda: alan_guncelle(str("000")))
buton_000.grid(row = 4, column=2)
buton_bol = Button(pencere, text = "/",command= lambda: islem_yap(str("/")))
buton_bol.grid(row = 4, column=3)


buton_esittir = Button(pencere, text = "=",command= lambda: islem_yap(str("=")))



pencere.mainloop()

