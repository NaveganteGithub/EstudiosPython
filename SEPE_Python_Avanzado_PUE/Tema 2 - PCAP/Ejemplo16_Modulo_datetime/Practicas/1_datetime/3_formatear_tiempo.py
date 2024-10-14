from datetime import datetime

"""
d -> dia

m -> mes (numero)
B -> mes (nombre)

Y -> Año (completo)
y -> Año (dos digitos)

H -> Hora
M -> Minutos
S -> Segundos
"""

fecha_hora = datetime(2024, 11, 25, 12, 50, 20, 700020)
print(fecha_hora.strftime("%d-%m-%Y %H-%M-%S"))
print(fecha_hora.strftime("%d-%m-%y %H-%M-%S"))
print(fecha_hora.strftime("%d-%B-%Y %H-%M-%S"))