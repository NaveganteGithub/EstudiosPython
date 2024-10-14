class Producto:

    def __init__(self, identificator, descripcion, precio):
        self.id = identificator
        self.descripcion = descripcion
        self.precio = precio

    def __str__(self):
        return f"ID {self.id}, Descripcion: {self.descripcion}, Precio: {self.precio}"

    """Ten cuidado al usar estos metodos sobrescritos sobre las instancias,
    porque tienes que seguir una serie de pautas para que no te salte una 
    excepcion de tipo 
    
    TypeError: unsupported operand type(s) for -=: 'float' and 'Producto'
    """
    def __iadd__(self, otra):  # p3 += p4
        print("Sobreescrito")
        self.precio = self.precio + otra.precio
        return self.precio

    def __isub__(self, otra):  # p3 -= p4
        print("Sobreescrito")
        self.precio = self.precio - otra.precio
        return self.precio
    
    def __imul__(self, otra):  # p3 *= p4
        print("Sobreescrito")
        self.precio = self.precio * otra.precio
        return self.precio
    
    def __itruediv__(self, otra):  # p3 /= p4
        print("Sobreescrito")
        self.precio = self.precio / otra.precio
        return self.precio
    
    def __ifloordiv__(self, otra):  # p3 //= p4
        print("Sobreescrito")
        self.precio = self.precio // otra.precio
        return self.precio
    
    def __imod__(self, otra):  # p3 %= p4
        print("Sobreescrito")
        self.precio = self.precio % otra.precio
        return self.precio
    
    def __ipow__(self, otra):  # p3 **= p4
        print("Sobreescrito")
        self.precio = self.precio ** otra.precio
        return self.precio


p3 = Producto(3, "Teclado", 37.95)
p4 = Producto(4, "Raton", 19.80)

print("Suma con asignacion antes", p3)
p3 += p4
print("Suma con asignacion", p3)

"""Ten cuidado con usar los asignadores de forma repetida 
en la misma funcion porque puede saltarte una excepcion

Traceback (most recent call last):
    p3 += p4
TypeError: unsupported operand type(s) for +=: 'float' and 'Producto'

p3 += p4
print("Suma con asignacion", p3)
"""

p3 = Producto(3, "Teclado", 37.95)
p4 = Producto(4, "Raton", 19.80)

print("Resta con asignacion antes", p3)
p3 -= p4
print("Resta con asignacion", p3)

"""
Solo puedes utilizar una operacion de asignacion por cada instancia, 
si intentas aplicar dos operadores de asignacion en una misma instancia 
te dara una excepcion 

Traceback (most recent call last):
    p3 *= p4
TypeError: unsupported operand type(s) for *=: 'float' and 'Producto'

p3 *= p4
print("Multiplicacion con asignacion", p3)
"""

p3 = Producto(3, "Teclado", 37.95)
p4 = Producto(4, "Raton", 19.80)

print("Multiplicacion con asignacion antes", p3)
p3 *= p4
print("Multiplicacion con asignacion", p3)


p3 = Producto(3, "Teclado", 37.95)
p4 = Producto(4, "Raton", 19.80)

print("Division con asignacion antes", p3)
p3 /= p4
print("Division con asignacion", p3)


p3 = Producto(3, "Teclado", 37.95)
p4 = Producto(4, "Raton", 19.80)

print("Division de entero con asignacion antes", p3)
p3 //= p4
print("Division de entero con asignacion", p3)


p3 = Producto(3, "Teclado", 37.95)
p4 = Producto(4, "Raton", 19.80)

print("Resto con asignacion antes", p3)
p3 %= p4
print("Resto con asignacion", p3)

p3 = Producto(3, "Teclado", 37.95)
p4 = Producto(4, "Raton", 19.80)

print("Exponente con asignacion antes", p3)
p3 **= p4
print("Exponente con asignacion", p3)
