from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('QLineEdit Widget')
        self.setFixedSize(QSize(400, 300))

        # === Widgets ===
        self.input = QLineEdit()
        self.input.setPlaceholderText('Type your Input')
        self.input.setInputMask('000.000.000.000;_')

        # === signals ===
        # This signal is also emitted when the text changes programmatically
        self.input.textChanged.connect(self.text_changed)
        # This signal is emitted only when the text is changed by the user
        self.input.textEdited.connect(self.text_edited)
        self.input.returnPressed.connect(self.return_pressed)
        self.input.selectionChanged.connect(self.selection_changed)

        # Set the central widget of the main window
        self.setCentralWidget(self.input)

    # === Slots ===
    def text_changed(self, s : str):
        print(f'Text Changed (programmatic): {s}')

    def text_edited(self, s : str):
        print(f'Text Edited (user): {s}')

    def return_pressed(self):
        print(f'Return Pressed')
        self.input.setText('BOOM BABY!')

    def selection_changed(self):
        print(f'Selection Changed')


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()