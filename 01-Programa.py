from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
import sys


app = QApplication(sys.argv) # Con este comando inicializamos la app
window = QMainWindow() # Esto es como la ventana principal en tkinter
window.setWindowTitle("Hola soy el titulo de la ventana") # con este metodo configuramos el titulo para la ventana
boton = QPushButton("Soy un botón")
window.setCentralWidget(boton)
window.show() # Con este comando mostramos la ventana
sys.exit(app.exec()) # con este comando hacemos que la app permanezca abierta 