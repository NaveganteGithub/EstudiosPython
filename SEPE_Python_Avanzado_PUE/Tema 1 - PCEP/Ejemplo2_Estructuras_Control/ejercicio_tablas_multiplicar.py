""" mostrar las tablas de multiplicar  """

for tabla in range(1, 11) :     # tablas del 1 al 10
    print("************** Tabla del", tabla, "**************")
    
    for num in range(1, 11) :
        print(tabla, "x", num, "=", tabla*num)