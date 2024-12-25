# Un decorador es un patron de diseño estructural que permite agregar
# funcionalidades adicionales a los objetos encapsuladores.

# Decorador simple
def mi_decorador(funcion):
    print(5 + 2)
    return funcion

@mi_decorador
def mi_funcion():
    print("Hola")

mi_funcion()


# Decorador con parámetros
def mi_decorador_2(a, b):

    print(a + b)

    def procesar_funcion(funcion):
        return funcion

    return procesar_funcion

@mi_decorador_2(7, 8)
def mi_funcion_2():
    print("Adios")

mi_funcion_2()


# Decorador de clase (versión args)
class Decorador:

    def __init__(self, funcion):
        self.mi_funcion = funcion

    def __call__(self, *numeros):
        resultado = [n * 2 for n in numeros]
        self.mi_funcion(*resultado)


@Decorador
def mi_funcion_3(*numeros):
    print(numeros)

mi_funcion_3(7,5,8,9,2,1,4)


# Decorador de clase (versión kwargs)
class DecoradorKwargs:

    def __init__(self, funcion):
        self.mi_funcion = funcion

    def __call__(self, **numeros):
        resultado = {day: num * 2 for day, num in numeros.items()}
        self.mi_funcion(**resultado)


@DecoradorKwargs
def mi_funcion_4(**numeros):
    print(numeros)

mi_funcion_4(domingo=4,lunes=8,martes=9,miercoles=2,jueves=5,viernes=1,sabado=7)
