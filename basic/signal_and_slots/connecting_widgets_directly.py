from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QLabel
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Connecting Widgets Together Directly')
        self.setFixedSize(QSize(400, 300))

        # === Widgets ===
        input = QLineEdit()
        label = QLabel()

        # === signals ===
        input.textChanged.connect(label.setText)

        # === layout ===
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(input)
        vertical_layout.addWidget(label)

        # === container ===
        container = QWidget()
        container.setLayout(vertical_layout)

        # Set the central widget of the main window
        self.setCentralWidget(container)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()