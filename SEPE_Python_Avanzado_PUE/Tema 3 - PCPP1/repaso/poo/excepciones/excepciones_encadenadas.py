
try:
    raise ZeroDivisionError from ArithmeticError("No dividas por cero")
except ZeroDivisionError as excepcion:
    print(repr(excepcion.__cause__))


try:
    raise TypeError from Exception("Tipo de dato erroneo")
except TypeError as excepcion:
    print(repr(excepcion.__context__))

    try:
        raise ZeroDivisionError from ArithmeticError("No dividas por cero")
    except ZeroDivisionError as excepcion:
        print(repr(excepcion.__context__))
