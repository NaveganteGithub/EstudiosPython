import tkinter
from tkinter import filedialog

ventana = tkinter.Tk()

ventana.geometry("750x550+150+0")


def nombre_archivo():
    ventana_file = filedialog.askopenfilename(title="Abrir archivo")
    print(ventana_file)


def nombre_archivos():
    ventana_file = filedialog.askopenfilenames(title="Abrir archivos")
    print(ventana_file)


def abrir_archivo():
    ventana_file = filedialog.askopenfile(title="Abrir archivo")
    print(ventana_file)


def abrir_archivos():
    ventana_file = filedialog.askopenfiles(title="Abrir archivos")
    print(ventana_file[0])


def salvar_archivo():
    ventana_file = filedialog.asksaveasfile(title="Salvar archivo")
    print(ventana_file)
    ventana_file.write("Hola")


def salvar_archivos():
    ventana_file = filedialog.asksaveasfilename(title="Salvar nombre archivo")
    print(ventana_file, ventana_file.title())


def directorios():
    ventana_dir = filedialog.askdirectory(title="Directorio")
    print(ventana_dir)


boton_1 = tkinter.Button(ventana, text="Nombre de archivo", command=nombre_archivo)
boton_1.pack(side=tkinter.RIGHT)

boton_2 = tkinter.Button(ventana, text="Nombres de archivo", command=nombre_archivos)
boton_2.pack(side=tkinter.RIGHT)

boton_3 = tkinter.Button(ventana, text="Abrir archivo", command=abrir_archivo)
boton_3.pack(side=tkinter.LEFT)

boton_4 = tkinter.Button(ventana, text="Abrir archivos", command=abrir_archivos)
boton_4.pack(side=tkinter.LEFT)

boton_5 = tkinter.Button(ventana, text="Salvar archivo", command=salvar_archivo)
boton_5.pack(side=tkinter.TOP)

boton_6 = tkinter.Button(ventana, text="Salvar archivos", command=salvar_archivos)
boton_6.pack(side=tkinter.TOP)

boton_7 = tkinter.Button(ventana, text="Capturar directorio", command=directorios)
boton_7.pack(side=tkinter.BOTTOM)

ventana.mainloop()
