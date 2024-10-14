# Para poder mostrar la pila de llamadas necesitamos el modulo traceback
import traceback

try:
    dividendo = int(input("Introduce dividendo: "))
    divisor = int(input("Introduce divisor: "))
    division = dividendo / divisor
except ValueError as error:
    print("Error, debe ser un valor numerico")
    print(error)
    print(type(error))
    # mostrar la pila de llamadas
    traceback.print_exc()
except ZeroDivisionError as e:
    print("El divisor no puede ser cero")
    print(e)
except BaseException as ex: # equivalente a "except:"
    print("Otro tipo de error")
else:
    # solo si no hay errores muestro el resultado
    print("Resultado:", division)
finally:
    # Se ejecuta siempre al final
    print("------ FIN ------")