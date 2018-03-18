from tkinter import *
pencere = Tk()
asilisim="mahmut"
asilsifre="mehmet"
def girisyapma():
    sifre = sifregiris.get()
    isim = isimgiris.get()
    if (sifre == asilsifre and isim == asilisim):
        girisdurumu.config(text="Doğru"+sayi)
    else:
        girisdurumu.config(text="Yanlış")

isim  = Label(pencere,text = "adınız")
isim.grid(row=0,column=0)
isimgiris = Entry(pencere,width="8")
isimgiris.grid(row=0,column=1)
sifre = Label(pencere,text="şiferniz")
sifregiris = Entry(pencere,width="8",show="*")
sifre.grid(row=1,column=0)
sifregiris.grid(row=1,column=1)
sifremihatirla =Checkbutton(pencere,text="şifremi hatırla")
sifremihatirla.grid(row=2,columnspan=2)
giris = Button(pencere,text="giriş",command=girisyapma())
giris.grid(row=3,column=1)
girisdurumu = Label(pencere,text="")
girisdurumu.grid(row=3,column=2)

pencere.mainloop()