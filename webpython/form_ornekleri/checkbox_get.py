#!C:/Python/Python35/python.exe
import cgi

form = cgi.FieldStorage()

if form.getvalue('python'):
   python  = "seçildi"
else:
   python = "Seçilmedi"

if form.getvalue('csharp'):
   csharp = "seçildi"
else:
   csharp = "Seçilmedi"

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Check Box Kontolü</title>")
print("</head>")
print("<body>")
print("<h2> CheckBox Python : %s</h2>" % python)
print("<h2> CheckBox CSharp : %s</h2>" % csharp)
print("</body>")
print("</html>")