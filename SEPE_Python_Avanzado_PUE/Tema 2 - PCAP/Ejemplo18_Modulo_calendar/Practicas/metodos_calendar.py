import calendar

calendario = calendar.Calendar()

def iterador_calendario(item_calendar):
    for d in item_calendar:
        print(d, end=", ")

    print()
    print()

# Mostrar los numeros de los dias de la semana
iterador_calendario(calendario.iterweekdays())
# mostrar los dias que tiene el mes (a semanas completas), retorna
# el numero del dia y los rellenos seran 0
iterador_calendario(calendario.itermonthdates(2024, 4))
# mostrar los dias que tiene el mes (a semanas completas), retorna
# un objeto date
iterador_calendario(calendario.itermonthdays(2024, 4))
# mostrar los dias que tiene el mes (a semanas completas), retorna una tupla
# (dia del mes, dia de la semana) los rellenos seran (0, dia de la semana)
iterador_calendario(calendario.itermonthdays2(2024, 4))
# mostrar los dias que tiene el mes (a semanas completas), retorna una tupla
# con el año, mes y dia
iterador_calendario(calendario.itermonthdays3(2024, 4))
# mostrar los dias que tiene el mes (a semanas completas), retorna una tupla
# con el año, mes, dia, y dia de la semana
iterador_calendario(calendario.itermonthdays4(2024, 4))
# mostrar los dias que tiene el mes (a semanas completas), retorna una lista
# con los dias de la semana, los rellenos a 0
iterador_calendario(calendario.monthdayscalendar(2024, 4))

iterador_calendario(calendario.monthdays2calendar(2024, 4))