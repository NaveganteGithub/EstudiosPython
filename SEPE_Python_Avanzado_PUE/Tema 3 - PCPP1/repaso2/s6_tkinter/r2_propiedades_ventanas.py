import tkinter as tk

ventana = tk.Tk()

ventana.title("Mi titulo")
ventana.geometry("1280x720+50+7")

# https://www.geeksforgeeks.org/iconphoto-method-in-tkinter-python/
foto = tk.PhotoImage(file=".\\logo\\man.png")
# El primer parametro se debe a que este metodo utilizara un metodo call u otro,
# si ponemos True utilizara el metodo call por DEFECTO
ventana.iconphoto(False, foto)

ventana.maxsize(width=1280, height=720)
ventana.minsize(width=500, height=500)
ventana.resizable(width=True, height=True)
print(ventana.attributes())
# ventana.aspect()

# Resulta de que el metodo call es el metodo que ultiliza tkinter
# por debajo para realizar todas sus operaciones, cuando usamos
# este metodo usamos tkinter a bajo nivel
# ventana.tk.call("wm", "iconphoto", ventana, foto)

ventana.mainloop()