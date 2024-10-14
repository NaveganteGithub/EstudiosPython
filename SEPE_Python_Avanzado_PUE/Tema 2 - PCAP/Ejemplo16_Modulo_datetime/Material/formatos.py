import datetime
import pytz # pip install pytz

zona_horaria_madrid = pytz.timezone("Europe/Madrid")
fecha_madrid_actual = datetime.datetime.now(tz=zona_horaria_madrid)
print(f"Fecha y hora actual en Madrid: {fecha_madrid_actual}")
#Fecha y hora actual en Madrid: 2024-04-16 13:35:10.991043+02:00
# Formatear la fecha y hora en el formato deseado
formato_deseado = "%Y-%m-%d %H:%M:%S"
fecha_formateada = fecha_madrid_actual.strftime(formato_deseado)
print(f"Fecha y hora actual en Madrid: {fecha_formateada}")
#Fecha y hora actual en Madrid: 2024-04-16 13:35:10