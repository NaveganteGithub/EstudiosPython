'''
    Un clase encapsulada tiene todas sus propiedades son privadas y se accede a ellas
    a traves de los metodos de acceso publicos: getter y setter
'''
class FechaEncapsulada:
    def __init__(self, dia=0, mes=0, anyo=0):
        # crear las 3 variables privadas
        self.__dia = 0
        self.__mes = 0
        self.__anyo = 0
        
        # Internamente al asignar valor a las variables llama a los metodos setter
        self.dia = dia
        self.mes = mes
        self.anyo = anyo
     
    @property
    def dia(self):
        return self.__dia

    @dia.setter
    def dia(self, dia):
        if dia > 1 and dia <= 31:
            self.__dia = dia
        else :
            print("Dia no es valido")

    @property
    def mes(self):
        return self.__mes

    @mes.setter
    def mes(self, mes):
        if mes >= 1 and mes <= 12:
            self.__mes = mes
        else:
            print("Mes no es valido")

    @property
    def anyo(self):
        return self.__anyo

    @anyo.setter
    def anyo(self, anyo):
        if anyo == 2024 or anyo == 2025:
            self.__anyo = anyo
        else:
            print("Anyo no es valido")

    def __str__(self):
        # dia/mes/año
        return f"{self.__dia}/{self.__mes}/{self.__anyo}"
    
fecha_buena = FechaEncapsulada(22, 4, 2024)
print(fecha_buena)

fecha_erronea = FechaEncapsulada(-12, 54, 3)
print(fecha_erronea)

fecha_erronea.dia = -12  # setter de dia
fecha_erronea.mes = 54
fecha_erronea.mes=10
#fecha_erronea.mes(8)  # TypeError: 'int' object is not callable
print(fecha_erronea)

print("Dia:", fecha_buena.dia)  # getter de dia






