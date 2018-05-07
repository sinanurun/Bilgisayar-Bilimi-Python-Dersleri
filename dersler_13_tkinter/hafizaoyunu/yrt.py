import tkinter as tk
import time

root = tk.Tk()

def change():
    button.config(text='Running')
    button.config(state='disabled')
    print ("start")
    root.after(5000,changeback)
def changeback():
    print ("end")
    button.config(state='normal')
    button.config(text="Run")

button = tk.Button(root,text="Run",command=change)
button.pack()


root.mainloop()