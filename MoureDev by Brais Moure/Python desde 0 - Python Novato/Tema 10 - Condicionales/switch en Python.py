
'''
Partir de la version 3.10 de python se agregon los switches

https://docs.python.org/3/whatsnew/3.10.html#syntax-and-operations
https://docs.python.org/3/whatsnew/3.10.html#simple-pattern-match-to-a-literal
'''
condicional = 1

match condicional:
    case 1:
        print("Pequeño")
    case 2:
        print("Mediano")
    case 3:
        print("Grande")
    case 4:
        print("Montañoso")
    case _:
        print("Null, a cumplido con la funcion")