from PySide6.QtWidgets import QApplication, QMainWindow, QCheckBox
from PySide6.QtCore import Qt
import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        
        casilla = QCheckBox("Casilla de verificación", self)
        casilla.stateChanged.connect(self.estadoCambiado)

        # Aplicar estilos al QCheckBox
        casilla.setStyleSheet("""
            QCheckBox {
                font-size: 16px;
                color: white;
                background-color: #2b2b2b;
                padding: 5px;
                border-radius: 5px;
            }

            QCheckBox::indicator {
                width: 18px;
                height: 18px;
                border: 2px solid #007acc;
                border-radius: 5px;
                background-color: white;
            }

            QCheckBox::indicator:hover {
                border: 2px solid #ffcc00;
            }

            QCheckBox::indicator:checked {
                background-color: #007acc;
                border: 2px solid #007acc;
            }
        """)

        self.setCentralWidget(casilla)

    def estadoCambiado(self, estado):
        if estado == Qt.Checked:
            self.setWindowTitle("Se marcó la casilla")
        elif estado == Qt.Unchecked:
            self.setWindowTitle("Se ha desmarcado la casilla")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())