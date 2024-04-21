"""
Aquí tienes 10 enunciados de ejercicios de Python para que practiques:

1. **Ejercicio 1**: Escribe un programa que imprima "Hola Mundo" en la consola.
2. **Ejercicio 2**: Crea una función que tome dos números como argumentos y devuelva su suma.
3. **Ejercicio 3**: Escribe un programa que pida al usuario su nombre y luego lo salude.
4. **Ejercicio 4**: Crea una función que tome una lista de números y devuelva el mayor de ellos.
5. **Ejercicio 5**: Escribe un programa que imprima todos los números del 1 al 10.
6. **Ejercicio 6**: Crea una función que tome una cadena y devuelva la misma cadena pero en reversa.
7. **Ejercicio 7**: Escribe un programa que pida al usuario un número y luego imprima si el número es par o impar.
8. **Ejercicio 8**: Crea una función que tome una lista y devuelva una nueva lista con los elementos únicos de la lista original.
9. **Ejercicio 9**: Escribe un programa que imprima los primeros 10 números de la serie de Fibonacci.
10. **Ejercicio 10**: Crea una función que tome una lista de números y devuelva la suma de todos los números de la lista.

Espero que estos ejercicios te ayuden a practicar Python. ¡Buena suerte! 😊

Origen: Conversación con Bing, 18/1/2024
(1) Ejercicios de Programación con Python | Aprende con Alf. https://aprendeconalf.es/docencia/python/ejercicios/.
(2) Ejercicios de programación Python con solución. https://pythondiario.com/ejercicios-de-programacion-python.
(3) 10 Ejercicios resueltos de Python Funciones – Digital Nest. https://bing.com/search?q=10+ejercicios+de+python.
(4) 10 Ejercicios resueltos de Python – Condicionales – Digital Nest. https://digitalnestweb.com/10-ejercicios-resueltos-de-python-condicionales/.
(5) 10 Ejercicios resueltos de Python Funciones – Digital Nest. https://digitalnestweb.com/10-ejercicios-resueltos-de-python-funciones/.
(6) 10 Ejercicios resueltos de Python Listas – Digital Nest. https://digitalnestweb.com/10-ejercicios-resueltos-de-python-listas/.

"""

# Ej 1

print("Hola Mundo")

# Ej 2

def suma(a:int, b:int):
    return a + b

print(suma(5, 2))

# Ej 3

nombre = input("¿Cual es tu nombre? ")
print("Hola", nombre)

# Ej 4

lista = [5,8,9,2,6,4,10]

def num_mayor(lista: list):
    return max(lista)

print(num_mayor(lista))

# Ej 5

for i in range(1,11):
    print(i)

# Ej 6

espejo = input("Introduce una cadena: ")
for i in reversed(espejo):
    print(i, end="")

print()

# Ej 7

num = int(input("Introduce un numero: "))
print("Es par" if num % 2 == 0 else "Es impar")

# Ej 8

lista = [5,8,9,2,6,4,10,5,9,2,1,5,9,10,9,6,1,10]

def eliminar_redundancias(lista: list):
    return list(set(lista))

print("La lista", lista, "ha sido resumida a", eliminar_redundancias(lista))

# Ej 9

fibonacci = [0,1]

for _ in range(8):
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

print(fibonacci)

# Ej 10

lista = [5,8,9,2,6,4,10,5,9,2,1,5,9,10,9,6,1,10]
print("Resultado de la suma", sum(lista))