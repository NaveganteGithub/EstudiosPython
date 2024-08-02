import shelve

fichero = "SEPE_Python_Avanzado_PUE\\Tema 3 - PCPP1\\Ejemplo21_POO_Avanzado\\Practicas\\fichero"
stream = shelve.open(fichero, flag="n")
"""
w -> dbm.error: db file doesn't exist; use 'c' or 'n' flag to create a new db ; No existe ese fichero
r -> dbm.error: db file doesn't exist; use 'c' or 'n' flag to create a new db ; No existe ese fichero
c -> si existe lo abre en lectura/escritura y sino lo crea, es la opcion por defecto de flag. c de create
n -> siempre lo crea nuevo y lo abre en modo lectura/escritura. n de new
"""

stream['Juan'] = {'Matematicas': 7.5, "Lengua": 4.2}
stream['Maria'] = {'Matematicas': 3.7, "Lengua": 7.9, 'Arte': 5.5}

stream.close()

stream = shelve.open(fichero)
print("Notas de Maria:", stream['Maria'])
stream.close()
