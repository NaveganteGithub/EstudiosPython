"""
    Solicitar al usuario la letra del dia de la semana (l,m,x,j,v,s,d)
    puede ser que introduzca la letra en mayuscula
    controlar si la letra no es valida
    mostrar el dia de la semana
"""

letra = input("Introduce dia de la semana (l,m,x,j,v,s,d): ")

if letra == 'l' or letra == 'L':
    print("Es lunes")
elif letra == 'm' or letra == 'M':
    print("Es martes")
elif letra == 'x' or letra == 'X':
    print("Es miercoles")
elif letra == 'j' or letra == 'J':
    print("Es jueves")
elif letra == 'v' or letra == 'V':
    print("Es viernes")
elif letra == 's' or letra == 'S':
    print("Es sabado")
elif letra == 'd' or letra == 'D':
    print("Es domingo")
else :
    print("Dia no valido")