
"""
r - READ
w - WRITE
a - APPEND
x - create

La diferencia entre w y x, es que, si existe el fichero w lo sobrescribe, en cambio x, no puede sobrescribir el archivo,
si lo intenta salta excepcion
"""

fichero = open("./prueba.txt", "wt", encoding="utf-8")
fichero.write("Ágil")
fichero.close()
fichero = open("./prueba.txt", "wt", encoding="utf-8") # Sobreescribe
fichero.write("Indomable")
fichero.writelines(["con", "\n", "Dios"])
fichero.close()

fichero = open("./prueba2.txt", "xt", encoding="utf-8")
fichero.write("Ágil")
fichero.close()
"""fichero = open("./prueba2.txt", "xt", encoding="utf-8")
fichero.write("Indomable") # FileExistsError: [Errno 17] File exists: './prueba2.txt'
fichero.close()"""

fichero = open("./prueba.txt", "at", encoding="utf-8")
fichero.writelines("-------")
fichero.close()

fichero = open("./prueba.txt", "rt", encoding="utf-8")
fichero_chars = fichero.read()
fichero.seek(0)
fichero_subtexto = fichero.readline(5)
fichero.seek(0)
fichero_lista = fichero.readlines()
fichero.seek(0)
fichero_sublista = fichero.readlines(2)
fichero.close()
print("Carateres:", fichero_chars, sep="\n")
print("Texto:", fichero_subtexto, sep="\n")
print("Lista:", fichero_lista, sep="\n")
print("Sublista:", fichero_sublista, sep="\n")

