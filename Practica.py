from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPalette, QColor
import sys

class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("hola soy el titulo")
        self.resize(QSize(400, 400))

        # Crear un QLineEdit (campo de texto)
        texto = QLineEdit("", self)
        texto.resize(110, 40)
        texto.move(10, 10)  # Posicionarlo manualmente en (10,10)
        texto.setAlignment(Qt.AlignCenter)  # Centrar el texto dentro del campo

        # Aplicar estilos a QLineEdit
        texto.setStyleSheet("""
            background-color: pink;
            color: white;
            font-size: 14px;
            border-radius: 10px;
            border: 2px solid white;
        """)

        self.show()  # Mostrar la ventana

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Aplicar el estilo Fusion (más moderno y homogéneo)
    app.setStyle('Fusion')

    # Crear una paleta oscura
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))  # Fondo gris oscuro
    palette.setColor(QPalette.WindowText, QColor(255, 255, 255))  # Texto blanco
    palette.setColor(QPalette.Base, QColor(25, 25, 25))  # Fondo de widgets (Ej: QLineEdit)
    palette.setColor(QPalette.Text, QColor(255, 255, 255))  # Color del texto en los widgets
    app.setPalette(palette)  # Aplicar la paleta a la app

    # Crear la ventana
    window = VentanaPrincipal()
    
    sys.exit(app.exec())


