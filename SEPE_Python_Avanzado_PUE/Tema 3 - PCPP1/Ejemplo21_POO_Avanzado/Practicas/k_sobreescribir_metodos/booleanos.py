
class Producto:

    def __init__(self, identificator, descripcion, precio):
        self.id = identificator
        self.descripcion = descripcion
        self.precio = precio

    def __str__(self):
        return f"ID {self.id}, Descripcion: {self.descripcion}, Precio: {self.precio}"

    # Retorna un valor booleano indicando si esta instancia es igual a la recibida como argumento
    # self representa el objeto a comparar, el segundo parametro representa el comparador
    def __eq__(self, otra):  # p1 == p2
        print("Sobreescrito")
        return self.id == otra.id and self.descripcion == otra.descripcion and self.precio == otra.precio

    # Retorna un valor booleano indicando si esta instancia no es igual a la recibida como argumento
    # self representa el objeto a comparar, el segundo parametro representa el comparador
    def __ne__(self, otra):  # p1 != p2
        print("Sobreescrito")
        # print(self.id != otra.id, self.descripcion != otra.descripcion, self.precio != otra.precio)
        return self.id != otra.id and self.descripcion != otra.descripcion and self.precio != otra.precio

    # Retorna un valor booleano indicando si esta instancia tiene un valor mayor, o varios valores mayores,
    # a la instancia recibida como argumento
    # self representa el objeto a comparar, el segundo parametro representa el comparador
    def __gt__(self, otra):  # p1 > p2
        print("Sobreescrito")
        return self.id > otra.id and self.descripcion > otra.descripcion and self.precio > otra.precio

    # Retorna un valor booleano indicando si esta instancia tiene un valor mayor o igual,
    # o varios valores mayores o iguales, a la instancia recibida como argumento
    # self representa el objeto a comparar, el segundo parametro representa el comparador
    def __ge__(self, otra):  # p1 >= p2
        print("Sobreescrito")
        return self.id >= otra.id and self.descripcion >= otra.descripcion and self.precio >= otra.precio

    # Retorna un valor booleano indicando si esta instancia tiene un valor menor, o varios
    # valores menores, a la instancia recibida como argumento
    # self representa el objeto a comparar, el segundo parametro representa el comparador
    def __lt__(self, otra):  # p1 < p2
        print("Sobreescrito")
        return self.id < otra.id and self.descripcion < otra.descripcion and self.precio < otra.precio

    # Retorna un valor booleano indicando si esta instancia tiene un valor menor, o varios
    # valores menores a la instancia recibida como argumento
    # self representa el objeto a comparar, el segundo parametro representa el comparador
    def __le__(self, otra):  # p1 <= p2
        print("Sobreescrito")
        return self.id <= otra.id and self.descripcion <= otra.descripcion and self.precio <= otra.precio


p1 = Producto(1, "Pantalla", 129.50)
p2 = Producto(1, "Pantalla", 129.50)
p1bis = Producto(1, "Pantallo", 129.50)
p3 = Producto(3, "Teclado", 37.95)
p4 = Producto(4, "Raton", 19.80)

print("Son iguales?", p1 == p2)
print("Son iguales?", p1.__eq__(p2))
# Antes de sobreescribir el metodo eq: Da False por comparar dos instancias distintas
# Despues de sobreescribir el metodo eq: Son iguales? True

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
