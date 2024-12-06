import tkinter as tk

ventana = tk.Tk()
ventana.geometry("1280x720+50+10")

lienzo = tk.Canvas(height=500, width=500, background="white")
lienzo.pack()
lienzo.create_line(20, 20, 80, 20, arrow=tk.LAST, dash=(5,1,1,1), width=3)
lienzo.create_oval(20, 50, 80, 120)
lienzo.create_arc(20, 130, 80, 170)
lienzo.create_rectangle(20, 170, 80, 200)

lienzo.create_text(180, 20, text="Hola")

imagen = tk.PhotoImage(file=".\\logo\\man.png")
lienzo.create_image(20, 900, image=imagen)

ventana.mainloop()
