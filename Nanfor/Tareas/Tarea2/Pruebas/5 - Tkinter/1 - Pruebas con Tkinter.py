from tkinter import *

mi_ventana = Tk() # Crea una ventana de Python

mi_ventana.title("Graficas con Python") # Agrega un titulo a la ventana arriba a la izquierda

mi_ventana.geometry('1280x720') # Define el tamaño de la ventana

texto = Label(mi_ventana, text="Mi texto de prueba") # Crea un texto para la interfaz

texto.grid(column=0,row=0) # Define que el texto sea colocado en un grid en la primera columna y en la primera fila

boton = Button(mi_ventana, text="Mi boton de prueba") # Crea un boton para la interfaz

boton.grid(column=4, row=2) # Define que el boton sea colocado en un grid en la quinta columna y en la tercera fila

mainloop() # Activa la venta creada 
# mi_ventana.mainloop() # Activa la venta creada 