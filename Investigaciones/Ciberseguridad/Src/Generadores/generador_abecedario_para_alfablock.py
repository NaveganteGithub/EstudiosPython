abecedario = {}
letras = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
contador = 0

"""Este programa generara un diccionario de python con una 
clave numerica que representa el caracter unicode/ascii, y 
para cada clave un bloque de string como valor

https://home.unicode.org/technical-quick-start-guide/
https://www.unicode.org/versions/stats/charcountv15_1.html
https://www.unicode.org/versions/stats/charcountv13_0.html
"""

unicode = 150000
ascii = 256
bloques_letras = {3:"ZZZ", 5:"ZZZZZ"}
long_bloque = 5

try:
    for i in range(unicode):
        contador_str = str(contador).zfill(long_bloque)
        bloque = "".join([letras[int(num)] for num in contador_str])
        abecedario[i] = bloque
        if bloque == bloques_letras[long_bloque]: 
            print(i)
            break
        contador += 1
        # if i == 10: break
except:
    print("Programa finalizado")
else:
    with open("Investigaciones\\Ciberseguridad\\Src\\Generadores\\unicode.txt", "wt", encoding="utf-8") as file:
        file.write(str(abecedario))
