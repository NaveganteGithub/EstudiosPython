'''
    Crear la clase calculadora con 4 metodos: sumar, restar, multiplicar, dividir
    Solicitar 2 numeros al usuario
    llamar a los 4 metodos
'''

class Calculadora:
    # si no pongo constructor, coge el constructor por defecto
    # Calculadora()
    '''
        def __init__(self):
            pass
    '''

    # Metodos de instancia porque reciben como argumento (self)
    # Estos metodos se invocan a traves del objeto   obj.metodo()
    def sumar(self, num1, num2):
        return num1 + num2

    def restar(self, num1, num2):
        return num1 - num2

    def multiplicar(self, num1, num2):
        return num1 * num2

    def dividir(self, num1, num2):
        resultado = 0
        try:
            resultado = num1 / num2
        except:
            print("Ha ocurrido un error")
        return resultado

n1 = float(input("Introduce primer numero: "))
n2 = float(input("Introduce segundo numero: "))

# Para poder llamar a los metodos necesito una instancia de Calculadora
calcu = Calculadora()
print(f"{n1} + {n2} = {calcu.sumar(n1,n2)}")
print(f"{n1} - {n2} = {calcu.restar(n1,n2)}")
print(f"{n1} * {n2} = {calcu.multiplicar(n1,n2)}")
print(f"{n1} / {n2} = {calcu.dividir(n1,n2)}")

