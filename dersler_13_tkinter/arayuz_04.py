from tkinter import *
from tkinter import messagebox
from time import *

pencere = Tk()

pencere.title("Python Programlama Tkinter")
pencere.geometry("500x250")

uygulama = Frame(pencere)
uygulama.grid()


def dialog():
    var = messagebox.showinfo("Uyarı", "Python Programlama")
    sleep(2)
    yok = messagebox.askyesnocancel("hata","uyarı aldınız")
    if yok == True:
        return dialog()
button1 = Button(uygulama, text=" Uyarı Ver ", width=20, command=dialog)
button1.grid(padx=110, pady=80)

# formu çiz
pencere.mainloop()