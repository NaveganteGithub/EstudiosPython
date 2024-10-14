import tkinter as tk
from tkinter import filedialog as file_dialog

ventana = tk.Tk()
ventana.title("Ejemplo propiedades de la ventana")

# Crear la barra del menu
barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

# Crear los menus
menu_file = tk.Menu(barra_menu, tearoff=0)  # tearoff permite quitar las lineas que se generan en la primera posicion
barra_menu.add_cascade(label="File", menu=menu_file)

menu_edit = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Edit", menu=menu_edit)


# Crear las opciones del menu File
def opcion(event=None):
    print("Has pulsado opcion", event)


def abrir():
    fichero = file_dialog.askopenfilename(title="Abrir fichero")
    print(fichero)


menu_new_proyect = tk.Menu(menu_file)

menu_file.add_command(label="New", command=opcion)
menu_file.add_command(label="Open", command=abrir)
menu_file.add_command(label="Close")

menu_file.add_separator()

menu_file.add_command(label="Copy")
menu_file.add_command(label="Paste")

# Crear las opciones del submenu Export del menu File
menu_export = tk.Menu(menu_file, tearoff=0)
menu_file.add_cascade(label="Export", menu=menu_export)
menu_export.add_command(label=".py")
menu_export.add_command(label=".pdf")

ventana.mainloop()
