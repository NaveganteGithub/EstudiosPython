import calendar
import locale

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

calendar.prmonth(2024, 4)
calendar.prmonth(2024, 4, w=4)
calendar.prmonth(2024, 4, w=4, l=2)

# Mostrar el canlendario comenzando la semana en domingo, se puede poner el numero correspondiente al dia de la semana
calendar.setfirstweekday(6)
calendar.setfirstweekday(calendar.SUNDAY) # Aunque es mejor trabajar con la constante
calendar.prmonth(2024,4, w=4, l=2)

# Dada una fecha retorna el dia de la semana en numero
print(calendar.weekday(2024, 4, 17))

# Retorno una cadena con los dias de la semana en x caracteres
print(calendar.weekheader(1))
print(calendar.weekheader(2))
print(calendar.weekheader(3))
# Cuando superamos el 3 ya no te muestra mas letras sino que agregara mas espacios
print(calendar.weekheader(4))
for i in range(5, 8 + 1):
    print(calendar.weekheader(i))
print(calendar.weekheader(9)) # Cuando pones 9 te muestra el nombre del dia de la semana completo

print("Es 2024 bisiesto?", calendar.isleap(2024)) # True
print("Es 2023 bisiesto?", calendar.isleap(2023)) # False

# Cuantos años bisiestos hay entre un rango de años
# Recordar que en los rangos el ultimo no esta incluido
print("Cuantos bisiestos entre 2010 y 2024 sin incluir", calendar.leapdays(2010, 2024))
print("Cuantos bisiestos entre 2010 y incluyendo el 2024", calendar.leapdays(2010, 2025))

mi_calendario = calendar.calendar(2024)
mi_calendario.format()

# Obtener el encabezado de la semana, estableciendo como primer dia el Domingo
header = calendar.weekheader(1)
cal = calendar.TextCalendar(calendar.SUNDAY)
# Obtener el calendario mes actual
month_calendar = cal.formatmonth(2024, 4)
#
combined_calendar = f"{header}\n{month_calendar}"
print(combined_calendar)

calendario = calendar.TextCalendar()
print(calendario.formatmonth(2024, 4))
calendario = calendar.HTMLCalendar()
print(calendario.formatmonth(2024, 4))
calendario = calendar.LocaleTextCalendar()
print(calendario.formatmonth(2024, 4))
calendario = calendar.LocaleHTMLCalendar()
print(calendario.formatmonth(2024, 4))

l = locale.setlocale(locale.LC_ALL, "sv_SE")
c = calendar.LocaleTextCalendar(locale=l)
print(c.formatmonth(2024, 4))

c = calendar.LocaleHTMLCalendar(locale=l)
print(c.formatmonth(2024, 4))
