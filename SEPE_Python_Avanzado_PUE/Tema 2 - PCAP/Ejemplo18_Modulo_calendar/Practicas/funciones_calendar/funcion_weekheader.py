import calendar

# Retorno una cadena con los dias de la semana en x caracteres
print(calendar.weekheader(1))
print(calendar.weekheader(2))
print(calendar.weekheader(3))
# Cuando superamos el 3 ya no te muestra mas letras sino que agregara mas espacios
print(calendar.weekheader(4))
for i in range(5, 8 + 1):
    print(calendar.weekheader(i))
print(calendar.weekheader(9)) # Cuando pones 9 te muestra el nombre del dia de la semana completo

"""
M T W T F S S
Mo Tu We Th Fr Sa Su
Mon Tue Wed Thu Fri Sat Sun
Mon  Tue  Wed  Thu  Fri  Sat  Sun 
 Mon   Tue   Wed   Thu   Fri   Sat   Sun 
 Mon    Tue    Wed    Thu    Fri    Sat    Sun  
  Mon     Tue     Wed     Thu     Fri     Sat     Sun  
  Mon      Tue      Wed      Thu      Fri      Sat      Sun   
  Monday   Tuesday  Wednesday  Thursday   Friday   Saturday   Sunday 
"""

# Obtener el encabezado de la semana, estableciendo como primer dia el Domingo
header = calendar.weekheader(1)
cal = calendar.TextCalendar(calendar.SUNDAY)
# Obtener el calendario mes actual
month_calendar = cal.formatmonth(2024, 4)

combined_calendar = f"{header}\n{month_calendar}"
print(combined_calendar)

"""
M T W T F S S
     April 2024
Su Mo Tu We Th Fr Sa
    1  2  3  4  5  6
 7  8  9 10 11 12 13
14 15 16 17 18 19 20
21 22 23 24 25 26 27
28 29 30
"""
