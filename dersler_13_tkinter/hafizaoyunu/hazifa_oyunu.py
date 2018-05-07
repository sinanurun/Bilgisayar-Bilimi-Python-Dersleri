from tkinter import *
from random import random
import time
from tkinter import messagebox

pencere = Tk()
hafiza = []

global bilinen
bilinen = 0

def cevir(x):
    if len(hafiza)==0:
        for i in atananlar:
            if x == i[0]:
                ilk_buton = i[2]
                ilk_buton.config(text=i[1], state="disabled")
                hafiza.append(i)
                print(i[1], hafiza)
    else:
        for i in atananlar:
            if x == i[0]:
                ikinci_buton = i[2]
                ikinci_buton.config(text=i[1], state="disable")
                if i[1] == hafiza[0][1]:
                   hafiza.clear()
                   global  bilinen
                   bilinen = bilinen + 1
                   if bilinen == 8:
                       messagebox.showinfo("Hafıza Kartı oyunu", "tebrikler Hepsini doğru Yaptınız")
                else:
                    ikinci_buton.after(100, lambda a=i[2]: cevirici(a))


def cevirici(ikinci_buton):
    birinci_buton = hafiza[0][2]
    time.sleep(0.5)
    birinci_buton.config(text="eşimi bul", state="active")
    ikinci_buton.config(text="eşimi bul", state="active")

    hafiza.clear()

icerikler = [1, 2, 3, 4, 5, 6, 7, 8]
icerikler = icerikler*2
atananlar = []
satirno = 0

for satir in range(0, 4):
    sutunno=0
    for sutun in range(0, 4):
        deger = len(icerikler)
        ilk = str(satirno)+str(sutunno)
        ikinci = int(random()*deger)
        butonx = Button(pencere, text="eşimi bul", command=lambda a=ilk: cevir(a))
        atanacak = (ilk, icerikler[ikinci], butonx)
        atananlar.append(atanacak)
        icerikler.pop(ikinci)
        butonx.grid(row = satirno,column= sutunno)
        sutunno += 1
    satirno += 1

pencere.mainloop()
