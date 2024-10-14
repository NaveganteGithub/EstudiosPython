"""
¡Claro! Aquí tienes algunos ejercicios de Python de nivel intermedio para que practiques:

1. **Ejercicio 1**: Crea una función que implemente el algoritmo de ordenación por mezcla (merge sort).
2. **Ejercicio 2**: Escribe un programa que implemente una pila (stack) utilizando listas en Python.
3. **Ejercicio 3**: Crea una función que tome una cadena y devuelva un diccionario con la frecuencia de cada carácter en la cadena.
4. **Ejercicio 4**: Escribe un programa que implemente una cola (queue) utilizando listas en Python.
5. **Ejercicio 5**: Crea una función que tome una lista de números y devuelva una nueva lista con los números primos de la lista original.
6. **Ejercicio 6**: Escribe un programa que implemente un árbol binario de búsqueda.
7. **Ejercicio 7**: Crea una función que tome una cadena y devuelva `True` si la cadena es un palíndromo y `False` en caso contrario.
8. **Ejercicio 8**: Escribe un programa que implemente el algoritmo de búsqueda binaria.
9. **Ejercicio 9**: Crea una función que tome una lista de números y devuelva una nueva lista con los números ordenados de menor a mayor.
10. **Ejercicio 10**: Escribe un programa que implemente el algoritmo de Dijkstra para encontrar el camino más corto en un grafo.

Espero que estos ejercicios te ayuden a mejorar tus habilidades en Python. ¡Buena suerte! 😊

Para más ejercicios de nivel intermedio, puedes visitar estos recursos¹²³⁴⁵..

Origen: Conversación con Bing, 18/1/2024
(1) Ejercicios de programación Python con solución. https://pythondiario.com/ejercicios-de-programacion-python.
(2) Entrenamiento de programación en Python 3 - Nivel intermedio. https://entrenamiento-python-intermedio.readthedocs.io/es/latest/.
(3) Ejercicios de nivel intermedio para hacer en Python · GitHub. https://gist.github.com/DeybisMelendez/3d1b06feed4000c671921ec77cf492ac.
(4) +100 Ejercicios Resueltos en Python | Udemy. https://www.udemy.com/course/100-ejercicios-resueltos-en-python/.
(5) Ejercicios Python - Ejercicios Python resueltos y retos semanales - J2LOGO. https://j2logo.com/ejercicios-python/.
(6) es.wikipedia.org. https://es.wikipedia.org/wiki/Python.
"""

# Ej 1

"""
Pseudocodigo: https://es.wikipedia.org/wiki/Ordenamiento_por_mezcla

function merge_sort(list m) is
    // Base case. A list of zero or one elements is sorted, by definition.
    if length of m ≤ 1 then
        return m

    // Recursive case. First, divide the list into equal-sized sublists
    // consisting of the first half and second half of the list.
    // This assumes lists start at index 0.
    var left := empty list
    var right := empty list
    for each x with index i in m do
        if i < (length of m)/2 then
            add x to left
        else
            add x to right

    // Recursively sort both sublists.
    left := merge_sort(left)
    right := merge_sort(right)

    // Then merge the now-sorted sublists.
    return merge(left, right)

function merge(left, right) is
    var result := empty list

    while left is not empty and right is not empty do
        if first(left) ≤ first(right) then
            append first(left) to result
            left := rest(left)
        else
            append first(right) to result
            right := rest(right)

    // Either left or right may have elements left; consume them.
    // (Only one of the following loops will actually be entered.)
    while left is not empty do
        append first(left) to result
        left := rest(left)
    while right is not empty do
        append first(right) to result
        right := rest(right)
    return result

"""

lista = [5,8,9,2,6,4,10]

