import tkinter

ventana = tkinter.Tk()
ventana.geometry("500x500+10+0")

lienzo = tkinter.Canvas(ventana, width="500", height="500", background="white")
lienzo.place(x=0, y=0)

lienzo.create_line(10, 10, 100, 10)
lienzo.create_line(10, 20, 100, 20, arrow=tkinter.FIRST)
lienzo.create_line(10, 30, 100, 30, arrow=tkinter.LAST)
lienzo.create_line(10, 40, 100, 40, arrow=tkinter.BOTH)
lienzo.create_line(10, 50, 100, 50, dash=(5, # grosor de línea
                                          2 # espacio entre línea y línea
                                          ))
lienzo.create_line(10, 70, 100, 70, width=20)
lienzo.create_line(10, 120, 100, 120, arrow=tkinter.LAST, arrowshape=(10, # grosor de flecha
                                                                      40, # altura de picos de flecha
                                                                      30, # que tan juntos estan los picos de la linea
                                                                      ))

lienzo.create_rectangle(110, 10, 150, 80)
lienzo.create_arc(70, 90, 150, 220)
lienzo.create_oval(160, 10, 200, 80)

lienzo.create_text(30, 180, text="Hola", justify="center", width="200")

mi_imagen = tkinter.PhotoImage(file=".\\logo\\man.png")
lienzo.create_image(200, 180, image=mi_imagen, width=50, height=50)

ventana.mainloop()
