"""Los context manager: son estructuras que nos permiten manejar recursos
abriendo recursos al principio del bloque y cerrarlos al salir del bloque
"""

class Contexto:

    def __init__(self, num):
        self.numero = num

    # Manejo la entrada al bloque del context manager
    def __enter__(self):
        print("Exponente", self.numero ** 2)
        return self.numero ** 2

    # Manejo la salida al bloque del context manager
    def __exit__(self, exc_type, exc_val, exc_tb):

        if exc_type is not None:
            print(
                "La excepción es un", exc_type,
                "el mensaje que devuelve es", exc_val,
                "su traza es", exc_tb
            )
            # La excepción es un <class 'TypeError'>
            # el mensaje que devuelve es unsupported operand type(s) for //: 'int' and 'str'
            # su traza es <traceback object at 0x0000015D10647280>

        del self.numero
        return "El numero ya no existe"

    def __floordiv__(self, other):
        print("Division", self.numero // other.numero)
        return self.numero // other.numero


contexto = Contexto(5)

with contexto as context:
    print(context // 2)
    # print(context // "2")
