from math import sqrt
def AsalKontrol(n):
 if n == 2:
    return True
 if n < 2 or n % 2 == 0:
    return False
 geciciDeger = 3
 kok = sqrt(n)
 while geciciDeger <= kok:
    if n % geciciDeger == 0:
        return False
    geciciDeger += 2
 return True
def AsalAralikBelirleme(ilk, son):
 for deger in range(ilk, son + 1):
    if AsalKontrol(deger):
        yield deger
def main():
 asal = list(AsalAralikBelirleme(20, 50))
 print(asal)
#if __name__ == " __main__ ":
main() # Programı çalıştır