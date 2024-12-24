import time
from threading import Thread

class temporizador(Thread):
    
    def __init__(self, segundos: int, nombre: str) -> None:
        super().__init__()
        self.tiempo = segundos
        self.nombre = nombre
        
    def run(self):
        time.sleep(self.tiempo)
        print(self.nombre, self.tiempo)

temp = temporizador(7, "Vida")
temp.start()
temp.join()