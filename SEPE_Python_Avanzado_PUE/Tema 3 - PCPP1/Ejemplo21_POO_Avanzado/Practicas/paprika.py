# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 12:53:08 2024

@author: Ismael Montoro Peñasco
"""

'''
Un clase encapsulada tiene todas sus propiedades 
son privadas y se accede a ellas a traves de los 
metodos de acceso publicos: getter y setter
'''
# # from paprika import to_string
# # from paprika import equals_and_hashcode
# from paprika import data
# # from paprika import singleton


# # @to_string
# # @equals_and_hashcode
# @data
# # @singleton
import paprika

@paprika.to_string
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
        if dia > 1 and dia <= 31:
            self.__dia = dia
        else :
            print("Dia no es valido")

    @property    
    def mi_Mes(self):
        return self.__mes
    
    @mi_Mes.setter
    def mi_Mes(self, mes):
        if mes >= 1 and mes <= 12:
            self.__mes = mes
        else:
            print("Mes no es valido")
    
    @property
    def mi_Anyo(self):
        return self.__anyo
    
    @mi_Anyo.setter
    def mi_Anyo(self, anyo):
        if anyo == 2024 or anyo == 2025:
            self.__anyo = anyo
        else:
            print("Anyo no es valido")

    def __str__(self):
        return f"{self.__dia}/{self.__mes}/{self.__anyo}"

    
fecha_buena = FechaEncapsulada(12, 4, 2024)    
print(fecha_buena)  
    
fecha_erronea = FechaEncapsulada(-12, 87, 3)    
print(fecha_erronea)    

fecha_erronea.mi_dia = -12
fecha_erronea.mi_Mes = 54
# fecha_buena.mi_dia(8) # TypeError: 'int' object is not callable

print(fecha_erronea)

print()