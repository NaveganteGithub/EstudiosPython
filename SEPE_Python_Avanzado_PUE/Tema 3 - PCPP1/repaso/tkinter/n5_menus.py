import tkinter

ventana = tkinter.Tk()
ventana.geometry("550x550+50+0")

menu_principal = tkinter.Menu(ventana)
ventana.config(menu=menu_principal)

menu_file = tkinter.Menu(ventana, tearoff=0)
menu_principal.add_cascade(label="File", menu=menu_file)

menu_file.add_command(label="Safe file")
menu_file.add_separator()

submenu = tkinter.Menu(ventana, tearoff=0)
menu_file.add_cascade(label="Export as...", menu=submenu)

submenu.add_command(label=".py")
submenu.add_command(label=".pdf")
submenu.add_command(label=".txt")

ventana.mainloop()