def merge_sort(lista_des: list):
    left = list() 
    right = list()

    if len(lista_des) <= 1:
        return lista_des
    
    # Enumerate nos dara un objeto, con todos los elementos de la lista 
    # en una celda y cada elemento tendra un index, haciendo asi una 
    # enumeracion de todos los elementos
    for i, x in enumerate(lista_des):
        if i < len(lista_des) / 2:
            left.append(x)
        else:
            right.append(x)

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left: list, right: list):
    result = list()

    # Recuerda que para mirar si una lista esta vacias solo 
    # tienes que poner la lista ha examinar
    while left and right:
        if left[0] <= right[0]: # first() en pseudocodigo, señala la primera posicion de una lista
            result.append(left[0])
            left = left[1:] # rest() en pseudocodigo, señala toda la parte de la lista no señalada
        else:
            result.append(right[0])
            right = right[1:] 
        
    while left:
        result.append(left[0])
        left = left[1:]

    while right:
        result.append(right[0])
        right = right[1:]

    return result
        
print(merge_sort(lista))
print()

# Ej 2

"""
Una pila (stack en inglés) es una lista ordenada o estructura de datos
que permite almacenar y recuperar datos, siendo el modo de acceso a 
sus elementos de tipo LIFO (del inglés Last In, First Out, «último en 
entrar, primero en salir»). Esta estructura se aplica en multitud de 
supuestos en el área de la informática debido a su simplicidad y 
capacidad de dar respuesta a numerosos procesos.

Para el manejo de los datos cuenta con dos operaciones básicas: 
apilar (push), que coloca un objeto en la pila, y su operación inversa, 
retirar (o desapilar, pop), que retira el último elemento apilado.

En cada momento solamente se tiene acceso a la parte superior de la pila, 
es decir, al último objeto apilado (denominado TOS, Top of Stack en inglés). 
La operación retirar permite la obtención de este elemento, que es retirado 
de la pila permitiendo el acceso al anterior (apilado con anterioridad), 
que pasa a ser el último, el nuevo TOS.

Las pilas suelen emplearse en los siguientes contextos:

    - Evaluación de expresiones en notación postfija (notación polaca inversa).
    - Reconocedores sintácticos de lenguajes independientes del contexto.
    - Implementación de recursividad.

https://es.wikipedia.org/wiki/Pila_(inform%C3%A1tica)#

"""

class pila:

    def __init__(self, limite: int) -> None:
        self.__limite = int(limite)
        self.__pila = list()
        
    def apilar(self, dato: object = None):

        if len(self.__pila) >= self.__limite:
            raise Exception("Exception StackOverflow")
        
        self.__pila.append(dato)

    def retirar(self):
        if len(self.__pila) <= 0:
            raise IndexError("The list is empty")
        
        self.__pila.pop()

    def get_pila(self):
        return self.__pila
    
mi_pila = pila(3)

mi_pila.apilar("a")
print(mi_pila.get_pila())
mi_pila.apilar("b")
print(mi_pila.get_pila())
mi_pila.apilar("c")
print(mi_pila.get_pila())

mi_pila.retirar()

mi_pila.apilar("d")
print(mi_pila.get_pila())

mi_pila.retirar()
mi_pila.retirar()
mi_pila.apilar(2)
print(mi_pila.get_pila())
print()
# Ej 3

def contador_frecuencia(cadena: str):
    resultado = dict()

    muestra = set(list(cadena))

    # print([letter + str(cadena.count(letter)) for letter in muestra])
        
    for letter in muestra:
        resultado[letter] = str(cadena.count(letter))

    return resultado

print(contador_frecuencia("Bienvenido"))
print()
# Ej 4

"""
Una cola (también llamada fila) es un tipo de dato abstracto, 
caracterizada por ser una secuencia de elementos en la que la 
operación de inserción push se realiza por un extremo y la 
operación de extracción pull por el otro. También se le llama 
estructura FIFO (del inglés First In First Out), debido a que 
el primer elemento en entrar será también el primero en salir

La particularidad de una cola es el hecho de que solo podemos
acceder al primer y al último elemento de la estructura. 
Así mismo, los elementos solo se pueden eliminar por el 
principio y solo se pueden añadir por el final de la cola.

Ejemplos de colas en la vida real serían: personas comprando en 
un supermercado, esperando para entrar a ver un partido de béisbol, 
esperando en el cine para ver una película, una pequeña peluquería, 
etc. La idea esencial es que son todos líneas de espera.

Operaciones Básicas:

    - Crear: se crea la cola vacía.
    - Encolar: se añade un elemento a la cola. 
      Se añade al final de esta.
    - Desencolar: (sacar, salir, eliminar): se elimina el elemento 
      frontal de la cola, es decir, el primer elemento que entró.
    - Frente: (consultar, front): se devuelve el elemento frontal 
      de la cola, es decir, el primer elemento que entró.

https://es.wikipedia.org/wiki/Cola_(inform%C3%A1tica)

"""

