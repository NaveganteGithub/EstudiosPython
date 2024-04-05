def detalle(nombre, apellido, edad, altura) :
    print("Nombre completo:", nombre, apellido)
    print("Edad:", edad)
    print("Altura:", altura)
    
# invocar a la funcion pasando los valores en el mismo orden que los parametros
# pasar por posicion
detalle('Pepito', 'Perez', 37, 1.75)

# invocar a la funcion pasando los valores con el nombre del parametro
# pasar con keyword
# util si le paso los parametros desordenados
detalle(nombre='Pepito', edad=37, apellido='Perez', altura=1.75)
print("Ejemplo de keyword", sep=" ", end="\n")

# si la funcion tiene declarados 4 parametros hay que invocarla con 4 datos
# TypeError: detalle() missing 1 required positional argument: 'altura'
# detalle('Pepito', 37, 1.75)

# TypeError: detalle() missing 1 required positional argument: 'apellido'
detalle(nombre='Pepito', edad=37, altura=1.75)