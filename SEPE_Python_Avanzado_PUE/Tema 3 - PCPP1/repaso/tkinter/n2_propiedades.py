import tkinter

ventana = tkinter.Tk()

ventana.title("Propiedades de ventana")

ventana.geometry("750x750+50+0")

foto = tkinter.PhotoImage(file=".\\logo\\man.png")
ventana.tk.call("wm", "iconphoto", ventana, foto)

ventana.config(padx="50", pady="50", background="white")

ventana.minsize(width=450, height=450)

ventana.maxsize(width=750, height=750)

ventana.resizable(width=False, height=True)

ventana.mainloop()
