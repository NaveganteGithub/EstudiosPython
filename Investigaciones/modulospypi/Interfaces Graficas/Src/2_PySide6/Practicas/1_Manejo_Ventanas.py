from PySide6.QtWidgets import *
import sys

class ejercicio1(QMainWindow):
    
    def setupUi(self):

        self.setFixedSize(500, 330)
        self.setStyleSheet("background: #242526;")

        estilos_estandar_frames = "background: #0CA8AC;"
        """ Si no pasamos el self no aparecen los frames 
        porque no hacemos referencia a la clase de la 
        ventana de PySide
        """
        eje_x = 10
        eje_y = 10
        ancho = 480
        alto = 100
        self.frame_arriba = QFrame(self) 
        self.frame_arriba.setGeometry(eje_x, eje_y, ancho, alto)
        self.frame_arriba.setStyleSheet(estilos_estandar_frames)

        self.frame_abajo = QFrame(self)
        self.frame_abajo.setGeometry(eje_x, alto + eje_y + 10, ancho, alto + 100)
        self.frame_abajo.setStyleSheet(estilos_estandar_frames)


aplicacion = QApplication(sys.argv)

ventana = ejercicio1()
ventana.setupUi()
ventana.show()

sys.exit(aplicacion.exec())
