'''
    crear una clase pila (LIFO)
    metodos push (añadir), pop (sacar), size (numero de elementos)
'''
class Pila:
    def __init__(self):
        self.pila = list()  # llamamos al constructor de list()

    def push(self, item):
        self.pila.append(item)
        #self.pila.insert(len(self.pila), item)

    def sacar(self):
        '''
        item = self.pila[-1]
        del self.pila[-1]
        return item
        '''
        try:
            return self.pila.pop()
        except:
            print("Pila vacia")


    def size(self):
        return len(self.pila)

pila = Pila()
pila.push(1)
pila.push(2)
pila.push(3)

print("Numero de elementos:",pila.size())

print(pila.sacar())
print(pila.sacar())
print(pila.sacar())
print(pila.sacar())  # Pila vacia  None
#print("---- ",pila.sacar())   # IndexError: pop from empty list


''' 
    crear una clase cola (FIFO) 
    metodos push, pop, size
'''
class Cola:
    def __init__(self):
        self.cola = []

    def push(self, item):
        self.cola.append(item)

    def sacar(self):
        '''
        item = self.cola[0]
        del self.cola[0]
        return item
        '''
        try:
            return self.cola.pop(0)
        except:
            return "Cola vacia"

    def size(self):
        return len(self.cola)

cola = Cola()
cola.push(1)
cola.push(2)
cola.push(3)

print("Numero de elementos", cola.size())

print(cola.sacar())
print(cola.sacar())
print(cola.sacar())
print(cola.sacar())
