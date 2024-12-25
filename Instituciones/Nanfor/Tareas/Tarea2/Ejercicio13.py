from tkinter import *

mi_ventana = Tk()
textos = list()
texto_actual = ''

mi_ventana.title("Tres en raya, el ganador a sido el jugador con las fichas O")

mi_ventana.geometry('1280x720')

for cont in range(1,10):
    if cont in [1,8,9]:
        texto_actual = ''
    elif cont % 2 != 0:
        texto_actual = 'O'
    else:
        texto_actual = 'X'
        
    textos.append(Label(mi_ventana, text=texto_actual, font={"Arial", 20}))

cont_column = 0
cont_row = 0

for main_cont in range(0,9):
    textos[main_cont].grid(column=cont_column, row=cont_row)
    
    if cont_column == 2:
        cont_column = 0
        cont_row += 1
    else:
        cont_column += 1

mi_ventana.mainloop()