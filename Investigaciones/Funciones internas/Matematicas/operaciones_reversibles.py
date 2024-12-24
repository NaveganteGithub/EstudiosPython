a = 17
b = 3

r1 = a >> b
# print(r1)
r2 = r1 << b
# print(r2)

'''

a = 9797979797

for _ in range(10): 
    # print(a)
    a >>= 2

for _ in range(10): 
    # print(a)
    a <<= 2

print(a - 9797979797)

b = 9898989898

for _ in range(10): 
    # print(a)
    b >>= 2

for _ in range(10): 
    # print(a)
    b <<= 2

print(b - 9898989898)

'''

# Operaciones reversibles
def reducion(num: int):
    
    def ida(num: int):
        factor1 = num // 2
        resto = num % 2
        resultado = factor1 + resto
        return resultado, resto
    
    def vuelta(num: int, resto: int):
        resultado = num * 2 - resto
        return resultado
    
    # print(num)
    reducido, resto = ida(num)
    # print(reducido)
    restaurado = vuelta(reducido, resto)
    # print(restaurado)
    return num, reducido, restaurado

# print(reducion(17))
'''for i in range(65, 90 + 1):
    resultado = reducion(i)
    print(resultado, "Calculo revertido" if resultado[0] == resultado[2] else "No se ha revertido el calculo", sep=" -> ")
    if resultado[0] != resultado[2] : break
    if i < 92 : print(chr(i))'''

'''for i in range(6565656565, 9090909090 + 1):
    resultado = reducion(i)
    print(resultado, "Calculo revertido" if resultado[0] == resultado[2] else "No se ha revertido el calculo", sep=" -> ")
    if resultado[0] != resultado[2] or i > 6565656638: break'''

def reducion_v2(num: int):
    """
    La operacion matematica que he pensado es una simple operacion de aritmetica 
    basica para comprobar mi teoria de si se podria realizar un operacion simple 
    para devolver un numero a su estado original con una operacion aritmetica 
    despues de realizar una operacion.

    Numero a tratar = X
    Cociente = Y
    Resto = Z
    Resultado = R
    
    NOTA: Para realizar esta operacion los numeros tienen 
    que ser numeros naturales

    X // 2 = Y
    X % 2 = Z
    Y + Z = R

    17 // 2 = 8
    17 % 2 = 1
    8 + 1 = 9

    Para devolver un numero a su estado original tenemos 
    que realizar la siguiente operacion

    R
    """

    def ida(num: int):
        factor1 = num // 2
        resto = num % 2
        resultado = factor1 + resto
        return resultado, resto
    
    def vuelta(num: int, resto: int):
        resultado = num * 2 - resto
        return resultado
    
    restos = list()
    reducido, resto_actual = ida(num)
    restos.append(resto_actual)
    rango_accion = 25
    # print(reducido)

    for _ in range(rango_accion):
        # print(reducido)
        reducido, resto_actual = ida(reducido)
        restos.append(resto_actual)
    
    restos.reverse()
    restaurado = vuelta(reducido, restos[0])

    for i in range(1, rango_accion + 1):
        restaurado = vuelta(restaurado, restos[i])
        # print(restaurado)
    return num, reducido, restaurado

for i in range(6565656565, 9090909090 + 1):
    resultado = reducion_v2(i)
    print(resultado, "Calculo revertido" if resultado[0] == resultado[2] else "No se ha revertido el calculo", sep=" -> ")
    if resultado[0] != resultado[2] or i > 6565656638: break