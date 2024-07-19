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


"""
p1 = Pelicula('Avatar 2', 140, 2023)
print(p1) # Avatar 2, 140, 2023

# Eliminar el objeto entero
print(p1.__dict__) # {'titulo': 'Avatar 2', 'duracion': 140, 'lanzamiento': 2023}
del p1
print(p1.__dict__)  # NameError: name 'p' is not defined
"""

try:
    p1 = Pelicula('Avatar 2', 140, 2023)  # Se ha creadolapelicula Avatar 2
    print(p1)  # Avatar 2, 140, 2023

    # Eliminar el objeto entero
    print(p1.__dict__)  # {'titulo': 'Avatar 2', 'duracion': 140, 'lanzamiento': 2023}
    del p1
    print(p1)  # Se ha borrado la pelicula Avatar 2
except NameError:
    pass

try:
    p2 = Pelicula('Avatar 2', 140, 2023)  # Se ha creadolapelicula Avatar 2
    print(p2)  # Avatar 2, 140, 2023

    # Eliminar un atributo del objeto
    print(p2.__dict__)  # {'titulo': 'Avatar 2', 'duracion': 140, 'lanzamiento': 2023}
    del p2.titulo
    print(p2.__dict__)  # {'duracion': 140}
    # print(p)  # AttributeError: 'Pelicula' object has no attribute 'titulo' error en la linea 15
except NameError:
    pass

try:
    p3 = Pelicula('Avatar 2', 140, 2023)  # Avatar 2, 140, 2023
    print(p3)  # {'titulo': 'Avatar 2', 'duracion': 140, 'lanzamiento': 2023}
    
    print(p3.__dict__)
    delattr(p3, "lanzamiento")
    print(p3.__dict__)   # {'titulo': 'Avatar 2', 'duracion': 140}
    # print(p) # NameError: name 'lanzamiento' is not defined
except NameError:
    pass
