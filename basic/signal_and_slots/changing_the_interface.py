from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
from random import choice

window_titles = [
    'Accounts',
    'Hello, Universe!',
    'Formula 1',
    'Surprise',
]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # === Window configuration ====
        self.setWindowTitle('Chaging the Interface')
        self.setFixedSize(QSize(400, 300))

        # === Widgets ===
        # we keep the reference on self because we are going to access the button object in another method
        self.button = QPushButton('Click Me -> Check the Window Title') 

        # === Signals ===
        self.button.clicked.connect(self.btn_change_me)
        self.windowTitleChanged.connect(self.window_title_changed)

        # === Set the central widget of the window ===
        self.setCentralWidget(self.button)

    # ==== slots ===
    # === Button ===
    def btn_change_me(self):
        # self.button.setText('Surprise!')
        # self.button.setDisabled(True)
        # you can also use
        # self.button.setEnabled(False)
        self.setWindowTitle(choice(window_titles))

    # === Main Window ===
    def window_title_changed(self, window_title : str):
        print(f'Window title changed: {window_title}')

        if window_title == 'Surprise':
            self.button.setEnabled(False)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()