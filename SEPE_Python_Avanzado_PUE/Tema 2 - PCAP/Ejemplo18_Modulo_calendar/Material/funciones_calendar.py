import calendar
import locale

# con la funcion calendar mostramos el calendario del año pasado como argumento
print(calendar.calendar(2024, w=4, l=2, c=10, m=2))

# mostrar el calendario de un mes y año especifico
print(calendar.month(2024, 4, w=4, l=2))

# mostrar el calendario de un mes y año especifico, sin necesidad de meterlo en print()
calendar.prmonth(2024, 4, w=4, l=2)

# Mostrar el calendario pero comenzsando la semana en domingo
# Podemos poner el numero correspondiente al dia de la semana
calendar.setfirstweekday(6)
# trabajar con la constante
calendar.setfirstweekday(calendar.SUNDAY)
calendar.prmonth(2024, 4, w=4, l=2)

# Dada una fecha retorna el dia de la semana en numero (lunes = 0)
print(calendar.weekday(2024, 4, 17))  # 2

# Retorna una cadena con los dias de la semana en x caracteres pasados como argumento
# 3 es el valor maximo para sacar los nombres abreviados
# A partir de 9 los saca completos
print(calendar.weekheader(1)) # S M T W T F S
print(calendar.weekheader(2)) # Su Mo Tu We Th Fr Sa
print(calendar.weekheader(3)) # Sun Mon Tue Wed Thu Fri Sat
print(calendar.weekheader(4)) # Sun  Mon  Tue  Wed  Thu  Fri  Sat
print(calendar.weekheader(5)) #  Sun   Mon   Tue   Wed   Thu   Fri   Sat
print(calendar.weekheader(6)) #  Sun    Mon    Tue    Wed    Thu    Fri    Sat
print(calendar.weekheader(7)) #  Sun     Mon     Tue     Wed     Thu     Fri     Sat
print(calendar.weekheader(8)) #   Sun      Mon      Tue      Wed      Thu      Fri      Sat
print(calendar.weekheader(9)) #   Sunday    Monday   Tuesday  Wednesday  Thursday   Friday   Saturday

# Retorna un valor booleano indicando si el año es bisiesto o no
print("Es 2024 bisiesto?", calendar.isleap(2024))  # True
print("Es 2023 bisiesto?", calendar.isleap(2023))  # False

# Cuantos años bisiestos hay entre un rango de años
# Recordar que en los rangos el ultimo no esta incluido  [desde, hasta)
print("Cuantos bisiestos entre 2010 y 2024 sin incluir", calendar.leapdays(2010,2024)) # 3
print("Cuantos bisiestos entre 2010 y 2024 incluye", calendar.leapdays(2010,2025)) # 4

# Obtener el encabezado de la semana completo
# w=9 es lo mismo que calendar.weekheader(9)
print(calendar.calendar(2024, w=9, l=2, c=10, m=2))

print(calendar.calendar(2024))
print(calendar.TextCalendar().formatmonth(2024,4))
print(calendar.HTMLCalendar().formatmonth(2024,4))

c = calendar.LocaleTextCalendar()
print(c.formatmonth(2024, 4))

# mostrar el calendario en Sueco
l = locale.setlocale(locale.LC_ALL, "sv_SE")
c = calendar.LocaleTextCalendar(locale=l)
print(c.formatmonth(2024, 4))

c = calendar.LocaleHTMLCalendar()
print(c.formatmonth(2024, 4))





