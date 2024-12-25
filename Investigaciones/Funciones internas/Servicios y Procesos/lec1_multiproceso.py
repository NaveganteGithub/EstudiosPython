from multiprocessing import Process
from time import sleep


def funcion_nombre(nombre):
    while True:
        print('Hola', nombre)
        sleep(7)


def funcion_nombre_corto(nombre):
    while True:
        print('Hola', nombre)
        sleep(1)


if __name__ == '__main__':

    # Los procesos y los subprocesos son independientes, los hilos no

    proceso1 = Process(target=funcion_nombre,     # Función
                       args=('Maria',))           # Parámetros de la función
    proceso1.start()

    proceso2 = Process(target=funcion_nombre, args=('David',))
    proceso2.start()

    proceso3 = Process(target=funcion_nombre_corto, args=('Daniel',))
    proceso3.start()

    proceso3.join()   # Proceso principal en modo espera hasta que el proceso3 termine

    # No tienes pórque limitarte a hacer que el proceso padre espere a
    # que terminen los subprocesos, dependiendo de los subprocesos que
    # hayas programado puedes agregar más join