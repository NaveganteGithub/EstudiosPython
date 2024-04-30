import tkinter as tk

# crear una nueva ventana

ventana = tk.Tk()

# Asignarle un titulo

ventana.title("Ejemplo de widgets")

# Definir tamaño de la ventana

'''tamaño = '200x300'
tamaño = '500x800'
ventana.geometry(tamaño)'''

# Definir la posicion de la ventana
tamaño = '500x800' # Ancho por Alto
posicion = '500+200' # Posicion X mas la posicion Y
forma = tamaño + "+" + posicion
ventana.geometry(forma)

boton = tk.Button(ventana, text='Pulsame', bg='#0000AA', fg='white')
boton.place(x=10, y=20)

etiqueta = tk.Label(ventana, text="Introduce tu nombre:", bg='blue', fg='white')
etiqueta.place(x=10, y=50)

etiqueta_2 = tk.Label(ventana, text="Introduce tu nombre:", bg='#0000AA', fg='white')
etiqueta_2.place(x=10, y=50)

# mostrar la ventana

ventana.mainloop()
