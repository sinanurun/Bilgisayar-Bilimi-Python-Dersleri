#!C:/Python/Python35/python.exe
import cgi

form = cgi.FieldStorage()


print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Radio Button Kontolü</title>")
print("</head>")
print("<body>")

if form.getvalue('pdili'):
   dil = form.getvalue('pdili')
   print("<h2> Radio Buttonla : %s</h2>" % dil)
else:
    print("<h2> Radio Buttonla bir dil seçimi yapılmadı</h2>")

print("</body>")
print("</html>")