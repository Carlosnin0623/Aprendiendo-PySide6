from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtCore import Qt
import sys


class MainWindow(QMainWindow):
  
    def __init__(self):
        super().__init__()
        self.resize(400, 400)
        self.setWindowTitle("Etiqueta y Imagen Estilizada")

        # Crear un contenedor central
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        # Crear etiqueta de texto
        etiqueta = QLabel("Soy una etiqueta")
        etiqueta.setFont(QFont("Open Sans", 18, QFont.Bold))
        etiqueta.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        etiqueta.setStyleSheet("""
            QLabel {
                color: white;
                background-color: #007acc;
                padding: 10px;
                border-radius: 8px;
                font-size: 18px;
            }
        """)

        # Crear etiqueta para la imagen
        imagen_label = QLabel()
        imagen = QPixmap('./imagenes/Naturaleza.jpg')
        imagen = imagen.scaled(250, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation)  # Reducimos la imagen
        imagen_label.setPixmap(imagen)
        imagen_label.setAlignment(Qt.AlignHCenter)
        imagen_label.setStyleSheet("""
            QLabel {
                border: 3px solid #007acc;
                border-radius: 10px;
                padding: 5px;
                background-color: white;
            }
        """)

        # Agregar widgets al layout en orden (texto primero, imagen después)
        layout.addWidget(etiqueta)
        layout.addWidget(imagen_label)

        self.setCentralWidget(central_widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
