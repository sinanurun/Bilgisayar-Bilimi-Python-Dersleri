from fractions import Fraction
# Bazı kesir tanımlamaları yapılıyor
f1 = Fraction(1, 2)
f2 = Fraction(1, 2)
f3 = f1
# İlişkilendirmeler
print("f1 =", f1)
print("f2 =", f2)
print("f3 =", f3)
# Pay ve paydalar ayrı ayrı inceleniyor
print("f1--> Pay, Payda:", f1.numerator, f1.denominator)
print("f2--> Pay, Payda:", f2.numerator, f2.denominator)
print("f3--> Pay, Payda:", f3.numerator, f3.denominator)
# Kesirler karşılaştırılıyor
print("f1 == f2 ?", f1 == f2)
print("f1 == f3 ?", f1 == f3)
print("f1 ile f2 aynı değer mi?", f1 is f2)
print("f1 ile f3 aynı değer mi?", f1 is f3)
print(id(f1))
print(id(f2))
print(id(f3))