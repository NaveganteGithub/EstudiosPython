class Producto:
    # Variables de clase: solo hay una copia en la clase
    __contador = 0  # privada

    def __init__(self, descripcion, precio):
        Producto.__contador += 1
        self.id = Producto.__contador
        self.descripcion = descripcion
        self.precio = precio

    @staticmethod
    def getContador():
        print("Metodo estatico getContador()")
        # No puedo acceder a los recursos de instancia
        #print(self.descripcion)
        
        # Solo puedo acceder a los recursos estaticos
        Producto.verContador()
        return Producto.__contador
    
    @classmethod
    def verContador(cls):
        print("Metodo clase verContador()")
        # No puedo acceder a los recursos de instancia
        #print(cls(descripcion) )
        #cls.getContador()
        return Producto("xxxxx",100)

    def __str__(self):
        return f"ID: {self.id}, Descripcion: {self.descripcion}, Precio: {self.precio}"

print("Contador:", Producto.getContador())

p1 = Producto("Pantalla", 129.50)
print(p1)

# Probar el metodo estatico
print("Contador:", Producto.getContador())
print("Contador:", p1.getContador())

# Probar el metodo de clase
print("Contador de clase:", Producto.verContador())
print("Contador de clase:", p1.verContador())

# El metodo de clase puede actuar como constructor
p3 = Producto.verContador()
print(p3)
