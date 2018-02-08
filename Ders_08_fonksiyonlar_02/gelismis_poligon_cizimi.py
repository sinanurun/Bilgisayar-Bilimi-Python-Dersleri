import turtle
import random
# Program fonksiyona gönderilen parametreler ile çokgen çizer.
# Uzunluk paremetresi girilerek herbir kenarın uzunluğu belirlenir.
# Çizim x ve y parametrelerine girilen koordinat noktalarından başlar.
# Bir sonraki parametre çizimin kenar rengini belirler. (Varsayılan değer olarak siyah).
# Çizilen çokgenin içine dolgu olup olmayacağı belirlenir(Varsayılan False).
def Cokgen(kenarSayisi, uzunluk, x, y, renk="black", dolgu=False):
 turtle.penup()
 turtle.setposition(x, y)
 turtle.pendown()
 turtle.color(renk)
 if dolgu:
    turtle.begin_fill()
 for i in range(kenarSayisi):
    turtle.forward(uzunluk)
    turtle.left(360//kenarSayisi)
 if dolgu:
    turtle.end_fill()
# Adım adım çizim işlemi iptal edilerek çizim hızlandırılıyor
    turtle.hideturtle()
    turtle.tracer(0)
# Fonksiyonlar örnek çizimler için kullanılıyor
Cokgen(3, 30, 0, 0) # Üçgen çizimi
Cokgen(4, 30, 50, 50, "blue") # Kenar rengi mavi olan Kare çizimi
Cokgen(5, 30, 100, 100, "red", True) # Dolgusu kırmızı olan beşgen çizimi
turtle.update()
turtle.exitonclick() # Fare tuşuna tıklandığında çıkış işlemi yapılacaktır.