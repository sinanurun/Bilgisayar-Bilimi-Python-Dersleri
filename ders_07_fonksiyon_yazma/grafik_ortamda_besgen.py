# turtle modülünü kullanarak beşgen çizimi
import turtle
import random
# turtle modülü programa ekleniyor
def polygon(sides,length,x,y,color):
#polygon adında ve içerisine 5 değer alabilen bir fonksiyon tanımlanıyor
 turtle.penup()
 print(help(turtle.penup))
# Çizimi yapacak kalemin yönleri belirleniyor
 turtle.setposition(x,y)
# Parametre olarak gelen x,y değerleri başlangıç noktası olarak belirleniyor
 turtle.pendown()
# Çizimi yapacak kalemin yönleri belirleniyor
 turtle.color(color)
# Parametre olarak gelen renk atanıyor
 turtle.begin_fill()
 for i in range(sides):
    turtle.forward(length)
    turtle.left(360//sides)
    turtle.end_fill()
polygon(5,100,50,50,"blue") # Tanımlanan fonksiyonun istenilen parametrelerle çağırılması