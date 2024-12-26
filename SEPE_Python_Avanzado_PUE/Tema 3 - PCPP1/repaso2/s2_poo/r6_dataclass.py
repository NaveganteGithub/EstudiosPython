import inspect
from pprint import pprint  # Pretty-print

# Los dataclasses son patrones de diseño de código que nos permite reducir el tiempo
# de trabajo escribiendo Código Repetitivo (boilerplate) que se ven comúnmente hasta
# cierto punto
from dataclasses import dataclass, astuple, asdict

@dataclass  # El decorador nos permite generar código para todas
class Empleado:

    nombre: str
    puesto: str
    salario: float

empleado = Empleado("Daniel", "Piloto", 15231.15)
print(empleado)
print(astuple(empleado))
print(asdict(empleado))
pprint(inspect.getmembers(Empleado, inspect.isfunction))

print("-" * 50)


@dataclass(frozen=True)
class Direccion:

    nombre: str
    edificio: int
    piso: str


direccion = Direccion("Calle Torre Laguna", 8, "14º A")
print(direccion)
print(astuple(direccion))  # ('Daniel', 'Piloto', 15231.15)
print(asdict(direccion))   # {'nombre': 'Daniel', 'puesto': 'Piloto', 'salario': 15231.15}
pprint(inspect.getmembers(Direccion, inspect.isfunction))

print("-" * 50)


@dataclass(order=True)
class Puesto:

    nombre: str
    funciones: list
    salario: float

puesto = Puesto("Pescadero", ["Limpiar", "Cortar", "Sacar espinas"], 1200.44)
print(puesto)
print(astuple(puesto))
print(asdict(puesto))
pprint(inspect.getmembers(Puesto, inspect.isfunction))

print("-" * 50)


@dataclass(frozen=True, order=True)
class Empresa:

    nombre: str
    direccion: str
    codigo_fiscal: int


empresa = Empresa("Mi Empresa", "Calle Torre Laguna", 156154986)
print(empresa)
print(astuple(empresa))
print(asdict(empresa))
pprint(inspect.getmembers(Empresa, inspect.isfunction))

print("-" * 50)

"""La libreria paprika nos ofrece una serie de dataclass que 
nos permiten reducir código en distintos casos. 
@singleton - Genera el constructor de la clase
@to_string - Genera el método str de la clase
@equals_and_hashcode - Genera el método eq y hash de la clase
"""

from paprika import singleton, to_string, equals_and_hashcode

@to_string
@equals_and_hashcode
@singleton  # Si no lo pongo no genera el constructor y lanza un TypeError
class Hora:

    hora: int
    minuto: int
    segundo: int

hora = Hora(4, 4, 26)
print(hora) # Datos@[dia=15, mes=4, tiempo=2024]

hora_2 = Hora(3, 9, 10)
hora_3 = Hora(15, 4, 14)
print(hora == hora_2) # True
print(hora == hora_3) # True

print(hash(hora)) # 1683041466363346935
pprint(inspect.getmembers(Hora, inspect.isfunction))


print("-" * 50)


from paprika import data

@data
class Fecha:

    dia: int
    mes: int
    tiempo: int

clase = Fecha(15, 4, 2024)
print(clase) # Datos@[dia=15, mes=4, tiempo=2024]

clase_2 = Fecha(18, 9, 2024)
clase_3 = Fecha(15, 4, 2024)
print(clase == clase_2) # True
print(clase == clase_3) # True

print(hash(clase)) # 2607810613518054557
pprint(inspect.getmembers(Fecha, inspect.isfunction))
