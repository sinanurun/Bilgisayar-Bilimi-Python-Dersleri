# "Değiştir" butonuna basıldığında trafik ışıklarını sırasıyla yakan program
from tkinter import Tk, Canvas
from tkinter.ttk import Button, Frame
from time import sleep
def can():
    print(renk)
    print("yandı")
    return ButonaBasildiginda()
def ButonaBasildiginda():
    # Her bir tıklamada ışıkların sırasıyla yanması
    global renk
    print(renk)
    if renk == "red":
        renk = "green"
        canvas.itemconfigure(kirmiziLamba, fill="black") # Kırmızı ışık kapatılıyor
        canvas.itemconfigure(yesilLamba, fill="green") # Yeşil ışık yanıyor
    elif renk == "green":
        renk = "yellow"
        canvas.itemconfigure(yesilLamba, fill="black") # Yeşil ışık kapatılıyor
        canvas.itemconfigure(sariLamba, fill="yellow") # Sarı ışık yanıyor
    elif renk == "yellow":
        renk = "red"
        canvas.itemconfigure(sariLamba, fill="black") # Sarı ışık kapatılıyor
        canvas.itemconfigure(kirmiziLamba, fill="red") # Kırmızı ışık yanıyor
    sleep(2)
    return can()
# Kullanılacak değişkenlerin tanımlanması
renk = "red" # Açık olarak gelecek ilk trafik ışığı renk
root = Tk() # Ana Pencere"nin oluşturulması
root.title("Trafik Işıkları") # Pencere başlığı
frame = Frame(root) # Nesnelerin birlikte tutulması için grafiksel bileşen ( widget ) oluşturuluyor
frame.pack() # Pencere içerisine frame yerleştiriliyor
# Grafiksel bileşenlerin yerleştirileceği çizim alanı ( canvas ) oluşturuluyor
canvas = Canvas(frame, width=150, height=300)
# frame"in içerisinde çizim arayüzü oluşturuluyor
# Trafik ışıkları oluşturuluyor, zemin rengi gri olarak ayarlanıyor
canvas.create_rectangle(50, 20, 150, 280, fill="gray")
# Kırmızı Lamba
# kirmiziLamba = canvas.create_oval(x0,y0,x1,y1, options)
kirmiziLamba = canvas.create_oval(70, 40, 130, 100, fill="red")
# Sarı Lamba
sariLamba = canvas.create_oval(70, 120, 130, 180, fill="black")
# Yeşil Lamba
yesilLamba = canvas.create_oval(70, 200, 130, 260, fill="black")
# Grafiksel butonun oluşturulması ve işlevsellik kazandırılması Butona Basildiginda
#Fare ile tıklama yapıldığında fonksiyon çağrılıyor
button = Button(frame, text="Değiştir", command=ButonaBasildiginda)
# Oluşturulan katmanın ilk satır ve ilk sütünuna buton,
# birinci satır ikinci sütunununa da çizim alanı yerleştiriliyor.
button.grid(row=0, column=0)
canvas.grid(row=0, column=1)
# Grafiksel arayüz oluşturuluyor
root.mainloop()