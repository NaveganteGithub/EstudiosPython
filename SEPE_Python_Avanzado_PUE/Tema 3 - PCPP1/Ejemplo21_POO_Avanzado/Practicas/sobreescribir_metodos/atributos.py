
# https://stackoverflow.com/questions/4295678/understanding-the-difference-between-getattr-and-getattribute

class Producto:

    def __init__(self, identificator, descripcion, precio):
        self.id = identificator
        self.descripcion = descripcion
        self.precio = precio

    # Con este metodo podemos administrar cuando
    # un atributo no existe dentro de un objeto
    def __getattr__(self, item):
        print("Sobreescrito")
        return f"El atributo {item} no existe"

    # Este metodo se llama cada vez que pedimos
    # el valor de un atributo, y tiene como fin
    # devolver el valor de la variable que
    # nosotros escribimos
    def __getattribute__(self, item):
        print("Sobreescrito 1")
        valor = super().__getattribute__(item)
        return f"El atributo {item} existe", valor

    #
    def __setattr__(self, key, value):
        print("Sobreescrito 2")
        return key, value

    def __delattr__(self, item):
        print("Sobreescrito 3")
        return f"Eliminando {item}"


p1 = Producto(1, "Pantalla", 129.50)
"""
Sobreescrito 2
Sobreescrito 2
Sobreescrito 2
"""

setattr(p1, "identificador", 5)  # Sobreescrito 2

print("El metodo __getattribute__", getattr(p1, "identificador"))
"""
El metodo __getattribute__ ('El atributo identificador existe', 5)
Sobreescrito 1
"""

print("El metodo __getattr__", getattr(p1, "id"))
"""
Sobreescrito
El metodo __getattr__ El atributo id no existe
"""

delattr(p1, "identificador")  # Sobreescrito 3
