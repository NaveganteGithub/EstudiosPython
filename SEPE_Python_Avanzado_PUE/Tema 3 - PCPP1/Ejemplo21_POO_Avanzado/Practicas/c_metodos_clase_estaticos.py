class Producto:

    desc = ""
    __contador = 0  # privada

    def __init__(self, descripcion, precio):
        self.id = Producto.__contador
        self.descripcion = descripcion
        self.precio = precio
        Producto.__contador += 1
        Producto.desc = descripcion

    # Los metodos de clase permiten trabajar con una alternativa
    # al metodo __init__ a la hora de instanciar objetos
    @classmethod
    def ver_contador(cls):
        print("Metodo de clase verContador()")
        # No se puede acceder a los recursos de instancia
        # print(self.descripcion)
        # cls.getContador()

        # Podemos acceder a las variables de clase
        print(cls.__contador)
        # return Producto("xxxxx", 100)
        return Producto(cls.desc, 100)

    # Los metodos estaticos nos permite trabajar
    # directamente con clase, pero a diferencia
    # de los metodos de clase no nos ofrece una
    # alternativa a __init__ solo es un metodo
    # para usar directamente con la clase.
    # Un metodo estatico solo se puede acceder
    # a otros metodos estaticos.
    @staticmethod
    def get_contador():
        print("Metodo estatico getContador()")
        # No se puede acceder a los recursos de instancia
        # print(self.descripcion)
        # Solo puedo acceder a los recursos estaticos
        Producto.ver_contador()
        return Producto.__contador
    
    def __str__(self):
        return f"ID: {self.id}, Descripcion: {self.descripcion}, Precio: {self.precio}"


print("Contador:", Producto.get_contador())
p1 = Producto("Pantalla", 129.50)
print(p1)
print("Contador:", Producto.get_contador())
print("Contador:", p1.get_contador())

print("Contador de clase:", Producto.ver_contador())
print("Contador de clase:", p1.ver_contador())

p3 = Producto.ver_contador()
print(p3)

print(Producto.ver_contador().__repr__())  # <__main__.Producto object at 0x000001DB97A83080>

"""Metodo estatico getContador()
Metodo de clase verContador()
0
Contador: 1
ID: 1, Descripcion: Pantalla, Precio: 129.5
Metodo estatico getContador()
Metodo de clase verContador()
2
Contador: 3
Metodo estatico getContador()
Metodo de clase verContador()
3
Contador: 4
Metodo de clase verContador()
4
Contador de clase: ID: 4, Descripcion: Pantalla, Precio: 100
Metodo de clase verContador()
5
Contador de clase: ID: 5, Descripcion: Pantalla, Precio: 100
Metodo de clase verContador()
6
ID: 6, Descripcion: Pantalla, Precio: 100
Metodo de clase verContador()
7
<__main__.Producto object at 0x0000022FD3D43080>

"""
