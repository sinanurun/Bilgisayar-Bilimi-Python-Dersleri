from tkinter import *
pencere = Tk()

rakam1 = Button(text = "buton 1",fg="red",bg="yellow")
rakam2 = Button(text = "buton 2",fg="blue",bg="yellow")
rakam3 = Button(text = "buton 3",fg="green",bg="yellow")

rakam1.pack(side=RIGHT)
rakam2.pack()
rakam3.pack(side = LEFT)


yazi = Label(text = "Merhaba Python severler")

yazi.pack(side = LEFT)
pencere.mainloop()

