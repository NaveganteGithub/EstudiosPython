"""
    Ejemplo de tipos de datos en Python
"""

# numeros enteros (int)
numero1 = 5
numero2 = 4
suma = numero1 + numero2
print(suma)
print("Resultado de la suma:", suma, type(suma))
print("Resultado de la suma: " + str(suma) + " " + str(type(str(suma))) ) # concatenar en Python es mas lioso


# numeros reales (float)
base = 5.78
altura = 9.23
triangulo = base * altura / 2
print("Area del triangulo", triangulo, type(triangulo))

# booleanos: True o False (bool)
soltero = True
print("Estas soltero?", soltero, type(soltero))

# cadenas de texto (str)
# se pueden utilizan comillas simples o dobles
nombre = "Pepito"
apellido = 'Perez'
edad = 27
print(nombre, apellido, type(nombre), type(edad))

print("2" + str(2))   # Error el operador de concatenacion + solo puede unir strings
resultado = "2" + 2
print(resultado)