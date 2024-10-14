
import tkinter

ventana = tkinter.Tk()

ventana.geometry("750x350+150+0")

menu_principal = tkinter.Menu(ventana)
ventana.config(menu=menu_principal)

menu_archivo = tkinter.Menu(menu_principal, tearoff=0)
menu_editar = tkinter.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Archivo", menu=menu_archivo)
menu_principal.add_cascade(label="Editar", menu=menu_editar)

menu_archivo.add_command(label="Abrir")
menu_archivo.add_command(label="Abrir como...")
menu_archivo.add_separator()
menu_archivo.add_command(label="Guardar como...")
menu_archivo.add_command(label="Guardar")

menu_secundario = tkinter.Menu(menu_archivo, tearoff=0)
menu_archivo.add_cascade(label="Exportar", menu=menu_secundario)
menu_secundario.add_command(label="PDF")
menu_secundario.add_command(label="ODT")

ventana.mainloop()
