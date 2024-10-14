# **Multiprocessing:**

import multiprocessing
import os

def worker(num, descripcion = None, id_transferido = None):    
    ppid = os.getppid()
    pid = os.getpid()
    print(f"Proceso {num} iniciado,", \
          "" if descripcion is None else descripcion, \
            "este subproceso que tiene el id", pid,\
            "id del proceso padre (que es el raiz tambien)", ppid,
            "" if id_transferido is None else "el id transferido es " + str(id_transferido))
    return

if __name__ == "__main__":
    """
    Empezaremos con el ejemplo 1, para empezar ponemos el print() dentro del if porque sino
    el resultado de la ejecucion del programa puede llegar a ser muy caotico, asi que para
    que no haya problemas con tu codigo la salida salga un poco desordenada procura, poner
    tu codigo dentro del if
    """
    print("Ejemplo 1")
    """
    La linea de multiprocessing.freeze_support() se pone para que no surja 
    la excepcion RuntimeError, se produce cuando intentas iniciar un nuevo 
    proceso antes de que el proceso actual haya terminado su fase de arranque. 
    Esto puede deberse a que no se está usando fork para iniciar tus procesos 
    secundarios y se ha olvidado usar el idiomático if __name__ == '__main__': 
    en el módulo principal y por eso se usa
    
    if __name__ == "__main__":
        ... codigo sin multiprocessing ...
        multiprocessing.freeze_support()
        ... codigo con multiprocessing ...

    recuerda siempre que cuando se acabe un bloque if __name__ == "__main__" 
    tienes que hacer esta estructura de nuevo para realizar otro uso de la 
    libreria multiprocessing
    """
    multiprocessing.freeze_support()
    # Aqui generamos un objeto Process con la funcion que hemos creados anteriormente
    process = multiprocessing.Process(target=worker(1))
    # Aqui iniciamos el proceso con el objeto Process anterior, con el metodo start()
    process.start()
    # Opcional: esperar a que el subproceso acabe, recuerda que si no paras al proceso
    # padre el proceso padre seguira ejecutandose y el hijo tambien
    process.join()

if __name__ == "__main__":
    print("\n\n\n", "Ejemplo 2", sep="")
    process = list()
    multiprocessing.freeze_support()
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i, "Proceso generado"))
        process.append(p)
        p.start()

    # Hacer que el proceso padre espere a que todos los subprocesos terminen
    # recuerda que si no detienes el proceso padre, este seguira ejecutandose
    # sin que los hijos acaben, lo que hara que se ejecuten las siguientes
    # lineas de codigo del programa a la vez que se ejecutan las lineas 
    # de la funcion del proceso generado. Comenta este for para comprobarlo.
    for p in process:
        p.join()

if __name__ == "__main__":
    print("\n\n\n", "Ejemplo 3", sep="")
    process = list()
    multiprocessing.freeze_support()
    for i in range(5):
        
        # Si hacemos asi los procesos se genera un error en
        # el pid de cada subproceso y es que todos los pid 
        # se mostraran iguales
        p = multiprocessing.Process(target=worker(i))
        process.append(p)
        p.start()

    # Esperar a que todos los procesos terminen
    for p in process:
        p.join()

if __name__ == "__main__":
    print("\n\n\n", "Ejemplo 4", sep="")
    process = list()
    multiprocessing.freeze_support()
    for i in range(5):
        
        # Si hacemos asi los procesos se genera un error en
        # el pid de cada subproceso y es que todos los pid 
        # se mostraran iguales
        p = multiprocessing.Process(target=worker, args=(i, None, os.getpid()))
        process.append(p)
        p.start()

    # Esperar a que todos los procesos terminen
    for p in process:
        p.join()