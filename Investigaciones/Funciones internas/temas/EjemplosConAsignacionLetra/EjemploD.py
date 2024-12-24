import time
import threading

def funcion_1():
    for i in range(5):
        print(f"Hilo 1: Iteración {i}")
        time.sleep(1)

def funcion_2():
    for i in range(3):
        print(f"Hilo 2: Iteración {i}")
        time.sleep(2)

# Crea los objetos de hilo
hilo_1 = threading.Thread(target=funcion_1)
hilo_2 = threading.Thread(target=funcion_2)

# Ejecuta las funciones utilizando run()
hilo_1.start()
hilo_2.start()

hilo_1.join()
hilo_2.join()