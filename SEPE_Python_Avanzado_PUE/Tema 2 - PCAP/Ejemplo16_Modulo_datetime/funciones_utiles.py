import datetime
import time


# crear un objeto date a partir de la clase date
hoy = datetime.date(2024, 4, 16)
print(hoy)  # 2024-04-16

# Para crear la marca de tiempo necesitamos el modulo time
timestamp = time.time()
print("Marca de tiempo:", timestamp) # 1713263158.9463198

# Crear la fecha a partir de esa marca de tiempo
fecha = datetime.date.fromtimestamp(timestamp)
print("Fecha:", fecha)  # 2024-04-16

fecha = datetime.date.fromtimestamp(432262.32244) # 1970-01-06
print("Fecha:", fecha)

hoy = datetime.date.today()
print(hoy)  # 2024-04-16
print("Año", hoy.year)
print("Mes", hoy.month)
print("Dia", hoy.day)

# crear una fecha a partir de ISO 8601
ayer = datetime.date.fromisoformat("2024-04-15")  # completar con 0 por delante
print(ayer) # 2024-04-15

# remplazar datos de fecha
anteayer = ayer.replace(day=14)
print(anteayer)  # 2024-04-14
print(ayer) # 2024-04-15

# numero del dia de la semana empezando 0=Lunes
print("Dia semana:", hoy.weekday())  # 1

# numero del dia de la semana empezando 1=Lunes
print("Dia semana:", hoy.isoweekday())  # 2

# crear la hora con la clase time
hora = datetime.time(12,48,39,27, pytz.timezone('America/New_York'))
hora2 = datetime.time(12,48,39,27, None)
print("Hora:", hora) # 12:48:39.000027
print("Hora:", hora2)

