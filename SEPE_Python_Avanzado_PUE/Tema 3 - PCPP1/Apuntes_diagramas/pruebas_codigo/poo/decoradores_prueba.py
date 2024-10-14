
# Los decoradores se activan aunque no utilices la funcion

# Los decoradores siempre van a requrir de parametros,
# unos seran para procesar datos, y otros para procesar
# la funcion a decorar

def mi_decorador(funcion):
    print("fsdfsdfsf")
    return funcion


@mi_decorador
def mi_prueba():
    print("Hola hola")


mi_prueba()


def mi_decorador_2(a, b):

    print(a, b)

    def procesar_decorador(funcion):
        return funcion

    return procesar_decorador


@mi_decorador_2(2,  2)
def mi_prueba_2():
    print("Hey hey")


mi_prueba_2()


class Decorador:

    def __init__(self, funcion):
        self.funcion = funcion

    def __call__(self, *argumentos_param):

        self.argumentos = argumentos_param

        print(self.argumentos)

        self.funcion(self.argumentos)


@Decorador
def prueba(*args):
    print("Hola", args)


prueba(2, 5, 7, 8, 9, 10)
