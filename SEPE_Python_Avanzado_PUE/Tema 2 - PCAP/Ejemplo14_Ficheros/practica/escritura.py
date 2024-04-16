# Abrir un fichero en modo escritura
'''
Se utiliza el método raw para no tener conflictos con las barras en /  \  en las rutas absolutas.
Ejemplo fichero = open(r'C:\Users\Lican\escritorio\Curso Python Pue\Curso_Python_Modulo10\requirements.txt', 'wt', encoding='utf-8')
'''

# ruta absoluta
#fichero = open("/Users/anaisabelvegascaceres/Desktop/fichero.txt", "wt", encoding="utf-8")

# ruta relativa
fichero = open("fichero.txt", "wt", encoding="utf-8")
texto = "Esto es una prueba"
fichero.write(texto)

# cerrar el fichero
#fichero.close()

'''
try:
    fichero = open("fichero.txt", "wt", encoding="utf-8")
except:
    print("Error al abrir el fichero")
else:
    texto = "Esto es una prueba"
    fichero.write(texto)
finally:
    fichero.close()
'''