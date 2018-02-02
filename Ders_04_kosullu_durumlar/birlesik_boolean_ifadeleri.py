x = 10
y = 20
b = (x == 10) # b’ye True değerini atar.
print(b)
b = (x != 10) # b’ye False değerini atar.
print(b)
b = (x == 10 and y == 20) # b’ye True değerini atar.
print(b)
b = (x != 10 and y == 20) # b’ye False değerini atar.
b = (x == 10 and y != 20) # b’ye False değerini atar.
b = (x != 10 and y != 20) # b’ye False değerini atar.
b = (x == 10 or y == 20) # b’ye True değerini atar.
b = (x != 10 or y == 20) # b’ye True değerini atar.
b = (x == 10 or y != 20) # b’ye True değerini atar.
b = (x != 10 or y != 20) # b’ye False değerini atar.
print(b)