import calendar

calendario = calendar.Calendar()

def iterador_calendario(item_calendar):
    for d in item_calendar:
        print(d, end=", ")

    print()
    print()

# Mostrar los numeros de los dias de la semana
iterador_calendario(calendario.iterweekdays())

"""
0, 1, 2, 3, 4, 5, 6,
"""

# mostrar los dias que tiene el mes (a semanas completas), retorna
# el numero del dia y los rellenos seran 0
iterador_calendario(calendario.itermonthdates(2024, 4))

"""
2024-04-01, 2024-04-02, 2024-04-03, 2024-04-04, 2024-04-05, 2024-04-06, 2024-04-07, 
2024-04-08, 2024-04-09, 2024-04-10, 2024-04-11, 2024-04-12, 2024-04-13, 2024-04-14, 
2024-04-15, 2024-04-16, 2024-04-17, 2024-04-18, 2024-04-19, 2024-04-20, 2024-04-21, 
2024-04-22, 2024-04-23, 2024-04-24, 2024-04-25, 2024-04-26, 2024-04-27, 2024-04-28, 
2024-04-29, 2024-04-30, 2024-05-01, 2024-05-02, 2024-05-03, 2024-05-04, 2024-05-05, 
"""

# mostrar los dias que tiene el mes (a semanas completas), retorna
# un objeto date
iterador_calendario(calendario.itermonthdays(2024, 4))

"""
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 
24, 25, 26, 27, 28, 29, 30, 0, 0, 0, 0, 0, 
"""

# mostrar los dias que tiene el mes (a semanas completas), retorna una tupla
# (dia del mes, dia de la semana) los rellenos seran (0, dia de la semana)
iterador_calendario(calendario.itermonthdays2(2024, 4))

"""
(1, 0), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 0), (9, 1), (10, 2), (11, 3), 
(12, 4), (13, 5), (14, 6), (15, 0), (16, 1), (17, 2), (18, 3), (19, 4), (20, 5), (21, 6), 
(22, 0), (23, 1), (24, 2), (25, 3), (26, 4), (27, 5), (28, 6), (29, 0), (30, 1), (0, 2), 
(0, 3), (0, 4), (0, 5), (0, 6), 
"""

# mostrar los dias que tiene el mes (a semanas completas), retorna una tupla
# con el año, mes y dia
iterador_calendario(calendario.itermonthdays3(2024, 4))

"""
(2024, 4, 1), (2024, 4, 2), (2024, 4, 3), (2024, 4, 4), (2024, 4, 5), (2024, 4, 6), (2024, 4, 7), 
(2024, 4, 8), (2024, 4, 9), (2024, 4, 10), (2024, 4, 11), (2024, 4, 12), (2024, 4, 29), (2024, 4, 30), 
(2024, 5, 1), (2024, 5, 2), (2024, 5, 3), (2024, 5, 4), (2024, 5, 5),
"""

# mostrar los dias que tiene el mes (a semanas completas), retorna una tupla
# con el año, mes, dia, y dia de la semana
iterador_calendario(calendario.itermonthdays4(2024, 4))

"""
(2024, 4, 1, 0), (2024, 4, 2, 1), (2024, 4, 3, 2), (2024, 4, 4, 3), (2024, 4, 5, 4), 
(2024, 4, 6, 5), (2024, 4, 7, 6), (2024, 4, 8, 0), (2024, 4, 9, 1), (2024, 4, 10, 2), 
(2024, 4, 11, 3), (2024, 4, 12, 4), (2024, 4, 13, 5), (2024, 4, 14, 6), (2024, 4, 15, 0), 
(2024, 4, 16, 1), (2024, 4, 17, 2), (2024, 4, 18, 3), (2024, 4, 19, 4), (2024, 4, 20, 5), 
(2024, 4, 21, 6), (2024, 4, 22, 0), (2024, 4, 23, 1), (2024, 4, 24, 2), (2024, 4, 25, 3), 
(2024, 4, 26, 4), (2024, 4, 27, 5), (2024, 4, 28, 6), (2024, 4, 29, 0), (2024, 4, 30, 1), 
(2024, 5, 1, 2), (2024, 5, 2, 3), (2024, 5, 3, 4), (2024, 5, 4, 5), (2024, 5, 5, 6),
"""

# mostrar los dias que tiene el mes (a semanas completas), retorna una lista
# con los dias de la semana, los rellenos a 0
iterador_calendario(calendario.monthdayscalendar(2024, 4))

"""
[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14], [15, 16, 17, 18, 19, 20, 21], 
[22, 23, 24, 25, 26, 27, 28], [29, 30, 0, 0, 0, 0, 0]
"""

iterador_calendario(calendario.monthdays2calendar(2024, 4))

"""
[(1, 0), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6)], 
[(8, 0), (9, 1), (10, 2), (11, 3), (12, 4), (13, 5), (14, 6)], 
[(15, 0), (16, 1), (17, 2), (18, 3), (19, 4), (20, 5), (21, 6)], 
[(22, 0), (23, 1), (24, 2), (25, 3), (26, 4), (27, 5), (28, 6)], 
[(29, 0), (30, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6)],
"""