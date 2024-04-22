# Ejemplo simple de decorador
def info(funcion):  # la funcion que recibe es mi_funcion
    print("Nombre:",funcion.__name__)
    print("Tipo:", type(funcion))
    return funcion
    
@info    # decorador, sobre la funcion
def mi_funcion():
    print("Estoy ejecutando mi funcion")
    
mi_funcion()


# Ejemplo con decorador con argumentos
def operacion(operador):
    def otra_funcion(funcion):
        print("La operacion que se va a hacer es : ", operador)
        return funcion
    return otra_funcion

@operacion('+')
def sumar(n1, n2):
    print(n1 + n2)
sumar(7,5)
    
@operacion('-')
def restar(n1, n2):
    print(n1 - n2)
restar(7,5)
    
@operacion('*')
def multiplicar(n1, n2):
    print(n1 * n2)
#multiplicar(7,5)
    
@operacion('/')
def dividir(n1, n2):
    print(n1 / n2)
#dividir(7,5)  


# Ejemplo de decorador con clase
class MiDecorador:
    def __init__(self, funcion):
        self.funcion = funcion  # la funcion contar
        print(self) # <__main__.MiDecorador object at 0x11f5cfa00>
        
    def __call__(self, *argumentos):  # *argumentos son los pasados a la funcion contar
        print("Hemos recibido:",argumentos)
        self.funcion(*argumentos) # Tengo que ejecutar la funcion que he recibido


@MiDecorador
def contar(*numeros):
    print("Numeros de datos:", len(numeros))

contar()
contar(1)
contar(1,7)
contar(1,7,5,2,8,6)
print(type(contar))  # <class '__main__.MiDecorador'>








