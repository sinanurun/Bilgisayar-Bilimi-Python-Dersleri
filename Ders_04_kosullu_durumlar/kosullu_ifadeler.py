n = int(input("Bir sayı giriniz: "))
print("|", n, "| = ", (-n if n < 0 else n), sep="")
notu = 75
durum = ("geçti" if notu >=70 else "kaldi")
print(durum)
