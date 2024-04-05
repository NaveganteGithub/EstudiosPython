# declarar funciones
def saludar():  # funcion sin parametros y que no retorna ningun resultado
    print("Hola, que tal?")
    
def despedir(nombre):  # fun que recibe el parametro nombre y retorna un mensaje personalizado
    return (nombre + ", Hasta luego")


# invocar o llamar a una funcion
saludar()  # obligatorio poner los parentesis

# si llamo a la funcion sin parentesis
# saludar  no da error pero no muestra nada porque no lo reconoce como funcion

# Si intentamos pasar parametros a una funcion que no los tiene declarados
#TypeError: saludar() takes 0 positional arguments but 1 was given
#saludar(1111)

# cuando invoco a una funcion que retorna un dato, ese dato hay que guardarlo, mostrarlo, ....
print(despedir('Pepito'))
resultado = despedir('Pepito')
print(resultado)

# si la funcion esta declarada con parametros y no se los paso
# TypeError: despedir() missing 1 required positional argument: 'nombre'
print(despedir())