ruta_fichero = "SEPE_Python_Avanzado_PUE\\Tema 2 - PCAP\\Apuntes_diagramas\\saludo2.txt"

with open(ruta_fichero, "r", encoding="utf-8") as fichero:
    resultado_read = fichero.read()
    print("Read ->", resultado_read)

print("\n" * 2)

with open(ruta_fichero, "r", encoding="utf-8") as fichero:
    resultado_readlines = fichero.readlines()
    print("Readlines ->", resultado_readlines)

print("\n" * 2)

with open(ruta_fichero, "r", encoding="utf-8") as fichero:

    resultado_readline = fichero.readline()
    print("Readline ->", resultado_readline)
    
    resultado_readline = fichero.readline()
    print("Readline 2 ->", resultado_readline)

print("\n" * 2)
print("Metodo seek")

with open(ruta_fichero, "r", encoding="utf-8") as fichero:

    resultado_read = fichero.read()
    print("Read ->", resultado_read)

    fichero.seek(0)

    resultado_readlines = fichero.readlines()
    print("Readlines ->", resultado_readlines)

    fichero.seek(0)

    resultado_readline = fichero.readline()
    print("Readline ->", resultado_readline)
    
    resultado_readline = fichero.readline()
    print("Readline 2 ->", resultado_readline)