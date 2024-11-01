
# La recursion son llamadas que la propia funcion se hace a si misma

def factorial(factorial_actual=1, numero_siguiente=1, numero_recursiones=1):

    if numero_recursiones == 1:
        return 1
    else:
        numero_siguiente += 1
        numero_recursiones -= 1
        factorial_actual *= numero_siguiente
        print(factorial_actual)
        # Aqui retornamos el valor de la propia funcion, esto es Recursion
        return factorial(factorial_actual=factorial_actual, numero_siguiente=numero_siguiente, numero_recursiones=numero_recursiones)

print(factorial(numero_recursiones=7))



def fibonacci(numero_recursiones=1, secuencia_procesar: list=None):

    SECUENCIA_FIBONACCI_INICIAL = [0, 1]
    secuencia_actual = secuencia_procesar

    if numero_recursiones == 0:
        print(secuencia_actual)
    else:
        if secuencia_actual is None:
            secuencia_actual = SECUENCIA_FIBONACCI_INICIAL

        secuencia_actual.append(secuencia_actual[-2] + secuencia_actual[-1])
        numero_recursiones -= 1
        return fibonacci(numero_recursiones=numero_recursiones, secuencia_procesar=secuencia_actual)

fibonacci(7)
