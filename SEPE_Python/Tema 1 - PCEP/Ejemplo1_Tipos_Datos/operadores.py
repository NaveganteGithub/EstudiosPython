# Operadores aritmeticos (+, -, *, /, %, **, //)
numero1 = 7
numero2 = 3
print("Suma", numero1 + numero2)
print("Resta", numero1 - numero2)
print("Multiplicacion", numero1 * numero2)
print("Division", numero1 / numero2)  # siempre devuelve el tipo real
print("Modulo o resto de division", numero1 % numero2)
print("Potencia", numero1 ** numero2)
print("Division entera", numero1 // numero2)

#  print(6 / 3) devuelve 2.0


# Operadores de asignacion (+=, -=, *=, /=, %=, **=, //=)
# numero1 = numero1 + 3
numero1 += 3
print(numero1)

# En Python no existen los incrementos, ni decrementos
# numero2++ 
# ++numero2 
# numero2--
# --numero2

# Operadores de comparacion (>, <, >=, <=, ==, !=)
print("El numero1 es menor que el numero2", numero1 < numero2)
print("El numero1 es mayor que el numero2", numero1 > numero2)
print("El numero1 es igual que el numero2", numero1 == numero2)
print("El numero1 es distinto que el numero2", numero1 != numero2)
print("El nombre1 es igual que el nombre2", 'Juan' == 'Juan')

# Operadores logicos (and, or, not)
print("and:", (numero1 > numero2) and (numero2 == 5))
print("or:", (numero1 > numero2) or (numero2 == 5))
print("not:", not(numero1 > numero2))
print("not:", not(numero2 == 5))


# Operadores de identidad (is, is not)
n1 = 6
n2 = 6
print("Es el mismo contenido??", n1 == n2)
print("Es el mismo contenido??", n1 is n2)

nombres1 = ['Juan', 'Maria']
nombres2 = ['Juan', 'Maria']
print("Es el mismo contenido??", nombres1 == nombres2)  # True, porque las listas son iguales
print("Es el mismo contenido??", nombres1 is nombres2)  # False, las variables contienen direcciones de memoria
print(type(nombres1))


# Operadores de pertenencia (in, not in)
print('Luis' in nombres1)     # False
print('Luis' not in nombres1) # True
print('Juan' in nombres1)     # True
print('Juan' not in nombres1) # False

# Replicar una cadena
print("hola" * 2)   # holahola