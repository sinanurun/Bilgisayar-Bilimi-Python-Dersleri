f = open("../ornekler/pythonum.txt","r") # f adında dosya nesnesi
for satir in f: # Her satırı metin olarak oku
    print(satir.strip()) # Sondaki yeni satır karakterini sil
f.close() # Dosyayı kapat
with open("veriler.dat") as f: # f adında dosya nesnesi
    for line in f: # Her satırı metin olarak oku
        print(line.strip()) # Sondaki yeni satır karakterini sil
    f.close() # Dosyayı kapat