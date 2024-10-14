from math import *

"""
El radian o radianes en plural, es un calculo que nos ayuda a determinar el angulo
de una circunferencia con x longitud

Longitud del arco = X
Radio de la circunferencia = Y
Radianes = Z

X / Y = Z
"""
print("Convierte el angulo de una circunferencia de la medida grados a radianes", radians(90))

for angulo_triangulo in [0,30,45,60,90]:
    print("Seno de un triangulo con angulo", angulo_triangulo, ":", sin(angulo_triangulo))

for angulo_triangulo in [0,30,45,60,90]:
    print("Coseno de un triangulo con angulo", angulo_triangulo, ":", cos(angulo_triangulo))

print("Seno de 90:", sin(radians(90)))
print("Coseno de 90:", cos(radians(90)))
print("Seno hiperbolico de 90:", sinh(radians(90)))
print("Coseno hiperbolico de 90:", cosh(radians(90)))

"""
Un logaritmo es un calculo en cual tenemos que averiguar que exponente necesitamos
para llegar desde un numero base hasta un resultado

    logb(y)

Ejemplo:

    log2(8)

1º Averiguamos el numero base y el resultado a obtener

    La Base (b) = 2
    Resultado a obtener (y) = 8

2º Intentaremos calcular averiguar el exponente, por supuesto puedes usar Calculadora 
o Python si los numeros son demasiado complejos

    2 ** x = 8

    En este caso es 3 porque 2 elevado a 3 es igual a 8
"""
print("log base 2 numero 8:", log(8, 2))

print("log base 10 numero 12345.7654:", log(12345.7654, 10))
print("log base 10 numero 12345.7654:", log10(12345.7654))

print("log base 2 numero 12345.7654:", log(12345.7654, 2))
print("log base 2 numero 12345.7654:", log2(12345.7654))

print("potencia 2 elevado a 8:", pow(2,8))
print("exponente e (euclides) elevado a 5:", exp(5))

print("Redondeo al alza 3.89:", ceil(3.89))  # 4
print("Redondeo al alza 3.19:", ceil(3.19))  # 4
print("Redondeo a la baja 3.89:", floor(3.89))  # 3
print("Redondeo a la baja 3.19:", floor(3.19))  # 3
print("Truncar 3.89:", trunc(3.89))  # 3
print("Truncar 3.19:", trunc(3.19))  # 3

# La funcion round no es del modulo math, es universal
print("Redondear a 2 decimales 5,552821:", round(5.552821, 2))

print("Factorial de 5:", factorial(5))

"""
https://www.youtube.com/watch?v=vklKtK5oCfg 

Distancia euclidiana multidimensional desde el origen a un punto.

Aproximadamente equivalente a:
    sqrt(sum(x**2 for x in coordinates))
"""
print(hypot(5, 7))
print(hypot(2, 1))
print(hypot(2, 2))
print(hypot(5, 7, 2, 3))

print("Raiz cuadrada de 25:", sqrt(4))
print("Raiz cuadrada de 25:", sqrt(9))
print("Raiz cuadrada de 25:", sqrt(25))
print("Raiz cuadrada de 8:", sqrt(8))