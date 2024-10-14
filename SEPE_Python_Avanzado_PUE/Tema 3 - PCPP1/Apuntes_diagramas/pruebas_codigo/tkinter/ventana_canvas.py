
import tkinter

ventana = tkinter.Tk()

ventana.geometry("750x750+150+100")

contenedor_dibujos = tkinter.Canvas(ventana, width=700, height=700, background="white")
contenedor_dibujos.place(x=10, y=10)

# contenedor_dibujos.create_line(50, 650, 250, 50, 450, 650, 550, 650, width=7, fill="black")

# contenedor_dibujos.create_rectangle(50, 120, 250, 340, width=5, fill="yellow")

# contenedor_dibujos.create_oval(70, 150, 140, 280, width=7, fill="black")

# contenedor_dibujos.create_oval(160, 150, 230, 280, width=7, fill="black")

contenedor_dibujos.create_arc(50, 140, 150, 280, width=5, fill="red")

# contenedor_dibujos.create_text(180, 150, width=5, text="Holahola")
# contenedor_dibujos.create_text(240, 150, width=26, text="Holahola")
# contenedor_dibujos.create_text(300, 150, text="Holahola")

mi_imagen = tkinter.PhotoImage(file="./logo/man.png")
contenedor_dibujos.create_image(350, 520, image=mi_imagen)

# dash: lineas punteadas dash=(distancia de las lineas, espacio entre linea y linea)
# arrow: flecha para la linea, opciones FIRST y LAST
# contenedor_dibujos.create_line(50, 150, 250, 50, dash=(5, 3), arrow=tkinter.LAST)
# contenedor_dibujos.create_line(70, 170, 270, 70, dash=(5, 1), arrow=tkinter.LAST)

ventana.mainloop()
