import calendar

# Cuantos años bisiestos hay entre un rango de años
# Recordar que en los rangos el ultimo no esta incluido
print("Cuantos bisiestos entre 2010 y 2024 sin incluir", calendar.leapdays(2010, 2024))
print("Cuantos bisiestos entre 2010 y incluyendo el 2024", calendar.leapdays(2010, 2025))

"""
Cuantos bisiestos entre 2010 y 2024 sin incluir 3
Cuantos bisiestos entre 2010 y incluyendo el 2024 4
"""