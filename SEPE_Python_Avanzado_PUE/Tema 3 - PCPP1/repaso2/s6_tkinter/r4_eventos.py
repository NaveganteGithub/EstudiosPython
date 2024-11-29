import tkinter as tk


ventana = tk.Tk()

# Evento por comando
def my_command():
    texto.set("Adios")

texto = tk.StringVar(value="Hola")
etiqueta = tk.Label(textvariable=texto)
# Existe un parametro llamado command que te permite introducir métodos
# y activarlo cuando el usuario pulse el botón
boton = tk.Button(ventana, text="Cambiar el texto", command=my_command)

etiqueta.place(x=10, y=10)
boton.place(x=10, y=30)


# Evento por accion: botones

def mi_evento(evento = None):

    if evento is None:
        exit("Evento no reconocido")

    print(type(evento), evento.__dict__, evento.type)
    
    match evento.num:
        case 1:
            print("Boton izquierdo pulsado")
        case 2:
            print("Rueda pulsada")
        case 3:
            print("Boton derecho pulsado")
        case _:
            raise RuntimeError from Exception("Boton desconocido")

cuadro = tk.Frame(ventana, background="yellow", height=50, width=50)
cuadro.bind("<Button-1>", mi_evento)
cuadro.bind("<Button-2>", mi_evento)
cuadro.bind("<Button-3>", mi_evento)
cuadro.place(x=10, y=70)

# Evento por accion: Entrar y salir

def introduccion(evento = None):

    if evento is None:
        exit("La accion no a sido recibida")

    print(type(evento), evento.__dict__, evento.type)
    match evento.type:
        case 7:
            print("Entrando")
        case 8:
            print("Saliendo")
        case _:
            print("Evento desconocido")

marco = tk.Frame(ventana, background="blue", height=50, width=50)
marco.bind("<Enter>", introduccion)
marco.bind("<Leave>", introduccion)
marco.place(x=70, y=70)

# Evento por accion: Teclado

def imprimir_letra(evento = None):
    # print(evento) # <KeyPress event send_event=True state=Mod1 keysym=f keycode=70 char='f' x=53 y=11>
    print(evento.char, end="")

caja_texto = tk.Entry(ventana)
caja_texto.bind("<Key>", imprimir_letra)
caja_texto.place(x=10, y=130)

# Evento por accion: Doble clic

def decision(evento = None):
    print(evento.__dict__)

cuadro = tk.Frame(ventana, height=50, width=50, background="green")
cuadro.bind("<Double 1>", decision)
cuadro.place(x=10, y=157)

ventana.mainloop()

