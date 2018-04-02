#!C:/Python/Python35/python.exe
# gönderilecek adres  get_forumdan?ad=Python&soyad=Kursum
# CGI işlemleri için CGI modülünü dahil ediyoruz
import cgi
# form adında bir örnek alan nesnesi oluşturuyoruz
form = cgi.FieldStorage()
# alanlardan verileri çekiyoruz
adi = form.getvalue('adi')
soyadi = form.getvalue('soyadi')
print("Content-type:text/html\r\n\r\n"
      "<html>"
        "<head>"
            "<meta http-equiv = Content-Type content = text/html; charset=iso-8859-9 / >"
                "<title>url kullanma</title>"
        "</head>"
      "<body>")
print("<h2>Merhaba %s %s</h2>" % (adi, soyadi))
print("<h2>Merhaba {} {}</h2>".format(adi, soyadi))
print("</body>"
      "</html>")