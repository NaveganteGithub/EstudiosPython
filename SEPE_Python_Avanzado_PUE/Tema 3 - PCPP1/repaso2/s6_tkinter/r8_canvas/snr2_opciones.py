import tkinter as tk

ventana = tk.Tk()
ventana.geometry("780x740+50+50")

# Todos estos parámetros están también presentes en los métodos, create_oval, create_arc, create_rectangle

lienzo = tk.Canvas(ventana, height=700, width=700,background="white")
lienzo.pack()
lienzo.create_line(10, 10, 120, 10)
lienzo.create_line(10, 30, 120, 30, width=4) # Ancho de linea
lienzo.create_line(10, 140, 120, 140, fill="green") # Color de linea
lienzo.create_line(10, 40, 120, 40, dash=(6,3)) # Punteo de linea

lienzo.create_line(10, 50, 120, 50, arrow=tk.LAST)  # Flecha de linea
lienzo.create_line(10, 90, 120, 90, arrow=tk.FIRST, arrowshape=(10,  # Ancho del centro de la flecha
                                                               30,  # Estrecho de la flecha
                                                               20))  # Ancho de la flecha

lienzo.create_line(10, 180, 120, 180, capstyle=tk.BUTT, width=7)  # Estilo de punta cuadrada
lienzo.create_line(10, 200, 120, 200, capstyle=tk.ROUND, width=7)  # Estilo de punta triangular
lienzo.create_line(10, 220, 120, 220, capstyle=tk.PROJECTING, width=7)

# Cuando hay más de dos líneas, podemos definir que estilo deben definir en sus puntos de union
lienzo.create_line(10, 310, 120, 310, 120, 260, joinstyle=tk.ROUND, width=4)
lienzo.create_line(10, 380, 120, 380, 120, 330, joinstyle=tk.BEVEL, width=4)  # Linea redondeada
lienzo.create_line(10, 440, 120, 440, 120, 400, joinstyle=tk.MITER, width=4)

# La linea es curva
lienzo.create_line(10, 500, 120, 500, 120, 480, smooth=True)
lienzo.create_line(10, 570, 120, 570, 120, 520, smooth=True, splinesteps=5) # Número de ángulos de la curva

# Cuando pones el curso encima del dibujo cambia ...
lienzo.create_line(140, 10, 250, 10, width=3, activewidth=5)  # de tamaño
lienzo.create_line(140, 20, 250, 20, fill="red", activefill="blue")  # el color
lienzo.create_line(140, 30, 250, 30, dash=(2,5), activedash=(5,2))  # el punteo

# Cuando ponemos el estado disabled el dibujo cambia ...
lienzo.create_line(140, 70, 250, 70, width=3, disabledwidth=8, state="disabled")  # de tamaño
lienzo.create_line(140, 90, 250, 90, fill="yellow", disabledfill="purple", state="disabled")  # el color
lienzo.create_line(140, 100, 250, 100, dash=(3,1), disableddash=(2,8), state="disabled")  # el punteo

ventana.mainloop()
