# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 09:46:15 2024
@author: Ismael Montoro Peñasco
"""

class Producto:
    
    def __init__(self, identificator, descripcion, precio):
        self.id = identificator
        self.descripcion = descripcion
        self.precio = precio
    
    ##################### FUNCIONALIDADES #####################

    # Cuando mostremos el objeto, represente su estado (contenido, valores)    
    def __str__(self):
        return f"ID {self.id}, Descripcion: {self.descripcion}, Precio: {self.precio}"
    
    # Cuando el objeto se elimine y lo mostremos, que se muestre "Clase eliminada"
    def __del__(self):
        return "Clase eliminada"
    
    # Retorna un valor numerico, imprendiscible para comparar elementos del conjunto
    def __hash__(self):
        # return int(self.id + len(self.descripcion) + self.precio)
        
        suma = 0
        for letra in self.descripcion:
            suma += ord(letra)
            
        return int(self.id + suma + self.precio)
    
    ##################### BOOLEANOS #####################

    # Retorna un valor booleano indicando si esta instancia es igual a la recibida como argumento
    # self representa el objeto a comparar, el segundo parametro representa el comparador
    def __eq__(self, otra): # p1 == p2
        return self.id == otra.id and self.descripcion == otra.descripcion and self.precio == otra.precio
    
    # Retorna un valor booleano indicando si esta instancia no es igual a la recibida como argumento
    # self representa el objeto a comparar, el segundo parametro representa el comparador
    def __ne__(self, otra): # p1 != p2
        # print(self.id != otra.id, self.descripcion != otra.descripcion, self.precio != otra.precio)
        return self.id != otra.id and self.descripcion != otra.descripcion and self.precio != otra.precio
    
    # Retorna un valor booleano indicando si esta instancia tiene un valor mayor, o varios valores mayores, 
    # a la instancia recibida como argumento
    # self representa el objeto a comparar, el segundo parametro representa el comparador
    def __gt__(self, otra): # p1 > p2
        return self.id > otra.id and self.descripcion > otra.descripcion and self.precio > otra.precio
    
    # Retorna un valor booleano indicando si esta instancia tiene un valor mayor o igual, 
    # o varios valores mayores o iguales, a la instancia recibida como argumento
    # self representa el objeto a comparar, el segundo parametro representa el comparador
    def __ge__(self, otra): # p1 >= p2
        return self.id >= otra.id and self.descripcion >= otra.descripcion and self.precio >= otra.precio
    
    # Retorna un valor booleano indicando si esta instancia tiene un valor menor, o varios 
    # valores menores, a la instancia recibida como argumento
    # self representa el objeto a comparar, el segundo parametro representa el comparador
    def __lt__(self, otra): # p1 < p2
        return self.id < otra.id and self.descripcion < otra.descripcion and self.precio < otra.precio
    
    # Retorna un valor booleano indicando si esta instancia tiene un valor menor, o varios 
    # valores menores a la instancia recibida como argumento
    # self representa el objeto a comparar, el segundo parametro representa el comparador
    def __le__(self, otra): # p1 <= p2
        return self.id <= otra.id and self.descripcion <= otra.descripcion and self.precio <= otra.precio

    ##################### CALCULOS #####################

    # Retorna un numero que sera el resultado de aplicar una suma
    # self representa el objeto a comparar, el segundo parametro representa el comparador
    def __add__(self, otra): # p3 + p4
        return self.precio + otra.precio
    
    # Retorna un numero que sera el resultado de aplicar una resta
    # self representa el objeto a comparar, el segundo parametro representa el comparador
    def __sub__(self, otra): # p3 - p4
        return self.precio - otra.precio
    
    # Retorna un numero que sera el resultado de aplicar una multiplicacion
    # self representa el objeto a comparar, el segundo parametro representa el comparador
    def __mul__(self, otra): # p3 * p4
        return self.precio * otra.precio
    
    # Retorna un numero que sera el resultado de aplicar una division
    # self representa el objeto a comparar, el segundo parametro representa el comparador
    def __truediv__(self, otra): # p3 / p4
        return self.precio / otra.precio
    
    # Retorna un numero que sera el resultado de aplicar una division con integer
    # self representa el objeto a comparar, el segundo parametro representa el comparador
    def __floordiv__(self, otra): # p3 // p4
        return self.precio // otra.precio
    
    # Retorna un numero que sera el resultado de aplicar una operacion de mod
    # self representa el objeto a comparar, el segundo parametro representa el comparador
    def __mod__(self, otra): # p3 % p4
        return self.precio % otra.precio
    
    # Retorna un numero que sera el resultado de aplicar un exponente
    # self representa el objeto a comparar, el segundo parametro representa el comparador
    def __pow__(self, otra): # p3 ** p4
        return self.precio ** otra.precio
    
    ##################### ASIGNACION #####################
    
    """Puedes sobreescribir todos estos metodos se pueden sobreescribir, pero asegurate
    de no sobreescribir varios a la vez, y solo sobreescribir solamente uno por clase,
    porque sino lo que ocurrira es una excepcion 
    
    TypeError: unsupported operand type(s) for -=: 'float' and 'Producto'
    """
    def __iadd__(self, otra): # p3 += p4
        self.precio = self.precio + otra.precio
        return self.precio
    
    """def __isub__(self, otra): # p3 -= p4
        self.precio = self.precio - otra.precio
        return self.precio
    
    def __imul__(self, otra): # p3 *= p4
        self.precio = self.precio * otra.precio
        return self.precio
    
    def __itruediv__(self, otra): # p3 /= p4
        self.precio = self.precio / otra.precio
        return self.precio
    
    def __ifloordiv__(self, otra): # p3 //= p4
        self.precio = self.precio // otra.precio
        return self.precio
    
    def __imod__(self, otra): # p3 %= p4
        self.precio = self.precio % otra.precio
        return self.precio
    
    def __ipow__(self, otra): # p3 **= p4
        self.precio = self.precio ** otra.precio
        return self.precio"""
    
    ##################### UNINARIOS #####################
    
    """Por el momento, parece ser que no funciona la
    sobreescritura en los operadores uninarios + y -
    """
    def __pos__(self):
        print("Sobreescrito")
        return self
    
    def __neg__(self):
        print("Sobreescrito")
        return -self
    
    ##################### FUNCIONES/METODOS #####################

    def __abs__(self):
        return +self
    
    def __round__(self, n=None):
        print("Sobreescrito")
        if n is None:
            return round(self.valor)
        return round(self.valor, n)
    
p1 = Producto(1, "Pantalla", 129.50)
p2 = Producto(1, "Pantalla", 129.50)
p1bis = Producto(1, "Pantallo", 129.50)

print(p1) 
# Antes de sobreescribir el metodo: <__main__.Producto object at 0x00000216326A7C90>
# Despues de sobreescribir el metodo: ID 1, Descripcion: Pantalla, Precio: 129.5

print("Son iguales?", p1 == p2) 
print("Son iguales?", p1.__eq__(p2))
# Antes de sobreescribir el metodo eq: Da False por comparar dos instancias distintas
# Despues de sobreescribir el metodo eq: Son iguales? True

p3 = Producto(3, "Teclado", 37.95)
p4 = Producto(4, "Raton", 19.80)
# Antes de sobreescribir el metodo hash: Da una excepcion: TypeError: unhashable type: 'Producto'
# Despues de sobreescribir el metodo hash: p1 y p2 al tener el mismo id, entiende que son iguales
conjunto = {p1, p2, p3, p4, p1bis}
print(*conjunto)
for p in conjunto:
    print(p)

print("Son iguales?", p1 == p2) 
print("Son iguales?", p1.__eq__(p2))

print("Son diferentes?", p1 != p2) 
print("Son diferentes?", p1.__ne__(p2))
print("Son diferentes?", p1 != p1bis)
print("Son diferentes?", p1 != p3)

print("La instancia es mayor?", p1 > p2) 
print("La instancia es mayor?", p1.__ne__(p2))

print("La instancia es mayor o igual?", p1 >= p2) 
print("La instancia es mayor o igual?", p1.__ne__(p2))

print("La instancia es menor?", p1 < p2) 
print("La instancia es menor?", p1.__ne__(p2))

print("La instancia es menor o igual?", p1 <= p2) 
print("La instancia es menor o igual?", p1.__ne__(p2))

print("Suma", p3 + p4)
# Antes de sobreescribir el metodo: TypeError: unsupported operand type(s) for +: 'Producto' and 'Producto'
# Despues de sobreescribir el metodo: 57.75
print("Resta", p3 - p4)
print("Multiplicacion", p3 * p4)
print("Division", p3 / p4)
print("Division con entero", p3 // p4)
print("Resto", p3 % p4)
print("Exponente", p3 ** p4)

p3 += p4
print("Suma con asignacion", p3)
# Antes de sobreescribir el metodo: TypeError: unsupported operand type(s) for +: 'Producto' and 'Producto'
# Despues de sobreescribir el metodo: 57.75
"""p3 -= p4
print("Resta con asignacion", p3)
p3 *= p4
print("Multiplicacion con asignacion", p3)
p3 /= p4
print("Division con asignacion", p3)
p3 //= p4
print("Division con entero con asignacion", p3)
p3 %= p4
print("Resto con asignacion", p3)
p3 **= p4
print("Exponente con asignacion", p3)
"""

a = -p3
print("Absolutos", abs(a), "Valor anterior", a)
print("Redondeo", round(a), "Valor anterior", a)

a = +p3
b = -p3
print("Positivo", a)
print("Negativo", b)
print("Positivo", p3.__pos__())
print("Negativo", p3.__neg__())
