
# Los args son variables donde podemos pasarle un número indeterminado de argumentos,
# para poder procesarlos en una lista
def lista_parametro(*args):
    for data in args:
        print(data)


# Los kwargs son variables que se puede pasar argumentos de forma indeterminada
# y procesar los datos en un diccionario
def diccionario_parametro(**kwargs):
    for clave, valor in kwargs.items():
        print(clave.capitalize(), "tiene el valor", valor)


# Paso de argumentos a un args
lista_parametro(1,2,3,4,5,6,7)

# Paso de argumentos a un kwargs
diccionario_parametro(
    nombre="David", sueldo=12345, email="davi02@mail.com",
    telefono=555214510, red_social="Telegram", empresa="ADDD",
    genero="hombre")
