import math

# convertir string a numero entero
dato = input("Introduce un numero: ")
print(type(dato))
# si el valor introducido no es un numero: ValueError: invalid literal for int() with base 10: 'tres'
# ValueError: invalid literal for int() with base 10: '12456mnbv'
# ValueError: invalid literal for int() with base 10: '12.56'
# ValueError: invalid literal for int() with base 10: 'True'
numero1 = int(dato)
print(type(numero1))
print(numero1)


# convertir string a numero real
# Introducir valor decimal con separador .
# ValueError: could not convert string to float: '566,6544'
# Tambien funciona con numeros enteros  75
radio = float(input("Introduce radio del circulo (75.12): "))
print("Area del circulo", math.pi * radio ** 2)  # ** es una potencia

# Redondear numeros   round(que?, decimales)
print("Area del circulo", round(math.pi * radio ** 2, 2) )


# convertir a texto
print('34', type(str(34)))
print('34.13', type(str(34.13)))
print('True', type(str(True)))