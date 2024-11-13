class Producto:

    def __init__(self, identificator, descripcion, precio):
        self.id = identificator
        self.descripcion = descripcion
        self.precio = precio

    def __str__(self):
        return f"ID {self.id}, Descripcion: {self.descripcion}, Precio: {self.precio}"

    # Retorna un numero que sera el resultado de aplicar una suma
    # self representa el objeto a comparar, el segundo parametro representa el comparador
    def __add__(self, otra): # p3 + p4
        print("Sobreescrito")
        return self.precio + otra.precio

    # Retorna un numero que sera el resultado de aplicar una resta
    # self representa el objeto a comparar, el segundo parametro representa el comparador
    def __sub__(self, otra): # p3 - p4
        print("Sobreescrito")
        return self.precio - otra.precio

    # Retorna un numero que sera el resultado de aplicar una multiplicacion
    # self representa el objeto a comparar, el segundo parametro representa el comparador
    def __mul__(self, otra): # p3 * p4
        print("Sobreescrito")
        return self.precio * otra.precio

    # Retorna un numero que sera el resultado de aplicar una division
    # self representa el objeto a comparar, el segundo parametro representa el comparador
    def __truediv__(self, otra): # p3 / p4
        print("Sobreescrito")
        return self.precio / otra.precio

    # Retorna un numero que sera el resultado de aplicar una division con integer
    # self representa el objeto a comparar, el segundo parametro representa el comparador
    def __floordiv__(self, otra): # p3 // p4
        print("Sobreescrito")
        return self.precio // otra.precio

    # Retorna un numero que sera el resultado de aplicar una operacion de mod
    # self representa el objeto a comparar, el segundo parametro representa el comparador
    def __mod__(self, otra): # p3 % p4
        print("Sobreescrito")
        return self.precio % otra.precio

    # Retorna un numero que sera el resultado de aplicar un exponente
    # self representa el objeto a comparar, el segundo parametro representa el comparador
    def __pow__(self, otra): # p3 ** p4
        print("Sobreescrito")
        return self.precio ** otra.precio


p3 = Producto(3, "Teclado", 37.95)
p4 = Producto(4, "Raton", 19.80)

print("Suma", p3 + p4)
# Antes de sobreescribir el metodo: TypeError: unsupported operand type(s) for +: 'Producto' and 'Producto'
# Despues de sobreescribir el metodo: 57.75
print("Resta", p3 - p4)
print("Multiplicacion", p3 * p4)
print("Division", p3 / p4)
print("Division con entero", p3 // p4)
print("Resto", p3 % p4)
print("Exponente", p3 ** p4)
