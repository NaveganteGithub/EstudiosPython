"""
Aquí hay algunos ejemplos de ejercicios de python que puedes hacer con las librerías AsyncIO, Multithreading y Multiprocessing. Estos ejercicios no son exhaustivos ni están ordenados por dificultad, sino que son solo sugerencias para practicar el uso de estas librerías.

**Ejercicios de AsyncIO**

- Crea una función asincrónica que imprima "Hola mundo" después de un segundo usando asyncio.sleep.
- Crea una función asincrónica que reciba una lista de URLs y las descargue usando aiohttp. Usa asyncio.gather para esperar a que todas las descargas se completen.
- Crea una función asincrónica que reciba un número n y devuelva el n-ésimo número de Fibonacci usando una expresión await.
- Crea una función asincrónica que reciba una cola asyncio.Queue y ponga en ella los números del 1 al 10 con un segundo de intervalo. Crea otra función asincrónica que reciba la misma cola y saque los números de ella imprimiéndolos. Usa asyncio.create_task para crear dos tareas que ejecuten estas funciones concurrentemente.
- Crea una función asincrónica que reciba un iterador y lo consuma usando un bucle async for. Imprime cada elemento del iterador con un segundo de intervalo.
- Crea una clase asincrónica que represente un contador. La clase debe tener un método __init__ que reciba el valor inicial del contador, un método __aiter__ que devuelva un objeto asincrónico iterable, y un método __anext__ que incremente el contador en uno y lo devuelva. Si el contador supera el valor 10, el método __anext__ debe lanzar un StopAsyncIteration.
- Crea un decorador asincrónico que mida el tiempo de ejecución de una función asincrónica. El decorador debe imprimir el nombre de la función y el tiempo que tardó en ejecutarse.
- Crea una función asincrónica que reciba un número n y cree n tareas asincrónicas que se ejecuten concurrentemente. Cada tarea debe imprimir su identificador (número de 1 a n) y esperar un tiempo aleatorio entre 1 y 5 segundos. La función debe devolver una lista con los resultados de las tareas en el orden en que se completaron.
- Crea una función asincrónica que implemente el algoritmo de ordenación por burbuja de forma asincrónica. Es decir, la función debe recibir una lista de números y ordenarla usando intercambios asincrónicos entre elementos adyacentes.
- Crea una función asincrónica que reciba un comando del sistema operativo (por ejemplo, "ls" o "dir") y lo ejecute usando asyncio.subprocess. La función debe imprimir la salida estándar y la salida de error del comando.

**Ejercicios de Multithreading**

- Crea una función que reciba una lista de números y devuelva la suma de sus cuadrados. Usa el módulo threading para dividir la lista en cuatro partes y calcular la suma parcial de cada parte en un hilo diferente. Usa una variable compartida para almacenar la suma total.
- Crea una función que reciba una cadena de texto y devuelva el número de vocales que contiene. Usa el módulo threading para crear un hilo por cada vocal y contar el número de ocurrencias de esa vocal en la cadena. Usa un diccionario compartido para almacenar los resultados por cada vocal.
- Crea una clase que herede de threading.Thread y que represente un temporizador. La clase debe recibir en el constructor el tiempo en segundos que debe durar el temporizador y un nombre. El método run debe imprimir el nombre del temporizador y el tiempo restante cada segundo. Cuando el tiempo se agote, el método run debe imprimir un mensaje indicando que el temporizador ha terminado.
- Crea una función que reciba una lista de URLs y las descargue usando el módulo requests. Usa el módulo threading para crear un hilo por cada URL y descargarla concurrentemente. Usa una cola thread-safe para almacenar el contenido de cada descarga.
- Crea una función que reciba un número n y devuelva el factorial de ese número. Usa el módulo threading para crear dos hilos: uno que calcule el factorial usando un bucle for y otro que lo calcule usando recursión. Usa un objeto threading.Event para sincronizar el inicio de los dos hilos y un objeto threading.Lock para evitar que los hilos impriman el resultado al mismo tiempo.
- Crea una función que reciba un nombre de archivo y lo copie a otro archivo con el mismo nombre pero añadiendo la extensión ".bak". Usa el módulo threading para crear dos hilos: uno que lea el archivo original y otro que escriba el archivo de copia. Usa una cola thread-safe para comunicar los datos entre los hilos.
- Crea una función que reciba una lista de números y los ordene usando el algoritmo de ordenación por mezcla (merge sort). Usa el módulo threading para dividir el problema en subproblemas más pequeños y asignar cada subproblema a un hilo diferente. Usa un objeto threading.Barrier para sincronizar los hilos en cada nivel de recursión.
- Crea una función que reciba un número n y devuelva el n-ésimo número de la sucesión de Fibonacci. Usa el módulo threading para crear un hilo que calcule el resultado y otro hilo que muestre una barra de progreso mientras el cálculo está en curso. Usa un objeto threading.Condition para notificar al hilo de la barra de progreso cuando el cálculo ha terminado.
- Crea una función que simule el funcionamiento de una impresora. La función debe recibir un número que indique la capacidad de la impresora en páginas por minuto. Usa el módulo threading para crear varios hilos que representen documentos con un número aleatorio de páginas que quieren imprimirse. Usa un objeto threading.Semaphore para limitar el número de documentos que pueden acceder a la impresora simultáneamente.
- Crea una función que simule una carrera de relevos entre dos equipos de cuatro corredores cada uno. Cada corredor tiene un tiempo aleatorio entre 10 y 20 segundos para completar su tramo. Usa el módulo threading para crear un hilo por cada corredor y un objeto threading.RLock para simular el testigo que se pasan los corredores. La función debe imprimir el estado de la carrera y el equipo ganador.

**Ejercicios de Multiprocessing**

- Crea una función que reciba una lista de números y devuelva el máximo de la lista. Usa el módulo multiprocessing para dividir la lista en cuatro partes y calcular el máximo de cada parte en un proceso diferente. Usa una tubería (pipe) para comunicar los máximos parciales al proceso principal.
- Crea una función que reciba una cadena de texto y devuelva el número de palabras que contiene. Usa el módulo multiprocessing para crear un proceso por cada palabra y contar el número de letras de esa palabra. Usa un objeto multiprocessing.Value para almacenar el número total de palabras.
- Crea una clase que herede de multiprocessing.Process y que represente una alarma. La clase debe recibir en el constructor el tiempo en segundos que debe durar la alarma y un mensaje. El método run debe esperar el tiempo indicado y luego imprimir el mensaje.
- Crea una función que reciba una lista de URLs y las descargue usando el módulo requests. Usa el módulo multiprocessing para crear un proceso por cada URL y descargarla concurrentemente. Usa un objeto multiprocessing.Manager para crear una lista compartida donde almacenar el contenido de cada descarga.
- Crea una función que reciba un número n y devuelva el número de primos menores o iguales que n. Usa el módulo multiprocessing para crear cuatro procesos que comprueben si los números en el rango [1, n] son primos o no. Usa un objeto multiprocessing.Array para almacenar los números primos encontrados por cada proceso.
- Crea una función que reciba un nombre de archivo y lo comprima usando el algoritmo de compresión LZW. Usa el módulo multiprocessing para crear dos procesos: uno que lea el archivo original y otro que escriba el archivo comprimido. Usa una cola multiprocessing.Queue para comunicar los datos entre los procesos.
- Crea una función que reciba una lista de números y los ordene usando el algoritmo de ordenación rápida (quick sort). Usa el módulo multiprocessing para dividir el problema en subproblemas más pequeños y asignar cada subproblema a un proceso diferente. Usa un objeto multiprocessing.Pool para gestionar el número de procesos creados.
- Crea una función que reciba un número n y devuelva el n-ésimo número de la serie de Taylor para la función exponencial. Usa el módulo multiprocessing para crear un proceso que calcule el resultado y otro proceso que muestre una animación mientras el cálculo está en curso. Usa un objeto multiprocessing.Event para notificar al proceso de la animación cuando el cálculo ha terminado.
- Crea una función que simule el lanzamiento de un dado en python.

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