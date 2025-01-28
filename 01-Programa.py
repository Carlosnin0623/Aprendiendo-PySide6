from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLineEdit 
from PySide6.QtCore import QSize # Para definir el tamaño de los widgets
import sys

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hola mundo") # con este metodo configuramos el titulo para la ventana
        boton = QPushButton("Presiona el boton")
        boton.setCheckable(True) # Si esta opcion esta configurada antes, permite habilitar un segundo parametro que detecta si el botón fue cliqueado y cuando dejo de estar cliqueado
        boton.clicked.connect(self.boton_cliqueado) # clicked: permite realizar una accion cuando se haga click en el boton
       # boton.pressed.connect(self.boton_presionado) # pressed: permite realizar una accion cuando el boton se quede presionado
       # boton.released.connect(self.boton_liberado) # released: permite realizar una accion cuando el boton ha dejado de ser presionado
        self.setCentralWidget(boton)

        self.boton = boton

      #  self.setMinimumSize(QSize(480, 320)) # setMinimumSize estableciendo un tamaño minimo para la ventana
      #  self.setMaximumSize(QSize(800, 600)) # setMaximumSize estableciendo un tamaño maximo para la ventana
      #  self.setFixedSize(QSize(600, 400)) #  setFixedSize Cuando queremos que el tamaño de la ventana no se pueda modificar
        self.resize(800, 600) # resize permite establecer un tamaño base para la ventana

        texto = QLineEdit() # QLineEdit() permite crear un campo de texto
        texto.textChanged.connect(self.texto_modificado)
        self.setCentralWidget(texto)

        self.texto = texto
    
    def boton_cliqueado(self, valor):
        if valor:
           self.boton.setText("Estoy activado")
        else:
            self.boton.setText("Estoy desactivado")
        print("Botón cliqueado" + str(valor))

    def boton_presionado(self):
        print("El click izquierdo ha sido presionado!!!")

    def boton_liberado(self):
        print("El boton ha dejado de ser presionado!!!")

    def texto_modificado(self):
        texto_recuperado = self.texto.text()
        self.setWindowTitle(texto_recuperado)

if __name__ == '__main__':
    app = QApplication(sys.argv) # Con este comando inicializamos la app
    window = MainWindow() # Esto es como la ventana principal en tkinter
    window.show() # Con este comando mostramos la ventana
    sys.exit(app.exec())# con este comando hacemos que la app permanezca abierta 