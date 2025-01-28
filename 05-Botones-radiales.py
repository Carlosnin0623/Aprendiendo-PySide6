from PySide6.QtWidgets import QApplication, QMainWindow, QRadioButton
from PySide6.QtCore import QSize
import sys

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aprendiendo a Crear botones radiales | Radio Buttons")
        self.resize(QSize(600, 300))

        boton_radial = QRadioButton("Hombre", self)
        boton_radial.toggled.connect(self.verificar_check)  # Detecta si se ha marcado/desmarcado
        boton_radial.setCheckable(True)

        # Aplicar estilos al QRadioButton
        boton_radial.setStyleSheet("""
            QRadioButton {
                font-size: 16px;
                color: white;
                background-color: #2b2b2b;
                padding: 5px;
                border-radius: 5px;
            }

            QRadioButton::indicator {
                width: 18px;
                height: 18px;
                border: 2px solid #007acc;
                border-radius: 10px;
                background-color: white;
            }

            QRadioButton::indicator:hover {
                border: 2px solid #ffcc00;
            }

            QRadioButton::indicator:checked {
                background-color: #007acc;
                border: 2px solid #007acc;
            }
        """)

        self.setCentralWidget(boton_radial)

    def verificar_check(self, valor):
        if valor:
            print("Radial marcado")
        else:
            print("Radial desmarcado")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())