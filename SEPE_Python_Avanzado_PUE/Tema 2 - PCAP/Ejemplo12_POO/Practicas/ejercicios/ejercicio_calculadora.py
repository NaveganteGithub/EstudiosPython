################## Ejercicio 3 ##################

'''
    Crea una clase calculadora:
        Metodos:
            Sumar
            Restar
            Multiplicaciones
            Divisiones

    Hacer que el usuario introduzca dos numeros

    Llama a los 4 metodos
'''


class Calculadora:

    def __init__(self, *factores: int):
        self.factores = factores

    def sumar(self):
        return sum(self.factores)

    def restar(self):
        resultado = self.factores[0]
        for factor in self.factores[1:]:
            resultado -= factor
        return resultado

    def multiplicar(self):
        resultado = self.factores[0]
        for factor in self.factores[1:]:
            resultado *= factor
        return resultado

    def dividir(self):
        resultado = self.factores[0]
        try:
            for factor in self.factores[1:]:
                resultado /= factor
        except:
            return 0
        else:
            return resultado


factor_1 = float(input("Numero 1: "))
factor_2 = float(input("Numero 2: "))

calculadora = Calculadora(factor_1, factor_2)

print(calculadora.sumar())
print(calculadora.restar())
print(calculadora.multiplicar())
print(calculadora.dividir())


##

class Calculadora:
    def sumar(self, factor1, factor2):
        return factor1 + factor2

    def restar(self, factor1, factor2):
        return factor1 - factor2

    def multiplicar(self, factor1, factor2):
        return factor1 * factor2

    def dividir(self, factor1, factor2):
        try:
            return factor1 / factor2
        except:
            return 0


factor_1 = float(input("Numero 1: "))
factor_2 = float(input("Numero 2: "))

calculadora = Calculadora()

print(calculadora.sumar(factor_1, factor_2))
print(calculadora.restar(factor_1, factor_2))
print(calculadora.multiplicar(factor_1, factor_2))
print(calculadora.dividir(factor_1, factor_2))