class cola():

    def crear(self):
        self.tail = list()
    
    def encolar(self, dato: object):
        self.tail.insert(0, dato)
    
    def desencolar(self):
        self.tail.pop()
    
    def frente(self):
        return self.tail[len(self.tail) - 1]
    
mi_cola_procesos = cola()

mi_cola_procesos.crear()
mi_cola_procesos.encolar(2)
mi_cola_procesos.encolar(3)
mi_cola_procesos.encolar(4)
mi_cola_procesos.encolar(5)

print(mi_cola_procesos.frente())

mi_cola_procesos.desencolar()
print(mi_cola_procesos.frente())

mi_cola_procesos.desencolar()
print(mi_cola_procesos.frente())
print()

# Ej 5

"""
¡Hola! Claro, te puedo explicar cómo funciona la criba de Eratóstenes. Es un método antiguo para encontrar todos los números primos hasta un número determinado⁵.

Aquí te dejo los pasos para aplicar la criba de Eratóstenes:

1. Primero, crea una lista de números enteros desde 2 hasta el número `n` que hayas elegido⁶.
2. Marca el número 2 como primo y elimina todos sus múltiplos de la lista⁶.
3. El siguiente número que no ha sido eliminado se considera primo. Elimina todos sus múltiplos de la lista⁸.
4. Repite el paso 3 hasta que el cuadrado del siguiente número no eliminado sea mayor que `n`⁴.
5. Todos los números que quedan en la lista son primos⁵.

Por ejemplo, si quieres encontrar todos los números primos menores a 20:

1. Escribe una lista de números desde 2 hasta 20.
2. Borra todos los múltiplos de 2 (excepto el 2).
3. De los números que quedan, borra todos los múltiplos de 3 (excepto el 3).
4. Continúa el proceso con los siguientes números (5, 7, 11, etc.) hasta que el cuadrado del siguiente número sea mayor que 20.
5. Los números que quedan son primos: 2, 3, 5, 7, 11, 13, 17, 19⁵.

Espero que esto te ayude a entender cómo funciona la criba de Eratóstenes. Si tienes alguna otra pregunta, no dudes en hacerla. 😊

Origen: Conversación con Bing, 2/2/2024
(1) ¿Qué es la Criba de Eratóstenes y cómo funciona?. https://micalculadoracientifica.com/criba-de-eratostenes/.
(2) Los números primos y la criba de Eratóstenes - WikiSaber. https://bing.com/search?q=C%c3%b3mo+utilizar+la+criba+de+Erat%c3%b3stenes.
(3) La criba de Eratóstenes explicada para niños. http://flandes-editorial.com/la-criba-de-eratostenes-explicada-para-ninos/.
(4) Números primos: cómo encontrarlos con la criba de Eratóstenes - Smartick. https://www.smartick.es/blog/matematicas/numeros-enteros/numeros-primos-criba-eratostenes/.
(5) Criba de eratóstenes del 1 al 100 - UDOE. https://udoe.es/criba-de-eratostenes-del-1-al-100/.
(6) ¿Qué es la Criba de Eratóstenes y cuál es su importancia en las matemáticas? - Yo Soy Tu Profe. https://yosoytuprofe.20minutos.es/2022/11/09/que-es-la-criba-de-eratostenes-y-cual-es-su-importancia-en-las-matematicas/.
(7) La criba de Eratóstenes. https://didactalia.net/comunidad/materialeducativo/recurso/la-criba-de-eratostenes/fe4a789d-6316-4e1a-bdaf-2a404e7d93ee.
(8) Los números primos y la criba de Eratóstenes - WikiSaber. https://www.wikisaber.es/los-numeros-primos-y-la-criba-de-eratostenes/.
"""

lista = [i for i in range(2, 257 + 1)]

