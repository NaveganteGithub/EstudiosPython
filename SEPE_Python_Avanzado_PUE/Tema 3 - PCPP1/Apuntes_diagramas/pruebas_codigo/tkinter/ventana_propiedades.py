
import tkinter

ventana = tkinter.Tk()

ventana.title("Mi titulo")

ventana.geometry("750x350+200+0")

ventana.tk.call("wm", "iconphoto", ventana, tkinter.PhotoImage(file=".\\logo\\man.png"))

ventana.config(background="yellow", padx=15, pady=15)

ventana.minsize(width=750, height=250)
ventana.maxsize(width=1000, height=400)

ventana.resizable(width=True, height=False)

ventana.mainloop()
