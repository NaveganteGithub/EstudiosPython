# Los administradores de contexto son bloques de codigo que se utilizan
# para abrir recursos y utilizarlos dentro de un bloque. Podemos usar
# clases para personalizar esos administradores de contexto.
# https://www.youtube.com/watch?v=HKlCLxEpLf8

class File:

    def __init__(self, archivo, modo):
        self.archivo = archivo
        self.modo = modo
        self.stream = None

    # Se ejecutara cuando vaya a empezar el bloque del administrador de contexto
    def __enter__(self):
        print(f'Abriendo {self.archivo}')
        self.stream = open(self.archivo, self.modo)
        return self.stream

    # Se ejecutara cuando vaya a terminar el bloque del administrador de contexto
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type, exc_val, exc_tb)
        print(f'Cerrando {self.archivo}')
        self.stream.close()
        return f"Final {self.archivo}"

# Administrador de contexto
with File("j_administradores_contexto.py", "r") as file: # __enter__
    print(file.name)
    print(file)
    print(file.read())

# __exit__
print(file.closed) # Devuelve True si se cierra correctamente
print(dir(file))
# Ten en cuenta que el atributo closed aparece
# porque estamos manejando un recurso que tiene
# el metodo close()
