import tkinter as tk

calculo = list()
operacion_matematica = ""

######################## LOGICA ########################
def marcar_pauta():
    """
    Esta funcion dibuja en la calculadora
    los digitos que tenemos introducidos
    actualmente
    :return:
    """
    operacion_matematica = " ".join(calculo)
    result_impresion.set(operacion_matematica)

def operacion(operador: str):
    """
    Esta funcion se encarga de evaluar e insertar
    los operadores que se seleccionen
    :param operador:
    :return:
    """

    # Esta condicional impide que el usuario no introduzca
    # un operador antes de introducir un numero
    if len(calculo) > 0:
        calculo.append(operador)
    # print(calculo, calculo[-1])

    # Actualizamos la calculadora
    marcar_pauta()

def introducir_numero(digito: str):
    """
    Esta funcion se encarga de evaluar e insertar
    los digitos que se seleccionen

    :param digito:
    :return:
    """
    # Como hay que concatenar varios digitos para formar un numero
    # y despues introducir un operador, tenemos que realizar una
    # condicional que evalue si el usuario ya ha introducido
    # numeros anteriormente para concatenar los digitos con el
    # numero actual, es decir para saber si hay o no un numero
    # en la ultima posicion de la lista
    if len(calculo) != 0 and len(calculo[-1]) != 0 and calculo[-1].isdigit():
        calculo[-1] = calculo[-1] + digito
        marcar_pauta()
        # print(calculo, calculo[-1])
        return

    # En caso de que no haya un digito en la ultima posicion lo introducimos
    calculo.append(digito)
    # print(calculo, calculo[-1])

    # Actualizamos la calculadora
    marcar_pauta()

def calcular(operacion_aritmetica: list):
    # Realizamos el calculo matematico
    operacion_matematica = " ".join(operacion_aritmetica)
    resultado = eval(operacion_matematica)
    result_impresion.set(resultado)

    # Reiniciamos todo lo introducido por el usuario
    operacion_matematica = ""
    calculo.clear()

def reiniciar():
    """
    Esta funcion limpiara todo lo realizado por el usuario
    :return:
    """
    result_impresion.set("")
    operacion_matematica = ""
    calculo.clear()

######################## INTERFAZ GRAFICA ########################

ancho = 6
altura = 2
tamaño_letra = 1

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("365x450")
ventana.configure(background="black")
ventana.resizable(width=False, height=False)

resultado = 0
result_impresion = tk.StringVar(value=resultado)
panel = tk.Label(ventana, background="black",
                 textvariable=result_impresion,
                 font=('Helvetica', 30),
                 foreground="white")
panel.place(x=27, y=70)

seccion_botones = tk.LabelFrame(ventana,
                                width=200, height=500,
                                borderwidth=2, background="black")
seccion_botones.place(x=27, y=150)

columna = 0
fila = 0
# Generaremos los botones del 1 al 9
for n in range(1, 9 + 1):
    # Convertimos de digito a string
    num_actual = str(n)
    # Creamos y agregamos el boton
    numero = tk.Button(seccion_botones,
                        text=num_actual,
                        width=ancho, height=altura,
                        font=tamaño_letra, background="gray", foreground="white",
                        command=lambda num=num_actual : introducir_numero(num))
    numero.grid(row=fila, column=columna)

    # Cambiaremos la posicion para el siguiente boton
    columna += 1
    if columna > 2:
        fila += 1
        columna = 0

boton_0 = tk.Button(seccion_botones,
                    text="0",
                    width=ancho, height=altura,
                    font=tamaño_letra, background="gray", foreground="white",
                    command=lambda : introducir_numero("0"))
boton_0.grid(row=3, column=0)

# Generamos los botones de la suma
fila = 0
for op in ['+', '-', '*', '//']:
    # Para poder utilizar funciones con parametros en los
    # botones hay que utilizar un lambda, en este caso se
    # esta utilizando un lambda sin argumentos
    # https://www.geeksforgeeks.org/how-to-pass-arguments-to-tkinter-button-command/
    operador = tk.Button(seccion_botones,
                      text=f" {op}" if op != "//" else "÷", # En el caso de la division el simbolo ÷
                      width=ancho, height=altura,
                      font=tamaño_letra,
                      command=lambda operador_actual =
                                     f" {op}" : introducir_numero(operador_actual))
    operador.grid(row=fila, column=3)
    fila += 1

igual = tk.Button(seccion_botones,
                  text="=",
                  width=ancho, height=altura,
                  font=tamaño_letra,
                  command=lambda : calcular(calculo))
reiniciar = tk.Button(seccion_botones,
                  text="C",
                  width=ancho, height=altura,
                  font=tamaño_letra,
                  command=reiniciar)

igual.grid(row=3, column=1)
reiniciar.grid(row=3, column=2)

ventana.mainloop()
