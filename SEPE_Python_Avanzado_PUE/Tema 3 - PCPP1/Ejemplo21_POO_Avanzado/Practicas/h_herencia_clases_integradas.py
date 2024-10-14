
# En Python podemos hacer que nuestras clases hereden las caracteristicas de las clases integradas en Python.
# Las clases integradas son aquellas que vienen por defecto en Python, como por ejemplo, str, int o float.
# En Python tenemos clases integradas como colas y pilas.
# https://www.youtube.com/watch?v=chqnG8HR-EU

"""

class ProcesarTexto(str):
    pass

texto = ProcesarTexto("Hola buenos dias a todos, ¿que tal?")
print(texto.title()) # Hola Buenos Dias A Todos, ¿Que Tal?

"""

class ProcesarTexto(str):

    def get_unique_words(self):
        return set(self.split())

    def get_unique_words_with_lower(self):
        return set(self.lower().split())

    def get_word_count(self):
        return len(self.split())

texto = ProcesarTexto("Hola hola buenos dias a todos, ¿que tal?")
print(texto.title())  # Hola Hola Buenos Dias A Todos, ¿Que Tal?
print(texto.get_unique_words())  # {'a', 'Hola', 'todos,', 'hola', '¿que', 'tal?', 'dias', 'buenos'}
print(texto.get_unique_words_with_lower())  # {'a', 'buenos', 'dias', 'hola', 'todos,', '¿que', 'tal?'}
print(texto.get_word_count())  # 8


class Tienda:

    def __init__(self):
        self.productos = {}

    def add(self, producto, cantidad):
        self.productos[producto] = self.productos.get(producto, 0) + cantidad

    def remove(self, producto, cantidad):
        self.productos[producto] = self.productos.get(producto, 0) - cantidad


class Tienda2:

    def __init__(self):
        self.productos = {}

    def add(self, producto, cantidad):
        self.productos[producto.lower()] = self.productos.get(producto.lower(), 0) + cantidad

    def remove(self, producto, cantidad):
        if self.productos.get(producto.lower(), 0) >= cantidad:
            self.productos[producto.lower()] = self.productos.get(producto.lower(), 0) - cantidad

eshop = Tienda2()
eshop.add("Peras", 7)
eshop.add("Manzana", 5)
eshop.add("Manzana", 2)
eshop.add("Platano", 6)
eshop.remove("Platano", 1)
print(eshop.productos)  # {'peras': 7, 'manzana': 7, 'platano': 5}