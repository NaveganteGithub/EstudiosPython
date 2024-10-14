

def saludo(funcion):
    print("Hola", end=" ")
    return funcion

@saludo
def persona(nomb):
    print(nomb)

persona("Daniel")


def calculo(x, y):

    print(x + y, end=" ")

    # Si no lo pones, da TypeError: 'NoneType' object is not callable
    def mi_funcion(funcion):
        return funcion

    return mi_funcion

@calculo(3, 4)
def divisa(moneda):
    print(moneda)

divisa("euros")


class MiDecorador:

    def __init__(self, funcion):
        self.mi_funcion = funcion

    def __call__(self, *args, **kwargs):
        self.mi_funcion(*args)


@MiDecorador
def manejo_args(*mis_args):
    params = list(mis_args)
    print(params)
    return params

print(manejo_args(1, 2, 3, 4, 5, 6, 7, 8, 9))