def primos(numeros: list) -> list:
    cont_positivos = 0
    num = 0
    longitud_lista = len(numeros)
    last_num = numeros[len(numeros) - 1]
    # print(last_num)

    try:
        while num < longitud_lista:
            num_actual = numeros[num]
            # print(numeros, num)
            
            for criba in range(1, last_num + 1):
                # print(num_actual, criba, str((num_actual // criba)), str((num_actual % criba)))
                
                if num_actual % criba == 0:
                    cont_positivos = cont_positivos + 1

                if cont_positivos > 2:
                    numeros.remove(num_actual)
                    num = num - 1
                    cont_positivos = 0
                    break

                if criba == last_num:
                    cont_positivos = 0
        
            num = num + 1

    except IndexError as i:
        pass
    finally:
        return numeros
    
print(primos(lista))
print()

# Ej 6

"""
¡Claro que sí! Aquí te dejo los pasos para crear un árbol binario de búsqueda:

1. **Inicializar el árbol**: Comienza con un árbol vacío o un nodo raíz si tienes un elemento inicial.

2. **Insertar elementos**:
   - Compara el nuevo elemento con el nodo raíz.
   - Si el nuevo elemento es menor que el nodo actual, muévete al hijo izquierdo. Si el nuevo elemento es mayor, muévete al hijo derecho.
   - Si llegas a un nodo vacío (es decir, no hay más nodos en esa dirección), inserta el nuevo elemento en ese lugar.

3. **Buscar elementos**:
   - Comienza en el nodo raíz.
   - Si el elemento que buscas es igual al nodo actual, has encontrado el elemento.
   - Si el elemento que buscas es menor que el nodo actual, muévete al hijo izquierdo. Si es mayor, muévete al hijo derecho.
   - Si llegas a un nodo vacío, el elemento que buscas no está en el árbol.

4. **Eliminar elementos**:
   - Para eliminar un elemento, primero debes encontrarlo utilizando el método de búsqueda descrito anteriormente.
   - Si el elemento a eliminar no tiene hijos, simplemente elimínalo.
   - Si el elemento a eliminar tiene un solo hijo, reemplaza el elemento con su hijo.
   - Si el elemento a eliminar tiene dos hijos, necesitas encontrar el sucesor inmediato (el valor más pequeño en el subárbol derecho) o el predecesor inmediato (el valor más grande en el subárbol izquierdo), reemplazar el valor del nodo con el sucesor o predecesor, y luego eliminar el sucesor o predecesor.

5. **Recorrer el árbol**: Puedes recorrer el árbol de varias maneras: en orden (izquierda, raíz, derecha), preorden (raíz, izquierda, derecha) y postorden (izquierda, derecha, raíz).

Recuerda que los árboles binarios de búsqueda son estructuras de datos dinámicas, lo que significa que puedes realizar estas operaciones tantas veces como sea necesario para insertar, buscar y eliminar elementos. ¡Espero que esto te ayude! 😊.

Origen: Conversación con Bing, 2/2/2024
(1) en.wikipedia.org. https://en.wikipedia.org/wiki/Binary_tree.
"""

# Ej 7

def palindromo(cadena: str) -> bool:
    matriz = list(cadena)
    revertida = list(reversed(matriz))
    for cad in range(0, len(matriz)):
        if matriz[cad] != revertida[cad]:
            return False
    
    return True

print(palindromo("ana"))
print(palindromo("Miguel"))
print(palindromo("121"))
print(palindromo("1212"))

print()

# Ej 8

lista = [5,2,1,9,8,7,6]
lista = sorted(lista)

def busqueda_binaria(vector: list[int], size_vector: int, data_search: int):
    centro: int
    inf: int = 0
    sup: int = size_vector - 1

    while inf <= sup:
        centro = ((sup - inf) // 2) + inf
        
        if vector[centro] == data_search:
            return centro
        elif data_search < vector[centro]:
            sup = centro - 1
        else:
            inf = centro + 1

    return -1

print(busqueda_binaria(lista, len(lista), 1))
print(busqueda_binaria(lista, len(lista), 2))
print(busqueda_binaria(lista, len(lista), 9))
# Ej 9

lista = [5,1,2,4,3,9,8,7,6]

def ordenar(lista_num: list[int]) -> list[int]:
    return sorted(lista_num)

print(lista)
print(ordenar(lista))

# Ej 10