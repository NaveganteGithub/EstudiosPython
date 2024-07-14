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
        # return self.id == otra.id and self.descripcion == otra.descripcion and self.precio == otra.precio
        return self.id == otra.id and self.descripcion == otra.descripcion and self.precio == otra.precio
    
    # Retorna un valor booleano indicando si esta instancia no es igual a la recibida como argumento
    # self representa el objeto a comparar, el segundo parametro representa el comparador
    def __ne__(self, otra): # p1 != p2
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
    
    def __sub__(self, otra): # p3 - p4
        return self.precio - otra.precio
    
    def __mul__(self, otra): # p3 * p4
        return self.precio * otra.precio
    
    def __div__(self, otra): # p3 / p4
        return self.precio / otra.precio
    
    def __floordiv__(self, otra): # p3 // p4
        return self.precio // otra.precio
    
    def __mod__(self, otra): # p3 % p4
        return self.precio % otra.precio
    
    def __pow__(self, otra): # p3 ** p4
        return self.precio ** otra.precio
    
    ##################### ASIGNACION #####################

    def __iadd__(self, otra): # p3 += p4
        return 
    
p1 = Producto(1, "Pantalla", 129.50)
p2 = Producto(1, "Pantalla", 129.50)
p1bis = Producto(1, "Pantallo", 129.50)

print(p1) 
# Antes de sobreescribir el metodo: <__main__.Producto object at 0x00000216326A7C90>
# Despues de sobreescribir el metodo: ID 1, Descripcion: Pantalla, Precio: 129.5

print("Son iguales?", p1 == p2) 
print("Son iguales?", p1.__eq__(p2))
# Antes de sobreescribir el metodo: Da False por comparar dos instancias distintas
# Despues de sobreescribir el metodo: Son iguales? True

p3 = Producto(3, "Teclado", 37.95)
p4 = Producto(4, "Raton", 19.80)

print(p3 + p4)

# Antes de sobreescribir el metodo: TypeError: unsupported operand type(s) for +: 'Producto' and 'Producto'
# Despues de sobreescribir el metodo: 57.75

# p1 y p2 al tener el mismo id, entiende que son iguales
conjunto = {p1, p2, p3, p4, p1bis}
print(*conjunto)
for p in conjunto:
    print(p)