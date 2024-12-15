# Explicit is better than implicit. -- Explicito mejor que implícito

## Implícito
from datetime import *

fecha = datetime(2024, 10, 11, 13, 50, 55, 1202)

print(fecha.date())
print(fecha.time())

## Explicito
from datetime import datetime

fecha_actual = datetime(year=2024, month=10, day=11, hour=13, minute=50, second=55, microsecond=1202)

print("Fecha", fecha_actual.date())
print("Hora", fecha_actual.time())
