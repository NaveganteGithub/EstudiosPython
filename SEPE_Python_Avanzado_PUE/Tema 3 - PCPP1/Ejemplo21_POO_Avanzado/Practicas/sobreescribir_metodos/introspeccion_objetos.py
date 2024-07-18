
class Producto:
    
    def __init__(self, identificator, descripcion, precio):
        self.id = identificator
        self.descripcion = descripcion
        self.precio = precio

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

    
p1 = Producto(1, "Pantalla", 129.50)
p2 = Producto(1, "Pantalla", 129.50)
p1bis = Producto(1, "Pantallo", 129.50)

print(p1) 
# Antes de sobreescribir el metodo: <__main__.Producto object at 0x00000216326A7C90>
# Despues de sobreescribir el metodo: ID 1, Descripcion: Pantalla, Precio: 129.5

p3 = Producto(3, "Teclado", 37.95)
p4 = Producto(4, "Raton", 19.80)

# Antes de sobreescribir el metodo hash: Da una excepcion: TypeError: unhashable type: 'Producto'
# Despues de sobreescribir el metodo hash: p1 y p2 al tener el mismo id, entiende que son iguales
conjunto = {p1, p2, p3, p4, p1bis}
print(*conjunto)
for p in conjunto:
    print(p)

try:
    print(p1)
    del p1
    print(p1)
except:
    pass
