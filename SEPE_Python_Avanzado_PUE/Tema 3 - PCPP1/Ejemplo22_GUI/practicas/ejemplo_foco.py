import tkinter as tk

def mostrar_foco():
    boton_2.focus_set() # Ponemos el foco en el boton 2

    # Mostrar un mensaje que boton tiene el foco
    if ventana.focus_get() is boton_2:
        print("El boton 2 tiene el foco")
    else:
        print(ventana.focus_get())

ventana = tk.Tk()
ventana.title("Ejemplo de Foco")
ventana.geometry("300x300")

boton_1 = tk.Button(ventana, text="Boton 1")
boton_1.bind("<FocusIn>", func=lambda e: print("Tengo el foco"))
boton_1.bind("<FocusOut>", func=lambda e: print("Pierdo el foco"))
boton_1.pack()


boton_2 = tk.Button(ventana, text="Boton 2")
boton_2.pack()

# Cuando transcurra x milisegundos llae a una funcion
ventana.after(1000, mostrar_foco)

ventana.mainloop()
