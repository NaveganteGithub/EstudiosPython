class pila:

    def __init__(self):
        self.mi_pila = list()

    def push(self, elemento):
        if self.size() <= 3:
            self.mi_pila.append(elemento)
        else:
            raise BufferError

    def pop(self):
        if self.size() > 0:
            return self.mi_pila.pop()
        else:
            return "No hay valores"

    def size(self):
        return len(self.mi_pila)

class cola:

    def __init__(self):
        self.mi_cola = list()

    def push(self, elemento):
        if self.size() <= 3:
            self.mi_cola.insert(0, elemento)
        else:
            raise BufferError

    def pop(self):
        if self.size() > 0:
            return self.mi_cola.pop()
        else:
            return "No hay valores"

    def size(self):
        return len(self.mi_cola)

print("Pila")
pila = pila()
pila.push(5)
print("Longitud", pila.size())
pila.push(4)
print("Longitud", pila.size())
pila.push(6)
print("Longitud", pila.size())
print("Valor", pila.pop())
print("Longitud", pila.size())
print("Valor", pila.pop())
print("Valor", pila.pop())
print("Valor", pila.pop())

print("Cola")
cola = cola()
cola.push(5)
print("Longitud", cola.size())
cola.push(4)
print("Longitud", cola.size())
cola.push(6)
print("Longitud", cola.size())
print("Valor", cola.pop())
print("Longitud", cola.size())