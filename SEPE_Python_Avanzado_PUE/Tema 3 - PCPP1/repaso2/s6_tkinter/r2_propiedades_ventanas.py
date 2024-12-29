import tkinter as tk

ventana = tk.Tk()

ventana.title("Mi titulo")
ventana.geometry("1280x720+50+7")

# https://www.geeksforgeeks.org/iconphoto-method-in-tkinter-python/
foto = tk.PhotoImage(file=".\\logo\\man.png")
# El primer parametro se debe a que este método utilizara un método call u otro,
# si ponemos True utilizará el método call por DEFECTO
# ventana.iconphoto(False, foto)

ventana.iconbitmap(".\\logo\\man.ico")

ventana.maxsize(width=1280, height=720)
ventana.minsize(width=500, height=500)
ventana.resizable(width=True, height=True)
print(ventana.attributes())
# ventana.aspect()

# Resulta que el método call es el método que utiliza tkinter
# por debajo para realizar todas sus operaciones, cuando usamos
# este método usamos tkinter a bajo nivel
# ventana.tk.call("wm", "iconphoto", ventana, foto)

ventana.mainloop()
