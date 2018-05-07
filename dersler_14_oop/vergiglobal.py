global vergi
vergi = 0
def elektrik():
    vergi = int(input("elektrik vergi tutarını giriniz"))
    global vergi
    vergi = vergi
def su():
    global vergi
    vergi = vergi + int(input("su vergi tutarını giriniz"))
def egitim():
    global vergi
    vergi = vergi + int(input("egitim vergi tutarını giriniz"))
elektrik()
su()
egitim()
print(vergi)