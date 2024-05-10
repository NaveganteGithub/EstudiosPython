import os

class archivos:

    def modo_lectura(self, fichero: str, codificacion: str):
        with open(fichero, "r", encoding=codificacion) as fichero_abierto:
            return fichero_abierto.read()
        
    def modo_lectura_lineas(self, fichero: str, codificacion: str):
        with open(fichero, "r", encoding=codificacion) as fichero_abierto:
            return fichero_abierto.readlines()
        
class posicionamiento:

    def ubicarme_directorio_actual(file_path: __file__) -> None:
        ruta_absoluta = os.path.abspath(file_path)
        last_delimiter = ruta_absoluta.rfind("\\")
        directorio_actual = ruta_absoluta[:last_delimiter + 1]
        os.chdir(directorio_actual)

    def moverse(ruta: str):
        os.chdir(ruta)

if __name__ == "__main__":
    posicionamiento.ubicarme_directorio_actual(__file__)