from masa import *


class yuvarlak_masa(masa):

    def __init__(self,ayak=40,yukseklik=20,cap=30):
        super().__init__(ayak,yukseklik)
        self.cap = cap
        print(self.cap)
        print(self.ayak)
        print(self.yukseklik)



orta = yuvarlak_masa()
orta.masa_ozellikleri()
n = masa()
n.masa_ozellikleri()