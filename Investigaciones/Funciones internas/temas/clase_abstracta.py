from abc import ABC, abstractmethod

class color(ABC):
    @abstractmethod
    def rgb(self):
        pass

    @abstractmethod
    def nombre(self):
        pass
    
class rojo(color):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Red"
        self.red = 255
        self.green = 0
        self.blue = 0

    def rgb(self):
        return self.red, self.green, self.blue

    def nombre(self):
        return self.name
    
class azul(color):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Azul"
        self.blue = 255

    def rgb(self):
        return self.blue

    def nombre(self):
        return self.name
    
    def nivel_confianza(self, ajuste: int):
        return 3 ** (self.blue // ajuste) * 2

class personalizado(color):
    def __init__(self, nomb: str, rgb: list) -> None:
        super().__init__()
        self.nombre_color = nomb
        self.colores = rgb

    def rgb(self):
        return self.colores[0], self.colores[1], self.colores[2]

    def nombre(self):
        return self.nombre_color
    
red = rojo()
blue = azul()
custom = personalizado("Green", [0, 255, 0])

rgb_red, rgb_green, rgb_blue = red.rgb()
print(red.nombre(), rgb_red, rgb_green, rgb_blue)

print(blue.nombre(), red.rgb())

print(custom.nombre(), custom.rgb()[0], custom.rgb()[1], custom.rgb()[2])


class rojo_infractor(color):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Red"
        self.red = 255
        self.green = 0
        self.blue = 0

    def rgb(self):
        return self.red, self.green, self.blue
    
try:
    red_infractor = rojo_infractor()
    print(rgb_red, rgb_green, rgb_blue)
except TypeError:
    print("La clase 'rojo_infractor' incumple con la clase abstracta.")