
# Ejemplo de decorador
def info(funcion):
    print("Nombre:", funcion.__name__)
    print("Tipo:", type(funcion))
    return funcion


@info
def mi_funcion():
    print("Estoy ejecutando mi funcion")


mi_funcion()


# Decorador con parametro
def operacion(operador):
    
    def otra_funcion(funcion):
        print("La operacion que se va a hacer es", operador)
        return funcion
    
    return otra_funcion


@operacion('+')
def sumar(n1, n2):
    print(n1 + n2)


sumar(7, 5)


@operacion('-')
def restar(n1, n2):
    print(n1 - n2)


restar(7, 5)


@operacion('*')
def mutiplicar(n1, n2):
    print(n1 * n2)


mutiplicar(7, 5)


@operacion('//')
def dividir(n1, n2):
    print(n1 // n2)


dividir(7, 5)

sumar(7, 5)
restar(7, 5)
mutiplicar(7, 5)
dividir(7, 5)


# Ejemplo de decorador con clase
class mi_decorador:
    
    def __init__(self, funcion):
        self.funcion = funcion  # Aqui pasas la funcion contar
        print("Funcion", self.funcion)
        
    # call es el equivalente a los disparadores de PL/SQL
    # es un metodo que se activa automaticamente cuando
    # llamamos al decorador con clase
    def __call__(self, *argumentos):  # Aqui recibimos los argumentos de la funcion contar
        print("Hemos recibido:", argumentos)
        '''
        Tengo que ejecutar la funcion que he recibido en init, 
        con los argumentos recibidos en call
        '''
        self.funcion(*argumentos) 
        

@mi_decorador
def contar(*numeros):
    print("Número de datos: ", len(numeros))
    

contar()
contar(1)
contar(1, 7)
contar(1, 7, 5, 2, 8, 6)
print(type(contar))
print(type(contar()))
print()


class mi_decorador_2:
    
    def __init__(self, funcion):
        self.funcion = funcion
        
    def __call__(self, argumentos):
        print("Hemos recibido:", argumentos)
        self.funcion(argumentos)
        

@mi_decorador_2
def contar(numeros):
    print(numeros)
    

contar(1)
