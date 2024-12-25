import os

# NOTA hay algunas operaciones que no se pueden hacer dentro de un mismo proceso

# Mover o renombrar archivos
# os.rename("Tarea3\\Pruebas\\ficheros\\prueba.txt", "Tarea3\\Pruebas\\ficheros\\destino\\prueba.txt")
# os.rename("Tarea3\\Pruebas\\ficheros\\destino\\prueba.txt", "Tarea3\\Pruebas\\ficheros\\prueba.txt")
# os.rename("Tarea3\\Pruebas\\ficheros\\prueba.txt", "Tarea3\\Pruebas\\ficheros\\prueba_2.txt")

# Saber si un archivo existe en cierta ruta 
print(os.path.isfile("Tarea3\\Pruebas\\ficheros\\destino\\prueba.txt"))
print(os.path.isfile("Tarea3\\Pruebas\\ficheros\\prueba.txt"))

# Listar archivos
print(os.listdir("Tarea3\\Pruebas\\ficheros"))

# Moverse por los directorios
print(os.listdir())
os.chdir("Tarea3\\Pruebas\\ficheros")
print(os.listdir("."))
print(os.listdir())

# Mostrar ruta actual
print(os.getcwd())

# Crear carpeta
os.mkdir("emision")

print(os.getcwd())
print(os.listdir())

# Eliminar carpeta
os.rmdir("emision")

print(os.getcwd())
print(os.listdir())