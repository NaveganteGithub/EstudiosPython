import tkinter as tk
from tkinter import messagebox

# crear una nueva ventana

ventana = tk.Tk()

# Asignarle un titulo

ventana.title("Ejemplo de eventos")
ventana.geometry("700x500+100+100")

# Agregar boton a la ventana

"""def pulsar():
    messagebox.showinfo("Detalle", "Has pulsado el boton")"""


def pulsar(event=None):
    messagebox.showinfo("Detalle", "Has pulsado el boton")


boton = tk.Button(ventana, text='Pulsame', command=pulsar)
boton.place(x=10, y=20)


# Agregar boton a la ventana

def pregunta(event=None):
    respuesta = messagebox.askquestion("Pregunta", "Cerramos la ventana?")
    print("Has elegido yes" if respuesta == "yes" else "Has elegido no")


boton_2 = tk.Button(ventana, text='Pregunta', command=pregunta)
boton_2.place(x=10, y=80)


# Abrir o cerrar ventana

def cerrar_ventana():
    ventana.destroy()


# boton = tk.Button(ventana, text="Cerrar", command=cerrar_ventana)  # Opcion 1
boton = tk.Button(ventana, text="Cerrar", command=ventana.destroy)  # Opcion 2
boton.pack()


def abrir_ventana():
    ventana_2 = tk.Toplevel(ventana)
    ventana_2.mainloop()


boton = tk.Button(ventana, text="Abrir", command=abrir_ventana)
boton.pack()

# Eventos para perifericos

def coordinate(event):
    boton_raton_pulsado = event.num

    match boton_raton_pulsado:
        case 1:
            boton_raton_pulsado = "Boton izquierdo del ratón pulsado"
        case 2:
            boton_raton_pulsado = "Rueda del ratón pulsada"
        case 3:
            boton_raton_pulsado = "Boton derecho del ratón pulsado"
        case _:
            boton_raton_pulsado = "Boton misterioso"

    print(boton_raton_pulsado, ', coordenadas x = %d, y = %d' % (event.x, event.y), sep="")


def entrada(event):
    print("He entrado dentro del Frame")


def salida(event):
    print("He salido fuera del Frame")


frame = tk.Frame(ventana, height=100, width=450, background="black")

# Eventos en un click para el raton
frame.bind("<Button-1>", coordinate)  # Boton izquierdo del ratón
frame.bind("<Button-2>", coordinate)  # Rueda del ratón
frame.bind("<Button-3>", coordinate)  # Boton derecho del ratón

# Eventos al mover el raton
frame.bind("<Enter>", entrada)  # Se activa al Introducir el Cursor del Ratón dentro de la ventana
frame.bind("<Leave>", salida)  # Se activa al Extraer el Cursor del Ratón dentro de la ventana

frame.place(x=150, y=150)


# Evento de doble click
def pulsacion_correcta(event):
    print("Se ha confirmado la pulsacion")


boton_3 = tk.Button(ventana, text="Doble click")
boton_3.bind("<Double 1>", pulsacion_correcta)
boton_3.place(x=50, y=200)


# Eventos para el teclado

# Caracteres
def caracteres(evento):
    tecla_pulsada = evento.char
    print(tecla_pulsada)


ventana.bind("<Key>", caracteres)  # Pulsa cualquier tecla, para que lo veas mejor pulsa una letra o digito


# Eventos al mover el raton
def entrada_ventana(event):
    print("He entrado dentro de la ventana")


def salida_ventana(event):
    print("He salido fuera de la ventana")


# ventana.bind("<Enter>", entrada_ventana)
# ventana.bind("<Leave>", salida_ventana)

# mostrar la ventana
ventana.mainloop()
