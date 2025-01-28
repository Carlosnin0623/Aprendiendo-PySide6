from PySide6.QtWidgets import QApplication, QMainWindow, QComboBox
from PySide6.QtCore import QSize
import sys

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aprendiendo sobre QComboBox")
        self.resize(QSize(600, 400))

        comboBox = QComboBox(self)
        comboBox.move(10, 10)
        comboBox.addItems(["Opción 1", "Opción 2", "Opción 3"])  # Agregar valores

        # Aplicar estilos con setStyleSheet()
        comboBox.setStyleSheet("""
            QComboBox {
                background-color: #1e1e1e;  /* Fondo oscuro */
                color: white;               /* Texto en blanco */
                border: 2px solid #007acc;  /* Borde azul */
                border-radius: 5px;         /* Bordes redondeados */
                padding: 5px;               /* Espaciado interno */
                font-size: 14px;
            }

            QComboBox QAbstractItemView {
                background-color: #2d2d2d;  /* Fondo de la lista */
                selection-background-color: #569cd6; /* Azul al seleccionar */
                selection-color: black;     /* Texto negro al seleccionar */
                border: 1px solid #007acc;
            }

            QComboBox::drop-down {
                border: none;
                width: 30px;
            }

            QComboBox::down-arrow {
                image: url(none);  /* Ocultar el ícono de la flecha */
            }

            QComboBox:hover {
                background-color: #292929;  /* Cambio de color al pasar el mouse */
            }

            QComboBox:focus {
                border: 2px solid #ffcc00;  /* Borde amarillo al hacer clic */
            }
        """)

        # Conectar señales
        comboBox.currentIndexChanged.connect(self.indice_cambiado)
        comboBox.currentTextChanged.connect(self.texto_cambiado)

    def indice_cambiado(self, indice):
        print("Nuevo índice: " + str(indice))

    def texto_cambiado(self, valor):
        print("Nuevo valor: " + valor)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())