#!C:/Python/Python35/python.exe
import cgi, cgitb

form = cgi.FieldStorage()


print("Content-type:text/html\r\n\r\n"
      "<html>"
      "<head>"
      "<meta charset'=UTF-8'>"
      "<title>Textarea Örneği</title>"
      "</head>"
      "<body>")


if form.getvalue('icerik'):
   icerik_gelen = form.getvalue('icerik')
   print("<h2> Girilen Text İçeriği %s</h2>" % icerik_gelen)
else:
    print("<h2> Diğer Sayfadan Bir içerik Gelmedi</h2>")

print("</body>"
      "</html>")