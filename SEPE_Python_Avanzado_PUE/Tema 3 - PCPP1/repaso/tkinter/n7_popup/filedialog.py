from tkinter import filedialog
from tkinter import Tk
from tkinter import Button

# https://stackoverflow.com/questions/44403566/add-multiple-extensions-in-one-filetypes-mac-tkinter-filedialog-askopenfilenam
ventana = Tk()
extension_por_defecto = ".docx"
extensiones = [("Archivos de texto", ".txt"), ("Documentos de Microsoft", "*.docx")]

def nombre_archivo():
    resultado = filedialog.askopenfilename(defaultextension=extension_por_defecto,
                                           filetypes=extensiones,
                                           initialfile="Nombre de archivo por defecto",
                                           title="¿Cual es el archivo?")
    print(resultado)

def nombre_archivos():
    resultado = filedialog.askopenfilenames(defaultextension=extension_por_defecto, filetypes=extensiones, title="¿Cuales son los archivos?")
    print(resultado)

def archivo():
    resultado = filedialog.askopenfile(defaultextension=extension_por_defecto, filetypes=extensiones, title="¿Cual es el archivo?")
    print(resultado)

def archivos():
    resultado = filedialog.askopenfiles(defaultextension=extension_por_defecto, filetypes=extensiones, title="¿Cuales son los archivos?")
    print(resultado)

def salvar_archivo():
    resultado = filedialog.asksaveasfile(defaultextension=extension_por_defecto, filetypes=extensiones, title="¿Cual es el archivo?")
    print(resultado)

def salvar_nombre_archivo():
    resultado = filedialog.asksaveasfilename(defaultextension=extension_por_defecto, filetypes=extensiones, title="¿Cual es el archivo?")
    print(resultado)

def directorio():
    resultado = filedialog.askdirectory(title="¿Directorios?")
    print(resultado)

boton_1 = Button(ventana, text="Boton 1", width=20, command=nombre_archivo)
boton_2 = Button(ventana, text="Boton 2", width=20, command=nombre_archivos)
boton_3 = Button(ventana, text="Boton 3", width=20, command=archivo)
boton_4 = Button(ventana, text="Boton 4", width=20, command=archivos)
boton_5 = Button(ventana, text="Boton 5", width=20, command=salvar_archivo)
boton_6 = Button(ventana, text="Boton 6", width=20, command=salvar_nombre_archivo)
boton_7 = Button(ventana, text="Boton 7", width=20, command=directorio)

boton_1.pack()
boton_2.pack()
boton_3.pack()
boton_4.pack()
boton_5.pack()
boton_6.pack()
boton_7.pack()

ventana.mainloop()
