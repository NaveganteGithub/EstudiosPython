'''
    abrir el fichero en modo lectura
    leer el contenido y copiarlo en fichero2.txt
    mostrar el contenido fichero2.txt
'''

fichero = open("fichero.txt", "rt", encoding="utf-8")
lineas = fichero.read()
print("Contenido de fichero.txt:", lineas)
fichero.close()

fichero_2 = open("fichero2.txt", "wt", encoding="utf-8")
fichero_2.write(lineas)
fichero_2.close()

fichero_2 = open("fichero2.txt", "rt", encoding="utf-8")
print("Contenido de fichero2.txt:", fichero_2.read())
fichero_2.close()
