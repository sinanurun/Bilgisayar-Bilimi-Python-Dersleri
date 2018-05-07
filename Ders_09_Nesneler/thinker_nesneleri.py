from tkinter import Tk, Button
dosya_adi = "tiklanma_sayisi_01.txt"
sayac = 0 # Tıklama sayısının hafızada tutulacağı değişken tanımlanıyor
def update():
# Grafikte bulunan butona tıklandığında sayaç artırma işlemi
    f = open(dosya_adi,"w")
    global sayac, b
    sayac += 1
    b.config(text="Tıklama Sayısı = " + str(sayac))
    f.write(str(sayac) + "\n")
    f.close()
    print("Güncelleniyor")
root = Tk()
b = Button(root)
b.configure(background="yellow", text="Tıklama Sayısı = 0",command=update)
# Ekrana buton nesnesi oluşturuluyor
b.pack()
root.config(bg='red')
root.mainloop()