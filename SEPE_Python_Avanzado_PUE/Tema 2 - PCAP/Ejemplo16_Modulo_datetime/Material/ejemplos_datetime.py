from datetime import datetime
from datetime import timedelta

# crear un objeto datetime
fecha_hora = datetime(2021, 11, 25, 6, 35, 43, 58)
print(fecha_hora) # 2021-11-25 06:35:43.000058

# obtenemos solo la fecha
print("Fecha:", fecha_hora.date()) # Fecha: 2021-11-25

# obtenemos solo la hora
print("Hora:", fecha_hora.time()) # Hora: 06:35:43.000058

# Fecha y hora actual
print("Ahora:", datetime.today()) # Ahora: 2024-04-16 14:32:59.536198
print("Ahora:", datetime.now()) # Ahora: 2024-04-16 14:33:55.061827
print("Ahora:", datetime.utcnow()) # Ahora: 2024-04-16 12:34:36.617954

# Obtener el timestamp (marca de tiempo)
print("Marca de tiempo:", fecha_hora.timestamp()) # Marca de tiempo: 1637818543.000058

# Establecer nuestro propio formato de fechas, establece el formato de los datos de salida
print(fecha_hora.date().strftime('%d/%m/%Y'))  # 25/11/2021   %Y 4 digitos
print(fecha_hora.date().strftime('%d/%m/%y'))  # 25/11/21     %y 2 digitos

# Establecer nuestro propio formato de horas
print(fecha_hora.time().strftime('%H:%M:%S'))  # 06:35:43

# Establecer nuestro propio formato de fecha y hora
print(fecha_hora.strftime('%d/%m/%Y - %H:%M:%S'))  # 25/11/2021 - 06:35:43
print(fecha_hora.strftime('%d/%B/%Y - %H:%M:%S'))  # 25/November/2021 - 06:35:43

# diferencia de fechas y horas
print(datetime(2024,4,16,9)   -    datetime(2024,4,15,9))  # dia

# Crear un periodo de tiempo
periodo = timedelta(days=1, hours=6)
print(datetime.today() + periodo)  # 2024-04-17 21:00:20.786069

# Creamos la fecha como string y strptime la reconoce como objeto fecha, establece el formato de los datos de entrada
dt_string = "16/04/2024 14:52:32"
print("dd/mm/yyyy")
dt_object1 = datetime.strptime(dt_string, "%d/%m/%Y %H:%M:%S")
print("dt_object1 =", dt_object1) #dt_object1 = 2024-04-16 14:52:32

dt_string = "04/16/2024 14:52:32"
print("mm/dd/yyyy ")
dt_object2 = datetime.strptime(dt_string, "%m/%d/%Y %H:%M:%S")
print("dt_object2 =", dt_object2) #dt_object2 = 2024-04-16 14:52:32