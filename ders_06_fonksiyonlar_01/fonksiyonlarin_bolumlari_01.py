from math import sqrt
sqrt(10)
print(sqrt(10))
# sqrt() #argüman olmadığı için hata veriyor parametre istiyor
#sqrt(10, 20) #argüman faazla olduğu için (iki tane ) için hata veriyor 1 parametre istiyor
sqrt(16)
print(sqrt(16))
#sqrt("16") # str değer istemiyor içerik muhakkak float ve ya int olmalı
type(sqrt(16.0))
print( type(sqrt(16.0)))
print(type(sqrt(float(int("16"))))) # iç içe birden fazla fonksiyon kullanımı