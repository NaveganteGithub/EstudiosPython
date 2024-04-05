def main():
    height = int(input("Height: "))
    pyramid(height)

def pyramid(n):
    for i in range(n):
        # print(i, end=" ") # Se puede utilizar print para realizar comprobaciones
        print("#" * (i + 1))

if __name__ == "__main__":
    main()

'''
En algunos IDE se tiene la posibilidad de realizar Depuraciones mediante herramientas
que llevan incorporadas o herramientas de tercero

En Visual Studio Code tienes una herramienta que sirve para depurar tu codigo mediante
el uso de breakpoints, despues de declarar tu breakpoint, activas la opcion de depuracion
y comenzara la depuracion empezando por la aparicion de una vista para depurar en la
interfaz de Visual Studio Code

    - Con el boton de "Continuar" haras que tu codigo se ejecute hasta el final del programa.
    - Con el boton de "Depurar paso a paso por procedimientos" haras que tu codigo se ejecute
    pero sin pasar por las funciones creadas, solo ejecutaras las funciones que haya declaradas
    en tu codigo, ni analizara el main, ni analizara el pyramid, es decir, solo ejecutara las
    funciones escritas en el codigo, y no la instrucciones dentro de dicho codigo.
    - Con el boton de "Depurar paso a paso por instrucciones" haran una ejecucion del codigo
    ejecutando las funciones examinando las instrucciones de cada funcion declarada, es decir,
    miraras cada instruccion de codigo, incluso las instrucciones de cada funcion


'''