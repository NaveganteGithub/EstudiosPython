# Los administradores de contexto son bloques de codigo que se utilizan
# para abrir recursos y utilizarlos dentro de un bloque. Podemos usar
# clases para personalizar esos administradores de contexto.
# https://www.youtube.com/watch?v=HKlCLxEpLf8

class File:

    def __init__(self, name):
        self.name = name

    # Se ejecutara cuando haya una operacion de entrada
    def __enter__(self):
        print(f'Opening {self.name}')

        return self

    # Se ejecutara cuando haya una operacion de salida
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'Closing {self.name}')

with File("j_administradores_contexto.py") as file:
    print(file.name)

print('Done!')
