# Sıcaklık değerini okumak için
dereceF = float (input ("Sıcaklığını F derece olarak girin:"))
# Dönüşümü gerçekleştirin
#dereceC = (dereceF - 32)/(5/9)
dereceC = (dereceF - 32)/(1.8)
# Sonucu bildir
print (dereceF, "derece F =", dereceC, "C derece")
