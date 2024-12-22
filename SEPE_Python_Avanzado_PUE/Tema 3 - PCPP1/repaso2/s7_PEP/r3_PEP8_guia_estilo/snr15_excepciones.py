# Usa la referencia del error, en vez de usar Excepcion o solo la cláusula except:

try:
    print(5/0)
except ArithmeticError:
    print(49/7)

