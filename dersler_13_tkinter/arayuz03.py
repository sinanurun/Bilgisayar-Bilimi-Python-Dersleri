import tkinter
import tkinter.ttk as ttk

pen = tkinter.Tk()


def merhaba(alfa):
    print('merhaba', alfa)
    btn.config(text="merhaba alfa")


btn = ttk.Button(text='merhaba', command=lambda: merhaba("can"))
btn.pack(padx=20, pady=20)

pen.mainloop()