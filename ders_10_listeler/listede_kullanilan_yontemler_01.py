lst=["one","two","three","one"]
lst.append("four")
print(lst)
liste = [1,2,3,4,5,6,3]
liste.append(7)
print(liste)
print(lst.count("one")) # aranan değer listede kaç kere var
liste.insert(1,"ali")
print(liste)
print(liste.index(3))
liste.remove("ali")
print(liste)
liste.reverse()
y_liste =liste
print(y_liste)
y_liste.sort()
print(y_liste)
print(y_liste.pop(2))
print(y_liste)