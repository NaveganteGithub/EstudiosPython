def main():
    x = get_num()
    print(f"x is {x}")

def get_num():
    while True:
        try:
            x = int(input("What´s x? "))
            return x
        except ValueError:
            pass
            '''
            pass sirve para pasar de largo o no hacer nada, en caso de la excepcion
            se pide que se maneje pero que no haga nada
            '''
main()

'''
def get_num():
    while True:
        try:
            x = int(input("What´s x? "))
            return x
        except ValueError:
            pass

'''

'''
def get_num():
    while True:
        try:
            x = int(input("What´s x? "))
            return x
        except ValueError:
            print("x is not an integer")
'''

'''
Tambien se puede realizar de esta manera, perderia legibilidad, pero se ganaria reduccion de lineas

while True:
    try:
        x = int(input("What´s x? "))
        break # break rompe el bucle
    except ValueError:
        print("x is not an integer")
'''