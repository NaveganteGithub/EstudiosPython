from PySide6.QtWidgets import *
import sys

class mi_primera_ventana(QMainWindow):

    def setupUi(self):
        self.setFixedSize(1280, 720)  # Ancho y Alto

# Fuente: https://www.youtube.com/watch?v=JjNgUlntdT0

"""
Es probable que en entornos virtuales no te salga la ventana la primera vez, 
asi que tienes que ejecutar el script varias veces hasta que te salga
"""

aplicacion = QApplication(sys.argv)

ventana = mi_primera_ventana()
ventana.setupUi()
ventana.show()

sys.exit(aplicacion.exec()) # exec_() esta deprecated, utiliza exec()
