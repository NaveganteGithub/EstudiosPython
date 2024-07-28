'''
1. **Importaciones con from e import:**
   a. Importa la función `sqrt` del módulo `math` y úsala para calcular la raíz cuadrada de un número.
   b. Importa la función `randint` del módulo `random` y úsala para generar un número entero aleatorio entre 1 y 100.
'''
print("Ejercicio 1.a.")
from math import sqrt
print(sqrt(8))

print("Ejercicio 1.b.")
from random import randint
print(randint(5, 15))

'''
2. **Métodos para cadenas de texto:**
   a. Crea una función que reciba una cadena y devuelva la misma cadena en mayúsculas.
   b. Crea una función que cuente cuántas veces aparece una letra específica en una cadena dada.
'''
cadena = "Hola buenas tardes"

print("Ejercicio 2.a.")
def mayusculas(cadena: str):
    return cadena.upper()

print(mayusculas(cadena))

print("Ejercicio 2.b.")
def concurrencia(cadena: str, letra: str):
    return cadena.count(letra)

print(concurrencia(cadena, "a"))

'''
3. **Excepciones avanzadas: aserciones y crear excepciones personalizadas:**
   a. Escribe una función que reciba un número entero y genere una aserción si el número es negativo.
   b. Crea una excepción personalizada llamada `MiExcepcion` y lanza esta excepción cuando un usuario ingrese un número mayor que 100.
'''
print("Ejercicio 3.a.")
def contar_stock(manzanas: int):
   assert manzanas > 0, "No se admiten negativos"
   print("Tienes", manzanas, "manzanas.")

contar_stock(5)
# contar_stock(-6) # Assertion error

print("Ejercicio 3.b.")
class MiExcepcion(Exception):
    
   def __init__(self, mensaje) -> None:
      super().__init__(mensaje)

   def get_mensaje(self):
      return self.mensaje

import sys
try:
   numero = int(input("Introduce un numero menor que 100: "))
   if numero >= 100:
      raise MiExcepcion("ERROR: has introducido un numero igual o mayor a cien.")
except MiExcepcion as error:
   print(error)
   args, descripcion, traza = sys.exc_info()
   print(args)
   print(descripcion)
   print(traza)

'''
4. **Programación POO, incluido el mro:**
   a. Define una clase llamada `Rectangulo` con métodos para calcular su área y perímetro.
   b. Crea una clase `Cuadrado` que herede de `Rectangulo` y sobrescribe el método para calcular el área.
'''
print("Ejercicio 4.a.")
class Rectangulo:

   def area(self, altura: int, base: int):
      return altura * base

   def perimetro(self, ancho: int, alto: int):
      return (ancho + alto) * 2

rectangulo = Rectangulo()
print(rectangulo.area(7, 12))
print(rectangulo.perimetro(7, 12))

print("Ejercicio 4.b.")
class Cuadrado(Rectangulo):

   def area(self, altura: int, base: int):
      if altura == base:
         return altura * base
      
      return 0

cuadrado = Cuadrado()
print(cuadrado.perimetro(7, 7))
print(cuadrado.perimetro(5, 5))

'''
5. **Funciones filter, map, reduce y lambdas:**
   a. Utiliza `filter` para obtener los números pares de una lista dada.
   b. Usa `map` para duplicar cada elemento de una lista.
   c. Implementa una función que sume todos los elementos de una lista usando `reduce`.
   d. Crea una lambda que multiplique un número dado por 2.
'''
lista_inicial = list(range(1, 100 + 1))

print("Ejercicio 5.a.")
def pares(n):
   return n % 2 == 0

resultados = list(filter(pares, lista_inicial))
print(resultados)

print("Ejercicio 5.b.")
def duplicar(n):
   return n * 2

resultados = list(map(duplicar, lista_inicial))
print(resultados)

print("Ejercicio 5.c.")
from functools import reduce
def suma(acum, n):
   return acum + n

resultados = reduce(suma, lista_inicial)
print(resultados)

print("Ejercicio 5.d.")
resultados = reduce(lambda acum, n: acum + n, lista_inicial)
print(resultados)

'''
6. **Ficheros:**
   a. Lee un archivo de texto y cuenta cuántas líneas tiene.
   b. Escribe una lista de strings en un archivo de texto.
'''
print("Ejercicio 6.a.")
lectura = None
try:
   lectura = open("SEPE_Python_Avanzado_PUE/Tema 2 - PCAP/Apuntes_diagramas/conversiones.csv", "rt", encoding="utf-8")
   resultado = len(lectura.readline())
   print(resultado)
except:
   pass
finally:
   lectura.close()

print("Ejercicio 6.b.")
cadenas = "Hola buenas esto es una cadena que va a ser una lista de cadenas".split()
try:
   escribir = open("SEPE_Python_Avanzado_PUE/Tema 2 - PCAP/Apuntes_diagramas/saludo.txt", "wt", encoding="utf-8")
   escribir.writelines(cadenas)
except:
   pass
finally:
   escribir.close()

'''
7. **Módulos os, datetime, time, calendar y pandas:**
   a. Utiliza el módulo `os` para listar todos los archivos en un directorio dado.
   b. Crea un script que obtenga la fecha y hora actual utilizando los módulos `datetime` y `time`.
   c. Usa el módulo `calendar` para imprimir el calendario de un mes específico.
   d. Importa el módulo `pandas` y crea un DataFrame con algunos datos y luego imprime las primeras filas.
'''



'''
8. **Generadores de iteradores:**
   a. Crea un generador que genere números pares.
   b. Implementa un iterador personalizado que genere los números de Fibonacci.

'''
print("Ejercicio 8.a.")
def generador():
   for i in range(1, 200):
      if i % 2 == 0:
         yield i

for e in generador():
   print(e, end=" ")

print()

print("Ejercicio 8.b.")
def fibonacci(n):
   secuencia = [0, 1]
   yield secuencia[0]
   yield secuencia[1]

   for _ in range(2, n):
      resultado = secuencia[-2] + secuencia[-1]
      secuencia.append(resultado)
      yield resultado

for f in fibonacci(100):
   print(f, end=" ")

# https://www.examtopics.com/exams/python-institute/pcap/view/1/

# https://www.programiz.com/python-programming/pass-statement
"""
A. .3423e2: Esto significa 0.3423 por 10 elevado a la potencia de 2 (que es 100). Entonces, es 0,3423 * 100 = 34,23, que es lo mismo que nuestro número.
B. 3423e-2: Esto significa 3423 multiplicado por 10 elevado a la potencia de -2 (que es 0,01). Entonces, es 3423 * 0,01 = 34,23, que también es el mismo que nuestro número.
C. .3423e-2: Esto significa 0,3423 multiplicado por 10 elevado a la potencia de -2 (que es 0,01). Entonces, es 0,3423 * 0,01 = 0,003423, que no es lo mismo que nuestro número.
D. 3423e2: Esto significa 3423 por 10 elevado a la potencia de 2 (que es 100). Entonces, es 3423 * 100 = 342300, que no es lo mismo que nuestro número.
Entonces, las opciones A y B son las que reflejan el valor 34,23. Muestran el número de una forma más sencilla utilizando notación científica.
"""