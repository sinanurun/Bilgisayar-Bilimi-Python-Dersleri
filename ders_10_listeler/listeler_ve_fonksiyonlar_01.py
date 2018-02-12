import random
def Topla(lst):
 sonuc=0
 for eleman in lst:
    sonuc+=eleman
 return result
def SifirAta(lst):
 for i in range(len(lst)):
    lst[i]=0
def RastgeleDegerAta(n):
 sonuc=[]
 for i in range(n):
    RastgeleDeger=random.randrange(100)
    sonuc+=[RastgeleDeger]
 return sonuc
def main():
 a=[2,4,6,8]
 print(a)
 print(sum(a)) #sum fonksiyonu ile liste içindeki değerler toplanır
 SifirAta(a)
 print(a)
 print(sum(a))
 a=[]
 print(a)
 print(sum(a))
 a=RastgeleDegerAta(10)
 print(a)
 print(sum(a))
main()