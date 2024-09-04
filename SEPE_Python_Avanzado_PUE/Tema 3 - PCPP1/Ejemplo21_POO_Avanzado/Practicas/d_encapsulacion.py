"""Un clase encapsulada tiene todas sus propiedades
son privadas y se accede a ellas a traves de los
metodos de acceso publicos: getter y setter
"""


class FechaEncapsulada:
    
    def __init__(self, dia, mes, anyo):
        self.__dia = 0
        self.__mes = 0
        self.__anyo = 0
        
        self.mi_dia = dia
        self.mi_Mes = mes
        self.mi_Anyo = anyo
    
    @property
    def mi_dia(self):
        return self.__dia

    @mi_dia.setter
    def mi_dia(self, dia):
        # if dia > 1 and dia <= 31:
        if 1 < dia <= 31:
            self.__dia = dia
        else:
            print("Dia no es valido")

    @mi_dia.deleter
    def mi_dia(self):
        print(f"Eliminando {self.__dia}")
        del self.__dia

    @property    
    def mi_Mes(self):
        return self.__mes
    
    @mi_Mes.setter
    def mi_Mes(self, mes):
        # if mes >= 1 and mes <= 12:
        if 1 <= mes <= 12:
            self.__mes = mes
        else:
            print("Mes no es valido")

    @mi_Mes.deleter
    def mi_Mes(self):
        del self.__mes

    @property
    def mi_Anyo(self):
        return self.__anyo
    
    @mi_Anyo.setter
    def mi_Anyo(self, anyo):
        # if anyo == 2024 or anyo == 2025:
        if anyo in [2024, 2025]:
            self.__anyo = anyo
        else:
            print("Anyo no es valido")

    @mi_Anyo.deleter
    def mi_Anyo(self):
        del self.__anyo

    def __str__(self):
        return f"{self.__dia}/{self.__mes}/{self.__anyo}"

    
fecha_buena = FechaEncapsulada(12, 4, 2024)    
print(fecha_buena)  # 12/4/2024
    
fecha_erronea = FechaEncapsulada(-12, 87, 3)
"""
Dia no es valido
Mes no es valido
Anyo no es valido
"""
print(fecha_erronea)  # 0/0/0

fecha_erronea.mi_dia = -12  # Dia no es valido
fecha_erronea.mi_Mes = 54  # Mes no es valido
# fecha_buena.mi_dia(8) # TypeError: 'int' object is not callable

print(fecha_erronea)  # 0/0/0
print(fecha_erronea.mi_dia)  # 0

setattr(fecha_erronea, "_FechaEncapsulada__dia", 55555)
print(getattr(fecha_erronea, "_FechaEncapsulada__dia"))  # 55555

del fecha_erronea.mi_dia