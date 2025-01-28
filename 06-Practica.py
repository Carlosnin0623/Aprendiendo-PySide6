from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel
from PySide6.QtGui import QPalette
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # setup
        self.container = QWidget()
        self.setCentralWidget(self.container)

        self.frameLayout = QVBoxLayout()
        self.container.setLayout(self.frameLayout)

        self.show_sample_btn = QPushButton(text='Sample Window', objectName='sample_button')
        self.another_btn = QPushButton(text='another button', objectName="another_button")
        self.label = QLabel(text="text label", objectName="textLabel")
        self.frameLayout.addWidget(self.show_sample_btn)
        self.frameLayout.addWidget(self.another_btn)
        self.frameLayout.addWidget(self.label)
        self.init_style()
        self.show()

    def init_style(self):
        self.setStyleSheet( """ QWidget {background-color:red; border: 2px solid white;} 
            QPushButton {background-color:blue; border:none;}
            QPushButton::pressed {background-color:black; color:white; border:2px solid yellow;}
            QPushButton#another_button {background-color:green; color:black; border-radius: 13px;}
        """)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    win = MainWindow()
    sys.exit(app.exec())