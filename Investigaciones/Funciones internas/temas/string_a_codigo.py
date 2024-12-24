# https://es.stackoverflow.com/questions/309128/cu%C3%A1l-es-la-diferencia-entre-exec-eval-y-compile-en-python-3
# https://stackoverflow.com/questions/44704229/python-3-exec-vs-eval-expression-evaluation
# https://stackoverflow.com/questions/6883033/accessing-args-from-within-a-function-in-python
''' 
eval() es una funcion de python que me sirve 
para ejecutar UNA sola linea de texto como si 
fuera un codigo de Python
'''
cadena = "2 + 5 ** 2"
resultado_eval = eval(cadena)
print(resultado_eval)

#############################

cadena = "print(2 + 5 ** 2)"
eval(cadena)

#############################

''' 
exec() es una funcion de python que me sirve 
para ejecutar VARIAS sola linea de texto como 
si fueran un codigo de Python
'''

codigo = f"""
x = 5
print(2 + x)
"""
exec(codigo)

############################

a = 5
codigo = f"""
x = {a}
print(2 + x)
"""
exec(codigo)

############################

codigo_2 = """
def calculo(a):
    return a
"""
exec(codigo_2) # En este caso como no hay print, devolvera None por eso no hay que poner variable

resultado_exec = calculo(2)
print(resultado_exec)

############################

codigo_3 = """
def calculo(*a):
    return a[0] ** a[1] + a[2]
"""
exec(codigo_3)

resultado_exec = calculo(2,5,6)
print(resultado_exec)

'''
eval() puede usarse para ejecutar codigo 
ya compilado con exec()
'''

cadena = "calculo(2,5,6)"
resultado = eval(cadena)
print(resultado)

############################

'''
compile() es una funcion que compila un codigo de 
una cadena de texto como si fuera un codigo Python
a un binario.
'''
codigo_4 = """
def calculo(*a):
    return a[0] ** a[1] + a[2]
"""

obj_code = compile(codigo_4, "<string>", "exec")
print(type(obj_code))

exec(obj_code)
resultado = calculo(2,5,6)
print(resultado)

################################

a = 5
codigo_5 = f"""
x = {a}
def calculo(*a):
    return a[0] ** a[1] + a[2] - x
"""

obj_code = compile(codigo_5, "<string>", "exec")
print(type(obj_code))

exec(obj_code)
resultado = calculo(2,5,6)
print(resultado)

################################

'''
Podemos usar compile() dentro de bucles for 
utilizando sus modos
'''

for i in range(10):
    codigo = "print(2 + 5 ** 2)"
    # Con el modo eval declaramos que solo se va a ejecutar un codigo de una linea
    codigo_compilado = compile(codigo, "<string>", "eval")
    exec(codigo_compilado)

for i in range(10):
    codigo = input("-$ ")
    if len(codigo) == 0: break
    '''
    Con el modo Single podemos hacer lo mismo que con eval, pero al contrario que eval
    el modo Single nos sirve para hacer interpretes interactivos que ejecuten un REPL
    (o Read Eval Print Loop), que es un bucle que lee un comando o expresion, la evalua
    para luego imprimir el resultado.
    '''
    codigo_compilado = compile(codigo, "<string>", "single")
    exec(codigo_compilado)
    
for i in range(10):
    codigo = f"""
print("Ciclo actual")
print({i})
"""
    codigo_compilado = compile(codigo, "<string>", "exec")
    exec(codigo_compilado)

################################

while True:
    codigo = input("-$ ")
    if len(codigo) == 0: break
    codigo_compilado = compile(codigo, "<string>", "single")
    exec(codigo_compilado)