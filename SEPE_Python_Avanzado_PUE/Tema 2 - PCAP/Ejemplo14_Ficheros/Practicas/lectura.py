fichero = open("fichero.txt", "rt", encoding="utf-8")
lectura = fichero.read()
print(lectura)
print(type(lectura))
print(lectura.splitlines())
fichero.close()

fichero = open("fichero.txt", "rt", encoding="utf-8")
fichero.seek(0) # seek te permite determinar la posicion del cursor o puntero
lectura = fichero.readlines()
print(lectura)
print(type(lectura))
fichero.close()