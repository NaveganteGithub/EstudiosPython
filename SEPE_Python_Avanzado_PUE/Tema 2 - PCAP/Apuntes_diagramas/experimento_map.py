# Extraer datos de una clase
class Numeros:

    def __init__(self, num1, num2, num3) -> None:
        self.before = num1
        self.now = num2
        self.after = num3

    def __str__(self) -> str:
        return self.before + " " + self.now + " " + self.after
    
numeros = [Numeros(5,4,6), Numeros(1,2,3), Numeros(5,7,7), Numeros(1,5,6)]

def how_is_now(num: Numeros):
    return num.now

numeros_now = list(map(how_is_now, numeros))
print(numeros_now)
