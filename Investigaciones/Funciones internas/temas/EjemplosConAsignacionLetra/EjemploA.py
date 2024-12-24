import threading, queue

vocales = ('A', 'E', 'I', 'O', 'U', "Á", "É", "Í", "Ó", "Ú", 'a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú')

def procesar(cadena: str):
    vocales_encontradas = list()
    
    for caracter in cadena:
        if caracter in vocales:
            vocales_encontradas.append(caracter)

    return vocales_encontradas

def ocurrencias(cadena: str, vocal: str, cola: queue):
    ocurrencia = cadena.count(vocal)
    cola.put([vocal, ocurrencia])
    
cadena = "Hola"
resultado_busqueda = procesar(cadena)
num_hilos = len(resultado_busqueda)
cola = queue.Queue()

for num_hilo in range(num_hilos):
    hilo = threading.Thread(target=ocurrencias, args=(cadena, resultado_busqueda[num_hilo], cola))
    hilo.run()

for _ in range(cola.qsize()):
    resultado_final = cola.get()
    print(resultado_final)
