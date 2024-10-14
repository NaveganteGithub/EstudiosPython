from urllib import request

archivo_internet = request.urlopen("https://github.com/trimstray/the-book-of-secret-knowledge/blob/master/README.md")
informacion = archivo_internet.read()
print(informacion.decode('utf-8'))