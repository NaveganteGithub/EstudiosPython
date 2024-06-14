import calendar

# Mostrar el calendario comenzando la semana en domingo, se puede poner el numero correspondiente al dia de la semana
calendar.setfirstweekday(6)
calendar.setfirstweekday(calendar.SUNDAY) # Aunque es mejor trabajar con la constante
calendar.prmonth(2024,4, w=4, l=2)