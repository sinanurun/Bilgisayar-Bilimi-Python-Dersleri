from tkinter import *
pencere = Tk()
def yazdir():
    icerik = giris.get()
    giris.delete(0,len(icerik))
    etiket.config(text=icerik)
giris = Entry(pencere)
giris.pack()
butonum = Button(pencere,text="Tıkla Bana",command=yazdir)
butonum.pack()
etiket = Label(pencere)
etiket.pack()

pencere.mainloop()