# Namespaces are one honking great idea -- let's do more of those!
# -- Los espacios de nombre son una gran idea -- hagamos mas de esos

## MAL
from tkinter.ttk import Button

boton_mal_importado = Button()

# BIEN
from tkinter import ttk

boton_bien_importado = ttk.Button()
