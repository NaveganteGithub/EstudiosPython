import enum

class MiEnumerador(enum.Enum):

    enumerador1 = 3,2,"buenas"
    enumerador2 = {5, 8, "hola"}
    enumerador3 = [4,1,"hey hey"]


print(MiEnumerador.enumerador3.name)
print(MiEnumerador.enumerador3.value)
