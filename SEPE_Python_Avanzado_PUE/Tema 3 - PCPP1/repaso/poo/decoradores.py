
def saludo(funcion):
    print("Hola", end=" ")
    return funcion

@saludo
def nombre(nomb):
    print(nomb)

nombre("David")

######################################

def calculo(x, y):

    print(x + y, end=" ")

    def funcion_decorador(funcion):
        return funcion

    return funcion_decorador

@calculo(5, 2)
def divisa(moneda):
    print(moneda)

divisa("euros")



class MiDecorador:

    def __init__(self, funcion):
        self.mi_funcion = funcion

    def __call__(self, *args, **kwargs):
        self.mi_funcion(*args)

@MiDecorador
def mi_amigo(*nombres):
    print(nombres)

mi_amigo("Jesus", "Daniel", "Ana", "Maria", "Santiago")