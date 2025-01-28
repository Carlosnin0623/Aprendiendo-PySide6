from PySide6.QtWidgets import QApplication, QMainWindow, QListWidget
from PySide6.QtCore import QSize
import sys

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aprendiendo sobre QListWidget")
        self.resize(QSize(600, 400))

        # Crear lista desplegable
        lista = QListWidget(self)
        lista.move(10, 10)
        lista.resize(200, 200)
        lista.addItems(["Opción 1", "Opción 2", "Opción 3"])  # Agregar valores a la lista

        # Aplicar estilos con setStyleSheet()
        lista.setStyleSheet("""
            QListWidget {
                background-color: #1e1e1e;  /* Fondo oscuro */
                color: white;               /* Texto en blanco */
                border: 2px solid #007acc;  /* Borde azul */
                border-radius: 8px;         /* Bordes redondeados */
                font-size: 14px;
            }
            
            QListWidget::item {
                padding: 8px;              /* Espaciado interno */
            }
            
            QListWidget::item:selected {
                background-color: #569cd6; /* Azul claro cuando se selecciona */
                color: black;              /* Texto en negro cuando está seleccionado */
                border-radius: 5px;
            }
            
            QListWidget::item:hover {
                background-color: #3e3e3e; /* Color cuando pasas el mouse */
                color: #dcdcaa;
            }
        """)

        # Conectar señales
        lista.currentItemChanged.connect(self.item_cambiado)

        self.lista = lista  # Guardamos la referencia para usarla en otro método

    def item_cambiado(self, item):
        if item:  # Verificar que el elemento no sea None
            print(f"Nuevo índice: {self.lista.row(item)}")  # Obtener índice
            print(f"Nuevo valor: {item.text()}")  # Obtener texto del item

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())