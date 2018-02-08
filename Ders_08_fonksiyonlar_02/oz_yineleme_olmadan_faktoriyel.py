def faktoriyel(n):
 sonuc = 1
 while n:
    sonuc *= n
    n -= 1
 return sonuc
def main():
 print(" 0! = ", faktoriyel(0))
 print(" 1! = ", faktoriyel(1))
 print(" 6! = ", faktoriyel(6))
 print("10! = ", faktoriyel(10))
main()