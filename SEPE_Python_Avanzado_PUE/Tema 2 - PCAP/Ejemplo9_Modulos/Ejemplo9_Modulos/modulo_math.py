from math import *

print("Seno de 90:", sin(radians(90)))
print("Coseno de 90:", cos(radians(90)))
print("Seno hiperbolico de 90:", sinh(radians(90)))
print("Coseno hiperbolico de 90:", cosh(radians(90)))

print("log base 10 numero 12345.7654:", log(12345.7654, 10))
print("log base 10 numero 12345.7654:", log10(12345.7654))

print("log base 2 numero 12345.7654:", log(12345.7654, 2))
print("log base 2 numero 12345.7654:", log2(12345.7654))

print("potencia 2 elevado a 8:", pow(2,8))
print("exponente e elevado a 5:", exp(5))

print("Redondeo al alza 3.89:", ceil(3.89))  # 4
print("Redondeo al alza 3.19:", ceil(3.19))  # 4
print("Redondeo a la baja 3.89:", floor(3.89))  # 3
print("Redondeo a la baja 3.19:", floor(3.19))  # 3
print("Truncar 3.89:", trunc(3.89))  # 3
print("Truncar 3.19:", trunc(3.19))  # 3

# La funcion round no es del modulo math, es universal
print("Redondear a 2 decimales 5,552821:", round(5.552821, 2))

print("Factorial de 4:", factorial(4))