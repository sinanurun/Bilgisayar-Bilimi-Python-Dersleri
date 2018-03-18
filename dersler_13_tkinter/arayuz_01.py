from tkinter import *
pencere = Tk()
frame1 = Frame(pencere)
frame1.pack()
frame2 = Frame(pencere)
frame2.pack()

rakam1 = Button(text = "buton 1",fg="red",bg="yellow")
rakam2 = Button(text = "buton 2",fg="blue",bg="yellow")
rakam3 = Button(text = "buton 3",fg="green",bg="yellow")

rakam1.pack()
rakam2.pack()
rakam3.pack(side = LEFT)


yazi = Label(text = "merhaba dünya")

yazi.pack()
pencere.mainloop()

