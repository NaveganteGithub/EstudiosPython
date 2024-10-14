import tkinter


# https://www.geeksforgeeks.org/how-to-set-border-of-tkinter-label-widget/
ventana = tkinter.Tk()

ventana.geometry("750x250+50+50")

texto_ejemplo = tkinter.StringVar(value="Hola")

texto = tkinter.Entry(ventana,
                      show="*",  # Ofuscar caracteres
                      background="yellow",  # Color de fondo del componente
                      # bg="red",  # Color de fondo del componente
                      foreground="blue",  # Color de los caracteres o contenido
                      # fg="pink",  # Color de los caracteres o contenido
                      border="2", # Grosor de borde interior
                      borderwidth="5",  # Grosor de borde exterior
                      width=100,  # Ancho de la caja de texto
                      # relief="solid", # Define el tipo de relieve (borde) que va tener la caja de texto
                      justify="center",  # Formateara el texto para centrarlo
                      readonlybackground="red",  # Cuando el estado del componente es readonly
                      # state="readonly",  # Definimos el estado del componete
                      textvariable=texto_ejemplo  # Insertar un texto a traves de un StringVar
                      )
texto.pack(side=tkinter.RIGHT)


ventana.mainloop()