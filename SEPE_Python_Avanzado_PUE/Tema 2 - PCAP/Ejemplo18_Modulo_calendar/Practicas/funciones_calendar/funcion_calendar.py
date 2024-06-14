import calendar

# El parametro w: para determinar el ancho del calendario
# El parametro l: para determinar la altura del calendario
# El parametro m: para determinar cuantas columnas tendra el calendario
print(calendar.calendar(2024))
print(calendar.calendar(2024, w=4))
print(calendar.calendar(2024, w=4, l=2))
print(calendar.calendar(2024, m=2))
print(calendar.calendar(2024, w=4, l=2, m=2))

print(calendar.month(2024, 4))
print(calendar.month(2024, 4, w=4))
print(calendar.month(2024, 4, w=4, l=2))
print(calendar.month(2024, 4, w=4, l=2))