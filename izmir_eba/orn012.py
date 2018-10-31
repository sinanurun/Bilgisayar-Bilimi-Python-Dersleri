class siralama:
    def __init__(self):
        self.slistesi = [0]
        self.boyut = 0


    def yukari_al(self,i):
        while i // 2 > 0:
          if self.slistesi[i] < self.slistesi[i // 2]:
             tmp = self.slistesi[i // 2]
             self.slistesi[i // 2] = self.slistesi[i]
             self.slistesi[i] = tmp
          i = i // 2

    def ekle(self,k):
      self.slistesi.append(k)
      self.boyut = self.boyut + 1
      self.yukari_al(self.boyut)

    def asagi_al(self,i):
      while (i * 2) <= self.boyut:
          mc = self.ufaklik(i)
          if self.slistesi[i] > self.slistesi[mc]:
              tmp = self.slistesi[i]
              self.slistesi[i] = self.slistesi[mc]
              self.slistesi[mc] = tmp
          i = mc

    def ufaklik(self,i):
      if i * 2 + 1 > self.boyut:
          return i * 2
      else:
          if self.slistesi[i*2] < self.slistesi[i*2+1]:
              return i * 2
          else:
              return i * 2 + 1

    def ufaksil(self):
      retval = self.slistesi[1]
      self.slistesi[1] = self.slistesi[self.boyut]
      self.boyut = self.boyut - 1
      self.slistesi.pop()
      self.asagi_al(1)
      return retval

    def siralamayap(self,alist):
      i = len(alist) // 2
      self.boyut = len(alist)
      self.slistesi = [0] + alist[:]
      while (i > 0):
          self.asagi_al(i)
          i = i - 1

bh = siralama()
bh.siralamayap([9,5,6,2,3])

print(bh.ufaksil())
print(bh.ufaksil())
print(bh.ufaksil())
print(bh.ufaksil())
print(bh.ufaksil())
