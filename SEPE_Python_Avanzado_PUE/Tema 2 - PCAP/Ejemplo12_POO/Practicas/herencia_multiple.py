class Animal:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return "{}, {}".format(self.nombre, self.edad)

class ProductoVenta:

    def __init__(self, codigo, precio):
        self.codigo = codigo
        self.precio = precio

    def __str__(self):
        return "{}, {}".format(self.codigo, self.precio)

class Perro(Animal, ProductoVenta):

    def __init__(self, nombre, edad, codigo, precio, vacunado, sexo):
        # super().__init__(nombre, edad) # Animal
        # super().__init__(codigo, precio) # ProductoVenta
        Animal.__init__(self, nombre, edad)
        ProductoVenta.__init__(self, codigo, precio)
        self.vacunado = vacunado
        self.sexo = sexo

    def __str__(self):
        # return super().__str__() + super().__str__() + " {} {}".format(self.vacunado, self.sexo)
        return Animal.__str__(self) + ProductoVenta.__str__(self) + " {} {}".format(self.vacunado, self.sexo)

animal = Animal("Nano", 5)
pv = ProductoVenta(45454645, 23.67)
perro = Perro("Nano", 5, 45454645, 23.67, True, "M")

print(perro)

print(Perro.__bases__)
