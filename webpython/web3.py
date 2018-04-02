#!C:/Python/Python35/python.exe
# gönderilecek adres  web3.py?ad=Python&soyad=Kursum
# Import modules for CGI handling
import cgi
# Create instance of FieldStorage
form = cgi.FieldStorage()
# Get data from fields
first_name = form.getvalue('ad')
last_name = form.getvalue('soyad')
print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print('<meta http-equiv = "Content-Type" content = "text/html; charset=iso-8859-9" / >')
print("<title>url kullanma</title>")
print("</head>")
print("<body>")
print("<h2>Merhaba %s %s</h2>" % (first_name, last_name))
print("<h2>Merhaba {} {}</h2>".format(first_name,last_name))
print("</body>")
print("</html>")