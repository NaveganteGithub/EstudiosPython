'''
    abrir el fichero en modo lectura
    leer el contenido y copiarlo en fichero2.txt
    mostrar el contenido fichero2.txt
'''
# abrir el fichero en modo lectura
fichero_lectura = open("fichero.txt", "rt", encoding="utf-8")

# abrir el fichero en modo escritura
fichero_escritura = open("fichero2.txt", "w+t", encoding="utf-8")

# leer el contenido del fichero.txt
contenido = list(fichero_lectura)
#contenido = fichero_lectura.readlines()

# recorrer la lista de lineas y por cada una la escribimos en fichero2.txt
for linea in contenido:
    fichero_escritura.write(linea)

# leer el contenido creado en fichero2.txt
fichero_escritura.seek(0)  # mover el cursor al principio
for linea in fichero_escritura.readlines():
    print(linea, end="")

# cerrar los ficheros
fichero_lectura.close()
fichero_escritura.close()
