from datetime import datetime
from datetime import timedelta


class Producto:

    def __init__(self, nomb, desc, precio, fecha_caduc):

        self.nombre: str = ""
        self.descripcion: str = ""
        self.precio: float = 0.00
        self.fecha_caducidad: datetime = None

        self.mi_nombre = nomb
        self.mi_descripcion = desc
        self.mi_precio = precio
        self.mi_fecha_caducidad = fecha_caduc

    # Tienes que poner el mismo nombre para el getter y para el setter
    @property
    def mi_nombre(self):
        return self.nombre

    @mi_nombre.setter
    def mi_nombre(self, nombre):
        print("Hola")
        self.nombre = nombre

    @mi_nombre.deleter
    def mi_nombre(self):
        print("Hola")
        print("Eliminado nombre", self.nombre)
        del self.nombre

    @property
    def mi_descripcion(self):
        return self.descripcion

    @mi_descripcion.setter
    def mi_descripcion(self, descripcion):
        self.descripcion = descripcion

    @mi_descripcion.deleter
    def mi_descripcion(self):
        del self.descripcion

    @property
    def mi_precio(self):
        print("Hola")
        return self.precio

    @mi_precio.setter
    def mi_precio(self, precio):
        print("Hola")
        """
        100 -> precio
        21  -> X
        """
        if precio > 0.00:
            self.precio = precio + (precio * 21 / 100)  # Precio con IVA

    @mi_precio.deleter
    def mi_precio(self):
        del self.precio

    @property
    def mi_fecha_caducidad(self):
        return self.fecha_caducidad

    @mi_fecha_caducidad.setter
    def mi_fecha_caducidad(self, fecha_caducidad: datetime):
        self.fecha_caducidad = fecha_caducidad

    @mi_fecha_caducidad.deleter
    def mi_fecha_caducidad(self):
        del self.fecha_caducidad


fecha_hoy = datetime.today() + timedelta(weeks=7)
instancia_correcta = Producto("Pera", "Peras traidas desde Andalucia", 0.50, fecha_hoy)
print(instancia_correcta.mi_fecha_caducidad)

instancia_incorrecta_1 = Producto("dsadasd", "fsdfsfds", -1.00, fecha_hoy)
print(instancia_incorrecta_1.mi_precio)
instancia_incorrecta_1.mi_precio = 20.00

del instancia_incorrecta_1.mi_nombre

# https://www.youtube.com/watch?v=jCzT9XFZ5bw
