liste = list(range(0, 21, 2))
for i in range(-2, 23):
 if i in liste:
    print(i," eleman, ", liste,'''listesinin bir üyesidir.''')
 if i not in liste:
    print(i," eleman ", liste, "listesinin bir üyesi değildir.")
ad = "python kursu"
print(ad)
print(type(ad))
listelenmisad = list(ad)
print(listelenmisad)
print(type(listelenmisad))
