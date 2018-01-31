saniye = int(input("saniye sayısını girin:"))
saat = saniye // 3600 # 3600 saniye = 1 saat
saniye = saniye % 3600
dakika = saniye // 60 # 60 saniye = 1 dakika
saniye = saniye% 60
print(saat, "sa", dakika, "dk", saniye, "sn")