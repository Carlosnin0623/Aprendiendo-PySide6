from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtGui import QFont, QPixmap  # QFont para fuentes y QPixmap para imágenes
from PySide6.QtCore import Qt  # Para alinear elementos
import sys


class MainWindow(QMainWindow):
  
  def __init__(self):
    super().__init__()
    self.resize(400,320)

    etiqueta = QLabel("Soy una etiqueta")
    fuente = QFont("Open Sans", 24, 400)
    etiqueta.setFont(fuente)
    etiqueta.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

    imagen = QPixmap('./imagenes/Naturaleza.jpg')
    imagen = imagen.scaled(600, 400, Qt.KeepAspectRatio) # Cambiar el tamaño de la imagen
    etiqueta.setPixmap(imagen)
    etiqueta.setScaledContents(True) # Esto es para que la imagen crezca dentro de su contenedor al 100%

    self.setCentralWidget(etiqueta)


if __name__ == '__main__':
  app = QApplication(sys.argv)
  window = MainWindow()
  window.show()
  sys.exit(app.exec())
