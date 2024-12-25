

mi_archivo = open("Tarea3\\Pruebas\\ficheros\\prueba.txt", "w")
mi_archivo.write("Hola buenas tardes")
mi_archivo.close()

mi_archivo = open("Tarea3\\Pruebas\\ficheros\\prueba.txt", "a")
mi_archivo.write("\nHola buenos dias")
mi_archivo.close()

mi_archivo = open("Tarea3\\Pruebas\\ficheros\\prueba.txt", "r")
leido = mi_archivo.read()
mi_archivo.close()
print(leido)

mi_archivo = open("Tarea3\\Pruebas\\ficheros\\prueba.txt", "r")
lista_lineas = mi_archivo.readlines()
mi_archivo.close()
print(lista_lineas)

# Me permite abrir recursos sin tener que preocuparme de tener que cerrarlos
with open("Tarea3\\Pruebas\\ficheros\\prueba.txt", "r") as mi_archivo:
    leido = mi_archivo.read()
    print(leido)