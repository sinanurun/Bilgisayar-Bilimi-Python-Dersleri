# Pencere içerisine diktörtgen bir kutu çizimi
from turtle import Turtle, mainloop
t = Turtle() # Adı t olan yeni bir Turtle() nesnesi oluşturuluyor
t.pencolor("red") # t nesnesinin çizim kalemi rengi kırmızı olarak ayarlanıyor
t.forward(200) # t nesnesinin kalemi 200 birim ileri oynatılıyor ve dikdörtgenin alt kenarı çiziliyor
t.left(90) # Turtle 90 derece sola döndürülüyor
t.pencolor("blue") # t nesnesinin rengi mavi olarak değiştiriliyor
t.forward(150) # Sağ kenarın çizilmesi için Turtle 150 birim yukarı ilerletiliyor
t.left(90) # Turtle 90 derece sola döndürülüyor
t.pencolor("green") # Turtle nesnesinin rengi yeşil olarak değiştiriliyor
t.forward(200) # Dikdörtgenin üst kenarının çizilmesi için Turtle 200 birim ilerletiliyor.
t.left(90) # Turtle 90 derece sola döndürülüyor
t.pencolor("black") # Turtle nesnesinin rengi siyah olarak değiştiriliyor
t.forward(150) # Son kenar olan sol kenarın çizilmesi için Turtle 150 birim ilerletiliyor.
t.hideturtle() # Turtle gizleniyor
mainloop() # Kullanıcıdan veri bekleniyor