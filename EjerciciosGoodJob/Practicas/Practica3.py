"""
¡Hola! Las bibliotecas **AsyncIO**, **Multithreading** y **Multiprocessing** son herramientas útiles para programar en Python. 

**AsyncIO** es una biblioteca de Python que permite la programación asíncrona. Es útil para escribir código que se ejecuta de manera eficiente en un solo hilo de ejecución. Algunos ejemplos de uso de AsyncIO son:

1. Crear servidores web y clientes web.
2. Realizar operaciones de entrada/salida (I/O) de manera asíncrona.
3. Realizar operaciones de red de manera asíncrona.
4. Realizar operaciones de base de datos de manera asíncrona.
5. Realizar operaciones de procesamiento de datos de manera asíncrona.

**Multithreading** es una técnica de programación que permite que un programa tenga varios hilos de ejecución. Es útil para escribir código que se ejecuta de manera eficiente en sistemas con varios núcleos de CPU. Algunos ejemplos de uso de Multithreading son:

1. Crear aplicaciones de GUI (interfaz gráfica de usuario) que responden rápidamente a las entradas del usuario.
2. Realizar operaciones de entrada/salida (I/O) de manera asíncrona.
3. Realizar operaciones de red de manera asíncrona.
4. Realizar operaciones de base de datos de manera asíncrona.
5. Realizar operaciones de procesamiento de datos de manera asíncrona.

**Multiprocessing** es una técnica de programación que permite que un programa tenga varios procesos de ejecución. Es útil para escribir código que se ejecuta de manera eficiente en sistemas con varios núcleos de CPU. Algunos ejemplos de uso de Multiprocessing son:

1. Realizar cálculos intensivos en CPU de manera paralela.
2. Realizar operaciones de entrada/salida (I/O) de manera asíncrona.
3. Realizar operaciones de red de manera asíncrona.
4. Realizar operaciones de base de datos de manera asíncrona.
5. Realizar operaciones de procesamiento de datos de manera asíncrona.

Espero que esto te haya ayudado. ¡Hasta la próxima!

Origen: Conversación con Bing, 25/1/2024
(1) python - multiprocessing vs multithreading vs asyncio - Stack Overflow. https://stackoverflow.com/questions/27435284/multiprocessing-vs-multithreading-vs-asyncio.
(2) Practical Guide to Asyncio, Threading & Multiprocessing. https://itnext.io/practical-guide-to-async-threading-multiprocessing-958e57d7bbb8.
(3) Multiprocessing VS Threading VS AsyncIO in Python - Lei Mao. https://leimao.github.io/blog/Python-Concurrency-High-Level/.

Hola, entiendo que quieres practicar el uso de las librerías AsyncIO, Multithreading y Multiprocessing en Python. Estas librerías te permiten realizar tareas concurrentes o paralelas, aprovechando los recursos de tu máquina o de una red. Aquí te propongo algunos ejercicios sencillos para que te familiarices con ellas:

**Ejercicios de AsyncIO**

AsyncIO es un módulo que te permite escribir código asincrónico, es decir, que no bloquea la ejecución mientras espera por una operación de entrada/salida o por un temporizador. Para usar AsyncIO, necesitas crear una función de tipo `async def`, que es una corutina, y usar la palabra clave `await` para suspenderla hasta que se complete una tarea. También necesitas crear un bucle de eventos (`event loop`) que se encarga de gestionar las corutinas y las tareas. Algunos ejercicios que puedes hacer son:

1. Crea una corutina que imprima "Hola" después de un segundo, y otra que imprima "Mundo" después de dos segundos. Usa `asyncio.sleep` para simular el tiempo de espera. Crea un bucle de eventos y ejecuta las dos corutinas concurrentemente usando `asyncio.gather`.
2. Modifica el ejercicio anterior para que las corutinas reciban un argumento con el mensaje a imprimir, y crea una lista con varios mensajes y tiempos de espera. Itera sobre la lista y crea una corutina para cada elemento, y luego ejecútalas concurrentemente con `asyncio.gather`.
3. Crea una función que dado un número `n`, devuelva una lista con los `n` primeros números de la sucesión de Fibonacci. Haz que esta función sea una corutina, y usa `asyncio.run` para ejecutarla desde el programa principal.
4. Crea una corutina que dado un `url`, haga una petición HTTP usando `aiohttp` (una librería externa que debes instalar) y devuelva el contenido de la respuesta. Crea una lista de varios `urls` y ejecuta la corutina para cada uno de ellos concurrentemente usando `asyncio.gather`. Imprime el tamaño en bytes de cada respuesta.
5. Crea una corutina que se comporte como un contador, es decir, que cada vez que se reanude con `await`, incremente una variable interna y la devuelva. Crea otra corutina que reciba un contador y un número `n`, y reanude el contador `n` veces, imprimiendo el valor devuelto cada vez. Crea un bucle de eventos y ejecuta varias instancias de la segunda corutina con diferentes contadores y números, usando `asyncio.gather`.

**Ejercicios de Multithreading**

Multithreading es un módulo que te permite crear hilos (threads) para ejecutar funciones concurrentemente. Un hilo es una unidad de ejecución que comparte el espacio de memoria con el proceso principal, pero tiene su propio contador de programa y su propia pila. Para crear un hilo, necesitas crear un objeto `Thread` y pasarle la función objetivo y los argumentos que quieras. Luego, debes llamar al método `start` para iniciar el hilo, y al método `join` para esperar a que termine. Algunos ejercicios que puedes hacer son:

6. Crea una función que imprima los números del 1 al 10, con un intervalo de un segundo entre cada uno. Usa el módulo `time` para hacer el intervalo. Crea dos hilos con esta función y ejecútalos concurrentemente. Observa el orden en que se imprimen los números.
7. Modifica el ejercicio anterior para que la función reciba un argumento con el nombre del hilo, y lo imprima junto con el número. Por ejemplo, "Hilo 1: 1". Observa cómo se intercalan los mensajes de los dos hilos.
8. Crea una función que dado un número `n`, devuelva el factorial de `n`. Haz que esta función imprima el nombre del hilo y el resultado. Crea una lista de varios números y crea un hilo para cada uno, pasándole la función y el número como argumentos. Ejecuta los hilos y observa el orden en que se imprimen los resultados.
9. Crea una variable global llamada `contador` e inicialízala a cero. Crea una función que incremente el contador en uno y lo imprima, y luego duerma durante un segundo. Crea 10 hilos con esta función y ejecútalos. Observa el valor del contador y explica por qué no coincide con el número de hilos.
10. Modifica el ejercicio anterior para proteger el acceso a la variable `contador` con un objeto `Lock`. Un `Lock` es un mecanismo de sincronización que evita que dos hilos modifiquen un recurso compartido al mismo tiempo. Para usar un `Lock`, debes crearlo y pasarlo a los hilos, y luego usar los métodos `acquire` y `release` para bloquear y desbloquear el recurso. Observa cómo cambia el valor del contador y el orden de los mensajes.

**Ejercicios de Multiprocessing**

Multiprocessing es un módulo que te permite crear nuevos procesos utilizando una API similar a la del módulo threading. Un proceso es una instancia de un programa que tiene su propio espacio de memoria y sus propios recursos. Para crear un proceso, necesitas crear un objeto `Process` y pasarle la función objetivo y los argumentos que quieras. Luego, debes llamar al método `start` para iniciar el proceso, y al método `join` para esperar a que termine. Algunos ejercicios que puedes hacer son:

11. Repite el ejercicio 6, pero usando procesos en lugar de hilos. Observa el orden en que se imprimen los números y compáralo con el caso de los hilos.
12. Repite el ejercicio 8, pero usando procesos en lugar de hilos. Observa el valor del contador y explica por qué es diferente al caso de los hilos.
13. Crea una función que dado un número `n`, devuelva la suma de los cuadrados de los números del 1 al `n`. Haz que esta función imprima el nombre del proceso y el resultado. Crea una lista de varios números y crea un proceso para cada uno, pasándole la función y el número como argumentos. Ejecuta los procesos y observa el orden en que se imprimen los resultados.
14. Crea una función que llene una lista con 10 números aleatorios entre 1 y 100, usando el módulo `random`. Crea un objeto `Manager` y usa su método `list` para crear una lista compartida entre los procesos. Crea 5 procesos con la función anterior y la lista compartida como argumentos. Ejecuta los procesos y luego imprime el contenido de la lista compartida desde el programa principal.
15. Crea una función que ordene una lista de números usando el método `sort`. Crea un objeto `Pool` con 4 trabajadores y usa su método `map` para aplicar la función a una lista de listas de números. Por ejemplo, `[[9, 4, 2], [7, 1, 3], [6, 8, 5]]`. Imprime el resultado devuelto por el método `map`..

Origen: Conversación con Bing, 25/1/2024
(1) Desarrollando con asyncio — documentación de Python - 3.13.0a3. https://docs.python.org/es/dev/library/asyncio-dev.html.
(2) Async IO in Python: A Complete Walkthrough – Real Python. https://realpython.com/async-io-python/.
(3) Asincronia en Python. Parte 1. https://blog.ascodecodigo.com/async_python/.
(4) multithreading - How do I use threading in Python? - Stack Overflow. https://stackoverflow.com/questions/2846653/how-do-i-use-threading-in-python.
(5) Multithreading in Python: The Ultimate Guide (with Coding Examples). https://www.dataquest.io/blog/multithreading-in-python/.
(6) Multithreading in Python - GeeksforGeeks. https://www.geeksforgeeks.org/multithreading-python-set-1/.
(7) multiprocessing — Paralelismo basado en procesos - Python. https://docs.python.org/es/3.9/library/multiprocessing.html.
(8) multiprocessing – Tareas concurrentes con procesos - Recursos Python. https://recursospython.com/guias-y-manuales/multiprocessing-tareas-concurrentes-con-procesos/.
(9) Fundamentos de multiprocesing — El módulo Python 3 de la semana. https://rico-schmidt.name/pymotw-3/multiprocessing/basics.html.
(10) undefined. http://www.python.org.
(11) undefined. http://www.python.org/about/.
(12) undefined. http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html.
(13) undefined. http://www.python.org/doc/.
(14) undefined. http://www.python.org/download/.
(15) undefined. http://www.python.org/getit/.
(16) undefined. http://www.python.org/community/.
(17) undefined. https://wiki.python.org/moin/.
(18) es.wikipedia.org. https://es.wikipedia.org/wiki/Python.
"""

"""import asyncio

async def hola():
    await asyncio.sleep(1)
    print("Hola")

async def mundo():
    await asyncio.sleep(2)
    print("Mundo")

async def main():
    await asyncio.gather(hola(), mundo())

bucle = asyncio.get_event_loop()
bucle.run_until_complete(main())
bucle.close()"""

"""
3. Crea una función que dado un número `n`, devuelva una lista con los `n` primeros números de la 
sucesión de Fibonacci. Haz que esta función sea una corutina, y usa `asyncio.run` para ejecutarla 
desde el programa principal.
"""

import asyncio

async def fibonacci(n):
    nums_fibonacci = [0, 1]

    for _ in range(n - 2):
        nums_fibonacci.append(nums_fibonacci[-1] + nums_fibonacci[-2])

    return nums_fibonacci

async def main():
    resultado = await fibonacci(5)
    print(resultado)

asyncio.run(main())

import time, threading

def contar():
    for num in range(1, 10 + 1):
        time.sleep(1)
        print(num)

# Si utilizas el metodo run() se ejecutara un hilo y después el otro hilo, es decir, secuencialmente
hilo1 = threading.Thread(target=contar)
hilo2 = threading.Thread(target=contar)
hilo1.start()
hilo2.start()