from tkinter import *

mi_ventana = Tk()

mi_ventana.title("Mi segunda ventana")

mi_ventana.geometry("1280x720")

"""
Label es un objeto que me permite introducir un texto en un ventana
este tiene varios parametros

El 1 parametro sera para indicar el objeto de la ventana Tk donde se quiere
implementar el objeto Label

El parametro text es el texto del objeto Label

El parametro font es el formato de letra que tendra el texto del objeto Label
    Se puede utilizar {} para indicar todos los formatos de la letra, pero es
    mas recomendable utilizar () para indicar todos los formatos de la letra,
    {} da demasidos errores, () no da tantos errores
"""
mi_texto = Label(mi_ventana, text="Un texto normal", font=("Arial", 20))

"""
place es una funcion que permite determinar la posicion de un widget
de manera no fija, o por libre.

"x" permite determinar la posicion de un widget siendo la posicion 0 
el borde izquierdo de la ventana

"y" permite determinar la posicion de un widget siendo la posicion 0 
el borde superior de la ventana

width permite definir el ancho de la caja de texto

height permite definir el alto de la caja de texto
    Como dato adicional si quieres tener un texto con un formato de letra 
    mas grande, tienes que hacer que tu caja de texto sea mas grande, y solo
    podras tener un letra tan grande como de grande se la caja de texto, es decir,
    si en un label quieres poner en la parametro font un tamaño de 20 por ejemplo
    tu caja de texto tiene que tener tambien un tamaño de 20 o mas
"""
mi_texto.place(x=150, y=20, width=1000, height=30)

mi_texto_2 = Label(mi_ventana, text="Un texto normal 2", font=("Arial", 40))
mi_texto_2.place(x=150, y=80, width=1000, height=60)

mi_texto_3 = Label(mi_ventana, text="Un texto normal 3", font=("Arial", 80))
mi_texto_3.place(x=150, y=180, width=1000, height=100)

mainloop()