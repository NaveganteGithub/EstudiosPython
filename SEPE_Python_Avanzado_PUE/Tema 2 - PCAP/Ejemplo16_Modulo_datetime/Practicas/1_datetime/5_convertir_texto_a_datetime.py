from datetime import datetime

# Para poder convertir fechas en texto a datetime tienes que poner el parametro del formato
# de la funcion strptime
fecha = "12/05/2024 12:05:23"
fecha_hora = datetime.strptime(fecha, "%d/%m/%Y %H:%M:%S")
print(fecha_hora)

fecha = "12 May 2024 12:05:23"
fecha_hora = datetime.strptime(fecha, "%d %B %Y %H:%M:%S")
print(fecha_hora)