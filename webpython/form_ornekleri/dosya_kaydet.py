#!C:/Python/Python35/python.exe
import cgi, os
import cgitb; cgitb.enable()

form = cgi.FieldStorage()

dosya_bilgisi = form['dosyam']
if dosya_bilgisi.filename :
    fn = os.path.basename(dosya_bilgisi.filename)
    open(fn, 'wb').write(dosya_bilgisi.file.read())
    bilgilendirme = "dosyanız yüklendi"
else:
    bilgilendirme = "hata ile karşılaşıldı"

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Check Box Kontolü</title>")
print("</head>")
print("<body>")
print("<h2> Dosya Yükleme İşi Sonu : %s</h2>" % bilgilendirme)
print("</body>")
print("</html>")
