#!C:/Python/Python35/python.exe
print("Content-type:text/html\r\n\r\n")
print('<html>')
print('<head>')
print('<meta http-equiv = "Content-Type" content = "text/html; charset=iso-8859-9" / >')
print('<title>İlk Python Web Sayfam</title>')
print('</head>')
print('<body>')

print("<font size=+1>Environment</font><\br>")
for param in os.environ.keys():
   print ("<b>%20s</b>: %s<\br>" % (param, os.environ[param]))
print('</body>')
print('</html>')