from tkinter import *
pencere = Tk()
def yazdir():
    print("tıklandı")
butonum = Button(pencere,text="Tıkla Bana",command=yazdir)
butonum.pack()

pencere.mainloop()