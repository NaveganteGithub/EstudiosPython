class Pelicula:
    # Constructor de la clase (al crear la instancia)
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print('Se ha creadolapelicula', self.titulo)

    # Destructor de la clase (al borrar la instancia)
    # sobreescribimos el metodo heredado de object
    def __del__(self):
        print('Se ha borrado la pelicula', self.titulo)

    def __str__(self):
        return f"{self.titulo}, {self.duracion}, {self.lanzamiento}"

p = Pelicula('Avatar 2', 140, 2023)
print(p)

delattr(p, "lanzamiento")
print(p.__dict__)   # {'titulo': 'Avatar 2', 'duracion': 140}
#print(p) # NameError: name 'lanzamiento' is not defined

# Eliminar un atributo del objeto
del p.titulo
print(p.__dict__)  # {'duracion': 140}
#print(p)  # AttributeError: 'Pelicula' object has no attribute 'titulo' error en la linea 15

# Eliminar el objeto entero
del p
print(p.__dict__)  # NameError: name 'p' is not defined