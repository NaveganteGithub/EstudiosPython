import Src.lib.pyclientweb as http

# https://assets.tryhackme.com/img/THMlogo.png
# https://download.sysinternals.com/files/PSTools.zip
url = input("¿URL del archivo?: ")
archivo = url.split("/")[-1]
r = bytes(http.get(url)['HTMLRaw'])

with open(archivo, 'wb') as file:
    file.write(r)