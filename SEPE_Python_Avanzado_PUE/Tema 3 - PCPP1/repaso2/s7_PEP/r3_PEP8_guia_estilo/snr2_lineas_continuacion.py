# Las líneas de continuación son líneas de código dividas porque son demasiado largas.
# Las líneas de continuación tienen ser utilizadas en paréntesis entre los paréntesis
# o los corchetes

## Malo

mala_lista = [1,2,3,
    4,5,6,
    7,8,9,
    10,11,12,
    13,14,15,
    16,17,18,
    19,20
]

def calculo(a,b,c,
    d,e,f,g):
    return (a + b) + c + (d + e) + f + g

a = calculo(2,7,4,1,
    8,9,5)

## Bueno

buena_lista = [
    1,2,3,4,5,
    6,7,8,9,10,
    11,12,13,14,
    15,16,17,18,
    19,20
]

def mi_calculo(
        a,b,c,d,
        e,f,g):
    return (a + b) + c + (d + e) + f + g

b = mi_calculo(
    2,7,4,1,
    8,9,5)