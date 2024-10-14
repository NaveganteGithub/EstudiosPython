import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo de Foco")
ventana.geometry("500x400")

canvas = tk.Canvas(ventana, width=400, height=400, background="pink")

# Crear una linea por medio de indicar coordenadas y unir puntos, contando que el pincel tendra un grado de inclinacion
# Indicando varios parametros de x y
# podemos mover un cursor que nos va
# dibujar un triangulo como si fuera
# un pincel
# canvas.create_line(10, 10, 300, 10, arrow=tk.LAST)  # Crear una flecha que mire hacia a la derecha
# canvas.create_line(10, 20, 300, 20, arrow=tk.FIRST)  # Crear una flecha que mire hacia a la izquierda
# Crear una flecha que mire a la izquierda, con grosor de 5 y de color azul
# canvas.create_line(10, 30, 300, 30, arrow=tk.FIRST, width=5, fill="blue")

# Cada Canva se crea en base a especificar las coordenadas de
# cada punto P1(Coord_X1, Coord_Y1), P2(Coord_X2, Coord_Y2)
# Crear un triangulo apuntando hacia arriba
"""canvas.create_line(10, 380, # Indicamos el punto inicial (abajo a la izquierda)
                   200, 10, # Indicamos el punto de arriba
                   380, 380, # Indicamos el punto de abajo a la derecha
                   10, 380, # Volvemos el punto inicial
                   width=5, fill="blue")"""

# Crear flechas pero con lineas de puntos
canvas.create_line(10, 40, 300, 40, dash=(4, 4), arrow=tk.LAST, width=5, fill="blue")
canvas.create_line(10, 50, 300, 50, dash=(4, 5), arrow=tk.LAST, width=5, fill="blue")
canvas.create_line(10, 60, 300, 60, dash=(1, 5), arrow=tk.LAST, width=5, fill="blue")
canvas.create_line(10, 70, 300, 70, dash=(6, 2, 2, 2), arrow=tk.LAST, width=5, fill="blue")
canvas.create_line(10, 80, 300, 80, dash=(6, 2, 9, 18), arrow=tk.LAST, width=5, fill="blue")
canvas.create_line(10, 100, 300, 100, dash=(3, 6, 1, 5), arrow=tk.LAST, width=5, fill="blue")

# Creamos un rectangulo
# canvas.create_rectangle(50,50,200,300, outline="yellow", width=5, fill="green")

# Creamos un ovalo, utiliza un cuadrado imaginario para dibujar
"""canvas.create_oval(50, 50, 200, 300)
canvas.create_oval(300, 50, 400, 150)
canvas.create_oval(300, 50, 400, 150, dash=(8, 10), outline="red", width=5)"""

"""canvas.create_text(150, 50,
                   text="Esto es un ejemplo",
                   font=("Arial", "20", "bold"),
                   justify=tk.RIGHT,
                   fill="blue",
                   anchor=tk.NW,
                   width=180,
                   )"""

# Crear imagenes
"""logo = tk.PhotoImage(file="logo/man.png")
canvas.create_image(50, 50, image=logo)"""

"""canvas.create_arc(10, 10, 300, 100, style="arc")
canvas.create_arc(10, 120, 300, 180, style="chord")
canvas.create_arc(10, 300, 300, 250, style="pieslice")"""

canvas.pack()

ventana.mainloop()
