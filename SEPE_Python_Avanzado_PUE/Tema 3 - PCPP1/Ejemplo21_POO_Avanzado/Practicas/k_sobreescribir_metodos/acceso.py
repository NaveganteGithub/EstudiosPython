class Producto:

    def __init__(self, identificator, descripcion, precio):
        self.id = identificator
        self.descripcion = descripcion
        self.precio = precio

    def __len__(self):
        self.cont = 0
        for _ in self.descripcion:
            self.cont += 1
        return self.cont

    def __iter__(self):
        print(self.__dict__)
        # return iter(self.__dict__)
        return iter(self.__dict__.values())

    def __contains__(self, item):
        verdadero = f"Productos contiene {item}"
        falso = f"Productos no contiene {item}"
        if item in self.__dict__:
            print(verdadero)
            return verdadero
        else:
            print(falso)
            return falso

    def __getitem__(self, item):
        valor = list(self.__dict__.values())
        return valor[item]

    def __setitem__(self, key, value):
        if key in list(self.__dict__):
            print(key, value)
            exec(f"self.{key} = {value}")
        else:
            raise TypeError

    def __delitem__(self, key):
        exec(f"del self.{key}")
        print(f"Variable {key} eliminada")


class Producto2:

    def __init__(self, identificator, descripcion, precio):
        self.id = identificator
        self.descripcion = descripcion
        self.precio = precio

    def __getitem__(self, item):
        valor = self.__dict__
        return valor[item]


p1 = Producto(3, "Teclado", 37.95)
p2 = Producto2(3, "Teclado", 37.95)
print(len(p1))

print("Por id:", p1[1])
print("Por clave:", p2['descripcion'])


for i in p1:
    print(i)

p1['descripcion'] = 1
print(p1[0])

del p1['cont']
# print(p1['cont'])
del p1['descripcion']
# print(p1['descripcion'])
"""Traceback (most recent call last):
  
    print(p1['descripcion'])
          ~~^^^^^^^^^^^^^^^
  
    return valor[item]
           ~~~~~^^^^^^
TypeError: list indices must be integers or slices, not str
"""

print('descripcion' in p1)
print('id' in p1)
'descripcion' in p1
'id' in p1
