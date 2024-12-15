# Errors should never pass silently. -- Los errores nunca deben pasar desapercibidos

# Mal
try:
    print(7 / 0)
except:
    pass

# Bien
try:
    print(7 / 0)
except ArithmeticError as error_aritmetico:
    print(error_aritmetico)
