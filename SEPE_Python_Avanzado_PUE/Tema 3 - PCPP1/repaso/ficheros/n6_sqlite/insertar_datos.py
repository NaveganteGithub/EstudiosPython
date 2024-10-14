import sqlite3

conexion = sqlite3.connect("mi_bd.db")

mi_cursor = conexion.cursor()

mi_cursor.execute("insert into Empleados values (?, ?, ?)", (1, "Andres", 2000.20))

empleados = [(2, "Sofia", 2102.13),
         (3, "Alejandro", 2350.75),
         (4, "Daniel", 2150.01)
         ]

mi_cursor.executemany("insert into Empleados values (?, ?, ?)", empleados)

hijos = [("Alberto", 1),
         ("Sara", 2)
         ]
mi_cursor.executemany("insert into Hijos_Empleados values(?, ?)", hijos)

conexion.commit()

conexion.close()
