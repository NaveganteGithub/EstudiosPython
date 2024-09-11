
# El PEP 344 se menciona que __cause__ sirve para guardar excepciones encadenadas de manera explicita.
# Una excepcion encadenada explicita se genera cuando salta una excepcion
# https://peps.python.org/pep-0344/#explicit-exception-chaining
# https://peps.python.org/pep-0344/#abstract
try:
    # raise [EXCEPTION] from [CAUSE]
    raise ZeroDivisionError from ArithmeticError("No se puede dividir por cero")
except ZeroDivisionError as excepcion:
    print(repr(excepcion.__cause__))

# El PEP 344 se menciona que __context__ sirve para guardar excepciones encadenadas de manera implicita.
# Una excepcion encadenada implicita se genera cuando se intenta manejar una excepcion
# despues de manejar una excepcion que no se ha podido manejar.
# https://www.youtube.com/watch?v=EyAip0iLliQ
# https://stackoverflow.com/questions/11235932/what-is-the-difference-between-cause-and-context
try:
    # raise [EXCEPTION] from [CAUSE]
    raise ZeroDivisionError from ArithmeticError("No se puede dividir por cero")
except ZeroDivisionError as excepcion:
    print(repr(excepcion.__context__))

    try:
        raise AttributeError()
    except AttributeError as excepcion_context:
        print(repr(excepcion_context.__context__))
