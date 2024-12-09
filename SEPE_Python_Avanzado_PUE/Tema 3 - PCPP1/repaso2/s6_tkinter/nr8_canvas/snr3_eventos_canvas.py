import tkinter as tk

# Ejemplo de Microsoft Copilot

def toggle_state(event):
    if canvas.itemcget(line, "state") == "disabled":
        canvas.itemconfig(line, state="normal")
    else:
        canvas.itemconfig(line, state="disabled")

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Dibuja una línea con parámetros deshabilitados
line = canvas.create_line(50, 50, 200, 200, fill="blue", width=2, dash=(4, 2), disabledfill="gray", disabledwidth=1, disableddash=(1, 1))

# Vincular evento para alternar estado de la línea
canvas.bind("<Button-1>", toggle_state)

root.mainloop()
