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
    
    # Cuando mostremos el objeto, represente su estado (contenido, valores)    
    def __str__(self):
        return f"ID {self.id}, Descripcion: {self.descripcion}, Precio: {self.precio}"
    
    # Retorna un valor booleano indicando si esta instancia es igual a la recibida como argumento
    # self representa el objeto a comparar, el segundo parametro representa el comparador
    def __eq__(self, otra): # p1 == p2
        return self.id == otra.id and self.descripcion == otra.descripcion and self.precio == otra.precio
    
    # Retorna un numero que sera el resultado de apliar una suma
    # self representa el objeto a comparar, el segundo parametro representa el comparador
    def __add__(self, otra): # p3 + p4
        return self.precio + otra.precio
    
    # Retorna un valor numerico, imprendiscible para comparar elementos del conjunto
    def __hash__(self):
        # return int(self.id + len(self.descripcion) + self.precio)
        
        suma = 0
        for letra in self.descripcion:
            suma += ord(letra)
            
        return int(self.id + suma + self.precio)
    
p1 = Producto(1, "Pantalla", 129.50)
p2 = Producto(1, "Pantalla", 129.50)
p1bis = Producto(1, "Pantallo", 129.50)

print(p1) 
# Antes de sobreescribir el metodo: <__main__.Producto object at 0x00000216326A7C90>
# Despues de sobreescribir el metodo: ID 1, Descripcion: Pantalla, Precio: 129.5

print("Son iguales?", p1 == p2) 
print("Son iguales?", p1.__eq__(p2))
# Antes de sobreescribir el metodo: Da False por compara dos instancias distintas
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