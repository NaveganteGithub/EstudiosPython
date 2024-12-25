class Persona:
    nombre = ''
    edad = ''
    ciudad = ''
    def descripcion(self):
        print(f"Mi nombre es {self.nombre} tengo {self.edad} años y vivo en {self.ciudad}")
        return
        
person = Persona()
person.nombre = "Alfredo"
person.edad = "25"
person.ciudad = "Mallorca"
person.descripcion()
person.nombre = "Daniel"
person.edad = "23"
person.ciudad = "Madrid"
person.descripcion()