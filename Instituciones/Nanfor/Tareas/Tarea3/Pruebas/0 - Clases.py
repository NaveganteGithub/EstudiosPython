


# -------------------------------- CREAR UNA CLASE -------------------------------- #

class Empresa: # La palabra reservada class permite crear una clase
    credito_permitido = True
    ayuda_discapacidad = False
    def __init__(self, id, nomb, calle, tipo, tarjeta) -> None:
        self.identificacion = id
        self.nombre = nomb
        self.calle = calle
        self.tipo_sociedad = tipo
        self.tarjeta = tarjeta
        return
    
    def identificar(self):
        return f"La empresa {self.nombre} de la {self.calle} tiene la identificacion fiscal {self.identificacion} es una sociedad {self.tipo_sociedad} su numero de tarjeta bancaria es {self.tarjeta}."
    
    def cambiar_Tarjeta(self, tarjeta):
        self.tarjeta = tarjeta

empresa = Empresa(1561564, "PIO", "Av Rafael Alverti", "Limitada", "1561 5615 6164 5968")
print(empresa.credito_permitido)
print(empresa.identificar())

print("\n" * 2)

# -------------------------------- HERENCIA SIMPLE -------------------------------- #

'''
Pasando una clase existente por el parametro de la declaracion 
de la clase consigues hacer una herencia
'''
class Tipo_Empresa(Empresa):
    def __init__(self, id, nomb, calle, tipo, tarjeta, sector) -> None:
            super().__init__(id, nomb, calle, tipo, tarjeta)
            self.sector = sector
            return
    
    def Tipo_Sector(self):
        return self.sector
    
    def cambiar_Tarjeta(self, tarjeta, codigo):
        if (codigo == self.identificacion):
            self.tarjeta = tarjeta
            print("Operacion autorizada")
        else:
            print("Operacion no autorizada")
        

empresa = Empresa(1656456, "NDIT", "Av de la Albufera N3", "Limitada", "5465 5644 4556 5456")
print(empresa.credito_permitido)
print(empresa.identificar())

tipo = Tipo_Empresa(1656456, "NDIT", "Av de la Albufera N3", "Limitada", "5465 5644 4556 5456", "Aeroespacial")
print(tipo.identificar())
print(tipo.Tipo_Sector())

# Los objetos al instanciarse no se tendrian que ver los datos, 
# se puede aplicar un for o instanciarlos en un archivo .py al 
# que no tengan acceso
tipo.cambiar_Tarjeta("1566 4654 5646 5161", 545564)
print(tipo.identificar())
tipo.cambiar_Tarjeta("1566 4654 5646 5161", 1656456)
print(tipo.identificar())

print("\n" * 2)

# -------------------------------- HERENCIA MULTIPLE -------------------------------- #

class Padre:

    genes_padre = 5167581655791569
    sistema_inmunologico_padre = 54634124564264

    def __init__(self, enfermedad, enfermedad_genetica):
        self.enfermedad_padre = enfermedad
        self.enfermedad_genetica_padre = enfermedad_genetica
        return

    def fuerza_golpe(self, masa, velocidad_final, velocidad_inicial, segundos_desaceleracion):
        '''
        F = masa * aceleracion
        F = masa * ((velocidad_final - velocidad_inicial) / segundos_desaceleracion)
        F = (0.5 kg) * (-100 m/s²) = -50 N (Newtons)
        '''
        return masa * ((velocidad_final - velocidad_inicial) / segundos_desaceleracion)
        
class Madre:

    genes_madre = 1956789578956896
    sistema_inmunologico_madre = 48756786786567

    def __init__(self, enfermedad, enfermedad_genetica):
        self.enfermedad_madre = enfermedad
        self.enfermedad_genetica_madre = enfermedad_genetica
        return

    def inteligencia(self, conocimiento, tiempo_resolucion):
        return conocimiento * tiempo_resolucion

class Hijo(Padre, Madre):

    def __init__(self, enfermedad_padre, enfermedad_genetica_padre, enfermedad_madre, enfermedad_genetica_madre, genetica_propia):
        Padre.__init__(self, enfermedad_padre, enfermedad_genetica_padre)
        Madre.__init__(self, enfermedad_madre, enfermedad_genetica_madre)
        self.genetica_hijo = genetica_propia
        return

    def carisma(self):
        print("No es cuestion de saber o no, es cuestion de saber hacer lo correcto")

hijo = Hijo("Ninguna", "Ninguna", "Hepatitis C", "Ninguna")

print(hijo.enfermedad_padre)
print(hijo.enfermedad_madre)
print(hijo.fuerza_golpe(50,30,10,0.25), "metros por cuadrado")
print(hijo.inteligencia(1000, 20), "inteligencia")


# -------------------------------- Jerarquía de clases -------------------------------- #

class Persona:

    personalidad = "leal"
    
    def __init__(self, nomb, edad, altura, peso):
        self.nombre = nomb
        self.edad = edad
        self.altura = altura
        self.peso = peso 

    def mostrar_info(self):
        print(self.nombre, self.edad, self.altura, self.peso)
        pass

class Mujer(Persona):
    pass

class Hombre(Persona):
    pass

