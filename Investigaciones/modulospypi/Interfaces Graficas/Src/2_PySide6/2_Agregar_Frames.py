from PySide6.QtWidgets import *
import sys

class mi_primera_ventana(QMainWindow):

    def setupUi(self):
        # Ventana
        self.setFixedSize(1280, 720) # Ancho y Alto
        
        # Frame
        self.frame_1 = QFrame(self)
        self.frame_1.setGeometry(20, 10, 500, 200) # Posicion Eje X, Posicion Eje Y, Ancho, Alto
        self.frame_1.setStyleSheet("background: black;")

        self.frame_2 = QFrame(self)
        self.frame_2.setGeometry(20, 250, 100, 200)
        self.frame_2.setStyleSheet("background: white;")

# Fuente: https://www.youtube.com/watch?v=JjNgUlntdT0

aplicacion = QApplication(sys.argv)

ventana = mi_primera_ventana()
ventana.setupUi()
ventana.show()

sys.exit(aplicacion.exec()) # exec_() esta deprecated, utiliza exec()
