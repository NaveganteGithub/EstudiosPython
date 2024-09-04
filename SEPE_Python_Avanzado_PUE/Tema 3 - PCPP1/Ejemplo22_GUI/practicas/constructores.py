import tkinter

ventana = tkinter.Tk()

ventana.geometry("750x250+50+50")

texto = tkinter.Entry(ventana,
                      show="*",  # Ofuscar caracteres
                      background="yellow",  # Color de fondo del componente
                      # bg="red",  # Color de fondo del componente
                      foreground="blue",  # Color de los caracteres o contenido
                      # fg="pink",  # Color de los caracteres o contenido
                      border="2", # Grosor de borde interior
                      borderwidth="5",  # Grosor de borde exterior
                      width=100,  # Ancho de la caja de texto
                      # relief="solid" # Define el tipo de relieve (borde) que va tener la caja de texto
                      )
texto.pack(side=tkinter.RIGHT)

ventana.mainloop()