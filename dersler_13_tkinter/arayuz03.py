import tkinter
import tkinter.ttk as ttk

pen = tkinter.Tk()
x = 0

def merhaba(alfa):
    global x
    x = x+1
    print('merhaba', alfa)
    btn.config(text="merhaba"+str(x))


btn = ttk.Button(text='merhaba', command =lambda:  merhaba("can"))
btn.pack(padx=20, pady=20)

pen.mainloop()