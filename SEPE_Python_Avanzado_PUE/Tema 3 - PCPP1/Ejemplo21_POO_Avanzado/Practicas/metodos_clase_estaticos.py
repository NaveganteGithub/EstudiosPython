class Producto:
    
    __contador = 0  # privada

    def __init__(self, descripcion, precio):
        Producto.__contador += 1
        self.id = Producto.__contador
        self.descripcion = descripcion
        self.precio = precio

    @staticmethod
    def getContador():
        print("Metodo estatico getContador()")
        # No se puede acceder a los recursos de instancia
        # print(self.descripcion)
        # Solo puedo acceder a los recursos estaticos
        Producto.verContador()
        return Producto.__contador

    @classmethod
    def verContador(cls):
        print("Metodo de clase getContador()")
        # No se puede acceder a los recursos de instancia
        # print(self.descripcion)
        # cls.getContador()
        return Producto("xxxxx", 100)
    
    def __str__(self):
        return f"ID: {self.id}, Descripcion: {self.descripcion}, Precio: {self.precio}"

print("Contador:", Producto.getContador())
p1 = Producto("Pantalla", 129.50)
print(p1)
print("Contador:", Producto.getContador())
print("Contador:", p1.getContador())

print("Contador de clase:", Producto.verContador())
print("Contador de clase:", p1.verContador())

p3 = Producto.verContador()
print(p3)