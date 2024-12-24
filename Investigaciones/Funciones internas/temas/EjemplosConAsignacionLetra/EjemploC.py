import threading
import time

# Variable global para el contador
contador = 0

# Función que incrementa el contador, lo imprime y duerme
def incrementar_contador():
    global contador
    contador += 1
    print(f"Contador: {contador}")
    time.sleep(1)

# Crear 10 hilos y ejecutar la función
for _ in range(10):
    t = threading.Thread(target=incrementar_contador)
    t.start()

# Esperar a que todos los hilos terminen
for t in threading.enumerate():
    if t != threading.current_thread():
        t.join()

print(f"Valor final del contador: {contador}")
