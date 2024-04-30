"""fichero = open("fichero.txt", "wt", encoding="utf-8")
fichero.write("Hola buenas")
fichero.close()"""

with open("fichero.txt", "wt", encoding="utf-8") as fichero:
    fichero.write("Hola")

try:
    fichero = open("fichero.txt", "wt", encoding="utf-8")
except:
    print("Error de apertura")
else:
    fichero.write("""Hola buenas,
mi mensaje para ti es,
estudia y aprende
""")
finally:
    fichero.close()