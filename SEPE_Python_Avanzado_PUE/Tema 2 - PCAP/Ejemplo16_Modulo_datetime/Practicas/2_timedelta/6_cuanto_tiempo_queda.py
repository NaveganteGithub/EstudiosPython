from datetime import timedelta, datetime

# datetime es un objeto en el que pondremos 
# fechas concretas, mientras que deltatime 
# es un objeto donde podremos cantidades de 
# dias
fecha_deseada = timedelta(weeks=5, days=14, hours=50, 
                          minutes=240, seconds=50, 
                          milliseconds=4500, microseconds=750000)

print(datetime.today() + fecha_deseada)
print("Dias", fecha_deseada.days)
print("Segundos", fecha_deseada.total_seconds())