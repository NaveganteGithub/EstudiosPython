class Producto:
    def __init__(self, id, descripcion, precio):
        self.id = id
        self.descripcion = descripcion
        self.precio = precio
     
    # cuando mostremos el objeto, represente su estado (contenido, valores)    
    def __str__(self):
        return f"ID: {self.id}, Descripcion: {self.descripcion}, Precio: {self.precio}"
    
    # Retorna un valor booleano indicando si esta instancia es igual a la recibida como argumento
    def __eq__(self, otra):
        return self.id == otra.id and self.descripcion == otra.descripcion and self.precio == otra.precio
    
    # Retorna un valor numerico, imprendiscible para comparar elementos del conjunto
    def __hash__(self):
        suma = 0
        for letra in self.descripcion:
            suma += ord(letra)
        
        return int(self.id + suma + self.precio)
        #return int(self.id + len(self.descripcion) + self.precio)
    
    # Devuelve un numero que sera el resultado de aplicar una suma
    def __add__(self, otra):
        return self.precio + otra.precio
    


p1 = Producto(1, "Pantalla", 129.50)
p1bis = Producto(1, "Pantallo", 129.50)
p2 = Producto(1, "Panttll", 129.50)


print(p1) # <__main__.Producto object at 0x11f3d2e80>
print(p1) # ID: 1, Descripcion: Pantalla, Precio: 129.5
print(p1.__str__()) # ID: 1, Descripcion: Pantalla, Precio: 129.5

print("Son iguales?", p1==p2)  # Son iguales? False   Compara direcciones de memoria
print("Son iguales despues de sobreescribir __eq__?", p1==p2)  # Son iguales? True
print("Son iguales despues de sobreescribir __eq__?", p1.__eq__(p2)) # Son iguales? True

p3 = Producto(3, "Teclado", 37.95)
p4 = Producto(4, "Raton", 19.80)

print(p3 + p4) # TypeError: unsupported operand type(s) for +: 'Producto' and 'Producto'
print(p3 + p4) # 57.75


''' Los conjuntos son colecciones que no permiten elementos duplicados '''
# p1 y p2 al tener el mismo id, entiende que son iguales
conjunto = {p1,p1bis, p2,p3,p4}
for p in conjunto:
    print(p)

