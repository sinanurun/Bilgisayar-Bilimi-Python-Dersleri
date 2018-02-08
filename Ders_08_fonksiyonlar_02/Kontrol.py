# Asal sayının kontrol edildiği fonksiyon tanımlama
from math import sqrt # * import math
def AsalKontrol(n):
# Fonksiyona gelen değer asal ise geriye True, değilse False döner.
 bolen= 2
 kok = sqrt(n) # * math.sqrt(n)
 while bolen <= kok:
    if n % bolen == 0: # Kalan kontrolü yapılıyor
        return False # Tam bölünme işlemi gerçekleşti. Asal Değil
    bolen += 1 # Bir sonraki bölen değerine geçiliyor.
 return True # Tüm değer kontrollerinden sonra kalanlı bölme gerçekleşmediğinde, True değeri dönüyor.
#print(AsalKontrol(5))