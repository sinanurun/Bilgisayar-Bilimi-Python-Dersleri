from tkinter import *
anaekran = Tk()
anaekran.title("Mutlu Hesaplar")
anaekran.master.maxsize(100,500)
l1 = Label(anaekran)
l1.configure(text="hesap makinemize hoş geldiniz")
l1.pack()
b1 = Button(anaekran)
b1.configure(text = "1")
b1.pack()

anaekran.mainloop()