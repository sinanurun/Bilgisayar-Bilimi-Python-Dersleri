from masa import *
class yuvarlak_masa(masa):
    def __init__(self,ayak=40,yukseklik=20,cap=30):
        super().__init__(ayak,yukseklik)
        self.cap = cap
        print("ayak",self.ayak)
        print("yukseklik",self.yukseklik)
        print("cap",self.cap)
orta = yuvarlak_masa(8,100,60)
orta.masa_ozellikleri()
normal = masa(5,80)
normal.masa_ozellikleri()
