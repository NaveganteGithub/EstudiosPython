from datetime import time
import pytz

# Crear un objeto datetime con información de zona horaria
zona_horaria = pytz.timezone('America/New_York')
hora = time(13, 11, 16, 12,  tzinfo=zona_horaria)

print("Hora con zona horaria:", hora)
print("tzinfo:", hora.tzinfo)

zona_horaria = pytz.timezone('Europe/Madrid')
hora = hora.replace(tzinfo=zona_horaria)
print(hora)
print("tzinfo:", hora.tzinfo)


from zoneinfo import ZoneInfo
from datetime import datetime, timedelta

dt = datetime(2020, 10, 31, 12, tzinfo=ZoneInfo("America/Los_Angeles"))
print(dt)  # 2020-10-31 12:00:00-07:00

dt = datetime(2020, 10, 31, 12, tzinfo=ZoneInfo("Europe/Madrid"))
print(dt)  # 2020-10-31 12:00:00+01:00