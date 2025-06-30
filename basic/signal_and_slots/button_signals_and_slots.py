from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # === window configuration ===
        self.setWindowTitle('Slots & Signals')
        self.setFixedSize(QSize(400, 300))

        # === Widgets ===
        button = QPushButton('Submit')
        button.setCheckable(True)
        self.button_is_checked = False
        button.setChecked(self.button_is_checked)

        # signal -> mouse click(pressed and released), slot(method) -> button_clicked
        button.clicked.connect(self.button_clicked) 
        # signal -> mouse pressed, slot(method) -> button_pressed
        button.pressed.connect(self.button_pressed)
        # signal -> mouse released, slot(method) -> button_released
        button.released.connect(self.button_released)
        # signal -> mouse click, slot(method) -> button_toggled
        button.clicked.connect(self.button_toggled)
        # signal -> mouse click, slot(method) -> button_toggled_data
        button.clicked.connect(self.button_toggled_data)

        # Set the central widget of the window
        self.setCentralWidget(button)

    # Signals and slots
    def button_clicked(self):
        print('Clicked')

    def button_pressed(self):
        print('Pressed')

    def button_released(self):
        print('Released')

    def button_toggled(self, checked : bool):
        print(f'Checked? {checked}')
        # When a button is made 'checkable' the .clicked signal send data (the state for the button)

    # Using the stored state of the button
    # in this escenario the .clicked signal is not sending the checked state of the button
    # the self.button_is_checked is simulating this state.
    def button_toggled_data(self):
        self.button_is_checked = not self.button_is_checked
        print(f'Checked?r {self.button_is_checked}')

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()